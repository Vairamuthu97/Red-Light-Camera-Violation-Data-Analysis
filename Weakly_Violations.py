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
                   D.update({month:viol/4.0}) #data ranges over 4 years, so we take the average
                else:
                   D[month] = D[month] + viol/4.0
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
                wd =  dt.weekday()

                viol = int(L[4])
                if wd not in D:
                   D.update({wd:viol/4.0}) #data ranges over 4 years, so we take the average
                else:
                   D[wd] = D[wd] + viol/4.0
    return D      
                
def LinearDataFitAndPlot(D):
    print(D)
    months = []
    viols = []
    for month in D:
        months.append(month)
        viols.append(D[month]) 
        
    x = np.array(months)
    y = np.array(viols)
    f = np.polyfit(x, y, 5) 
    F = np.poly1d(f)
    print("Fitted Linear Function: ", F)          
    X = np.linspace(-5, 15, 70) 
    Y = F(X)
    plt.plot(x, y, 'bo', X, Y, 'r--')
    plt.xlim(0, 13)
    plt.ylim(50000, 120000)
    plt.legend(['data points', 'fitted curve F(X)'])
    plt.xlabel('months')
    plt.ylabel('number of speed violations')
    plt.grid() 
    plt.show()

def LinearDataFitAndPlotWeekDays(D):
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
    X = np.linspace(-5, 15, 70) 
    Y = F(X)
    plt.plot(x, y, 'bo', X, Y, 'r--')
    plt.xlim(0, 13)
    plt.ylim(50000, 120000)
    plt.legend(['data points', 'fitted curve F(X)'])
    plt.xlabel('Weakdays')
    plt.ylabel('number of speed violations')
    plt.grid() 
    plt.show()


def main():
    Data = GetMonthlyData("Red_Light_Camera_Violations.csv")
    LinearDataFitAndPlot(Data)

    Data = GetWeeklyData("Red_Light_Camera_Violations.csv")
    LinearDataFitAndPlotWeekDays(Data)    
main()