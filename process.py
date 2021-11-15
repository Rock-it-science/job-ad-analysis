import pandas as pd

def process_data():
    '''
    Process raw.csv into processed.csv
    Remove rows with empty content and remove dupliates
    '''

    df = pd.read_csv('raw.csv')
    print(df)

    # Drop duplicates
    df = df.drop_duplicates()
    print(df)

    # Remove where content is empty string
    # Since b'' is hardcoded into the string for some reason, b'' is the actual string value for empty string
    df.drop(df[df['content'] == "b''"].index, inplace=True)
    print(df)

    # Write to processed.csv
    df.to_csv('processed.csv')