# [] create The Weather

import os

os.system("curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt")

mean_temps_file = open('mean_temp.txt', 'a+')
mean_temps_file.write("RIO de Janeiro, Brazil, 30.0,18.0\n")

mean_temps_file.seek(0)

headings = mean_temps_file.readline()

headings_list = headings.strip().split(',')

##print(headings_list)

my_name = "Ben Reed"

print(my_name)

city_temp_line = mean_temps_file.readline()

while city_temp_line:
    city_temp_list = city_temp_line.strip().split(',')

    if len(city_temp_list) > 3:
        city_name = city_temp_list[0]
        highest_avg_temp = city_temp_list[3]

        print(f"City of {city_name} month ave: Highest high is {highest_avg_temp} Celsius")
    city_temp_line = mean_temps_file.readline()

mean_temps_file.close()
