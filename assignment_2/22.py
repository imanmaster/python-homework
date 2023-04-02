def t():
    import datetime
    time = datetime.datetime.now()
    y = time.year
    m = time.month
    d = time.day
    return str(y)+'/'+str(m)+'/'+str(d)


fname = input(('enter your first name : '))
lname = input(('enter your last name : '))
bday = input(('enter your birth day : '))
pnumber = input(('enter your phone number : '))
rtime = input(('enter your registration time : '))
dic = {
    'FirstName': fname,
    'LastName': lname,
    'BirthDate': bday,
    'PhoneNumber': pnumber,
    'Registration Time': rtime
}
if dic['Registration Time'] == '' or dic['Registration'] == None:
    dic['Registration Time'] = t()
print(dic)
