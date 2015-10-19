import urllib2
import json
import os
import glob
import csv
#from xlsxwriter import Workbook

f = csv.writer(open("test1.csv", "wb+"))
f.writerow(["name", "price"])
def cs(name,value):
	f.writerow([name,value])
#val = ['@Notify_T #BD', '@Notify_T CM', '@Notify_T DB', '@Notify_T EA', '@Notify_T EF', '@Notify_T IO', '@Notify_T AF', '@Notify_T AG',
#        '@Notify_T GO', '@Notify_T IF', '@Notify_T IS', '@Notify_T CF', '@Notify_T TS', '@Notify_T MC', '@Notify_T ST', '@Notify_T TA', '@Notify_T TP' ]

codes=[]
response = urllib2.urlopen('https://www.kimonolabs.com/api/XXXX')
data = json.load(response)

for i in range(2,11):  #bd
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(21,29): #cm
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(29,38): #db
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(38,42):   #ea
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(42,46):  #ef
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(476,482):   #io
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(482,486):     #af
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)
#----
for i in range(486,487):    #ag
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(487,491):   #go
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(565,573):   #if
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(573,581):   #is
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(581,595):   #cf
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(595,599):  #ts
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(599,603):  #mc
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(603,615):  #st
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(615,634):  #ta
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)

for i in range(634,638):  #tp
	name=data["results"]["collection1"][i]["scheme"]["text"]
	value=data["results"]["collection1"][i]["nav"]
	print name
	print value
	cs(name,value)


for csvfile in glob.glob(os.path.join('.', 'test1.csv')):
    workbook = Workbook('new_' + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rb') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()
'''
def val():
	for i in range(10):
		i=data['list']['resources'][i]['resource']['fields']
		l=i['name']
		m=i['price']
		cs(l,m)

#val()

i2=data['list']['resources'][1]
j2=i2['resource']
k2=j2['fields']
l2=k2['name']
m2=k2['price']
print l2
print m2
'''

#print data['name']

#val=[k1,k2]


