# Cargill App to manage team data

## Technology stack
### Backend API:
- Python v3.9 with flask
- SQLalchemy

### Database
- Postgres

### Front end
- ReactJS with material UI
- Axios

### Deployment tools
- Docker
- Git

## Setup walkthrough
1. clone the code from github using below command
    ```
   git clone https://github.com/kurtesy/cargill_app.git
   ```
2. Now run postgres docker image to run the db
    ```
   cd Cargill_Full_Stack_App/cargill_server
   docker-compose -f docker-compose.yml up
   ```
3. Go to the project directory and setup python server
    ```
   cd Cargill_Full_Stack_App/cargill_server/src
   pip install -r requirments.txt
   python server.py
   ```
4. Lastly lets run the React UI
    ```
   cd Cargill_Full_Stack_App/cargill_ui
   yarn
   yarn start
   ```
5. Your UI will be running in http://localhost:3000/

## API Doc

You can check the Swagger doc for the 2 main APIs

`http://localhost:5000/api/docs/#/`

#### Bonus some useful commands for docker
1. Delete all docker images
``docker rmi $(docker images -a -q)``
2. Stop docker
``docker-compose stop ``
3. Remove all docker volumes
``docker-compose rm -v ``
4. Check logs
``docker-compose logs -f ``
5. Hard remove all (Beware of this command as it remove everything in docker context)
``docker system prune -a``