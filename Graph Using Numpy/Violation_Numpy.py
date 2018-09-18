import datetime
import matplotlib.pyplot as plt
import numpy as np
import calendar

def GetMonthlyData(s):
    D = {}
    with open(s, 'r') as f:
        for line in f:
            if not line.startswith("INTERSECTION"):
                L = line.split(",")
                date = L[3].split("/")
                month = int(date[0])
                viol = int(L[4])
                if month not in D:
                    D.update({month:viol})
                else:
                    D[month] = D[month] + viol
    return D


def GetWeeklyData(s):
    D = {}
    with open(s, 'r') as f:
        for line in f:
            if not line.startswith("INTERSECTION"):
                L = line.split(",")
                date = L[3].split("/")
                month = int(date[0])
                day = int(date[1])
                year = int(date[2])
                dt = datetime.date(year,month,day)
                wd = dt.weekday()
                viol = int(L[4])
                if wd not in D:
                    D.update({wd:viol})
                else:
                    D[wd] = D[wd] + viol
    return D

def Graphing_Monthly_Data(D):
    print(D)
    months = []
    viols = []
    for month in D:
        months.append(month)
        viols.append(D[month])
    x = np.array(months)
    y = np.array(viols)
    f = np.polyfit(x, y, 12)
    F = np.poly1d(f)
    print("Fitted Linear Function: ", F)
    X = np.linspace(-2, 13)
    Y = F(X)
    plt.plot(x, y, 'bo', X, Y, 'r--')
    plt.xlim(0, 13)
    plt.ylim(50000, 120000)
    plt.legend(['DATA POINTS', 'FITTED CURVE '])
    plt.xlabel('MONTHS (EACH DATA POINTS REPRESENT A MONTH. POINT 0 IS SUNDAY, 1 IS MONDAY AND SO ON )')
    plt.ylabel('NUMBER OF SPEEDING TICKET ')
    plt.grid()
    plt.show()

def Graphing_Weekly_Data(D):
    print(D)
    months = []
    viols = []
    for month in D:
        months.append(month)
        viols.append(D[month])
    x = np.array(months)
    y = np.array(viols)
    f = np.polyfit(x, y, 7)
    F = np.poly1d(f)
    print("Fitted Linear Function: ", F)
    X = np.linspace(-15,15)
    Y = F(X)
    plt.plot(x, y, 'bo', X, Y, 'r--')
    plt.xlim(0, 7)
    plt.ylim(50000, 120000)
    plt.legend(['Data POINTS', 'FITTED CURVE '])
    plt.xlabel('WEAKDAYS (EACH DATA POINTS REPRESENT A WEAKDAY.POINT 0 IS SUNDAY, 1 IS MONDAY AND SO ON )')
    plt.ylabel('NUMBER OF SPEEDING TICKET ')
    plt.grid()
    plt.show()

def main():
    Data = GetMonthlyData("C://Users//Jayakumar//Downloads//Red_Light_Camera_Violations.csv")
    Graphing_Monthly_Data(Data)
    Data = GetWeeklyData("C://Users//Jayakumar//Downloads//Red_Light_Camera_Violations.csv")
    Graphing_Weekly_Data(Data)
main()