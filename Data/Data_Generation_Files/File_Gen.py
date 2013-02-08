import csv
import random

def data_set(i):
	outfile=open('File_%i.csv'%i,'wb')
	output=csv.writer(outfile)

	output.writerow(['City','Quantity','Product_Code'])
	for j in range(251):
		output.writerow([random.choice(['Cardiff','Swansea','Newport','Bangor']),random.randint(0,200),i])
	outfile.close()

