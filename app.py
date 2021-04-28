import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import numpy as np
from information import information
from corporations import corporation
from sdcfile import sdc
from growth import gv
import webbrowser




def main():
    st.title('자율주행 자동차 개발 프로젝트')
    

    menu = ['Home','About SDC','Corporations','Growth value','SDC']
    choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Home':
        st.header('라이다 및 영상인식기반 모빌리티 자율주행 솔루션 실무과정')
        st.write('훈련기간 : 2021-01-11 ~ 2021-08-02')
        st.image('learning.JPG')
    if choice == 'About SDC' :
        information()
    if choice == 'Corporations' :
        corporation()
    if choice == 'Growth value':
        gv()
    if choice == 'SDC':
        sdc()
# 자율주행에 대한 기본적인 정보제공

# 자율주행을 현재 개발중인 국내회사 홈페이지 연동
# 자율주행 개발에 대한 미래가치 or 프로펫을 통한 미래 예측







if __name__ == '__main__':
    main()