import streamlit as st
import random

st.set_page_config(page_title="환경 정책 카드 게임", layout="centered")

if "cards" not in st.session_state:
    st.session_state.cards = [
        ("🌱 재활용 캠페인", 10),
        ("🚯 해변 청소", 15),
        ("🏭 규제 완화", -10),
        ("🛑 플라스틱 금지", 20),
        ("💸 환경 예산 삭감", -20),
        ("🌳 해양 보호 구역 지정", 25),
    ]
    st.session_state.score = 50
    st.session_state.turns = 0

st.title("🃏 환경 정책 카드 뽑기")
st.write("카드를 뽑아 도시의 환경 점수를 관리하세요!")

if st.button("카드 뽑기"):
    card, effect = random.choice(st.session_state.cards)
    st.session_state.score += effect
    st.session_state.turns += 1
    st.success(f"당신은 **{card}** 카드를 뽑았습니다! (점수 {effect:+})")

st.metric("환경 점수", st.session_state.score)

if st.session_state.turns >= 5:
    st.subheader("📊 최종 결과")
    st.write(f"당신의 환경 점수: **{st.session_state.score}**")
    if st.session_state.score >= 80:
        st.success("🌟 지속가능한 도시를 만들었습니다!")
    elif st.session_state.score >= 50:
        st.warning("😐 도시가 간신히 유지됩니다.")
    else:
        st.error("💀 도시가 붕괴했습니다...")
    if st.button("🔄 다시 시작"):
        st.session_state.score = 50
        st.session_state.turns = 0
        st.rerun()
