"""
Filtering Script for history files of Realms in Exile
"""

# Author: Johan de Jongh (github: @de-longhi)

# License: MIT

import re
import os
import sys
import re

def effect(input_file : str, output_file : str) -> None:
    current_ID = ""
    result = ""
    effect_name = input("Enter the name of the effect you want to check for: ")
    filter_line = input("Enter the exact line you want to search for: ")
    file = open(input_file, 'r')
    line = file.readline()
    output = open(output_file, 'w')
    while (line):
        if line[0].isalpha():
            current_ID = line   
        elif re.match(r'^(\t|\s{4})(\t|\s{4})effect.*', line):
            line = file.readline()
            if re.match(r'^(\t|\s{4})(\t|\s{4})(\t|\s{4})' + effect_name + r'.*', line):
                line = file.readline()
                if re.match(r'^(\t|\s{3}\s?)(\t|\s{3}\s?)(\t|\s{3}\s?)(\t|\s{3}\s?)' + filter_line + r'.*', line):
                    line = file.readline()
                    result = "{0}{1}\t{2}{3}\n\t\t{4}\n\t\t{5}\n\t{6}\n{7}\n\n".format(result, "character:" + current_ID, effect_name," = {", filter_line.strip(), line.strip(), "}", "}")
        line = file.readline()
    
    output.write(result)
    file.close()
    output.close()
        
    

def filter_lines() -> None:
    with open(input_file, 'r') as f:
        lines = f.readlines()

    filtered_lines = []
    for i in range(len(lines)):
        if not re.match(r'^($|#).*', lines[i]):
            filtered_lines.append(lines[i])

    with open(output_file, 'w') as f:
        for line in filtered_lines:
            f.write(line)

if __name__ == "__main__":
    args = sys.argv
    if (len(args) == 1):
        print('Uses: "python3 filter.py <filepath or buffer>"')
        sys.exit()
    input_file = args[1]
    if not os.path.exists(input_file):
        print("file does not exist!")
        sys.exit()
    output_file = input("Enter the output file path: \n")
    if input("Do you want to filter for an attribute(1) or a change of attribute(2)?\n") == 1:
        pass
    else:
        change_type = input("Enter the name of the change you want to filter for, E.g. 'birth'\n")
    
        if change_type == "effect":
            effect(input_file, output_file)

    #filter_lines(input_file, output_file)
    print("Filtered lines have been written to", output_file)
