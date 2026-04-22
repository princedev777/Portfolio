import streamlit as st

st.set_page_config(page_title="Prince Phiri's Portfolio",page_icon="😁",layout="wide")

st.subheader("Hello, My Name Is Prince Phiri 🖐🖐")
st.title("A Software Engineer")
st.subheader("About Me🤴🏾")
st.write("I Am a Junior Developer trying to make a career in the tech world as best as I can by learning skills and applying them into real world solutions,This was Never Truly a passion of mine at first but now it become a wonderful and eternal learning journey that i an happy to be a part of.....most times😂")

st.write("---")
left_column,right_column = st.columns(2)
with left_column:
    st.header("Tech Skills")
    st.write("* Python")
    st.write("* Java") 
    st.write("* QA and test automation in C# using dotnet framework")
    st.write("* React")
    st.write("* HTML,CSS.Javascript")
    
with right_column:
    st.header("Soft Skills")
    st.write("* Teamwork")
    st.write("* Communication Skills")
    st.write("* Adaptability")
    st.write("* Good at explaining what I understand")
    
st.write("---")
st.header("Projects")
st.subheader("NB:Majority of these are incomplete due to constantly being busy with something else but they will be finished soon")


project_column,status_column = st.columns(2)
with project_column:
  st.subheader("Project List")
  st.markdown("* [Movie Website](https://github.com/Prince-afk119/MovieWebsite)")
  st.markdown("* [Simple QR code Generator](https://github.com/Prince-afk119/QRCodeGenerator)")
  st.markdown("* [Screen Time Manager](https://github.com/Prince-afk119/ScreenTimeEarned)")
  st.markdown("* [Bio Chat](https://github.com/Prince-afk119/BioChat)")