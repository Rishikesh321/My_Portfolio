from click import style
from prompt_toolkit import HTML
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import streamlit.components.v1 as components
from PIL import Image


st.set_page_config(page_title="Rishi's Portfolio",page_icon=":tada:")

#--Lottie---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding_1 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_rrqimc3f.json")
lottie_coding_2 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fwlx9xtz.json")
lottie_coding_3 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_qufi1zre.json")
lottie_coding_4 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_utxzyfe9.json")
lottie_coding_5 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json")
lottie_coding_6 = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_zd4ppbmb.json")
lottie_coding_7 = load_lottieurl("https://assets6.lottiefiles.com/temp/lf20_8SCZZt.json")
lottie_coding_8 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_hbhhy6a8.json")
lottie_coding_9 = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_k5mfy04e.json")
lottie_coding_10 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_3vbOcw.json")
facebook = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_nzzpyr6i.json")
linkedin = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_qqx4zbms.json")
github = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_1ldonjtk.json")
instagram = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_grzsrsgs.json")

#components.html("""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>""",height = 300)
#components.iframe("""<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="rishikesh-chakraborty-5a7ba315b" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/rishikesh-chakraborty-5a7ba315b?trk=profile-badge">Rishikesh Chakraborty</a></div>""",height = 300)

#----Sidebar menu----
with st.sidebar:
 selected = option_menu(
    menu_title= None,
    options=["Who Am I ?","Skills","Work Experience","Education","Blogs","Contact Me"],
    icons = ["file-person","pc-display","book","file-earmark-bar-graph-fill","chat-left-text-fill"],
    menu_icon= "cast",
    default_index= 0
    #orientation= "horizontal"
 )
 st.subheader("Downlad My Resume from here")
    #--------------------------Resume download button------------------------
 with open("PDF\Rishikesh_Chakraborty.pdf", "rb") as pdf_file:
      PDFbyte = pdf_file.read()

      st.download_button(label="Download",
                    data=PDFbyte,
                    file_name="Rishikesh_Resume.pdf",
                    mime='application/octet-stream')

if selected == "Who Am I ?":
 #-----------------------------Header-----------------------------------------------------------------------------
  left_column , right_column = st.columns(2)
  with left_column:
   with st.container():
    image = Image.open('Images/rishi.jpg')
    image = image.rotate(270, expand = 1)
    st.image(image,width=200)
  with right_column:
    with st.container():
       st_lottie(lottie_coding_10, height=300, key="hello")  
  with st.container():
    st.subheader("Hi, I am Rishi :wave:")
    st.title("A Data Analyst from India, A curious explorer")
    st.write("Motivated , teamwork-oriented, and resposible Data Analyst & presentations by the average professional. trilingual in English, Hindi and Bengali.")
    st.write("##")
  with st.container():
    st.subheader("Connect with me")
    left_column , right_column = st.columns(2)
    with left_column:
       st_lottie(facebook, height=200, key="fac")
       st.markdown("[Facebook](https://www.facebook.com/profile.php?id=100011600379060)", unsafe_allow_html=True)
       st_lottie(linkedin, height=200, key="lin")
       st.markdown("[Linkedin](www.linkedin.com/in/rishikesh-chakraborty-5a7ba315b)", unsafe_allow_html=True)
    with right_column:
      st_lottie(github, height=200, key="git")
      st.markdown("[Github](https://github.com/Rishikesh321)", unsafe_allow_html=True)
      st_lottie(instagram, height=200, key="insta")
      st.markdown("[Instagram](https://www.instagram.com/zephyrus_009)", unsafe_allow_html=True)
    
    
    

# ------------------------------SKILLS-------------------------------------------------------------------------------
if selected == "Skills":
  
  #---Technical Skills----

  with st.container():
    st.header("My Technical Skills") 
    
  # Data Management    
    left_column , right_column = st.columns(2) 
    
    with left_column:
       st.write("##")
       st.subheader("Data Management")
       st.write("Data quality Assessment, Data Analysis, Pattern & Trend Identification,Visualization of Data Insights")     
    with right_column:
       st_lottie(lottie_coding_1, height=300, key="coding")
       
    # Analytics Tools   
    left_column , right_column = st.columns(2) 
    
    with left_column:
       st_lottie(lottie_coding_2, height=300, key="data")
    with right_column:
       st.write("##")
       st.subheader("Analylics Tools")
       st.write("Advance Microsoft Excel Functions, MySQL, Power BI, Python, R, Troubleshooting") 

    # Research   
    left_column , right_column = st.columns(2) 
    
    with left_column:
       st.write("##")
       st.subheader("Resarch")
       st.write("Data Science Research Methods, Data Modeling")  
    with right_column:
       st_lottie(lottie_coding_3, height=300, key="reseach")
#----------------------------------------------WORK EXPREIENCE--------------------------------------------------------------       

if selected == "Work Experience":
  #----Experience-----
  with st.container():
      st.title("Data Analst")
      st.subheader("Coding Objects Private Limited (2020 - Present)")
      st.write("1. Converted data into actionable insights by predicting and modeling future outcome")
      st.write("2. Utilized MySQL, Power BI, Streamlit, Shiny and other dashboard/visualization toolsets for dataintelligence and analysis"
    )
  #----- Live Demonstration ------
  with st.container():
      st.write("---")
      st.write("##")
      st.title ("Now it's time for Some ML")
#----------------------------------------------------EDUCATION-------------------------------------------------------------

if selected == "Education":
    with st.container():
       st.title("My Education Details")
       fig = go.Figure(data=[go.Table(header=dict(values=['Qualification', 'Stream','Year','Institute','Score']),
                cells=dict(values=[["B.tech","12th","10th"], ["PWE","Science","-"],[2020,2016,2014],["National Power Training Institute, Durgapur","Guru Teg Bahadur Public School, Durgapur","Durgapur Ispat Vidyalaya, Durgapur"],["8.04 CGPA","79.6 %","7.4 CGPA"]]))]) 
       
       st.plotly_chart(fig,use_container_width=True)

    #-------------------Professional Certificates-----------------------------------------
       st.write("---")
       st.title("Professional Certificates")
       left_column, right_column = st.columns(2)
       with left_column:
           st_lottie(lottie_coding_4, height=300, key="bi")
           st.subheader("Certification of Microsoft Power BI(2021)")
           st.write("online - Udemy")
           st.write("[Certificate](https://udemy-certificate.s3.amazonaws.com/pdf/UC-8de180fb-21bd-45a4-9d04-36fc050ac59f.pdf)")
       with right_column:
           st_lottie(lottie_coding_5, height=300, key="big_bi")
           st.subheader("Certification of Building Big Data Pipelineswith R & Sparklyr & Power BI ")
           st.write("online - Udemy")
           st.write("[Certificate](https://udemy-certificate.s3.amazonaws.com/pdf/UC-84dd8601-00dd-47a7-8272-8b04019d667f.pdf)")
           st.write("[Github](https://github.com/Rishikesh321/Earthquake-Prediction-2017.git)")
#---------------------------Blogs-------------------------------------------------------
if selected == "Blogs":       
   
    st.title("Let's Learn & Grow Together")
    left_column,right_column = st.columns(2)
    
    with left_column:
      with st.container():
        st_lottie(lottie_coding_6, height=300, key="vis")
        st.subheader("Data Visualization in R")
        st.write("Data visualization is the graphic representation of data. It involves producing images that communicate relationships among the represented data to viewers of the images.")
        st.write("[Click here to visit]( https://rishikesh-chakraborty.shinyapps.io/Visualisation_Tutorial/)")
        st_lottie(lottie_coding_7, height=300, key="decesion")
        st.subheader("Decision Tree in R")
        st.write("What is Decision Trees? Decision Trees are a popular Data Mining technique that makes use of a tree-like structure to deliver consequences based on input decisions.")
        st.write("[Click here to visit]( https://rishikesh-chakraborty.shinyapps.io/Decission_Tree_Tutorial/)")
    with right_column:
        st_lottie(lottie_coding_8, height=300, key="cluster")
        st.subheader("Cluster Analysis in R")
        st.write("Cluster analysis is a class of techniques that are used to classify objects or cases into relative groups called clusters.")
        st.write("[Click here to visit]( https://rishikesh-chakraborty.shinyapps.io/Cluster_analysis_Tutorial/)")
        st.write("##")
        st_lottie(lottie_coding_9, height=300, key="tidy")
        st.subheader("Tidymodels in R")
        st.write("Much like the tidyverse consists of many core packages, such as ggplot2 and dplyr, tidymodels also consists of several core packages")
        st.write("[Click here to visit]( https://rishikesh-chakraborty.shinyapps.io/Tidymodels_Tutorial/)") 
#----------------------------Contact Me------------------------------------------------------------
if selected == "Contact Me":
    with st.container():
        st.header(":mailbox: Get in touch with me") 
         
        contact_form = """  <form action="https://formsubmit.co/rishikeshchakraborty26@gmail.com" method="POST">
                             <input type="hidden" name="_captcha" value="false">
                             <input type="text" name="name" placeholder = "Your Name" required>
                             <input type="email" name="email" placeholder = "Your Email"  required>
                             <textarea name="message" placeholder="Your message here"></textarea>
                            <button type="submit">Send</button> 
                            </form>
                              """  
        st.markdown(contact_form,unsafe_allow_html=True)
       
       #CSS local file
        def local_css(file_name):
           with open(file_name) as f:
               st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)


        local_css("style.css")