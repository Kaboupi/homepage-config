VENV = venv
VENV_PYTHON = $(VENV)/bin/python

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
	@echo "=== Создание виртуального окружения и установка зависимостей ==="
	python -m venv $(VENV)
	$(VENV_PYTHON) -m pip install -r gen/requirements.txt
	@touch $(VENV)/.infrastructure_done

run: venv
	@echo "=== Start config gen ==="
	@$(VENV_PYTHON) gen/main.py

clean:
	@echo "=== Start venv cleanup ==="
	rm -rf $(VENV)
	@echo "Cleaned."
