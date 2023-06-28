import sys
from DownloadableFunctions import *
import os

py_file_name=sys.argv[1]
#print(py_file_name)
parent_dir=os.getcwd()
#print("Current Working Directory " , os.getcwd())
sys.path.append(parent_dir+r"\DownloadableFunctions")
import_module = __import__(py_file_name)
Introduction_Data=import_module.introduction()
#print(Introduction_Data)



avaialable_function_table={}
avaialable_function_file = open(parent_dir+r"\AvailableFunctions.txt")
avaialable_function_file_contents = avaialable_function_file.read()
Lines = avaialable_function_file_contents.splitlines()
for line in Lines:
        key_values=line.split("=>")
        key=key_values[0]
        value=(key_values[1]).split("|")
        avaialable_function_table[key] = value

#print(avaialable_function_table)

if Introduction_Data['Function Type'] in avaialable_function_table:
        if py_file_name not in avaialable_function_table[Introduction_Data['Function Type']]:
                avaialable_function_table[Introduction_Data['Function Type']].append(py_file_name)
else:
        avaialable_function_table[Introduction_Data['Function Type']]=[py_file_name]

Output_file = open(parent_dir+r"\AvailableFunctions.txt", "w")
for key in avaialable_function_table:
        value_text=""
        for each_func in avaialable_function_table[key]:
                value_text+=each_func+"|"
        text=key+"=>"+value_text[:-1]
        Output_file.write(text)
        Output_file.write("\n")
Output_file.close()
