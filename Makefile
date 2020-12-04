install:
	poetry install

install_requirements:
	@pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements1.txt

install_dev_requirements:
	@pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.dev.txt

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
	#poetry run pytest -vv --cov=task_manager --cov-report xml tasks/tests/

.PHONY: install loaddb lint sort test install_requirements install_dev_equirements
