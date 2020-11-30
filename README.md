# CaloryHelper

## Description

This is service for establishing amount of calory in product.

## Starting project

For starting local version, you need:

* Start virtual environment
Windows:
```bash
python -m venv venv
```
MacOS:
```bash
python3 -m venv venv
```

* Activate virtual environment
```
call venv/Scripts/activate
```

* Install needed libraries
```bash
pip install -r requirements.txt
```

* Start project
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

* Go to your browser for test application by adrress http://localhost:8000

## Using

You should sign up in our service, than you can get inforamtion about calory amount in your nutrition by uploading photo and clarifying product name. Further in your history you can see your history in time


There are test images in directory testImages for fast testing


Who work on this project:
* Frontend - https://github.com/Grekov-Igor
* Backend - https://github.com/SeamMiner
* AI and Parsing - https://github.com/DaniilGorokhov
