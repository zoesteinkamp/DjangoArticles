if [[ "$VIRTUAL_ENV" != "" ]]
then
   pip3 install -r requirements.txt &&
   python manage.py migrate &&
   python manage.py loaddata articles/fixtures/fixtures1.json &&
   python manage.py loaddata articles/fixtures/fixture2.json &&
   python manage.py loaddata articles/fixtures/articles.json
   python manage.py loaddata articles/fixtures/fixturesqoutes.json
   python manage.py runserver
else
 echo “no virtual environment running”
fi
