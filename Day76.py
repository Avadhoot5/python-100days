# Exercise 8 

import os

filePath = "C:\\Users\\bavdo\\Desktop\\Desktop Files\\Desktop Programming Files\\100 days python\\PDFMerge"

def get_pdf_list(path):

    month_values = {}

    month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']

    for month_num, month_name in enumerate(month_list, start=1):
        month_values[str(month_name[:3])] = month_num

    contents = os.listdir(path)
    contents_dict = {}

    for i in contents:
        contents_dict[i] = month_values[i.split(' ')[1][:3]]
    
    sorted_dict = dict(sorted(contents_dict.items(), key = lambda x: x[1]))

    return sorted_dict

month_list = get_pdf_list(filePath)

def merge_PDF(pdf_list):
    
    from pypdf import PdfWriter
    
    merger = PdfWriter()

    for i in pdf_list.keys():
        merger.append(f'{filePath}\\{i}')

    merger.write(f'PDFMerge\\output.pdf')

merge_PDF(month_list)
