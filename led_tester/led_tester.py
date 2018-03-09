'''
Created on March 1, 2018

@author: Jiali Yu
'''
# -*- coding: utf-8 -*-
import requests

def parseFile(input):
    if input.startswith("http"):
        r = requests.get(input).text
        lines = r.split('\n')
        N = int(lines[0])
        instructions = lines[1:-1]
        return N, instructions
    else:
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        return N, instructions
    return
if __name__ == "__main__":
    parseFile(input)  # pragma: no cover
