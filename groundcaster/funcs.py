from pathlib import Path
import pandas as pd


# Function to load data
def load_data(file_path: str | Path, prefix: str) -> list[pd.DataFrame]:
    """
    Load and concatenate CSV files from a directory into a DataFrame.

    This function reads all CSV files in the specified directory that match the provided prefix,
    parses the "Date" column into datetime format with day first, and concatenates the data into a single DataFrame.

    Args:
        file_path (str|Path): The directory path where the CSV files are located.
        prefix (str): The prefix of the CSV files to be loaded.

    Returns:
        list[pd.DataFrame]: A list of DataFrames of all matched CSV files.

    """
    return [
        pd.read_csv(p, parse_dates=["Date"], dayfirst=True)
        for p in Path(file_path).glob(f"{prefix}*.csv")
    ]
