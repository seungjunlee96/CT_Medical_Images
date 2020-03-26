# CT_Medical_Images
This repo illustrates some examples that show how to deal with medical images.
<br>
# Dataset 
[CT Medical Images](https://www.kaggle.com/kmader/siim-medical-images) from kaggle.<br>
This dataset contain **CT images from cancer imaging archive with contrast and patient age**
<br>
# Example
Example Visualization of CT images <br>
please refer to `visualization.py`
1. Example of DICOM file visualization 
![dicom_sample](/dicom_sample.png)<br>
2. Example of TIFF file visualization <br>
![tiff_sample](/tiff_sample.png)<br>
# Explanation on Standard Data formats for medical images: DICOM , TIFF 
The images data are provided both in **DICOM** and **TIFF** formats.<br>
The images data files are named with a naming convention allowing us to identify some meta-data about the images.

### What is DICOM?
**DICOM** stands for **Digital Imaging and Communications in Medicine** <br>
:The standard for the communication and management of medical imaging information.<br>
- Archiving and transmitting medical images.<br>
- integration of medical imaging devices (radiological scanners), servers , network hardware ,and **Picture Archiving and Communication Systems (PACS)**.


### Dependency:
  ```
  pip3 install --user pydicom
  pip3 install --user dicom_numpy
  ```

# references
- https://en.wikipedia.org/wiki/DICOM
- https://www.kaggle.com/gpreda/visualize-ct-dicom-data
