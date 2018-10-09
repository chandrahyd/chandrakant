import datetime
date=input("enter date like (mon dd year)  only:")
newdate=datetime.datetime.strptime(date,'%b %d %Y')
print(newdate.date())
