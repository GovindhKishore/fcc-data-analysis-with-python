import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress



def draw_plot(slope=None):
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series(range(df['Year'].min(), 2051))  # include 2050
    # Compute the corresponding y values using the regression line formula
    y = slope * x + intercept
    plt.plot(x, y)

    # Create second line of best fit
    df_recent = df.loc[df['Year'] >= 2000]
    slope2, intercept2, *_ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x = pd.Series(range(2000, 2051))  # include 2050
    # Compute the corresponding y values using the regression line formula
    y = slope2 * x + intercept2
    plt.plot(x, y)

    # Add labels and title

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    plt.show()
draw_plot()