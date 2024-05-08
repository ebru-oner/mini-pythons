import pandas as pd
from functools import lru_cache
import sqlite3
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

# use online data

# cache nutritients data
@lru_cache(maxsize=None)
def cache_data():
    try:
        return pd.read_csv('./McDonalds_Menu_Nutritients.csv')
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# create database
@lru_cache(maxsize=None)
def create_db():
    try:
        conn = sqlite3.connect('nutritions.db')
        df = cache_data()
        df.to_sql('NUTRITIONS', conn, if_exists='replace')
        return conn
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# get all data
def get_all_data():
    conn  = create_db()
    if conn is not None:
        return pd.read_sql('SELECT * FROM NUTRITIONS', conn)

# observe the data
def observe_data():
    df = cache_data()
    return df.describe(include='all')

# Find the max sodium content
def get_max_amount(nutrient='Protein'):
    df = cache_data()
    return df.loc[df[nutrient].idxmax()]

# plot by Category/content
def plot_content_per_category():
    df = cache_data()
    plot = sns.swarmplot(x='Category', y='Sodium', data = df)
    plt.setp(plot.get_xticklabels(), rotation=70)
    plt.title('Sodium content')
    plt.show()

def get_menu_item_with_max_content(content):
    df = cache_data()
    observe_values = df[content].describe()
    print(observe_values)
    id_of_max = df[content].idxmax()
    print(id_of_max)
    return df.at[id_of_max, 'Item']
    
def scatter_plot(x_axis, y_axis):
    df = cache_data()
    plot = sns.scatterplot(x=x_axis, y=y_axis, data=df)
    plt.show()

def box_plot(content):
    df = cache_data()
    plot = sns.set_style('whitegrid')
    ax = sns.boxplot(x=df[content])
    plt.show()

print(box_plot('Sugars'))



# It shows the correlation between the two variables, 
#protein and fat. 
#Correlation is a measure of association between two variables 
#and has a value of between negative 1 and plus 1. 
#We see that the points on the scatter plot are closer 
#to a straight line in the positive direction, so we have a 
#positive correlation between the two variables. 