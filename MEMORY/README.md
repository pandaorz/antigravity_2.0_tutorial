# 🧠 Antigravity v2 專案長期記憶庫 (Memory Engine)

本檔案由 Antigravity v2 於完成階段性開發與 GitHub 推送後自動提煉生成。旨在記錄專案核心技術決策、環境配置與開發習慣，供後續開啟新對話（New Thread）時的 Agent 自動讀取，以維持跨對話的完美連續性，落實 **Student Loop 學習閉環**。

---

## 📅 專案基本資訊
*   **專案名稱**：Antigravity v2 終極修煉手冊 (`antigravity_2.0_tutorial`)
*   **本地路徑**：`d:\Users\148015\Projects\antigravity_2.0_tutorial`
*   **GitHub 帳號**：`pandaorz`
*   **遠端倉庫**：[antigravity_2.0_tutorial](https://github.com/pandaorz/antigravity_2.0_tutorial)
*   **更新時間**：2026-05-22 (台北時間)

---

## 🛠 關鍵技術決策與架構規範

### 1. 繁體中文與輸出規範
*   **決策**：全程使用 **台灣繁體中文 (zh-TW)**，包含程式碼註解、說明文件與對話。技術專有名詞保留原文。
*   **格式**：Markdown 檔案使用 ATX 標題，檔案編碼統一採用 `UTF-8`。

### 2. GitHub 閱讀體驗優化 (相對路徑政策)
*   **背景**：在 v2 中由於沒有網頁版 IDE，使用者使用本地編輯器。為確保手冊在 GitHub 網頁端線上閱讀時可以流暢跳轉，採用了**相對路徑**決策。
*   **規範**：所有教學文件（如 [README.md](../README.md)）內部的檔案跳轉與程式碼範例連結，一律使用相對路徑（例如：`[index.html](examples/web_app/index.html)`），嚴禁使用 Windows 本地絕對路徑，確保 GitHub 線上點擊 100% 成功。

### 3. 環境與資安稽核最佳實踐 (SecOps)
*   **環境**：Windows 11 / PowerShell (pwsh) 5.1+。Pre-flight 檢查確認本專案無需特規 Python 虛擬環境隔離。
*   **資安規範**：
    *   所有程式碼嚴格符合 **Secure Coding** 規範（OWASP Top 10 與 CWE TOP 25）。
    *   在 JavaScript 中以 `textContent` 替代 `innerHTML` 防範 XSS 注入。
    *   SQL 查詢範例均使用參數化查詢（Prepared Statements）以防範 SQL 注入（CWE-89）。
    *   機密資訊（如 API Keys）在 `.gitignore` 中過濾，絕不暴露於代碼中。

### 4. 免密碼安全自動化部署 (GitHub CLI)
*   **踩坑與實踐**：基於資安考量，AI 不應要求使用者提供帳密。透過偵測本地已配置並登入的 GitHub CLI (`gh` 工具)，以高安全性憑證（Token scopes: `repo`）自動完成遠端 Repository 建立與 Push，實現 100% 免密碼安全自動化。

### 5. Antigravity 2.0 工具家族 50 大情境與解耦協作基因
*   **決策**：明確記錄 Antigravity 2.0 在 Google I/O 2026 的解耦革命（解耦為 Desktop App, IDE, CLI, SDK），並為每個工具及跨工具協作撰寫了共計 50 個無佔位符的實戰情境。
*   **規範**：
    *   **Antigravity v2 (Agent Manager)**：作為 Mission Control (控制中樞) 監控多代理任務、集中管理 MCP、排程背景守護任務與實行安全沙盒權限控制，已無內建編輯介面。
    *   **Antigravity IDE v2**：直系繼承者，提供本地編輯器（VS Code 等）之 AI 滴入式增量修改與行內 Diff。
    *   **Antigravity CLI**：用於 Git pre-commit 自動化安全掃描、CI/CD 無 UI 測試等高速背景命令列工具。
    *   **Antigravity SDK**：提供 Python 程式化介面，用以客製化開發多代理共識與自動化資料清洗 Pipeline。

---

## 📂 階段性成果與檔案清單
1.  **[README.md](../README.md)**：終極手冊入口，包含 9 大實戰場景引導與 Antigravity 2.0 導覽。
2.  **[docs/tool_family.md](../docs/tool_family.md)**：Antigravity 2.0 工具家族（Agent Manager、IDE v2、CLI、SDK）特色剖析與 50 大實戰情境終極寶典（HTML 折疊高可讀性排版）。
3.  **[docs/agent_operations.md](../docs/agent_operations.md)**：Agent 進階控制指南（子代理、長工排程、Slash 指令）。
4.  **[examples/](../examples/)**：包含極致美學網頁、跨平台腳本、學霸筆記、EML 生成、SecOps 審查、PubMed 檢索、Pandas 數據分析、Database 優化、Playwright 測試等九大實體完整代碼。

---

## 🔮 後續迭代方向
*   [ ] 當新增第十個實戰場景時，需同步更新 README.md、tool_family.md 與此記憶庫。
*   [ ] 若未來引入 Poetry 或 Pipenv 等虛擬環境，需於 Pre-flight check 部分記錄虛擬環境啟動指令。
