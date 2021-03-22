import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import numpy as np




def information():
    st.subheader('1.자율주행 자동차 정보')
    st.write('자율주행 자동차는 스마트 머신이라는 종류에 해당한다')
    st.image('smart_mch.jpg',width=None)

    st.subheader('2.자율주행 차량이란')
    st.write('- 스스로 주변 환경 및 차량 상태를 인식, 판단, 제어하는 기능을 가진 자동차')
    st.write('- 자율주행 기술은 1~5단계로 나누어 판단한다')
    st.image('2.png',width= None)
    st.write('- 최근 시중에 판매되고 있는 차량은 레벨2 기술까지 적용되고 있다')

    st.subheader('3.자율주행 자동차 개발의 현주소')
    st.write('- 현재 세계 각 기업에서는 자율주행 차량 개발에 많은 투자를 하고 있다')
    st.write('- 구글의 Waymo를 시작으로, 많은 기업이 참여하고 있는 중이다')
    st.write('- 아래 표는 2020년 해외 조사기관이 발표한 자율주행차 리더보드이다')
    st.image('2020leader.png',width= None)
    st.write('- 현대자동차가 6위에 기록되어 자율주행 개발시장에 앞서있음을 볼 수 있다')
    st.write('- 하지만 아직 어느기업도 완전자율주행 개발에 성공하지 못했다. 각 나라별 교통법규, 신호체계, 도로환경이 다르기 때문에 맞춤형 개발이 필요하고, 이에 따라 데이터수집과 실전테스트가 상당시간 필요하기 때문이다')
    st.write('- 자율주행 자동차가 아니더라도, 실내주행 전동차, 음식서빙로봇, 드론 등 다양한 분야에서도 자율주행 시스템을 활용하고 있는데, 자율주행 시스템이 가지고 있는 하드웨어가 할 수 있는 영역이 무궁무진하기 때문이다')
    









