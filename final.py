import csv
from typing import final
final = []
with open ('final.csv','r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        final.append(row)

headers1 = final[0]
headers = final
planets_data = []
for index,datarow in enumerate(planets_data1):
    planets_data.append(planets_data1[index]+planets_data2[index])
with open ('final.csv','a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planets_data)