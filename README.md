# پروژه API عملیات CRUD اطلاعات کتاب ها
 با استفاده از Django Rest Framework در این پروژه API عملیات خواندن، ایجاد، آپدیت، حذف، علاقه مندی ها و همچین جستجو در داده ها با موضوع اطلاعات کتاب ها پیاده سازی شده است.

## Technologies used
- [Python 3.8](https://www.python.org/) - Programming Language
- [Django](https://docs.djangoproject.com/en/4.0/releases/4.0/) - Web Framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - For Building RESTful APIs
- [SQLite3](https://www.sqlite.org/) - Database
- [Git](https://git-scm.com/doc) - Version Control System

## Setup

Then setup env using the following command
```
python -m venv venv
```
Activate env with the following command
```
venv/Scripts/activate
```
Install requirements
```
pip install -r requirements.txt
```
Create a development database:
```
python manage.py migrate
```
If everything is alright, you should be able to start the Django development server:
```
python manage.py runserver
```
