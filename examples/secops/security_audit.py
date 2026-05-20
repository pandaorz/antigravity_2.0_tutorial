#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Antigravity v2 - SecOps 資安檢測與代碼審查工具 (Secure Coding Practice)
------------------------------------------------------------------
符合規範：OWASP Top 10 / CWE-89 (SQL Injection)
功能：
1. 實作一個簡單但高效的 SAST (靜態代碼分析) 引擎。
2. 掃描特定程式碼中寫死的金鑰與字串拼接 SQL 注入風險。
3. 提供具體漏洞代碼與「SQLite 參數化查詢」安全修補代碼的真實比較。
"""

import re
import sys

# 1. 模擬「含有 SQL 注入漏洞的危險代碼」
VULNERABLE_CODE = """
def get_user_profile_bad(user_id):
    # ❌ 嚴重漏洞 (CWE-89): 直接使用字串拼接 SQL 語句！
    # 如果 user_id 傳入 "1' OR '1'='1"，將會洩漏所有用戶資料！
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    return cursor.fetchall()
"""

# 2. 模擬「修補後的安全程式碼」
SECURE_CODE = """
def get_user_profile_good(user_id):
    # ✅ 安全實踐 (OWASP A03): 使用 SQLite 的參數化查詢 (Prepared Statement)
    # 資料庫引擎會將 user_id 視為純參數，杜絕 SQL 注入攻擊！
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    return cursor.fetchall()
"""

# 3. 靜態弱點檢測引擎 (SAST Engine)
class SecurityScanner:
    def __init__(self):
        # 定義檢測正則表達式與說明
        self.rules = [
            {
                "id": "CWE-89",
                "name": "SQL Injection Risk",
                "pattern": r"\.execute\(\s*['\"].*SELECT.*FROM.*\+\s*\w+",
                "severity": "HIGH",
                "description": "發現使用 '+' 拼接 SQL 字串！這會直接導致 SQL 注入漏洞，允許攻擊者控制資料庫。",
                "remediation": "請改用參數化查詢 (Prepared Statements)，例如：cursor.execute('SELECT * FROM t WHERE id = ?', (user_id,))"
            },
            {
                "id": "CWE-798",
                "name": "Hardcoded Credential",
                "pattern": r"(api_key|password|secret)\s*=\s*['\"][a-zA-Z0-9_-]{16,}['\"]",
                "severity": "HIGH",
                "description": "程式碼中疑似含有寫死的 API 金鑰或密碼！",
                "remediation": "請將敏感金鑰移至環境變數中，並使用 os.environ.get() 進行讀取。"
            }
        ]

    def scan_code(self, code_content, filename="SimulatedCode"):
        """掃描代碼並輸出資安報告"""
        findings = []
        lines = code_content.split('\n')
        
        for rule in self.rules:
            for line_idx, line in enumerate(lines, 1):
                if re.search(rule["pattern"], line):
                    findings.append({
                        "file": filename,
                        "line": line_idx,
                        "content": line.strip(),
                        "rule_id": rule["id"],
                        "rule_name": rule["name"],
                        "severity": rule["severity"],
                        "desc": rule["description"],
                        "remediation": rule["remediation"]
                    })
        return findings

def main():
    scanner = SecurityScanner()
    
    print("==========================================")
    print("🛡️ Antigravity SecOps 靜態安全掃描引擎")
    print("==========================================")
    
    # 測試一：掃描漏洞代碼
    print("[RUN] 正在掃描含有漏洞的代碼...")
    bad_findings = scanner.scan_code(VULNERABLE_CODE, "get_user_profile_bad")
    
    # 測試二：掃描安全代碼
    print("[RUN] 正在掃描修補後的安全代碼...")
    good_findings = scanner.scan_code(SECURE_CODE, "get_user_profile_good")
    
    # 4. 輸出資安稽核報告
    print("\n📊 掃描報告結果：")
    print("------------------------------------------")
    
    all_findings = bad_findings + good_findings
    if not all_findings:
        print("🟢 恭喜！未偵測到任何安全漏洞。")
    else:
        for f in all_findings:
            print(f"🚨 [{f['severity']}] 發現弱點: {f['rule_name']} ({f['rule_id']})")
            print(f"   位置: {f['file']}.py (第 {f['line']} 行)")
            print(f"   程式碼: {f['content']}")
            print(f"   說明: {f['desc']}")
            print(f"   🛡️ 修補建議: {f['remediation']}")
            print("------------------------------------------")
            
    print("✅ 安全稽核完成。")
    print("==========================================")

if __name__ == "__main__":
    main()
