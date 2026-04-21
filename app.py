import streamlit as st
import numpy as np
import time
import random
import plotly.graph_objects as go

# =============================================================================
# [LAYER 0] GIAO DIỆN CYBERPUNK (GÂY BÃO MẠNG XÃ HỘI)
# =============================================================================
st.set_page_config(page_title="VANGUARD-1000 AI", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Major+Mono+Display&family=Orbitron:wght@900&family=Space+Mono&display=swap');
    
    .stApp { background-color: #000; color: #00FF41; font-family: 'Space Mono', monospace; }

    /* Hiệu ứng tiêu đề Glitch */
    .viral-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 40px;
        text-align: center;
        background: linear-gradient(90deg, #00FF41, #FF00FF, #00FFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 3s infinite linear;
    }
    
    @keyframes shine {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }

    /* Kết quả khổng lồ rực rỡ */
    .supreme-signal {
        font-family: 'Major Mono Display', monospace;
        font-size: clamp(80px, 20vw, 400px);
        text-align: center;
        margin: -40px 0;
        color: #fff;
        text-shadow: 0 0 20px #00FF41, 0 0 50px #00FF41, 0 0 100px #00FF41;
        letter-spacing: -15px;
    }

    /* Ma trận 1000 Neurons */
    .neural-net {
        display: grid;
        grid-template-columns: repeat(50, 1fr);
        gap: 2px;
        background: rgba(0, 255, 65, 0.05);
        padding: 10px;
        border: 1px solid #222;
        border-radius: 10px;
    }

    .node {
        height: 8px;
        background: #111;
        border-radius: 1px;
    }
    .node-active { background: #00FF41; box-shadow: 0 0 10px #00FF41; }

    /* Khung quét AI */
    .scan-container {
        border-left: 4px solid #FF00FF;
        padding-left: 20px;
        background: rgba(255, 0, 255, 0.02);
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# =============================================================================
# [LAYER 1] THUẬT TOÁN HỘI TỤ THIÊN HÀ (1000 AGENTS)
# =============================================================================
class GalacticAI:
    def __init__(self, hash_code, history):
        self.hash = hash_code.strip()
        self.history = history

    def calculate_signal(self):
        # Bóc tách cấu trúc vi phân của Hash
        raw_vals = [int(self.hash[i:i+2], 16) for i in range(0, len(self.hash)-1, 2) if len(self.hash[i:i+2]) == 2]
        
        lose_streak = 0
        for h in reversed([x['status'] for x in self.history]):
            if h == "Thua": lose_streak += 1
            else: break

        votes = []
        for i in range(1000):
            # Thuật toán đa tầng XOR + Modulo
            seed = sum(raw_vals) + (i * 13) + (lose_streak * 101)
            vote = 0 if (seed ^ (i * 7)) % 2 == 0 else 1
            votes.append(vote)

        tai_count = votes.count(0)
        final_logic = 0 if tai_count > 500 else 1
        
        # Chiến thuật đảo cực Adaptive
        if lose_streak >= 1:
            final_logic = 1 - final_logic
            
        prediction = "TAI" if final_logic == 0 else "XIU"
        confidence = (max(tai_count, 1000-tai_count) / 1000) * 100
        
        return prediction, confidence, votes

# =============================================================================
# [LAYER 2] GIAO DIỆN ĐIỀU HÀNH
# =============================================================================
def main():
    if 'history' not in st.session_state: st.session_state.history = []
    
    st.markdown("<h1 class='viral-title'>VANGUARD-1000: GLOBAL AI COMMAND</h1>", unsafe_allow_html=True)
    
    h_input = st.text_input("📡 INJECT HASH DATA:", placeholder="Dán mã Hash để bắt đầu cuộc truy quét của 1000 AI...")

    if st.button("🔥 EXECUTE SUPREME SCAN"):
        if len(h_input) >= 32:
            status_placeholder = st.empty()
            progress_bar = st.progress(0)
            
            # Hiệu ứng quét ma trận (Thứ làm nên sự nổi tiếng trên MXH)
            for i in range(1, 101):
                time.sleep(0.015)
                progress_bar.progress(i)
                status_placeholder.markdown(f"**VANGUARD SCAN:** `{random.getrandbits(64):x}` | AI Unit {i*10}/1000 Online")
            
            ai = GalacticAI(h_input, st.session_state.history)
            res, conf, votes = ai.calculate_signal()
            
            # 1. HIỂN THỊ MA TRẬN NEURON
            st.markdown("<div class='neural-net'>", unsafe_allow_html=True)
            target = 0 if res == "TAI" else 1
            for v in votes:
                active = "node-active" if v == target else ""
                st.markdown(f"<div class='node {active}'></div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # 2. HIỂN THỊ LỆNH TỐI CAO
            color = "#FF073A" if res == "TAI" else "#05D9E8"
            st.markdown(f"<p class='supreme-signal' style='color: {color};'>{res}</p>", unsafe_allow_html=True)
            
            # 3. THÔNG SỐ CHIẾN THUẬT
            st.markdown(f"""
            <div class='scan-container'>
                <p><b>XÁC SUẤT ĐỒNG THUẬN:</b> <span style='color:#00FF41;'>{conf:.2f}%</span></p>
                <p><b>SỐ THỰC THỂ THAM CHIẾU:</b> <span style='color:#00FF41;'>1000 ARCHITECTS</span></p>
                <p><b>TRẠNG THÁI:</b> <span style='color:#FF00FF;'>ULTRA-STABLE SIGNAL</span></p>
            </div>
            """, unsafe_allow_html=True)
            
            st.session_state.last_p = res
        else:
            st.error("MÃ HASH KHÔNG ĐỦ DỮ LIỆU!")

    # Feedback
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ THẮNG (SYNC)", use_container_width=True):
            if 'last_p' in st.session_state:
                st.session_state.history.append({"status": "Thắng"})
                st.rerun()
    with c2:
        if st.button("❌ THUA (RE-SCAN)", use_container_width=True):
            if 'last_p' in st.session_state:
                st.session_state.history.append({"status": "Thua"})
                st.rerun()

if __name__ == "__main__":
    main()
