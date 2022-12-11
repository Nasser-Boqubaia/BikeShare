import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the city name to analyze, Cities are chicago, new york city, and washington:\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter the month name to filter data, months range from january to june or all:\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day name to filter data, or all:\n")

    print('-'*40)
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
    
    #Load city file
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #extract month and day from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
        
    #filter by month if specif    
    if month != 'all':
    
        #use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]
            
    #filter by day of week if specified
    if day != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
              
            
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month:-
    
    #find the most common month
    mc_month = df['month'].mode()[0]
    mc_month_count = df['month'].value_counts()[mc_month]
    print('Most Frequent month: {} - Count: {}'.format(mc_month, mc_month_count))
    
    
    # TO DO: display the most common day of week:-
    
    #find the most common day
    mc_day = df['day_of_week'].mode()[0]
    mc_day_count = df['day_of_week'].value_counts()[mc_day]
    print('Most Frequent day: {} - Count: {}'.format(mc_day, mc_day_count))
    
    
    # TO DO: display the most common start hour:-
    
    #extract hour from the Start Time to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    #find the most common hour (from 0 to 23)
    mc_hour = df['hour'].mode()[0]
    mc_hour_count = df['hour'].value_counts()[mc_hour]
    print('Most Frequent hour: {} - Count: {}'.format(mc_hour, mc_hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    #find the most common start station
    mc_start = df['Start Station'].mode()[0]
    mc_start_count = df['Start Station'].value_counts()[mc_start]
    print('Most Frequent Start Station: {} - Count: {}'.format(mc_start, mc_start_count))

    # TO DO: display most commonly used end station
    
    #find the most common start station
    mc_end = df['End Station'].mode()[0]
    mc_end_count = df['End Station'].value_counts()[mc_end]
    print('Most Frequent End Station: {} - Count: {}'.format(mc_end, mc_end_count))

    # TO DO: display most frequent combination of start station and end station trip
    
    mc_comb = df[['Start Station', 'End Station']].mode().loc[0]
    print('Most Frequent combination of start station and end station trip: ({}) TO ({})'.format(mc_comb[0], mc_comb[1]))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    #total trip duration
    sum_trip = df['Trip Duration'].sum()
    print('Total trip duration: {}'.format(sum_trip))
    
    # TO DO: display mean travel time
    
    #mean of trip duration
    mean_trip = df['Trip Duration'].mean()
    print('Mean of trip duration: {}'.format(mean_trip))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    #count of user types
    user_count = df['User Type'].value_counts()
    print('Count of user types:\n {}'.format(user_count))

    # TO DO: Display counts of gender
    
    #only access Gender column in case Gender exists in the dataFrame
    if 'Gender' in df:
        #count of user gender
        gender_count = df['Gender'].value_counts()
        print('Count of user gender:\n {}'.format(gender_count))
        
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    
    #only access Birth Year column in case Birth Year exists in the dataFrame
    if 'Birth Year' in df:
        #find earliest birth year
        earliest_year = df['Birth Year'].min()
        print('Earliest birth year: {}'.format(earliest_year))
    
        #find most recent birth year
        recent_year = df['Birth Year'].max()
        print('Most recent birth year: {}'.format(recent_year))
    
        #find most common birth year
        common_year = df['Birth Year'].value_counts().idxmax()
        print('Most common birth year: {}'.format(common_year))
    
    else:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_types(df):
    """Displays statistics on bikeshare users."""
    #For Washington city only because it has no Gender, and Birth Year 
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    #count of user types
    user_count = df['User Type'].value_counts()
    print('Count of user types:\n {}'.format(user_count))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_rows(df):
    
    start_time = time.time()
    
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n").lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc : start_loc + 5])
        start_loc += 5
        view_display = input("Do you wish to continue?: \n").lower()
        view_data = view_display
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
        
def main():
    while True:
        try:
            city, month, day = get_filters()
            
        except Exception as e:
            print("Exception occurred: {}".format(e))
            continue 
        
        
        try:
            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)  
            user_stats(df)
            
            data_rows(df)
            
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
                
        except Exception as e:
            print("Exception occurred: {}".format(e))
            continue 

if __name__ == "__main__":
	main()
