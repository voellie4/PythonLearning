import one

print("top level of two.py")

#indicate python file is run directly from command line
if __name__ == '__main__':
	one.func()
	print("two.py is run from command line")

#if run directly:
#top level of one.py
#one.py is imported
#top level of two.py
#func() from one.py
#two.py is run from command line