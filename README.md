# django-csvtojson


### A CSV to Django initial_data JSON converter.

django-csvtojson Generates an initial_data.json from a csv file for use with Django migrations.

Simplifies data entry for entering a large quantity of objects to your Django app.

**Caveats:**

At this time django-csvtojson does not support creating foreign key relations with other models.


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
create_json("users", "user", "test.csv")
```

### Example input and output files:
See `test.csv` and `test.json`