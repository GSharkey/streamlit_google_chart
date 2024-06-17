import streamlit as st
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
from datetime import datetime, timedelta

def main():
    st.title("구글 트렌드 검색 데이터 확인")

    # 사이드바 설정
    st.sidebar.title("날짜 범위 선택")
    start_date = st.sidebar.date_input("시작 날짜", value=datetime.now() - timedelta(days=30))
    end_date = st.sidebar.date_input("종료 날짜", value=datetime.now())

    # 사용자로부터 검색어 입력 받기
    keyword = st.text_input(f"키워드를 기입해주세요. ({start_date.strftime('%Y-%m-%d')} ~ {end_date.strftime('%Y-%m-%d')})", "")

    if keyword:
        # 구글 트렌드 API 연결
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=[keyword], timeframe=f"{start_date.strftime('%Y-%m-%d')} {end_date.strftime('%Y-%m-%d')}")

        # 검색 동향 데이터 가져오기
        interest_over_time_df = pytrend.interest_over_time()

        # 차트 그리기
        st.line_chart(interest_over_time_df)

    # 인기 검색어 Top 10 출력
    st.subheader(f"구글 인기 검색어 Top 10")

    # 구글 트렌드 API를 사용하여 인기 검색어 Top 10 가져오기
    pytrend = TrendReq()
    top_trends_df = pytrend.trending_searches(pn='south_korea')

    # 데이터프레임 생성
    top_trends_df = top_trends_df.reset_index()
    top_trends_df.columns = ['순위', '검색어']

    # 표 형식으로 출력
    st.dataframe(top_trends_df)

if __name__ == "__main__":
    main()
