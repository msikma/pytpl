# Copyright (C) 2016, Michiel Sikma
# MIT licensed

"""
Example command line script.
"""
import argparse
import pkg_resources
from pytpl.extable.table import make_extable

PACKAGE = pkg_resources.require('pytpl')[0]
PYTPL_URL = 'https://mycoolwebsite.com/'


def main():
    """
    Example command line script, to run as 'pytpl' on the command line.

    Note that this script does not have a shebang on the first line
    like setup.py does. When installing the module, a script is generated
    that calls this function when invoking 'pytpl' on the command line.
    """
    argparser = argparse.ArgumentParser(add_help=False)
    argparser.description = 'Python Template example script.'
    argparser.epilog = (
        'This is just an example script designed to show how to use setup.py '
        'to build command line tools. For more information, see <{}>.'
    ).format(PYTPL_URL)

    argparser.add_argument(
        '-h', '--help',
        action='help',
        help='Show this help message and exit.'
    )
    argparser.add_argument(
        '-V', '--version',
        action='version', version='{} ({})'.format(
            PACKAGE.project_name,
            PACKAGE.version
        ),
        help='Show version number and exit.'
    )
    argparser.parse_args()

    # argparser.parse_args() will exit if the user requested --help
    # or --version, or if an invalid command was entered.

    print('Python Template - example command line script')
    print('It works! Try running this with --help too.')

    # Just as an example, let's print a table to the terminal from
    # one of our other modules.
    table_str = make_extable('hello world!')
    print(table_str)
