import streamlit as st
from PIL import Image
import base64

# ---- CONFIG ----
st.set_page_config(page_title="Santhosh Ruban F | Portfolio", layout="wide")

# ---- LIGHT/DARK MODE ----
theme = st.sidebar.radio("Choose Theme", ["Light", "Dark"])
if theme == "Light":
    st.markdown("""
        <style>
        body { background-color: #0e1117; color: white; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body { background-color: white; color: black; }
        </style>
    """, unsafe_allow_html=True)

# ---- HEADER ----
st.title("Santhosh Ruban F")
st.subheader("Data Scientist")

# ---- SIDEBAR NAVIGATION ----
menu = ["Home", "About Me", "Projects", "Contact"]
choice = st.sidebar.selectbox("Navigation", menu)

# ---- DOWNLOAD RESUME ----
def download_resume():
    with open("Data Scientist Resume.pdf", "rb") as file:
        btn = st.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="SanthoshRubanF_Resume.pdf",
            mime="application/pdf"
        )

# ---- HOME ----
if choice == "Home":
    st.write("""
    👋 Hi! I'm **Santhosh Ruban F**, a Data Scientist passionate about building AI solutions for business intelligence, automation, and decision-making.

    💡 Key areas of focus:
    - Predictive Modeling
    - Computer Vision and OCR
    - Data Visualization & Warehousing
    - Streamlit App Development
    - Data Engineering & APIs

    📍 Based in Chennai, Tamil Nadu
    📧 Email: santhoshruban@gmail.com | 📞 +91 90955 55109
    """)
    download_resume()

# ---- ABOUT ----
elif choice == "About Me":
    st.header("About Me")
    st.write("""
    🎯 **Career Objective:**
    To work in a growth-oriented company where I can apply my strong technical and organizational skills, while continuously growing as a Data Scientist.

    🛠 **Skills:**
    - **Languages/Tools:** Python, SQL, MongoDB, Tableau, Power BI, Streamlit, PostgreSQL, SQLite
    - **Libraries/Frameworks:** NumPy, Pandas, Seaborn, Matplotlib, Scikit-learn, TensorFlow, EasyOCR
    - **Techniques:** Supervised & Unsupervised Learning, Deep Learning, Data Engineering, OCR, Data Visualization

    📚 **Certifications:**
    - Data Scientist, Python, Machine Learning, Deep Learning
    - Artificial Intelligence, NLP, PyTorch, Power BI
    - AWS, GIT & GitHub, ChatGPT

    🎓 **Education:**
    - Advanced Programming in Data Science – IIT-M / GUVI (Feb 2023 - Jul 2023)
    - B.A English Literature – Madurai Kamaraj University (2018 - 2021)
    - B.E Mechanical Engineering – LICET, Anna University (2010 - 2017)
    """)
    download_resume()

# ---- PROJECTS ----
elif choice == "Projects":
    st.header("Projects")

    st.success("1. 🎗 Predicting Breast Cancer in a Patient")
    st.write("""
    - **Tech Stack:** Python, Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib
    - Trained and optimized SVM & Logistic Regression models for classification
    - [GitHub Repo](https://github.com/SanthoshRubanF/Predicting-Breast-Cancer-in-a-patient)
    """)

    st.info("2. 📊 YouTube Data Harvesting & Warehousing")
    st.write("""
    - **Tech Stack:** Python, Streamlit, Google API, MongoDB, PostgreSQL
    - Built an app to extract, store, and analyze YouTube channel data
    - [GitHub Repo](https://github.com/SanthoshRubanF/YouTube-Data-Harvesting-and-Warehousing-using-SQL-MongoDB-and-Streamlit)
    """)

    st.success("3. 💸 Phonepe Pulse Data Visualization")
    st.write("""
    - **Tech Stack:** Python, PostgreSQL, Streamlit, Plotly
    - Visualized transaction/user data using interactive maps and graphs
    - [GitHub Repo](https://github.com/SanthoshRubanF/Phonepe-Pulse-Data-Visualization-and-Exploration)
    """)

    st.info("4. 🧾 BizCardX: Extracting Business Card Data")
    st.write("""
    - **Tech Stack:** Python, Streamlit, EasyOCR, SQLite
    - OCR app to extract, edit, and store business card data
    - [GitHub Repo](https://github.com/SanthoshRubanF/BizCardX-Extracting-Business-Card-Data-with-OCR)
    """)

    st.success("5. 📊 Tender Recommender: Government Tender Tracker & Matcher")
    st.write("""
    - **Tech Stack:** Python, Streamlit, BeautifulSoup, Scikit-learn, SQLite  
    - Scrapes tenders from GeM, recommends based on TF-IDF matching  
    - [GitHub Repo](https://github.com/SanthoshRubanF/Government-Tender-Tracker-Bid-Match-Recommender)
    """)

    st.info("6. 👩‍💼 Employee Data Management System")
    st.write("""
    - **Tech Stack:** Python, Streamlit, Pandas, SQLite  
    - A web app to manage employee records with add, update, view, and delete features  
    - [GitHub Repo](https://github.com/SanthoshRubanF/Employee-Data-Management)
    """)

    st.info("7. 📝 Complaint Management System")
    st.write("""
    - **Tech Stack:** Python, Streamlit, Pandas, SQLite  
    - A streamlined platform to register, track, and resolve user complaints efficiently  
    - [GitHub Repo](https://github.com/SanthoshRubanF/Complaint-Management-System)
    """)

# ---- CONTACT ----
elif choice == "Contact":
    st.header("Contact")
    st.write("""
    📧 Email: santhoshruban@gmail.com
    🔗 [LinkedIn](http://www.linkedin.com/in/santhoshrubanf)
    💻 [GitHub](https://github.com/SanthoshRubanF)
    📍 Chennai, Tamil Nadu, India - 600058
    ☎️ +91 90955 55109
    """)
