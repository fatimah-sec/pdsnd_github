import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months_list=['January', 'February', 'March', 'April', 'May', 'June','All']
days_list=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','All']

def get_filters():
    """
    
    This function asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=str(input("Type one of the listed cities to analyze (chicago, new york , washington) or type the first litter ")).lower()
        if(city=="chicago" or city=="c" or city=="new york" or city=="n" or city=="washington" or city=="w"):
            break
        else:
            print("invaled input\n")
    if (city=="c"):
        city="chicago"
    elif(city=="n"):
        city="new york city"
    elif(city=="w"):
        city="washington"
    elif(city=="new york"):
        city="new york city"


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=str(input("type one of the month to filter by, or type in all\n")).title()
        if month not in months_list:
            print("Please enter a valid month name")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=str(input('Do you want to filter by day? If yes, then type out the day. If not, type in all\n')).title()
        if day not in days_list:
            print('Please enter a valid day')
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    This function Loads data for the specified city and filters (based on user entry) by month and day if applicable.

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nCalculating The Most Common Month of Travel...\n', df['month'].mode() [0])

    # TO DO: display the most common day of week
    print('\nCalculating The Most Common Day of Travel...\n', df['day_of_week'].mode() [0])


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('\nCalculating The Most Common Start Hour of Travel...\n', df['hour'].mode() [0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """ This function Displays statistics on the most popular stations and trip. both the most popular start and end stations"""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nCalculating The Most Popular  Start Station ...\n',df['Start Station'].mode() [0])


    # TO DO: display most commonly used end station
    print('\nCalculating The Most Popular  End Station ...\n',df['End Station'].mode() [0])

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination="From " +df['Start Station'].map(str)+ "  To "+df['End Station']
    print('\nCalculating The Most Popular Combination of Start Station and End Station ...\n',frequent_combination.mode() [0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """ This function Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    print('\nCalculating  Total Travel Time...\n')
    Total_travel_s=df['Trip Duration'].sum()
    Total_travel_m= np.divide(Total_travel_s,60)
    Total_travel_h= np.divide(Total_travel_m,60)
    print('\n Total Travel Time in Seconds... ',Total_travel_s)
    print('\n Total Travel Time in Minutes... ',Total_travel_m)
    print('\n Total Travel Time in hours... ',Total_travel_h)
    


    # TO DO: display mean travel time
    Mean_travel_s=df['Trip Duration'].mean()
    Mean_travel_m=np.divide(Mean_travel_s,60)
    Mean_travel_h=np.divide(Mean_travel_m,60)
    print('\n Mean Travel Time in Seconds... ',Mean_travel_s)
    print('\n Mean Travel Time in Minutes... ',Mean_travel_m)
    print('\n Mean Travel Time in Hours... ',Mean_travel_h)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\ User Types Count...\n')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if ('Gender' not in df):
        print('\n Gender Data is not Available For this City  ...\n')
    else:
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' not in df):
        print('\n Birth Year Data is not Available For this City  ...\n')
    else:
        print('\n The most common year of birth is ....  ',int(df['Birth Year'].mode()))
        print('\n The most earliest year of birth is ....  ',int(df['Birth Year'].min()))
        print('\n The most recent year of birth is ....  ',int(df['Birth Year'].max()))
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def view_data(df):
    """Displays the raw data for the user."""
    Line_num=0
    n=5
    user_input=input('\nWould you like to view raw data? Enter yes or no.\n').lower()
    while user_input =='yes':
        print(df[Line_num:n])
        user_input=input('\nWould you like to view  more Lines? Enter yes or no.\n').lower()
        Line_num=n
        n=Line_num+5
    
    if(user_input !='no'):
        print("Invalude input")
        
        
        
        
        
        
        
        
        
        
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
