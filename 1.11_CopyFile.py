# open both files 
with open('firstfile.txt','r') as firstfile, open('secondfile.txt','a') as secondfile: 
      
    # read content from first file 
    for line in firstfile: 
               
             # append content to second file 
             secondfile.write(line)
print("Copied the contents from first file to second file.")