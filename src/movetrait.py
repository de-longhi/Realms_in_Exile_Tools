"""
Script for moving the location of "trait = blood_of_numenor" from inside the date to right before the date. 
The script also removes the "effect" block if necessary.
"""

# Author: Johan de Jongh (github: @de-longhi)

# License: MIT

import re
import sys
import re

def main():
    args = sys.argv
    if (len(args) != 2):
        raise TypeError('Incorrect use of arguments. Uses: "python3 src/filter.py <filepath or buffer of input file>"')
    input_file = args[1]
    
    file = open(input_file, 'r')
    line = file.readline()
    
    result = ""
    
    while line:
        temp = ""
        if re.match(r'^(\s{3}|\s{4}|\t)\d.*', line):
            temp += line
            line = file.readline()
            while not re.match(r'^(\s{3}|\s{4}|\t)}.*', line):
                if re.match(r'^(\s{3}|\s{4}|\t){2}effect = { add_trait = blood_of_numenor_.\s?}.*', line):
                    number_index = re.search(r'\d', line).start()
                    result += "\n"
                    result += "\ttrait = blood_of_numenor_" + line[number_index]
                    result += "\n"
                elif re.match(r'^(\s{3}|\s{4}|\t){2}effect = {$', line):
                    temp2 = line
                    empty_effect_flag = True
                    line = file.readline()
                    while not re.match(r'^(\s{3}|\s{4}|\t){2}}', line):
                        if not re.match(r'^\s*$', line) and not re.match(r'^(\s{3}|\s{4}|\t){3}add_trait = blood_of_numenor_.*', line):
                            empty_effect_flag = False
                            temp2 += line
                        elif re.match(r'^(\s{3}|\s{4}|\t){3}add_trait = blood_of_numenor_.*', line):
                            number_index = re.search(r'\d', line).start()
                            result += "\n"
                            result += "\ttrait = blood_of_numenor_" + line[number_index]
                            result += "\n"
                        line = file.readline()
                    temp2 += line
                    if not empty_effect_flag:
                        temp += temp2
                else: temp += line
                line = file.readline()
            temp += line
            result += temp
        else: result += line
        line = file.readline()
    file.close()
    output = open(input_file, 'w')
    output.write(result)
    output.close()
    
if __name__ == "__main__":
   main()
