import subprocess
import os
import sys
import time


def list_video_files(directory_path):
    """ List all video files in the given directory.
    Args:
        directory_path (str): The path to the directory to list.
    Returns:
        list: Array of video file paths in the directory, or empty list if error occurs
    """
    
    # Define supported video file extensions
    video_extensions = {
        '.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', 
        '.m4v', '.3gp', '.ogv', '.ts', '.mts', '.m2ts', '.vob',
        '.MP4', '.AVI', '.MOV', '.MKV', '.WMV', '.FLV', '.WEBM',
        '.M4V', '.3GP', '.OGV', '.TS', '.MTS', '.M2TS', '.VOB'
    }
    
    try: 
        # Check if the directory exists
        if not os.path.isdir(directory_path):
            print(f"Error: The directory '{directory_path}' does not exist.")
            return []
        
        # Get all files in the directory
        all_files = os.listdir(directory_path)
        
        # Filter for video files only
        video_files = []
        for file_name in all_files:
            file_extension = os.path.splitext(file_name)[1]
            if file_extension in video_extensions and "_ALTERED" not in file_name:
                full_path = os.path.join(directory_path, file_name)
                # Only add if it's actually a file (not a directory)
                if os.path.isfile(full_path):
                    video_files.append(file_name)
                
        
        print(f"Found {len(video_files)} video files in directory")
        for i, video_file in enumerate(video_files, 1):
            print(f"  {i}. {video_file}")
        
        return video_files

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def cleaned_directory(raw_path):
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


def automatic_editing(directory_path, video_file_names):
    """ Automatically edit video files in the given directory.
    Args:
        directory_path (str): The path to the directory containing files to edit.
        video_file_names (list): List of video file names to edit.
    Returns:
        None
    """
    if not video_file_names:
        print("No video files found to process.")
        return None
    
    print(f"\nStarting batch processing of {len(video_file_names)} video files...")
    
    count = 0
    for file_name in video_file_names:
        full_path = os.path.join(directory_path, file_name)
        
        # Determine the name of the altered file that will be created
        file_base_name, file_extension = os.path.splitext(file_name)
        altered_file_name = file_base_name + "_ALTERED" + file_extension
        altered_full_path = os.path.join(directory_path, altered_file_name)

        print(f"\nProcessing file {count + 1}/{len(video_file_names)}: {file_name}")

        try:
            # Run auto-editor command
            subprocess.run(["auto-editor", full_path, "--no-open"], check=True)
            
            # Wait for the altered file to be created
            max_wait_time = 300  # 5 minutes timeout
            wait_start_time = time.time()
            
            print(f"Waiting for edited file to be created: {altered_file_name}")
            
            while not os.path.exists(altered_full_path):
                # Check for timeout
                if time.time() - wait_start_time > max_wait_time:
                    print(f"Timeout waiting for: {altered_file_name}")
                    break
                    
                time.sleep(5)  # Wait for 5 seconds before checking again
            
            if os.path.exists(altered_full_path):
                print(f"✓ Successfully processed: {file_name}")
                count += 1
            else:
                print(f"✗ Failed to create edited file: {altered_file_name}")
                    
        except subprocess.CalledProcessError as e:
            print(f"✗ Error running auto-editor on {file_name}: {e}")
        except Exception as e:
            print(f"✗ Unexpected error processing {file_name}: {e}")
    
    print(f"\n=== Processing Complete ===")
    print(f"Total video files processed successfully: {count}/{len(video_file_names)}")
    return None


if __name__ == "__main__":
    # Get directory path from command line argument
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("\nPlease provide a directory path.")
        print('Usage: python3 main.py "<directory_path>"')
        print('Example: python3 main.py "/home/user/videos"')
        sys.exit(1)
    
    # Clean the directory path
    clean_path = cleaned_directory(path)
    
    # Get list of video files in the directory
    video_files = list_video_files(clean_path)
    
    # Process the video files
    automatic_editing(clean_path, video_files)