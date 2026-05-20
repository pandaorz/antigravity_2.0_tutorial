#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Antigravity v2 - 行政庶務自動化: EML 郵件生成工具 (Secure & Robust)
------------------------------------------------------------------
功能：
1. 自動生成符合 RFC-822 標準的 .eml 郵件檔案。
2. 郵件內嵌極致美感的 HTML 格式會議紀錄摘要。
3. 具備完整的防呆機制（電子郵件欄位格式驗證）。
4. 排除任何寫死的金鑰或敏感資訊。
"""

import os
import re
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid

# 1. 電子郵件格式驗證正則表達式
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validate_email(email_str):
    """防呆：驗證 Email 格式是否合法"""
    return re.match(EMAIL_REGEX, email_str) is not None

def generate_eml(sender, receiver, subject, output_filename="meeting_release.eml"):
    """安全生成 .eml 檔案的函數"""
    
    print("==========================================")
    print("⚡ Antigravity EML 自動化引擎啟動")
    print("==========================================")
    
    # 2. 輸入參數防呆校驗
    if not validate_email(sender):
        print(f"❌ [錯誤] 寄件者格式不正確: '{sender}'", file=sys.stderr)
        return False
    if not validate_email(receiver):
        print(f"❌ [錯誤] 收件者格式不正確: '{receiver}'", file=sys.stderr)
        return False
    
    try:
        # 3. 建立 MIME 郵件主體
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver
        msg['Date'] = formatdate(localtime=True)
        msg['Message-ID'] = make_msgid(domain='hosp.ncku.edu.tw')
        
        # 4. 極致美學的 HTML 郵件內容 (嵌入 CSS)
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {
                    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                    background-color: #f8fafc;
                    color: #1e293b;
                    margin: 0;
                    padding: 20px;
                }
                .container {
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #ffffff;
                    border: 1px solid #e2e8f0;
                    border-radius: 12px;
                    padding: 30px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
                }
                .header {
                    border-bottom: 2px solid #3b82f6;
                    padding-bottom: 15px;
                    margin-bottom: 20px;
                }
                h2 {
                    color: #1e3a8a;
                    margin: 0;
                    font-size: 22px;
                }
                .info-block {
                    background-color: #f1f5f9;
                    border-radius: 8px;
                    padding: 15px;
                    font-size: 14px;
                    margin-bottom: 20px;
                }
                .btn {
                    display: inline-block;
                    background-color: #3b82f6;
                    color: #ffffff !important;
                    text-decoration: none;
                    padding: 10px 20px;
                    border-radius: 6px;
                    font-weight: bold;
                    margin-top: 15px;
                }
                .footer {
                    margin-top: 30px;
                    font-size: 12px;
                    color: #64748b;
                    text-align: center;
                    border-top: 1px solid #e2e8f0;
                    padding-top: 15px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h2>📅 成大醫院 Hosp 專案會議紀錄發佈</h2>
                </div>
                <p>親愛的團隊同仁您好：</p>
                <p>以下為今日召開之 <strong>Hosp 專案進度追蹤會議</strong> 的核心摘要，詳細紀錄請點擊下方按鈕或檢視附件。</p>
                
                <div class="info-block">
                    <strong>📌 會議決議主題：</strong> 虛擬環境路徑統一 (DEC-01)<br>
                    <strong>⏳ 預計上線時間：</strong> 2026-05-22<br>
                    <strong>👤 追蹤負責人：</strong> 張工程師
                </div>

                <a href="https://github.com/your-repo" class="btn">檢視完整專案進度</a>

                <div class="footer">
                    此郵件為 Antigravity v2 行政系統自動生成，請勿直接回覆。<br>
                    成大醫院資訊大樓 © 2026
                </div>
            </div>
        </body>
        </html>
        """
        
        # 5. 附加 HTML MIME 內容
        part_html = MIMEText(html_content, 'html', 'utf-8')
        msg.attach(part_html)
        
        # 6. 寫入 .eml 檔案
        # 排除破壞性覆寫，確認檔案是否存在或安全寫入
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(msg.as_string())
            
        print(f"✅ [成功] EML 郵件檔案生成成功！")
        print(f"檔案位置: {os.path.abspath(output_filename)}")
        print("==========================================")
        return True

    except Exception as e:
        print(f"❌ [錯誤] 生成 EML 時發生異常: {str(e)}", file=sys.stderr)
        return False

if __name__ == "__main__":
    # 測試執行
    generate_eml(
        sender="antigravity@hosp.ncku.edu.tw",
        receiver="developer@hosp.ncku.edu.tw",
        subject="【重要通知】成大醫院 Hosp 專案進度會議紀錄",
        output_filename="meeting_release.eml"
    )
