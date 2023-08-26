# from pytube import YouTube
# import streamlit as st
# from moviepy.video.io.VideoFileClip import VideoFileClip
# # import os
# from pathlib import Path
# def video_to_mp3(input_file, output_file):
#     try:
#         video_clip = VideoFileClip(input_file)
#         audio_clip = video_clip.audio
#         audio_clip.write_audiofile(output_file,codec='mp3')
#         audio_clip.close()
#         st.success(f"Audio extracted and saved as {output_file}")
#     except Exception as e:
#         st.warning(f"An error occurred: {e}")

# st.set_page_config("Audio Extracter")
# st.title("Audio App")
# option = st.radio(f":red[Choose option of Extract audio]", ("By Youtube video", "By Existing video"))

# if option == "By Youtube video":
#     video_url = st.text_input("Enter URL of video")
# #     SAVE_PATH = Path.home().joinpath("Downloads")
# #     SAVE_PATH = os.path.join(os.path.expanduser("~"), "Desktop")
#     output_file = st.text_input("Enter the filename: ")
#     if not output_file.endswith(".mp3"):
#         output_file+=".mp3"
#     try:
#         if st.button("Extract Audio"):
#             yt = YouTube(video_url)
#             video_stream = yt.streams.filter(file_extension='mp4').get_audio_only()
#             video_stream.download(filename=output_file)
# #             audio_output_path=Path.home().joinpath(SAVE_PATH,output_file)
# #             audio_output_path = os.path.join(SAVE_PATH, output_file)
#             st.success(f"Audio extracted and saved as {output_file}")
#     except Exception as e:
#         st.warning("An error occurred during extraction.", e)

# else:
#     st.subheader("Select the file")
#     input_file = st.file_uploader("Upload a file",type=["mp4"])
# #     downloads_path = Path.home().joinpath("Downloads") #os.path.join(os.path.expanduser("~"), "Desktop")
#     output_file = st.text_input("Enter the filename: ")
#     if not output_file.endswith(".mp3"):
#         output_file+=".mp3"
        
#     if st.button("Extract Audio"):
#         if input_file is not None:
# #             downloads_path = Path.home().joinpath(downloads_path, output_file) # os.path.join(downloads_path, output_file)
#             video_to_mp3(input_file.name, output_file)

# # from pathlib import Path
# # path = Path.home().joinpath( 'Documents', 'mysql_access' )
# # print(path)
        
from pytube import YouTube
import streamlit as st
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def video_to_mp3(input_file, output_file):
    try:
        video_clip = VideoFileClip(input_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_file, codec='mp3')
        audio_clip.close()
    except Exception as e:
        st.warning(f"An error occurred: {e}")

st.set_page_config("Audio Extracter")
st.title("Audio App")
option = st.radio("Choose option of Extract audio", ("By Youtube video", "By Existing video"))

if option == "By Youtube video":
    video_url = st.text_input("Enter URL of video")
    output_file = st.text_input("Enter the filename: ")
    if not output_file.endswith(".mp3"):
        output_file += ".mp3"
    
    if st.button("Extract Audio"):
        try:
            yt = YouTube(video_url)
            video_stream = yt.streams.filter(file_extension='mp4').get_audio_only()

            # Download the video stream
            video_stream.download(filename=output_file)
            video_path = output_file
            
            # Convert video to audio
            audio_output_file = os.path.splitext(output_file)[0] + ".mp3"
            video_to_mp3(video_path, audio_output_file)

            # Provide the download link for the audio
            st.download_button(
                label="Download Extracted Audio",
                data=audio_output_file,
                file_name=audio_output_file
            )
            st.success(f"Audio extracted and saved as {audio_output_file}")
        except Exception as e:
            st.warning(f"An error occurred during extraction: {e}")

else:
    st.subheader("Select the file")
    input_file = st.file_uploader("Upload a file", type=["mp4"])
    output_file = st.text_input("Enter the filename: ")
    if not output_file.endswith(".mp3"):
        output_file += ".mp3"
        
    if st.button("Extract Audio"):
        if input_file is not None:
            try:
                input_path = os.path.join(".", input_file.name)
                output_path = os.path.join(".", output_file)

                # Save uploaded file
                with open(input_path, "wb") as f:
                    f.write(input_file.read())

                # Convert video to audio
                video_to_mp3(input_path, output_path)

                # Provide the download link for the audio
                st.download_button(
                    label="Download Extracted Audio",
                    data=output_path,
                    file_name=output_file
                )
                st.success(f"Audio extracted and saved as {output_file}")
            except Exception as e:
                st.warning(f"An error occurred during extraction: {e}")
