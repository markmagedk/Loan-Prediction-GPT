import streamlit as st
import requests
from streamlit_lottie import st_lottie
import joblib
import numpy as np

st.set_page_config(page_title='LoanGPT', page_icon='::star::')


def load_lottie(url):  # test url if you want to use your own lottie file 'valid url' or 'invalid url'
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def prepare_input_data_for_model(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
                                 CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area):
    if Gender == 'Male':
        gender = 1
    else:
        gender = 0
    if Married == 'Yes':
        married = 1
    else:
        married= 0
    if Dependents == '0':
        dep = 0
    elif Dependents =='1' :
        dep = 1
    elif Dependents=='2' :
        dep=2
    else :
        dep=3
    if Education == 'Graduate':
        edu = 1

    else:
        edu=0
    if Self_Employed == 'Yes':
        se=1

    else:
        se = 0
    if Credit_History=='Yes':
        ch=1
    else:
        ch=0
    if Property_Area== 'Urban':
        pa = 1
    elif Property_Area =='Rural':
        pa = 2
    else:
        pa=3


    A = [gender, married, dep, edu,se, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, ch, pa]
    sample = np.array(A).reshape(-1, len(A))

    return sample

st.write('LoanGPT')

st.image('images.png')

loaded_model = joblib.load(open("LoanPrediction_model", 'rb'))


#lottie_link = "https://assets5.lottiefiles.com/packages/lf20_kK73MQ.json"
#animation = load_lottie(lottie_link)

#Second_lottie_link = "https://assets5.lottiefiles.com/packages/lf20_FrZL7ohUPU.json"
#gif = load_lottie(Second_lottie_link)



st.write('---')
st.subheader('Enter the information to predict whether your loan will be approved or not :')


with st.container():
    right_column, left_column = st.columns(2)

    with right_column:
        name = st.text_input('Name : ')
        gender = st.radio('Gender : ', ['Female', 'Male'])
        married = st.radio('Married : ', ['Yes', 'No'])
        dep = st.selectbox('Dependents', ('0', '1', '2', '3+'))
        edu = st.radio('Education : ', ['Graduated', 'Not Graduated'])
        se = st.radio('Self Employed : ', ['Yes', 'No'])
        ai = st.number_input('Applicant Income', step=500)
        cai=st.number_input('Coapplicant Income', step=500)
        la = st.number_input('Loan Amount', step=10)
        lat = st.number_input('Loan Amount Term', step=36)
        ch = st.radio('Credit History : ', ['Yes', 'No'])
        pa= st.selectbox(' Property Area', ('Urban', 'Rural', 'Semiurban'))
        sample = prepare_input_data_for_model(gender, married, dep, edu, se, ai, cai,
                                              la, lat, ch, pa)

    #with left_column:
        #st_lottie(animation, speed=1, height=400, key="widget1")

    if st.button('Predict'):
        pred_Y = loaded_model.predict(sample)

        if pred_Y == 1:
            st.success('Congratulations, Your loan will be approved.')
        else:
            st.error('Sorry, You are so poor to get a loan.')