install:
	poetry install

init:
	poetry run python manage.py loaddata task_status_data.json

lint:
	poetry run flake8 task_manager tasks
	# poetry run flake8 tests
	poetry run isort task_manager/*.py
	# poetry run isort tests/*.py

test:
	poetry run pytest -vv --cov=task_manager --cov-report xml tests/

.PHONY: install lint test publish