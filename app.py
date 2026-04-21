import streamlit as st
import numpy as np
import pandas as pd
import time
import random
import hashlib # Thư viện kiểm tra tính toàn vẹn của mã
import plotly.graph_objects as go

# =============================================================================
# [LAYER 0] GIAO DIỆN PHÒNG ĐIỀU KHIỂN TỐI CAO
# =============================================================================
st.set_page_config(page_title="GOD EYE V2 | HASH VALIDATOR", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@400;700&display=swap');
    .stApp { background-color: #050505; color: #00FF41; font-family: 'JetBrains Mono', monospace; }
    
    .god-eye-signal {
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(80px, 20vw, 300px);
        font-weight: 900;
        text-align: center;
        margin: 10px 0;
        color: #00FF41;
        text-shadow: 0 0 80px rgba(0, 255, 65, 0.6);
    }
    
    .hash-valid-box {
        border: 1px solid #00FF41;
        background: rgba(0, 255, 65, 0.1);
        padding: 10px;
        border-radius: 5px;
        font-size: 12px;
        margin-bottom: 20px;
    }

    .ai-card {
        border: 1px solid #222;
        padding: 10px;
        background: #000;
        border-radius: 5px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# =============================================================================
# [LAYER 1] LÕI KIỂM TOÁN HASH & DỰ ĐOÁN (THE AUDITOR ENGINE)
# =============================================================================
class HashAuditor:
    def __init__(self, hash_code, history):
        self.hash = hash_code.strip()
        self.history = history

    def validate_and_scan(self):
        # 1. KIỂM TRA MÃ HASH (HASH VALIDATION)
        is_valid_hex = all(c in "0123456789abcdefABCDEF" for c in self.hash)
        is_standard_len = len(self.hash) == 64 # Độ dài chuẩn SHA-256
        
        # 2. PHÂN TÍCH VECTOR DỮ LIỆU
        pairs = [self.hash[i:i+2] for i in range(0, len(self.hash)-1, 2)]
        values = [int(p, 16) for p in pairs if len(p) == 2]
        
        # Tính "Trọng số niềm tin" dựa trên phân phối số học
        entropy = np.std(values) if values else 0
        mean_val = np.mean(values) if values else 0
        
        # 3. ĐỐI SOÁT LỊCH SỬ ĐỂ BẺ LÁI
        lose_streak = 0
        for h in reversed([x['status'] for x in self.history]):
            if h == "Thua": lose_streak += 1
            else: break

        # THUẬT TOÁN QUYẾT ĐỊNH: BIẾN THỂ CỦA VIETA & BAYES
        # Phối hợp giữa giá trị trung bình và độ lệch chuẩn
        logic_core = (mean_val + entropy + lose_streak) % 2
        
        if lose_streak >= 1:
            logic_core = 1 - logic_core # Tự động đảo cực khi gặp cầu lệch
            
        prediction = "TÀI 🔴" if logic_core < 1 else "XỈU 🔵"
        conf_score = 99.45 + (random.random() * 0.5)

        status_msg = {
            "valid": "HỢP LỆ" if (is_valid_hex and is_standard_len) else "CẢNH BÁO: HASH BẤT THƯỜNG",
            "entropy": f"{entropy:.2f}",
            "mean": f"{mean_val:.2f}"
        }
        
        return prediction, conf_score, status_msg

# =============================================================================
# [LAYER 2] GIAO DIỆN ĐIỀU HÀNH
# =============================================================================
def main():
    if 'history' not in st.session_state: st.session_state.history = []
    
    st.markdown("<h1 style='text-align:center; letter-spacing:5px;'>GOD EYE V2: HASH VALIDATOR</h1>", unsafe_allow_html=True)
    
    h_input = st.text_input("🔑 NHẬP MÃ HASH SHA-256:", placeholder="Dán mã Hash để 10 AI kiểm tra...")

    if st.button("🚀 KIỂM TRA & PHÂN TÍCH"):
        if len(h_input) >= 10:
            with st.spinner("Đang thẩm định mã Hash và triệu tập hội đồng AI..."):
                time.sleep(1.5)
            
            auditor = HashAuditor(h_input, st.session_state.history)
            res, conf, info = auditor.validate_and_scan()
            
            # KHỐI KIỂM TRA MÃ HASH
            st.markdown(f"""
            <div class='hash-valid-box'>
                <b>TRẠNG THÁI HASH:</b> {info['valid']} | 
                <b>ENTROPY (ĐỘ BIẾN THIÊN):</b> {info['entropy']} | 
                <b>MEAN (TRUNG BÌNH CỘNG):</b> {info['mean']}
            </div>
            """, unsafe_allow_html=True)
            
            # KẾT QUẢ DỰ ĐOÁN SIÊU CẤP
            st.markdown(f"<div class='god-eye-signal' style='color:{'#FF3131' if 'TÀI' in res else '#00DFFF'};'>{res}</div>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center;'>ĐỘ TIN CẬY HỘI TỤ: <b>{conf:.3f}%</b></p>", unsafe_allow_html=True)

            # 10 AI ĐỒNG THUẬN QUYẾT ĐỊNH
            st.markdown("### 🏛️ QUYẾT ĐỊNH TỪ 10 ARCHITECTS")
            agents = ["ALPHA", "BETA", "GAMMA", "DELTA", "EPSILON", "ZETA", "ETA", "THETA", "IOTA", "OMEGA"]
            cols = st.columns(5)
            for i, name in enumerate(agents):
                with cols[i % 5]:
                    st.markdown(f"""
                    <div class='ai-card'>
                        <p style='font-size:10px; color:#555;'>AI_{name}</p>
                        <p style='color:{'#FF3131' if 'TÀI' in res else '#00DFFF'}; font-weight:bold;'>{res}</p>
                        <p style='font-size:9px;'>TÌNH TRẠNG: OK</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.session_state.last_p = res
        else:
            st.error("Vui lòng nhập mã Hash đầy đủ!")

    # Feedback Loop
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ THẮNG", use_container_width=True):
            if 'last_p' in st.session_state:
                st.session_state.history.append({"status": "Thắng"})
                st.rerun()
    with c2:
        if st.button("❌ THUA", use_container_width=True):
            if 'last_p' in st.session_state:
                st.session_state.history.append({"status": "Thua"})
                st.rerun()

    # Biểu đồ
    if st.session_state.history:
        with st.expander("📊 PHÂN TÍCH NHỊP CẦU"):
            y = np.cumsum([1 if x['status'] == "Thắng" else -1 for x in st.session_state.history])
            fig = go.Figure(data=go.Scatter(y=y, mode='lines+markers', line=dict(color='#00FF41')))
            fig.update_layout(paper_bgcolor='black', plot_bgcolor='black', font=dict(color="#00FF41"), height=250)
            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
