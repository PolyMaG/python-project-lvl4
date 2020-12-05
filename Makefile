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
	coverage erase
	coverage run --source=. manage.py test
	coverage xml

.PHONY: install loaddb lint sort test
