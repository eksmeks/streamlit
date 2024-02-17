#web_streamlit2

import streamlit as st

from PIL import Image

image = Image.open('blue_strings.png')
st.image(image) #, caption='Sunrise by the mountains')

def get_audio_format(file_path):
    file_extension = file_path.split('.')[-1].lower()
    if file_extension == "mp3":
        return "mp3"
    elif file_extension == "wav":
        return "wav"
    else:
        return None

def main():
    #st.title("eksmeks entertainment")

    audio_files = {
        "dub1_2komma7[140bpm]": "_dub1_2komma7[140bpm].mp3",
        "666xx2[160bpm]": "666xx2[160bpm].mp3",
        "e5cut[160bpm]edit": "e5cut[160bpm]edit.mp3",
        "exp5m_vonminute2_40[177bpm]edit2": "exp5m_vonminute2_40[177bpm]edit2.mp3",
        "käx9[178bpm]": "käx9[178bpm].mp3",
        "RAc2ggaZA9Hv.128[180bpm]": "RAc2ggaZA9Hv.128[180bpm].mp3",
        #"happy28_keine_atastrophe_x[157bpm]": "happy28_keine_atastrophe_x[157bpm].wav",
        #"relatedtoacid[155bpm]": "relatedtoacid[155bpm].wav",
        #cd Desktop\python\web_streamlit && streamlit run web_streamlit2.py
        "standalone1[170bpm]": "standalone1[170bpm].mp3",
        #"rec_num_1[mix]":"rec_num_1.mp3",
        "23max23S23.2.3.[1ong][185bpm]":"23max23S23.2.3.[1ong][185bpm].mp3",
        "NOTiTELNOPLAN._7[190bpm]":"NOTiTELNOPLAN._7[190bpm].mp3"
    }

    selected_mp3 = st.selectbox("select", list(audio_files.keys()))
    audio_path = audio_files[selected_mp3]

    #play_button = st.button("load mp3")
    #if play_button:
    with open(audio_path, "rb") as audio_file:
        audio_data = audio_file.read()
        audio_format = get_audio_format(audio_path)
        if audio_format == "mp3":
            st.audio(audio_data, format="audio/mp3", start_time=0)
        if audio_format == "wav":
            st.audio(audio_data, format="audio/wav", start_time=0)

    #st.title("Local Video Player Example")
    #video_path = "ghreen1.mp4"
    
    mp4_files = {
        "ghreen1": "ghreen1.mp4",
        "ghreen2": "ghreen2.mp4",
        #"conca_output_great":"conca_output_great.mp4",
        #"conca_output_great_crazy":"conca_output_great_crazy.mp4",
        "minus_matters":"minus_matters.mp4",
        #"original_mandelbrot_zoom":"original_mandelbrot_zoom.mp4",
        #"out_hole":"out_hole.mp4",
        "out_long":"out_long.mp4",
        #"out_long2":"out_long2.mp4",
        "out_mandel_hoch":"out_mandel_hoch.mp4",
        #"all_mp4":"all_mp4.mp4",
        "out_tan_shit":"out_tan_shit.mp4",
        "out_tan_slime":"out_tan_slime.mp4",
        "tangential_journey_2":"tangential_journey_2.mp4",
        "tanzer1":"tanzer1.mp4",
        "minus_matters":"minus_matters.mp4",
    }

    selected_mp4 = st.selectbox("select", list(mp4_files.keys()))
    mp4_path = mp4_files[selected_mp4]

    #play_button2 = st.button("load mp4")
    #if play_button2:
    with open(mp4_path, "rb") as video_file:
        video_data = video_file.read()
        st.video(video_data) #loop

if __name__ == "__main__":
    main()
