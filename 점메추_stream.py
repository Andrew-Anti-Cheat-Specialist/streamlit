import streamlit as st
import random

# 한식, 중식, 일식 메뉴 리스트
menu_dict = {
    "한식": ["김치찌개", "된장찌개", "부대찌개", "삼겹살", "비빔밥", "떡볶이", "치킨"],
    "중식": ["짜장면", "짬뽕", "마라탕", "깐풍기", "양장피", "볶음밥", "탕수육"],
    "일식": ["초밥", "라멘", "가츠동", "텐동", "돈까스", "우동", "오코노미야끼"]
}

# 제목 및 설명
st.title("오늘의 점메추 Streamlit! ")
st.write("점메추 == 만족하는 메뉴가 나올 때까지 버튼을 눌러보세요!")

# 사용자 카테고리 선택
category = st.radio("카테고리를 선택하세요", list(menu_dict.keys()))

# 첫 번째 추천 버튼 (초록색)
if st.button("점심 메뉴 추천받기!"):
    selected_menu = random.choice(menu_dict[category])
    st.success(f"오늘의 추천 메뉴: **{selected_menu}**")  # 초록색 표시

# 다시 추천 버튼 (노란색)
if st.button("다시 추천받기"):
    selected_menu = random.choice(menu_dict[category])
    st.warning(f"오늘의 추천 메뉴: **{selected_menu}**")  # 노란색 표시
