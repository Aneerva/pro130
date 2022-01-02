import csv
data = []
with open ('dataset2.csv','r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
planets_data = data [1:]
for datapoint in planets_data:
    datapoint[2]=datapoint[2].lower()
planets_data.sort(key = lambda planets_data:planets_data[2])
with open ('dataset2sorted.csv','a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planets_data)