"""
Django CSV to JSON converter.
Best used for populating an initial_data.json for Django's Migrations

Nabil Jamaleddine
"""
import csv
import json

def convert_csv_boolean (boolean):
    """ Convert String booleans from csv to a Python boolean """
    if boolean.lower() == "true":
        return True

    elif boolean.lower() == "false":
        return False
    pass

def create_json (app_name, model_name, csv_file_name, primary_key_start_value):
    """ Create the json objects """
    # Initialize the json model
    app_name = str(app_name)
    model_name = str(model_name)
    primary_key_start_value = abs(int(primary_key_start_value) - 1)
    row_count = 0

    if primary_key_start_value == None:
        primary_key_start_value = 0

    # Get user input for reading in the csv file
    csv_file_name = str(csv_file_name)
    json_file_name = csv_file_name.split(".")[0] + ".json"

    # Read the csv file and write to the json file
    csv_file = open(csv_file_name, 'r')
    json_file = open(json_file_name, 'w')

    # Count the number of lines in the file (exclude the header row)
    numline = len(csv_file.readlines()) - 1

    # # reread the file
    # csv_file = open(csv_file_name, 'r')

    # Create each json object for the csv
    for row in csv.DictReader(csv_file):
        row_count += 1

        # Read rows
        fields = {
            "name": row["name"],
            "is_graduate_school": convert_csv_boolean(row["is_graduate_school"]),
            "is_other": convert_csv_boolean(row["is_other"])
        }

        row_insert = {
            "model": "{0}.{1}".format(app_name, model_name),
            "pk": primary_key_start_value + row_count,
            "fields": fields
        }

        print row_insert

        json.dump(row_insert, json_file, sort_keys=False, indent=4)

        # End the file without a comma
        if row_count == numline:
            json_file.write('\n')
        else:
            json_file.write(',\n')
