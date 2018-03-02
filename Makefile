clean:
	find . -name *__pycache__ -type d -delete
	find . -name \*.pyc -delete

migrate:
	python manage.py makemigrations

test: clean
	tox
