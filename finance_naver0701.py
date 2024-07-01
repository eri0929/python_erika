import pandas as pd
import warnings
import matplotlib.pyplot as plt
import streamlit as st

warnings.filterwarnings('ignore')


def get_exchange_rate_data(code,currency_name) : 
    df = pd.DataFrame()     #초기값을 만들어줌 
    for page_num in range(1,11) :
        base_url = f'https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_{code}KRW&page={page_num}' #6대신 page_num
        temp = pd.read_html(base_url, encoding='cp949', header=1)  #page_num은 변수이기 때문에 소괄호 + 앞에 f str 처리 
        df = pd.concat([df,temp[0]])
    
    total_rate_data_view(df,code,currency_name)   

def total_rate_data_view(df,code,currency_name): 
    plt.rc('font', family='Malgun Gothic')   #한글폰트를 추가하고 싶을 때  
    df_total = df[['날짜', '매매기준율', '사실 때', '파실 때', '보내실 때', '받으실 때']] 
    #전체 차트 작성
    df_total_chart = df_total.copy()   #카피 카피 
    df_total_chart = df_total_chart.set_index('날짜') 

   
    #print(f'==={currency_name[code_in]} - {code}===')  #strealim에서 print는 st.
    st.subheader(f'{currency_name} : {code}')
    #print(df.head(20))
    st.dataframe(df_total.head(20))

    #최신 데이터와 과거 데이터의 순서를 바꿈. 역순으로 표시함 2
    df_total_chart = df_total_chart[::-1] 
    #df_total_chart['매매기준율'].plot(figsize=(15,6), title= '환전비율')
    ax = df_total_chart['매매기준율'].plot(figsize=(15,6), title= '환전비율')
    fig = ax.get_figure()
    #plt.show()   #strealim에서 plt는..안씀 
#     month_rate_data_view(df)


# def month_rate_data_view(df_total) : 
#     df_total['날짜'] = df_total['날짜'].str.replace('.','').astype('datetime64[ms]') 
#     # '월' 파생변수 생성하기 
#     df_total['월'] = df_total['날짜'].dt.month

#     month_in = int(input('검색할 월입력>>')) 

#     month_df = df_total.loc[df_total['월']==month_in,['날짜', '매매기준율', '사실 때', '파실 때', '보내실 때', '받으실 때']]
#     month_df[::-1].reset_index(drop=True)
#     #데이터 표시 
#     print(f'==={currency_name[code_in]} - {code}===')
#     print(month_df.head(20))
#     month_df_chart = month_df.copy()
#     month_df_chart = month_df_chart.set_index('날짜')
#     month_df_chart['매매기준율'].plot()
#     plt.show()
#     print(f'==={currency_name[code_in]} - {code}===')
#     print(month_df.head(20))


#ㅠㅠ.... 

def exchange_main():
    currency_symbols_name = {'엔화':'JPY', '유로':'EUR' , '위안': 'CNY'}
    
    currency_name = st.selectbox('통화 선택',currency_symbols_name.keys())
    #code_in = int(input('통화유형 선택(0:JPY, 1:EUR, 2: CNY)'))
    #currency_symbols = ['JPY', 'EUR' , 'CNY']
    code = currency_symbols_name[currency_name]  #-1 추가
    # currency_name = ['엔화', '유로', '위안']
    clicked = st.button('환율 데이터 가져오기')
    if clicked: 
        get_exchange_rate_data(code,currency_name)


if __name__=='__main__':
    exchange_main()
