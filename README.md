# Oxford's Abandoned Bikes
### A place to log any bicycles that appear to have been sadly left by their owner

### Overview
This is a program which I have designed to help me keep track of any abandoned bicycles left around oxford. I have used Python for the backend to practise using Flask for Python and database connections with PostgreSQL.
The database consists of two tables, one for locations (bike racks / fence posts) and one for bikes. Each bike is associated with one and only one location.

### Technology used
- Python
- Flask
- PostgreSQL
- Pytest
- Psycopg

### Running the program
Clone this repo and start the server by doing the following:
```bash
git clone https://github.com/lplclaremont/ox-abandoned-bikes
cd ox-abandoned-bikes/api
# install requred libraries
pipenv install -r requirements.txt

# create the database and test database
createdb abandoned_bikes
createdb abandoned_bikes_test

# run the server
flask run
```

Now you can visit the API endpoints by making requests the the following:
- http://127.0.0.1:5000/ ---> home
- GET http://127.0.0.1:5000/locations ---> a list of all locations
- GET http://127.0.0.1:5000/locations/id ---> a single location by it's ID
- POST http://127.0.0.1:5000/locations ---> add new location to database by passing JSON in the body
- DELETE http://127.0.0.1:5000/locations/id ---> remove a location by it's ID

- GET http://127.0.0.1:5000/bikes ---> a list of all bikes
- GET http://127.0.0.1:5000/bikes/id ---> a single bike by it's ID
- POST http://127.0.0.1:5000/bikes ---> add new bike to database by passing JSON in the body
- DELETE http://127.0.0.1:5000/bikes/id ---> remove a bike by it's ID


### Testing the program
Inside the ox-abandoned-bikes/api directory, run the following:

```bash
pipenv run pytest
```