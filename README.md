# Red-Light-Camera-Violation-Data-Analysis
For this project I want to extract the date and the corresponding number of red light violations in the City of Chicago and do a linear regression on the data, using NumPy. The data is contained in the 50.2 MB file Red_Light_Camera_Violations.csv Since the file is bigger, I could not upload the Raw File, However,obtained from the City of Chicago's Data Portal (https://data.cityofchicago.org/). This file contains data from July 1, 2014 to November 1,2017. 

In this project my goal is to analysis the follwing two problems:

Problem 1)  Extract the number of violations for each month of the year. Denote the months of the year numerically.
            That is, let 1 stand for January, 2 for February, ..., and 12 for December.
            Create two NumPy arrays for the months (X) and the number of red light violations (Y). 
            Write a generic linear function ax+b and then fit the data to that function, using the appropriate NumPy functon. 
            Your final report for Problem 1 should include the code you used and a plot of the data, as points, and the graph of the fitted function, 
            all in one single plot. For plotting, you should use MatPlotLib but you can also use any other Python-related plotting tool.

Problem 2)  Extract the number of violations for each day of the week. Denote the days of the week numerically.
            That is, let 1 stand for Monday, 2 for Tuesday, ..., and 7 for Sunday.
            Create two NumPy arrays for the days (X) and the number of red light violations (Y). 
            Fit the data with a degree 7 polynomial, using the appropriate NumPy functon. 
            Your final report for Problem 2should include the code you used and a plot of the data, as points, and the graph of the fitted function, 
            all in one single plot. For plotting, you should use MatPlotLib but you can also use any other Python-related plotting tool.