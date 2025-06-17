# FreeCodeCamp Data Analysis Projects

This folder contains my solutions for the **FreeCodeCamp Data Analysis with Python Certification**. Each project demonstrates core data analysis skills using Python libraries such as Pandas, NumPy, and Matplotlib/Seaborn.

## Table of Contents

- [Project 1: Demographic Data Analyzer](#project-1-demographic-data-analyzer)
- [Project 2: Mean-Variance-Standard Deviation Calculator](#project-2-mean-variance-standard-deviation-calculator)
- [Project 3: Page View Time Series Visualizer](#project-3-page-view-time-series-visualizer)
- [Setup and Running Projects](#setup-and-running-projects)

---

## Project 1: Demographic Data Analyzer

Analyzes demographic data from `adult_data.csv` to calculate various statistics, including race counts, average age by gender, education percentages, and more.

### Files

- `Projects/demographic_data_analyzer/demographic_data_analyzer.py`
- `Projects/demographic_data_analyzer/adult_data.csv`

### Key Learning Points

- Data loading and initial exploration with Pandas.
- Filtering, grouping, and aggregation of data.
- Conditional logic for data analysis.

---

## Project 2: Mean-Variance-Standard Deviation Calculator

Implements a function to calculate the mean, variance, standard deviation, max, min, and sum of a 3x3 matrix (or a flattened version) using NumPy.

### Files

- `Projects/mean_std_var/stats_calc.py`

### Key Learning Points

- Efficient numerical operations with NumPy arrays.
- Reshaping and flattening arrays.
- Handling `ValueError` for invalid input.

---

## Project 3: Page View Time Series Visualizer

Processes `fcc-forum-pageviews.csv` to create visualizations of daily forum page views, including line plots, bar charts, and box plots.

### Files

- `Projects/Page View Time Series Visualizer/time_series_visualizer.py`
- `Projects/Page View Time Series Visualizer/fcc-forum-pageviews.csv`
- `Projects/Page View Time Series Visualizer/line_plot.png` (generated)
- `Projects/Page View Time Series Visualizer/bar_plot.png` (generated)
- `Projects/Page View Time Series Visualizer/box_plot.png` (generated)

### Key Learning Points

- Time series data handling and cleaning.
- Data visualization with Matplotlib and Seaborn.
- Creating different types of plots to represent trends and distributions.

---

## Setup and Running Projects

To run these projects locally:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/GovindhKishore/fcc-data-analysis-with-python.git
    cd fcc-data-analysis-with-python
    ```
    

2.  **Navigate into the `Projects` directory:**
    ```bash
    cd Projects
    ```

3.  **Install dependencies:**
    It is recommended to use a virtual environment. The required libraries are listed in `requirements.txt` which is located in this directory.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute the main script for each project:**
    -   **Demographic Data Analyzer:** `python demographic_data_analyzer/demographic_data_analyzer.py`
    -   **Mean-Variance-Standard Deviation Calculator:** The `stats_calc.py` file contains a function. You would typically import and call it in another script.
    -   **Page View Time Series Visualizer:** `python "Page View Time Series Visualizer"/time_series_visualizer.py` (This will generate the plot images).
