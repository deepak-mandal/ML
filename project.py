# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xZmwqJsHi0_SmFdmJ6kv8Y3E2GxJtCoF
"""

import pandas
raw_housing_data=pandas.read_csv("/home/deepak/ml/1. Regression - Module - (Housing Prices).csv")
raw_housing_data

raw_housing_data.dtypes

raw_housing_data.head(10)

raw_housing_data.tail(10)

raw_housing_data.describe()

"""raw_housing_data.describe(include=all)"""

raw_housing_data.info()

raw_housing_data["Sale Price"].mean()

raw_housing_data["Sale Price"].min()

raw_housing_data["Sale Price"].max()

raw_housing_data["Sale Price"].std()

raw_housing_data["Sale Price"].quantile(.25)

raw_housing_data["Condition of the House"].unique()

import numpy as np
np.std(raw_housing_data["Sale Price"])

dir(np)

import matplotlib.pyplot as plt
plt.plot(raw_housing_data["Sale Price"])
plt.plot(raw_housing_data["Sale Price"], color="green")
plt.xlabel("Record number")
plt.ylabel("Sale Price")
plt.title("Line graph - sale price on y axis")
plt.show()

plt.plot(raw_housing_data["Sale Price"], marker="o", markerfacecolor="Blue", markersize=5, color="green", linewidth=5, linestyle="dashed")

raw_housing_data.groupby("Condition of the House")["ID"].count()

values=(30, 1701, 14031, 5679, 172)
labels=("Bad", "Excellent", "Fair", "Good", "Okay")
#for building the Pie Chart
plt.pie(values, labels=labels)

#Bar Graph
plt.bar(labels, values, color="Blue")

#Coustimizing the Bar Graph
plt.bar(labels, values, color="Blue", linewidth=5, linestyle="dashed")
plt.xlabel("Condition of the House")
plt.ylabel("Count of the House")
plt.title("Coustimized Bar Graph")
plt.show()

import matplotlib.pyplot as plt
plt.scatter(x=raw_housing_data["Flat Area (in Sqft)"], 
           y=raw_housing_data["Sale Price"], 
           color="red")
plt.xlabel("Area")
plt.ylabel("Selling Price")
plt.title("Selling Price Vs Area")
plt.show()

plt.scatter(x=raw_housing_data["No of Bathrooms"],
           y=raw_housing_data["Sale Price"],
           color="Red")
plt.xlabel("No of Bathrooms")
plt.ylabel("Selling Price")
plt.title("Selling Price Vs No of Bathrooms")
plt.show()

plt.scatter(x=raw_housing_data["Age of House (in Years)"],
           y=raw_housing_data["Sale Price"],
           color="red")
plt.xlabel("Age of House")
plt.ylabel("Selling Price")
plt.title("Selling Price Vs Age of House")
plt.show()

raw_housing_data.describe()

plt.hist(raw_housing_data["Age of House (in Years)"], bins=10)

plt.hist(raw_housing_data["Age of House (in Years)"], bins=10)
plt.xlabel("Age of House (in Years)")
plt.ylabel("No. of Records")
plt.title("Age wise Distribution of Houses")
plt.show()

plt.boxplot(raw_housing_data["Age of House (in Years)"])

import pandas as pd
#To calculate the mean of a column with respect to another column
data=pd.read_csv("/home/deepak/ml/1. Regression - Module - (Housing Prices).csv")
data["Sale Price"].mean()
'''
#Initialising a new column
data["condition_sale"]=0
#calculating mean based on the condition of the House
for i in data["Condition of the House"].unique():
    data["condition_sale"][data["Condition of the House"]==str(i)] = data["Sale Price"][data["Condition of the House"]==str(i).mean()]
    
#Plotting the mean sales based on the condition of the House
plt.figure(dpi=100)
plt.bar(data("Condition of the House").unique(), data["condition_sale"].unique())
plt.xlabel("Condition of the House")
plt.ylabel("Mean Sale Price")
plt.show()
'''
#initilasing a new column
data["zip_condition_sale"]=0
c="Condition of the House"
z="Zipcode"

#Calculating mean based on the condition of the House and zipcode

for i in data[c].unique():
    for j in data[z].unique():
        data["zip_condition_sale"][(data[c]==str(i))&(data[z]==j)] = data["Sale Price"][(data[c]==str(i))&data[z]==j].mean()

        
len(data["zip_condition_sale"].unique())
#print(data["zip_condition_sale"])

zip_condition_sale=data.groupby(["Condition of the House", "Zipcode"])["Sale Price"].mean()
zip_condition_sale

import numpy as np
zipcode_condition_sale2 = pd.pivot_table(data, index=["Condition of the House", "Zipcode"], values=["Sale Price"], aggfunc=np.mean)
zipcode_condition_sale2

#IMPORTANT
zipcode_condition_sale3=pd.pivot_table(data, index=["Zipcode"], columns=["Condition of the House"], values=["Sale Price"], aggfunc=np.mean)
zipcode_condition_sale3

#To find out the plot length from plot area
data["Plot length"] = data["Flat Area (in Sqft)"]**0.5
data["Plot length"].head()

#Calculating total area of the house
data["total_area"] = data["Flat Area (in Sqft)"] + data["Lot Area (in Sqft)"]
data["total_area"].head()

#Brute Force:- Repeating of code

data["Condition of the House"][data["Condition of the House"]=="Fair"] = "1"
data["Condition of the House"][data["Condition of the House"]=="Okay"] = "0"
data["Condition of the House"][data["Condition of the House"]=="Bad"] = "0"
data["Condition of the House"][data["Condition of the House"]=="Good"] = "1"
data["Condition of the House"][data["Condition of the House"]=="Excellent"] = "3"
data["Condition of the House"].unique()

import pandas as pd
data=pd.read_csv("/home/deepak/ml/1. Regression - Module - (Housing Prices).csv")
#Imp. 
#Map function is several times more efficient when compared to the brute force & It helps in reducing the size of the code
data['Condition of the House'] = data['Condition of the House'].map({'Good':'1', 'Excellent':'3', 'Bad':'0', 'Fair':'1', 'Okay':'0'})
data['Condition of the House'].unique()

year=[]
for i in range(len(data["Date House was Sold"])):
    K= data["Date House was Sold"][i].split()[-1]
    year.append(K)
data["Year Sold"] = year
data["Year Sold"].head()

def year(value):
    return value.split()[-1]
data["Year Sold"] = data["Date House was Sold"].map(year)
data["Year Sold"].head()

data["Luxury_home"]=0
for i in range(len(data)):
    count=0
    if data["Waterfront View"][i]=="Yes":
        count=count+1
    if data["Condition of the House"][i] in ["Good", "Excellent"]:
        count=count+1
    if data["Overall Grade"][i] >=8:
        count=count+1
    if count>=2:
        data["Luxury_home"][i]="Yes"
    else:
        data["Luxury_home"][i]="No"
        
data["Luxury_home"].unique()
#Point to be Noted: It is time Consuming

def luxury_home(row):
    count=0
    if row[0]=="Yes":    #Waterfront View
        count=count+1
    if row[1] in ["Good", "Excellent"]:    #Condition of the House
        count=count+1
    if row[2]>=8:    #Overall grade
        count=count+1
    if count>=2:
        return "Yes"
    else:
        return "No"
    
data["Luxury_name"]=data[["Waterfront View", "Condition of the House", "Overall Grade"]].apply(luxury_home, axis=1)
data["Luxury_home"].unique()

#Pandas.apply() function: takes only few Sec.

"""Problem Statement
To build a Linear Regression model to Predict the Sale Price of the house based on its characteristics.

"""

raw_housing_data["Sale Price"].head(10)

raw_housing_data["Sale Price"].tail(10)

raw_housing_data["Sale Price"]

raw_housing_data["Sale Price"].describe()

import matplotlib.pyplot as plt
plt.scatter(x=raw_housing_data["ID"],
           y=raw_housing_data["Sale Price"])

import seaborn as sns
sns.boxplot(x=raw_housing_data["Sale Price"])

q1=raw_housing_data["Sale Price"].quantile(0.25)
q3=raw_housing_data["Sale Price"].quantile(0.75)
iqr=q3-q1
iqr

upper_limit=q3+1.5*iqr    #from mathematical equation for Outlier
lower_limit=q1-1.5*iqr
upper_limit, lower_limit

def limit_imputer(value):
    if value>upper_limit:
        return upper_limit
    if value<lower_limit:
        return lower_limit
    else: 
        return value
    
#For treating outliers
raw_housing_data["Sale Price"] = raw_housing_data["Sale Price"].apply(limit_imputer)

#To check wheather, we actually treated the outlier or not
raw_housing_data["Sale Price"].describe()

import seaborn as sns
sns.boxplot(x=raw_housing_data["Sale Price"])

#Treatment of missing values
raw_housing_data["Sale Price"].describe()

raw_housing_data.info()    #To find how many missing values

raw_housing_data.dropna(inplace=True, axis=0, subset=["Sale Price"])

#For verification
raw_housing_data.info()

#To check how the values are dustributed over the range?
plt.hist(raw_housing_data["Sale Price"], bins=10, color="green")
plt.xlabel("Intervals")
plt.ylabel("Selling Price")
plt.title("Histogram of Selling Price")
plt.show()

len(raw_housing_data["Latitude"].unique())

raw_housing_data.info()

raw_housing_data["Zipcode"].isnull().any()

numerical_columns=["No of Bathrooms", "Flat Area (in Sqft)", "Lot Area (in Sqft)",
                   "Area of the House from Basement (in Sqft)", "Latitude", "Longitude",
                  "Living Area after Renovation (in Sqft)"]

from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan, strategy="median")
raw_housing_data[numerical_columns]=imputer.fit_transform(raw_housing_data[numerical_columns])

raw_housing_data.info()

raw_housing_data.info()

raw_housing_data[447:451]



column=raw_housing_data["Zipcode"].values.reshape(-1, 1)
imputer=SimpleImputer(missing_values=np.nan, strategy="most_frequent")
raw_housing_data["Zipcode"]=imputer.fit_transform(column)
#raw_housing_data["Zipcode"].shape
#column.shape
raw_housing_data.info()

raw_housing_data["Zipcode"].isnull().any()

raw_housing_data.info()

#As It's hard to find any numeric relationship beween zipcode and sale price, So, converted to object data type
raw_housing_data["Zipcode"]=raw_housing_data["Zipcode"].astype(object)

raw_housing_data.dtypes

raw_housing_data["No of Times Visited"].unique()

mapping={"None":"0",
        "Once":"1",
        "Twice":"2",
        "Thrice":"3",
        "Four":"4"}
raw_housing_data["No of Times Visited"]=raw_housing_data["No of Times Visited"].map(mapping)
raw_housing_data["No of Times Visited"].unique()

raw_housing_data["Ever Renovated"]=np.where(raw_housing_data["Renovated Year"]==0, "No", "Yes")

raw_housing_data.iloc[:1,0:]

raw_housing_data["Purchase Year"] = pd.DatetimeIndex(raw_housing_data["Date House was Sold"]).year

#Year since renovation=year of sale - year of renovation
raw_housing_data["Years Since Renovation"]=np.where (raw_housing_data["Ever Renovated"]=="Yes", abs(raw_housing_data["Purchase Year"]-raw_housing_data["Renovated Year"]), 0)
raw_housing_data.head()

raw_housing_data.head()

raw_housing_data.drop(columns=["Purchase Year", "Date House was Sold", "Renovated Year"], inplace=True)

#raw_housing_data.drop(columns=["Ever Renovate"], inplace=True)

raw_housing_data.head()

raw_housing_data.to_csv("transformed_housing_data.csv", index=False)

transformed_housing_data=pd.read_csv("/home/deepak/ml/transformed_housing_data.csv")


#Correlation
import pandas as pd
transformed_housing_data=pd.read_csv("/home/deepak/ml/transformed_housing_data.csv")
transformed_housing_data["Sale Price"].corr(transformed_housing_data["Flat Area (in Sqft)"])


import numpy as np
np.corrcoef(transformed_housing_data["Sale Price"], transformed_housing_data["Flat Area (in Sqft)"])

transformed_housing_data

transformed_housing_data.drop(columns=["ID"])

transformed_housing_data["Flat Area (in Sqft)"].corr(transformed_housing_data["Sale Price"])

transformed_housing_data.drop(["ID"], axis=1).corr()

transformed_housing_data.drop(columns="ID", inplace=True)











from sklearn import preprocessing
scale=preprocessing.StandardScaler()









