import cv2
import os
import json
import sys

def extract_frames(video_name):
    video_path = f'/Users/papijorge/Movies/BonkGameplay/{video_name}.mp4'

    # Create a directory to save the frames
    frames_dir = 'frames'
    os.makedirs(frames_dir, exist_ok=True)

    # Create a subdirectory for the current video
    video_frames_dir = os.path.join(frames_dir, video_name)
    os.makedirs(video_frames_dir, exist_ok=True)

    # Check if frames already exist
    existing_frames = [f for f in os.listdir(video_frames_dir) if f.endswith('.png')]
    if existing_frames:
        print(f"Frames already exist in {video_frames_dir}. Skipping extraction.")
    else:
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Error: Could not open video file {video_path}")
            return

        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            # Save the frame as an image file in the subdirectory
            frame_path = os.path.join(video_frames_dir, f'frame_{frame_count:04d}.png')
            cv2.imwrite(frame_path, frame)
            frame_count += 1

        cap.release()
        cv2.destroyAllWindows()

        print(f"Extracted {frame_count} frames to {video_frames_dir}")

    # Save the path to a configuration file
    config = {
        'video_frames_dir': video_frames_dir
    }
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python frame_extraction.py <video_name>")
        sys.exit(1)
    vidName = sys.argv[1]
    extract_frames(vidName)

