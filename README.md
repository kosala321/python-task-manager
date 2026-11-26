# Python Task Manager API

A beginner-friendly REST API built with FastAPI.

## Features

- Create tasks
- List tasks
- Complete tasks
- Delete tasks
- Automated tests

## Requirements

- Python 3
- pip

## Installation

Create a virtual environment:

    python3 -m venv .venv

Activate it:

    source .venv/bin/activate

Install dependencies:

    pip install -r requirements-dev.txt

## Run the application

    uvicorn app.main:app --reload

## Run tests

    python -m pytest -v

## API documentation

Visit:

    http://127.0.0.1:8000/docs

## Development
Run tests using python -m pytest -v.
