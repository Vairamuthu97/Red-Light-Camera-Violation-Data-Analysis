from datetime import datetime 

def ExtractData(x):
    L = []
    with open (x,'r') as f:
        for line in f:
            if not line.startswith('INTERSECTION'):
                line = line.replace('\n',"")
                A = line.split(',')
                Date = A[3]
                Violations = int(A[4])
                L.append([Date,Violations])
    return L

def updatingData(Data):
    L = []
    for i in range(len(Data)-1):
        date = Data[i+1][0]
        VIO = Data [i+1][1]
        L.append([date,VIO])
    return L

def groupByMonth(pairs):
  sums = {}
  for pair in pairs:
    mmyy = datetime.strptime(pair[0], '%m/%d/%Y').strftime('%m/%Y')
    sums.setdefault(mmyy, 0)
    sums[mmyy] += pair[1]
  return sums.items()

def getWeekday(sDate):
    import calendar
    date = datetime.strptime(sDate, '%m/%d/%Y')
    return calendar.day_name[date.weekday()]

def groupByWeekDays(pairs):
  wkDaysums = {}
  for pair in pairs:

    
    wkDay = getWeekday(pair[0])

    # For each Year and each WeekDays uncommand the following 2 line
    yr = datetime.strptime(pair[0], '%m/%d/%Y').strftime('%Y')    
    wkDay = yr + "-"  + wkDay

    # # For each year and each month and each WeekDays uncommand the following 2 line
    # mmyy = datetime.strptime(pair[0], '%m/%d/%Y').strftime('%m/%Y')
    # wkDay = mmyy + "-"  + wkDay

    # wkDaysums.setdefault(wkDay, 0)
    # wkDaysums[wkDay] += pair[1]
  return wkDaysums.items()

def writeToNewFile(s,predate):
    predate =  sorted(predate,key=lambda x:datetime.strptime(x[0], '%m/%d/%Y'),reverse=True)
    sortByMon = groupByMonth(predate)
    sortByWeekDay = groupByWeekDays(predate)
    with open (s, 'w')  as f:
        f.write("DATE      | Violations \n")
        for itm in sortByMon:
            f.write(itm[0] + "|" + str(itm[1])+"\n")

    with open ("WeekDay_" + s, 'w')  as f:
        f.write("DATE      | Violations \n")
        for itm in sortByWeekDay:
            f.write(itm[0] + "|" + str(itm[1])+"\n")

def main ():
    redlight = "Red_Light_Camera_Violations.csv"
    Data = ExtractData(redlight)
    predate = updatingData(Data)
    writeToNewFile("DATA2.0.txt",predate)
    
main()

