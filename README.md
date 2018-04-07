# bitkeeper

## Installation Tips

Do this:

```
>>>  pip install django-csvimport
```

Modify the settings.py file of your Django project to include these INSTALLED APPS:

```python
INSTALLED_APPS = [
     .
     .
     .
    'bitkeeper',
    'csvimport.app.CSVImportConf'  # use AppConfig for django >=1.7 csvimport >=2.2
]
```

Then do this:

```
python manage.py migrate
```


Then to install Bitkeeper itself, here are some useful tips:
0) 
```
>>> mkdir bitkeeper
>>> cd bitkeeper
>>> git clone https://github.com/WPRDC/bitkeeper.git .
```

1) Be sure to add 'bitkeeper' to the ```INSTALLED_APPS``` list in Django's settings.py and wire up the URLs through urls.py.

2) Install marshmallow and its soft dependencies.

```
>>> pip install python-dateutil
>>> pip install marshmallow
```

3) Pip-install the wprdc-etl pipeline code:

```
>>> pip install -e git+https://github.com/WPRDC/wprdc-etl@d9bdfb045f21cffacd9c6242240bfc518e82e3d5#egg=pipeline
```

and some dependency that doesn't automatically install for some reason:

```
>>> pip install xlrd

4) Restart the Django server.

5) Set up the migrations directory in the bitkeeper app to contain only an empty __init__.py file.

```
>>> mkdir migrations
>>> touch __init__.py
```

6) Load the data into the database:
6a) To work around issues in importing data into a Postgres database (rather than a SQLite database), I edited models.py to comment out all foreign keys and many-to-many Fields.
6b) 
```
>>> python manage.py importcsv --mappings='' --model='bitkeeper.FireDepartment' --delimiter='t' bitkeeper/data/fd.csv

```

6c) Then I added all the foreign keys and many-to-many fields back in and migrated the database/app over.

6d) Finally, I did this:

```
>>> ./manage.py shell
>>> exec(open('bitkeeper/import_foreign_keys.py').read())
```

Using ```python manage.py dbshell``` is useful for examining the tables while building them (allowing commands like 

```sql
SELECT municipality, municode, bitkeeper1_municipality.police_department_id FROM bitkeeper1_municipality;
```

7) Rename all app-named stuff, even the directories (like ```templates/<app-name>/``` and ```static/<app-name>```) to be consistent with the deployed app name. (All of this should be automatically taken care of in future versions, which means that a simple GitHub repository of the files and directories isn't sufficient.)
