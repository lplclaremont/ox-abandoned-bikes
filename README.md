# Oxford's Abandoned Bikes
### A place to log any bicycles that appear to have been sadly left by their owner

### Overview
This is a program which I have designed to help me keep track of any abandoned bicycles left around oxford. I have used Python for the backend to practise using Flask and database connections with PostgreSQL.
The database consists of two tables, one for locations (bike racks / fence posts) and one for bikes. Each bike is associated with one and only one location.

### Technology used
- Python
- Flask
- PostgreSQL
- Pytest
- Psycopg

### Approach
The idea began through the desire to create a RESTful API using Python. This allowed me to find solutions to a few requirements:
- **Creating endpoints:**
I have decided to use Flask to create the API application as it provides neat and clear routing to direct HTTP requests to parts of my code.
- **Model class:**
I've manually implemented a Model class for both the Locations and Bikes objects. These are what the python program will create when getting data from the database.
- **Repository class:**
This class handles the actual behaviour of the API and uses instances of the model classes and does something with them (displays information, makes new entries in DB etc.)
- **Connection to PostgreSQL database:**
This is done through the psycopg Python library. I've decided to not use a MVC framework, to aid my understanding, and manually implement the connection to the database by sending the SQL queries in my code with certain parameters. This can be seen in the repository class, which utilises the DatabaseConnection class in order to act as an abstraction of the code which connects us to the PostgreSQL database.

### Running the program
Clone this repo and start the backend server:
```bash
git clone https://github.com/lplclaremont/ox-abandoned-bikes
cd ox-abandoned-bikes/api
# install requred libraries
pipenv install -r requirements.txt

# create the database and test database
brew install postgresql
createdb abandoned_bikes
createdb abandoned_bikes_test

# run the api server
flask run
```
In a new terminal start the frontend server:

```bash
cd ox-abandoned-bikes/frontend

# install depedencies
npm install

# run the frontend server
npm run dev
```

Now you can open a browser and visit the site locally at http://localhost:5173/

### Testing the program
Inside the ox-abandoned-bikes/api directory, run the following:

```bash
pipenv run pytest
```