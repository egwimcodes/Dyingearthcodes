# Dyingearth Soil Sensor Python Project

![Dyingearth Soil Sensor Python Project](https://raw.githubusercontent.com/egwimcodes/Dyingearthcodes/master/static/assets/images/p_imgs/l1.png)

![Dyingearth Soil Sensor Python Project](https://raw.githubusercontent.com/egwimcodes/Dyingearthcodes/master/static/assets/images/p_imgs/l2.png)

![Dyingearth Soil Sensor Python Project](https://raw.githubusercontent.com/egwimcodes/Dyingearthcodes/master/static/assets/images/p_imgs/l3.png)

![Dyingearth Soil Sensor Python Project](https://raw.githubusercontent.com/egwimcodes/Dyingearthcodes/master/static/assets/images/p_imgs/l4.png)

![Dyingearth Soil Sensor Python Project](https://raw.githubusercontent.com/egwimcodes/Dyingearthcodes/master/static/assets/images/p_imgs/l5.png)


## Analytics Page

![Dyingearth Soil Sensor Python Project](https://raw.githubusercontent.com/egwimcodes/Dyingearthcodes/master/static/assets/images/p_imgs/m1.png)

## Api

![Dyingearth Soil Sensor Python Project](https://raw.githubusercontent.com/egwimcodes/Dyingearthcodes/master/static/assets/images/p_imgs/ai.png)

## Project Overview

The **Dyingearth** Soil Sensor Project stands as a testament to my dedication to merging technology with practical solutions. In this Python-based initiative, I endeavored to create a sophisticated system capable of tracking crucial soil parameters: humidity, temperature, and moisture content. This project was born out of a recognition of the pivotal role these factors play in agriculture and environmental monitoring.. [dyingearth.com]([https://dyingearthcodes.onrender.com](https://dyingearthcodes.onrender.com)).


## Preview 


## Live demo

Check the live demo here 👉️ ([https://dyingearthcodes.onrender.com](https://dyingearthcodes.onrender.com))

## Getting Started

### Configure Database Details:

First, navigate to the .env file and replace the placeholder values with your specific database details. Optionally, you can update the email settings if necessary.
First, creat

### Verify Database Connection:

To ensure your database connection is established correctly, run the following command:

```bash

python manage.py dbshell

```

### Activate the Virtual Environment:

Activate the virtual environment using the following command:

```bash

env/Scripts/activate

```

### Install Dependencies:

Install project dependencies by running:

```bash

pip install -r requirements.txt

```

### Make Migrations and Migrate:

Make and apply migrations to set up the database schema:

```bash

python manage.py makemigrations
python manage.py migrate

```

### Create a Superuser:

Create a superuser (admin user) for the application by running:

```bash

python manage.py createsuperuser

```
Follow the prompts to enter your credentials.

### Start the Server:

Start the development server with the following command:

```bash

python manage.py runserver

```


## Setup for Tasks


### Start Celery Worker:

Start the Celery worker to handle asynchronous tasks:

```bash

celery -A dyingearthcode worker --pool=solo -l INFO

```
## Start Celery Beat Server:

Start the Celery beat server for periodic tasks (Note: Ensure Celery beat is installed and running):

```bash

celery -A dyingearthcode beat -l INFO

```

With these steps, you should have the Dyingearth Soil Sensor Project up and running, ready to collect and analyze soil data. Feel free to explore the project, and don't hesitate to reach out for any assistance or feedback


Open [http://localhost:9000](http://localhost:9000) with your browser to see the result.

## About Me
@Egwimcodes ([https://egwimcodes.dev](https://egwimcodes.dev))
Wisdom Egwim is a highly skilled, ambitious Software Developer with a robust background in Python, Django, FastApi, Flutter, Dart, Javascript, ReactJS, NextJS, Css, Tailwindcss, and Bootstrap. My expertise extends beyond conventional boundaries, encompassing a profound understanding of ML and Robotics.
