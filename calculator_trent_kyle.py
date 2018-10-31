#Kyle Trent
#cs480 lab3

import math
'''
sudo code
-------------------------------------------------------------------------------
methods:

error methods:

div by 0 error
non useable number error
imroper use of operators error
wrong symbol error
overflow error
wrong parens error

'''
def getInput():
    expressionStr = input("Enter the term to be calculated press ctrl+c to quit:  ")
    return expressionStr

def simplify(expressionStr):
    isOk = True
    #test to only use corect operators
    if("//" in expressionStr or "|" in expressionStr or "~" in expressionStr or ">>" in expressionStr or "<<" in expressionStr or
       "and" in expressionStr or "or" in expressionStr or "not" in expressionStr or "<" in expressionStr or ">" in expressionStr or "==" in expressionStr
       or "!=" in expressionStr or ">=" in expressionStr or "<=" in expressionStr or "%" in expressionStr or "**" in expressionStr):
        return False
    return isOk

print("This is my calculator with which python was used to create.  A note of importance: please do not include "+
      "an '=' sign in your mathematical expression as it is not needed.\n")
      
while True:
    #make sure only the operands specified in the lab can be used
    try:
        expressionStr = getInput()
        if (simplify(expressionStr)):
            if("^" in expressionStr):
                expressionStr = expressionStr.replace("^", "**")
            answer = eval(expressionStr)
            print(answer)
        else:
            print("You have used an improper syntax or operands")
    except ZeroDivisionError:
        print ("Error division by 0")

    except NameError:
        print("Name error please use numbers")

    except TypeError:
        print("Type error please use proper syntax")

    except SyntaxError:
        print("You have used improper syntax in your expression")
