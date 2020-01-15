#!/usr/bin/env python3

import csv
import datetime
from pprint import pprint

# 1. load input.csv into a variable called `polls`

with open ('input.csv', 'r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	rows = [dict(row) for row in rows] # Convert OrderedDict to regular dict
	polls = [dict(row) for row in rows]

#pprint(polls)

#print(polls)

# 2. write a new file called output.csv and write a row with two headers: "date" and "approve"


with open ('output.csv','w') as f:

	writer = csv.writer(f)
	writer.writerow(['data','approve'])

#	json.dump(polls,f,indent=2)

	# 3. Loop through each row of `polls` 

	myrawstring={}	
	for poll in polls:
		raw_date = poll['enddate']
		approve = poll ['approve']
		print(raw_date)
		print(approve)

		date = datetime.datetime.strptime(raw_date,"%m/%d/%Y")
		print(date)

		print('\n -- ')
		new_date = date.strftime("%d-%b-%y") # https://strftime.org/
		print(new_date)

		writer.writerow ([new_date,approve])	

    # 4. and within that loop... convert the format of `enddate` from "1/22/2017" to "22-Jan-17"
#from datetime import time
    
#	new_date = datetime.datetime.strptime(date,"input format here")
#	new_date1 = date.strftime("insert out put format here")



    # hint: to read the date you will need to use
    #       date = datetime.datetime.strptime(myrawstring, "insert input format here")
    #
    #       and to write the date you will need to use something like 
    #       new_date = date.strftime("insert output format here")
    # 
    #       date formats can be found at https://strftime.org/
    
    #new_date

    # 5. write a new row of data with the transformed date and value for "approve" 




#by. Xiaowen wen and B student. 

