#Pandas is used to open csv files and convert it into lists 
import pandas as pd
#Used for making plots
import matplotlib.pyplot as plt
#Library used to do maths
import numpy as np

#Load data to pandas
data = pd.read_csv('data.csv')

#Give time from data
time =  data['Time']
humidity_values = data['Humidity']

#Use len to function to find the number of value
number_of_readings = len(humidity_values)
print(number_of_readings)

#Adds all the values using the sum function numpy and then print it 
sum_of_all_humidity_values = np.sum( humidity_values )
print(sum_of_all_humidity_values)

#We plot the pressure value and label it
mean_value_of_the_humidity = sum_of_all_humidity_values / number_of_readings
print(mean_value_of_the_humidity)

mean_value_of_the_humidity = np.full(shape=number_of_readings, fill_value=mean_value_of_the_humidity)

#We plot the pressure valuea nd label it 
plt.plot( humidity_values, label="humidity")
#We plot the mean value and label it
plt.plot( mean_value_of_the_humidity, label="mean")

#Put the title for the graph
plt.title("HAB-LAB: Humidity's Graph")
#Legend creates the box for the key for the graph 
plt.legend()
#Labels the x-axis
plt.xlabel("Number of readings")
#Labels the y-axis
plt.ylabel("Relative humidity (%)")
#Show the graph
plt.show()