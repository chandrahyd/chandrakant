import datetime
startdate=input("enter startdate like (mon-dd-year):")
enddate=input("enter enddate like (mon-dd-year):")
start=datetime.datetime.strptime(startdate,'%b-%d-%Y')
end=datetime.datetime.strptime(enddate,'%b-%d-%Y')
date_list = [start + datetime.timedelta(days=x) for x in range((end-start).days)]
print(date_list)

