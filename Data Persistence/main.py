# my_file = open("my-file.txt", "r+")
# by_lines = my_file.readlines()
# print(by_lines)
# for line in by_lines:
#    print(line.removesuffix("\n"))
    
# print(by_lines)

# people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

input_file_path = 'names.txt'
output_file_path = 'name_counts.txt'

# Read the input file and count the occurrences of each name
name_counts = {}
name = ""

try:  
    with open("repeated-names.txt", "r") as my_file:
        for line in my_file:
            name = line.strip()
            if name:
                if name in name_counts:
                    name_counts[name] += 1
                else:
                    name_counts[name] = 1


except FileNotFoundError as fnfe:
    print(fnfe)
finally:
    my_file.close
    
# Write the counts to the output file
with open(output_file_path, 'w') as file:
    for name, count in name_counts.items():
        file.write(f'Name: {name}, Count: {count}\n')