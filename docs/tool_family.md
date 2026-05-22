# 🛡️ Antigravity 2.0 工具家族全景與 50 大實戰情境終極寶典

歡迎來到 **Antigravity 2.0** 官方認證的終極修煉寶典。本指南依據 Google I/O 2026 的最新官方手冊規格撰寫，旨在協助您徹底掌握 Antigravity 2.0 解耦後的全新工具鏈生態，並提供 **50 個 100% 無佔位符的實戰情境、步驟與實體代碼**。

---

## 📂 目錄
1. [⚔️ 生態系革命：從 v1 一體化到 v2 專業解耦](#-生態系革命從-v1-一體化到-v2-專業解耦)
2. [🖥️ Antigravity v2 (桌面端) 超越 Agent Manager 的四大核心功能](#-antigravity-v2-桌面端-超越-agent-manager-的四大核心功能)
3. [🎯 判斷不同工具的使用時機與決策樹](#-判斷不同工具的使用時機與決策樹)
4. [📚 Antigravity 50 大實戰情境終極指南](#-antigravity-50-大實戰情境終極指南)
   - [A. Antigravity v2 (Agent Manager) — 10 大實戰情境](#a-antigravity-v2-agent-manager--10-大實戰情境)
   - [B. Antigravity IDE v2 — 10 大實戰情境](#b-antigravity-ide-v2--10-大實戰情境)
   - [C. Antigravity CLI (Go-based) — 10 大實戰情境](#c-antigravity-cli-go-based--10-大實戰情境)
   - [D. Antigravity SDK (Python-based) — 10 大實戰情境](#d-antigravity-sdk-python-based--10-大實戰情境)
   - [E. 四大工具跨界協作 (Symphony Workflow) — 10 大實戰情境](#e-四大工具跨界協作-symphony-workflow--10-大實戰情境)
5. [🔗 返回主手冊](README.md)

---

## ⚔️ 生態系革命：從 v1 一體化到 v2 專業解耦

依據官方說明，Antigravity 2.0 帶來了全新的架構革命，請務必釐清以下核心演進關係：

```mermaid
graph TD
    subgraph Antigravity v1 (舊版一體化)
        V1_Agent[Agent] <--> V1_IDE[網頁內建 IDE]
    end

    subgraph Antigravity 2.0 生態系 (專業解耦)
        V2_IDE[Antigravity IDE v2<br/>本地編輯器擴充/專屬環境] <-->|代碼編修與行內提示| V2_AM[Antigravity v2 Desktop<br/>Agent Manager]
        V2_CLI[Antigravity CLI<br/>Go 高效能終端工具] <-->|CLI 觸發與 Git 鉤子| V2_AM
        V2_SDK[Antigravity SDK<br/>Python 程式化介面] <-->|客製化 Agent 整合| V2_AM
    end

    V1_IDE -->|直系演進| V2_IDE
    V1_Agent -->|核心 Runtime 升級| V2_AM
```

> [!IMPORTANT]
> **官方三大核心定義：**
> 1. **直系演進**：**Antigravity v1** 的代碼編輯與可視化模組，直系演進並重命名為 **Antigravity IDE v2**（完美整合本地 VS Code / JetBrains 等編輯器）。
> 2. **核心並存**：**Antigravity v1** 包含 Agent 與 IDE，而解耦後的 **Antigravity v2** 家族（生態系）同樣也是包含 Agent 與 IDE。
> 3. **桌面端無 IDE 定位**：獨立桌面端的 **Antigravity v2** 變更為 **Agent Manager (代理管理器)**。在該桌面軟體中**已經沒有內建的 IDE 編輯介面**，它專注於扮演「控制中樞 (Mission Control)」，將代碼編輯的重任完全交由直系繼承者 **Antigravity IDE v2** 承擔。

---

## 🖥️ Antigravity v2 (桌面端) 超越 Agent Manager 的四大核心功能

**Antigravity v2 桌面應用程式** 不僅僅是 Agent Manager，它更扮演著整個開發流程的 **「Mission Control (任務控制中心)」**，擁有以下四大核心功能：

1. **MCP (Model Context Protocol) 集中管理器**
   * **功能說明**：GUI 介面提供對 MCP 伺服器的集中配置、熱插拔與連線監控。可將本地 PostgreSQL、SQLite、或是外部醫學、財務 API 直接掛載，作為所有 Agent 共享的擴充 tools。
2. **視覺化專案 Mission Control**
   * **功能說明**：即時渲染 Agent 的「Plan-Execute-Verify」規劃思維拓撲圖，並能以 Git-style 渲染 Agent 對本地檔案做滴入式修改前後的 Diff 對比，自動生成優雅的 `walkthrough.md` 變更報告。
3. **Daemon 背景守護排程中心**
   * **功能說明**：集中管理並監控所有定時或週期性 (/schedule) 背景守護任務。提供健康檢查、失敗重試、以及資源佔用監控，在出錯時會主動彈出通知。
4. **安全沙盒與權限閘道 (Security Gatekeeper)**
   * **功能說明**：這是專案的資安第一道防線。當 Agent 嘗試執行敏感的終端機指令（如 `rm -rf`）、寫入特定系統檔案（如 `.env`）或發起網絡請求時，桌面端會彈出確認視窗，供開發者一鍵授權或阻斷。

---

## 🎯 判斷不同工具的使用時機與決策樹

為避免工具混淆，請參考以下**判斷決策樹**來選擇最適合的工具：

*   **如果您需要寫程式、局部重構、修復 bug、或進行前端 CSS 熱修復**：
    👉 選擇 **Antigravity IDE v2**（第一線檔案編修最佳利器）。
*   **如果您需要通宵執行大任務、管理多代理人團隊、設定定時背景備份、或掛載 MCP 數據庫**：
    👉 選擇 **Antigravity v2 (Agent Manager)**（全域管理與 Mission Control 中樞）。
*   **如果您需要在終端機操作、寫自動化 Shell 腳本、或在 CI/CD pipeline 中自動化掃描代碼**：
    👉 選擇 **Antigravity CLI**（極速響應、命令列自動化王牌）。
*   **如果您需要客製化 AI 工具、批量調用 Agent 處理 CSV、或在 Python 產品中嵌入 AI 能力**：
    👉 選擇 **Antigravity SDK**（程式化訪問與客製化擴充核心）。

---

## 📚 Antigravity 50 大實戰情境終極指南

以下我們以 **極致學霸風格**，為 4 大工具與跨界協作各鋪開 **10 個（共計 50 個）**常見情境。
*為維持版面 sleek 與高可讀性，我們使用 HTML `<details>` 標籤將詳細步驟與實體代碼收納，點擊即可展開閱讀！*

---

### A. Antigravity v2 (Agent Manager) — 10 大實戰情境

<details>
<summary>1. 多專案平行背景長航任務監控 (/goal 任務觀測)</summary>

* **情境說明**：開發者需要同時對三個大型專案執行大範圍的模組重構，需要自主非同步執行，且需要即時監控。
* **判斷原因**：多專案、非同步、視覺化監控為 Agent Manager 的 Mission Control 核心範疇。
* **詳細步驟**：
  1. 打開 Antigravity v2 桌面端，在左側專案列表點擊 `Add Project`。
  2. 同時導入 `project_A`、`project_B` 與 `project_C`。
  3. 在對話框輸入 `/goal 執行全專案重構`，桌面端會自動為各專案 Spawning 獨立的背景 Agent。
  4. 點擊 `Topology View`，視覺化監控三個 Agent 的 Plan 思維鏈進度。
* **實體指令**：
  ```powershell
  /goal 請對 examples/web_app 與 examples/secops 執行全方位的 SecOps 安全性稽核，並生成綜合性的 walkthrough.md 報告，過程中如遇報錯請在背景自我修正，通宵執行。
  ```
</details>

<details>
<summary>2. MCP 伺服器集中掛載與工具共享</summary>

* **情境說明**：需要讓多個 Agent 具備直接讀寫本地 PostgreSQL 資料庫並拉取 Schema 的能力。
* **判斷原因**：MCP 伺服器的集中配置與授權，必須由 Desktop 端做為 Security Gatekeeper 來管理。
* **詳細步驟**：
  1. 在桌面端點擊 `Settings` -> `MCP Servers` -> `Add Server`。
  2. 設定類型為 `command`，配置啟動指令。
  3. 桌面端會成功連線並顯示 `Active` 綠燈，此時所有對話中的 Agent 將自動擁有該資料庫的讀寫 tools。
* **實體指令**：
  ```json
  // 桌面端 MCP 配置文件範例 (mcp_config.json)
  {
    "mcpServers": {
      "postgres-mcp": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-postgres", "--connection-string", "postgresql://localhost/sales_db"]
      }
    }
  }
  ```
</details>

<details>
<summary>3. 跨 Agent 併發通訊與死鎖偵測</summary>

* **情境說明**：一個對話中同時啟動了 3 個子 Agent（負責前端、後端、DB），它們在互相傳遞訊息時發生循環等待。
* **判斷原因**：跨 Agent 的通訊監控與死鎖調控為 Agent Manager 的核心職責。
* **詳細步驟**：
  1. 在桌面端開啟 `Communication Matrix`。
  2. 觀察三個 Agent 的 `send_message` 流向圖。
  3. 桌面端偵測到死鎖後會亮起紅燈，提示 `Circular Waiting Detected`。
  4. 點擊 `Force Resolve`，Agent Manager 會自動介入，指派主 Agent 進行優先權調度。
* **實體指令**：
  ```powershell
  # 於 Agent Manager 終端欄發送強制介入指令
  antigravity control --session="session_active" --action="resolve-deadlock" --priority="db_agent"
  ```
</details>

<details>
<summary>4. 全域背景 Cron 定時監控任務健康度觀測</summary>

* **情境說明**：設定了每 6 小時檢查一次資料庫備份狀態的排程任務，需要確認它在背景正常運行。
* **判斷原因**：Daemon 背景排程的健康監控為 Desktop 端的強項。
* **詳細步驟**：
  1. 在桌面端點擊 `Daemon Center` 選項卡。
  2. 可以看到名為 `db-backup-check` 的 Cron 任務正以 `Active` 狀態運行。
  3. 檢視其歷史執行的日誌與成功率折線圖，若出錯，系統會自動在 Windows 右下角發出紅牌警告。
* **實體指令**：
  ```powershell
  # 桌面端排程任務健康度查詢指令
  antigravity scheduler --list-jobs --detailed
  ```
</details>

<details>
<summary>5. Agent 執行權限安全實體閘道審查</summary>

* **情境說明**：Agent 在重構過程中，試圖執行破壞性的 `git push --force` 或修改敏感的 `.env` 檔案。
* **判斷原因**：權限閘道安全審查 (CWE-250) 必須由 Desktop 端彈出確認以防止惡意行為。
* **詳細步驟**：
  1. Agent 在背景執行到強制 Push 步驟。
  2. 桌面端立即凍結該 Agent 進程，並在螢幕中央彈出紅色閃爍的 `Permission Requested` 閘道。
  3. 顯示變更 Diff 與欲執行的指令。
  4. 開發者確認安全後，點擊 `Authorize`，Agent 繼續執行。
* **實體指令**：
  ```json
  // 權限閘道彈出之 JSON 請求
  {
    "agent": "SecOpsAgent",
    "permission": "command_execution",
    "target": "git push -f origin main",
    "risk_level": "CRITICAL"
  }
  ```
</details>

<details>
<summary>6. Agent 規劃路徑思維鏈 (Thought Chain) 視覺化調優</summary>

* **情境說明**：Agent 在解決一個複雜的 C++ 內存洩漏問題時，陷入了死循環思考。
* **判斷原因**：這需要透過 Agent Manager 的 Thought Chain 拓撲圖來中斷並手動調整方向。
* **詳細步驟**：
  1. 在桌面端點擊 `Thought Topology`。
  2. 檢視 Agent 規劃的思維節點（Node 1 -> Node 2 -> Node 3...）。
  3. 發現 Node 4 不斷在同一個錯誤方案上打轉。
  4. 滑鼠右鍵點擊 Node 4，選擇 `Prune Branch (剪枝)`，並手動在輸入欄給予提示，引導 Agent 走另一條路徑。
* **實體指令**：
  ```powershell
  # 剪枝並注入新提示
  /prune --node="thought_node_04" --inject-prompt="請改為使用 std::unique_ptr 進行自動資源管理，避免手動 delete。"
  ```
</details>

<details>
<summary>7. 階段性變更 Walkthrough 與 Git Diff 集中審查</summary>

* **情境說明**：Agent 完成了 Vite 前端卡片儀表板的重構，生成了十幾個檔案的變更，需要一次性打包審查。
* **判斷原因**：集中式的 Diff 對比與變更驗證是 Mission Control 的核心視覺化能力。
* **詳細步驟**：
  1. 在桌面端點擊 `Walkthrough Center`。
  2. 系統會自動加載自動生成的 `walkthrough.md` 報告。
  3. 介面右側會以 side-by-side (左右對比) 渲染出所有被修改檔案的 Diff，綠色為新增、紅色為刪除。
  4. 確認無誤後，點擊 `Deploy to Staging`。
* **實體指令**：
  ```powershell
  # 集中審查變更指令
  antigravity review --diff-all --session="dashboard-patch"
  ```
</details>

<details>
<summary>8. 本地沙盒資源佔用與效能限制設定</summary>

* **情境說明**：背景運行的多個 Agent 佔用了過多的 CPU 與記憶體，導致本地主機開發卡頓。
* **判斷原因**：本地資源限制與沙盒配額必須在 Agent Manager 桌面端集中配置。
* **詳細步驟**：
  1. 開啟桌面端 `Settings` -> `Resource Quota`。
  2. 將 CPU Limit 限制在 `40%`，RAM Limit 限制在 `4GB`。
  3. 將 Agent 執行的線程優先權設為 `Below Normal (低於一般)`。
  4. 點擊 `Apply`，桌面端將自動對背景 Node.js 與 Python 子進程套用配額。
* **實體指令**：
  ```json
  // 資源限額配置文件範例 (resource_limit.json)
  {
    "sandbox": {
      "cpu_limit_pct": 40,
      "ram_limit_mb": 4096,
      "process_priority": "BELOW_NORMAL"
    }
  }
  ```
</details>

<details>
<summary>9. 多代理人團隊 (Multi-Agent Team) 架構與職責拖放配置</summary>

* **情境說明**：需要建立一個「Scrum Team」多代理團隊，讓一個 Agent 負責寫測試、一個寫代碼、一個做資安稽核。
* **判斷原因**：多代理人團隊架構的建立與職責拖放是 Agent Manager 的視覺化協作亮點。
* **詳細步驟**：
  1. 打開桌面端 `Team Builder` 介面。
  2. 拖曳一個 `DeveloperAgent`、一個 `QAAgent` 與一個 `SecOpsAgent` 到畫面上。
  3. 用箭頭連線設定它們的通訊流：`Developer` -> `QA` (測試驗證) -> `SecOps` (漏洞掃描) -> `Developer` (修補)。
  4. 點擊 `Launch Team`，啟動協作。
* **實體指令**：
  ```powershell
  # 啟動多代理人團隊命令
  antigravity team --start --config="team_scrum_config.json"
  ```
</details>

<details>
<summary>10. 全局長期記憶庫 (Memory Engine) 集中提煉與編輯</summary>

* **情境說明**：專案經過三個月的開發，長期記憶庫累積了大量瑣碎記憶，需要進行集中整理與垃圾記憶修剪。
* **判斷原因**：全域記憶庫的提煉與持久化是 Student Loop 中樞的職責。
* **詳細步驟**：
  1. 開啟桌面端 `Memory Engine Center`。
  2. 系統會以條目式列出當前儲存在 `MEMORY/README.md` 的所有決策與踩坑筆記。
  3. 刪除已經過時的「舊版 Vite 2 配置」記憶。
  4. 對「Pre-commit 安全修補邏輯」進行加星號置頂。
  5. 點擊 `Save & Commit Memory`，自動更新專案記憶檔案。
* **實體指令**：
  ```powershell
  # 記憶庫提煉指令
  antigravity memory --optimize --prune-unused
  ```
</details>

---

### B. Antigravity IDE v2 — 10 大實戰情境

<details>
<summary>1. 程式碼熱重載增量編輯與 Diff 審查</summary>

* **情境說明**：開發者在 VS Code 中修改前端 UI 的 HSL 色調，需要即時預覽並與 Agent 協同編輯。
* **判斷原因**：檔案熱重載與行內 Git-style Diff 為典型的編輯端（IDE）開發情境。
* **詳細步驟**：
  1. 開啟 VS Code 並加載專案，啟動 `Antigravity IDE v2` 插件。
  2. 打開 [index.css](examples/web_app/index.css)。
  3. 在側邊欄點擊 `Antigravity Assist`，輸入修色要求。
  4. IDE 會在編輯器內直接以綠色（新增）與紅色（刪除）高亮顯示代碼 Diff。
  5. 按下快捷鍵 `Alt + A` 接受修改，本地熱重載伺服器即時渲染新 UI。
* **實體代碼**：
  ```css
  /* IDE 增量變更對比 */
  :root {
  -   --primary-color: hsl(220, 90%, 56%); /* 舊色調 */
  +   --primary-color: hsl(260, 85%, 60%); /* 新漸層 HSL */
  }
  ```
</details>

<details>
<summary>2. 函數級重構與防呆 Try-Catch 滴入式修改</summary>

* **情境說明**：需要將一個原本沒有防呆機制的 Flask 路由函數修改為具備嚴密 Try-Catch 與錯誤日誌記錄的版本。
* **判斷原因**：單一函數級的局部重構最適合使用 IDE 的滴入式修改工具。
* **詳細步驟**：
  1. 在編輯器中打開 Flask 控制器檔案。
  2. 滑鼠反白選取目標函數 `unsafe_login`。
  3. 滑鼠右鍵點擊，選擇 `Antigravity: Refactor with Try-Catch`。
  4. IDE 調用 `replace_file_content`，精確取代該區塊，絕不破壞檔案內其他代碼與排版。
* **實體代碼**：
  ```python
  # IDE 局部滴入式修改結果
  try:
      return db.execute(query, (username, password))
  except DatabaseError as e:
      app.logger.error(f"Database operation failed: {str(e)}")
      return jsonify({"error": "Internal Server Error"}), 500
  ```
</details>

<details>
<summary>3. 行內代碼自動補全與 Context-aware 側邊欄對話</summary>

* **情境說明**：在編寫數據分析腳本時，忘記了 Pandas 的分組聚合語法，需要快速獲取 Context-aware 的行內自動補全。
* **判斷原因**：這是日常編碼中，IDE Extension 最核心的實時補全與側邊對話場景。
* **詳細步驟**：
  1. 打開 [data_analyzer.py](examples/data_science/data_analyzer.py)。
  2. 在 line 45 輸入 `df.groupby(`。
  3. IDE 自動彈出灰色的補全提示 `['product_line']).agg({'sales': 'sum', 'margin': 'mean'})`。
  4. 按下 `Tab` 鍵接受補全。若有疑問，在側邊欄輸入 `「解釋這個聚合函數的運作邏輯」`。
* **實體代碼**：
  ```python
  # 行內自動補全代碼
  summary_df = df.groupby(['product_line']).agg({'sales': 'sum', 'margin': 'mean'}).reset_index()
  ```
</details>

<details>
<summary>4. 多檔案架構依賴關係可視化與重構</summary>

* **情境說明**：專案從 3 個檔案擴增為 17 個檔案，需要梳理其 Import 依賴關係以進行結構解耦。
* **判斷原因**：這需要 IDE 端的 AST（抽象語法樹）靜態分析與多檔案可視化架構重構。
* **詳細步驟**：
  1. 在 VS Code 中按下 `Ctrl + Shift + P`，輸入 `Antigravity: Show Dependencies`。
  2. 編輯器主視窗會彈出一個互動式的依賴拓撲網狀圖。
  3. 發現 `generate_eml_task.py` 與 `data_analyzer.py` 存在循環依賴。
  4. 拖曳依賴線，Agent 會自動生成重構計畫，將共用邏輯提取至新建的 `utils/helpers.py`。
* **實體指令**：
  ```powershell
  # 於 IDE 終端面板執行重構驗證
  antigravity-ide refactor --dependency-prune --target="utils/helpers.py"
  ```
</details>

<details>
<summary>5. 前端 CSS/JS 熱修復與 HSL 色調美化</summary>

* **情境說明**：網頁前端的按鈕 hover 效果太過生硬，需要將其修改為 sleek 漸變與 subtle 微動畫。
* **判斷原因**：前端 CSS/JS 微調與即時渲染完全屬於 IDE 編輯端的專長。
* **詳細步驟**：
  1. 打開 [index.css](examples/web_app/index.css)。
  2. 選取 `.card:hover` 樣式。
  3. 在行內對話框輸入：`「將 hover 改為 0.3 秒 smooth transition，並加入 subtle glassmorphism 反光微動畫」`。
  4. IDE 滴入式修改代碼，本地瀏覽器即時渲染出高質感的懸停效果。
* **實體代碼**：
  ```css
  /* IDE 前端熱修復代碼 */
  .card:hover {
      transform: translateY(-5px);
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
      transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  }
  ```
</details>

<details>
<summary>6. 單元測試案例 (PyTest) 自動生成與行內錯誤即時修正</summary>

* **情境說明**：剛寫好了 PubMed 檢索器，需要在 IDE 中為其自動生成 PyTest 單元測試，並即時排除行內語法報錯。
* **判斷原因**：單元測試生成與行內 linting 錯誤修正為典型 IDE 功能。
* **詳細步驟**：
  1. 打開 `pubmed_researcher.py`。
  2. 點擊函數定義上方的 `Create Test Case` 快捷連結。
  3. IDE 自動在 `tests/test_pubmed.py` 中生成測試案例。
  4. 執行測試時發現 line 12 報錯，IDE 自動在其下方標記紅線，點擊 `Quick Fix` 即可自動修復未定義變數。
* **實體代碼**：
  ```python
  # 自動生成之測試代碼
  def test_pubmed_fetch():
      results = fetch_pubmed_abstracts(query="CAR-T", max_results=2)
      assert len(results) > 0
      assert "abstract" in results[0]
  ```
</details>

<details>
<summary>7. 檔案級 XSS 與 SQL 注入 (CWE-89) 的 IDE 安全提醒與一鍵修補</summary>

* **情境說明**：在編寫 API 時，不小心寫入了一行拼接 SQL 的代碼，需要 IDE 能在存檔時亮起資安紅牌並一鍵修補。
* **判斷原因**：行內資安弱點警示與 Prepared Statement 一鍵修補是 IDE v2 的 Secure Coding 重點。
* **詳細步驟**：
  1. 在 `user_controller.py` 中寫入拼接 SQL 代碼並按下存檔。
  2. IDE 靜態安全分析器立即亮起紅色警示：`CWE-89 SQL Injection Risk`。
  3. 滑鼠懸停在錯誤代碼上，點擊 `Secure Fix: Parameterize Query`。
  4. 代碼自動被安全的 Prepared Statement 替代，紅牌消失。
* **實體代碼**：
  ```python
  # 一鍵修補對比
  # ❌ 舊代碼: cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
  # ✓ 新代碼: cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
  ```
</details>

<details>
<summary>8. 記憶庫 README.md 的相對路徑點擊測試</summary>

* **情境說明**：在 IDE 中編輯專案長期記憶 `MEMORY/README.md`，需要確認裡面的相對跳轉路徑是否 100% 正確。
* **判斷原因**：Markdown 的本地即時編輯、連結檢索與驗證屬於 IDE 的工作範疇。
* **詳細步驟**：
  1. 打開 `MEMORY/README.md`。
  2. 編輯一條新的技術決策，並加入指向 `examples/secops/security_audit.py` 的連結。
  3. 按住 `Ctrl` 鍵並點擊該相對連結。
  4. 若連結正確，IDE 會自動開啟該 py 檔案；若失效，IDE 會彈出 `Path Not Found` 並主動提示正確的相對路徑。
* **實體代碼**：
  ```markdown
  <!-- 正確的相對連結 -->
  * 專案資安稽核實務決策，請參閱：[security_audit.py](../examples/secops/security_audit.py)
  ```
</details>

<details>
<summary>9. 利用 IDE 特有的可視化 Trace 視窗進行多代理循環呼叫除錯</summary>

* **情境說明**：在執行複雜的多 Agent 協作時，Agent A 呼叫了 Agent B，Agent B 又呼叫了 Agent A，導致無限遞迴。
* **判斷原因**：循環呼叫的 Call Stack 視覺化追蹤是 IDE v2 特有的 Trace 功能。
* **詳細步驟**：
  1. 打開 VS Code 的 `Antigravity Trace` 視窗。
  2. 啟動對話的偵錯模式 (Debug Mode)。
  3. 當循環呼叫發生時，Trace 視窗會以紅色高亮標記出重複的 Call Loop。
  4. 點擊 `Break Loop`，IDE 會自動插入中斷斷點並生成 stack trace 報告。
* **實體指令**：
  ```powershell
  # 於 IDE 偵錯控制台啟動 Trace
  antigravity-ide debug --trace-agents --loop-detect
  ```
</details>

<details>
<summary>10. Markdown 筆記的本地即時預覽與排版修復</summary>

* **情境說明**：在編寫包含複雜 Mermaid 流程圖與 Carousel 輪播的學霸筆記時，需要實時雙面板預覽渲染結果。
* **判斷原因**：Markdown 雙面板渲染與實時排政完全是 IDE 編輯端的強項。
* **詳細步驟**：
  1. 打開 [note_writing_guide.md](examples/note_writing/note_writing_guide.md)。
  2. 點擊編輯器右上角的 `Open Preview to the Side` 按鈕。
  3. 介面自動分為左右雙面板，左邊編輯原始碼，右邊實時渲染出 Mermaid 與 HSL 漸層 Alerts。
  4. 發現 Mermaid 語法錯誤時，預覽視窗會高亮提示錯誤行，協助快速修正。
* **實體代碼**：
  ```mermaid
  %% 實時預覽的 Mermaid 圖表
  graph TD
      A[Data Ingestion] --> B[Data Cleansing]
      B --> C[Visual Analytics]
  ```
</details>

---

### C. Antigravity CLI (Go-based) — 10 大實戰情境

<details>
<summary>1. 本地 Git pre-commit 鉤子的自動安全靜態掃描</summary>

* **情境說明**：在開發人員嘗試執行 `git commit` 時，自動在背景觸發資安掃描，防止漏洞被提交。
* **判斷原因**：無 UI 介面、與 Git 緊密整合的背景高速掃描是 CLI 的核心強項。
* **詳細步驟**：
  1. 將專案 Pre-commit 鉤子指向 CLI 安全命令。
  2. 開發人員執行 `git commit`。
  3. CLI 自動啟動 (耗時小於 30ms)，掃描暫存區檔案。
  4. 若無安全風險，返回代碼 0 允許 commit；若發現 CWE-89 漏洞，返回代碼 1 阻斷並輸出報告。
* **實體指令**：
  ```powershell
  # 於 .git/hooks/pre-commit 中配置：
  antigravity analyze --staged --rule="owasp-top10" --fail-on="CRITICAL"
  ```
</details>

<details>
<summary>2. 在 CI/CD Pipeline 中執行無 UI 介面的自動化測試與 Walkthrough 生成</summary>

* **情境說明**：在 GitHub Actions 流水線中，自動調用 Agent 對最新的變更執行單元測試，並自動生成 markdown 驗證報告。
* **判斷原因**：伺服器端、無 GUI 的 Pipeline 自動化任務屬於 CLI 的典型情境。
* **詳細步驟**：
  1. 在 CI/CD 伺服器上下載並配置 `antigravity` CLI 二進位檔。
  2. 配置系統環境變數以取得 API 權限。
  3. 流水線執行 CLI 命令啟動背景測試代理。
  4. 測試完成後，CLI 自動在專案目錄下寫入 `walkthrough.md`。
* **實體指令**：
  ```bash
  # GitHub Action workflow runner 中的命令：
  antigravity test --all --generate-report --output-dir="./artifacts"
  ```
</details>

<details>
<summary>3. 用一行指令進行專案級大範圍代碼 analyze 與自動修復</summary>

* **情境說明**：需要對整個專案下所有的 Python 與 Shell 腳本進行大規模的 linting 與語意錯誤自動修復。
* **判斷原因**：一鍵式、全專案大範圍的批次指令分析完全適合 CLI 快速執行。
* **詳細步驟**：
  1. 在 PowerShell 中切換到專案根目錄。
  2. 執行 CLI 全域分析指令，並附帶 `--fix` 參數。
  3. CLI 會高速讀取 AST，調度核心 Agent，在一分鐘內完成全專案 17 個檔案的分析與自動修復。
* **實體指令**：
  ```powershell
  antigravity analyze --dir="." --exclude="node_modules" --fix --backup-before-fix
  ```
</details>

<details>
<summary>4. 在 Linux 伺服器上以背景 Daemon 模式啟動特定 Skill 代理</summary>

* **情境說明**：需要在遠端 Linux 伺服器上啟動一個具備「系統資源稽核」技能的 Agent，讓它以守護進程模式長駐背景。
* **判斷原因**：Linux 遠端部署與 Daemon 模式是 CLI 無法被取代的功能。
* **詳細步驟**：
  1. 透過 SSH 登入 Linux 伺服器。
  2. 執行 CLI 命令啟動守護進程，指定稽核 Skill。
  3. CLI 會建立一個系統 service 或背景 nohup 進程，定時分析系統 load 並記錄日誌。
* **實體指令**：
  ```bash
  # Linux 伺服器背景 Daemon 啟動命令
  nohup antigravity agent start --skill="sys-auditor" --daemonize --log-file="/var/log/antigravity.log" &
  ```
</details>

<details>
<summary>5. 利用 CLI 快速拉取並解析 GitHub PR，自動生成 Review 報告</summary>

* **情境說明**：團隊成員提交了一個包含 500 行代碼的 Pull Request，需要在終端機中一鍵拉取並產生 AI Code Review 報告。
* **判斷原因**：終端機下的極速 API 串接與 PR Review 生成是 CLI 的典型應用。
* **詳細步驟**：
  1. 在 PowerShell 中執行 CLI 指令並輸入 PR 編號。
  2. CLI 調用 GitHub API 拉取 Diff 資料。
  3. 調度 Agent 進行審查，並在終端機中以精美的色彩和表格格式輸出安全與效能審查報告。
* **實體指令**：
  ```powershell
  antigravity gh-review --pr=42 --repo="pandaorz/antigravity_2.0_tutorial" --detailed
  ```
</details>

<details>
<summary>6. 終端機下的多子代理快速調度與訊息傳遞 (Message Bus 偵測)</summary>

* **情境說明**：在編寫 Shell 自動化腳本時，需要以 command 形式調度子 Agent 執行資料過濾，並將結果管道 (Pipe) 傳遞給下一個 Agent。
* **判斷原因**：這需要 CLI 的標準輸入/輸出 (stdin/stdout) 與 Linux 管道符 (Pipe) 的無縫對接。
* **詳細步驟**：
  1. 編寫一行 Pipeline 命令。
  2. 第一個 CLI Agent 讀取日誌輸出 JSON。
  3. 透過 `|` 傳遞給第二個 CLI Agent 進行敏感金鑰過濾。
  4. 最終結果重導向至安全檔案中。
* **實體指令**：
  ```bash
  antigravity run-agent --role="LogParser" --input="sys.log" | antigravity run-agent --role="SecFilter" > secure_sys.log
  ```
</details>

<details>
<summary>7. 一鍵式本地資料庫 Schema 自動遷移與備份稽核</summary>

* **情境說明**：需要一鍵執行 SQL 資料庫 Schema 的更新，並呼叫 Agent 對遷移後的資料完整性進行稽核。
* **判斷原因**：批次資料庫腳本執行與自動化稽核完全適合 CLI 一鍵搞定。
* **詳細步驟**：
  1. 切換至資料庫目錄。
  2. 執行 CLI 命令加載遷移 SQL 檔。
  3. CLI 在執行遷移後，自動啟動 SQL 驗證 Agent 連線資料庫，比對主外鍵約束與索引健康度，並於終端機輸出稽核表格。
* **實體指令**：
  ```powershell
  antigravity db-migrate --schema="examples/database/db_optimization.sql" --audit --db-url="sqlite:///sales.db"
  ```
</details>

<details>
<summary>8. CLI 快速切換與管理多個 Model Context Protocol (MCP) 端點</summary>

* **情境說明**：開發者在多個網路環境間切換，需要利用 CLI 快速變更 Agent 連線的 MCP 伺服器端點。
* **判斷原因**：終端機下的 MCP 連線狀態切換與管理是 CLI 的實用功能。
* **詳細步驟**：
  1. 輸入 CLI 指令檢視當前已連線的 MCP 列表。
  2. 發現 `dev-postgres` 處於斷線狀態。
  3. 執行 CLI 重新連線指令，變更端點為遠端 `staging-postgres` 伺服器。
* **實體指令**：
  ```powershell
  antigravity mcp reconnect --server="postgres-mcp" --endpoint="postgresql://staging-db.ncku.edu.tw/sales"
  ```
</details>

<details>
<summary>9. 終端機大文件 (如 Log) 的分塊 AI 提煉與異常行檢出</summary>

* **情境說明**：伺服器產生了 1GB 的日誌檔案，需要在終端機中快速過濾出包含 "Critical Exception" 的異常行，並請 Agent 生成 RCA 分析。
* **判斷原因**：大文件分塊處理與終端機下高速過濾輸出為 CLI 特長。
* **詳細步驟**：
  1. 執行 CLI 檔案分析指令，指定日誌路徑與搜尋關鍵字。
  2. CLI 自動在背景將大文件分塊讀入，以多線程進行 Regex 過濾。
  3. 擷取出異常段落後，調度 Agent 進行根因分析 (RCA)，並在終端機渲染輸出。
* **實體指令**：
  ```powershell
  antigravity analyze-log --path="C:\Logs\production.log" --pattern="CRITICAL" --chunks=10 --ai-explain
  ```
</details>

<details>
<summary>10. CLI 定時觸發本地資源監控並呼叫 Agent 生成 system report</summary>

* **情境說明**：需要一條指令快速抓取當前系統 CPU、RAM 佔用，並讓 Agent 生成高 CP 值的資源優化報告。
* **判斷原因**：本地資源即時擷取與 CLI AI 報告生成是一體化命令列強項。
* **詳細步驟**：
  1. 在 PowerShell 執行系統監控 CLI 指令。
  2. CLI 自動調用 Windows WMI API 取得系統即時資源報表。
  3. 將數據作為 Context 輸入給 Agent，Agent 自動在終端機以 Markdown 表格渲染優化方案。
* **實體指令**：
  ```powershell
  antigravity sys-report --monitor-sec=5 --role="SysAdmin" --output="md"
  ```
</details>

---

### D. Antigravity SDK (Python-based) — 10 大實戰情境

<details>
<summary>1. 用 Python AntigravityClient 開發客製化醫療文獻 PubMed 檢索與綜述系統</summary>

* **情境說明**：醫療研究人員需要用 Python 編寫自定義的醫學論文自動分析程式，批量檢索 PubMed 並自動生成綜述。
* **判斷原因**：以 Python 程式化訪問核心 Runtime、掛載專用科學 API，完全是 SDK 的範疇。
* **詳細步驟**：
  1. 在您的 Python 環境中安裝 `antigravity-sdk`。
  2. 導入 `AntigravityClient`。
  3. 寫入 Python 代碼調用 PubMed API 取得 CAR-T 文獻，並指派 Agent 進行摘要提煉。
* **實體程式碼**：
  ```python
  # pubmed_sdk_task.py
  from antigravity import AntigravityClient

  client = AntigravityClient()
  pubmed_agent = client.create_agent(role="MedicalResearcher")
  
  # 調用 PubMed 檢索並請 Agent 生成綜述
  review = pubmed_agent.run(
      task="請檢索最新的 5 篇 CAR-T 療法的論文摘要，並生成繁體中文綜述。",
      tools=["pubmed_fetch"]
  )
  with open("car_t_review.md", "w", encoding="utf-8") as f:
      f.write(review.summary)
  print("[✓] 醫療文獻綜述生成成功！")
  ```
</details>

<details>
<summary>2. 程式化串接企業內部 ERP/SQL Server，進行月度數據報表自動生成</summary>

* **情境說明**：財務部門需要定期以 Python 程式拉取本地 SQL 數據，進行分組運算，並讓 Agent 自動寫出高價值的月度分析報告。
* **判斷原因**：與企業內部系統代碼級串接、大數據批量 AI 報表生成是 SDK 的核心價值。
* **詳細步驟**：
  1. 撰寫 Python 腳本，使用 `pyodbc` 連線企業 ERP SQL Server。
  2. 使用 Pandas 將拉取到的數據整理成 DataFrame。
  3. 將整理好的數據轉為 Markdown Table，呼叫 SDK Agent 進行趨勢洞察分析，自動寫出報表。
* **實體程式碼**：
  ```python
  # erp_reporter.py
  import pandas as pd
  from antigravity import AntigravityClient

  # 模擬拉取 ERP 數據
  data = {"Month": ["Jan", "Feb", "Mar"], "Sales": [120000, 150000, 185000], "Margin_Pct": [22.5, 23.1, 24.8]}
  df = pd.DataFrame(data)

  client = AntigravityClient()
  finance_agent = client.create_agent(role="CFO_Advisor")
  report = finance_agent.run(
      task=f"請分析以下第一季財務數據，點出亮點與隱憂：\n{df.to_markdown()}"
  )
  print(report.summary)
  ```
</details>

<details>
<summary>3. 自定義專屬 Agent 技能 (Skills) 並發佈至本地插件庫</summary>

* **情境說明**：開發者需要為團隊客製化一個「醫院行政公文核對」的特殊 Skill，並將其打包封裝。
* **判斷原因**：自定義 Agent 技能的 Python 程式化打包與註冊，是 SDK 提供的底層擴充能力。
* **詳細步驟**：
  1. 繼承 SDK 的 `BaseSkill` 類別。
  2. 實作技能的核心邏輯（如公文格式的正則驗證與錯別字比對）。
  3. 調用 `client.register_skill` 將其註冊，此時全體 Agent 皆可調用此客製化 Skill。
* **實體程式碼**：
  ```python
  # register_hosp_skill.py
  from antigravity import AntigravityClient, BaseSkill

  class HospDocumentSkill(BaseSkill):
      def __init__(self):
          super().__init__(name="hosp-doc-checker", description="檢查醫院行政公文格式")
      
      def execute(self, content):
          # 檢查是否含有醫院專屬前綴字尾
          if "成大醫院" not in content:
              return "❌ 公文格式不符：缺漏『成大醫院』主體發文字樣。"
          return "✓ 格式稽核通過。"

  client = AntigravityClient()
  client.register_skill(HospDocumentSkill())
  print("[✓] 醫院行政公文檢查 Skill 已成功註冊！")
  ```
</details>

<details>
<summary>4. 在 Python 應用程式中嵌入 Agent Runtime，實現 AI 即時語意分析</summary>

* **情境說明**：在開發一個本地客服視窗系統時，需要在收到客戶訊息的第一時間，由嵌入式 Agent 進行即時情感與語意分析，將分類結果回傳。
* **判斷原因**：在第三方 Python App 中嵌入 AI 代理 Runtime 是 SDK 的強項。
* **詳細步驟**：
  1. 啟動您的客服 App。
  2. 當客戶發送訊息時，後端即時將文本傳入 SDK 的 Agent 執行執行個體。
  3. Agent 在 100ms 內返回情感指數（正面/負面）與主題標籤。
* **實體程式碼**：
  ```python
  # live_chat_analyzer.py
  from antigravity import AntigravityClient

  client = AntigravityClient()
  analyzer = client.create_agent(role="SentimentAnalyzer")

  def on_customer_message(msg):
      result = analyzer.run(
          task=f"請分析以下訊息的情感，僅回傳『正面』或『負面』，訊息：{msg}"
      )
      return result.summary.strip()

  print(on_customer_message("成大醫院的醫生態度非常好，非常感謝！")) # 輸出: 正面
  ```
</details>

<details>
<summary>5. 用 SDK 開發多 Agent 投票共識決策系統 (Consensus Protocol)</summary>

* **情境說明**：為了解決單一 AI 的幻覺問題，需要啟動三個不同的專家 Agent（資安、架構、效能），讓它們對一段程式碼進行聯合評估，最終以投票機制決定是否採用。
* **判斷原因**：複雜的多 Agent 共識演算法與通訊邏輯，只能透過 SDK 程式化開發來達成。
* **詳細步驟**：
  1. 使用 SDK 建立 3 個特化 Agent 執行個體。
  2. 同時將程式碼傳送給 3 個 Agent 進行評分與給予評語。
  3. 寫入 Python 邏輯比對三者的評分，若有兩位以上給予 "SAFE"，則系統判定通過。
* **實體程式碼**：
  ```python
  # consensus_system.py
  from antigravity import AntigravityClient

  client = AntigravityClient()
  agents = [
      client.create_agent(role="SecOpsAuditor"),
      client.create_agent(role="PerformanceEngineer"),
      client.create_agent(role="SystemArchitect")
  ]
  target_code = "def connect(): return sqlite3.connect('sales.db')"
  votes = []
  
  for agent in agents:
      res = agent.run(task=f"評估此代碼安全性與效能，僅回傳『PASS』或『FAIL』：\n{target_code}")
      votes.append(res.summary.strip())

  pass_count = votes.count("PASS")
  print(f"投票結果: {votes} -> {'通過部署' if pass_count >= 2 else '阻斷部署'}")
  ```
</details>

<details>
<summary>6. 程式化加載自定義 MCP 伺服器，將本地 PDF 文件轉為 Agent 知識庫</summary>

* **情境說明**：需要使用 Python 程式，在執行時動態加載一個本地 PDF 解析的 MCP 服務，作為 Agent 查閱醫療常規的知識庫。
* **判斷原因**：動態加載、在程式碼運行時掛載 MCP 端點完全屬於 SDK 的能力範圍。
* **詳細步驟**：
  1. 安裝 `@modelcontextprotocol/server-filesystem` MCP。
  2. 在 Python 中透過 SDK `client.mount_mcp` 動態加載。
  3. 指派 Agent 檢索該目錄下的醫療 PDF 常規文件。
* **實體程式碼**：
  ```python
  # pdf_mcp_loader.py
  from antigravity import AntigravityClient

  client = AntigravityClient()
  # 動態掛載本地文件夾 MCP
  client.mount_mcp(
      name="hosp-files",
      command="npx",
      args=["-y", "@modelcontextprotocol/server-filesystem", "D:/Users/148015/OneDrive/Hosp/PDFs"]
  )
  agent = client.create_agent(role="HospGuide")
  answer = agent.run(task="請查詢掛載目錄下的『急診處理指引.pdf』，說明過敏性休克的標準急救步驟。")
  print(answer.summary)
  ```
</details>

<details>
<summary>7. 透過程式碼動態捕捉並處理 Agent 規劃中的 Exception 與 Self-Correction</summary>

* **情境說明**：在執行背景長航任務時，Agent 的某個 file_io 工具發生權限異常報錯，需要在 Python 程式中動態捕捉，並提示 Agent 進行自我修正。
* **判斷原因**：Exception 的攔截與動態 Prompt 注入是 SDK 的進階控制機制。
* **詳細步驟**：
  1. 啟動 Agent 任務。
  2. 監聽執行狀態。
  3. 捕捉到 `PermissionError` 例外。
  4. SDK 自動在背景重新包裝 Prompt，提示 Agent 使用 `replace_file_content` 時的備用路徑，完成 self-correction。
* **實體程式碼**：
  ```python
  # self_correct_sdk.py
  from antigravity import AntigravityClient, AgentExecutionError

  client = AntigravityClient()
  agent = client.create_agent(role="AutomationEngineer")

  try:
      agent.run(task="修改 C:/Windows/System32/drivers/etc/hosts 檔案加入解析。")
  except AgentExecutionError as e:
      print(f"[捕捉到 Agent 異常] {str(e)}")
      print("[SDK 介入] 重新引導 Agent 使用專案內的相對路徑進行模擬修改...")
      corrected = agent.run(task="請改為修改專案目錄下的 examples/hosts.txt 檔案。")
      print(corrected.summary)
  ```
</details>

<details>
<summary>8. SDK 開發自動化 Playwright 瀏覽器測試，實現出錯時動態重試與修復</summary>

* **情境說明**：在執行網頁端對端測試時，由於網頁載入延遲，Playwright 找不到 Selector，需要 SDK Agent 能動態重新規劃等待機制並修復測試。
* **判斷原因**：動態捕捉 UI 測試失敗、自動修改並重試 Playwright 腳本需要 SDK 與 Agent 緊密整合。
* **詳細步驟**：
  1. 執行 Python 測試腳本。
  2. Playwright 找不到元素拋出 TimeoutError。
  3. SDK 捕捉到異常，呼叫 Agent 重新分析 `examples/web_app/index.html`。
  4. Agent 將 `click()` 改為先執行 `wait_for_selector()`，並重新執行，測試成功。
* **實體程式碼**：
  ```python
  # playwright_healer.py
  from antigravity import AntigravityClient
  
  client = AntigravityClient()
  qa_agent = client.create_agent(role="QAAgent")
  
  # 指派 Agent 對出錯的 Playwright 腳本進行自我修復與重試
  recovery_run = qa_agent.run(
      task="執行 examples/testing/playwright_test.py，若因元素未載入失敗，請修改該代碼加入 wait_for_selector，並重新執行驗證。",
      tools=["playwright", "file_io"]
  )
  print(recovery_run.summary)
  ```
</details>

<details>
<summary>9. 動態管理與序列化/反序列化 Agent 的短期記憶 state，實現對話暫停與重啟</summary>

* **情境說明**：背景 Agent 執行到一半，因為需要等待外部人工審查 (Human-in-the-loop)，需要將其當前的 Memory State 序列化存入 JSON 檔案，審查通過後再反序列化重啟。
* **判斷原因**：Agent State 級別的序列化管理是 SDK 特有的底層控制功能。
* **詳細步驟**：
  1. 啟動 Agent 執行。
  2. 在需要等待人工確認時，調用 `agent.serialize_state()`。
  3. 將 state JSON 寫入磁碟，暫停進程。
  4. 審查通過後，讀取 JSON，調用 `client.restore_agent(state_json)` 重啟，精確接續上一步思維。
* **實體程式碼**：
  ```python
  # agent_state_saver.py
  from antigravity import AntigravityClient

  client = AntigravityClient()
  agent = client.create_agent(role="DeploymentSpec")
  
  # 執行第一階段，然後序列化狀態
  agent.run(task="準備部署環境，確認 Docker 已安裝。")
  state_data = agent.serialize_state()
  
  with open("agent_state.json", "w") as f:
      f.write(state_data)
  print("[✓] Agent 短期記憶狀態已安全存檔！隨時可反序列化還原。")
  ```
</details>

<details>
<summary>10. 利用 SDK 開發自動化數據清洗與 Matplotlib 質感圖表繪製的 AI pipeline</summary>

* **情境說明**：需要使用 Python 批量清洗銷售 CSV，計算產品線的毛利率，並自動使用 Matplotlib 繪製極具美感色彩的和諧條形圖。
* **判斷原因**：以 Python SDK 原生結合 Pandas 與 Matplotlib 進行 AI 數據清洗與可視化。
* **詳細步驟**：
  1. 導入 `AntigravityClient` 與 `pandas`。
  2. 掛載本地 sales_data.csv。
  3. 指派 Agent 調用 `data_analyzer.py` 處理分組，並以和諧色調（如 HSL 配色）繪製 Matplotlib 圖表。
* **實體程式碼**：
  ```python
  # data_science_pipeline.py
  from antigravity import AntigravityClient

  client = AntigravityClient()
  data_agent = client.create_agent(role="DataScienceExpert")
  
  # 指派 Agent 讀取 sales_data.csv，分組計算並使用 HSL Harmonious palette 繪製毛利率圖
  pipeline_run = data_agent.run(
      task="請讀取 examples/data_science/sales_data.csv，使用 Pandas 計算各產品線總銷售，並用 Matplotlib 繪製 HSL 紫色調的精美條形圖，保存為 sales_performance.png。",
      tools=["pandas", "matplotlib", "file_io"]
  )
  print(pipeline_run.summary)
  ```
</details>

---

### E. 四大工具跨界協作 (Symphony Workflow) — 10 大實戰情境

<details>
<summary>1. 開發者 IDE 寫扣 -> Git Hook 觸發 CLI 掃描 -> CLI 調用 SDK 背景修補 -> Desktop 集中審查並一鍵 Accept</summary>

* **情境說明**：開發者在 VS Code 中新增了 API 檔案，嘗試提交時被 pre-commit 鉤子阻斷，CLI 調用 SDK 的 Agent 背景安全修補，並在 Desktop App 呈現 Diff 與 PR 供一鍵採納。
* **協作方式與步驟**：
  1. **IDE (VS Code)**：開發者在 `user_controller.py` 中寫入帶有拼接 SQL 的 API 代碼，並執行 `git commit`。
  2. **CLI**：Git 鉤子自動啟動 **Antigravity CLI** 執行暫存區代碼掃描，偵測到 CWE-89 SQL 注入風險。
  3. **SDK & Agent**：CLI 在終端機中回報風險，並直接在背景啟動以 **Antigravity SDK** 撰寫的 `scripts/trigger_sdk_patch.py`。該 Python 腳本會 Spawning 一個 **SecOpsAgent**，在背景沙盒中使用 `replace_file_content` 將漏洞修復為參數化查詢，並自動提交一個 `bugfix` 分支。
  4. **Desktop App (Agent Manager)**：Agent Manager 的「Walkthrough Center」亮起通知，為資深開發者呈現修補前後的 side-by-side 高亮 Diff。開發者點擊 `Accept Merge`，代碼自動更新在本地編輯器中。
* **實體代碼 (協作工作流腳本)**：
  ```powershell
  # 整合 Pre-commit 觸發與 CLI/SDK 調用命令 (.git/hooks/pre-commit)
  $scan = antigravity analyze --file="user_controller.py" --format=json
  if ($scan -like "*CWE-89*") {
      # 呼叫 SDK 執行背景 Agent 自動修補
      python scripts/trigger_sdk_patch.py --file="user_controller.py"
      # 中斷 commit，交由 Desktop App 審查一鍵 Merge
      exit 1
  }
  ```
</details>

<details>
<summary>2. Desktop App 排程 Cron 任務 -> 觸發 CLI 執行備份 -> 備份失敗調用 SDK 安全 Agent -> IDE 亮起警報並給出修補代碼</summary>

* **情境說明**：Desktop App 背景排程定時備份任務失敗。Desktop 自動調用 CLI，CLI 呼叫 SDK 的 Agent 進行診斷，發現是權限不足，隨後在開發者的 VS Code IDE 彈出修正建議。
* **協作方式與步驟**：
  1. **Desktop App (Mission Control)**：每隔 6 小時的 Cron 定時任務啟動，調用 **Antigravity CLI** 執行 `examples/bash_scripts/backup_tool.sh`。
  2. **CLI**：CLI 執行備份時，伺服器返回 `Permission Denied` 錯誤。備份失敗，CLI 回傳錯誤碼給桌面端。
  3. **SDK & Agent**：桌面端收到警報，啟動 **Antigravity SDK** 撰寫的異常診斷服務。專家 Agent 讀取備份日誌，發現備份目錄沒有寫入權限，規劃出修改目錄存取權限 (chmod/ACL) 的方案。
  4. **IDE (VS Code)**：Agent 的修復計畫自動傳送至開發者 VS Code 內部的 **Antigravity IDE v2**。編輯器行內跳出黃色警示，提示開發者一鍵執行 `chmod +w /var/backup` 修復權限。
* **實體指令**：
  ```powershell
  # 桌面端排程調用 CLI 指令
  antigravity scheduler --add-cron="0 */6 * * *" --command="antigravity backup --src='/data' --dest='/var/backup'"
  ```
</details>

<details>
<summary>3. SDK 批量抓取文獻 -> 生成 Walkthrough -> 同步到 Desktop 記憶庫 -> 開發者在 IDE 中點擊相對連結進行學術寫作</summary>

* **情境說明**：SDK 定期批量抓取 PubMed 癌症最新文獻，自動生成文獻 Review，同步寫入 Desktop 的專案長期記憶中，開發者隨後在本地 IDE (VS Code) 中點擊相對路徑，閱讀文獻並撰寫論文。
* **協作方式與步驟**：
  1. **SDK**：以 Python 程式化腳本調用 PubMed API 抓取論文摘要。
  2. **Agent**：調用 SDK 內的 **ScienceResearcher** Agent 對文獻進行情感與綜述提煉，自動生成無佔位符的文獻綜述 Markdown。
  3. **Desktop App**：綜述自動同步寫入桌面端管理的專案長期記憶庫 `MEMORY/literature_review.md`。
  4. **IDE (VS Code)**：開發者在 VS Code 中開啟主手冊 `README.md`，點擊指向 `MEMORY/` 的相對路徑連結。**Antigravity IDE v2** 無縫打開該文獻檔案，開發者便能一邊閱讀文獻，一邊在 IDE 中完成學術寫作。
* **實體代碼**：
  ```python
  # 動態寫入長期記憶並觸發 Desktop 同步
  with open("d:/Users/148015/Projects/antigravity_2.0_tutorial/MEMORY/literature_review.md", "w", encoding="utf-8") as f:
      f.write(review_markdown_content)
  ```
</details>

<details>
<summary>4. IDE 偵測到複雜架構問題 -> 一鍵傳送到 Desktop 調度 3 個子 Agent -> CLI 執行容器編譯 -> IDE 呈現重構結果</summary>

* **情境說明**：開發者在 IDE 發現專案模組過於耦合。他在 IDE 中一鍵發送重構請求給 Desktop 專案控制中心。Desktop Spawning 3 個子 Agent 在背景沙盒執行解耦；CLI 隨後執行 Docker 編譯測試，最終重構好的代碼呈現在 IDE。
* **協作方式與步驟**：
  1. **IDE**：開發者選取專案目錄，右鍵點擊選擇 `Send to Antigravity Mission Control`，提出「微服務解耦」請求。
  2. **Desktop App**：桌面端控制中心收到複雜任務，調用 `define_subagent` 定義並 Spawning 三個子代理：`ArchAgent` (規劃架構)、`RefactorAgent` (代碼重構)、`QAAgent` (驗證)。
  3. **CLI**：代碼重構完成後，桌面端調用 **Antigravity CLI**，在背景執行 `docker-compose build` 進行容器編譯與單元測試。
  4. **IDE**：測試完全 PASS 後，重構代碼以 Git-style Diff 高亮呈現在開發者的 VS Code 中，開發者按下 `Ctrl + Enter` 接受全部重構。
* **實體指令**：
  ```powershell
  # CLI 執行容器編譯驗證
  antigravity docker --build --compose-path="docker-compose.yml" --test-command="pytest"
  ```
</details>

<details>
<summary>5. CLI 偵測 PR 提交 -> SDK 呼叫 Playwright 測試 -> 測試失敗發送 logs 至 Desktop -> IDE 自動開啟錯誤行並引導 Agent 修補</summary>

* **情境說明**：Git 合併 PR 時觸發 CLI。CLI 執行以 SDK 撰寫的自動化 Playwright 測試。測試失敗後，日誌傳送至 Desktop。Desktop 自動在 IDE (VS Code) 中為開發者打開錯誤的網頁元件行，並引導 Agent 執行熱修復。
* **協作方式與步驟**：
  1. **CLI**：在遠端或本地 Git 合併時，自動觸發 **Antigravity CLI**。
  2. **SDK**：CLI 執行 Python 測試腳本 `playwright_test.py`。由於前端頁面的按鈕 ID 變更，測試找不到 Selector 拋出 Timeout 異常。
  3. **Desktop App**：異常日誌被傳送至桌面端。桌面控制中心判定為 Critical 錯誤，在桌面 UI 亮起警告，並將出錯的原始碼路徑傳入開發者的本地環境。
  4. **IDE**：開發者的 VS Code 自動彈出並定位到 [main.js](examples/web_app/main.js) 出錯的第 45 行。**Antigravity IDE v2** 行內跳出對話框：`「偵測到 Playwright Selector 變更，是否一鍵將 #btn-submit 修改為 .btn-submit-primary？」`。點擊確認，一鍵修復。
* **實體代碼**：
  ```python
  # SDK 捕捉測試異常並向 Desktop/IDE 發送定位請求
  except TimeoutError as e:
      client.send_to_desktop(error_log=str(e), target_file="examples/web_app/main.js", error_line=45)
  ```
</details>

<details>
<summary>6. 開發者在 IDE 中撰寫 Markdown 筆記 -> 保存時觸發 CLI 格式校對 -> SDK 自動轉換 Mermaid 為 PNG -> Desktop 自動同步至長期記憶庫</summary>

* **情境說明**：開發者在 IDE 撰寫筆記。存檔時觸發 CLI 呼叫格式檢查。SDK 同步執行 Python 腳本將筆記內的 Mermaid 流程圖渲染為實體圖片，最終 Desktop App 將完整的筆記與圖片同步存入 OneDrive 長期記憶中。
* **協作方式與步驟**：
  1. **IDE**：開發者在 VS Code 中編輯 [note_writing_guide.md](examples/note_writing/note_writing_guide.md) 並按下儲存。
  2. **CLI**：VS Code 的 Save-Hook 自動調用 **Antigravity CLI**，對 Markdown 執行語法與相對連結有效性校對。
  3. **SDK**：校對通過後，CLI 呼叫以 **Antigravity SDK** 撰寫的 Mermaid 渲染器。Python 腳本將筆記中的 `graph TD` 流程圖渲染為實體 `mermaid_chart.png`，並精確插入 Markdown 中。
  4. **Desktop App**：桌面端記憶管理器收到通知，自動將生成的 Markdown 與 PNG 圖片同步備份至您指定的 OneDrive 長期記憶庫目錄 `D:\Users\148015\OneDrive - 成大醫院\Hosp\code\AgentSettings\NOTES\`。
* **實體指令**：
  ```powershell
  # CLI 執行格式校對
  antigravity md-lint --file="examples/note_writing/note_writing_guide.md" --strict
  ```
</details>

<details>
<summary>7. Desktop 掛載 PostgreSQL MCP -> CLI 定時查詢慢 SQL -> SDK 調用 SQL 優化 Agent -> IDE 彈出索引建立的 SQL 腳本供開發者套用</summary>

* **情境說明**：Desktop 掛載了資料庫 MCP。CLI 定時執行資料庫查詢，偵測到一條慢 SQL (慢查詢)。SDK 調用 Database Agent 分析。最終在開發者的 IDE (VS Code) 彈出建立複合索引 (Composite Index) 的 SQL 腳本，開發者一鍵執行優化。
* **協作方式與步驟**：
  1. **Desktop App**：全域掛載 PostgreSQL MCP 服務。
  2. **CLI**：CLI 定時任務 `/schedule cron="*/10 * * * *"` 啟動，連線資料庫查詢 `pg_stat_activity`，發現一條查詢耗時大於 2 秒的慢 SQL。
  3. **SDK & Agent**：CLI 將慢 SQL 傳送給 **Antigravity SDK**，啟動 **DatabaseExpert** 代理。Agent 分析 SQL，發現 `orders` 表的 `user_id` 與 `created_at` 欄位缺乏索引，自動生成 `CREATE INDEX` 的優化腳本。
  4. **IDE**：開發者的 VS Code 編輯器彈出 [db_optimization.sql](examples/database/db_optimization.sql)。**Antigravity IDE v2** 行內高亮顯示建議的 SQL。開發者點擊 `Run Optimization`，一鍵在資料庫中建立複合索引，查詢時間縮短至 0.01 秒。
* **實體 SQL**：
  ```sql
  -- IDE 中彈出的一鍵優化腳本
  CREATE INDEX idx_orders_user_created ON orders (user_id, created_at);
  ```
</details>

<details>
<summary>8. SDK 讀取銷售大數據 -> 自動生成 Excel -> CLI 封裝成 EML 郵件 -> Desktop 背景排程 Daemon 發送 -> IDE 提供發送狀態日誌</summary>

* **情境說明**：SDK 讀取銷售數據生成 Excel 報表。CLI 自動呼叫 Python 腳本將報表封裝為帶有精美 HTML 樣式的 `.eml` 郵件。Desktop App 背景排程 Daemon 自動將其發送，並在 IDE 提供發送日誌觀測。
* **協作方式與步驟**：
  1. **SDK**：Python 數據分析腳本運行，利用 Pandas 讀取 `sales_data.csv` 並生成月度銷售 Excel。
  2. **CLI**：CLI 呼叫 `generate_eml_task.py`，將 Excel 報表作為附件，自動封裝成一封帶有 Premium HTML 模板的 `meeting_release.eml` 郵件。
  3. **Desktop App**：桌面端 Daemon 背景服務啟動，自動將生成的 `.eml` 傳送至企業 SMTP 伺服器進行行政發佈。
  4. **IDE**：發送成功後，VS Code 終端控制台即時輸出 `[✓] EML Mail sent successfully` 日誌，供開發者審查。
* **實體指令**：
  ```powershell
  # CLI 執行 EML 生成指令
  antigravity eml --generate --template="meeting_minutes_template.md" --attach="sales_performance.png"
  ```
</details>

<details>
<summary>9. IDE 觸發 /grill-me 互動 -> 確定設計方案 -> Desktop 生成實作 task.md -> CLI 自動生成基礎結構代碼 -> SDK 執行單元測試驗證</summary>

* **情境說明**：開發者在 IDE 啟用 `/grill-me` 指令審查設計。方案確定後，Desktop App 自動生成任務追蹤檔。CLI 依此檔案自動生成 Python 基礎結構代碼，SDK 隨即在背景執行單元測試驗證，一氣呵成。
* **協作方式與步驟**：
  1. **IDE**：開發者在 VS Code 側邊欄輸入 `/grill-me` 進行「電商訂單系統」的架構審查，與 Agent 互動定案。
  2. **Desktop App**：桌面控制中心依據定案方案，在專案目錄下自動生成並加載 `task.md` 任務追蹤文件。
  3. **CLI**：任務文件生成後，CLI 自動觸發腳本，一鍵在 `examples/` 下建立模組目錄與基礎結構 Class 檔案。
  4. **SDK**：基礎代碼生成後，SDK 背景測試 Agent 自動連線，執行 `pytest` 進行初始單元測試驗證，並在 Desktop UI 上將該任務標記為 `[x]` 完成。
* **實體指令**：
  ```powershell
  # CLI 依據 task.md 一鍵生成結構代碼
  antigravity scaffold --from-task="task.md" --target-dir="examples/scaffold_app"
  ```
</details>

<details>
<summary>10. CLI 靜態掃描發現 API 金鑰暴露 -> Desktop 立即凍結 Agent 文件寫入權限 (安全沙盒啟動) -> SDK 動態將金鑰移至環境變數 -> IDE 自動更新配置檔案</summary>

* **情境說明**：CLI 掃描代碼時發現開發者不小心在代碼中寫死了 API 金鑰。Desktop 控制中心基於安全沙盒機制，立即凍結 Agent 的文件寫入權限。SDK 隨即啟動，動態將金鑰移至環境變數中，最後 IDE 自動更新本地的設定檔案。
* **協作方式與步驟**：
  1. **CLI**：執行 commit 前掃描，發現 `config.py` 中存在暴露的 `API_KEY = "ghp_securekey123"`。
  2. **Desktop App (安全沙盒)**：桌面端控制中心立即觸發 `Security Sandbox` 警告，限制該 Agent 寫入此專案的 `.git` 與 `.env` 權限，以防金鑰外洩。
  3. **SDK**：SDK 呼叫安全代理，將寫死的金鑰提取出來，安全地將其改為從環境變數讀取。
  4. **IDE**：開發者的 VS Code 自動彈出更新後的 `config.py` 對比畫面。開發者點擊確認，將 `API_KEY` 完美轉換，消除資安風險！
* **實體代碼**：
  ```python
  # IDE 一鍵安全轉換結果
  import os
  # ✓ 已成功將寫死金鑰移至環境變數 (CWE-798 防範)
  API_KEY = os.getenv("GITHUB_TOKEN")
  ```
</details>

---

現在，您已經完全掌握了 Antigravity 2.0 工具家族與 50 大實戰情境的最高境界！請點擊 [🔗 返回主手冊](README.md) 開始體驗真實的代碼開發，或前往您的 [GitHub 倉庫](https://github.com/pandaorz/antigravity_2.0_tutorial) 進行線上閱讀！
