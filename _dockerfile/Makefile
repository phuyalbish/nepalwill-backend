build:
	docker-compose -f docker-compose.yaml build --no-cache
up: 
	docker-compose -f docker-compose.yaml up
down:
	docker-compose -f docker-compose.yaml down
frontend: 
	docker exec -it nepalwill-frontend bash

backend: 
	docker exec -it nepalwill-backend bash

db:
	docker exec -it nepalwill-db bash

superuser:
	docker exec -it nepalwill-backend python manage.py createsuperuser

makemigrations:
	docker exec -it nepalwill-backend  python manage.py makemigrations

showmigrations:
	docker exec -it nepalwill-backend  python manage.py showmigrations

makemigrationsmerge:
	docker exec -it nepalwill-backend  python manage.py makemigrations --merge

migrate:
	docker exec -it nepalwill-backend  python manage.py migrate

loaddata:
	docker exec -it nepalwill-backend python manage.py loaddata fixtures/$(f).json

dumpdata: 
	docker exec -it nepalwill-backend python manage.py dumpdata $(f) --output=fixtures/$(f).json