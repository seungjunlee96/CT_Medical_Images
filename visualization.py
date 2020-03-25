# references
# 1.https://www.kaggle.com/gpreda/visualize-ct-dicom-data/notebook

#Load Packages
import numpy as np
import pandas as pd
from skimage.io import imread
import seaborn as sns
import matplotlib.pyplot as plt
from glob import glob
import pydicom as dicom
import os



def my_args():
    import argparse
    parser = argparse.ArgumentParser(description = "Visualization for CT Medical Images")
    parser.add_argument("--data_dir", type = str, default = os.path.join(os.getcwd(),'data'))
    return parser.parse_args()

def read_data(csv):
    data_df = pd.read_csv(csv)
    print("CT Medical images - (rows,cols) = ({},{})"
          .format(data_df.shape[0],data_df.shape[1]))
    print(data_df.head())
    return data_df

def preprocess_data(imgs):
    # Load packages
    import pandas as pd
    from glob import glob
    import os

    data = pd.DataFrame([{'path': filepath} for filepath in imgs])
    data['file'] = data['path'].map(os.path.basename) # get only file name
    data['ID'] = data['file'].map(lambda x : str(x.split('_')[1]))
    data['Age'] = data['file'].map(lambda x : int(x.split('_')[3]))
    data['Contrast'] = data['file'].map(lambda x : bool(int(x.split('_')[5])))
    data['Modality'] = data['file'].map(lambda x : str(x.split('_')[6].split('.')[-2]))
    return data

def show_images(data, dim = 16, img_type = 'TIFF'):
    import matplotlib.pyplot as plt
    img_data = list(data[:dim].T.to_dict().values())
    f, ax = plt.subplots(nrows=4,
                         ncols=4,
                         figsize = (20,20))

    for i , data_row in  enumerate(img_data):
        if img_type == 'TIFF':
            data_row_img = imread(data_row['path'])
            ax[i//4, i%4].matshow(data_row_img,cmap = 'gray')
        elif img_type == 'DICOM':
            data_row_img = dicom.read_file(data_row['path'])
            ax[i//4, i%4].imshow(data_row_img.pixel_array,cmap=plt.cm.bone)

        ax[i//4, i%4].axis('off')
        ax[i//4, i%4].set_title('Modality: {Modality} Age: {Age} \nSlice : {ID} Contrast: {Contrast}'
                                .format(**data_row))

    return plt.show()


def countplot_comparison(feature, data_df , tiff_data , dicom_data):
    import seaborn as sns
    import matplotlib.pyplot as plt
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1,
                                        ncols=3,
                                        figsize = (16,4))

    s1 = sns.countplot(data_df[feature], ax = ax1)
    s1.set_title("Overview data")

    s2 = sns.countplot(tiff_data[feature], ax = ax2)
    s2.set_title("Tiff files data")

    s3 = sns.countplot(dicom_data[feature], ax = ax3)
    s3.set_title("Dicom files data")

    return plt.show()


#extract voxel data
def extract_voxel_data(dcm_lst):
    # https: // dicom - numpy.readthedocs.io / en / latest /
    import dicom
    import dicom_numpy
    datasets = [dicom.read_dile(fName) for fName in dcm_lst]
    try:
        voxel_ndarray, ijk_to_xyz = dicom_numpy.combine_slices(slice_datasets=datasets)
    except dicom_numpy.DicomImportException as e:
        raise
    return voxel_ndarray

def main():
    args = my_args()
    data_dir = args.data_dir
    # print(os.listdir(data_dir))

    csv = os.path.join(data_dir,'overview.csv')
    data_df = read_data(csv)

    dicom_dir = os.path.join(data_dir, 'dicom_dir')
    dicom_files = glob(os.path.join(dicom_dir,'*.dcm'))
    #print("the number of DICOM files = {}".format(len(dicom_files)))
    dicom_data = preprocess_data(dicom_files)
    print(dicom_data.head(10))

    tiff_dir = os.path.join(data_dir, 'tiff_images')
    tiff_images = glob(os.path.join(tiff_dir,'*.tif'))
    tiff_data = preprocess_data(tiff_images)
    #print(tiff_data.head(10))

    #countplot_comparison('Contrast',data_df,tiff_data,dicom_data)
    #countplot_comparison('Age',data_df,tiff_data,dicom_data)

    # show_images(tiff_data,dim = 16 , img_type='TIFF')
    show_images(dicom_data,dim=16 , img_type='DICOM')


    dicom_file_path = list(dicom_data[:1].T.to_dict().values())[0]['path']
    dicom_file_dataset = dicom.read_file(dicom_file_path)
    print(dicom_file_dataset)


if __name__ == "__main__":
    main()