# FreeCodeCamp Data Analysis with Python

<<<<<<< HEAD
Compiling my work for the FreeCodeCamp Data Analysis with Python Certification, this repository includes completed projects and supplementary learning resources. It should be noted that certain learning materials, specifically Jupyter Notebooks within designated folders (notebooks), are direct extractions from the FreeCodeCamp course content, used herein for educational demonstration and appropriate citation.

## Table of Contents

- [Projects](#projects)
- [Learning Resources / Notebooks](#learning-resources--notebooks)
- [Setup and Installation](#setup-and-installation)
- [Contact](#contact)
=======
This folder contains my solutions for the **FreeCodeCamp Data Analysis with Python Certification**. Each project demonstrates core data analysis skills using Python libraries such as Pandas, NumPy, and Matplotlib/Seaborn.

## Table of Contents

- [Project 1: Page View Time Series Visualizer](#project-3-page-view-time-series-visualizer)
- [Project 2: Demographic Data Analyzer](#project-1-demographic-data-analyzer)
- [Project 3: Mean-Variance-Standard Deviation Calculator](#project-2-mean-variance-standard-deviation-calculator)

- [Setup and Running Projects](#setup-and-running-projects)
>>>>>>> 9125475 (Initial commit from pycharm)

---
## Project 1: Page View Time Series Visualizer

<<<<<<< HEAD
## Projects
=======
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

## Project 2: Demographic Data Analyzer
>>>>>>> 9125475 (Initial commit from pycharm)

This directory (`Projects/`) contains the main certification projects required by FreeCodeCamp. Each project addresses a specific data analysis challenge, demonstrating skills in data manipulation, visualization, and statistical computation.

* **[Access Projects README here for details](Projects/README.md)**

<<<<<<< HEAD
    * Demographic Data Analyzer
    * Mean-Variance-Standard Deviation Calculator
    * Page View Time Series Visualizer
=======
- `Projects/demographic_data_analyzer/demographic_data_analyzer.py`
- `Projects/demographic_data_analyzer/adult_data.csv`
>>>>>>> 9125475 (Initial commit from pycharm)

## Learning Resources / Notebooks

<<<<<<< HEAD
This section holds various materials used for learning and practising data analysis concepts.

* **`notebooks/`**: Contains Jupyter Notebooks related to the topics mentioned below, which are directly extracted from the Data Analysis with Python FCC Course.
* **`JupyterNotebooks/`**: Contains Jupyter Notebooks used for exploration, learning, and demonstrations of data analysis concepts.
* **`NumPy/`**: Exercises and examples specifically focused on the NumPy library.
* **`Pandas/`**: Exercises and examples specifically focused on the Pandas library.

---

## Setup and Installation

To set up and run the code in this repository:
=======
- Data loading and initial exploration with Pandas.
- Filtering, grouping, and aggregation of data.
- Conditional logic for data analysis.

---

## Project 3: Mean-Variance-Standard Deviation Calculator

Implements a function to calculate the mean, variance, standard deviation, max, min, and sum of a 3x3 matrix (or a flattened version) using NumPy.

### Files

- `Projects/mean_std_var/stats_calc.py`

### Key Learning Points

- Efficient numerical operations with NumPy arrays.
- Reshaping and flattening arrays.
- Handling `ValueError` for invalid input.

---

## Setup and Running Projects

To run these projects locally:
>>>>>>> 9125475 (Initial commit from pycharm)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/GovindhKishore/fcc-data-analysis-with-python.git
    cd fcc-data-analysis-with-python
    ```
    

<<<<<<< HEAD
2.  **Install dependencies (for the main projects):**
    The core projects (in the `Projects/` directory) have their dependencies listed in `requirements.txt`.
    ```bash
    cd Projects
    pip install -r requirements.txt
    cd .. # Go back to the root if you want to explore other folders
    ```
    *Note: It is highly recommended to use a [Python virtual environment](https://docs.python.org/3/library/venv.html) to manage dependencies.*

## Contact

Feel free to reach out if you have any questions or feedback.

* Your Name - [govindhkishore7@gmail.com](govindhkishore7@gmail.com)
* Project Link: [https://github.com/GovindhKishore/fcc-data-analysis-with-python](https://github.com/GovindhKishore/fcc-data-analysis-with-python)
=======
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
    -   **Page View Time Series Visualizer:** `python "Page View Time Series Visualizer"/time_series_visualizer.py` (This will generate the plot images).
    -   **Demographic Data Analyzer:** `python demographic_data_analyzer/demographic_data_analyzer.py`
    -   **Mean-Variance-Standard Deviation Calculator:** The `stats_calc.py` file contains a function. You would typically import and call it in another script.
    
>>>>>>> 9125475 (Initial commit from pycharm)
