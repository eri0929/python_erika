import streamlit as st
import finance_naver0701

#사이드바 화면 
st.sidebar.header('Log in')
user_id = st.sidebar.text_input('아이디 입력', value='streamlit', max_chars=15)
user_password = st.sidebar.text_input('패스워드 입력', value='1234', type='password')


if user_password =='1234':
    st.sidebar.header('Erika World')
    opt_data = ['   ' , '환율조회','따릉이','유성우']
    menu = st.sidebar.selectbox('메뉴 선택', opt_data, index=0)
    st.sidebar.write('선택한 메뉴', menu) 

    if menu =='환율조회':
        st.subheader('환율조회>>>>>>>>>>')
        finance_naver0701.exchange_main()
      
    elif menu=='따릉이':
        st.subheader('따릉이 데이터 분석>>>>>>>>>>')
    
    elif menu=='유성우':
        st.subheader('유성우 데이터 분석>>>>>>>>>>')
    
    else: 
        st.subheader('Erika World')

   


#메인 화면 
#st.subheader('Erika World')
