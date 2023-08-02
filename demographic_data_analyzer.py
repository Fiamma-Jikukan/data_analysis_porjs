import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.

    race_count = df['race'].value_counts()
    print(race_count)

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    num_of_batch = len(df.loc[df['education'] == 'Bachelors'])
    total_num = len(df)
    percentage_bachelors = ((num_of_batch / total_num ) * 100)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    all_adv_edu = df.loc[(df['education'] == 'Bachelors' ) | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    all_none_adv_edu = df.loc[(df['education'] != 'Bachelors' ) & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]

    higher_education = len(all_adv_edu)
    lower_education = len(all_none_adv_edu)


    # percentage with salary >50K
    all_adv_edu_more_50K = all_adv_edu.loc[all_adv_edu['salary'] == '>50K']
    num_of_all_adv_edu_more_50K = len(all_adv_edu_more_50K)

    all_none_adv_edu_more_50K = all_none_adv_edu.loc[all_none_adv_edu['salary'] == '>50K']
    num_of_all_none_adv_edu_more_50K = len(all_none_adv_edu_more_50K)

    higher_education_rich = (num_of_all_adv_edu_more_50K / higher_education) * 100
    lower_education_rich = (num_of_all_none_adv_edu_more_50K / lower_education) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours = df['hours-per-week'].min()
    all_min_hours_more50K = len(df.loc[(df['hours-per-week'] == min_hours) & (df['salary'] == '>50K')])
    num_min_workers = len(df.loc[df['hours-per-week'] == min_hours])

    rich_percentage = (all_min_hours_more50K / num_min_workers ) * 100

    # What country has the highest percentage of people that earn >50K?
    num_each_country = df.loc[:, ['native-country']].value_counts()
    sal_by_country_k = df.loc[df['salary'] == '>50K', ['native-country']].value_counts()
    tryinghard = pd.DataFrame({'total': num_each_country, 'rich': sal_by_country_k})
    tryinghard['rich'] = tryinghard['rich'].astype('Int64')
    presenage = (tryinghard['rich'] / tryinghard['total'] ) * 100

    highest_earning_country = presenage.dropna().sort_values(ascending=False).index[0][0]
    highest_earning_country_percentage = presenage.dropna().sort_values(ascending=False)[0]

    # Identify the most popular occupation for those who earn >50K in India.
    indifo = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India') , ['occupation']].value_counts()

    top_IN_occupation = indifo.index[0][0]

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

calculate_demographic_data()