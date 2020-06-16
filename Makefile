# this is the target
unittest:
	docker build -t bayarea-relief .
	docker run bayarea-relief
start-env:
	pip3 install virtualenv
	python3 -m venv env
	source env/bin/activate
stop-env:
	deactivate
database-start:
	docker-compose up -d
	docker exec -it $$(docker ps -aqf "name=postgres") /bin/bash
database-stop:
	docker-compose down
webserver:
	pip3 install -r requirements.txt
	python -m bay_area_relief