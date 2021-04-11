DOCKER_EXEC=$(shell command -v docker > /dev/null && echo "docker exec -ti challenge_backend_1")


up:
	docker-compose -f docker-compose.yml up -d

stop:
	docker-compose -f docker-compose.yml stop

down:
	docker-compose -f docker-compose.yml down

ps:
	docker-compose -f docker-compose.yml ps

enter:
	$(DOCKER_EXEC) bash