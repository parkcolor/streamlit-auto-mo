import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import numpy as np
from information import information
from corporations import corporation
import webbrowser
import requests
from fbprophet import Prophet


def gv():
    st.subheader('자율주행 자동차 개발에 대한 성장가능성을 평가합니다')
    
    st.subheader('주식을 이용한 성장가능성 판단')
    st.write('현대자동차 자율주행 기술이 상용화된 시점(2008-01-08)부터 계산')
    today = datetime.now().date().isoformat()
    data1 = yf.Ticker('005380.KS')
    df1 = data1.history(start='2008-01-08', end = today)
    new_df1 = df1.reset_index()
    new_df1['Year'] = new_df1['Date'].dt.year
    # st.line_chart(new_df1['Close'])

    res1 = requests.get('https://api.stocktwits.com/api/2/streams/symbol/005380.KS.json')
    res_data1 = res1.json()

    p_df = df1.reset_index()
    p_df.rename(columns = {'Date' :'ds', 'Close' :'y'}, inplace = True)

    m = Prophet()
    m.fit(p_df)

    h_future = m.make_future_dataframe(periods=730)
    h_forecast = m.predict(h_future)

    fig1 = m.plot(h_forecast)
    st.pyplot(fig1)


    st.write('카카오모빌리티 자율주행 개발이 시작된 시점부터 계산')
    data2 = yf.Ticker('035720.KS')
    df2 = data2.history(start='2020-03-01', end = today)
    
    p_df1 = df2.reset_index()
    p_df1.rename(columns = {'Date' :'ds', 'Close' :'y'}, inplace = True)

    m1 = Prophet()
    m1.fit(p_df1)

    k_future = m1.make_future_dataframe(periods= 730)
    k_forecast = m1.predict(k_future)

    fig2 = m.plot(k_forecast)
    st.pyplot(fig2)












if __name__ == '__main__':
    main()