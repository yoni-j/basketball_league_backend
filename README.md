## Setup for running

1. Python virtual environment:   
Using poetry to manage the projects dependencies.   
   **Install Poetry** - https://python-poetry.org/docs/#installation
        

2. Get the code:    
Clone this project    


3. Install dependencies:    
enter projects directory and install dependencies using Poetry. Poetry will look for pyproject.toml file
    ```
    cd league_backend
    poetry install
    ```
 
---
### From this point in the setup you should run the commands with "poetry run" at the start

---

4. Database:    
Using postgres. You need to set up a user,
   * After you have installed postgres, enter postgres cli client:    
   ```
   sudo su - postgres
   psql
   ```
   * create a database, a user and a role
    ```
    CREATE DATABASE league_backend_db;
    CREATE USER league_backend_user WITH PASSWORD 'league_backend_pass';
    ALTER ROLE league_backend_user SET client_encoding TO 'utf8';
    GRANT ALL PRIVILEGES ON DATABASE league_backend_db TO league_backend_user;       
   ```
   * to exit postgres cli:   
   `Ctrl+D`
   
     and then exit superuser shell   
   `exit`
    * Now you can migrate the data:
   ```   
   poetry run python manage.py migrate   
   ```   

5. Create a superuser for yourself to start working
    ```
    poetry run python manage.py createsuperuser 
   ```
   
6. Run management command to setup data
    ```
    poetry run python manage.py base_setup 
   ```

8. Run the server
    ```
   poetry run python manage.py runserver
   ```
 
### tests

```bash
poetry run python manage.py test
```


