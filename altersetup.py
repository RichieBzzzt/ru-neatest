import sys
print(sys.argv)
fin = open("setup-tokenised.py", "rt")
fout = open("setup.py", "wt")
for line in fin:
  fout.write(line.replace('@@Major@@', sys.argv[1]).replace('@@Minor@@', sys.argv[2]).replace('@@Revision@@', sys.argv[3]))
fin.close()
fout.close()
