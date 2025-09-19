#code to that copies files form one file to another
with open("sample.txt|", "r") as source_file, open("copy.txt, "w") as dest_file:
    for line in source_file:
       new_File = dest_file.write(line)

print(new_File)
