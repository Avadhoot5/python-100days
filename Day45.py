# if __name__ == "__main__"

# when script if run direclty then, __name__ var is set to string __main__ 
# when the script is imported as a module into another script, the __name__ var is set to the name of the module


import Importing as i

a = i.hel()
print(a)