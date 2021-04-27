import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import numpy as np
import webbrowser




def corporation():
    st.header('국내 자율주행 자동차 개발 기업 소개')
    c_list = ['현대자동차','카카오모빌리티','a2z','토르드라이브','스트라드비전','컨트롤웍스']
    choice = st.selectbox('선택하세요',c_list)

    if choice == '현대자동차':
        st.image('hyundai.jpg',width=None)
        st.subheader('현대자동차')
        st.write('- 국내 완성차 기업에 최고인 현대자동차')
        st.write('- 현대자동차는 자율주행으로 인한 사회적 혜택을 아래와 같이 정의한다')
        st.image('social.png',width=None)
        st.write('- 현재 판매중인 모든 차량에서 최대 3단계 자율주행을 제공한다')
        st.write('- 현대자동차 자체 개발 및 협력사 개발을 통해 빠르게 성장하고 있다')
        url1 = 'https://motional.com/'
        st.write('- 현대자동차 협력사 : Motional')
        if st.button('홈페이지 바로가기'):
            webbrowser.open('https://motional.com/',new=1)
    if choice == '카카오모빌리티':
        st.image('kko.png',width=None)
        st.subheader('카카오모빌리티')
        st.write('- 카카오모빌리티는 완성차를 개발하는 개념이 아닌 서비스제공 형태로 접근한다')
        st.write('- 2020년 3월 개발을 시작으로 꾸준한 성장을 보여주고 있다')
        st.write('- 자율주행 차량을 통제하는 관제시스템과 이를 총괄하는 운영시스템으로 나누고, 데이터와 기술, 운영 노하우를 접목시켜 가장 안전한 서비스를 제공하는게 목적이다')
        st.write('- 주변환경을 인식하고 주행전략을 결정하여 차량을 제어하는 기술과, 수요에 맞춰 배차하고 원격으로 차량을 조정하는 서비스를 함께 개발하고 있다')
        st.write('- 무엇보다 빅데이터 측면에선 압도적인 수준에 도달해 있기 때문에, 환경에 알맞는 서비스제공은 카카오모빌리티가 우위를 점할 것 같다')
        url2 = 'https://auto.v.daum.net/v/20200303103632878'
        if st.button('관련기사 바로보기'):
            webbrowser.open_new_tab('https://auto.v.daum.net/v/20200303103632878')
    if choice == 'a2z':
        st.image('a2z.jpg',width=None)
        st.subheader('a2z 오토노머스')
        st.write('- 현대자동차 자율주행 개발부에서 근무하던 기술자 3명이 나와 창업한 자율주행차 전문개발 스타트업')
        st.write('- 2018년부터 개발을 시작하여 현재 세종시에서 실전주행을 진행중에 있다')
        st.write('- 다른 스타트업들에 비해 엄청난 고공성장을 이루고 있으며, 지자체 및 수많은 기업에 파트너십을 맺어 미래성장가능성도 충분히 보여주고 있다')
        st.write('- 자율주행 개발자들을 위한 SDK(Software Development Kit)를 개발 및 배포하여 개발환경에 진입장벽을 낮추었다')
        st.write('- 자동차 전문 유튜버인 김한용 기자가 a2z 자율주행차 시승영상을 올리면서 a2z가 본격적으로 알려졌다')
        st.video('https://youtu.be/FAnnpoHkfgw')
        st.subheader('a2z 파트너사')
        st.image('ptn.png',width=None)
        url3 = 'http://www.autoa2z.co.kr/'
        if st.button('a2z 홈페이지 바로가기'):
            webbrowser.open_new_tab('http://www.autoa2z.co.kr/')
    if choice == '토르드라이브':
        st.image('토르.jpg',width=None)
        st.subheader('토르드라이브')
        st.write('- 2016년 서울대 출신 연구진이 모여 만든 스타트업으로 현재 서울, 미국 일부지역에서 자율주행 자동차를 개발하고 있다.')
        st.write('- 다른 국내 스타트업과 달리 미국 진출에 성공한 케이스로 자율주행 자동차 및 실내에서 운영가능한 자율주행 전동차도 개발하였다')
        st.write('- 자율주행 기술을 항공, 운송산업분야 등 다양한 비즈니스 모델에 접목시켜 실효성을 검증하는 중이다')
        
        st.subheader('토르드라이브 회사소개')
        st.video('https://youtu.be/Kuiv2Fb-n0U')
        
        st.subheader('인천공항 자율주행 전동차 도입사례')
        st.video('https://youtu.be/GNnwR-lGJUU')
        url4 = 'https://www.irobotnews.com/news/articleView.html?idxno=22582'
        if st.button('해당기사 바로가기'):
            webbrowser.open_new_tab('https://www.irobotnews.com/news/articleView.html?idxno=22582')
        if st.button('토르드라이브 홈페이지 바로가기'):
            url5 = 'https://www.thordrive.ai/'
            webbrowser.open_new_tab('https://www.thordrive.ai/')
    if choice == '스트라드비전':
        st.image('스트라드비전.png',width=None)
        st.subheader('스트라드비전')

        st.write('- 2014년 창업하여 최초 AI를 기반한 객체인식 기술을 개발하여 초소형 하드웨어용(웨어러블기기) S/W 개발이 목표였다')
        st.write('- 오히려 자동차업계에서 관심을 받았고 자율주행 소프트웨어 개발제안을 받아 성공적으로 목표를 전향한 케이스이다')
        st.write("""- 현재는 완성차 제조사를 대상으로 900만대 차량에 자율주행을 위한 소프트웨어 'SVNet'을 공급하고 있다""")
        st.write('- 미국, 중국, 독일, 일본, 인도에 회사를 두고 있으며, 현대자동차 등 대기업과의 협력사로서 활발히 활동하고 있다')

        st.subheader('스트라드비전 회사소개영상')
        st.video('https://youtu.be/da4YM27FSss')

    if choice == '컨트롤웍스':
        st.image('컨트롤웍스.png',width= None)
        st.subheader('컨트롤웍스')
        st.write('- 컨트롤웍스는 자율주행 기술에 대한 소프트웨어 개발보다는 해당 기술에 필요한 하드웨어를 제작 및 공급하는 회사로 더 많이 알려져있다')
        st.write('- 라이다센서를 비롯하여 자율주행 개발에 필요한 제품들을 공급하며, 기업과의 협력 뿐만 아니라 대학교 개발지망생들과 자율주행시스템을 제작하기도 하였다')
        st.image('control.png',width=None)
        url6 = 'https://www.control-works.co.kr/'
        if st.button('컨트롤웍스 홈페이지 바로가기'):
            webbrowser.open_new_tab('https://www.control-works.co.kr/')
    












        









