import os

database = "database/newOGs_db"

for fasta in os.listdir("ReadyToOGSearch_AA_renamed/"):
	if ".fasta" in fasta:
		print "%s: running..." % fasta
		os.system("blastp -db " + database + " -query ReadyToOGSearch_AA_renamed/" + fasta + " -out " + fasta + " -outfmt 6 -num_threads 8 -evalue 1e-10")
		print "%s: completed" % fasta
