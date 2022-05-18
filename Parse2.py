# Description: This pipeline contains 2 programs which are run in sequence - Parse1.py 
# and Parse2.py. The output of Parse1.py is used by Parse2.py program. 

# Parse2.py: 

# Enter the local file path of the input file in .CSV format (generated from Parse1.py)
inputFile = open("C:\\InputFile2.csv", mode="r")

# Enter the local file path of the output file in .CSV format
outputFile = open("C:\\OutputFile2.csv", "w")

# Enter the Product Name of the specific Gene from the GenBank file
findProduct = "DNA protection during starvation protein"

# This indicates the number of Genes the program will retrieve that are located above 
# the current Gene in the input text file (which is indicated by findProduct variable).
upper = 1

# This indicates the number of Genes the program will retrieve that are located below 
# the current Gene in the input text file (which is indicated by findProduct variable).
lower = 1
#--------------------------------------------------------------------------------------

version1=""
version2=""

outputFile.write("Version,CDS,Product,ProteinId,LocusTag\n")

fileLines = inputFile.readlines()
for i in range(1, len(fileLines)):
	version1=""
	version2=""

	if fileLines[i].find(findProduct) != -1:
		version1 = fileLines[i].split(",")[0]

		for u in range(i - upper, (i-upper) + upper):
			version2 = fileLines[u].split(",")[0]
			if version1 == version2:
				outputFile.write(fileLines[u])
				print(fileLines[u])

		version2 = ""
		print(fileLines[i])
		outputFile.write(fileLines[i])

		for l in range(i + 1, i+lower+1):
			version2 = fileLines[l].split(",")[0]
			if version1 == version2:
				print(fileLines[l])
				outputFile.write(fileLines[l])

outputFile.close()
print("done")