# Getting Started with Django

This project was bootstrapped with [Django](https://www.djangoproject.com/).

## Production Server
- Backend Server: https://vara-new-api.eba-8td7muy2.us-west-2.elasticbeanstalk.com/
- Frontend Server: https://main.d271r6z8tdry4i.amplifyapp.com/

## Repository Links
- Backend Server: https://github.com/shreyas2499/vara-api
- Frontend Server: https://github.com/shreyas2499/vara-ui

### `Note` 
  Since, I was not able to buy a domain name for this assessment, the browser throws a SSL certificate issue. I have added a manually signed certificate, but browsers do not completely accept it. So in order to get the production application running, please follow the steps below:
  1) Go to the Backend Server link. You should be able to see a page like below: ![Screenshot 2024-04-29 at 00 13 15](https://github.com/shreyas2499/vara-ui/assets/59840906/8f678190-91e5-4ce4-89b2-2accd2340770)
  2) Please click on the `Advanced` button to proceed. Once you click on that, you should be able to see this screen: ![Screenshot 2024-04-29 at 00 13 22](https://github.com/shreyas2499/vara-ui/assets/59840906/6e97700a-2e61-485c-a12b-b0f7ef49fc95)
  3) Click on `Proceed to vara-new-api.eba-8td7muy2.us-west-2.elasticbeanstalk.com (unsafe)` option. Once you have done this, you are all set to use the application!

## Tech Stack
1) Backend: Django
2) Database: Sqlite3
3) Frontend: React
4) Backend Deployment Server: AWS ElasticBeanstalk
5) Frontend Deployment Server: AWS Amplify

## Key Features
- Product Deployed on AWS
  1) Frontend Deployed using AWS Amplify
  2) Backend Deployed using AWS ElasticBeanstalk
     
- REST based APIs

- Database stores all the relevant information. Has the following tables
  1) MonthlyConsumption: Stores the data from the excel provided (https://docs.google.com/spreadsheets/d/1xYtvMLc8LhBFOgovS8RLCQa2yso7C0ViuyFgXZdt6Z4/edit#gid=1381247138)
  2) User: Stores user information such as email, hashedPassword and a preferences json.

- Demo account
  A demo account is created with the credentials for the purpose of testing. Please find the credentials here:
  - email: admin@gmail.com
  - password: admin

# Local Setup
- `Git clone` the repository
- Move into the project's root folder by using `cd`
- This step is not required, but recommened. Create a virtual environment using `python -m venv env`
- Run `python manage.py makemigrations`
- Run `python mange.py migrate`
- Run `python manage.py runserver` to start the server locally
- You should be able to the see the local url in the terminal. Click on the link in your terminal to get started!
