import streamlit as st 
import pandas as pd 
import numpy as np 
import pickle

with open("model_svr.pkl","rb") as file_1:
    model = pickle.load(file_1)

def Genders(Gender):
    if Gender == 'Male':
        return 0
    elif Gender == 'Female':
        return 1
def Education_level(Education):
    if Education == 'Primary School':
        return '1'
    elif Education == 'Secondary School':
        return '2'
    elif Education == 'High School':
        return '3'
    elif Education == 'University':
        return '4'
    elif Education == 'Master':
        return '5'
    elif Education == 'Doctor':
        return '6'
def MaritalStatus(marital):
    if marital == 'Married':
        return 1
    elif marital == 'Single':
        return 2
    elif marital == 'Others':
        return 3
    
def pays(pay):
    if pay == 'Pay Duly':
        return '-1.0'
    elif pay == 'Payment Delay for 1 month':
        return '1.0'
    elif pay == 'Payment Delay for 2 month':
        return '2.0'
    elif pay == 'Payment Delay for 3 month':
        return '3.0'
    elif pay == 'Payment Delay for 4 month':
        return '4.0'
    elif pay == 'Payment Delay for 5 month':
        return '5.0'
    elif pay == 'Payment Delay for 6 month':
        return '6.0'
    elif pay == 'Payment Delay for 7 month':
        return '7.0'
    elif pay == 'Payment Delay for 8 month':
        return '8.0'
def run():
    st.title("Hey, Let's Make :blue[Prediction]:sunglasses:")
    with st.form("prediction_form"):
        Limit = st.number_input('**Limit Balance**', min_value=1000.0, max_value= 1000000.0, value = 5000.0, help='Credit Card Limit Balance')
        Gender = st.selectbox('**Gender**', ('Male','Female'), index=1)
        Education = st.selectbox('**Education Level**', ('Primary School','Secondary School','High School','University','Master','Doctor'), index=1)
        Marital = st.selectbox('**Marital Status**',('Married','Single','Others'), index=1)
        Age = st.number_input('Customers Age', min_value=15, max_value= 100, value = 20)
        st.write('-'*50)
        pay0 = st.selectbox('**Repayment status in September**', ('Pay Duly','Payment Delay for 1 month','Payment Delay for 2 month','Payment Delay for 3 month','Payment Delay for 4 month','Payment Delay for 5 month','Payment Delay for 6 month','Payment Delay for 7 month','Payment Delay for 8 month'), index=1)
        pay2 = st.selectbox('**Repayment status in August**', ('Pay Duly','Payment Delay for 1 month','Payment Delay for 2 month','Payment Delay for 3 month','Payment Delay for 4 month','Payment Delay for 5 month','Payment Delay for 6 month','Payment Delay for 7 month','Payment Delay for 8 month'), index=1)
        pay3 = st.selectbox('**Repayment status in July**', ('Pay Duly','Payment Delay for 1 month','Payment Delay for 2 month','Payment Delay for 3 month','Payment Delay for 4 month','Payment Delay for 5 month','Payment Delay for 6 month','Payment Delay for 7 month','Payment Delay for 8 month'), index=1)
        pay4 = st.selectbox('**Repayment status in June**', ('Pay Duly','Payment Delay for 1 month','Payment Delay for 2 month','Payment Delay for 3 month','Payment Delay for 4 month','Payment Delay for 5 month','Payment Delay for 6 month','Payment Delay for 7 month','Payment Delay for 8 month'), index=1)
        pay5 = st.selectbox('**Repayment status in May**', ('Pay Duly','Payment Delay for 1 month','Payment Delay for 2 month','Payment Delay for 3 month','Payment Delay for 4 month','Payment Delay for 5 month','Payment Delay for 6 month','Payment Delay for 7 month','Payment Delay for 8 month'), index=1)
        pay6 = st.selectbox('**Repayment status in April**', ('Pay Duly','Payment Delay for 1 month','Payment Delay for 2 month','Payment Delay for 3 month','Payment Delay for 4 month','Payment Delay for 5 month','Payment Delay for 6 month','Payment Delay for 7 month','Payment Delay for 8 month'), index=1)
        st.write('-'*50)
        Bill_amt_1 = st.number_input('**Amount of bill statement in September**', min_value=-100000.0, max_value= 100000.0, value = 1000.0, help='Credit Card Limit Balance')
        Bill_amt_2 = st.number_input('**Amount of bill statement in August**', min_value=-100000.0, max_value= 100000.0, value = 1000.0, help='Credit Card Limit Balance')
        Bill_amt_3 = st.number_input('**Amount of bill statement in July**', min_value=-100000.0, max_value= 100000.0, value = 1000.0, help='Credit Card Limit Balance')
        Bill_amt_4 = st.number_input('**Amount of bill statement in June**', min_value=-100000.0, max_value= 100000.0, value = 1000.0, help='Credit Card Limit Balance')
        Bill_amt_5 = st.number_input('**Amount of bill statement in May**', min_value=-100000.0, max_value= 100000.0, value = 1000.0, help='Credit Card Limit Balance')
        Bill_amt_6 = st.number_input('**Amount of bill statement in April**', min_value=-100000.0, max_value= 100000.0, value = 1000.0, help='Credit Card Limit Balance')
        st.write('-'*50)
        Pay_amt_1 = st.number_input('**Amount of previous payment in September**', min_value=0.0, max_value= 100000.0, value = 1000.0, help='Credit Card Limit Balance')
        Pay_amt_2 = st.number_input('**Amount of previous payment in August**', min_value=0.0, max_value= 100000.0, value = 1000.0, help='Credit Card Limit Balance')
        Pay_amt_3 = st.number_input('**Amount of previous payment in July**', min_value=0.0, max_value= 100000.0, value = 1000.0, help='Credit Card Limit Balance')
        Pay_amt_4 = st.number_input('**Amount of previous payment in June**', min_value=0.0, max_value= 100000.0, value = 1000.0, help='Credit Card Limit Balance')
        Pay_amt_5 = st.number_input('**Amount of previous payment in May**', min_value=0.0, max_value= 100000.0, value = 1000.0, help='Credit Card Limit Balance')
        Pay_amt_6 = st.number_input('**Amount of previous payment in April**', min_value=0.0, max_value= 100000.0, value = 1000.0, help='Credit Card Limit Balance')
        
        submitted = st.form_submit_button("Submit")
    # st.write("Outside the form")

    data_inf = {
        'limit_balance': Limit,
        'Gender': Gender,
        'Education': Education, 
        'Marital_status': Marital, 
        'Age': Age,
        'pay_0': pay0,
        'pay_2': pay2, 
        'pay_3': pay3, 
        'pay_4': pay4,
        'pay_5': pay5, 
        'pay_6': pay6, 
        'bill_amt_1': Bill_amt_1,
        'bill_amt_2': Bill_amt_2,
        'bill_amt_3': Bill_amt_3,
        'bill_amt_4': Bill_amt_4,
        'bill_amt_5': Bill_amt_5,
        'bill_amt_6': Bill_amt_6,
        'pay_amt_1': Pay_amt_1,
        'pay_amt_2': Pay_amt_2,
        'pay_amt_3': Pay_amt_3,
        'pay_amt_4': Pay_amt_4,
        'pay_amt_5': Pay_amt_5, 
        'pay_amt_6': Pay_amt_6
        }
    data_inf = pd.DataFrame([data_inf])
    if submitted:
      data_inf['Gender'] = Genders(Gender)
      data_inf['Education'] = Education_level(Education)
      data_inf['Marital_status'] = MaritalStatus(Marital)
      data_inf['pay_0'] = pays(pay0)
      data_inf['pay_2'] = pays(pay2)
      data_inf['pay_3'] = pays(pay3)
      data_inf['pay_4'] = pays(pay4)
      data_inf['pay_5'] = pays(pay5)
      data_inf['pay_6'] = pays(pay6)
      result= model.predict(data_inf)
      if result[0] == 1:
          result = 'Yes'
      else:
          result = 'No'
      st.write(f'### Prediksi Default Payment Next Month: {result}')
      # st.balloons()
      st.snow()
if __name__ == '__main__':
  run()
