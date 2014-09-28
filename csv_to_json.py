"""
Django CSV to JSON converter.
Best used for populating an initial_data.json for Django's Migrations

Nabil Jamaleddine
"""
import csv
import json

def test ():
    print "HELLO WORLD"

def validate_field (value):
    """
    Convert String booleans from csv to a Python boolean

    Passes back value for all other data types
    """
    if value.lower() == "true":
        return True

    elif value.lower() == "false":
        return False

    return value

def create_json (app_name, model_name, csv_file_name, json_output_file_name=None, primary_key_start_value=None):
    """ Create the json objects """
    # Initialize the json model
    app_name = str(app_name)
    model_name = str(model_name)
    row_count = 0

    if primary_key_start_value == None:
        primary_key_start_value = 0
    else:
        primary_key_start_value = abs(int(primary_key_start_value) - 1)

    # Get user input for reading in the csv file
    csv_file_name = str(csv_file_name)
    if json_output_file_name == None:
        json_file_name = csv_file_name.split(".")[0] + ".json"
    else:
        json_file_name = json_output_file_name

    # Read the csv file and write to the json file
    csv_file = open(csv_file_name, 'r')
    json_file = open(json_file_name, 'w')

    # Count the number of lines in the file (exclude the header row)
    numline = len(csv_file.readlines()) - 1

    # reread the file
    csv_file = open(csv_file_name, 'r')
    reader = csv.DictReader(csv_file, skipinitialspace=True)

    # Initialize fields dictionary
    fields = {}

    # Create each json object for the csv
    for row in reader:
        row_count += 1

        # Read rows
        for field_name in reader.fieldnames:
            fields[field_name] = row[field_name]

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
