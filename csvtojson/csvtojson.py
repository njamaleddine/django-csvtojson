"""
Django CSV file to JSON converter.

Used for populating an initial_data.json for Django's Migrations

Author: Nabil Jamaleddine
"""
from __future__ import print_function
import csv
import json
import re


def validate_field(value):
    """
    Validates major data types using regular expression matching.

    Converts String booleans from a csv to Python boolean values

    Also converts integer, and float values
    """

    if value.lower() == "true":
        return True

    elif value.lower() == "false":
        return False

    elif re.match(r"\d+$", value):
        return int(value)

    elif re.match(r"[-+]?\d+\.\d+$", value):
        return float(value)

    return value


def create_json(app_name, model_name, csv_file_name, json_output_file_name=None, primary_key_start_value=None):
    """ Create array of json from csv """
    app_name = str(app_name)
    model_name = str(model_name)

    if primary_key_start_value is None:
        primary_key_start_value = 0
    else:
        primary_key_start_value = abs(int(primary_key_start_value)) - 1

    # Get user input for reading in the csv file
    csv_file_name = str(csv_file_name)
    if json_output_file_name is None:
        json_file_name = '{}.{}'.format(csv_file_name.split(".")[0], "json")
    else:
        json_file_name = json_output_file_name

    # Read the csv file and write to the json file
    csv_file = open(csv_file_name, 'r')
    json_file = open(json_file_name, 'w')

    # Count the number of lines in the file (exclude the header row)
    total_rows = len(csv_file.readlines()) - 1

    # reread the file
    csv_file = open(csv_file_name, 'r')
    reader = csv.DictReader(csv_file, skipinitialspace=True)

    # Initialize fields dictionary
    fields = {}

    json_file.write('[\n')

    # Create each json object for the csv
    for index, row in enumerate(reader):
        # Populate fields with field data
        for field_name in reader.fieldnames:
            fields[field_name] = validate_field(row[field_name])

        row_insert = {
            "model": "{0}.{1}".format(app_name, model_name),
            "pk": primary_key_start_value + (index + 1),
            "fields": fields
        }

        print(row_insert)

        json.dump(row_insert, json_file, sort_keys=False, indent=4)

        # End the file without a comma
        if (index + 1) == total_rows:
            json_file.write('\n')
        else:
            json_file.write(',\n')

    json_file.write(']')
