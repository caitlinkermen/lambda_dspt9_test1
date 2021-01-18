def null_count(df):
    # Check a dataframe for nulls and return the number of missing values.
    # Example Input (df = pd.DataFrame)
    # Expected Output (int)
    return df.isna().sum().sum()

#def train_test_split(df, frac):
    # Create a Train/Test split function for a dataframe and returns both the Training and Testing sets. 
    # Frac referes to the precent of data you would like to set aside for training.
    # train_test_split(df, frac=0.2)
    # Expected Output (tuple of two dataframes)
#def randomize(df, seed):
    # Develop a randomization function that randomizes all of a dataframes cells then returns that randomized dataframe. 
    # This function should also take a random seed for reproducible randomization.
    # Example Input (df = pd.DataFrame)
    # randomize(df, seed=101)
    # Expected Output (pd.Dataframe)
#def addy_split(addy_series):
    # Split addresses into three columns (df['city'], df['state'], and df['zip']) - you can use regexes to detect the format and pull out important pieces.
    # Example Input (addy_series = pd.Series) | address | | 890 Jennifer Brooks\nNorth Janet, WY 24785 | 
    # | 8394 Kim Meadow\nDarrenville, AK 27389 | | 379 Cain Plaza\nJosephburgh, WY 06332 | | 5303 Tina Hill\nAudreychester, VA 97036 |
    # addy_split(addy_series)
    # Expected Output (pd.Dataframe)
#def abbr_2_st(state_series, abbr_2_st=True):
    # Return a new column with the full name from a State abbreviation column -> An input of FL would return Florida. 
    # This function should also take a boolean (abbr_2_state) 
    # and when False takes full state names and return state abbreviations. -> An input of Florida would return Fl.
    # Example Input (state_series = pd.Series)
    # abbr_2_st(state_series, abbr_2_st=True)
    # Expected Output (pd.Series)
#@def list_2_series(list_2_series, df):
    # Single function to take a list and dataframe then turn the list into a series and add it to the inputted dataframe as a new column.
#def rm_outlier(df):
    # A 1.5*Interquartile range outlier detection/removal function that gets rid of outlying rows and returns that outlier cleaned dataframe.
def split_dates(date_series):
    # Function to split dates of format "MM/DD/YYYY" into multiple columns 
    # (df['month'], df['day'], df['year']) and then return the same dataframe with those additional columns.
    import pandas as pd
    date_series = pd.to_datetime(date_series,format='%Y-%m-%d')
    df = pd.DataFrame({'Date':date_series})
    df['month'] = df['Date'].dt.month
    df['day'] = df['Date'].dt.day 
    df['year'] = df['Date'].dt.year 
    return df