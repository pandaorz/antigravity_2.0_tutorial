#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Antigravity v2 - 數據分析與視覺化 (Data Science & Visualisation)
------------------------------------------------------------------
功能：
1. 讀取 sales_data.csv 檔案。
2. 利用 Pandas 進行數據聚合，彙整各產品線的總銷售額、總成本與淨利潤。
3. 計算產品毛利率。
4. 使用 Matplotlib 繪製極具美感的高級 HSL 色調長條圖。
5. 具備套件缺失時的「防呆 Step-by-Step 安裝引導」。
"""

import os
import sys

# 1. 套件依賴性防呆檢查
try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError:
    print("❌ [錯誤] 偵測到您的 Python 環境尚未安裝 pandas 或 matplotlib 套件！")
    print("💡 請在終端機中執行以下指令進行安裝：")
    print("------------------------------------------")
    print("  pip install pandas matplotlib")
    print("------------------------------------------")
    sys.exit(1)

def run_analysis(csv_path="sales_data.csv", output_img="sales_performance.png"):
    print("==========================================")
    print("📊 Antigravity 數據分析與視覺化引擎啟動")
    print("==========================================")
    
    if not os.path.exists(csv_path):
        print(f"❌ [錯誤] 找不到資料源: {csv_path}。請確認檔案是否已建立。", file=sys.stderr)
        return False
        
    try:
        # 2. 讀取數據
        print(f"[RUN] 正在讀取資料: {csv_path} ...")
        df = pd.read_csv(csv_path)
        
        # 3. 數據彙整與計算 (Aggregation)
        print("[RUN] 正在使用 Pandas 進行多維度彙整...")
        summary = df.groupby('Category').agg({
            'Sales': 'sum',
            'Cost': 'sum'
        }).reset_index()
        
        # 計算淨利潤與毛利率
        summary['Profit'] = summary['Sales'] - summary['Cost']
        summary['Margin_Percent'] = (summary['Profit'] / summary['Sales']) * 100
        summary['Margin_Percent'] = summary['Margin_Percent'].round(2)
        
        # 輸出終端機表格
        print("\n📊 數據彙整分析表：")
        print(summary.to_string(index=False, formatters={
            'Sales': '{:,.0f}'.format,
            'Cost': '{:,.0f}'.format,
            'Profit': '{:,.0f}'.format,
            'Margin_Percent': '{:.2f}%'.format
        }))
        print("------------------------------------------")
        
        # 4. 使用 Matplotlib 繪製極致美感圖表
        print("[RUN] 正在使用 Matplotlib 繪製高視覺質感圖表...")
        
        # 設定暗黑與和諧色彩系統 (Sleek Theme)
        plt.style.use('ggplot')
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # 高級調色盤 (HSL Tailored Colors)
        colors = ['#3b82f6', '#8b5cf6', '#10b981'] # Blue, Purple, Green
        
        bars = ax.bar(
            summary['Category'], 
            summary['Sales'], 
            color=colors, 
            edgecolor='rgba(255,255,255,0.1)', 
            width=0.5,
            label='Total Sales'
        )
        
        # 標題與標籤美化
        ax.set_title("Sales Performance by Category", fontsize=14, fontweight='bold', pad=15)
        ax.set_xlabel("Product Category", fontsize=11, labelpad=10)
        ax.set_ylabel("Total Sales (USD)", fontsize=11, labelpad=10)
        
        # 在長條圖上方加入數值標籤與毛利提示
        for i, bar in enumerate(bars):
            yval = bar.get_height()
            margin = summary.loc[i, 'Margin_Percent']
            ax.text(
                bar.get_x() + bar.get_width()/2.0, 
                yval + 30, 
                f"${yval:,.0f}\nMargin: {margin}%", 
                ha='center', 
                va='bottom', 
                fontsize=9, 
                fontweight='semibold'
            )
            
        plt.tight_layout()
        
        # 5. 儲存圖片
        plt.savefig(output_img, dpi=300)
        plt.close()
        
        print(f"✅ [成功] 銷售圖表已順利生成！")
        print(f"圖表位置: {os.path.abspath(output_img)}")
        print("==========================================")
        return True

    except Exception as e:
        print(f"❌ [錯誤] 進行數據分析時發生異常: {str(e)}", file=sys.stderr)
        return False

if __name__ == "__main__":
    # 解析同目錄下的 csv 檔案
    csv_file = os.path.join(os.path.dirname(__file__), "sales_data.csv")
    run_analysis(csv_file)
