import streamlit as st
import numpy as np
import pandas as pd
import time
import random
import plotly.graph_objects as go
from datetime import datetime

# =============================================================================
# [LAYER 0] GIAO DIỆN SIÊU CẤP (ULTRA UI)
# =============================================================================
st.set_page_config(page_title="SUPREME CONVERGENCE AI", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Major+Mono+Display&family=JetBrains+Mono:wght@400;700&display=swap');
    .stApp { background-color: #000; color: #00FF41; font-family: 'JetBrains Mono', monospace; }
    .prediction-giant {
        font-family: 'Major Mono Display', monospace;
        font-size: clamp(100px, 20vw, 300px);
        text-align: center;
        margin: 20px 0;
        text-shadow: 0 0 50px #00FF41;
        line-height: 0.8;
    }
    .council-box {
        border: 1px solid #111;
        padding: 15px;
        background: rgba(0, 255, 65, 0.02);
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# =============================================================================
# [LAYER 1] LÕI HỘI TỤ (CONVERGENCE CORE)
# =============================================================================
class SupremeCouncil:
    def __init__(self, hash_code, history):
        self.hash = hash_code
        self.history = history
        self.agents = ["AETHER", "CHRONOS", "VOID", "PHANTOM", "TITAN", "NEBULA", "ORACLE", "MATRIX", "CYPHER", "GENESIS"]

    def analyze(self):
        # Chuyển Hash thành Vector số học
        hex_data = [int(c, 16) for c in self.hash if c in "0123456789abcdef"]
        core_value = sum(hex_data)
        
        # Nhịp sàn (Lose Streak)
        lose_count = 0
        for h in reversed([x['status'] for x in self.history]):
            if h == "Thua": lose_count += 1
            else: break
        
        # THUẬT TOÁN HỘI TỤ (CONVERGENCE ALGORITHM)
        # 10 AI phân tích 10 vùng dữ liệu khác nhau nhưng cùng dùng 1 Lõi Logic
        # Mục tiêu: Đạt 100% đồng thuận trên cùng 1 tín hiệu
        
        main_logic = (core_value + len(hex_data)) % 2
        
        # Bẻ lái theo nhịp thua (Adaptive Intelligence)
        if lose_count >= 1:
            main_logic = 1 - main_logic
            
        final_signal = "TÀI 🔴" if main_logic == 0 else "XỈU 🔵"
        
        reports = []
        for name in self.agents:
            reports.append({
                "name": name,
                "signal": final_signal, # Tất cả đều ra cùng 1 kết quả
                "reason": random.choice([
                    "Hội tụ Ma trận Fractal thành công.",
                    "Đồng bộ xung nhịp nhị phân tuyệt đối.",
                    "Xác nhận Điểm Giao Thoa (Singularity).",
                    "Cân bằng Entropy đạt trạng thái tĩnh."
                ])
            })
            
        return final_signal, reports

# =============================================================================
# [LAYER 2] ĐIỀU HÀNH
# =============================================================================
def main():
    if 'history' not in st.session_state: st.session_state.history = []
    
    st.markdown("<h1 style='text-align:center;'>SUPREME CONVERGENCE AI</h1>", unsafe_allow_html=True)
    st.write("---")

    h_input = st.text_input("📡 NHẬP MÃ HASH (DỮ LIỆU GỐC):")

    if st.button("🚀 KÍCH HOẠT HỘI TỤ 10 AI"):
        if len(h_input) >= 32:
            with st.spinner("Đang ép 10 AI hội tụ vào một thực tại..."):
                time.sleep(1.5)
            
            council = SupremeCouncil(h_input, st.session_state.history)
            res, reports = council.analyze()
            
            # HIỂN THỊ TÍN HIỆU ĐỒNG NHẤT
            st.markdown(f"<div class='prediction-giant' style='color:{'#FF3131' if 'TÀI' in res else '#00DFFF'};'>{res}</div>", unsafe_allow_html=True)
            
            st.markdown("### 🏛️ HỘI ĐỒNG ĐỒNG THUẬN (10/10)")
            cols = st.columns(5)
            for i, r in enumerate(reports):
                with cols[i % 5]:
                    st.markdown(f"""
                    <div class='council-box'>
                        <p style='font-size:10px; color:#555;'>{r['name']}</p>
                        <p style='color:{'#FF3131' if 'TÀI' in res else '#00DFFF'}; font-weight:bold;'>{r['signal']}</p>
                        <p style='font-size:9px;'>{r['reason']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.session_state.last_p = res
        else:
            st.error("Hash không hợp lệ!")

    # Phản hồi
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ THẮNG (ĐỒNG BỘ)", use_container_width=True):
            if 'last_p' in st.session_state:
                st.session_state.history.append({"status": "Thắng"})
                st.rerun()
    with c2:
        if st.button("❌ THUA (CỐ ĐỊNH LẠI AI)", use_container_width=True):
            if 'last_p' in st.session_state:
                st.session_state.history.append({"status": "Thua"})
                st.rerun()

if __name__ == "__main__":
    main()
