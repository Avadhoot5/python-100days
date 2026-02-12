# Exercise 7 solution 

import os

def clearClutter(fileExtension):

    def filterExtension(file):
        if (file.split('.')[1] == fileExtension):
                return True
        return False

    filePath = "C:\\Users\\bavdo\\Desktop\\Desktop Files\\Desktop Programming Files\\100 days python\\Exercise7"
    

    listDir = os.listdir(filePath)
    listExtension = list(filter(filterExtension, listDir))

    try:
        for i in range(len(listExtension)):
            os.rename(f'{filePath}\\{listExtension[i]}', f'{filePath}\\{str(i+1)}.{fileExtension}')
    except:
        print('there is something wrong with the file path')
    
clearClutter('pdf')
