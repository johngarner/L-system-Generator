"""Adapted, edited, and added to by John Garner from Runestone Academy's How to Think Like a Computer Scientist at
https://runestone.academy/runestone/books/published/thinkcspy/Strings/TurtlesandStringsandLSystems.html"""

import turtle


# This creates the L-system itself
def createLSystem(numIter, axiom, ruleChoice):
    startString = axiom
    endString = ""
    for i in range(numIter):
        endString = processString(startString, ruleChoice)
        startString = endString
    return endString


# This processes strings using the ruleset chosen
def processString(oldStr, ruleChoice):
    newStr = ""
    for ch in oldStr:
        if ruleChoice == "1":
            newStr = newStr + applyRules1(ch)
        elif ruleChoice == "2":
            newStr = newStr + applyRules2(ch)
        elif ruleChoice == "3":
            newStr = newStr + applyRules3(ch)
        elif ruleChoice == "4":
            newStr = newStr + applyRules4(ch)
        elif ruleChoice == "5":
            newStr = newStr + applyRules5(ch)
    return newStr


# This applies and contains the first ruleset
def applyRules1(ch):
    newStr = ""
    if ch == 'F':
        newStr = 'F-F++F-F'  # Rule 1/1
    else:
        newStr = ch  # if the rule does not apply, this keeps the character
    return newStr


# This applies and contains the second ruleset
def applyRules2(ch):
    newStr = ""
    if ch == 'F':
        newStr = 'F-F++F+F-F-F'  # Rule 1/1
    else:
        newStr = ch  # if the rule does not apply, this keeps the character
    return newStr


# This applies and contains the third ruleset
def applyRules3(ch):
    newStr = ""
    if ch == 'F':
        newStr = 'F-G+F+G-F'  # Rule 1/2
    elif ch == 'G':
        newStr = 'GG'  # Rule 2/2
    else:
        newStr = ch  # if neither rule applies, this keeps the character
    return newStr


# This applies and contains the fourth ruleset
def applyRules4(ch):
    newStr = ""
    if ch == 'F':
        newStr = 'F+F-F-F-G+F+F+F-F'  # Rule 1/2
    elif ch == 'G':
        newStr = 'GGG'  # Rule 2/2
    else:
        newStr = ch  # if neither rule applies, this keeps the character
    return newStr


# This applies and contains the fifth ruleset
def applyRules5(ch):
    newStr = ""
    if ch == 'F':
        newStr = 'F=F-F++F-F'  # Rule 1/2
    elif ch == 'X':
        newStr = 'FF'  # Rule 2/2
    else:
        newStr = ch  # if neither rule applies, this keeps the character
    return newStr


# This instructs the turtle to draw the L-system fractal
def drawLSystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'G':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)


# This is the main, it initialises and runs the generator and prompts the user for inputs
def main():
    startIt = 0
    ruleChoice = "0"
    startAx = "F"
    startAng = 90

    while startIt not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("Please choose a number of iterations between 1 and 9:")
        startIt = int(input())
    while ruleChoice not in ["1", "2", "3", "4", "5"]:
        print("Please choose ruleset 1, 2, 3, 4, or 5:")
        ruleChoice = input()

    if ruleChoice == "1":
        startAng = 60
        startAx = "F"

    elif ruleChoice == "2":
        startAng = 72
        startAx = "F-F-F-F-F"

    elif ruleChoice == "3":
        startAng = 120
        startAx = "F-G-G"

    elif ruleChoice == "4":
        startAng = 90
        startAx = "F"

    elif ruleChoice == "5":
        startAng = 60
        startAx = "F++F++F"

    inst = createLSystem(startIt, startAx, ruleChoice)  # this creates the string
    print(inst)
    t = turtle.Turtle()  # this creates the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.hideturtle()
    t.speed(0)
    drawLSystem(t, inst, startAng, 5)  # this draws the picture
    wn.exitonclick()


main()
