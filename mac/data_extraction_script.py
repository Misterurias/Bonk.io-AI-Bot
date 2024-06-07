import subprocess
import sys

if __name__ == "__main__":
    vidName = input("Name of video: ")

    # Call frame_extraction.py
    subprocess.run([sys.executable, 'frame_extraction.py', vidName])
    
    # Call object_detection.py
    subprocess.run([sys.executable, 'object_detection.py'])
    
    # Call data_extraction.py
    subprocess.run([sys.executable, 'data_extraction.py'])
