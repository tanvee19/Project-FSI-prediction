# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data.csv', delimiter = ',')


# Importing the dataset and intialising the columns
data = pd.read_csv('yearwisedata.csv', delimiter = ',')
list_col=['Country', 'Year', 'Rank', 'Total', 'Security Apparatus',
       'Factionalized Elites', 'Group Grievance','Economy',
       'Economic Inequality', 'Human Flight and Brain Drain',
       'State Legitimacy', 'Services', 'Human Rights',
       'Demographic Pressures', 'Refugees and IDPs',
       'External Intervention']

# Handling country data proper
for i in range(len(data)):
    str1=data['Country'][i].replace(' ','')
    data['Country'][i]=str1.lower()

data.to_csv('data.csv') 
    
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data.csv', delimiter = ',')

# fetching results as per the given country by user and plotting grapgh for it 
country_name=str(input("Enter Country Name >")).lower()
x_axis = data[data['Country']==country_name]['Year']
y_axis = data[data['Country']==country_name]['Total']
plt.plot(x_axis, y_axis, marker='o', color="b", alpha=0.3, markersize=7, label=country_name.upper())
plt.xlabel('Years')
plt.ylabel('FSI Score')
plt.title(country_name.upper()+' FSI Score')
plt.legend()
plt.show()


# Representing the data of particular country and particular year
country_name=str(input("Enter Country Name >")).lower()
year=int(input("Enter Year >"))
list_values = list(data[data['Country']==country_name][data['Year']==year].values[0])
plt.plot(list_col[4:], list_values[4:] , marker='o', color="r", alpha=0.3, linestyle='dashed', label=country_name.upper())
plt.xticks(rotation='vertical')
plt.xlabel('Various Features of FSI')
plt.ylabel('Values')
plt.title(country_name.upper()+' Features support')
plt.legend()
plt.show()


# comparison of two countries FSi Score
country_name_1=str(input("Enter Country Name >")).lower()
country_name_2=str(input("Enter Country Name >")).lower()
x_axis = data[data['Country']==country_name]['Year']
y_axis_1 = data[data['Country']==country_name_1]['Total']
y_axis_2 = data[data['Country']==country_name_2]['Total']
plt.plot(x_axis, y_axis_1, marker='o', color="b", alpha=0.3, linestyle='dashed',label=country_name_1.upper())
plt.plot(x_axis, y_axis_2, marker='o', color="r", alpha=0.3, linestyle='solid',label=country_name_2.upper())
plt.xlabel('Years')
plt.ylabel('FSI Score')
plt.title(country_name_1.upper()+' v/s '+country_name_2.upper()+' FSI Score')
plt.legend()
plt.show()


# comapring the data of particular country and particular year with another name and year 
country_name_1=str(input("Enter First Country Name >")).lower()
year_1=int(input("Enter Year Value >"))
str1=country_name_1.upper()+"("+str(year_1)+")"
country_name_2=str(input("Enter Second Country Name >")).lower()
year_2=int(input("Enter Year Value >"))
str2=country_name_2.upper()+"("+str(year_2)+")"
list_values_1 = list(data[data['Country']==country_name_1][data['Year']==year_1].values[0])
list_values_2 = list(data[data['Country']==country_name_2][data['Year']==year_2].values[0])
plt.plot(list_col[4:], list_values_1[4:], marker='o', color="b", alpha=0.3, linestyle='dashed', markersize=7, label=str1)
plt.plot(list_col[4:], list_values_2[4:], marker='v', color="r", alpha=0.3, linestyle='dashed', markersize=10, label=str2)
plt.xticks(rotation='vertical')
plt.xlabel('Various Features of FSI')
plt.ylabel('Values')
plt.title(country_name_1.upper()+' v/s '+country_name_2.upper()+' Features support')
plt.legend()
plt.show()


