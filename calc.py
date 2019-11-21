import re

print("Magic Python Calculator")
print("type 'quit' to exit/n")

previous = 0 
run = True


def performMath()
    global run
    global previous
    equation = ""
    if previous == 0:
       equation = input("Enter equation:")
    else:
       equation = input(str(previous))   


    if equation == "quit":
    	print("Goodbye!")
    	run = False
    else:

    	equation = re.sub('[a-sA-Z,.:()')

    if previous == 0:
    	previous = eval(equation)

    else:
         previous = eval(str(previous)+equation)	

 
        previous = eval(equation)

        

while run
  performMath()

