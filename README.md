# PyNote
Journal, Idea Tracker and Other things. This application is based and built off [Flask-AppBuilder](https://github.com/dpgaspar/Flask-AppBuilder) by [dpgaspar](https://github.com/dpgaspar)

Running demo hosted at pynote.devsetgo.com
* username Admin
* password $Password

-------------------------------------------------------------
## Run the application from OS
Prerequisits
* Python (3.5)
* virtualenv

Run the application
* create a virtual environment - virtualenv env
* Install Requirements in Virtual Environment - pip install -r requirements.txt
* fabmanger create-admin
    - Follow instructions
* fabmanger Run
    - Application is now running
    - Test and modify code as you want

----------------------------------------------------------
## Run the Application with Docker
----------------------------------------------------------
### Demo version
* Docker Pull mikeryan56/pynote_demo:latest
* demo db
    - username: admin
    - password: $Password

* or clone and run (gunicorn -c gunicorn_cfg.py app:app)
----------------------------------------------------------
### Regular version
: To be built later
