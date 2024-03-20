"""
Filtering Script for history files of Realms in Exile. This script is designed to filter through 
the history files of characters in the Realms in Exile mod of Crusader Kings 3. You may choose whether
you want to filter for an attribute of a character or a change in attribute of a character.
"""

# Author: Johan de Jongh (github: @de-longhi)

# License: MIT

import re
import os
import sys
import re

def main() -> None:
    args = sys.argv
    if (len(args) == 1):
        raise TypeError('Not enough arguments. Uses: "python3 src/filter.py <filepath or buffer>"')
    
    input_file = args[1]
    if not os.path.exists(input_file):
        raise FileNotFoundError("Input file not found.")
    output_file = input("Enter the output file path: \n")
    
    if input("Do you want to filter for an attribute(1) or a change of attribute(2)?\n") == "1":
        raise NotImplementedError("This functionality has not been implemented yet.")
    else:
        change_type = input("Enter the name of the change you want to filter for, E.g. 'birth'\n")
    
        if change_type == "effect":
            effect(input_file, output_file)
        else:
            raise NotImplementedError("Functionality for {0} has not been implemented yet.".format(change_type))

    print("Filtered lines have been written to", output_file)
    
def effect(input_file : str, output_file : str) -> None:
    """_summary_

    Args:
        input_file (str): _description_
        output_file (str): _description_
    """
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
            while not re.match(r'(\t|\s{4})(\t|\s{4})}', line):
                if re.match(r'^(\t|\s{4})(\t|\s{4})(\t|\s{4})' + effect_name + r'.*', line):
                    line = file.readline()
                    if re.match(r'^(\t|\s{3}\s?)(\t|\s{3}\s?)(\t|\s{3}\s?)(\t|\s{3}\s?)' + filter_line + r'.*', line):
                        line = file.readline()
                        result = "{0}{1}\t{2}{3}\n\t\t{4}\n\t\t{5}\n\t{6}\n{7}\n\n".format(result, "character:" + current_ID, effect_name," = {", filter_line.strip(), line.strip(), "}", "}")
                line = file.readline()
        line = file.readline()
    
    output.write(result)
    file.close()
    output.close()
        
if __name__ == "__main__":
   main()
