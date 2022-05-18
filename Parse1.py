# Description: This pipeline contains 2 programs which are run in sequence: Parse1.py 
# and Parse2.py. The output of Parse1.py is used by Parse2.py program.

# Parse1.py: A single GenBank file is a text file which contains information about 
# multiple Genomes.
# This program parses only those Genomes which contains the Product Name of the Gene 
# which is passed as a parameter in the findProduct variable.
# It generates a .CSV file which contains the following attributes of the Gene: 
# Version, CDS, Product, ProteinId, LocusTag

# Enter the local file path of the input file (GenBank file) in .GB format
inputFile = open("C:\\InputFile1.gb", mode="r")

# Enter the local file path of the output file in .CSV format
outputFile = open("C:\\OutputFile1.csv", "w")

# Enter the Product Name of the specific Gene from the GenBank file
findProduct = "DNA protection during starvation protein"
#--------------------------------------------------------------------------------------

version = ""
cds = ""
product = ""
proteinId = ""
locusTag = ""
twoLines = False

outputFile.write("Version,CDS,Product,ProteinId,LocusTag\n")

fileLines = inputFile.read()
inputFile.close()
records = fileLines.split("//\n")

for recordLine in records:
	counter = 0
	if recordLine.find(findProduct) != -1:
		dataLines = recordLine.split("\n")
		for dataLine in dataLines:
			counter = counter + 1

			#find Version
			if dataLine.startswith("VERSION     "):
				version = dataLine.replace("VERSION     ", "")
			#find Version

			#find CDS, product, protein_id, locus_tag
			twoLines = False
			proteinId = ""
			locusTag = ""
			if dataLine.startswith("     CDS             "):
				cds = dataLine.replace("CDS             ", "")
				cds = cds.replace(",", "#").strip()
				for i in range(counter, len(dataLines)):
					if dataLines[i].startswith("                     /locus_tag="):
						locusTag = dataLines[i].replace('/locus_tag="',"")
						locusTag = locusTag.replace('"', "").strip()

					if dataLines[i].startswith("                     /product="):
						product = dataLines[i].replace('/product="',"")
						product = product.replace(",", "#").strip()
						twoLines = False

						if dataLines[i].endswith("\"") != True:
							product = product + " " + dataLines[i+1].strip()
							twoLines = True

						product = product.replace('"',"")

						if twoLines == True:
							if dataLines[i+2].startswith("                     /protein_id="):
								proteinId = dataLines[i+2].replace("                     /protein_id=","")
						else:
							if dataLines[i+1].startswith("                     /protein_id="):
								proteinId = dataLines[i+1].replace("                     /protein_id=","")

						proteinId = proteinId.replace('"',"")

						break
				print (version + "," + cds + "," + product + "," + proteinId + "," + locusTag)
				outputFile.write(version + "," + cds + "," + product + "," + proteinId + "," + locusTag + "\n")
			#find CDS, product, protein_id, locus_tag

outputFile.close()
print("done")