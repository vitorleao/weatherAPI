## Purpose / Description
Provides a API that return the weather forecast to the 5 next days and store into the database these requests.

## Requirements
- [Python 3](https://www.python.org/)
- [Docker](https://docs.docker.com/)

## Getting Started
### Cloning repository
- Run the command `git clone https://github.com/vitorleao/weatherAPI.git` and open the folder with `cd weatherAPI`

### Creating virtual enviroment
- Tip `python -m venv venv` to create.
- Activate the env on Linux with `source venv/bin/` or Windows `source venv/Scripts/activate`.

### Running the API
- Execute `docker-compose up --build -d`

## Accessing database and finding data
- In the terminal, open the container: `docker exec -it mongodb /bin/bash`.
- Enter in mongo database: `mongosh -u root -p password`.
- Access database: `use test_database`.
- Consult the data: `db.external_data.find().pretty()`

## Running the tests
Before running the tests, request the 'city' method at least once to ensure the existence of a record in the database.
- Access API container: `docker exec -it weatherapi-app /bin/bash`
- Run the unit tests: `pytest tests/test_main.py`

## Importing Collections
- If you prefer a tool to consome the API like Insomnia, Postman, SoapUI, etc. It is possible get samples through of collections presents into `/docs` directory.

## API Documentation
Check the API documentation on http://localhost:8000/docs

## Next steps
- Improve db user roles
- Improve data insertion on db
- Improve application logs
- Add more tests cenaries
- Import more collections tools files
- ...

## Contributors
- [Vitor Leão](https://github.com/vitorleao)
