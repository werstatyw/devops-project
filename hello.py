#!/usr/bin/env python
"""this is cli"""

import click

from mylib.myadd import add


@click.command()
@click.option('--value1')
@click.option('--value2')
def calculate(value1, value2):
    result = add(value1, value2)
    click.echo({result})
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    calculate()

