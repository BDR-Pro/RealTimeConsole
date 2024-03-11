import sys
def RemoveLastLine():
    sys.stdout.write("\033[F")  # Move the cursor up one line
    sys.stdout.write("\033[K")  # Clear the line
