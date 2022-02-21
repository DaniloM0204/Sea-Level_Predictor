import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    y = df["CSIRO Adjusted Sea Level"]
    x = df["Year"]

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    

    # Create second line of best fit
    

    # Add labels and title
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    