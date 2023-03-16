# String Methods in Python

# String are immutable in Python
# When we apply String methods to them, it creates a copy of the string and applies the given method on the string & prints the value.

# Len, Upper, and Lower 

length = "Hello World"
print(len(length))
print(length.upper())
print(length.lower())

# Rstrip(): removes any trailing character, if these characters are present at the start it won't remove them

trail = "Hello !!!!!"
print(trail.rstrip("!"))

# Similarly Lstrip: removes trailing character from start, strip() - removes all the trailing characters

trail_1 = "!! Hello there !!!!"
print(trail_1.strip("!"))

# replace(): replaces all occurences of the string with another string 

replace = "Hello gets replaced"
print(replace.replace("Hello", "Welcome"))

# split(): splits the string at the specified instance and returns the seperated strings as list items.

split = "This string will be replaced with split string methods and the contents will be displayed in list format"
print(split.split(" "))

# capitalize(): turns only the first character of the string to uppercase and rest all items are turned to lower case

cap = "hello"
print(cap.capitalize())
cap1 = "heLlO WORLD"
print(cap1.capitalize())

# center(): alligns the string to the center as per the parameters given by the user.

cen = "This string is displayed in the center"
cen2 = cen.center(59)
print(cen2) # where 59 is the total length of the string after the center method is applied to the string.
print(len(cen))
print(len(cen2))

# count(): returns the number of times the given value has occured in the string.

cnt = "the program should count the number of times s appears in the given string"
print(cnt.count("s"))

# endswith(): checks if the string ends with a given value

endwith = "this string ends with !!"
print(endwith.endswith("!"))

# Also, you can check for a value in between the string by specifying the start and end index positions.

# find() returns the first occurence of the given value & returns the index where it is present. If value is not present it returns -1
# index() is similar to find(), but if the given value is not present in the string it THROWS AN ERROR

finding = "below is the index of index word"
print(finding.find("index"))

# isalum(): is alpha numeric returns TRUE if the string contains: A-Z, a-z, 0-9
# !IMPORTANT - Spaces are also not allowed, if space exists it returns false

checkalum = "thisisacheckforalphanumeric42323"
checkalum1 = "hello this checks if string is alpha numeric \n !@ or not"
print(checkalum)
print(checkalum1)
print(checkalum.isalnum())
print(checkalum1.isalnum())

# isalpha(): only aphabets are allowed.

only_alpha = "hello"
print(only_alpha.isalpha())

# lower, upper, printable, space, title 

lower = "all the words are in lower case"
print(lower)
print(lower.islower())

upper = "ALL THE WORDS ARE IN UPPER CASE"
print(upper)
print(upper.isupper())

printable = "This string is printable"
not_printable = "This string is not printable \t" # because this string consists of escape sequence characters which can't be shown to the user
print(printable)
print(printable.isprintable())
print(not_printable)
print(not_printable.isprintable())

# Only SPACES are considered 

space_check = "     "
space_check_2 = "thereisnospacehere"
print(space_check)
print(space_check.isspace())
print(space_check_2)
print(space_check_2.isspace())

# Title()  capitalizes each letter of the word within the string

title_set = "set the title of this string"
print(title_set.title())
# istitle() checks the title of the string and returns TRUE if right.

# swapcase() swaps the lower and upper cases of the string

lower_to_upper = "this is changed from lower to upper case using swapcase method"
upper_to_lower = "THIS IS BEGIN SWAPPED FROM UPPER CASE TO LOWER CASE"
print(lower_to_upper.swapcase())
print(upper_to_lower.swapcase())
