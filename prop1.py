import re

def mzerospace(file1, file2):
    file = open(file1, "r")
    text = file.readlines()
    new_file = []
    for line in text:
        if line == "\n" : a = 1
        else:
            line = re.sub(' +',' ',line).strip().replace(" ", ",")
            print (line)
            new_file.append(line + "\n")
    file.close()
    new_f = open(file2, "w")
    new_f.writelines(new_file)
    new_f.close()
    # Code picks one file and turns into file2.
    # Use TXT format for both input and output files...
    # Open the output file as a csv on excel or whatever.