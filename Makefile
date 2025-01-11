install:
	poetry install

run:
	poetry run uvicorn app.main:app --reload

test:
	poetry run pytest

lint:
	poetry run flake8 app/

format:
	poetry run black app/
