# Video Editor CLI Tool

A Python-based batch video editing tool that automatically processes multiple video files using the `auto-editor` command-line tool. This tool removes silent parts from videos automatically and processes entire directories of video files in one go.

## Prerequisites

### 1. Install Auto-Editor

First, you need to install the `auto-editor` tool. Visit the official installation guide:

**🔗 [Auto-Editor Installation Guide](https://github.com/WyattBlue/auto-editor)**

Follow the installation instructions for your operating system (Windows, macOS, or Linux).

### 2. Download the Script

Download the `v2_main.py` file and save it to your computer.

## How to Use

### Step 1: Prepare Your Video Directory

1. Create a folder containing all the video files you want to process
2. Make sure all files are video formats (`.mp4`, `.avi`, `.mov`, `.mkv`, etc.)
3. Copy the full path of this directory

### Step 2: Get Directory Path

**On Windows:**
1. Open File Explorer
2. Navigate to your video folder
3. Click on the address bar
4. Copy the full path (e.g., `C:\Users\YourName\Videos\MyVideos`)

**On macOS/Linux:**
1. Open Finder/File Manager
2. Navigate to your video folder
3. Right-click and select "Copy Path" or use terminal command `pwd`
4. Copy the full path (e.g., `/Users/YourName/Videos/MyVideos`)

### Step 3: Run the Script

Download this python code: https://github.com/Ssamdeman/Automation_on_Auto_Editor/blob/main/v2_main.py

Open your terminal/command prompt and run:

```bash
python3 v2_main.py "/path/to/your/video/directory"
```

**Examples:**

Windows:
```bash
python3 v2_main.py "C:\Users\YourName\Videos\MyVideos"
```

macOS/Linux:
```bash
python3 v2_main.py "/Users/YourName/Videos/MyVideos"
```

### Step 4: Wait for Processing

The script will:
1. Scan the directory for video files
2. Show you how many videos were found
3. Process each video file automatically
4. Create new files with `_ALTERED` suffix
5. Show progress and completion status

## Example Output

```
Found 3 video files in directory
  1. presentation.mp4
  2. meeting_recording.mov
  3. tutorial.avi

Starting batch processing of 3 video files...

Processing file 1/3: presentation.mp4
Waiting for edited file to be created: presentation_ALTERED.mp4
✓ Successfully processed: presentation.mp4

Processing file 2/3: meeting_recording.mov
Waiting for edited file to be created: meeting_recording_ALTERED.mov
✓ Successfully processed: meeting_recording.mov

Processing file 3/3: tutorial.avi
Waiting for edited file to be created: tutorial_ALTERED.avi
✓ Successfully processed: tutorial.avi

=== Processing Complete ===
Total video files processed successfully: 3/3
```

## Important Notes

- **Original files are preserved** - The script creates new files with `_ALTERED` suffix
- **Automatic skip** - Files already containing `_ALTERED` in their name will be skipped
- **Video formats supported**: `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`, `.flv`, `.webm`, `.m4v`, `.3gp`, `.ogv`, `.ts`, `.mts`, `.m2ts`, `.vob`
- **Processing time** - Each video may take several minutes depending on file size
- **Timeout** - The script waits up to 5 minutes for each file to be processed

## Troubleshooting

**Error: "auto-editor command not found"**
- Make sure auto-editor is properly installed and available in your system PATH

**Error: "Directory does not exist"**
- Double-check the directory path is correct and in quotes

**No video files found**
- Ensure your directory contains supported video file formats
- Check that files don't already have `_ALTERED` in their names

## Requirements

- Python 3.6 or higher
- Auto-editor installed and configured
- Video files in supported formats

---

**Happy editing! 🎬**
