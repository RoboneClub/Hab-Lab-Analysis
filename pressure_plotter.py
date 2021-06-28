#Pandas is used to open csv files  and convert to lists
import pandas as pd
#Used for making plots
import matplotlib.pyplot as plt
#Library used to do maths
import numpy as np

#Load data to pandas
data = pd.read_csv('data.csv')

#Give time from data
time =  data['Time']
pressure_values = data['Pressure']

#Use len function to find the number of values 
number_of_readings = len(pressure_values)
print(number_of_readings)

#Adds all the values using the sum function numpy and then print it
sum_of_all_pressure_values = np.sum( pressure_values )
print(sum_of_all_pressure_values)

#Add all the number of readings then divide by the number of readings
mean_value_of_the_pressure = sum_of_all_pressure_values / number_of_readings
print(mean_value_of_the_pressure)

#We use np.full to repeat the mean value 968 times to be able to visulise them on the graph
mean_value_of_the_pressure = np.full(shape=number_of_readings, fill_value=mean_value_of_the_pressure)

#We plot the pressure value and label it 
plt.plot( pressure_values, label="pressure")
#We plot the mean value and label it 
plt.plot( mean_value_of_the_pressure, label="mean")

#Put title for the graph
plt.title("HAB-LAB: Pressure's Graph")
#Legend creates the box for the key for the graph
plt.legend()
#Labels the x-axis
plt.xlabel("Number of readings")
#Labels the y-axis
plt.ylabel("Pressure (hPa)")
#Show the graph
plt.show()