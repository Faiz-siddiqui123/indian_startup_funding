import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




st.set_page_config(layout='wide',page_title='startup Analysis')

df=pd.read_csv('startup_cleaned.csv')
df['date']=pd.to_datetime(df['date'],errors='coerce')
df['year']=df['date'].dt.year
df['month']=df['date'].dt.month
def load_investor_detail(investor):
    st.title(investor)
    #load the recent five investors
    last5_df=df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)


    col1,col2=st.columns(2)


    with col1:
        #biggest investment
        biggest_investment=df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(
            ascending=False).head(5)
        st.subheader('Biggest Investments')
        st.dataframe(biggest_investment)
        #fig,ax=plt.subplots()
        #ax.bar(biggest_investment.index,biggest_investment.values)
        #st.pyplot(fig)
        st.subheader('sector invested with bar chart ')
        st.bar_chart(biggest_investment)
    with col2:



        date_investor = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
        try:
            st.subheader('sector invested year wise ')
            st.line_chart(date_investor)
        except :
            st.write('something went wrong')
    #for pie chart
    veritcal_investor = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
    try:
        st.subheader('sectors invested in')
        fig1, ax1 = plt.subplots()
        ax1.pie(veritcal_investor, labels=veritcal_investor.index, autopct='%0.01f%%')


        st.pyplot(fig1)
    except:
        st.write('The amount is zero ')

    date_investor = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    try:
        st.subheader('sector invested year wise ')
        fig3,ax3=plt.subplots()
        ax3.plot(date_investor.index,date_investor.values)
        st.pyplot(fig3)

    except:
        st.write('something went wrong')




st.sidebar.title('Startup funding Analysis')

option=st.sidebar.selectbox('select one',['Overal analysis','Startup','Investor'])

def load_overall_analysis():
    st.title('Overall analysis')
    #toala invested amount
    total=round(df['amount'].sum())
    st.metric('total',str(total)+'Cr')

    max=round(df['amount'].max())
    max_df=df[df['amount'] == max]
    st.subheader('Top investor detail ')
    st.dataframe(max_df)

    col1,col2=st.columns(2)
    with col1:
        st.subheader('Top five max investor detail')
        max_five=df.groupby('startup')['amount'].max().sort_values(ascending=False).head(5)
        st.dataframe(max_five)

        st.metric('maximum investment',str(max)+'Cr')
    with col2:
        st.subheader('bar chart for max investor')

        st.bar_chart(max_five)

    col3,col4=st.columns(2)
    with col3:
        mean=round(df.groupby('startup')['amount'].sum().mean(),2)

        st.metric("average investment",str(mean)+"Cr")

    with col4:
        total_funded=len(set(df['startup'].tolist()))
        st.metric('total number of investor',total_funded)

    st.header('MOM graph')
    selected_option=st.selectbox('Select type',['Total','Count'])
    if selected_option=='Total':
        year_month = df.groupby(['year', 'month'])['amount'].sum().reset_index()
        year_month['x-axis'] = year_month['month'].astype('str') + '-' + year_month['year'].astype('str')

        fig3, ax3 = plt.subplots()
        ax3.plot(year_month['x-axis'], year_month['amount'])
        st.pyplot(fig3)
    else:
        year_month_count = df.groupby(['year', 'month'])['amount'].count().reset_index()
        year_month_count['x-axis'] = year_month_count['month'].astype('str') + '-' + year_month_count['year'].astype('str')

        fig4, ax4= plt.subplots()
        ax4.plot(year_month_count['x-axis'], year_month_count['amount'])
        st.pyplot(fig4)













if option=='Overal analysis':

    btn0=st.sidebar.button('show Overall analysis')

    load_overall_analysis()

elif option=='Startup':
    st.title('Startup analysis')
    st.sidebar.selectbox('select Startup',sorted(df['startup'].unique().tolist()))
    btn1=st.button('Find startup detail')

else:

    selected_investor=st.sidebar.selectbox('select Startup',set(df['investors'].str.split(',').sum()))
    btn2 = st.sidebar.button('Find startup detail')
    if btn2:
        load_investor_detail(selected_investor)

