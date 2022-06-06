"""
Load datasets
"""
import pandas as pd


def load_data(filename: str):
    """
    Reads and prepares data for the analysis
    Args:
        filename(str): File path for the dataset

    Returns:
        pd.DataFrame
    """
    if filename.endswith('.csv'):
        df = pd.read_csv(filename)

        df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
        df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)

    elif filename.endswith('.parquet'):
        df = pd.read_parquet(filename)

    # Calculate trip duration
    df['duration'] = df.lpep_dropoff_datetime - df.lpep_pickup_datetime
    df.duration = df.duration.apply(lambda td: td.total_seconds() / 60)

    # Filter the data
    df = df[(df.duration >= 1) & (df.duration <= 60)]

    # Selecet numerical and categorical variables
    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].astype(str)

    return df

