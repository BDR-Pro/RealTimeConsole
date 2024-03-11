from ClearConsole import clearConsole
from time import sleep
###write anythin in the console to remove it 
##prefer to use it in the beginning of the code to remove any previous output
sleep(3)
clearConsole() #clear the console output
print("I am going to print Hello World 10 times")
for i in range(10):
    print("Hello World")
    sleep(0.1)

print("I am going to clear the console now")
sleep(3)
clearConsole() #clear the console output