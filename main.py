import os
import numpy as np
import matplotlib.pylab as plt
import csv
import logging
import time

from fp_tree_node import *
from fp_growth import *

# Setting up a logger
logger = logging.getLogger()  # Initiating a logger
logging.basicConfig(filename="logs.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger.setLevel(logging.DEBUG)


# To begin with FP growth Algorithm, first we need to fetch the transactional data

transactions = []  # Initiliazing a list to store the transactions from csv file

# For "Adults" dataset(https://archive.ics.uci.edu/dataset/2/adult) fetched from UCI benchmark datasets

input_dataset_path = "datasets/Adult/adult.csv"  # Input dataset path

# For each type of input dataset, we need to store the respective outputs in separate folders
outputs_path = "outputs/Adult/Frequent_Items"

# Creating output folder, if it doesnt exist
try:
    logger.info("---------------Creating Outputs folder---------------")
    os.makedirs(outputs_path)
    logger.info("---------------Outputs Folder created---------------")
except FileExistsError as e:
    logger.info("!!Output Folder already exists!!")
    pass

# Reading input CSV dataset and converting it into transactional data

logger.info("---------------Reading Input Data---------------")
try:
    with open(input_dataset_path) as input_data:
        for row in csv.reader(input_data):
            transactions.append(row)
except Exception as e:
    logger.error(e)
logger.info("---------------Transactional Data formed---------------")

"""
Upon manual inspection of the input data, there are several data entry points with unwanted characters such as "?" and single quotes('"')
For missing data points, data points are stored as either ""(empty values) or "?" in the dataset which bring no value. 
Hence it crucial to clean the data before using FP Growth algorith to mine frequent patterns.

"""

logger.info("---------------Performing Data Cleaning---------------")
try:
    for item in transactions:
        item = list(filter(lambda x: x != '', item))
        for i in item:
            if '?' in i:
                item.remove(i)
            if '"' in i:
                i = i.replace('"', '')
except Exception as e:
    logger.error(e)

logger.info("---------------Data Cleaning Complete---------------")
logger.info("Total number of transactions from Dataset: %s ",
            int(len(transactions)))

# Finding maximum number of attributes present in the transactional dataset

maximum_number_of_attributes = 0
for transaction in transactions:
    if maximum_number_of_attributes < len(transaction):
        maximum_number_of_attributes = len(transaction)

logger.info("Maximum number of attributes present in the dataset : %s",
            maximum_number_of_attributes)

"""

Since there are around 32k transactions in the dataset and the minimum_support is not defined in the question, let us keep a list of minimum_support values

"""
# List of minimum support valeus to test FP Growth Algorithm

minimum_support = [100,200,500,700,1000,2000,5000,10000,15000]

# Since we are running the algorithm multiple times, we are storing the time taken for the algorithm to complete and memory used for each threshold value for analysis

time_taken = {}
memory_used = {}


for threshold in minimum_support:
    frequent_itemsets = []
    start_time = time.time()
    for itemset, support in mine_frequent_itemsets(transactions, threshold):
        frequent_itemsets.append((itemset, support))
        print(frequent_itemsets)
        print("--------------------------")

