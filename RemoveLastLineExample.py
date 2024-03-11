from RemoveLastLine import RemoveLastLine
from time import sleep

for i in range(100):
    print(f"{'#' * i}---{i}% done...")
    RemoveLastLine()
    sleep(.1)
    
    
# This is a simple example of how to use the RemoveLastLine function to create a real-time console output.


