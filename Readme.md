# Attendance System Using Face Recognition 

This project can provide attendance by recognizing
faces. It is included with a fraud detection system. Technologies used: Python (Libraries: Open CV, NumPy,
face_recognition etc..)

## Deployment

### Step 1 

- Install anaconda and create a new python-3.7.10 environment
- now install the below packages 

```bash
 conda install -c anaconda pillow
```
```bash
conda install -c conda-forge opencv=3.4.2
```

```bash
conda install -c conda-forge imutils
```
- Note for installing tensorflow, mysql use pip it is recomended.
```bash
pip install tensorflow==2.1.0
```
```bash
pip install mysql-connector-python
```
```bash
conda install -c conda-forge face_recognition=1.3.0
```
### Note:- make sure h5py package version is 2.10.0 because it is compatible with our tensorflow version 2.1.0

Above are the necessary python packages required to run this project

### Step 2

- Download mysql server, workbench, shell.
- create a Schema and a tabel inside it.
- Below is the schema of the table I followed.
![img.png](img.png)
- Database name facerec.
- Table name studetails.
- Change the paths in the python files as per your convenience 

