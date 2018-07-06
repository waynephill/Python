file = open("teams.txt","r")
outfile=""
for line in range (1,5):
    if line % 2 != 0:
        outfile = outfile + file.readline()
    else:
        file.readline()

file = open("teams.txt","w")
file.write(outfile)
file.close()