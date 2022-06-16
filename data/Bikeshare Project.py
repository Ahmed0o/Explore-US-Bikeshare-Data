import time
import pandas as pd
import numpy as np

#preparing data files, lines(6:8)
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

#User Choosing Nickname
Nickname = input('Hello, What is your favorite Nickname?: ')

#Using a message to show if users input is wrong
Wrong = 'Invalid input.  Try again {}.'.format(Nickname.title())

#Filters for easy browsing, lines(17:99)
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi {}, I am your assistant today.'.format(Nickname.title()))
    print("Let\'s explore some US bikeshare data!")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #"""Some Steps:  First i use while to make it easy if user enter wrong input.
    #            Second we can append (.lower) to be sure that (the user input will met our data exactly)."""
    while True:
        city = input('Which city do you need to explore {}?(chicago,new york city,washington): '.format(
            Nickname.title())).lower()
        if city not in CITY_DATA:
            print(Wrong)
        else:
            break

    while True:
        filter = input('Do you need to filter data by month, day, both or (no filter),{}?'.format(
            Nickname.title())).lower()
        if filter == 'month':
            while True:
                # get user input for month (all, january, february, ... , june)
                month = input('Which month do you need to explore {}?(january,february,march,april,may,june) or all: '.format(
                    Nickname.title())).lower()
                months = ['all', 'january', 'february',
                          'march', 'april', 'may', 'june']
                day = "all"
                if month not in months:
                    print(Wrong)
                else:
                    break
            break
        elif filter == 'day':
            while True:
                # get user input for day of week (all, monday, tuesday, ... sunday)
                day = input("Which day do you need to explore {}?(saturday, sunday, monday, tuesday, wednesday, thursday, friday) or all:".format(
                    Nickname.title())).lower()
                days = ['all', 'saturday', 'sunday', 'monday',
                        'tuesday', 'wednesday', 'thursday', 'friday']
                month = 'all'
                if day not in days:
                    print(Wrong)
                else:
                    break
            break
        elif filter == 'both':
            while True:
                # get user input for month (all, january, february, ... , june)
                month = input('Which month do you need to explore {}?(january,february,march,april,may,june) or all: '.format(
                    Nickname.title())).lower()
                months = ['all', 'january', 'february',
                          'march', 'april', 'may', 'june']
                if month not in months:
                    print(Wrong)
                else:
                    break
            while True:
                # get user input for day of week (all, monday, tuesday, ... sunday)
                day = input('Which day do you need to explore {}?(saturday, sunday, monday, tuesday, wednesday, thursday, friday) or all: '.format(
                    Nickname.title())).lower()
                days = ['all', 'saturday', 'sunday', 'monday',
                        'tuesday', 'wednesday', 'thursday', 'friday']
                if day not in days:
                    print(Wrong)
                else:
                    break
            break
        elif filter == 'no filter':
            month = 'all'
            day = 'all'
            break
        else:
            print(Wrong)

    print("your request in progress {} ".format(Nickname.title()))
    print('-'*40)
    return city, month, day


#(load data)function will help to prepare data for user, lines(103,133)
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])
    #convert time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extract month and DOW from time column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #filter by month if needed
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    #create new dataframe for month
        df = df[df['month'] == month]
    #filter by day of week if needed
    if day != 'all':
        #create new dataframe for day of the week
        df = df[df['day_of_week'] == day.title()]

    return df

#Prepare time stats statistics, line(135,153)
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('common month: ', most_common_month)
    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('common day of week: ', most_common_day)
    # display the most common start hour
    most_common_start_hour = (df['Start Time'].dt.hour).mode()[0]
    print('common start hour: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#some station_stats statistics, line(155,174)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("common_start_station: ", common_start_station)
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("common_end_station: ", common_end_station)
    # display most frequent combination of start station and end station trip
    df["combination_of_start_station_and_end_station_trip"] = "Start at: " + df['Start Station'] +", " + "End at: " + df['End Station']
    common_combination_of_start_station_and_end_station_trip = df['combination_of_start_station_and_end_station_trip'].mode()[0]
    print("common_combination_of_start_station_and_end_station_trip: ", common_combination_of_start_station_and_end_station_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#some trip_duration_stats, line(177,193)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time_in_seconds = df["Trip Duration"].sum()
    print("total_travel_time_in_seconds: ", total_travel_time_in_seconds)
    total_travel_time_in_minutes = (total_travel_time_in_seconds / 60)
    print("total_travel_time_in_minutes: ", total_travel_time_in_minutes)
    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("mean_travel_time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#some of user stats, line(195,220)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print(user_type)
    # Display counts of gender
    #one of DataFrames haven't 'Gender','Birth Year' columns , be careful
    if 'Gender' in df:
        gender_type = df['Gender'].value_counts()
        print(gender_type)
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_BY = df['Birth Year'].min()
        print("earliest_BY: ", earliest_BY)
        most_recent_BY = df['Birth Year'].max()
        print("most_recent_BY: ", most_recent_BY)
        most_common_BY = df['Birth Year'].mode()[0]
        print("most_common_BY: ", most_common_BY)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Asking user to show a sample from data, line(222,231)
def show_sample(df):
    while True:
        show_rows = input('Do you like to see 5 rows sample from our data {}.(yes,no)'.format(Nickname.title())).lower()
        if show_rows == 'yes':
            print(df.sample(5))
        elif show_rows == 'no' :
            break
        else:
            print(Wrong)

#Rearranging all functions, line(233,243)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_sample(df)

#If user need to start or not, line(246,254)
        restart = input(
            '\nWould you like to restart? Enter yes or no.\n').lower()
        while restart not in ["no", "yes"]:
            print(Wrong)
            restart = input(
                '\nWould you like to restart? Enter yes or no.\n').lower()
        if restart == 'no':
            print('Nice to meet you {} '.format(Nickname.title()))
            break

if __name__ == "__main__":
    main()
