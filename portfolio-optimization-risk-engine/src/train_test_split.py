# =========================================================
# TRAIN / TEST SPLIT
# =========================================================

def train_test_split(simple_stock_returns_A, simple_stock_returns_B):
    
    train_returns_A = simple_stock_returns_A.loc["2024":"2025"]
    test_returns_A = simple_stock_returns_A.loc["2026":]
    
    train_returns_B = simple_stock_returns_B.loc["2024":"2025"]
    test_returns_B = simple_stock_returns_B.loc["2026":]

    return train_returns_A, test_returns_A, train_returns_B, test_returns_B



