# f strings 

name = 'avadhoot'
country = 'India' 

txt = "Hello My name is {0} and I am from {1}"
print(txt.format(name,country))

# by using fstring you can directly include variables inside the string 

print(f"Hello My Name is {name} and I am from {country}")

# to dislpay the output as it is use {{}}

print(f"Hello My Name is {{name}} and I am from {{country}}")
