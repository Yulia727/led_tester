#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import urllib.request
import re
import sys
sys.path.append('.')
import led_tester
import re


class LightTester:
    Lights = None
    
    def __init__(self, N):
        self.lights = [[False]*N for _ in range(N)]

    def apply(self, command, x1, y1, x2, y2):
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        if x1 < 0:
            x1 = 0
        
        if x2 < 0:
            x2 = 0
        elif x2 > len(self.lights)-1:
            x2 = len(self.lights)-1
            
        if y1 < 0:
            y1 = 0
        
        if y2 < 0:
            y2 = 0
        elif y2 > len(self.lights)-1:
            y2 = len(self.lights)-1

        if command == "turn on":
            self.turnOn(x1, y1, x2, y2)
            
        elif command == 'turn off':
            self.turnOff(x1, y1, x2, y2)
            
        elif command == 'switch':
            self.switch(x1, y1, x2, y2)


    def turnOn(self, x1, y1, x2, y2):
        for i in range (x1, x2 + 1):
            for j in range (y1, y2 + 1):
                    self.lights[i][j] = True
                           
    def turnOff(self, x1, y1, x2, y2):
        for i in range (x1, x2 + 1):
            for j in range (y1, y2 + 1):
                    self.lights[i][j] = False
                           
    def switch(self, x1, y1, x2, y2):
        for i in range (x1, x2 + 1):
            for j in range (y1, y2 + 1):
                if self.lights[i][j] == False:
                    self.lights[i][j] = True       
                else:
                    self.lights[i][j] = False
                                    
    def count(self):
        count = 0
        numrows = len(self.lights)
        numcols = len(self.lights[0])
        
        for i in range(0, numrows):
                for j in range(0, numcols):
                    if self.lights[i][j] == True:
                        count += 1
        return count


def main(input):

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
    main()