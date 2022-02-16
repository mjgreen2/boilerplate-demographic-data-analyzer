#Solution to Demographic Data Analyzer project
#Created in Visual Studio Code
#by Michael Green

import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(filepath_or_buffer = "adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race'].value_counts(), None, object)

    # What is the average age of men?
    men = df[df['sex'] == 'Male']
    men_age = men['age']
    average_age_men = round(np.sum(men_age)/np.size(men_age), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bach = pd.DataFrame(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round(np.size(bach['education'])/np.size(df['education']) * 100, 1)
    

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with `Bachelors`, `Masters`, or `Doctorate`
    adv_degree = pd.DataFrame(df[df['education'] == 'Masters'])
    adv_degree = pd.concat([adv_degree, df[df['education'] == 'Bachelors'], df[df['education'] == 'Doctorate']])
    higher_education = np.size(adv_degree['education'])/np.size(df['education']) * 100


    # without `Bachelors`, `Masters`, or `Doctorate`
    no_college = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    lower_education = np.size(no_college['education'])/np.size(df['education']) 


    # percentage with salary >50K
    money_degree =pd.DataFrame(adv_degree[adv_degree['salary'] == '>50K'])
    higher_education_rich = round(np.size(money_degree['salary'])/np.size(adv_degree['salary']) * 100, 1)

    money_no_college = no_college[no_college['salary'] == '>50K']
    lower_education_rich = round(np.size(money_no_college['education'])/np.size(no_college['education']) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours = df['hours-per-week'].min()
    num_min_workers = df[df['hours-per-week'] == min_hours]

    money_min_workers = num_min_workers[num_min_workers['salary'] == '>50K']
    rich_percentage = np.size(money_min_workers['salary'])/np.size(num_min_workers['salary']) * 100

    # What country has the highest percentage of people that earn >50K?
    money_people = df[df['salary'] == '>50K']
    money_list = pd.Series(money_people['native-country'].value_counts(), None, object)
    pop_list = pd.Series(df['native-country'].value_counts(), None, object)
    percent_list = money_list/pop_list
    highest_earner = dict(percent_list[percent_list == percent_list.max()])
    highest_earning_country = list(highest_earner)[0]
    highest_earning_country_percentage = round(highest_earner.get(highest_earning_country) * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    indians = df[df['native-country'] == 'India']
    money_indians = indians[indians['salary'] == '>50K']
    jobs_of_money_indians = pd.Series(money_indians['occupation'].value_counts(), None, object)
    highest_indian_earner = dict(jobs_of_money_indians[jobs_of_money_indians == jobs_of_money_indians.max()])
    top_IN_occupation = list(highest_indian_earner)[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

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
        'top_IN_occupation': top_IN_occupation
    }
