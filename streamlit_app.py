import random

import streamlit as st


st.set_page_config(page_title="เกมทายตัวเลข", page_icon="🎯", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8f6ef 0%, #edf4ef 100%);
        color: #193b35;
    }
    [data-testid="stHeader"] { background: transparent; }
    .block-container { max-width: 760px; padding-top: 3rem; }
    h1, h2, h3 { font-family: Georgia, serif; color: #193b35; }
    .eyebrow {
        color: #b94f35;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }
    div.stButton > button[kind="primary"] {
        background: #b94f35;
        border-color: #b94f35;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="eyebrow">A little game of intuition</p>', unsafe_allow_html=True)
st.title("เกมทายตัวเลข")
st.caption("NUMBER GUESSING GAME · เลือกระดับ แล้วลองทายตัวเลขที่ซ่อนไว้")

levels = {
    "1 · Easy (ง่าย)": (50, 10),
    "2 · Medium (ปานกลาง)": (100, 7),
    "3 · Hard (ยาก)": (200, 5),
}

if "game" not in st.session_state:
    st.session_state.game = None

if st.session_state.game is None:
    with st.container(border=True):
        st.subheader("เริ่มเกมใหม่")
        level_name = st.selectbox("เลือกระดับความยาก", list(levels))
        max_number, max_attempts = levels[level_name]
        st.write(f"สุ่มตัวเลขตั้งแต่ **1 ถึง {max_number}** · คุณมีโอกาสทาย **{max_attempts} ครั้ง**")
        if st.button("เริ่มเกม", type="primary", use_container_width=True):
            st.session_state.game = {
                "number": random.randint(1, max_number),
                "max_number": max_number,
                "max_attempts": max_attempts,
                "level_name": level_name.split(" · ", 1)[1],
                "attempts": 0,
                "history": [],
                "status": "playing",
            }
            st.rerun()
else:
    game = st.session_state.game
    with st.container(border=True):
        st.markdown(f"**{game['level_name']}** &nbsp; · &nbsp; ช่วงตัวเลข 1–{game['max_number']}", unsafe_allow_html=True)
        remaining = game["max_attempts"] - game["attempts"]
        st.progress(game["attempts"] / game["max_attempts"], text=f"ใช้ไป {game['attempts']} / {game['max_attempts']} ครั้ง")
        st.markdown(f"### เหลือโอกาสอีก {remaining} ครั้ง")

    if game["status"] == "playing":
        with st.form("guess_form", clear_on_submit=True):
            guess = st.number_input(
                "กรอกตัวเลขที่ต้องการทาย",
                min_value=1,
                max_value=game["max_number"],
                step=1,
                value=1,
            )
            submitted = st.form_submit_button("ส่งคำตอบ", type="primary", use_container_width=True)

        if submitted:
            guess = int(guess)
            game["attempts"] += 1
            game["history"].append(guess)
            if guess == game["number"]:
                game["status"] = "won"
            elif game["attempts"] >= game["max_attempts"]:
                game["status"] = "lost"
            st.rerun()

    if game["history"]:
        st.caption("คำตอบก่อนหน้า: " + "  ·  ".join(str(value) for value in game["history"]))
        if game["status"] == "playing":
            latest_guess = game["history"][-1]
            if latest_guess < game["number"]:
                st.info("น้อยไป! ลองใหม่")
            elif latest_guess > game["number"]:
                st.info("มากไป! ลองใหม่")

    if game["status"] == "won":
        st.success(f"ถูกต้อง! คุณชนะแล้ว ทายทั้งหมด {game['attempts']} ครั้ง")
    elif game["status"] == "lost":
        st.error(f"หมดโอกาสแล้ว! ตัวเลขที่ถูกต้องคือ {game['number']}")

    if game["status"] != "playing" and st.button("เล่นอีกครั้ง", type="primary", use_container_width=True):
        st.session_state.game = None
        st.rerun()

st.markdown("---")
st.caption("===== GAME OVER =====")
