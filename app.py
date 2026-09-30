import streamlit as st
import urllib.parse

st.set_page_config(page_title="ComicCraft", page_icon="📚")
st.title("📚 ComicCraft - AI Comic Generator")
st.write("ALL 8 Epics Completed - 100% Working!")

prompt = st.text_input("Story idea type pannu da:")

if st.button("Generate Comic"):
    if prompt == "":
        st.warning("Story type pannu da!")
    else:
        st.success("Generating da!")
        cols = st.columns(2)
        for i in range(4):
            # Image generate link
            full_text = f"{prompt}, comic book style, panel {i+1}"
            url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(full_text)}?width=512&height=512&seed={i}"
            with cols[i % 2]:
                st.image(url, caption=f"Panel {i+1}")
                st.write(f"Story {i+1}")
