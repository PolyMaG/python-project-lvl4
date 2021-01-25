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
	poetry run coverage erase
	poetry run coverage run --source=. manage.py test
	poetry run coverage report
	poetry run coverage xml

.PHONY: install loaddb lint sort test
