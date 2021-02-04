
import random
from pyparsing import Regex 
import re


#isolate from expression into a list:
exp = "3d10 + 5 - (8*9) + 2d10 - 100 + d10 - 20 + d4"
#replace with sums then evaluate expression with parsemath 


def exp1(expression):
    iter_obj = iter(expression)
    dc = ""
    dcList = []
    x = iter_obj.__next__()
    try:
        for c in range(0, len(expression)):
            if re.match("[0-9]", x) or x == "d":
                if x == "d":
                    dc += "d"
                    x = iter_obj.__next__()
                    if re.match("[0-9]", x):
                        dc += x
                        while True:
                            if not re.match("[0-9]", x):
                                break
                            x = iter_obj.__next__()
                            if re.match("[0-9]", x):
                                dc += x
                        dcList.append(dc)
                        #dc = ""
                        x = iter_obj.__next__()
                        continue
                    x = iter_obj.__next__()
                    continue
                dc += x
                while True:
                    if not re.match("[0-9]", x):
                        break
                    x = iter_obj.__next__()
                    if re.match("[0-9]", x):
                        dc += x
                if x == "d":
                    dc += x
                    x = iter_obj.__next__()
                    if re.match("[0-9]", x):
                        dc += x
                        while True:
                            if not re.match("[0-9]", x):
                                break
                            x = iter_obj.__next__()
                            if re.match("[0-9]", x):
                                dc += x
                        dcList.append(dc)
            dc = ""
            x = iter_obj.__next__()
    except StopIteration:
        if len(dc) > 1 and dc != "d":
            dcList.append(dc)
        print(dcList)
        return dcList
          

exp1(exp)

#instead return a dictionary of the strings dcs and a list of the values to use to replace the values in the string with the sums
def rollcalc(dcList):
    dcDict = {}
    for dCalc in dcList:
        if dCalc[0] == "d":
            dc = "1" + dCalc
        else:
            dc = dCalc
        expression = dc.split("d")
        rollRange = int(expression[1])
        rolls = int(expression[0])
        if expression[1] == "0":
            values = [ 0 for x in range(abs(int(rolls))) ]
            dcDict[dCalc] = values
        else:
            values = [ random.randint(1,abs(int(rollRange))) for x in range(abs(int(rolls))) ]
            dcDict[dCalc] = values
        #print(f"{dc}: `" + ", ".join(map(str,values)) + "`")
    print(dcDict)
    return dcDict

def replaceDC(expression, dcDict):
    for dc in dcDict:
        if dc in expression:
            expression = expression.replace(str(dc), str(sum(dcDict[dc])))
    return expression


print(rollcalc(exp1(exp)))

dcDict = rollcalc(exp1(exp))

replaceDC(exp, dcDict)
