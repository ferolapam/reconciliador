.PHONY: venv install install-dev run test docker-build docker-up lint

venv:
	python -m venv .venv

install: venv
	. .venv/bin/activate || true
	pip install --upgrade pip
	pip install -r app/requirements.txt

install-dev: install
	pip install -r app/requirements-dev.txt

run:
	python -m uvicorn app.service:app --reload --port 8000

test:
	pytest -q

docker-build:
	docker build -t reconciliador:local .

docker-up:
	docker-compose up --build -d

lint:
	black .
	isort .
	flake8
