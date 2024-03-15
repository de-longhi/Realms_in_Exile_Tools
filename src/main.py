import re
import os
import sys
def main():
    pass

import re

def filter_lines(input_file, output_file):
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

    filter_lines(input_file, output_file)
    print("Filtered lines have been written to", output_file)


if __name__ == "__main__":
    main()