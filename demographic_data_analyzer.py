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
    percentage_bachelors = round(np.size(bach['education'])
                            /np.size(df['education']) * 100, 1)
    

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with `Bachelors`, `Masters`, or `Doctorate`
    adv_degree = pd.DataFrame(df[df['education'] == 'Masters'])
    adv_degree = pd.concat([adv_degree, 
                            df[df['education'] == 'Bachelors'], 
                            df[df['education'] == 'Doctorate']])
    higher_education_percentage = (np.size(adv_degree['education'])
                                    /np.size(df['education']) * 100)


    # without `Bachelors`, `Masters`, or `Doctorate`
    no_college = df[(df['education'] != 'Bachelors') 
                    & (df['education'] != 'Masters') 
                    & (df['education'] != 'Doctorate')]
    lower_education_percentage = (np.size(no_college['education'])
                                    /np.size(df['education']))


    # percentage with salary >50K
    rich_degree =pd.DataFrame(adv_degree[adv_degree['salary'] == '>50K'])
    higher_education_rich = round(np.size(rich_degree['salary'])
                                    /np.size(adv_degree['salary']) * 100, 1)

    rich_no_college = no_college[no_college['salary'] == '>50K']
    lower_education_rich = round(np.size(rich_no_college['education'])
                                    /np.size(no_college['education']) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    total_min_workers = pd.DataFrame(df[(df['hours-per-week'] 
                                            == min_work_hours)], 
                                            columns=['salary'])
    rich_min_workers  = pd.DataFrame(total_min_workers[
                                    total_min_workers['salary'] == '>50K'], columns=['salary'])
    rich_percentage = (np.size(rich_min_workers['salary'])
                        /np.size(total_min_workers['salary']) 
                        * 100)

    # What country has the highest percentage of people that earn >50K?
    rich_people = df[df['salary'] == '>50K']
    country_rich_pop = pd.Series(rich_people['native-country'].value_counts(),                              None, object)
    country_total_pop = pd.Series(df['native-country'].value_counts(), 
                                    None, object)
    country_rich_percentage = country_rich_pop/country_total_pop
    highest_earner = country_rich_percentage[country_rich_percentage == country_rich_percentage.max()]
    highest_earning_country = highest_earner.index[0]
    highest_earning_country_percentage = round(highest_earner.get(highest_earning_country) * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    rich_indians = pd.DataFrame(df[(df['native-country'] == 'India') 
                    & (df['salary'] == '>50K')], columns=['occupation']).value_counts(sort=True)
    top_IN_occupation = rich_indians.idxmax()[0]
    
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
