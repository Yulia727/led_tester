import urllib.request
from led_tester import led_tester

def test_read_file():
    ifile = "./tests/test_data.txt"
    N, instructions = led_tester.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'turn on 2,2 through 7,7']