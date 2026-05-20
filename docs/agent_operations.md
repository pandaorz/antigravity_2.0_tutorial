# 🤖 Antigravity v2 Agent 進階操作與 Subagents 協作指南

本指南將帶您深入了解 Antigravity v2 最強大的**控制中樞**。您將學會如何靈活運用「斜線指令 (Slash Commands)」、如何「定義並調度子 Agent (Subagents)」進行非同步多兵種協作，以及了解「響應式喚醒 (Reactive Wakeup)」的底層運作邏輯。

---

## 📂 目錄
1. [⚡ 斜線指令 (Slash Commands) 實戰](#-斜線指令-slash-commands-實戰)
2. [👥 多子代理協作 (Subagents Multi-Agent System)](#-多子代理協作-subagents-multi-agent-system)
3. [🔔 響應式喚醒 (Reactive Wakeup) 運作原理](#-響應式喚醒-reactive-wakeup-運作原理)
4. [💡 經典 Agent 協作場景實戰演練](#-經典-agent-協作場景實戰演練)

---

## ⚡ 斜線指令 (Slash Commands) 實戰

斜線指令是使用者在 Chat UI 介面中快速觸發 Agent 特殊模式或自動化工作流的「快捷鍵」。以下是 v2 四大核心指令的詳細操作步驟與適用情境：

### 1. `/goal` — 進入「超長航程/通宵執行」模式
*   **適用情境**：當您有一個非常龐大、耗時且需要極高準確度的任務時（例如：重構整個專案的安全性、進行大規模跨檔案的升級、或是撰寫長篇技術手冊）。
*   **功能說明**：觸發後，Agent 會被給予「超高容錯率與自主執行權」。Agent 會極度徹底地規劃，並非同步在背景自主執行「Plan-Execute-Verify」循環，遇到小阻礙會自我修正（Self-Correction）並主動重試，直到達成您的最終目標，中途不會輕易停下向您提問。
*   **詳細操作步驟**：
    1.  在對話框中輸入 `/goal`。
    2.  緊接著輸入您的複雜目標，例如：
        > `/goal 幫我把 examples/ 目錄下所有的 Python 腳本進行靜態安全性稽核，修補所有潛在漏洞，並確保全部都能在 Windows 環境下成功執行，最後生成 walkthrough.md 報告。`
    3.  送出後，您可以直接關閉視窗或去做其他事。Agent 將在後台通宵工作，完成後會主動發送通知喚醒您。

### 2. `/schedule` — 定時與週期任務排程
*   **適用情境**：當您需要 Agent 定期幫您監控系統、拉取最新醫學文獻，或是定時備份資料庫時。
*   **功能說明**：利用 `schedule` 工具，您可以設定「單次計時器 (One-shot Timer)」或是「標準的 5 欄位 Cron 週期任務」。
*   **詳細操作步驟**：
    1.  輸入 `/schedule`。
    2.  設定 Cron 表達式與指令，例如：
        > `/schedule cron="0 */2 * * *" prompt="請執行 examples/bash_scripts/backup_tool.sh 進行資料庫定期備份，並檢查備份日誌是否正常。"`
    3.  Agent 就會在背景啟動定時器，每隔 2 小時自動執行一次，並將結果記錄在後台任務中。若執行失敗，會主動跳出通知您。

### 3. `/browser` — 啟用網頁瀏覽與自動化 Playwright 模式
*   **適用情境**：當您需要 Agent 前往某個沒有公開 API 的網站抓取資料、驗證您剛寫好的網頁前端 UI、或是檢查外部連結是否失效。
*   **功能說明**：引導 Agent 使用 Playwright 啟動 Chromium 瀏覽器，進行點擊、輸入、截圖與資料擷取。
*   **詳細操作步驟**：
    1.  輸入 `/browser` 並附帶目標與網址：
        > `/browser 前往 https://news.ycombinator.com 幫我抓取今天前 5 熱門的技術新聞，並整理成繁體中文摘要。`
    2.  Agent 會自動調用瀏覽器，並將點擊過程與擷取到的文字/截圖即時回傳給您。

### 4. `/grill-me` — 設計審查與互動式面試
*   **適用情境**：在開始一個大專案的實作計畫之前，如果您對設計決策、技術選型或系統架構感到猶豫。
*   **功能說明**：Agent 會轉換為「嚴厲的架構審查官」，主動提出 3 到 5 個關鍵性、痛點式的問題（例如邊界條件、效能瓶頸、資安考量），透過一問一答引導您激發出最完美的設計方案。
*   **詳細操作步驟**：
    1.  輸入 `/grill-me` 並簡述您的想法：
        > `/grill-me 我打算用 Node.js 寫一個即時聊天室，資料庫用 Redis 加 MongoDB，請對我進行架構審查。`
    2.  UI 會跳出互動式問答 Modal，Agent 會一步步針對併發控制、資料一致性對您進行提問，最終引導您定案最穩健的實作計畫。

---

## 👥 多子代理協作 (Subagents Multi-Agent System)

當單一 Agent 遇到過於龐大或跨領域的任務時，v2 允許主 Agent 扮演「PM (專案經理)」，在背景定義並指派任務給多個**特化型子 Agent (Subagents)**。

### 🛠 子代理四大操作工具

1.  **`define_subagent` (定義子代理)**：
    *   **用途**：定義一個具備特殊 System Prompt、特殊 Skills 與工具權限的全新 Agent。
    *   **例子**：定義一個專精 OWASP 的 `SecOps_Auditor`，或是一個專精 SEO 的 `SEO_Expert`。
2.  **`invoke_subagent` (喚醒並指派任務)**：
    *   **用途**：啟動已定義 of 子代理，並分派具體任務（可選擇隔離的 `branch` 空間或共享的 `share` 空間）。
3.  **`send_message` (發送訊息)**：
    *   **用途**：在任務執行過程中，主 Agent 與子 Agent 之間進行溝通、交換資料或下達新指令。
4.  **`manage_subagents` (管理子代理)**：
    *   **用途**：列出所有活動中的子代理 (`list`)，或是在必要時終止它們 (`kill`)。

---

## 🔔 響應式喚醒 (Reactive Wakeup) 運作原理

這是 Antigravity v2 最具革命性的背景執行機制。

> [!TIP]
> **「我不需要在聊天視窗前傻傻等待 Agent 跑完長任務！」**
> 
> 在傳統的 AI 助理中，當您執行一個編譯、部署或大範圍重構的長任務時，您必須開著網頁，看著 AI 一行行吐字，一旦斷網或關閉網頁任務可能就中斷了。
> 
> **Antigravity v2 的 Reactive Wakeup 原理**：
> 1.  當主 Agent 調用了長任務（例如背景命令 `run_command`、啟動了子代理 `invoke_subagent`、或是設定了定時器 `schedule`）之後，**主 Agent 可以主動宣布進入「空閒 (Idle) 狀態」**。
> 2.  此時，Agent **完全停止消耗您的 Token 與運算資源**。
> 3.  **當以下事件發生時，系統會自動「喚醒 (Wakeup)」Agent**：
>     *   背景執行命令完成或出錯。
>     *   某個子代理 (Subagent) 完成了它的任務並發送回執。
>     *   定時器 (Timer/Cron) 時間到期。
>     *   使用者發送了新的訊息。
> 4.  被喚醒的 Agent 會自動載入先前的上下文與背景任務的輸出日誌，精確地接著上一步繼續工作，並通知使用者！

---

## 💡 經典 Agent 協作場景實戰演練

### 📖 真實案例：開發一個高安全性的 API 系統
在這個案例中，我們將演練**主 Agent** 如何定義一個**資安稽核子 Agent**，並指派它審查程式碼。

#### 1. 步驟一：使用者下達指令
> 「請幫我寫一個 Python Flask 的登入 API 系統，並找一個專門的資安 Agent 幫我們審查程式碼安全性。」

#### 2. 步驟二：主 Agent 定義並調度資安子 Agent
主 Agent 在後台會調用 `define_subagent` 工具：
*   **Name**: `SecOpsAuditor`
*   **System Prompt**: `「你是一位專精 OWASP Top 10 的靜態代碼分析專家，你的任務是找出程式碼中的漏洞並提供 Prepared Statement 等防禦性修補方案。」`

隨後調用 `invoke_subagent` 指派任務：
*   **Prompt**: `「請幫我審查剛寫好的 examples/secops/security_audit.py 檔案，找出裡面的 SQL Injection 弱點，並將修改建議以 JSON 格式發送給我。」`

#### 3. 步驟三：非同步背景運作與 Reactive Wakeup
主 Agent 呼叫完工具後便停止動作。子 Agent 在背景沙盒中獨立閱讀檔案並進行分析。當子 Agent 分析完意並呼叫 `send_message` 將結果回傳時，主 Agent 被**自動喚醒**，並將稽核結果與修補方案無縫呈現給使用者！

這就是 Antigravity v2 多 Agent 協作系統的優雅之處。

---

現在您已經完全掌握了 Agent 的操作精髓！請返回 **[README.md](../README.md)**，並開始動手執行 `examples/` 目錄下的九大實戰場景，體驗真實的代碼開發吧！
