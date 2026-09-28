# Variables
PYTHON = python3
PIP = pip3
INTERPRETER = mjlang.py
EXAMPLE_DIR = examples
TEST_DIR = tests

.PHONY: all help test run-example install clean

# Default target
all: test

help:
	@echo "MJLang Build System"
	@echo "Available commands:"
	@echo "  make test         - Run automated unit tests"
	@echo "  make run-example  - Run the Smooth Criminal example script"
	@echo "  make install      - Install mjlang CLI globally via pip"
	@echo "  make clean        - Remove Python cache files and build artifacts"

test:
	@echo "🕺 Running MJLang Unit Tests..."
	$(PYTHON) -m unittest discover -s $(TEST_DIR)

run-example:
	@echo "🎙️ Executing Smooth Criminal Example..."
	$(PYTHON) $(INTERPRETER) $(EXAMPLE_DIR)/smooth_criminal.mj

install:
	@echo "🚀 Installing MJLang globally..."
	$(PIP) install .

clean:
	@echo "🧹 Cleaning up bytecode and build artifacts..."
	rm -rf __pycache__
	rm -rf $(TEST_DIR)/__pycache__
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -name "*.pyc" -delete
