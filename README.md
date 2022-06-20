# Neighborhood
My NeighbourHood 

# Description
This a neighbourhood app where a user sign up and join a hood or create a hood of their own. See the businesses in the hood, or add a business or see important posts in the hood they belong to.

## Live site
(https://myhood2.herokuapp.com/)

## User Stories
- Sign in with the application to start using.
- Set up a profile about them and a general location and their neighborhood name.
- Find a list of different businesses in their neighborhood.
- Find Contact Information for the health department and Police authorities near their neighborhood.
- Create Posts that will be visible to everyone in their neighborhood
- Change their neighborhood when they decide to move out.
- Only view details of a single neighborhood they are enrolle in.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Select between signup or login|
| Select SignUp| **Email**,**Username**,**Password** | Go to login|
| Select profile|**Profile name**|Change or update your profile|
| Select Home | **On home page** | Get all the neighbourhoods available, add new neighbourhood button, leave or join neighbourhood|
| Select join hood| **Go to home page or profile** | See name of your hood |
| Select Home| **Explore Hood** |Click the explore button and view details of your neighbourhood.|
| Select add business | **Add business** | Add a new business|
| select post | **post**| Add a new post |
|Select search| **search business**|search for businesses in the neighbourhood|

## Technologies used
* Django Framework - used to create the application. 
* Heroku - used to deploy the application. 

## Set up and installation
#### Clone the Repo
####  Activate virtual environment
Activate virtual environment using python as default handler
    `virtualenv -p /usr/bin/python venv && source venv/bin/activate`
For windows users use this to activa your environment
   ` source venv/Scripts/active`    
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE <DBNAME>;
####  .env file
Create .env file and add the following filling where appropriate:
    SECRET_KEY = '<Secret_key>'
    DBNAME = '<DBNAME>'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.6 manage.py makemigrations gallery
    python3.6 manage.py migrate
#### Run the app
    python3.6 manage.py runserver
    Open terminal on localhost:8000

## Known Bugs
NO know bugs so far.

## Contact Information
If you have any questions feel free to contact me.

## License
* MIT LICENSE
* Copyright (c) 2022 Joyce Njoroge





