def func():
	print("func() from one.py")

print("top level of one.py")

#indicate python file is run directly from command line
if __name__ == '__main__':
	print("one.py is run from command line")
else:
	print("one.py is imported")

#if run directly:
#top level of one.py
#one.py is run from command line