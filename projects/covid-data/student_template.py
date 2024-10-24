import sys

import numpy as np
import pandas as pd



def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """

    # your code here
    df = pd.DataFrame(data, columns=['date', 'county', 'state', 'cases', 'deaths'])                  #First, we can use pandas to filter the data by first creating a data frame of the data.
    first_rock_case = df[(df['county'] == 'Rockingham') & (df['state'] == 'Virginia')]               # Once the data frame is created we can filter the data to only show us the data in Rockingham
    first_hburg_case = df[(df['county'] == 'Harrisonburg city') & (df['state'] == 'Virginia')]       # and Harrisonburg Virginia. We can check that the data has been filtered
    print(first_rock_case)                                                                           # to only give us the data we want using the print function.
    print(first_hburg_case)

    rock_case1 = df.loc[[8173], ['date']]                                                           #We can now see the data. We can look at the data using the debug, or look at the printed data
    burg_case1 = df.loc[[1901], ['date']]                                                           # and we can see when the first positive cases for Harrisonburg and Rockingham.
                                                                                                    #We can use the df.loc function to select a specific entry in a specific row and column.
    print("The first positive COVID case in Rockingham County was on", rock_case1 )                 #We can select the row (the numeric value) and the case column to return the date that corresponds with
    print("The first positive COVID case in Harrisonburg was on", burg_case1)                       # the positive case (aka the first time Harrisonburg and Rockingham appear). The answer is then stored
                                                                                                    #in the corresponding print function.
    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """

    # your code here
    df = pd.DataFrame(data, columns=['date', 'county', 'state', 'cases', 'deaths'])                 #First, we can use pandas to filter the data by first creating a data frame of the data.
    rock_case_max = df[(df['county'] == 'Rockingham') & (df['state'] == 'Virginia')]                # Once the data frame is created we can filter the data to only show us the data in Rockingham
    # print(rock_case_max)                                                                          # and Harrisonburg Virginia. We can check that the data has been filtered
    hburg_case_max = df[(df['county'] == 'Harrisonburg city') & (df['state'] == 'Virginia')]        # to only give us the data we want using the print function.
    # print(hburg_case_max)

    #rock_cases = rock_case_max[:, 4]            #select the cases columns from the rockingham and harrisonburg
    #hburg_cases = hburg_case_max[:, 4]          #creating an array for the cases for rockingham and harrisonburg
    #rock_cases_list = rock_cases.tolist()       # so we may iterate through the cases to find the difference
    #hburg_cases_list = hburg_cases.tolist()     # (did not work errored); try pandas method for filtering

    #df_rock_cases = rock_case_max['cases'].tolist()     #This is another method to pull the cases data for Rockingham County and Harrisonburg
    #df_hburg_cases = hburg_case_max['cases'].tolist()   #by specifying the data we wanted to look at (the cases column) and putting them into
                                                         #iterable lists.

    data_rock = np.asarray(rock_case_max['cases'])      #Makw into arrays so that can be put into loops just as we did for the drop-jump assignment.
    data_hburg = np.asarray(hburg_case_max['cases'])    #np.asrray also works.

    #Rockingham
    daily_case_rock = []                                        #create an empty list to hold the new data
    for i in range(1,len(data_rock)):                           #A for loop is used to iterate through the data lists created above
        daily_rock_cases = data_rock[i]-data_rock[i-1]          #To find the new number of daily cases, take second (i-1 gives you this) entry
        daily_case_rock.append(daily_rock_cases)                #minus the first to get the difference between case numbers each day.
                                                                #Then put those values into a new list.

    #Harrisonburg                                               #Repeat all the prior steps used for the Rockingham data for the Harrisonburg data
    daily_case_hburg = []
    for i in range(1,len(data_hburg)):
        daily_hburg_cases = data_hburg[i]-data_hburg[i-1]
        daily_case_hburg.append(daily_hburg_cases)

    max_daily_cases_hburg = max(daily_case_hburg)
    print("The maximum number of daily cases in Harrisonburg is",max_daily_cases_hburg)

    max_index_hburg = np.argmax(daily_case_hburg)
    print(max_index_hburg)

    hburg_case2 = df.loc[[667], ['date']]
    print("In Harrisonburg, the highest number of new cases was on", hburg_case2)

    return

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    #We can use the same set up in question 2 to begin to answer question 3.
    df = pd.DataFrame(data, columns=['date', 'county', 'state', 'cases', 'deaths'])                 #First, we can use pandas to filter the data by first creating a data frame of the data.
    rock_case_max = df[(df['county'] == 'Rockingham') & (df['state'] == 'Virginia')]                # Once the data frame is created we can filter the data to only show us the data in Rockingham
    # print(rock_case_max)                                                                          # and Harrisonburg Virginia. We can check that the data has been filtered
    hburg_case_max = df[(df['county'] == 'Harrisonburg city') & (df['state'] == 'Virginia')]        # to only give us the data we want using the print function.
    # print(hburg_case_max)

    data_rock = np.asarray(rock_case_max['cases'])      #Makw into arrays so that can be put into loops just as we did for the drop-jump assignment.
    data_hburg = np.asarray(hburg_case_max['cases'])    #np.asrray also works.

    #Rockingham
    daily_case_rock = []                                        #To solve this we need to take the data from the loops used in question 2
    for i in range(1,len(data_rock)):                           #and apply it to another loop
        daily_rock_cases = data_rock[i]-data_rock[i-1]
        daily_case_rock.append(daily_rock_cases)

    worst_rock_week = []
    for i in range(len(daily_case_rock)):                         #Using a similar format to question 2. The goal is to sum or take mean of 7 entries of
        rock_week = (daily_case_rock[i:i+7])                      #case data (from the question 2 loops) at a time then add that to a list. The use the
        avg_rock = sum(rock_week)                                 #max function to identify the greatest number of average cases per week. Then use argmax
        worst_rock_week.append(avg_rock)                          #to find the entry number of the case so we can call the corresponding date and print our answer.
                                                                  #[i:i+7] can be used to tell python to look at the first entry to the 7th entry.
                                                                  #this allows us to look the at the first thing in that data set and the 7th thing in the data set.
                                                                  #we can use a for loop to do this throughout the entire data.
    worst_week_rock_max = max(worst_rock_week)
    worst_week_rock_index = worst_rock_week.index(worst_week_rock_max)      #there is actually a way to find the index of a value.
    print(worst_week_rock_index)                                            #you can use the "index()" or "list.index(elmnt)" function

    rock_case3 = df.loc[[669], ['date']]
    print("The worst week for cases in Rockingham County was the week of",worst_rock_week)   #once the index/location is recognized we can use df.loc to call out the date


    #Harrisonburg                                               #Repeat all the prior steps used for the Rockingham data for the Harrisonburg data
    daily_case_hburg = []
    for i in range(1,len(data_hburg)):
        daily_hburg_cases = data_hburg[i]-data_hburg[i-1]
        daily_case_hburg.append(daily_hburg_cases)

    worst_hburg_week = []
    for i in range(len(daily_case_hburg)):
        hburg_week = (daily_case_hburg[i:i+7])
        avg_hburg = sum(hburg_week)
        worst_hburg_week.append(avg_hburg)

    worst_week_hburg_max = max(worst_hburg_week)
    worst_week_hburg_index = worst_hburg_week.index(worst_week_hburg_max)
    print(worst_week_hburg_index)

    hburg_case3 = df.loc[[663], ['date']]
    print("The worst week for cases in Harrisonburg was the week of",hburg_case3)

    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    ##for (date, county, state, cases, deaths) in data:
        ##print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)


