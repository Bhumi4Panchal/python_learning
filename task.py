import time
timestamp = time.strftime("Date is %B %dth %Y%n Time is %H/%M/%S") #time.strftime is method
print(timestamp)
timestamp = time.strftime('%H')
print("Hours is :",timestamp)
timestamp = time.strftime('%M')
print("Minute is :",timestamp)
timestamp = time.strftime('%S')
print("Second is :",timestamp)
