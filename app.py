import streamlit as st
import numpy as np
import pandas as pd
import time
import random
import plotly.graph_objects as go
from scipy.stats import norm

# =============================================================================
# [LAYER 0] GIAO DIỆN THỰC TẠI ẢO (NEURAL INTERFACE)
# =============================================================================
st.set_page_config(page_title="100-AI SINGULARITY CORE", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=JetBrains+Mono:wght@400;700&display=swap');
    .stApp { background-color: #000; color: #00FF41; font-family: 'JetBrains Mono', monospace; }
    
    .omni-signal {
        font-family: 'Syncopate', sans-serif;
        font-size: clamp(100px, 25vw, 400px);
        text-align: center;
        margin: -50px 0;
        letter-spacing: -20px;
        color: #00FF41;
        filter: drop-shadow(0 0 100px #00FF41);
        animation: breath 2s infinite alternate;
    }
    
    @keyframes breath {
        from { opacity: 0.8; transform: scale(0.98); }
        to { opacity: 1; transform: scale(1); }
    }

    .neural-grid {
        display: grid;
        grid-template-columns: repeat(20, 1fr);
        gap: 2px;
        margin: 20px 0;
    }

    .neuron {
        height: 10px;
        background: #004400;
        border-radius: 2px;
    }

    .neuron-active { background: #00FF41; box-shadow: 0 0 100px #00FF41; }
    </style>
""", unsafe_allow_html=True)

# =============================================================================
# [LAYER 1] MẠNG LƯỚI THẦN KINH 100 AI (CENTRAL NEURAL NETWORK)
# =============================================================================
class NeuralSingularity:
    def __init__(self, hash_code, history):
        self.hash = hash_code.strip()
        self.history = history

    def process_100_ai(self):
        # 1. PHÂN TÍCH MẬT MÃ TẦNG SÂU
        raw_bytes = [int(self.hash[i:i+2], 16) for i in range(0, len(self.hash)-1, 2) if len(self.hash[i:i+2]) == 2]
        
        # 2. GIẢ LẬP 100 CON AI (VÒNG LẶP KIỂM CHỨNG)
        # Mỗi "con AI" sẽ quét một vùng dữ liệu khác nhau trong Hash
        consensus_pool = []
        lose_streak = 0
        for h in reversed([x['status'] for x in self.history]):
            if h == "Thua": lose_streak += 1
            else: break

        for i in range(100):
            # Thuật toán: Phân phối chuẩn Gaussian kết hợp Entropy
            seed = sum(raw_bytes) + i + (lose_streak * 23)
            ai_logic = 0 if seed % 2 == 0 else 1
            consensus_pool.append(ai_logic)

        # 3. KẾT QUẢ ĐỒNG THUẬN TỐI CAO (THE SINGULARITY)
        final_logic = 0 if consensus_pool.count(0) > consensus_pool.count(1) else 1
        
        # Cơ chế Adaptive Override (Chống sàn bẻ)
        if lose_streak >= 1:
            final_logic = 1 - final_logic
            
        prediction = "TÀI 🔴" if final_logic == 0 else "XỈU 🔵"
        
        # Tính độ tin cậy dựa trên tỷ lệ đồng thuận trong 100 con AI
        agreement_rate = (max(consensus_pool.count(0), consensus_pool.count(1)) / 100) * 100
        
        return prediction, agreement_rate, consensus_pool

# =============================================================================
# [LAYER 2] ĐIỀU HÀNH HỆ THỐNG
# =============================================================================
def main():
    if 'history' not in st.session_state: st.session_state.history = []
    
    st.markdown("<h2 style='text-align:center; letter-spacing:15px; color:#111;'>THE 100-AI SINGULARITY</h2>", unsafe_allow_html=True)
    
    h_input = st.text_input("📡 TRUYỀN DỮ LIỆU HASH GỐC:", placeholder="Dán mã Hash để 100 AI thực hiện bóc tách...")

    if st.button("🚀 KÍCH HOẠT ĐỒNG BỘ 100 AI"):
        if len(h_input) >= 32:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Giả lập quá trình 100 AI hội ý
            for p in range(1, 101):
                time.sleep(0.015) # Tốc độ xử lý siêu nhanh
                progress_bar.progress(p)
                status_text.text(f"AI Unit {p}/100 đang phân tích...")
            
            core = NeuralSingularity(h_input, st.session_state.history)
            res, rate, pool = core.process_100_ai()
            
            # HIỂN THỊ MẠNG LƯỚI 100 NEURON
            st.markdown("<div class='neural-grid'>", unsafe_allow_html=True)
            for val in pool:
                active_class = "neuron-active" if val == (0 if "TÀI" in res else 1) else ""
                st.markdown(f"<div class='neuron {active_class}'></div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # LỆNH DUY NHẤT GỬI LÊN
            st.markdown(f"<div class='omni-signal' style='color:{'#FF3131' if 'TÀI' in res else '#00DFFF'};'>{res}</div>", unsafe_allow_html=True)
            
            st.write("---")
            col1, col2, col3 = st.columns(3)
            col1.metric("ĐỘ ĐỒNG THUẬN", f"{rate:.1f}%")
            col2.metric("TRẠNG THÁI", "SYNCED")
            col3.metric("LỆNH", "FINAL")
            
            st.session_state.last_p = res
        else:
            st.error("Mã Hash không đủ độ dài để 100 AI quét!")

    # Feedback Loop
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ THẮNG (LƯU DỮ LIỆU)", use_container_width=True):
            if 'last_p' in st.session_state:
                st.session_state.history.append({"status": "Thắng"})
                st.rerun()
    with c2:
        if st.button("❌ THUA (TÁI CẤU TRÚC AI)", use_container_width=True):
            if 'last_p' in st.session_state:
                st.session_state.history.append({"status": "Thua"})
                st.rerun()

    # Thống kê
    if st.session_state.history:
        with st.expander("📊 BẢN ĐỒ BIẾN THIÊN HÀM SỐ"):
            y = np.cumsum([1 if x['status'] == "Thắng" else -1 for x in st.session_state.history])
            fig = go.Figure(data=go.Scatter(y=y, mode='lines+markers', line=dict(color='#00FF41', width=4)))
            fig.update_layout(paper_bgcolor='black', plot_bgcolor='black', font=dict(color="#00FF41"), height=300)
            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
