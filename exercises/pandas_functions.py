import pandas as pd
from functools import lru_cache 

# Using online data

@lru_cache(maxsize=None)
def memoize_data():
    return pd.read_csv("./Electric_Vehicle_Data.csv")

# From the given data set print first and last five
def print_head_and_tail():
    df = memoize_data()
    return df.head(),df.tail()

# Find vehicle with max range
def find_max_range():
    df = memoize_data()
    max_value = df['Electric Range'].max()
    max_range = df[df['Electric Range'] == max_value][['Make','Model','Electric Range']]
    return max_range.drop_duplicates()

# Find vehicle with min range
def find_min_range():
    df = memoize_data()
    df['Electric Range'] = df['Electric Range'].replace(0,None)
    min_value = df['Electric Range'].min()
    min_range = df[df['Electric Range'] == min_value][['Make','Model','Electric Range']]
    return min_range.drop_duplicates()

# Print details of Tesla
def print_details():
    df = memoize_data()
    brand_group = df.groupby('Make')
    tesla_df = brand_group.get_group('TESLA')
    return tesla_df.head(), tesla_df.tail()

# Print total cars per brand
def get_total_cars_per_brand():
    df = memoize_data()
    brand_counts = df['Make'].value_counts()
    return brand_counts

# Find each companies highest range model
def get_highest_ranges():
    df = memoize_data()
    df['Electric Range'] = df['Electric Range'].replace(0,None)
    max_ranges = df.groupby('Make')['Electric Range'].max().sort_values(ascending=False).reset_index(name='Maximum range')
    return max_ranges

# Find average range of each car making company
def get_average_ranges():
    df = memoize_data()
    df['Electric Range'] = df['Electric Range'].replace(0,None)
    avg_ranges = df.groupby('Make')['Electric Range'].mean().sort_values(ascending=False).reset_index(name='Average range')
    return avg_ranges
