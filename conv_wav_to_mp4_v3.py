import sys
import os
import moviepy.editor as mp

# Get the image file path from the command line arguments
image_file = sys.argv[1]

# Load the image file
image = mp.ImageClip(image_file)

# Iterate through all the WAV files in the directory
for filename in os.listdir():
    if filename.endswith(".wav"):
        # Open the audio file
        audio = mp.AudioFileClip(filename)

        # Set the duration of the image to match the audio file
        image = image.set_duration(audio.duration)

        # Create the video and set the audio
        video = mp.CompositeVideoClip([image])
        video = video.set_audio(audio)

        # Get the output video file name
        output_file = filename.split(".")[0] + ".mp4"

        # Save the video with the same name as the audio file
        video.write_videofile(output_file,fps=30, audio_codec="aac", audio_bitrate="320k")
