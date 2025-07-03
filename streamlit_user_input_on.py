#streamlit_user_input_on

import streamlit as st

input_file_path = 'website_text_content.txt'

def main():
    with open('website_text_content.txt', 'r', encoding='utf-8') as file:
        stryng = file.read()
    st.text(stryng)
    user_input = st.text_input(" ", value="-")
    if st.button("txt", key="scroll_button"):
        if user_input not in stryng:
            with open('website_text_content.txt', 'a', encoding='utf-8') as file:
                file.write(str(user_input+"\n"))
    
if __name__ == "__main__":
    main()
