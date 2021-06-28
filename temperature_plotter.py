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
sesnor_temperature_values = data['Temperature']

#Finds us the real tempreature because tempreature in the readings are higher maybe because the sensors might heat up  
real_temperature_values = np.add(sesnor_temperature_values, -6)

#Use len function to find the number of values 
number_of_readings = len(real_temperature_values)
print(number_of_readings)

#Adds all the values using the sum function numpy and then print it
sum_of_all_temperature_values = np.sum( real_temperature_values )
print(sum_of_all_temperature_values)

#Add all the number of readings then divide by the number of readings
mean_value_of_the_temperature = sum_of_all_temperature_values / number_of_readings
print(mean_value_of_the_temperature)

#We use np.full to repeat the mean value 968 times to be able to visulise them on the graph
mean_value_of_the_temperature = np.full(shape=number_of_readings, fill_value=mean_value_of_the_temperature)

#We plot the pressure value and label it 
plt.plot( real_temperature_values, label="temperature")
#We plot the mean value and label it 
plt.plot( mean_value_of_the_temperature, label="mean")

#Put title for the graph
plt.title("HAB-LAB: temperature's Graph")
#Legend creates the box for the key for the graph
plt.legend()
#Labels the x-axis
plt.xlabel("Number of readings")
#Labels the y-axis
plt.ylabel("Temperature (˚C)")
#Show the graph
plt.show()


