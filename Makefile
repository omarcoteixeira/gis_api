export FLASK_ENV=development

frontend-install:
	npm i --prefix frontend;

frontend-run: frontend-install
	npm run-script start --prefix frontend;

install:
	pip install -r requirements.txt

test:
	pytest tests

run:
	python app.py;