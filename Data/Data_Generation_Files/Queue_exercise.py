import random
import csv

data=[('Queue Identifier','Servers','Service Rate','Arrival Rate')]

for i in range(1000000):
	data.append((i + 1,random.randint(1,20),random.triangular(1,10,5),random.triangular(1,10,5)))

#data=[[random.randint(0,100000),random.randint(1,20),random.triangular(1,10,5),random.triangular(1,10,5)] for i in range(10)]



servers=csv.writer(open("queue_servers.csv",'w'))
for row in data:
	r=[row[0],row[1]]
	servers.writerow(r)
arrival_rates=csv.writer(open("queue_arrival_rates.csv",'w'))
for row in data:
	r=[row[0],row[3]]
	arrival_rates.writerow(r)
service_rates=csv.writer(open("queue_service_rates.csv",'w'))
for row in data:
	r=[row[0],row[2]]
	service_rates.writerow(r)
