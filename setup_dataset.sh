#!/bin/bash

# Project root
PROJECT_NAME="wound-web-app"

# Create directories
mkdir -p $PROJECT_NAME/backend
mkdir -p $PROJECT_NAME/frontend

# Create backend files
touch $PROJECT_NAME/backend/main.py
touch $PROJECT_NAME/backend/model.h5
touch $PROJECT_NAME/backend/utils.py

# Create frontend files
touch $PROJECT_NAME/frontend/index.html
touch $PROJECT_NAME/frontend/style.css
touch $PROJECT_NAME/frontend/script.js

# Create root file
touch $PROJECT_NAME/requirements.txt

echo "Project structure created successfully!"