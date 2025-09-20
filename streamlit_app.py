import streamlit as st
import random

st.set_page_config(page_title="환경 정책 카드 게임", layout="centered")

# 초기화
if "cards" not in st.session_state:
    st.session_state.cards = [
        ("🌱 재활용 캠페인", 10, "정책"),
        ("🚯 해변 청소", 15, "정책"),
        ("🏭 규제 완화", -10, "정책"),
        ("🛑 플라스틱 금지", 20, "정책"),
        ("💸 환경 예산 삭감", -20, "정책"),
        ("🌳 해양 보호 구역 지정", 25, "정책"),
        ("🌊 폭풍 해일 발생", -15, "재난"),
        ("🔥 해양 산불 발생", -20, "재난"),
        ("🐟 해양 생물 번식 성공", 20, "자연"),
        ("🦀 산호초 회복", 15, "자연"),
        ("⚡ 태풍 피해", -25, "재난"),
        ("☀️ 강수량 증가로 수질 개선", 10, "자연"),
    ]
    st.session_state.score = 50
    st.session_state.turns = 0
    st.session_state.history = []

st.title("🃏 환경 정책 카드 게임 (업그레이드 버전)")
st.write("카드를 뽑아 도시의 환경 점수를 관리하세요!\n"
         "정책 카드와 자연/재난 카드가 랜덤으로 등장합니다.")

# 카드 뽑기
if st.button("카드 뽑기"):
    card, effect, category = random.choice(st.session_state.cards)
    st.session_state.score += effect
    st.session_state.turns += 1
    st.session_state.history.append(f"{category} 카드: {card} ({effect:+})")
    if effect > 0:
        st.success(f"✅ {card} ({category} 카드) 뽑음! 점수 {effect:+}")
    else:
        st.error(f"⚠️ {card} ({category} 카드) 뽑음! 점수 {effect:+}")

# 현재 점수 & 남은 카드 수
st.metric("환경 점수", st.session_state.score)
st.write(f"🔹 뽑은 카드 수: {st.session_state.turns} / 최대 7턴")

# 카드 뽑은 내역
if st.session_state.history:
    st.subheader("📜 카드 뽑은 내역")
    for h in st.session_state.history:
        st.write(h)

# 게임 종료
if st.session_state.turns >= 7:
    st.subheader("📊 최종 결과")
    st.write(f"최종 환경 점수: **{st.session_state.score}**")
    if st.session_state.score >= 90:
        st.success("🌟 지속가능한 도시 완성!")
    elif st.session_state.score >= 70:
        st.success("🙂 도시가 안정적이며 환경이 잘 관리되었습니다.")
    elif st.session_state.score >= 50:
        st.warning("😐 도시가 간신히 유지됩니다.")
    else:
        st.error("💀 도시가 붕괴했습니다... 환경 관리 실패!")

    if st.button("🔄 다시 시작"):
        st.session_state.score = 50
        st.session_state.turns = 0
        st.session_state.history = []
        st.rerun()
