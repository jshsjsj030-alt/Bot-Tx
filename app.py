import streamlit as st
import time
import random
from datetime import datetime
import pandas as pd

# --- 1. CẤU HÌNH GIAO DIỆN HIGHTECH ---
st.set_page_config(page_title="vINFINITE SUPREME AI", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00FF00; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #111; color: #00FF00; border: 1px solid #00FF00; border-radius: 5px; }
    .console-box { border: 2px solid #00FF00; padding: 25px; background: #000; border-radius: 15px; box-shadow: 0 0 30px #00FF00; margin-bottom: 20px; }
    .prediction-text { font-size: 65px; font-weight: bold; text-align: center; text-shadow: 0 0 20px #00FF00; animation: pulse 2.5s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.8; } 100% { opacity: 1; } }
    </style>
""", unsafe_allow_html=True)

# --- 2. LOGIC PHÂN TÍCH AI (MÔ PHỎNG GEMINI) ---
def supreme_engine(hash_val, history_data):
    results = [h['status'] for h in history_data]
    win_s, lose_s = 0, 0
    for res in reversed(results):
        if res == "Thắng": win_s += 1; lose_s = 0
        elif res == "Thua": lose_s += 1; win_s = 0
        else: break

    # Chọn Engine dựa trên nhịp thắng thua
    if lose_s >= 2:
        engine = "DEEP-VOID V3"; target = hash_val[10:22]; mode = "SAFETY-GUARD"
    elif win_s >= 3:
        engine = "HYPER-FLOW V2"; target = hash_val; mode = "ULTIMATE-SYNC"
    else:
        engine = "PENTAGON V1"; target = hash_val[:8] + hash_val[-8:]; mode = "HYPER-SYNC"

    # Thuật toán tính điểm HEX
    score = sum(int(c, 16) for c in target if c in "0123456789abcdef")
    
    # Dự đoán và đảo lệnh khi thua (Evolution Logic)
    prediction = "TÀI 🔴" if score % 2 == 0 else "XỈU 🔵"
    if lose_s > 0: 
        prediction = "XỈU 🔵" if prediction == "TÀI 🔴" else "TÀI 🔴"

    conf = min(85 + (win_s * 2) - (lose_s * 10), 98)
    return prediction, conf, mode, engine

# --- 3. GIAO DIỆN CHÍNH ---
if 'history' not in st.session_state: st.session_state.history = []
if 'win_count' not in st.session_state: st.session_state.win_count = 0
if 'lose_count' not in st.session_state: st.session_state.lose_count = 0

st.markdown("### ┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┒")
st.markdown("### ┃      vINFINITE SUPREME - REPLICA FINAL v5.2      ┃")
st.markdown("### ┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┚")

# Thống kê nhanh ở Sidebar
with st.sidebar:
    st.header("📊 THỐNG KÊ")
    st.metric("THẮNG", st.session_state.win_count)
    st.metric("THUA", st.session_state.lose_count)
    if st.button("🗑️ RESET PHIÊN"):
        st.session_state.history = []; st.session_state.win_count = 0; st.session_state.lose_count = 0; st.rerun()

hash_input = st.text_input("📡 NHẬP MÃ HASH SHA-256:", placeholder="Dán mã Hash tại đây...")

if st.button("🚀 KÍCH HOẠT PHÂN TÍCH"):
    if len(hash_input) >= 16:
        with st.spinner("🧬 ĐANG ĐỒNG BỘ THUẬT TOÁN..."):
            time.sleep(1)
        
        pred, conf, mode, engine = supreme_engine(hash_input, st.session_state.history)
        
        st.markdown(f"""
        <div class="console-box">
            <p style="color: #888; font-size: 12px;">ENGINE: {engine} | STATUS: {mode}</p>
            <div class="prediction-text" style="color: {'#ff4b4b' if 'TÀI' in pred else '#4bafff'};">
                {pred}
            </div>
            <p style="text-align: center; color: #fff;">ĐỘ TIN CẬY: {conf}%</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Mã Hash không hợp lệ!")

# --- 4. ĐIỀU KHIỂN ---
st.write("---")
c1, c2 = st.columns(2)
with c1:
    if st.button("✅ THẮNG", use_container_width=True):
        st.session_state.history.append({"status": "Thắng"})
        st.session_state.win_count += 1; st.rerun()
with c2:
    if st.button("❌ THUA", use_container_width=True):
        st.session_state.history.append({"status": "Thua"})
        st.session_state.lose_count += 1; st.rerun()
