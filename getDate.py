from datetime import datetime


def readDate_FromDB(my_date):
    new_date = datetime.strptime(my_date,'%Y-%m-%d %H:%M:%S.%f')
    printDate(new_date)

def createDate_fromNOW(my_date):
    print(my_date.strftime('%a, %d %b %Y %H:%M:%S GMT'))
fixDate('2018-09-24 14:32:17.075185')