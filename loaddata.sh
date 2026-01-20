#!/bin/bash


apps=(
    "users"
    "contacts"
)

for app in "${apps[@]}"
do
    file="fixtures/${app}.json"
    if [ -f "$file" ]; then
        echo "Loading $file..."
        python manage.py loaddata "$file"
    else
        echo "File $file not found, skipping..."
    fi
done

echo "All available fixtures loaded"