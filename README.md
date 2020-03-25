# CT_Medical_Images

## Dataset 
[CT Medical Images](https://www.kaggle.com/kmader/siim-medical-images) from kaggle.<br>
This dataset contain **CT images from cancer imaging archive with contrast and patient age**

## Visualization
For visualization of CT images, it was mostly borrowed from a [kaggle kernel](https://www.kaggle.com/gpreda/visualize-ct-dicom-data).

### Data format for medical images: DICOM , TIFF 
The images data are provided both in **DICOM** and **TIFF** formats.<br>
The images data files are named with a naming convention allowing us to identify some meta-data about the images.

### What is DICOM?
**DICOM** stands for **Digital Imaging and Communications in Medicine** <br>
:The standard for the communication and management of medical imaging information.<br>
- Archiving and transmitting medical images.<br>
- integration of medical imaging devices (radiological scanners), servers , network hardware ,and **Picture Archiving and Communication Systems (PACS)**.


### Dependency:
  `pip3 install --user pydicom`
  `pip3 install --user dicom_numpy`


# references
- https://en.wikipedia.org/wiki/DICOM
