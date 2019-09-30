# Too Much Java

![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)
![forthebadge](https://forthebadge.com/images/badges/made-with-vue.svg)
![forthebadge](https://forthebadge.com/images/badges/makes-people-smile.svg)

## Overview

Too-Much-Java is an online platform designed for automatic code grading.

In short, it allows instructors to create assignments, categorized by units and courses, and provide instructions as well as starter files. The student, on the other hand, can submit code files receive instanteous feedback from TMJ.

The frontend is written in Vue.js and the backend in Django. Currently, TMJ only natively supports Java. However, feel free to edit the Django grading method to enable support for more langauges.

## Features

- Automatic code grading with instanenous feedback
- Classification of courses & units
- Junit support
- Markdown instructions
- Starter / template files
- Django admin panel (/admin)
- Alterantive assignment creation based on text file (/dropoff)
- Course codes to prevent registration spams and automatically enroll students to their courses

## Usage

### Configuration

Firstly, clone and configure TMJ.

Inside [frontend/src/settings.js](https://github.com/gundamMC/too-much-java/blob/master/frontend/src/settings.js), you can change the appearance of your site.

```javascript
module.exports = {
    host: 'Potato High School',
    domain: 'https://potatohigh.com',
    download_domain: 'https://dl.potatohigh.com'
}
```

Next, we can change the settings of the backend. If you are running a development server, then you don't need to change anything, as Djangow will be using a SQLite database. If you are deploying for production, open [too_much_Java/settings/prod.py](https://github.com/gundamMC/too-much-java/blob/master/too_much_java/settings/prod.py) and change the allowed hosts and database information.

```python
ALLOWED_HOSTS = [
    'example.com',
    'www.example.com'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tmj',
        'USER': os.environ['TMJ_DB_USER'],
        'PASSWORD': os.environ['TMJ_DB_PASS'],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

As for the secret key, database username, and databsae password, add those to your environment variable (TMJ_SECRET_KEY, TMJ_DB_USER, TMJ_DB_PASS) to keep them secured.

### Building the frontend

Build the frontend with npm:

```
npm install
npm run build
```

Since Django is configured to search for the frontend, you don't need to do anything with the files.

### Run Django

When running Django, always use the `--settings=too_much_java.settings.[dev/prod]` arugment so Django knows which file to use.

Firstly, make migrations and then migrate to initiate the database. Next, run collectstatic to gather the frontend files. Lastely, run createsuperuser to create a super user (you'll need this). Now, you can serve TMJ with django's test server or use soething else like gunicorn.

### TMJ Set Up

#### Users

TMJ uses its own student object for authorization. Thus, if a upser user wants to view the main site, a student object must be created through the admin panel (/admin) to allow for login. 

#### Registeration

Registering requiers a course code. It not only serves as a "password" to secure the site, it also automatically enrolls the student to a specific course (defined in admin panel). Super users can create multiple course codes.

#### Grader Setup

TMJ uses Junit 5 for grading.

To use the built-in Java grader, place download the jars for `junit-platform-console-standalone` (Junit 5) and `json` and place them inside `grader_resources`.

Each unit test will count as a point in the grader, and you can use Junit's `assertEquals` to add specific messages regarding the test results.
