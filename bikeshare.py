import time

import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv', 'new york': 'new_york_city.csv', 'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bike share data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = " "
    while city not in CITY_DATA.keys():
        city = str(input("PLease enter the city ( chicago , new york , washington ) :\n "))
        city = city.lower()
        if city not in CITY_DATA.keys():
            print("\n------------Not accepted choice please enter choice from the next list !------------ \n")


    # get user input for month (all, january, february, ... , june)
    months_name = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = " "
    while month not in months_name.keys():
        month = str(input("PLease enter the month ( all, january , february , march , april , may , june ) all to apply no month filter : \n"))
        month = month.lower()

        if month not in months_name.keys():
            print("\n------------Not accepted choice please enter choice from the next list !------------ \n")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = " "
    while day not in days:
        day = str(input("please enter the day : ( all , monday , tuesday , wednesday , thursday , friday , saturday , sunday )all to apply no month filter : \n"))
        day = day.lower()
        if day not in days:
            print("\n------------Not accepted choice please enter choice from the next list !------------ \n")
    print('-' * 130)
    print(f"The choosen day is ({day.title()}) and The choosen month is ({month.title()}) and your city is ({city.title()})")
    print('-' * 130)
    return city, month, day


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day'] = df['Start Time'].dt.day_name()

    # filter by month if applicables
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_id = months.index(month) + 1

        # filter by month to create the new dataframe
        check_one = df[df['month'] == month_id]
        df = check_one
    # filter by day of week if applicable

    if day != 'all':
        # filter by day of week to create the new dataframe
        check_two = df[df['day'] == day.title()]
        df = check_two
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('-' * 50,"\nCalculating The Most Frequent Times of Travel...\n",'-' * 50)

    start_time = time.time()

    # display the most common month

    # find the most popular month

    popular_month = df["month"].mode()[0]

    print(f"\nMost Popular Start month : ({popular_month})")

    # display the most common day of week

    popular_day = df["day"].mode()[0]

    print(f"\nMost Popular Start day : ({popular_day})")

    # display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df["hour"].mode()[0]

    print(f"\nMost Popular Start Hour : ({popular_hour})")
    print("\n\n\nThis took %s seconds." % (time.time() - start_time))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('-' * 50,"\nCalculating The Most Popular Stations and Trip...\n",'-' * 50)
    start_time = time.time()

    # display most commonly used start station

    popular_start_station = df['Start Station'].mode()[0]

    print(f"\nMost Popular Start Station: ({popular_start_station})")

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print(f"\nMost Popular End Station: ({popular_end_station})")

    # display most frequent combination of start station and end station trip


    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')

    most_frequent_trip = df['Start To End'].mode()[0]

    print(f"\nmost_frequent_trip : ({most_frequent_trip})")

    print("\n\n\nThis took %s seconds." % (time.time() - start_time))



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('-' * 35,"\nCalculating Trip Duration...\n",'-' * 35)
    start_time = time.time()

    # display total travel time
    total_travel_time = round(df['Trip Duration'].sum())
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)

    print(f"\nTotal_travel_time is : ({hour}) hours , ({minute}) minutes and ({second}) seconds.")

    # display mean travel time

    mean_travel_time = round(df['Trip Duration'].mean())
    mins, sec = divmod(mean_travel_time, 60)
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nMean_travel_time is : ({hrs}) hours , ({mins}) minutes and ({sec}) seconds.")
    else:
        print(f"\nmean_travel_time is : ({mins}) minutes and ({sec}) seconds")

    print("\n\n\nThis took %s seconds." % (time.time() - start_time))



def user_stats(df):
    """Displays statistics on bike share users."""


    print('-' * 25,"\nCalculating User Stats...\n",'-' * 25)

    start_time = time.time()

    # Display counts of user types

    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print("user_types :\n\n ", user_types,"\n\n")

    # Display counts of gender
    # print value counts for each user type

    try:
        user_gender = df['Gender'].value_counts()

        print("user_gender :\n\n ", user_gender)
    except:
        print("--------------The Gender not shown  in this file--------------")
    # Display earliest, most recent, and most common year of birth
    try:
        most_recent = int(df['Birth Year'].max())
        earliest = int(df['Birth Year'].min())
        common_year_of_birth = int(df['Birth Year'].mode()[0])
        print(f"\nmost_recent :  ({most_recent})")
        print(f"\nearliest :  ({earliest})")
        print(f"\ncommon_year_of_birth : ({common_year_of_birth})")
    except:
        print("--------------The Birthdays not shown in this file--------------")
    print("\n\n\nThis took %s seconds." % (time.time() - start_time))



def data_show(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        df:
    Returns:
        None.
    """
    choice = ['yes', 'no']
    mychoice = ''
    # counter variable is initialized as a tag to ensure only details from
    # a particular point is displayed
    num = 0
    while mychoice not in choice:

        print('-' * 70,"\nDo you want to show the source of this data? ( Yes OR No )\n",'-' * 70)
        mychoice = input().lower()
        # the raw data from the df is displayed if user opts for it
        if mychoice == "yes":
            pd.set_option("display.max_columns", 200)
            print(df.head())
        elif mychoice not in choice:
            print("\n---------Not accepted choice please choice Yes Or No --------\n")

    # Extra while loop here to ask user if they want to continue viewing data
    while mychoice == 'yes':
        print('-' * 70,"\nDo you want to show more data ? ( Yes OR No )\n",'-' * 70)
        num += 5
        mychoice = input().lower()
        # If user opts for it, this displays next 5 rows of data
        if mychoice == "yes":
            pd.set_option("display.max_columns", 200)
            print(df[num:num + 5])
        elif mychoice != "yes":
            break

        print( "-" * 150)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_show(df)
        restart = input('\nWould you want to search another city ? (Yes Or No).\n')
        if restart.lower() == 'no':
            break
        else:
            print("\n---------Not accepted choice please choice Yes Or No --------\n")

if __name__ == "__main__":
    main()
