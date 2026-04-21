import streamlit as st
import numpy as np
import time
import random

# =============================================================================
# [LAYER 0] GIAO DIỆN TỐI GIẢN & QUYỀN LỰC (SUPREME COMMAND UI)
# =============================================================================
st.set_page_config(page_title="1000-AI COMMAND CORE", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=JetBrains+Mono:wght@700&display=swap');
    
    .stApp { background-color: #000; color: #00FF41; font-family: 'JetBrains Mono', monospace; }
    
    /* Hiển thị kết quả duy nhất khổng lồ */
    .single-command {
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(120px, 30vw, 450px);
        text-align: center;
        margin: 40px 0;
        line-height: 1;
        letter-spacing: -10px;
        color: #fff;
        text-shadow: 0 0 50px #00FF41, 0 0 100px #00FF41;
        animation: pulse 1.5s infinite alternate;
    }
    
    @keyframes pulse {
        from { transform: scale(0.95); opacity: 0.8; }
        to { transform: scale(1); opacity: 1; }
    }

    .info-box {
        background: rgba(0, 255, 65, 0.1);
        border: 1px solid #00FF41;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
    }

    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        background-color: #00FF41 !important;
        color: black !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# =============================================================================
# [LAYER 1] LÕI HỘI TỤ 1000 AI (1000-NEURAL CONVERGENCE)
# =============================================================================
class SupremeAI:
    def __init__(self, hash_code, history):
        self.hash = hash_code.strip()
        self.history = history

    def get_final_command(self):
        # 1. Bóc tách Hash
        raw_vals = [int(c, 16) for c in self.hash if c in "0123456789abcdef"]
        sum_val = sum(raw_vals) if raw_vals else 0
        
        # 2. Kiểm tra lịch sử (Nhịp bẻ)
        lose_streak = 0
        for h in reversed([x['status'] for x in self.history]):
            if h == "Thua": lose_streak += 1
            else: break

        # 3. Giả lập 1000 AI bỏ phiếu
        votes = []
        for i in range(1000):
            seed = sum_val + i + (lose_streak * 37)
            # Mỗi AI dùng một thuật toán XOR khác nhau
            vote = 0 if (seed ^ (i % 17)) % 2 == 0 else 1
            votes.append(vote)

        # 4. Quyết định tối cao
        final_logic = 0 if votes.count(0) > votes.count(1) else 1
        
        # Tự động bẻ lái nếu sàn đang ép chuỗi thua
        if lose_streak >= 1:
            final_logic = 1 - final_logic
            
        prediction = "TÀI" if final_logic == 0 else "XỈU"
        confidence = (max(votes.count(0), votes.count(1)) / 1000) * 100
        
        return prediction, confidence

# =============================================================================
# [LAYER 2] ĐIỀU HÀNH
# =============================================================================
def main():
    if 'history' not in st.session_state: st.session_state.history = []
    
    st.markdown("<h2 style='text-align:center; color:#555;'>1000-AI SUPREME COMMAND</h2>", unsafe_allow_html=True)
    
    h_input = st.text_input("📡 NHẬP MÃ HASH PHIÊN:", placeholder="Dán mã Hash tại đây...")

    if st.button("🔥 PHÂN TÍCH VÀ XUẤT LỆNH"):
        if len(h_input) >= 32:
            with st.spinner("1000 AI ĐANG HỘI Ý..."):
                time.sleep(1.5)
            
            ai = SupremeAI(h_input, st.session_state.history)
            res, conf = ai.get_final_command()
            
            # HIỂN THỊ 1 LỆNH DUY NHẤT
            color = "#FF073A" if res == "TÀI" else "#05D9E8"
            st.markdown(f"<div class='single-command' style='color: {color}; text-shadow: 0 0 50px {color};'>{res}</div>", unsafe_allow_html=True)
            
            # THÔNG TIN PHỤ TỐI GIẢN
            st.markdown(f"""
            <div class='info-box'>
                <b>ĐỘ ĐỒNG THUẬN:</b> {conf:.2f}% | <b>TRẠNG THÁI:</b> ĐÃ ĐỒNG BỘ 1000 AI
            </div>
            """, unsafe_allow_html=True)
            
            st.session_state.last_p = res
        else:
            st.error("Mã Hash không đủ độ dài!")

    # Phản hồi thắng thua để AI học nhịp sàn
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ THẮNG", use_container_width=True):
            if 'last_p' in st.session_state:
                st.session_state.history.append({"status": "Thắng"})
                st.rerun()
    with col2:
        if st.button("❌ THUA", use_container_width=True):
            if 'last_p' in st.session_state:
                st.session_state.history.append({"status": "Thua"})
                st.rerun()

if __name__ == "__main__":
    main()
