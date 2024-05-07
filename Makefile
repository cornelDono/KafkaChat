DC = sudo docker compose
EXEC = sudo docker exec -it
LOGS = sudo docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: app-down
app-shell:
	${EXEC} ${APP_CONTAINER} bash

.PHONY: app-shell
app-down:
	${DC} -f ${APP_FILE} down

.PHONY: test
test:
	${EXEC} ${APP_CONTAINER} pytest
