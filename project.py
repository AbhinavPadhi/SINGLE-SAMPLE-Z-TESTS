import pandas as p
from plotly import figure_factory as ff
import statistics as s
import random
from plotly import graph_objects as go

df = p.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

populationMean = s.mean(data)
population_std_deviation = s.stdev(data)

print("population mean is ", populationMean)
print("population standard deviation is " , population_std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = s.mean(dataset)
    return mean

mean_list = []
for i in range(0,100):
    set_of_means= random_set_of_mean(30)
    mean_list.append(set_of_means)

std_deviation = s.stdev(mean_list)
mean = s.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)

zScore = (mean - populationMean) / std_deviation
print("z score is" , zScore)
