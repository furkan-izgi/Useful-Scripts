import cv2
import time
import os
from tkinter import filedialog

def video_to_frames(input_loc, output_loc):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        if not ret:
            continue
        # Write the results back to output location.
        cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
        count = count + 1
        print("%d frames extracted" % count, flush=True, end="\r")
        # If there are no more frames left
        if count == 4820:
            continue
        if (count == (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds forconversion." % (time_end-time_start))
            break

if __name__=="__main__":
    title = '''                                                           
 _____ _   _            _          _____                   
|  |  |_|_| |___ ___   | |_ ___   |   __|___ ___ _____ ___ 
|  |  | | . | -_| . |  |  _| . |  |   __|  _| .'|     | -_|
 \___/|_|___|___|___|  |_| |___|  |__|  |_| |__,|_|_|_|___|
                                                           
by mickimouse
'''
    print(title)
    input_loc = filedialog.askopenfilename(title="Select the Video File")
    output_loc = filedialog.askdirectory(title="Select the Output Folder")
    if input_loc == "" or output_loc == "":
        print("No file or folder selected")
        exit(0)
    else:
        video_to_frames(input_loc, output_loc)