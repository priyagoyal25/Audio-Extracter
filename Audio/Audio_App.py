from pytube import YouTube
import streamlit as st
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def video_to_mp3(input_file, output_file):
    try:
        video_clip = VideoFileClip(input_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_file,codec='mp3')
        audio_clip.close()
        st.success(f"Audio extracted and saved as {output_file}")
    except Exception as e:
        st.warning(f"An error occurred: {e}")

st.set_page_config("Audio Extracter")
st.title("Audio App")
option = st.radio(f":red[Choose option of Extract audio]", ("By Youtube video", "By Existing video"))

if option == "By Youtube video":
    video_url = st.text_input("Enter URL of video")
    # SAVE_PATH=""
    # SAVE_PATH = os.path.join(os.path.expanduser("~"), "Downloads")
    output_file = st.text_input("Enter the filename: ")
    if not output_file.endswith(".mp3"):
        output_file+=".mp3"
    try:
        if st.button("Extract Audio"):
            yt = YouTube(video_url)
            video_stream = yt.streams.filter(file_extension='mp4').get_audio_only()
            # audio_file_path = os.path.join(output_path, '%(video_stream.title)s.mp3')
            # video_stream.download(audio_file_path)
            video_stream.download(output_path="/download/",filename=output_file)
            st.success("Audio extracted")
            # audio_output_path = os.path.join(SAVE_PATH, output_file)
            # st.success(f"Audio extracted and saved as {audio_output_path}")
    except Exception as e:
        st.warning(f"An error occurred during extraction {e}")

else:
    st.subheader("Select the file")
    input_file = st.file_uploader("Upload a file",type=["mp4"])
    downloads_path=""
    # downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    output_file = st.text_input("Enter the filename: ")
    if not output_file.endswith(".mp3"):
        output_file+=".mp3"
        
    if st.button("Extract Audio"):
        if input_file is not None:
            downloads_path=os.path.join(downloads_path, output_file)
            video_to_mp3(input_file.name, downloads_path)
