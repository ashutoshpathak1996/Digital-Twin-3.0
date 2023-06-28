import sys
from DownloadableFunctions import *
import os

py_file_name=sys.argv[1]
#print(py_file_name)
parent_dir=os.getcwd()
sys.path.append(parent_dir+r"\DownloadableFunctions")
import_module = __import__(py_file_name)
Introduction_Data=import_module.introduction()
print(Introduction_Data)
activeORpassive = str(Introduction_Data['active_passive'])
performative = str(Introduction_Data['performative_types'])


if activeORpassive == 'Active':
        active_function_table={}
        active_function_file = open(parent_dir+r"\ActiveFunctionsList.txt")
        active_function_file_contents = active_function_file.read()
        Lines = active_function_file_contents.splitlines()
        for line in Lines:
                key, value=line.split("=>")
                active_function_table[key] = value

##        print(active_function_table)

        active_function_table[py_file_name]='0'

        print(active_function_table)

        Output_file = open(parent_dir+r"\ActiveFunctionsList.txt", "w")
        for key in active_function_table:
                text=key+"=>"+active_function_table[key]
                Output_file.write(text)
                Output_file.write("\n")
        Output_file.close()

else:
        passive_function_table={}
        passive_function_file = open(parent_dir+r"\PassiveFunctionsList.txt")
        passive_function_file_contents = passive_function_file.read()
        Lines = passive_function_file_contents.splitlines()
        for line in Lines:
                key, value=line.split("=>")
                passive_function_table[key] = value

##        print(passive_function_table)

        passive_function_table[py_file_name]= performative

        print(passive_function_table)

        Output_file = open(parent_dir+r"\PassiveFunctionsList.txt", "w")
        for key in passive_function_table:
                text=key+"=>"+passive_function_table[key]
                Output_file.write(text)
                Output_file.write("\n")
        Output_file.close()
        
