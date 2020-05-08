run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

test:
	python manage.py test --noinput --keepdb

showmigrations:
	python manage.py showmigrations

superuser:
	python manage.py createsuperuser

shell:
	python manage.py shell

statics:
	python manage.py collectstatic --noinput
