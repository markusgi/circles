DOCKER_EXEC=$(shell command -v docker > /dev/null && echo "docker exec -ti challenge_backend_1")

enter:
	$(DOCKER_EXEC) bash

dev:
	$(DOCKER_EXEC) python3 manage.py runserver

adminuser:
	$(DOCKER_EXEC) python3 manage.py createsuperuser

migrate:
	$(DOCKER_EXEC) python3 manage.py migrate

makemigrations:
	$(DOCKER_EXEC) python3 manage.py makemigrations

import_persons:
	$(DOCKER_EXEC) python3 manage.py import_persons_from_csv