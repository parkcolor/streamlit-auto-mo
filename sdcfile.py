import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import numpy as np
import webbrowser

def sdc():
    st.header('SDC : Self-Driving Car')
    st.subheader('자율주행 기술')
    st.write('SDC에 탑재되는 자율주행 기술을 소개합니다')
    st.write('EC2 서버 한계로 인해 모델을 활용하여 실제 구동한 영상과 이미지로 대체합니다')

    c_list = ['SSD','YOLO','Semantic Segmentation']
    choice = st.selectbox('선택하세요',c_list)

    if choice == 'SSD':
        st.header('SSD : Single Shot Multibox Detetor')
        st.write('2015년 빠른 속도를 앞세운 YOLO모델이 탄생하였지만, 정확도 측면에서 다소 한계점이 있었고, 작은 물체를 잘 잡아내지 못하는 단점을 보완하는 목적으로 SSD가 탄생하였습니다.'        )
        st.write('[SSD 모델 구조]')
        st.image('ssd1.png')

        st.write('이미지를 활용한 실제 모델 구동영상')
        st.video('ssd.mp4')
        st.video('ssd_video.mp4')
        link = '[작동코드](https://en-percent.tistory.com/54)'
        st.markdown(link,unsafe_allow_html=True)
        st.write('암호 : 1234')

    if choice == 'YOLO':
        st.header('YOLO : You Only Look Once')
        st.image('yy1.png')
        st.write('입력받은 이미지를 S X S 그리드 영역으로 나누고 물체가 있을 영역에 Bounding Box를 예측하는 방식의 모델입니다.')
        st.image('yy.png')
        st.video('yolo_video.mp4')
        link1 = '[홈페이지 바로가기](https://pjreddie.com/darknet/yolo/)'
        link2 = '[작동코드](https://en-percent.tistory.com/55)'
        st.markdown(link1,unsafe_allow_html=True)
        st.write('암호 : 1234')
    
    if choice == 'Semantic Segmentation':
        st.header('열심히 맹그는중!')