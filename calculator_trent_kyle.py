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

interpretation methods:

seperate + order terms in parens
compute terms in parens
compute final term
output and input
'''
def calculate():
    expression = input("Enter the term to be calculated press ctrl+c to quit:  ")
    answer = eval(expression)
    return answer
while True:
    try:
        answer = calculate()
        print(answer)
    except ZeroDivisionError:
        print ("Error division by 0")

    except NameError:
        print("Name error please use numbers")

    except TypeError:
        print("To use exponentiation please use ** instead of ^")

    except SyntaxError:
        print("You have used improper syntax in your expression")
