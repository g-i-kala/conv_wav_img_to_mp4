import sys
import moviepy.editor as mp

# Get the audio and image file paths from the command line arguments
audio_file = sys.argv[1]
image_file = sys.argv[2]

# Open the audio file and the image file
audio = mp.AudioFileClip(audio_file)
image = mp.ImageClip(image_file)

# Set the audio as the background audio for the image
video = mp.CompositeVideoClip([image.set_audio(audio)])

# Set the duration of the video to match the audio file
video = video.set_duration(audio.duration)

# Get the output video file name
output_file = audio_file.split(".")[0] + ".mp4"

# Save the video with the same name as the audio file

video.write_videofile("test.mp4",fps=30, audio_codec="aac", audio_bitrate="320k")
