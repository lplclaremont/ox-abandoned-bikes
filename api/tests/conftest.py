import pytest
from lib.database_connection import DatabaseConnection
from app import app

# This is a Pytest fixture.
# It creates an object that we can use in our tests.
# We will use it to create a database connection.

# This one makes a DatabaseConnection instance and connects it to the test database
@pytest.fixture
def db_connection():
    conn = DatabaseConnection()
    conn.connect('abandoned_bikes_test')
    conn.seed("seeds/abandoned_bikes.sql")
    return conn

# We'll also create a fixture for the client we'll use to make test requests.
@pytest.fixture
def web_client():
    app.config['TESTING'] = True # This gets us better errors
    with app.test_client() as client:
        yield client

# Now, when we create a test, if we allow it to accept a parameter called `db_connection`,
# Pytest will automatically pass in the object we created above.

# For example:

# def test_something(db_connection):
#     # db_connection is now available to us in this test.