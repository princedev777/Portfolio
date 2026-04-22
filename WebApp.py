import streamlit as st

st.set_page_config(page_title="Prince Phiri's Portfolio",page_icon="😁",layout="wide")

st.subheader("Hello, My Name Is Prince Phiri 🖐🖐")
st.title("A Software Engineer")
st.subheader("About Me🤴🏾")
st.write("I Am a Junior Developer trying to make a career in the tech world as best as I can by learning skills and applying them into real world solutions,This was Never Truly a passion of mine at first but now it become a wonderful and eternal learning journey that i an happy to be a part of.....most times😂")

st.write("---")
left_column,right_column = st.columns(2)
with left_column:
    st.header("Tech Skills👨🏾‍💻")
    st.write("* Python")
    st.write("* Java") 
    st.write("* QA and test automation in C# using dotnet framework")
    st.write("* React")
    st.write("* HTML,CSS.Javascript")
    
with right_column:
    st.header("Soft Skills🔊")
    st.write("* Teamwork")
    st.write("* Communication Skills")
    st.write("* Adaptability")
    st.write("* Good at explaining what I understand")
    
st.write("---")
st.header("Projects")
st.subheader("NB:Majority of these are incomplete due to constantly being busy with something else but they will be finished soon")


project_column,status_column = st.columns(2)
with project_column:
  st.subheader("Project List🦺")
  st.link_button(" Movie Website","https://github.com/Prince-afk119/MovieWebsite")
  st.link_button("Simple QR code Generator","https://github.com/Prince-afk119/QRCodeGenerator")
  st.link_button("Screen Time Manager","https://github.com/Prince-afk119/ScreenTimeEarned")
  st.link_button("Bio Chat","https://github.com/Prince-afk119/BioChat")
  
  
st.write("---")
st.header("Contact Me!📞")
col1,col2 = st.columns([0.3, 6])
with col1:
    st.image("Images/linkedin-logo-linkedin-icon-transparent-free-png.webp", width=30)
with col2:
    st.link_button("LinkedIn","https://www.linkedin.com/in/yourprofile")

col1,col2 = st.columns([0.3, 6])
with col1:
    st.image("Images/gmail-logo-google-product-icon-logotype-gmail-editorial-vector-illustration_773275-3198.avif", width=30)
with col2:
    st.markdown("Princephirise@gmailcom")
