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
        st.header('본 프로젝트는 자율주행자동차(SDC)개발 프로젝트 입니다.')
        st.subheader('[섹션 설명]')
        st.write('About SDC : 자율주행 기술에 대한 정보를 볼 수 있습니다')
        st.write('Corporations : 자율주행 기술을 개발하는 국내기업을 소개합니다')
        st.write('Growth value : 국내 기업에 대한 성장가능성 예측데이터를 볼 수 있습니다')
        st.write('SDC : SDC에 탑재되는 다양한 컴퓨터비전 기술을 볼 수 있습니다.')
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