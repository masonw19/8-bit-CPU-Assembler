import re

# initalize some stuff
j       = 0
ramFull = 16  # CPU only has 16 bytes of RAM so can have maximum of 16 instructions in text file

# create an empty bin file
def fileCreate(fileName):
    f = open(fileName + ".bin", "wb")
    f.close()

# write to output file  
def writeFile(fileName, data): 
    f = open(fileName + ".bin", "ab")
    f.write(bytearray(data))
    f.close()

# 'main'
fileName = input("Enter text file name: ")       # ask for the file name

fileCreate(fileName)                             # create an output file

rf = open(fileName + ".txt", "r")                # open the input file for reading

# split the file into a list for each line. Each line is an array of its strings
for line in rf:
    # ignore comments
    if line[0] == '#':
        continue
    line = line.replace('\n', '').replace('\r', '').replace('\t', ' ') # replace new line symbols
    tok = re.split(r'[, ]', line)     

    #print (str(tok))

    if '' in tok:
        tok.remove('')

    # write the data to the .bin file
    if tok[0].lower() == "lda":
        x       = int(tok[1])
        data    = [0x10 | x]  
        
        writeFile(fileName, data)
    elif tok[0].lower( ) == 'hlt':
        data    = [0xf0]

        writeFile(fileName, data)
    elif tok[0].lower() == 'invb':
        data    = [0xb0]

        writeFile(fileName, data)
    elif tok[0].lower() == "add":
        x       = int(tok[1])
        data    = [0x90 | x]  
        
        writeFile(fileName, data)
    elif tok[0].lower() == "outa":
        data    = [0xe0]  
        
        writeFile(fileName, data)
    elif tok[0].lower() == "and":
        x       = int(tok[1])
        data    = [0x80 | x]  
        
        writeFile(fileName, data)
    elif tok[0].lower() == "or":
        x       = int(tok[1])
        data    = [0xa0 | x]  
        
        writeFile(fileName, data)
    elif tok[0].lower() == "sub":
        x       = int(tok[1])
        data    = [0xd0 | x]  
        
        writeFile(fileName, data)
    elif tok[0].lower() == "sta":
        x       = int(tok[1])
        data    = [0x20 | x]  
        
        writeFile(fileName, data)
    elif tok[0].lower() == "mova":
        x       = int(tok[1])
        data    = [0x30 | x]  
        
        writeFile(fileName, data)
    elif tok[0].lower() == "ina":
        x       = int(tok[1])
        data    = [0x30 | x]  
        
        writeFile(fileName, data)
    elif tok[0].lower() == "jmp":
        x       = int(tok[1])
        data    = [0x40 | x]  
        
        writeFile(fileName, data)
    elif tok[0].lower() == "jc":
        x       = int(tok[1])
        data    = [0x50 | x]  
        
        writeFile(fileName, data)
    else:
        data    = 0x00

        writeFile(fileName, data)
    
    j+=1
    if j == ramFull:
        print("ram is full")
        break

print("SUCCESS: output is in '" + fileName + ".bin'" )