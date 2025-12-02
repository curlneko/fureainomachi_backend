format:
	black .
	isort .

lint:
	flake8 .

typecheck:
	mypy app/

test:
	pytest -v --cov=app --cov-report=html tests/

all: format lint typecheck test