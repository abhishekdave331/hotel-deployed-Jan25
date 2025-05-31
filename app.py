
import numpy as np
import pandas as pd
import streamlit as st
import joblib

with open('final_model.joblib', 'rb') as file:
    model = joblib.load(file)

with open('transformer.joblib', 'rb') as file:
    tranformer = joblib.load('file')

def prediction(input_list):
    input_list = np.array(input_list,dtype=object)

    pred = model.predict_proba([input_list])[:,1][0]

    if pred>0.5:
        return f'This booking is more likely to get cancelled with chances {round(pred,2)}.'
    else:
        return f'This booking is less likely to get cancelled with chances {round(pred,2)}.'

def main():
    st.title('INN Hotel Group')
    lt = st.text_input('Enter the lead time in days:')
    mkt = (lambda x:1 if x=='Online' else 0)(st.selectbox('How the booking was made?',['Online','Offline']))
    price = st.text_input('Enter the price of room:')
    adult = st.selectbox('How many adults',[1,2,3,4])
    arr_m = st.slider('What is the month of Arrival?',min_values=1,max_valie=12,step=1)
    weekd_lambda = (lambda x: 0 if x=='Mon' else
                                1 if x=='Tue' else
                                2 if x=='Wed' else
                                3 if x=='Thus' else
                                4 if x=='Fri' else
                                5 if x=='Sat' else
                                6 if x=='Sun' else)
    arr_w = weekd_lambda(st.selectbox('What is weekday of arrival?',['Mon','Tue','Wed','Thus','Fri','Sat','Sun']))
    dep_w = weekd_lambda(st.selectbox('What is weekday of departure?',['Mon','Tue','Wed','Thus','Fri','Sat','Sun']))
    weekn = st.text_input('Enter the number of week nights in stay:')
    wkndn = st.text_input('Enter the number of weekend nights in stay:')
    totan = weekn+wkndn
    park = (lambda x:1 if x=='Yes' else 0)(st.selectbox('Doest customer need parking?',['Yes','No']))
    spcl = st.selectbox('How many special requests have been made?',[0,1,2,3,4,5])

    lt_t,price_t = transformer.transform([[lt,price]])[0]

    inp_list = [lt_t,spcl,price_t,adult,wkndn,park,weekn,mkt,arr_m,arr_w,totan,dep_w]

    if st.button('Predict'):
        response = prediction(inp_list)
        st.success(response)

if __name__=='__main__':
    main()
