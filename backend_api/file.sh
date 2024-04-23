cd backend_api/
git pull
python manage.py migrate
python manage.py collectstatic --noinput
service gunicorn restart
service nginx restart