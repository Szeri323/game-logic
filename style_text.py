import os

print("hello world".center(os.get_terminal_size().columns))


# Color text in terminal:

print( '\033[93m' + "test" + '\033[0m')