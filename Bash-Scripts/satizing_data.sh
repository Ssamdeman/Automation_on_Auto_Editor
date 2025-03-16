#!/bin/bash  # 1

# Check if a CSV file was provided as an argument  # 2
if [ -z "$1" ]; then  # 3
    echo "Usage: $0 <path_to_csv_file>"  # 4
    exit 1  # 5
fi  # 6

# Get the CSV file path from the first argument  # 7
CSV_FILE="$1"  # 8

# Check if the CSV file exists  # 9
if [ ! -f "$CSV_FILE" ]; then  # 10
    echo "Error: CSV file does not exist"  # 11
    exit 1  # 12
fi  # 13

# Create a temporary file to store the sanitized CSV file by removing leading/trailing spaces and backslashes  # 14
TEMP_CSV_FILE=$(mktemp)  # 15

# Remove backslashes, leading spaces, and trailing spaces from the CSV file and save the result in the temporary file  # 16
sed 's/\\//g;s/^[[:space:]]*//;s/[[:space:]]*$//' "$CSV_FILE" > "$TEMP_CSV_FILE"  # 17

# Read the sanitized CSV file line by line and print each sanitized file path  # 18
while IFS= read -r FILE_PATH; do  # 19
    # Print the sanitized FILE_PATH for verification  # 20
    echo "Sanitized FILE_PATH: $FILE_PATH"  # 21
done < "$TEMP_CSV_FILE"  # 22

# Save the sanitized paths to a new output CSV file  # 23
OUTPUT_CSV="sanitized_paths.csv"
cp "$TEMP_CSV_FILE" "$OUTPUT_CSV"

# Print confirmation message  # 24
echo "Sanitized file paths have been saved to $OUTPUT_CSV"

# Remove the temporary file after processing  # 25
rm "$TEMP_CSV_FILE"  # 26

