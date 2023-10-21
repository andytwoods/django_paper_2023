
# Django Paper 2023, demo project 

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

A demo project for this paper <insert reference when known>


## Run Locally

Clone the project

```bash
  git clone https://github.com/andytwoods/django_paper_2023
```

Go to the project directory

```bash
  cd django_paper_2023
```

Create a virtual environment, e.g. via

```bash
  python3 -m venv venv
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run local server

```bash
  python3 manage.py runserver
```
## Lessons

Visit http://127.0.0.1:8000/study/1/ to get the expected error message ("study 1 does not exist")

Make yourself a superuser by following steps asked for in this command

```bash
  python3 manage.py createsuperuser
```

Visit the admin page

```bash
http://127.0.0.1:8000/admin/
```

Here, create a study. 

Revisit http://127.0.0.1:8000/study/1/. You shoud see the study you created in admin.
## Acknowledgements

 - Readme  written rapidly via [https://readme.so/](https://readme.so/)