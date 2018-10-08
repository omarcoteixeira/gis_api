export FLASK_ENV=development

setup:
	conda install -c virtualenv;                \
	conda create -n venv python=2.7 anaconda;   \
	/bin/bash -c "source activate venv";

ci-install: setup
	pip install -r requirements.txt

install:
	pip install -r requirements.txt

test:
	pytest tests

run:
	python app.py