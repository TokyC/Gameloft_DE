import pandas as pd


# return the passed data frame df after filtering it, removing all data that doesn't have 'filter_value' in column
# 'col_name'.
def filter_on_column(df: pd.DataFrame, col_name: str, filter_value) -> pd.DataFrame:
    """Filter the data frame df on column col_name with the value filter_value.
    """
    return df[df[col_name] == filter_value]


# convert the data frame df into a dictionary where each column in the data frame
# correspond to a key in the dictionary and its value are all the column values.
# e.g.,
# | A | B | ----\   {'A': [1], 'B': [2]}
# | 1 | 2 | ----|
def df_to_dict(df: pd.DataFrame) -> dict:
    """Convert the data frame df into a dictionary where each column in the data frame
    correspond to a key in the dictionary and its value are all the column values.
    """
    dictionary = {}
    for col in df.columns:
        dictionary[col] = df[col].tolist()
    return dictionary


if __name__ == '__main__':
    # load data
    df_1 = pd.read_csv('data1.csv')
    df_2 = pd.read_csv('data2.csv')

    # joining them on user_id
    df = df_1.merge(df_2, on='user_id', how='inner')

    # add day, mount columns from event_date columns
    df['day'] = df['event_date'].apply(lambda x: x.split('-')[2])
    df['month'] = df['event_date'].apply(lambda x: x.split('-')[1])

    # filter the data frame to unique rows based on the user_id
    print(f"Before removing duplicate user_id : {df.shape[0]} lines ")
    df = df.drop_duplicates(subset='user_id', keep='first')
    print(f"After removing duplicate user_id:  {df.shape[0]} lines left\n")

    # store dataframe on local
    print("Storing the Dataframe on local...")
    df.to_csv('cleaned_data.csv', index=False)
    print("Done!")
