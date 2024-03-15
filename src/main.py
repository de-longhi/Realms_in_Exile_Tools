import re
import os
import sys

import re

input_file = ""
output_file = ""

change_type = ""

effect_name = ""
filter_line = ""

def effect() -> None:
    effect_name = input("Enter the name of the effect you want to check for: ")
    filter_line = input("Enter the exact line you want to search for: ")

def filter_lines() -> None:
    with open(input_file, 'r') as f:
        lines = f.readlines()

    filtered_lines = []
    for i in range(len(lines)):
        #if re.match(r'^\s{3}|\t|$|#', lines[i]):
        if re.match(r'^($|#)', lines[i]):
            pass
        else:
            filtered_lines.append(lines[i])

    with open(output_file, 'w') as f:
        for line in filtered_lines:
            f.write(line)

if __name__ == "__main__":
    input_file = input("Enter the input file path: ")
    if not os.path.exists(input_file):
        print("file does not exist!")
        sys.exit()
    output_file = input("Enter the output file path: ")
    change_type = input("Enter the name of the change you want to filter for: ")
    
    if change_type == "effect":
        effect()

    filter_lines(input_file, output_file)
    print("Filtered lines have been written to", output_file)
