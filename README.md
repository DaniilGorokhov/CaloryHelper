# CaloryHelper

This is service for establishing amount of calory in product.
For start local version, you need:

*Start virtual environment
Windows:
```bash
python -m venv venv
```
MacOS:
```bash
python3 -m venv venv
```

```
call venv/Scripts/activate
```

*Install needed libraries
```bash
pip install -r requirements.txt
```

*Start project
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

*Go to your browser for test application by adrress http://localhost:8000
