import sys

#arg1 = sys.argv[1]
#arg2 = sys.argv[2]


arg1 = "inputfile:src/test2.txt"
arg2 = "inputfile:src/test3.txt"

infile=arg1.split(":")[1]
print(infile)

outfile=arg2.split(":")[1]
print(outfile)


'''
fileint_path = infile
filein = open(fileint_path)

fileout_path = outfile
fileout = open(fileout_path, 'w')
try:
    alltext = filein.read( )
    fileout.write(alltext)
finally:
    filein.close()
    fileout.close()
'''

