export FLASK_ENV=development

install:
	pip install -r requirements.txt -q

test:
	pytest tests

run:
	python app.py