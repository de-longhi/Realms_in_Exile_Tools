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
import platform


def main() -> None:
    output_file = ""
    args = sys.argv
    if (len(args) == 1):
        raise TypeError('Not enough arguments. Uses: "python3 src/filter.py <filepath or buffer>"')
    
    input_file = args[1]
    if not os.path.exists(input_file):
        raise FileNotFoundError("Input file not found.")
    
    if (len(args) == 3 and args[2] == "default"):
           
        s = _findLastIndex(input_file, "\\")+1 if platform.system() == "Windows" else _findLastIndex(input_file, "/") + 1
        output_file = "out/lotr_" + input_file[s:]
        effect(input_file, output_file, True)
        
    else:
        
        output_file = input("Enter the output file path: \n")
    
        if input("Do you want to filter for an attribute(1) or a change of attribute(2)?\n") == "1":
            raise NotImplementedError("This functionality has not been implemented yet.")
        else:
            change_type = input("Enter the name of the change you want to filter for, E.g. 'birth'\n")
    
        if change_type == "effect":
            effect(input_file, output_file, False)
        else:
            raise NotImplementedError("Functionality for {0} has not been implemented yet.".format(change_type))

    print("Filtered lines have been written to", output_file)
    
def _findLastIndex(str, x):
    index = -1
    for i in range(0, len(str)):
        if str[i] == x:
            index = i
    return index
def effect(input_file : str, output_file : str, default_settings : bool) -> None:
    """ This function handles all the parsing and filtering of prompts to do with effects.

    Args:
        input_file (str): Filepath or buffer to the input file.
        output_file (str): Filepath or buffer to the output file.
    """
    result = ""
    effect_name = ""
    filter_line = ""
    
    if default_settings == True:
        effect_name = "add_trait_xp"
        filter_line = "trait = blood_of_numenor"
    else:
        effect_name = input("Enter the name of the effect you want to check for: ")
        filter_line = input("Enter the exact line you want to search for: ")
    
    file = open(input_file, 'r')
    line = file.readline()
    output = open(output_file, 'w')
    while (line):
        if line[0].isalpha():
            current_ID = line   
        elif re.match(r'^(\t|\s{4}){2}effect = {.*}.*', line): #XXX
            line = file.readline()
        elif re.match(r'^(\t|\s{4}){2}effect.*', line):
            line = file.readline()
            while not re.match(r'(\t|\s{4}){2}' + "}" + r'.*', line):
                if re.match(r'^(\t|\s{4}){3}' + effect_name + r'.*', line):
                    line = file.readline()
                    if re.match(r'^(\t|\s{3}\s?){4}' + filter_line + r'.*', line):
                        line = file.readline()                      
                        result = "{0}{1}\tif = {{\n\t\tlimit = {{ is_alive = no }}\n\t\t{2} = {{\n\t\t\t{3}\n\t\t\t{4}\n\t\t}}\n\t}}\n}}\n\n".format(result, "character:" + current_ID, effect_name, filter_line.strip(), line.strip())
                line = file.readline()
        line = file.readline()
    
    output.write(result)
    file.close()
    output.close()
        
if __name__ == "__main__":
   main()
