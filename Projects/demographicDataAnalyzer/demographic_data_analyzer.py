import pandas as pd


def calculate_demographic_data():
    # Read data from file
    df = pd.read_csv('adult_data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df.sex == 'Male'].age.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    num_people_with_bd = df.loc[df.education == 'Bachelors'].shape[0]
    total_people = df.shape[0]
    percentage_bachelors = round((num_people_with_bd / total_people) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[df.education.isin(['Bachelors', 'Doctorate', 'Masters'])].shape[0]
    lower_education = df.loc[~(df.education.isin(['Bachelors', 'Doctorate', 'Masters']))].shape[0]

    # percentage with salary >50K
    people_advedu_above50 = df.loc[(df.education.isin(['Bachelors', 'Doctorate', 'Masters'])) & (df.salary == '>50K')].shape[0]
    higher_education_rich = round((people_advedu_above50 / higher_education) * 100, 1)
    people_without_advedu_above50 = df.loc[~(df.education.isin(['Bachelors', 'Doctorate', 'Masters'])) & (df.salary == '>50K')].shape[0]
    lower_education_rich = round((people_without_advedu_above50 / lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week has a salary of >50K?

    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours].shape[0]
    num_people_min_rich = df.loc[(df.salary == '>50K') & (df['hours-per-week'] == min_work_hours)].shape[0]
    rich_percentage = round((num_people_min_rich / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    total_people_country = df.groupby("native-country")["salary"].count()
    rich_each_country = df.loc[df.salary == ">50K"].groupby("native-country")["salary"].count()
    percentage_rich_each_country = (rich_each_country / total_people_country) * 100
    highest_earning_country = percentage_rich_each_country.idxmax()
    highest_earning_country_percentage = round(percentage_rich_each_country.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    df_people_50k_india = df.loc[(df.salary == '>50K') & (df['native-country'] == 'India')]
    top_india_occupation = df_people_50k_india.occupation.value_counts().idxmax()


    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_india_occupation
    }

print(calculate_demographic_data())
