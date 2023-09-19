import csv 
from datetime import datetime 

# 1. Processing as a simple text file
# acc_file = open('accounts.csv')
# lines = acc_file.readlines()
# for line in lines:
#     data = line.split(',')
#     print(data)

# 2. Proessing as CSV file with lists
# acc_file = open('accounts.csv')
# csv_reader = csv.reader(acc_file, delimiter=',')
# for row in csv_reader:
#     print(row)

acc_file = open('accounts.csv')
dict_reader = csv.DictReader(acc_file)
current_date = datetime.now()
for row in dict_reader:
    if row['plan'] != 'free':
        print(row['expire_date'])
        exp_date = datetime.strptime(row['expire_date'], "%Y-%m-%d")
        print(exp_date)
        print(exp_date.isoweekday())
        if exp_date < current_date:
            print("EXPIRED")
