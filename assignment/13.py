year = int(input('input a year: '))
month = int(input('input a month [1-12]: '))
day = int(input('input a day [1-31]: '))
if month>=1 and month<=6:
    if day == 31:
        month+=1
        day=-1
        
    day+=1
if month>=7 and month<=12:
    if day==31:
        print('invalid day')
    if day==30:
        month+=1
        day=-1
    day+=1
if month>12:
    month=0
    year+=1
print('The next date is [yyyy-mm-dd]%i-%i-%i '%(year,month,day))