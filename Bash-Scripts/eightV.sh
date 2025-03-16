#!/bin/bash

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
# Initialize a counter variable  # 14
count=$((count=0))

 #Open a new file descriptor for standard input
exec 3<&0

# Read the CSV file line by line  # 14
while IFS= read -r raw_one_file_path; do  # 15

    # Reset IFS to default just in case it has been modified  # 16
    IFS=""
    
    #TODO: TEST : echo "Processing file: $raw_one_file_path"  # 17

    one_file_path="$raw_one_file_path"  
    #echo
    #TODO: TEST : echo "Cleaned Processing file: $one_file_path"  # 20
    #echo

    # Check if the file exists. Since the the modified version of file will be  # 20
    # Extract the base name without the .MP4 extension and append _ALTERED.MP4  # 20 
    ALTERED_FILE="${raw_one_file_path%.MP4}_ALTERED.MP4"  # 21
    
    #TODO: TEST echo "Altered file: $ALTERED_FILE"  # 22
    # if the file exist, skip the next path  # 23
    if [ -f "$ALTERED_FILE" ]; then  # 24
        echo
        echo "File already exists: $ALTERED_FILE"  # 25
        echo 
        continue  # 26
    fi  # 27


    #confirmation yes or no to run the auto-editing script  # 28
    echo
    echo -n "Do you want to run auto-editor on \"$one_file_path\"? (yes/no): "
    read user_input <&3
    echo
    if [ "$user_input" != "yes" ]; then  # 29
        echo "Skipping file: $one_file_path"  # 30
        continue  # 31
    else  # New else block
        echo
        echo "Editing file: $one_file_path"  # New echo statement for clarity
        echo
        # Add your auto-editing command here
        auto-editor "$one_file_path"  # New auto-editor command
    fi  # 32
    #waiting for 5 seconds and check if the file is created  # 33
    
    #create a while loop to check if the file is created once file crated then exit the loop then move to the next file # 34
    while [ ! -f "$ALTERED_FILE" ]; do  # 35
        sleep 5  # 36
    done  # 37
    
    IFS=""


    count=$((count+1))
   

done < "$CSV_FILE"  # 38

echo "Total number of files processed: $count"  # 39



**
#use the read command instead of IFS. 
# #!/bin/bash

# # Check if a file was provided as an argument
# if [ -z "$1" ]; then
#     echo "Usage: $0 <path_to_file>"
#     exit 1
# fi

# # Get the file path from the first argument
# FILE="$1"

# # Check if the file exists
# if [ ! -f "$FILE" ]; then
#     echo "Error: File does not exist"
#     exit 1
# fi

# # Read the file line by line without modifying IFS
# while read -r line; do
#     # Process each line
#     echo "Processing line: $line"
#     # Add your processing logic here
# done < "$FILE"



**