install:
	poetry install

lint:
	# poetry run flake8 task_manager
	# poetry run flake8 tests
	poetry run isort task_manager/*.py
	# poetry run isort tests/*.py

test:
	poetry run pytest -vv --cov=task_manager --cov-report xml tests/

publish:
	poetry build
	poetry publish -r testpypi

.PHONY: install lint test publish