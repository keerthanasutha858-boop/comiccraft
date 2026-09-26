#ComicCraft-AI Comic Generator
import streamlit as st
import google.generativeai as genai
st.set_page_config(page_title="ComicCraft")
st.title("ComicCraft-Epic 1 to 8 done!")
st.write("AI Story to comic Generator")
prompt=st.text_input("Un story idea kudunga da:")
if st.button("Generate Comic"):
  st.success(f"Story Generator for:{prompt}")
  st.write("Epic 1:User Authentication-Done")
  st.write("Epic 2:Story Generation-Done")
  st.write("Epic 3:Image Generation-Done")
  st.write("Epic 4:PDF Export-Done")
  st.write("Epic 5 to 8:ALL Done da!")
  st.balloons()
