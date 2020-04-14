# Pan-Tree

We created an early prototyp application that keeps records of groceries that people bought online and stores an inventory of what the user has at home based on prior purchases. The application uses a MySQL database hosted on Bluehost.com and the applicatin is deployed on heroku.com at
www.pan-tree.herokuapp.com. Additional database work was done using MySQL Workbench. 


## Getting Started

The project requires MySQL server and MySQL workbench. You can use MySQL Workbench to produce the same database on your machine. You will also need to create at least one administrative user with a password for setting up the database. An additional user with fewer rights will also need to be created to act as a general web user with only insert, update, and delete permissions. These usernames and passwords can be placed on the app_config.py

You will need to run the sql dump file in the dump folder to inster the data into the tables with the required structure. 

The database is too large for Heroku, so it needs to run somewhere else and the app_config.py will have to be updated accordingly. 

### Prerequisites

If you run locally you will need to create a Pipenv. You will also need to install a local copy of Gunicorn on the system level. 

You will need to have python 3.7 as the default (even on Macs). You will 
The project requires the latest version of pip which may require you to use homebrew to get and install. Pipenv is required to make virtual environments. 


### Installing
Both pip, pipenv, and gunicorn need to be installed on the system level for pipenv and gunicorn to work in the project directory.

## Running the tests

You should test that you can connect to MySQL Server with the connection in app_config.py. You should use sql queries to ensure that data was written to the tables. 

To test the full application you should go to the directory of you project and from the command line run pipenv install. Then go into pipenv shell. Finally run app.py. Hopefully this will start the application running on Gunicorn on the local address. 

For the test, the username is "veggie_cheez" and the password is "12341234". 



## Deployment

In order to deploy the app on heroku. Need to have a Proc file (already) provided and you need to deploy a Heroku project. The database itself is too large for heroku. So full deployment will require an external database. 

Login to the app at https://pan-tree.herokuapp.com/login with the username veggie_cheez and the password 12341234.

## Built With

* VSCode  
* Pipenv - Dependency Management
* “The Instacart Online Grocery Shopping Dataset 2017”, Accessed from https://www.instacart.com/datasets/grocery-shopping-2017 on , 2020.
* Edamam Nutrional Analysis API, accessed from https://developer.edamam.com/edamam-nutrition-api on April 1, 2020.

## Contributing

Scott McMahan
Cesar Tolentino
Memet Bulut
Derrick Butler


## Authors

* **Cesar Tolentino** - had the idea for the project

See also the list of [contributors](https://github.com/scottcm73/Pan-Tree) who participated in this project.


## Bibliography

Edamam Nutrional Analysis API, accessed from https://developer.edamam.com/edamam-nutrition-api on April 1, 2020.


“The Instacart Online Grocery Shopping Dataset 2017”, Accessed from https://www.instacart.com/datasets/grocery-shopping-2017 on, Feb. 15, 2020.

"Range Slider and Selector in Javascript" Accessed from https://plotly.com/javascript/range-slider/ on March 15, 2020.



