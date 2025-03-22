test:
	isort .
	black .
	flake8 .
	mypy .
