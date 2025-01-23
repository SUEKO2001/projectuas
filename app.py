import pickle
import streamlit as st
import base64

# import background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('background.jpg')

#membaca Model

diabetes_model = pickle.load(open('dieb_model.sav', 'rb'))

# Path atau URL ke logo
logo_url = "https://cdn-icons-png.flaticon.com/512/5935/5935561.png"
# HTML dan CSS untuk posisi logo
st.markdown(
    f"""
    <style>
    .logo-container {{
        display: flex;
        justify-content: center; /* Posisi tengah */
        align-items: center;
        height: 100px; /* Atur tinggi sesuai kebutuhan */
    }}
    </style>
    <div class="logo-container">
        <img src="{logo_url}" alt="Logo" width="100">
    </div>
    """,
    unsafe_allow_html=True
)
#judul web
st.markdown("<h2 style='text-align: center;'>Aplikasi Prediksi Penyakit Diabetes Menggunakan Algoritma Support Vector Machine (SVM)</h2>",
            unsafe_allow_html=True)

#bagi kolom
col1,col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ('Input nilai Pregnancies')
    Glucose = st.text_input ('Input nilai Glucose')
    BloodPressure = st.text_input ('Input nilai BloodPressure')
    SkinThickness = st.text_input ('Input nilai SkinThickness')
with col2 :
    Insulin = st.text_input ('Input nilai pregnancies')
    BMI = st.text_input ('Input nilai Insulin')
    DiabetesPedigreeFunction =st.text_input('Input nilai diabetes Pedigree function')
    Age = st.text_input('Input nilai Age')

#code prediksi
diab_diagnosis = ''

#membuat tombol untuk prediksi
if st.button('**Test Prediksi Diabetes**', type="primary"):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = '**Pasien Terkena Diabetes**'
        st.error(diab_diagnosis)
    else:
        diab_diagnosis = '**Pasien Tidak Terkena Diabetes**'
        st.success(diab_diagnosis)
