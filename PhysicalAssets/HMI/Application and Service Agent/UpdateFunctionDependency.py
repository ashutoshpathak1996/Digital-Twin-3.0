import sys
#from DownloadableFunctions import *
import os

py_file_name=sys.argv[1]
#print(py_file_name)
parent_dir=os.getcwd()
sys.path.append(parent_dir+r"\DownloadableFunctions")
import_module = __import__(py_file_name)
Introduction_Data=import_module.introduction()
print(Introduction_Data)
data_to_insert = str(Introduction_Data['Dependant Function'])


dependant_function_table={}
dependant_function_file = open(parent_dir+r"\FunctionDependency.txt")
dependant_function_file_contents = dependant_function_file.read()
Lines = dependant_function_file_contents.splitlines()
for line in Lines:
        key, value=line.split("=>")
        dependant_function_table[key] = value

print(dependant_function_table)

if py_file_name in dependant_function_table:
        dependant_function_table[py_file_name].append(data_to_insert)
else:
        dependant_function_table[py_file_name]=data_to_insert

Output_file = open(parent_dir+r"\FunctionDependency.txt", "w")
for key in dependant_function_table:
        text=key+"=>"+dependant_function_table[key]
        Output_file.write(text)
        Output_file.write("\n")
Output_file.close()
