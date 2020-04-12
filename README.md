Home-Inventory App

Our group decided to develop an unconventional data application. Cesar Tolentino had the unique idea of making an application that keeps records of groceries that people buy online and stores an inventory of what the user has at home based on prior purchases. 

We got the data for the application from Instacart in the form of enormous CSV files. We eventually decided we didn't need all of the over two million items purchased that are listed in a table linking orders and products. 

Two massive tables that were originally for training and testing were concatenated. We put the data into a mysql database running on a virtual private server at Bluehost.  MySQL Workbench was employed to structure the tables and their relationships based on the CSVs. 

We deployed the application on Heroku instead of on the virtual private server because it makes deploying such applications simple. At the same time, it would not involve changing the setup of a server.

The landing page is a login page for the app. The user either logs in or signs up as a new user with an email address and password. The app sends and stores the password with hash encryption. 

Upon successful login, the user is directed toward a dynamic dashboard with price totals for each order date. 

A plot of the cost totals has a date range selected using javascript.
The style of the pages in the dashboard app is made from dashboard templates using bootstrap.

We also got data from several relative jsonified routes. 

Other parts of the application include letting users place items in the trash or consume them. The user can also classify an item as wasted goes bad or is thrown out before consumption or use.

Another gets data about orders. 

This is an early prototype for a real-world application. If given more time, we would make further refinements in the controls, the plots, and the interactivity.

We also got data from the Edamam Nutritional Analysis API. We used the api to search for data about the purchased products.

Login to the app at https://pan-tree.herokuapp.com/login  with the username veggie_cheez and the password 12341234.


Bibliography

“The Instacart Online Grocery Shopping Dataset 2017”, Accessed from https://www.instacart.com/datasets/grocery-shopping-2017 on, Feb. 15, 2020.

Edamam Nutrional Analysis API, accessed from https://developer.edamam.com/edamam-nutrition-api on April 1, 2020.

