# Copyright (C) 2016, Michiel Sikma
# MIT licensed

"""
Table generator using terminaltables.
"""
from terminaltables import SingleTable


def make_extable(stuff):
    """
    Returns an example table to be printed in the terminal.

    :param stuff: Some string that we want to include in the output
    :return: Table string to print into the terminal
    """
    table_data = [
        ['Zigs', 'Zags', 'Stuff'],
        [str(2**8), 'many', stuff]
    ]

    table = SingleTable(table_data)
    table.inner_row_border = True

    return table.table
