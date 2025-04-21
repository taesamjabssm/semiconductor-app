import streamlit as st

# 로그인 상태 저장
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

# 주제 데이터
topics = [
    {
        "title": "반도체란?",
        "content": "반도체는 전기가 잘 흐르는 도체와 잘 흐르지 않는 부도체의 중간 정도 전도성을 가진 물질입니다.",
        "img": "https://images.unsplash.com/photo-1581090700227-1e8a2f2f86a4?auto=format&fit=crop&w=600&q=80",
    },
    {
        "title": "PN 접합 다이오드",
        "content": "P형 반도체와 N형 반도체가 접합된 소자로, 한쪽 방향으로만 전류를 흐르게 하는 특성이 있습니다.",
        "img": "https://images.unsplash.com/photo-1631597228761-c44efb705b79?auto=format&fit=crop&w=600&q=80",
    },
    {
        "title": "트랜지스터",
        "content": "전기적 신호를 증폭하거나 스위칭 역할을 하는 반도체 소자입니다. 주로 NPN과 PNP 타입으로 나뉩니다.",
        "img": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=600&q=80",
    },
]

st.set_page_config(page_title="반도체 학습", layout="centered")

st.title("🔌 간단한 반도체 원리 학습")

# 로그인 인터페이스
if not st.session_state.is_logged_in:
    st.warning("로그인이 필요합니다.")
    if st.button("로그인"):
        st.session_state.is_logged_in = True
        st.experimental_rerun()
    st.stop()

# 로그아웃 버튼
if st.button("로그아웃"):
    st.session_state.is_logged_in = False
    st.experimental_rerun()

# 주제 출력
for idx, topic in enumerate(topics):
    with st.expander(topic["title"]):
        st.image(topic["img"], use_column_width=True)
        st.write(topic["content"])
