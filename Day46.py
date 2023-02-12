# os Module
# VISIT PRACTICE TOPIC folder 

import os

folder = os.listdir('Days/')

for fold in folder:
    print(fold)
    print(os.listdir(f"Days/{folder}"))

