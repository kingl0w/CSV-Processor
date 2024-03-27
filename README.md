# CSV Processor

## Overview
The CSV Processor is a Python script designed to parse large data sets in multiple .csv files. It pulls every nth line from each .csv file and creates a new .csv file with the combined lines in order. After processing, it deletes the original .csv files, leaving only the combined .csv file.

## Usage
1. Ensure you have the necessary Python packages installed by running `pip install -r requirements.txt`.
2. Run the script in the directory containing your .csv files.
3. When prompted, enter the interval in seconds. The script will select every row that is a multiple of this interval.

## Customization
Feel free to modify the script as needed to suit your specific use case.