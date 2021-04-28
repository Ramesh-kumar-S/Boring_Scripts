Day={
     "Monday": {
              "1":"SPM",
              "2":"CC",
              "3":"PEHV",
              "4":"CC",
              "5":"WCN"
            },
     "Tuesday": {
              "1":"WCN",
              "2":"PEHV",
              "3":"SPM",
              "4":"CC",
              "5":"SPM"
            },
     "Wednesday": {
              "1":"PEHV",
              "2":"WCN",
              "3":"CC",
              "4":"SPM",
              "5":"WCN"
            },
     "Thursday": {
              "1":"SPM",
              "2":"WCN",
              "3":"PEHV",
              "4":"CC",
              "5":"PEHV"
            },
     "Friday": {
              "1":"WCN",
              "2":"CC",
              "3":"PEHV",
              "4":"PW",
              "5":"SPM"
            },
    }
day=input("Enter the Day :")
period=input("Enter the Period :")
time=0
if period=="1":
    time = "9.00 - 9.45"
elif period =="2":
    time = "10.00 - 10-45"
elif period =="3":
    time="11.15 - 12.00"
elif period =="4":
    time="12.15 - 1.00"
else:
    time="2.15 - 3.00"
print("Period :",Day[day][str(period)],"\nTime :",time)
