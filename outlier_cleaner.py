#!/usr/bin/python


import sys
sys.path.append("../outliers/")
import numpy
import matplotlib.pyplot as plt
import pickle
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    res_error = []
    for i in range(len(ages)):
        res_error.append((predictions[i]-net_worths[i])*(predictions[i]-net_worths[i]))
        tp = (ages[i], net_worths[i], res_error[i])
        cleaned_data.append(tp)
    cleaned_data=  sorted(cleaned_data,key=lambda x: x[2])
    turnc_len = int(len(res_error)*0.9)
    cleaned_data = cleaned_data[:turnc_len]
    cleaned_data_list =zip(*cleaned_data)
    print cleaned_data_list
    return cleaned_data

if __name__ == '__main__':

   ages1 = [1,2,3,4,5,6,7,8,9,10]
   pred = [10,30,70,88,99,111,222,444,666,777]
   net = [8,24,77,89,98,114,221,456,678,789]
   out1 = outlierCleaner(pred, ages1, net)
   print out1

