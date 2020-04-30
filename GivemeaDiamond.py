"""
Jamie is a programmer, and James' girlfriend.
She likes diamonds, and wants a diamond string from James.
Since James doesn't know how to make this happen, he needs your help.

Task
You need to return a string that looks like a diamond shape when
printed on the screen, using asterisk (*) characters.
Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative,
as it is not possible to print a diamond of even or negative size.

Examples
A size 3 diamond:

 *
***
 *
...which would appear as a string of " *\n***\n *\n"

A size 5 diamond:
  *
 ***
*****
 ***
  *
  """

"""
def diamond(n):
    if n>0:
        for i in range(n+1):
            if i%2==1   :
                print(i * '*')
                if i == n:
                    i=i-2
                    while i >0:
                        print((i)*'*')
                        i=i-2
    else:
        n = abs(n)
        for i in range(n+1):
            if i%2==1:
                print(i * '*')
                if i == n:
                    i=i-2
                    while i >0:
                        print((i)*'*')
                        i=i-2
"""

#Best Practice
#Algorithm:
#first we are taking input(n) from user after we chech our input.
#If n is divided by 2 and n < 1 we should return None ( 6%2=0  not 6%2=1)
#second we are create a list and we are using list comprehension if you want to understand clearly algorithm
# please choice a number and try

def diamond(n):
    if not n%2 or n<1: return None
    d = [" "*i+"*"*(n-2*i)+"\n" for i in range(int(n/2),0,-1)]
    return ''.join(d) + "*"*n + "\n" + ''.join(d[::-1])
print(diamond(7))