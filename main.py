import pandas as pd
import glob
import os
import re

def extract_number(filename):
    match = re.search(r'_(\d+)\.csv$', filename)
    if match:
        return int(match.group(1))
    else:
        return 0

def main():
    interval = int(input("Enter the interval in seconds: "))
    step = 5 * interval

    csv_files = glob.glob('*.csv')
    csv_files = sorted(csv_files, key=extract_number)

    combined_data = []

    for file in csv_files:
        df = pd.read_csv(file)
        selected_rows = df.iloc[::step]
        combined_data.extend(selected_rows.values.tolist())

    combined_df = pd.DataFrame(combined_data, columns=df.columns)
    combined_df.to_csv('combined.csv', index=False)

    for file in csv_files:
        if file != 'combined.csv':
            os.remove(file)

if __name__ == '__main__':
    main()