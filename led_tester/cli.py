# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
import click
from led_tester import led_tester
from led_tester.main import LightTester
import re

click.disable_unicode_literals_warning = True



@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_tester."""

    N,instructions = led_tester.parseFile(input)
    
    Lights = LightTester(N)

    for instruction in instructions:
        pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
        cmd = pattern.match(instruction)
        if (cmd != None):
            command = cmd.group(1)
            x1 = cmd.group(2)
            y1 = cmd.group(3)
            x2 = cmd.group(4)
            y2 = cmd.group(5)
            Lights.apply(command, x1, y1, x2, y2)
        else:
            continue;
    print("# occupied:", Lights.count())
    return Lights.count()

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
