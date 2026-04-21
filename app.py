import ccxt # Thư viện lấy dữ liệu Binance
import pandas as pd

def analyze_trend():
    # 1. Lấy dữ liệu nến 1m từ Binance
    exchange = ccxt.binance()
    bars = exchange.fetch_ohlcv('BTC/USDT', timeframe='1m', limit=50)
    df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'vol'])
    
    # 2. Tính toán chỉ báo kỹ thuật (Ví dụ: SMA)
    sma = df['close'].rolling(window=5).mean()
    current_price = df['close'].iloc[-1]
    
    # 3. Đưa ra hướng đi
    if current_price > sma.iloc[-1]:
        return "TÀI (Dựa trên xu hướng BTC tăng)"
    else:
        return "XỈU (Dựa trên xu hướng BTC giảm)"

# Kết hợp với giao diện Supreme của bạn ở trên
