import subprocess
import os
import sys
import time


def list_directories(directory_path):
    """ List all directories in the given path.
    Args:
        directory_path (str): The path to the directory to list.
    Returns:
        list: Array of filenames in the directory, or empty list if error occurs
    """
    try: 
    # Check if the directory exists
        if not os.path.isdir(directory_path):
            print(f"Error: The directory '{directory_path}' does not exist.")
            return False
        


        #  # Use 'dir' on Windows, 'ls' on Unix-based systems (macOS, Linux)
        # command = 'dir' if sys.platform == 'win32' else 'ls'
        file_names = os.listdir(directory_path)

        # now make another array with the full path of each file
        full_paths = []
        for file_name in file_names:
            full_path = os.path.join(directory_path, file_name)
            full_paths.append(full_path)
        
        #Testing the full paths AND PRINTING THEM
        count = 0
        for final_full_path in full_paths:
            ##print(f"File {count}{final_full_path}")
            count += 1




        return full_paths


    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    


def cleaned_dictory(raw_path):
    """ Clean the directory path by removing any trailing slashes.
    Args:
        raw_path (str): The raw directory path.
    Returns:
        str: The cleaned directory path.
    """
   # Strip any leading/trailing whitespace
    cleaned_path = raw_path.strip()
   
   # Normalize path separators for the current OS
    cleaned_path = os.path.normpath(cleaned_path)
    
    return cleaned_path




# def testing_list_directories(directory_path, file_names):
#     """ Test the list_directories function. It prints the file names in the directory. The file names are appended to the directory path wiht '/'.
#     so everu file name is a path.
#     Args:
#         directory_path (str): The path to the directory to list.
#         file_names (list): List of file names to print.
#     Returns:
#         list of file names in the directory
#     """
#     # Test with a valid directory
#     print("Testing with a file_names in the arraya: and I can printout the file names")
    
#     # Get list of files in the directory
#     file_names = list_directories(directory_path)
    
#     # Print the file count
#     print(f"Found {len(file_names)} files in {directory_path}")
    
#     # Print each file as a full path
#     for file_name in file_names:
#         full_path = os.path.join(directory_path, file_name)
#         print(full_path)
    
    
#     return True



def automatic_editing(directory_path, list_file_names):
    """ Automatically edit files in the given directory.
    Args:
        directory_path (str): The path to the directory containing files to edit.
        file_names (list): List of file names to edit.
    Returns:
        None
    """
    count = 0
    for file_name in list_file_names:
        full_path = os.path.join(directory_path, file_name)
        #print(f"Editing file: {full_path}")

     # Determine the name of the altered file that will be created
        file_base_name, file_extension = os.path.splitext(file_name)
        altered_file_name = file_base_name + "_ALTERED" + file_extension
        altered_full_path = os.path.join(directory_path, altered_file_name)

        print(f"Editing file: {full_path}")

        try:
            # Run auto-editor command
            subprocess.run(["auto-editor", full_path], check=True)
            
            # Wait for the altered file to be created
            max_wait_time = 300  # 5 minutes timeout
            wait_start_time = time.time()
            
            print(f"Waiting for edited file to be created: {altered_full_path}")
            
            while not os.path.exists(altered_full_path):
                # Check for timeout
                if time.time() - wait_start_time > max_wait_time:
                    print(f"Timeout waiting for: {altered_full_path}")
                    break
                    
                time.sleep(5)  # Wait for 5 seconds before checking again
            
            if os.path.exists(altered_full_path):
                print(f"Finished editing: {full_path}")
                count += 1
            else:
                print(f"Failed to create edited file: {altered_full_path}")
                    
        except subprocess.CalledProcessError as e:
            print(f"Error running auto-editor on {full_path}: {e}")
        except Exception as e:
            print(f"Unexpected error processing {full_path}: {e}")
    
    print(f"Total number of files processed: {count}")
    return None


    

    

if __name__ == "__main__":
    # You can hardcode the path or get it as command line argument
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("\nPlease provide a directory path. "
        'Usage: python3 main.py "<directory_path> (in quotes)"\n')
        sys.exit(1)
    
    if __name__ == "__main__":
    # You can hardcode the path or get it as command line argument
     if len(sys.argv) > 1:
        path = sys.argv[1]
   
    
   
   
    all_file_names = list_directories(cleaned_dictory(path))

    automatic_editing(cleaned_dictory(path), all_file_names)
