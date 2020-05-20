#!/usr/bin/env python3

import sys
import numpy
import glob, subprocess
from Bio import SeqIO

# python MyCode.py input_user input_ref (file or GB whole DB)
# index are: python [0] -in [2] -ref [4]
#  this is to import the module with argv


output_blast = open("blast_results.txt", "w") # creating output file

# try/except to read input file fasta from user
try:
	input_user = SeqIO.to_dict(SeqIO.parse(sys.argv[2], "fasta"))
except:
	print("Missing Input file") # in case of missing input file in the commandline this message will be print out
	sys.exit(1)


input_ref = sys.argv[4]

try:
	if input_ref.casefold() == "default":
		#input_ref = XXXXXXX # Here i need to load whole GB database
		print("BLasting your seqs vs default dataset")
	else:
		subprocess.call("/path/to/blast_install/bin/makeblastdb -in " + input_ref + " -dbtype nucl -out " + input_ref + "_ref_db" , shell=True)
		#pass
except:
	print("Missing Reference DB") # in case of missing input file in the commandline this message will be print out
	sys.exit(1)


for x in input_user:
	output_blast.write(input_user[x].id + "\n")
	output_blast.write(str(input_user[x].seq) + "\n")


#input_user.close()
#output_blast.close()
