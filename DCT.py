import numpy as np
from scipy.fftpack import dct  # 或從 scipy.fft 匯入 dct

def compute_dct(density_array, dct_type=2, norm='ortho'):
    """
    將一維密度變化陣列轉換成 DCT 特徵。
    
    參數：
        density_array (np.ndarray): 一維密度變化資料。
        dct_type (int): DCT 類型，通常使用 type 2。
        norm (str): 正規化方式，建議使用 'ortho'。

    回傳：
        dct_result (np.ndarray): DCT 轉換後的結果。
    """
    # 檢查輸入是否為一維
    if density_array.ndim != 1:
        raise ValueError("輸入必須是一維陣列")
    
    return dct(density_array, type=dct_type, norm=norm)

# 範例密度變化資料
density = np.array([0.1, 0.3, 0.5, 0.4, 0.2, 0.1, 0.0])

# 計算 DCT
dct_features = compute_dct(density)
print("DCT 特徵：", dct_features)
