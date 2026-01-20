#!/bin/bash


# Dont Seperate with commas just list them line by line 
apps=(
    "users"
    "contacts"
)

for app in "${apps[@]}"
do
    echo "Dumping $app..."
    python manage.py dumpdata "$app" --natural-foreign --natural-primary --indent 2 > "fixtures/${app}.json"
done

echo "All app data dumped to fixtures/"