import streamlit as st
import pandas as pd
import time

st.title('startup dashboard')
st.header('I am learning stremlit')
st.subheader('yes I am learning it ')
st.write('this is a normal rext')
st.markdown("""
### my favrate movies
- race
- dhoom 
- pk
""")

st.code("""
def foo(input):
   return input**2
x=foo(2)
   

""")

st.latex("x^2+y^3=6")

df=pd.DataFrame({
    'name':['faiz','shareque','naim'],
    'marks':[100,300,200],
    'package':[3,16,3]
})
st.dataframe(df)

st.metric('Revenue','Rs 3L','-3%')
st.metric('Revenue','Rs 3L','3%')

st.header('here is jason file')
st.json({
    'name':['faiz','shareque','naim'],
    'marks':[100,300,200],
    'package':[3,16,3]
})

st.header('This is a picture when south africa loss semifianl')
st.image('africa.jpg')

st.subheader('this is nature video')
st.video('nature.mp4')

st.sidebar.title('side bar ')

col1,col2=st.columns(2)

with col1:
    st.subheader('this is image')
    st.image('africa.jpg')
with col2:
    st.subheader('this is nature video')
    st.video('nature.mp4')

st.error('login failed')

st.success('login succesfull')
st.info('do login again ')
st.warning('dont touch it')

#bar=st.progress(0)

#for i in range(1,101):
#    time.sleep(0.1)
  #  bar.progress(i)


#email=st.text_input('enter email')
st.number_input('enter a number ')

st.date_input('select date')



Email=st.text_input('enter email')
password=st.text_input('enter password')
gender=st.selectbox('select gender',['male','femle','others'])
btn=st.button('login karo ')
if btn:
    if Email=='kiyakroyar@123' and password=='258369':
        st.balloons()
        st.write(gender)
        st.success('Login successfull')
    else:
        st.write('password or mail is wrong')
        st.error('login failed')

file=st.file_uploader('upload a  csv file')

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())