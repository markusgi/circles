# Hiring Challenge 

Mi solution to the hiring challenge. A simple dockerized django backend with persons and circles, displayed in a vue frontend with jwt login.

# Developer guide

The current tech stack of this project is:

    Vuetify
    Vue.js
    Django
    Docker


# Setup project
(1) download docker image
```bash
docker build -t challenge-backend:latest .
```

(2) start the project:
```bash
make up
```
The backend should now be accessible via

Backend:  localhost:8000/backend/api
(3) enter the container 
```bash
make enter
```
(3) apply migrations
```bash
python manage.py migrate
```

(*) import csv Persons, enter django container then:
```bash
python manage.py import_persons_from _csv employees.csv
```

(4) run frontend
```bash
cd frontend
npm install
npm run serve
```
