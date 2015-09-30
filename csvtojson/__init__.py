from csvtojson import create_json

__title__ = 'Django CSV To JSON'
__version__ = '0.1.0'
__author__ = 'Nabil Jamaleddine'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Nabil Jamaleddine'


def get_version():
    return __version__


def main(*args):
    create_json(
        app_name=args[0],
        model_name=args[1],
        csv_file_name=args[2],
        json_output_file_name=args.get(3, None),
        primary_key_start_value=args.get(4, None)
    )
