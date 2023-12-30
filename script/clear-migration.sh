cd ../

find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

rm db.sqlite3
touch db.sqlite3

python manage.py makemigrations
python manage.py migrate
