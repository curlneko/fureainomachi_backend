format:
	black .
	isort .

lint:
	flake8 .

typecheck:
	mypy .

test:
	pytest -v --cov=app --cov-report=html --cov-report=term-missing tests/

all: format lint typecheck test