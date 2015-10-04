# django-csvtojson


### A CSV to Django initial_data JSON converter.

django-csvtojson Generates an initial_data.json from a csv file to use with Django migrations.

Simplifies data entry for entering a large quantity of objects to your Django app.

**Caveats:**

At this time django-csvtojson does not support creating foreign key relations with other models.


### Installation:
```
pip install --egg git+https://github.com/njamaleddine/django-csvtojson
```

### Using the script from the command line:

```python
from csv_to_json import create_json

create_json(app_name, model_name, csv_file_name, json_output_file_name, primary_key_start_value)
```

### Parameters:
`app name`:
The name of the app that the Django model is located in.


`model_name`:
The name of the Django model.


`csv_file_name`:
The csv input file name


`json_output_file_name` **(Optional)**:
The JSON output file name. Defaults to the csv_file_name with a JSON file extension


`primary_key_start_value` **(Optional)**:
The primary key to start from. If you already have models in the database table you can offset the first primary key to begin at another value. Default value = 1.


### Example Usage:
```python
create_json("users", "user", "users.csv")
```

##### If the file wasn't generated in the right directory, move/save it to the desired folder.

##### Create a blank django migration for the app:
```python
python manage.py makemigrations --empty app_name
```

##### Write up a django migration to load the fixture data:
```python

from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command


def load_user_data(apps, schema_editor):
    call_command("loaddata", "../fixtures/users.json")


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_user_data)
    ]

```

##### Run the django migration to load the new json data into your database:
```python
python manage.py migrate
```

### Example input and output files:
See `tests/test.csv` and `tests/test.json`
