import random,csv,datetime

f=open("Holidays_1995.csv","wb")
output=csv.writer(f)
output.writerow(["Id","Start_Date","End_Date","Price"])
for i in range(1000):
    tp=random.choice([1,2,3])
    if tp==1:
        days=random.randint(1,3)
        price=random.randint(100,300)
    if tp==2:
        days=random.randint(7,14)
        price=random.randint(350,1000)
    if tp==3:
        days=random.randint(20,30)
        price=random.randint(1100,2000)

    start_day=random.randint(1,27)
    start_month=random.randint(1,12)
    start_date = datetime.date(1995, start_month, start_day)

    end_date=start_date+datetime.timedelta(days=days)
    output.writerow([i+1,start_date.strftime("%d/%m/%Y"),end_date.strftime("%d/%m/%Y"),price])
f.close()

f=open("Dates_1996.csv","wb")
output=csv.writer(f)
output.writerow(["Id","Start_Date","End_Date"])
prices=[]
for i in range(1000):
    tp=random.choice([1,2,3])
    if tp==1:
        days=random.randint(1,3)
        price=random.randint(150,300)
    if tp==2:
        days=random.randint(7,14)
        price=random.randint(350,1000)
    if tp==3:
        days=random.randint(20,30)
        price=random.randint(1000,2000)

    prices.append(price)
    start_day=random.randint(1,27)
    start_month=random.randint(1,12)
    start_date = datetime.date(1996, start_month, start_day)

    end_date=start_date+datetime.timedelta(days=days)
    output.writerow([i+1,start_date.strftime("%d/%m/%Y"),end_date.strftime("%d/%m/%Y")])
f.close()

f=open("Prices_1996.csv","wb")
output=csv.writer(f)
output.writerow(["Id","Price"])
for i in range(1000):
    output.writerow([i+1,prices[i]])
f.close()
