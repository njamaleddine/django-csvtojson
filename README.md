django-csvtojson
==================

###Django CSV to JSON converter.

Generates an initial_data.json from a csv file for use with Django migrations.

Simplifies data entry for entering a large quantity of models to your database tables into your Django app.


No installation needed, just run the script with a few parameters and a formatted csv.

###Using the script from the command line:

`>>> python`
`>>> from csv_to_json import create_json`
`>>> create_json(app_name, model_name, csv_file_name, primary_key_start_value)`

###Ex:
`create_json("users", "user", "test.csv")`