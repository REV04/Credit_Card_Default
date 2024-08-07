import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title = 'Credit Card Default - EDA',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)
def run():
    # Membuat title
    st.title('Credit Card Default :blue[EDA]')
    # Menambahkan gambar
    st.image('https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hiXqlqvZItfG_Fhsq5s8MQ.jpeg'
    ,width = 900, caption= 'Credit Card Default')
    # Menambahkan Deskripsi
    st.write("# ***:red[Let's Explore it]***")
    # Membuat Garis lurus
    st.markdown('---')
    # Magic Syntax
    '''
    Pada page ini, penulis akan melakukan eksplorasi sederhana Data set yang digunakan adalah dataset FIFA 2022. Dataset ini berasal dari FIFA
    '''
    # Show dataframe
    df = pd.read_csv('P1G5_Set_1_Richard_Edgina.csv')
    penampung = []
    for i in df['age']:
        # Condition for classification ages
        if 0 <= i <= 14:
            penampung.append('Pedriatic Group')
        elif 14 < i <= 47:
            penampung.append('Young Age')
        elif 47 < i <= 63:
            penampung.append('Middle Age')
        elif i > 63:
            penampung.append('Elderly Age')
    # Make new column
    df['Age Group'] = penampung
    KelompokUmur = df.groupby(['Age Group','default_payment_next_month'])['default_payment_next_month'].count()
    KelompokUmur.plot(kind='barh')
    EducationLevel = df.groupby(['education_level','default_payment_next_month'])['default_payment_next_month'].count()
    Repayment = df.groupby(['pay_0','default_payment_next_month'])['default_payment_next_month'].count()
    container = []
# Loop for i in data frame with column 'Age'
    for i in df['bill_amt_1']:
    # Condition for classification ages
        if -1000000.0 <= i < 0.0:
            container.append('Bank Owe You')
        elif i == 0.0:
            container.append('There is no Billing Amount')
        elif 0.0 < i <= 10000.0:
            container.append('Small Billing Amount')
        elif 10000.0 < i <= 100000.0:
            container.append('Medium Billing Amount')
        elif i > 100000.0:
            container.append('Big Billing Amount')
# Make new column
    df['Billing Amount Group'] = container
    BillingAmount = df.groupby(['Billing Amount Group','default_payment_next_month'])['default_payment_next_month'].count()
    st.header('Data Frame Credit Card')
    st.markdown('---')
    st.dataframe(df)
    st.markdown('---')
    st.write('## **EDA**')
    st.markdown('---')
    # Membuat Barplot
    st.write('### ***Age Distribution and Main Age Group for Credit Card Defaults***')
    fig = plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)
    sns.set_style('whitegrid')
    sns.histplot(df['age'], kde = False, color ='red', bins = 30)
    plt.subplot(1,2,2)
    KelompokUmur.plot(kind = 'barh')
    # st.title('Histogram of Age')
    plt.show()
    st.pyplot(fig)
    st.write('The histogram on the left indicates that the age distribution is slightly skewed, with the majority of ages clustering around 30 years and the fewest ages being over 50 years old. The chart on the right shows that the age group with the highest rate of payment defaults is the young age group, while the elderly age group has the lowest rate of payment defaults.')
    st.markdown('---')
    st.write('### ***Education Distribution and Main Education Level Group for Credit Card Defaults***')
    fig = plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)
    sns.set_style('whitegrid')
    sns.histplot(df['education_level'], kde = False, color ='red', bins = 30)
    plt.subplot(1,2,2)
    EducationLevel.plot(kind = 'barh')
    # st.title('Histogram of Age')
    plt.show()
    st.pyplot(fig)
    st.write('The histogram on the left indicates that the age distribution is slightly skewed, with the majority of education level on Secondary School and the fewest Education level is Doctor. The chart on the right shows that the Education Level group with the highest rate of payment defaults is the Secondary School group, while the Doctor group has the lowest rate of payment defaults.')
    st.markdown('---')
    st.write('### ***Repayment Status In September 2005 Distribution and Main Repayment Status Group for Credit Card Defaults***')
    fig = plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)
    sns.set_style('whitegrid')
    sns.histplot(df['pay_0'], kde = False, color ='red', bins = 30)
    plt.subplot(1,2,2)
    Repayment.plot(kind = 'barh')
    # st.title('Histogram of Age')
    plt.show()
    st.pyplot(fig)
    st.write('The histogram on the left indicates that the age distribution is highly skewed, with the majority of repayment status on pay duly and the fewest repayment status is payment delay greater than 3 months. The chart on the right shows that the Repayment status with the highest rate of payment defaults is the pay duly.')
    st.markdown('---')
    st.write('### ***Billing Amount In September 2005 Distribution and Main Billing Amount Group for Credit Card Defaults***')
    fig = plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)
    sns.set_style('whitegrid')
    sns.histplot(df['bill_amt_1'], kde = False, color ='red', bins = 30)
    plt.subplot(1,2,2)
    BillingAmount.plot(kind = 'barh')
    # st.title('Histogram of Age')
    plt.show()
    st.pyplot(fig)
    st.markdown('---')
    st.write('The histogram on the left indicates that the billing amount distribution is highly skewed, with the majority of billing amount clustering around 0 dollar and the fewest billing amount being over 30000 dollars. The chart on the right shows that the billing amount group with the highest rate of payment defaults is medium billing amount, while Bank Owe you group has the lowest rate of payment defaults.')
if __name__ == '__main__':
    run()