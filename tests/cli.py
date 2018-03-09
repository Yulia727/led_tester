# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
import click
from led_tester import led_tester

click.disable_unicode_literals_warning = True



@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_tester."""
    
    N, instructions = led_tester.parseFile(input)
    
    ledTester = LightTester(N)
    
    for instruction in instructions:
        ledTester.apply(instruction)
    
    print('#occupied: ', LedTester.count())
    return 0


if __name__ == "__main__":
    main()  # pragma: no cover
