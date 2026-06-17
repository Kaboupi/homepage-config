PYTHON_VERSION = python3
VENV = venv
VENV_PYTHON = $(VENV)/bin/$(PYTHON_VERSION)

.DEFAULT_GOAL := help

LOG_LEVEL ?= INFO

.PHONY: run venv clean help

help:
	@echo "Available commands: make [CMD]"
	@echo "  - help  : Displays this message"
	@echo "  - venv  : Set up local venv"
	@echo "  - run   : Render J2 templates with variables from .env"
	@echo "            and start all the containers"
	@echo "  - stop  : Stop all the containers"
	@echo "  - clean : Clean venv and down all the containers"

venv: $(VENV)/.infrastructure_done

$(VENV)/.infrastructure_done: gen/requirements.txt
	@echo "=> Creating venv and dependencies"
	$(PYTHON_VERSION) -m venv $(VENV)
	@echo "=> Created venv"
	$(VENV_PYTHON) -m pip install -r gen/requirements.txt
	@echo "=> Installing requirements"
	@touch $(VENV)/.infrastructure_done
	@echo "=> Finish"

run: venv
	@echo "=> Start config gen"
	$(VENV_PYTHON) gen/main.py --log-level $(LOG_LEVEL)
	@echo "=> Start docker containers"
	docker compose up -d
	@echo "=> Success!"

stop:
	@echo "=> Stop docker containers"
	docker compose stop
	@echo "=> All containers are stopped!"

lint: venv
	@echo "=> Start ruff linter checks"
	$(VENV_PYTHON) -m ruff check

fix: venv
	@echo "=> Start ruff linter fixes"
	$(VENV_PYTHON) -m ruff check --fix

clean:
	@echo "=> Start venv cleanup"
	rm -rf $(VENV)
	@echo "=> Start containers cleanup"
	docker compose down -v --remove-orphans
	@echo "=> All cleaned"
