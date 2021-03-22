import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import numpy as np
from information import information




def main():
    st.title('자율주행 자동차 개발 프로젝트')
    

    menu = ['Home','Information','Corporations','Growth value']
    choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Home':
        st.write('홈 화면입니다')
    if choice == 'Information' :
        information()
    if choice == 'Corporations' :
        corporation()
# 자율주행에 대한 기본적인 정보제공

# 자율주행을 현재 개발중인 국내회사 홈페이지 연동
# 자율주행 개발에 대한 미래가치 or 프로펫을 통한 미래 예측







if __name__ == '__main__':
    main()