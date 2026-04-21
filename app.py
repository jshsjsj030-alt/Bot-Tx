import streamlit as st
import time
import random
from datetime import datetime
import pandas as pd

# --- 1. GIAO DIỆN HACKER SUPREME (RGB DARK MODE) ---
st.set_page_config(page_title="vINFINITE OMNI-REPLICA", page_icon="👹", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF00; font-family: 'Consolas', monospace; }
    .console-box { border: 2px solid #00FF00; padding: 30px; background: #050505; border-radius: 20px; box-shadow: 0 0 40px #00FF00; margin-bottom: 25px; text-align: center; }
    .titan-box { border: 3px solid #FFD700; padding: 30px; background: #0a0a00; border-radius: 20px; box-shadow: 0 0 60px #FFD700; margin-bottom: 25px; text-align: center; }
    .void-box { border: 2px solid #FF00FF; padding: 30px; background: #0a000a; border-radius: 20px; box-shadow: 0 0 50px #FF00FF; margin-bottom: 25px; text-align: center; }
    .warning-box { border: 2px solid #FF4B4B; padding: 15px; background: #200000; border-radius: 10px; color: #FF4B4B; margin-top: 15px; font-weight: bold; }
    .pred-text { font-size: 85px; font-weight: bold; letter-spacing: 5px; margin: 15px 0; }
    .glitch { animation: pulse 0.8s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }
    </style>
""", unsafe_allow_html=True)

# --- 2. BỘ THƯ VIỆN PHẢN HỒI (CHẤT RIÊNG CỦA MÌNH) ---
LOG_MSGS = {
    "WIN": ["Khớp nhịp sàn tuyệt đối. Tiếp tục duy trì!", "Thuật toán đang đè bẹp bộ Seed của nhà cái.", "Hệ thống đang trong trạng thái Hyper-Flow."],
    "LOSE": ["Phát hiện nhịp bẻ! AI đang đảo ngược logic.", "Sàn đổi mã hóa. Đang tái cấu trúc thuật toán.", "Cảnh báo: Nhịp Hash đang bị nhiễu. Đảo lệnh!"],
    "TITAN": ["TITAN ACTIVATED: Quét sạch sàn!", "Toán học là chân lý, bệt là thời cơ.", "Ultimate Sync: Đỉnh cao phân tích."],
    "INIT": ["Hệ thống vInfinite Omni đã sẵn sàng. Đang chờ dữ liệu..."]
}

# --- 3. LÕI THUẬT TOÁN ĐA TẦNG (FULL OPTION) ---
def omni_replica_engine(hash_val, history):
    # Trích xuất lịch sử
    results = [h['status'] for h in history]
    win_s, lose_s = 0, 0
    for res in reversed(results):
        if res == "Thắng": win_s += 1; lose_s = 0
        elif res == "Thua": lose_s += 1; win_s = 0
        else: break

    # A. PHÂN TÍCH ENTROPY (SOI SEED GIẢ)
    unique_chars = len(set(hash_val))
    is_risky = unique_chars < 12 # Dấu hiệu mã bị can thiệp

    # B. CHỌN MODE VÀ THUẬT TOÁN (TẤT CẢ TRONG 1)
    if win_s >= 4:
        # THUẬT TOÁN TITAN: XOR 3 LỚP (ĐẦU - GIỮA - CUỐI)
        engine = "TITAN ULTIMATE"; mode = "GOD-MODE"; box = "titan-box"
        core_score = int(hash_val[:4], 16) ^ int(hash_val[30:34], 16) ^ int(hash_val[-4:], 16)
        conf = 99
    elif lose_s >= 2:
        # THUẬT TOÁN DEEP-VOID: SOI LÕI GIỮA (BẢO VỆ VỐN)
        engine = "DEEP-VOID (PROTECT)"; mode = "SAFETY-GUARD"; box = "void-box"
        core_score = sum(int(c, 16) for c in hash_val[16:48] if c in "0123456789abcdef")
        conf = 92
    else:
        # THUẬT TOÁN PENTAGON: SOI TRỌNG SỐ BIÊN
        engine = "PENTAGON SCAN"; mode = "HYPER-SYNC"; box = "console-box"
        core_score = int(hash_val[:8], 16) + int(hash_val[-8:], 16)
        conf = 85

    # C. LOGIC DỰ ĐOÁN & CƠ CHẾ ĐẢO LỆNH (DYNAMIC REVERSAL)
    prediction = "TÀI 🔴" if core_score % 2 == 0 else "XỈU 🔵"
    
    # Nếu thua tay trước, AI tự động "nghi ngờ chính mình" và đảo ngược kết quả
    if lose_s >= 1:
        prediction = "XỈU 🔵" if prediction == "TÀI 🔴" else "TÀI 🔴"
        mode += " [REVERSED]"

    return prediction, conf, mode, engine, box, is_risky

# --- 4. GIAO DIỆN VẬN HÀNH ---
if 'history' not in st.session_state: st.session_state.history = []
if 'ai_log' not in st.session_state: st.session_state.ai_log = random.choice(LOG_MSGS["INIT"])

st.markdown("## 👹 vINFINITE OMNI-REPLICA")
st.markdown(f"> **AI REPLICA:** *{st.session_state.ai_log}*")

# Sidebar Thống kê
with st.sidebar:
    st.header("📊 DATA CENTER")
    w = sum(1 for h in st.session_state.history if h['status'] == "Thắng")
    l = sum(1 for h in st.session_state.history if h['status'] == "Thua")
    st.metric("TỔNG THẮNG", w, delta=f"+{w}")
    st.metric("TỔNG THUA", l, delta=f"-{l}", delta_color="inverse")
    if st.button("RESET TOÀN BỘ"):
        st.session_state.history = []; st.rerun()

# Nhập mã Hash
hash_input = st.text_input("📡 DÁN MÃ HASH SHA-256:", placeholder="Nhập Hash để thực thi...")

if st.button("🚀 KÍCH HOẠT OMNI SCAN"):
    if len(hash_input) >= 32:
        with st.status("🧠 ĐANG THỰC THI TƯ DUY PHÂN TÍCH...", expanded=False):
            time.sleep(0.5); st.write("Đang đối soát XOR dải biên...");
            time.sleep(0.5); st.write("Kiểm tra Entropy mã Hash...");
            time.sleep(0.5); st.write("Kích hoạt Omni-Logic Evolution...");
        
        pred, conf, mode, eng, box_type, risky = omni_replica_engine(hash_input, st.session_state.history)
        
        st.markdown(f"""
        <div class="{box_type}">
            <p style="color: #888; letter-spacing: 2px;">{eng} | {mode}</p>
            <div class="pred-text {'glitch' if 'TITAN' in eng else ''}" style="color: {'#ff4b4b' if 'TÀI' in pred else '#4bafff'};">
                {pred}
            </div>
            <p style="font-size: 20px;">ĐỘ TIN CẬY: {conf}%</p>
        </div>
        """, unsafe_allow_html=True)
        
        if risky:
            st.markdown('<div class="warning-box">⚠️ CẢNH BÁO: Phát hiện mã Hash có dấu hiệu can thiệp (Seed ảo). Khuyên dùng: ĐỨNG NGOÀI!</div>', unsafe_allow_html=True)
    else:
        st.error("Mã Hash không hợp lệ!")

# Hệ thống nút bấm phản hồi (Nạp dữ liệu cho AI)
st.write("---")
c1, c2 = st.columns(2)
with c1:
    if st.button("✅ THẮNG (WIN)", use_container_width=True):
        st.session_state.history.append({"status": "Thắng"})
        st.session_state.ai_log = random.choice(LOG_MSGS["WIN"] if len(st.session_state.history) < 4 else LOG_MSGS["TITAN"])
        st.rerun()
with c2:
    if st.button("❌ THUA (LOSE)", use_container_width=True):
        st.session_state.history.append({"status": "Thua"})
        st.session_state.ai_log = random.choice(LOG_MSGS["LOSE"])
        st.rerun()

# Hiển thị lịch sử ngắn
if st.session_state.history:
    with st.expander("📜 NHẬT KÝ SOI"):
        st.table(pd.DataFrame(st.session_state.history).tail(5))
