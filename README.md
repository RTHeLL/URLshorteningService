# Link shortening service

Extracted project: https://url-shortening-service-kinder.herokuapp.com/

## Requirements
- PostgreSQL 12.9
- Python 3.8.10
- Pipenv 2022.1.8

## Install and start
Clone `https://github.com/RTHeLL/URLshorteningService.git`

###### Install ######
1. Go to `URLSS` folder
2. Use command `pipenv install` or `pip install -r requirements.txt`


###### Configure PostgreSQL ######
1. Go to `URLSS/URLSS` folder
2. Open `settings.py` file
3. Find `DATABASES` dictionary
4. Specify the database in the `NAME` field
5. Specify the user in the `USER` field
6. Specify the password in the `PASSWORD` field
7. Specify the host in the `HOST` field
8. Specify the port in the `PORT` field
9. Save and exit

###### Make migrations ######
1. Go to `URLSS` folder
2. Use command `./mange.py migrate` or `python manage.py migrate`

###### Run ######
1. Go to `URLS` folder
2. Use command `./mange.py runserver` or `python manage.py runserver`
