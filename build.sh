#!/bin/bash
# poetry export -f requirements.txt --output requirements.txt

pip3 install -r requirements.txt

python3 manage.py collectstatic --noinput  
python3 manage.py makemigrations

python3 manage.py migrate

# python3 manage.py loaddata fixtures/*.json


# gunicorn --bind 0.0.0.0:8081 core.wsgi:application




# make build.sh executable build.sh
# sudo chmode +x ./build.sh

# If the port is already used

# For mac/Linux
# lsof -i :PORT
# kill -9 PID



# For Windows
# netstat -ano | findstr :PORT

# netstat -ano | findstr :8000

# taskkill /PID PID /F

# taskkill /PID 12345 /F