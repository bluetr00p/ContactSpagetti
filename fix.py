import glob
import os

searchTerm = os.getcwd() + "/import/*.vcf"
files = glob.glob(searchTerm)

output = open("SuperContact.vcf", "a")

#open the files
for file in files:
    contact = open(file) #load file 
    content = contact.read() #read file
    
    content = content.replace("VERSION:2.1", "VERSION:3.0") #make into icloud readable format

    for line in content:
        output.write(line)
    contact.close()

output.close()