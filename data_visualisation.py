import pandas as pd 
%matplotlib inline
import matplotlib.pyplot as plt
import calendar
from numpy import arange

plt.boxplot(top100_yr2010)

# AUSTRALIAN EMISSION DATAFRAME 
Aus_Population = {'1990':17065100, '2000':19153000, '2007':20827600,
                 '2008':21249200,'2009':21691700,'2010':22031750,
                 '2011':22340024, '2012':22728254, '2013':23117353}
population = pd.Series(Aus_Population)

Aus_Emission = {'1990':15.45288167, '2000':17.20060983, '2007':17.86526004,
                '2008':18.16087566,'2009':18.20018196,'2010':16.92095367,
                '2011':16.86260095, '2012':16.51938578, '2013':16.34730205}

co2_Emission = pd.Series(Aus_Emission)
australia = pd.DataFrame({'co2_emission':co2_Emission, 'Population':population})
# print first 10 rows
countries.head(10)

# COUNTRIES FILE
# create a DataFrame from a csv file
countries = pd.read_csv('data/countries.csv',encoding = 'ISO-8859-1')
countries.set_index('Region')

# Sorting Countries by Region then Income
#group by region first
countries_by_region = countries.groupby('Region') # creates a groupby object (abstract)
print("The size of each region group is:")
print(countries_by_region.count())

# group by income too
print("The size of each region group AND income group is:")
countries_by_region_by_income = countries.groupby(['Region', 'IncomeGroup'])
print(countries_by_region_by_income.count())
# bar chart 
countries = ['Burundi','Ethiopia','Rep of Congo','Switzerland','Norway','Luxembourg']
gnp = [90,110,110,49600,51810,56380] # GNP per capita (2004)
plt.bar(arange(len(gnp)),gnp)
plt.xticks( arange(len(countries)),countries, rotation=30)
plt.show()
# clustered bar chart (smaller sample for demonstration)
countries = ['Afghanistan', 'Albania', 'Algeria', 'Angola']
births = [1143717, 53367, 598519, 498887]
deaths = [529623, 16474, 144694, 285380]
plt.bar(arange(len(births))-0.3, births, width=0.3)
plt.bar(arange(len(deaths)),deaths, width=0.3,color='r')
plt.xticks(arange(len(countries)),countries, rotation=30)

# EMISSION FILE
# create a new DataFrame for the CO2 emission from a csv file
emission = pd.read_csv('data/emission.csv',encoding = 'ISO-8859-1')
yr2010 = emission['2010']
names  = emission['Country']
yr2010.index = names
yr2010_sorted = yr2010.sort_values(ascending = False)
top100_yr2010 = yr2010_sorted[0:100]

# IRIS FILE
iris=pd.read_csv('data/iris.csv',encoding = 'ISO-8859-1',header=None)
setosa=iris.loc[iris[4]=='Iris-setosa']
versicolor=iris.loc[iris[4]=='Iris-versicolor']
virginica=iris.loc[iris[4]=='Iris-virginica']
# scatter plot 
plt.scatter(setosa.iloc[:,2],setosa.iloc[:,3],color='green')
plt.scatter(versicolor.iloc[:,2],versicolor.iloc[:,3],color='red')
plt.scatter(virginica.iloc[:,2],virginica.iloc[:,3],color='blue')
plt.xlim(0.5,7.5)
plt.ylim(0,3)
plt.ylabel("petal width")
plt.xlabel("petal length")
plt.grid(True)

# AGES - histograms
ages = [17,18,18,19,21,19,19,21,20,23,19,22,20,21,19,19,14,23,16,17]
plt.hist(ages, bins=10)
plt.grid(which='major', axis='y')
plt.show()