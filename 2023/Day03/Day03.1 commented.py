allow = False
sum_part_numbers = []

def all_symbols():
    with open('2023/Day03/input.txt', 'r') as f:
        symbols = ''
        for line in f:
            for chr in line.strip():
                if not (chr.isdigit() or chr == '.'):
                        if chr not in symbols:
                            symbols += chr
        return(symbols)


with open('2023/Day03/input.txt', 'r') as f:
    symbols = all_symbols()
    print(symbols)
    lines = f.readlines()
    for i in range(0, len(lines)):
        #print('LINE NUMBER',i+1)
        line = lines[i]
        if i < len(lines)-1:
            nextline = lines[i+1]
        if i > 0:
            prevline = lines[i-1]
        part_number = ''
        for index, item in enumerate(line):
            if item.isdigit():
                part_number += item             
            elif len(part_number) > 0:
                #print(part_number) #Put check for symbols instead of this line
                
                # Check to the right
                if item in symbols:
                    allow = True
                
                # Check to the left
                if line[index-len(part_number)-1] in symbols:
                    allow = True
                
                # Check for symbols below
                #print(nextline[index])
                if nextline[index] in symbols:
                    allow = True
                for digit in range(len(part_number)+1):
                    if i < len(lines)-1:
                        if nextline[index-digit-1] in symbols:
                            allow = True
                # Check for symbols above
                for digit in range(len(part_number)+2):
                    if i > 0:
                        if prevline[index-digit] in symbols:
                            allow = True

                if allow:
                    sum_part_numbers.append(part_number)
                part_number = ''
                allow = False
sum = 0
for valid in sum_part_numbers:
    sum += int(valid)        
#print(sum_part_numbers)        
print(sum)
    
    

    
    






