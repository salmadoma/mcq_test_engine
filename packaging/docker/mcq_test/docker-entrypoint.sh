#!/bin/bash

echo "Running entrypoint script.."

if [ "$DEBUG" == "1" ]; then
    # development mode
    echo "DEBUG is enabled!"
    python3 manage.py makemigrations --noinput
    python3 manage.py migrate
    python3 manage.py runserver 0.0.0.0:"$MCQ_TEST_SERVER_PORT"
else
    echo "DEBUG is disabled"
    # production mode
    python3 manage.py makemigrations --noinput
    python3 manage.py migrate
    python3 manage.py runserver 0.0.0.0:"$MCQ_TEST_SERVER_PORT"
fi

