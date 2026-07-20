import streamlit as st
st.title('서주희의 첫 웹앱!')
st.write('만나서 반가워요!!😘')
import streamlit as st

# -------------------------------------------------
# 페이지 설정
# -------------------------------------------------
st.set_page_config(
    page_title="MBTI 포켓몬 추천",
    page_icon="⚡",
    layout="centered"
)

# -------------------------------------------------
# MBTI별 포켓몬 데이터
# -------------------------------------------------
pokemon_data = {
    "ISTJ": {
        "pokemon": "거북왕",
        "emoji": "🐢💧",
        "type": "물",
        "title": "신뢰할 수 있는 수호자",
        "description": (
            "책임감이 강하고 맡은 일을 꾸준히 완수하는 ISTJ에게는 "
            "단단한 방어력과 안정적인 전투력을 가진 거북왕이 잘 어울립니다."
        ),
        "strength": "책임감 · 신중함 · 안정성"
    },
    "ISFJ": {
        "pokemon": "해피너스",
        "emoji": "🥚💗",
        "type": "노말",
        "title": "따뜻한 치유자",
        "description": (
            "다른 사람을 세심하게 돌보고 편안함을 주는 ISFJ에게는 "
            "동료를 치유하고 보호하는 해피너스가 잘 어울립니다."
        ),
        "strength": "배려심 · 헌신 · 따뜻함"
    },
    "INFJ": {
        "pokemon": "뮤",
        "emoji": "✨🐾",
        "type": "에스퍼",
        "title": "신비로운 이상주의자",
        "description": (
            "깊은 통찰력과 풍부한 내면세계를 지닌 INFJ에게는 "
            "신비롭고 무한한 가능성을 간직한 뮤가 잘 어울립니다."
        ),
        "strength": "통찰력 · 이상주의 · 공감"
    },
    "INTJ": {
        "pokemon": "뮤츠",
        "emoji": "🧠⚡",
        "type": "에스퍼",
        "title": "독립적인 전략가",
        "description": (
            "복잡한 문제를 분석하고 장기적인 전략을 세우는 INTJ에게는 "
            "강한 지성과 독립성을 가진 뮤츠가 잘 어울립니다."
        ),
        "strength": "전략적 사고 · 독립성 · 분석력"
    },
    "ISTP": {
        "pokemon": "개굴닌자",
        "emoji": "🥷💧",
        "type": "물·악",
        "title": "냉철한 해결사",
        "description": (
            "상황을 빠르게 파악하고 실용적인 해결책을 찾아내는 ISTP에게는 "
            "민첩하고 침착한 개굴닌자가 잘 어울립니다."
        ),
        "strength": "순발력 · 실용성 · 침착함"
    },
    "ISFP": {
        "pokemon": "님피아",
        "emoji": "🎀✨",
        "type": "페어리",
        "title": "감성적인 예술가",
        "description": (
            "부드러운 감성과 자신만의 미적 세계를 가진 ISFP에게는 "
            "다정하면서도 개성 넘치는 님피아가 잘 어울립니다."
        ),
        "strength": "감수성 · 온화함 · 개성"
    },
    "INFP": {
        "pokemon": "세레비",
        "emoji": "🌿⏳",
        "type": "에스퍼·풀",
        "title": "꿈꾸는 중재자",
        "description": (
            "진정성과 이상을 중요하게 여기고 더 나은 미래를 꿈꾸는 INFP에게는 "
            "시간을 넘어 희망을 전하는 세레비가 잘 어울립니다."
        ),
        "strength": "상상력 · 진정성 · 이상주의"
    },
    "INTP": {
        "pokemon": "메타몽",
        "emoji": "🧬🟣",
        "type": "노말",
        "title": "호기심 많은 탐구자",
        "description": (
            "고정관념에 얽매이지 않고 다양한 가능성을 탐구하는 INTP에게는 "
            "어떤 모습으로도 변신할 수 있는 메타몽이 잘 어울립니다."
        ),
        "strength": "호기심 · 논리력 · 유연한 사고"
    },
    "ESTP": {
        "pokemon": "루카리오",
        "emoji": "🥊🔵",
        "type": "격투·강철",
        "title": "대담한 모험가",
        "description": (
            "즉각적으로 행동하고 도전을 즐기는 ESTP에게는 "
            "빠른 판단력과 강한 전투 감각을 가진 루카리오가 잘 어울립니다."
        ),
        "strength": "행동력 · 대담함 · 적응력"
    },
    "ESFP": {
        "pokemon": "피카츄",
        "emoji": "⚡🐭",
        "type": "전기",
        "title": "사랑받는 분위기 메이커",
        "description": (
            "밝은 에너지로 주변 사람들에게 즐거움을 주는 ESFP에게는 "
            "친근하고 활기찬 피카츄가 가장 잘 어울립니다."
        ),
        "strength": "활기 · 친화력 · 낙천성"
    },
    "ENFP": {
        "pokemon": "이브이",
        "emoji": "🦊✨",
        "type": "노말",
        "title": "가능성 넘치는 활동가",
        "description": (
            "새로운 가능성을 발견하고 자유롭게 성장하는 ENFP에게는 "
            "다양한 모습으로 진화할 수 있는 이브이가 잘 어울립니다."
        ),
        "strength": "열정 · 창의성 · 가능성"
    },
    "ENTP": {
        "pokemon": "팬텀",
        "emoji": "👻💜",
        "type": "고스트·독",
        "title": "재치 있는 발명가",
        "description": (
            "기발한 아이디어와 장난기 넘치는 재치를 지닌 ENTP에게는 "
            "예측할 수 없는 매력의 팬텀이 잘 어울립니다."
        ),
        "strength": "창의력 · 재치 · 도전정신"
    },
    "ESTJ": {
        "pokemon": "윈디",
        "emoji": "🔥🐕",
        "type": "불꽃",
        "title": "믿음직한 관리자",
        "description": (
            "목표를 분명히 정하고 조직을 힘 있게 이끄는 ESTJ에게는 "
            "충성스럽고 위엄 있는 윈디가 잘 어울립니다."
        ),
        "strength": "추진력 · 책임감 · 리더십"
    },
    "ESFJ": {
        "pokemon": "푸크린",
        "emoji": "🎤💗",
        "type": "노말·페어리",
        "title": "다정한 친선대사",
        "description": (
            "사람들과 조화롭게 어울리고 주변을 따뜻하게 챙기는 ESFJ에게는 "
            "친근하고 사랑스러운 푸크린이 잘 어울립니다."
        ),
        "strength": "사교성 · 배려 · 협동심"
    },
    "ENFJ": {
        "pokemon": "가디안",
        "emoji": "🛡️✨",
        "type": "에스퍼·페어리",
        "title": "사람을 이끄는 조력자",
        "description": (
            "타인의 잠재력을 발견하고 헌신적으로 돕는 ENFJ에게는 "
            "소중한 사람을 끝까지 지키는 가디안이 잘 어울립니다."
        ),
        "strength": "공감 · 리더십 · 헌신"
    },
    "ENTJ": {
        "pokemon": "리자몽",
        "emoji": "🐉🔥",
        "type": "불꽃·비행",
        "title": "거침없는 지휘관",
        "description": (
            "큰 목표를 세우고 강한 추진력으로 성취해 내는 ENTJ에게는 "
            "당당한 존재감과 강력한 힘을 가진 리자몽이 잘 어울립니다."
        ),
        "strength": "결단력 · 야망 · 통솔력"
    }
}

# -------------------------------------------------
# 디자인
# -------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff7d6 0%, #e8f5ff 50%, #f7eaff 100%);
    }

    .main-title {
        text-align: center;
        font-size: 2.6rem;
        font-weight: 800;
        color: #293241;
        margin-bottom: 0.2rem;
    }

    .sub-title {
        text-align: center;
        color: #5f6b7a;
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }

    .result-card {
        background-color: rgba(255, 255, 255, 0.93);
        border: 3px solid #ffd43b;
        border-radius: 24px;
        padding: 30px;
        margin-top: 25px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(41, 50, 65, 0.13);
    }

    .pokemon-emoji {
        font-size: 5rem;
        margin-bottom: 5px;
    }

    .mbti-label {
        display: inline-block;
        background-color: #293241;
        color: white;
        border-radius: 20px;
        padding: 6px 16px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .pokemon-name {
        color: #e63946;
        font-size: 2.3rem;
        font-weight: 800;
        margin: 5px 0;
    }

    .pokemon-type {
        color: #67727e;
        font-size: 0.95rem;
        margin-bottom: 12px;
    }

    .pokemon-title {
        color: #3d5a80;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 15px;
    }

    .description {
        color: #344054;
        font-size: 1.05rem;
        line-height: 1.8;
        word-break: keep-all;
    }

    .strength-box {
        background-color: #fff6cc;
        border-radius: 12px;
        padding: 12px;
        margin-top: 18px;
        color: #665200;
        font-weight: 700;
    }

    .footer {
        text-align: center;
        color: #7c8794;
        font-size: 0.85rem;
        margin-top: 35px;
    }

    div.stButton > button {
        width: 100%;
        border: none;
        border-radius: 14px;
        padding: 0.8rem;
        font-size: 1.1rem;
        font-weight: 700;
        background: linear-gradient(90deg, #ffcb05, #ff9f1c);
        color: #293241;
    }

    div.stButton > button:hover {
        color: #293241;
        border: none;
        box-shadow: 0 5px 15px rgba(255, 159, 28, 0.35);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# 화면 구성
# -------------------------------------------------
st.markdown(
    '<div class="main-title">⚡ MBTI 포켓몬 연구소</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">MBTI를 선택하면 성격과 잘 어울리는 포켓몬을 추천해 드려요!</div>',
    unsafe_allow_html=True
)

mbti_groups = {
    "분석가형": ["INTJ", "INTP", "ENTJ", "ENTP"],
    "외교관형": ["INFJ", "INFP", "ENFJ", "ENFP"],
    "관리자형": ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
    "탐험가형": ["ISTP", "ISFP", "ESTP", "ESFP"]
}

group = st.selectbox(
    "나의 MBTI 그룹을 선택하세요",
    options=list(mbti_groups.keys())
)

selected_mbti = st.selectbox(
    "나의 MBTI를 선택하세요",
    options=mbti_groups[group]
)

show_result = st.button("나와 어울리는 포켓몬 찾기 🔍")

# -------------------------------------------------
# 결과 출력
# -------------------------------------------------
if show_result:
    result = pokemon_data[selected_mbti]

    st.balloons()

    st.markdown(
        f"""
        <div class="result-card">
            <div class="pokemon-emoji">{result["emoji"]}</div>
            <div class="mbti-label">{selected_mbti}</div>
            <div class="pokemon-name">{result["pokemon"]}</div>
            <div class="pokemon-type">타입: {result["type"]}</div>
            <div class="pokemon-title">“{result["title"]}”</div>
            <div class="description">{result["description"]}</div>
            <div class="strength-box">
                ✨ 공통된 매력: {result["strength"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("이 추천은 재미를 위한 성격 유형 콘텐츠이며 심리검사 결과가 아닙니다.")

st.markdown(
    '<div class="footer">Made with Streamlit · Pokémon MBTI Matching</div>',
    unsafe_allow_html=True
)
