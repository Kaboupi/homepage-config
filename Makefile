PYTHON_VERSION = python3
VENV = venv
VENV_PYTHON = $(VENV)/bin/$(PYTHON_VERSION)

.DEFAULT_GOAL := help

.PHONY: run venv clean help

help:
	@echo "Available commands:"
	@echo "- help: help page"
	@echo "- venv: set up venv"
	@echo "- run: start config gen"
	@echo "- clean: clean venv"

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
	@echo "=> Start docker containers"
	docker compose up -d
	@echo "=> Start config gen"
	$(VENV_PYTHON) gen/main.py
	@echo "=> Success!"

clean:
	@echo "=> Start venv cleanup"
	rm -rf $(VENV)
	@echo "=> Cleaned"
