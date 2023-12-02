stacks = {1:['Z','N','D','-'],2:['M','C','-','-'],3:['P','-','-','-']}
#subroutine to get last item
def getStackLast():
    last_item = ""
    for stack in stacks:
        last_item += stacks[stack][-1]
    return last_item
#open file
myfile = open("instructions.txt", "r")
instructions = myfile.readlines()
for line in instructions:
    line = line.replace("move","").replace("from ","").replace("to ","").strip().split()
    line = [int(i) for i in line]
    crates = line[0]
    from_crate = line[1]
    to_crate = line[2]
    for crate in range (crates):
        crate_removed = stacks[from_crate].pop()
        stacks[to_crate].append(crate_removed)
        print(stacks)
print(getStackLast())