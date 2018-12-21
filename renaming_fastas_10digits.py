import os

for taxon in os.listdir("./"):
	if ".fasta" in taxon:
		name = taxon[:10]
		f = open(taxon, "r").readlines()
		fm = []
		for i in f: fm.append(i.strip())
		fn = open("renamed/" + taxon, "w")
		for j in fm:
			if ">" in j:
				j = j.replace(">", "")
				j = name + "_" + j
				j = ">" + j
				fn.write("%s\n" % j)
			else:
				fn.write("%s\n" % j)
