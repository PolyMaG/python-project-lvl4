install:
	poetry install

loaddb:
	poetry run python manage.py loaddata task_status_data.json

lint:
	poetry run flake8 task_manager tasks

sort:
	poetry run isort task_manager/*.py
	poetry run isort tasks/tests/*.py

test:
	poetry run python manage.py test
	# poetry run pytest -vv --cov=task_manager --cov-report xml tests/

.PHONY: install loaddb lint sort test 