#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Antigravity v2 - 科學與文獻分析工具: PubMed 醫學文獻檢索器
------------------------------------------------------------------
功能：
1. 使用 Python 標準庫 urllib，不依賴第三方套件，自動檢索 NCBI PubMed 資料庫。
2. 查詢指定醫學關鍵字（例如 CAR-T、Lung Cancer 治療進展）。
3. 取得最新 5 篇文獻的 Title、Journal、Date、Authors 與 PMID。
4. 自動在本地生成精美的 Markdown 格式文獻綜述檔案 'literature_review.md'。
"""

import argparse
import json
import urllib.parse
import urllib.request
import sys
import os

# 1. NCBI e-utilities API 端點
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def search_pubmed(query, retmax=5):
    """步驟一：搜尋 PubMed 關鍵字，取得 PMID 列表"""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": retmax
    }
    
    url_params = urllib.parse.urlencode(params)
    request_url = f"{ESEARCH_URL}?{url_params}"
    
    try:
        req = urllib.request.Request(request_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode('utf-8'))
            pmid_list = data.get("esearchresult", {}).get("idlist", [])
            return pmid_list
    except Exception as e:
        print(f"❌ [錯誤] 搜尋 PubMed 時發生網路異常: {str(e)}", file=sys.stderr)
        return []

def fetch_summaries(pmid_list):
    """步驟二：取得 PMID 列表中每篇文獻的詳細 Summary"""
    if not pmid_list:
        return {}
        
    pmids_str = ",".join(pmid_list)
    params = {
        "db": "pubmed",
        "id": pmids_str,
        "retmode": "json"
    }
    
    url_params = urllib.parse.urlencode(params)
    request_url = f"{ESUMMARY_URL}?{url_params}"
    
    try:
        req = urllib.request.Request(request_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode('utf-8'))
            results = data.get("result", {})
            return results
    except Exception as e:
        print(f"❌ [錯誤] 拉取文獻 Summary 時發生網路異常: {str(e)}", file=sys.stderr)
        return {}

def generate_markdown_review(query, pmid_list, summaries_data, output_file="literature_review.md"):
    """步驟三：將檢索結果轉化為精美高可讀性的 Markdown 綜述報告"""
    
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# 🔬 醫學文獻檢索綜述報告：{query}\n\n")
            f.write(f"> **檢索來源**：NCBI PubMed 資料庫  \n")
            f.write(f"> **產出時間**：隨機自動生成  \n")
            f.write(f"> **檢索筆數**：最新 {len(pmid_list)} 筆相關研究\n\n")
            f.write("---\n\n")
            
            if not pmid_list:
                f.write("⚠️ *未查找到相關醫學文獻。*\n")
                return
                
            for idx, pmid in enumerate(pmid_list, 1):
                article = summaries_data.get(pmid, {})
                if not article or "title" not in article:
                    continue
                    
                title = article.get("title", "無標題")
                journal = article.get("source", "未知期刊")
                pubdate = article.get("pubdate", "未知時間")
                
                # 取得作者清單
                authors_list = article.get("authors", [])
                authors = ", ".join([auth.get("name", "") for auth in authors_list[:3]])
                if len(authors_list) > 3:
                    authors += " et al."
                
                # 寫入 Markdown
                f.write(f"### {idx}. {title}\n")
                f.write(f"*   **重要作者**: {authors}\n")
                f.write(f"*   **發表期刊/日期**: *{journal}* ({pubdate})\n")
                f.write(f"*   **PubMed ID (PMID)**: [{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)\n\n")
            
            f.write("---\n")
            f.write("🔍 *本報告由 Antigravity v2 科學文獻分析模組自動彙整生成。*\n")
            
        print(f"✅ [成功] 醫學文獻綜述已成功生成！")
        print(f"報告儲存路徑: {os.path.abspath(output_file)}")
        
    except Exception as e:
        print(f"❌ [錯誤] 寫入 Markdown 報告時發生異常: {str(e)}", file=sys.stderr)

def main():
    # 支援指令列參數 (預設為 CAR-T 細胞療法)
    parser = argparse.ArgumentParser(description="PubMed 醫學文獻檢索綜述工具")
    parser.add_argument("--query", type=str, default="CAR-T therapy solid tumors", help="文獻搜尋關鍵字")
    args = parser.parse_args()
    
    print("==========================================")
    print("🔬 Antigravity PubMed 科學文獻檢索系統")
    print("==========================================")
    print(f"檢索關鍵字: '{args.query}'")
    
    # 1. 執行搜尋
    print("[RUN] 正在請求 NCBI PubMed API 搜尋文獻...")
    pmid_list = search_pubmed(args.query)
    
    # 2. 獲取中介資料
    print(f"[RUN] 搜尋成功，取得 PMID 列表: {pmid_list}。正在拉取詳細資訊...")
    summaries = fetch_summaries(pmid_list)
    
    # 3. 輸出 Markdown
    generate_markdown_review(args.query, pmid_list, summaries)
    print("==========================================")

if __name__ == "__main__":
    main()
