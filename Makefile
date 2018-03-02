clean:
	find . -name \*.pyc -delete

migrate:
	python manage.py makemigrations

test: clean
	tox
