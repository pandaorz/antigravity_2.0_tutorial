# 🚀 Antigravity v2 終極修煉手冊：從 10x 開發到全能 Agent 協作

歡迎來到 **Antigravity v2** 的時代！

不論您是需要寫出安全高效程式碼的 **資深 10x 軟體工程師**、要撰寫學術級筆記的 **學霸導師**，抑或是需要處理繁複公文與自動化排程的 **精確行政管理師**，Antigravity v2 都是您最強大的 AI 協作夥伴。

本手冊旨在教您如何徹底釋放 Antigravity v2 的威力。除了深入剖析 v2 的革新特色與 v1 的關鍵差異，我們更為您設計了 **9 大實戰場景**，並在專案工作區提供了**完整的、無佔位符的實體程式碼範例**。您可以直接在本地點開檔案、執行腳本，並親身體會 AI 開發的未來！

---

## 🎯 快速導覽

1. [📂 專案目錄結構](#-專案目錄結構)
2. [⚔️ 第一部分：Antigravity v2 核心革新與 v1 深度對比](#-第一部分antigravity-v2-核心革新與-v1-深度對比)
   - [IDE 模式大變革：v2 沒有傳統 IDE 怎麼辦？](#ide-模式大變革v2-沒有傳統-ide-怎麼辦)
   - [v1 vs v2 功能快速對照表](#v1-vs-v2-功能快速對照表)
3. [🛡️ 第二部分：Antigravity v2 工具家族全景與協作生態](docs/tool_family.md)
   - [Desktop App / IDE Extensions / CLI / SDK 全成員特色](docs/tool_family.md#-四大核心工具剖析)
   - [企業級 CI/CD 自動化安全修補與 Code Review 協作案例](docs/tool_family.md#-跨工具家族協作實戰-symphony-workflow)
4. [🛠 第三部分：九大實戰場景教學與代碼說明](#-第三部分九大實戰場景教學與代碼說明)
   - [場景 1：極致美學網頁開發](#場景-1極致美學網頁開發)
   - [場景 2：跨平台 Bash/PowerShell 腳本](#場景-2跨平台-bashpowershell-腳本)
   - [場景 3：學霸級筆記撰寫](#場景-3學霸級筆記撰寫)
   - [場景 4：行政庶務與 EML 自動化](#場景-4行政庶務與-eml-自動化)
   - [場景 5：資安檢測與漏洞審查 (SecOps)](#場景-5資安檢測與漏洞審查-secops)
   - [場景 6：科學文獻搜尋與分析 (Science)](#場景-6科學文獻搜尋與分析-science)
   - [場景 7：數據彙整與圖表繪製 (Data Science)](#場景-7數據彙整與圖表繪製-data-science)
   - [場景 8：資料庫 Schema 設計與 SQL 調優 (Database)](#場景-8資料庫-schema-設計與-sql-調優-database)
   - [場景 9：Playwright 瀏覽器自動化 (Automation)](#場景-9playwright-瀏覽器自動化-automation)
5. [🤖 第四部分：Agent 進階操作與 Subagents 指南](docs/agent_operations.md)
6. [🧠 第五部分：長期記憶引擎 (Memory Engine) 與學習閉環](#-第五部分長期記憶引擎-memory-engine-與學習閉環)

---

## 📂 專案目錄結構

本教學專案在您的工作區中已建構了以下實體目錄與檔案，建議您搭配 VS Code 或其他編輯器點擊連結查看：

*   **[README.md](README.md)**：本主教學手冊。
*   **[docs/tool_family.md](docs/tool_family.md)**：Antigravity v2 工具家族成員（Desktop App, IDE, CLI, SDK）特色與跨工具自動化協作指南。
*   **[docs/agent_operations.md](docs/agent_operations.md)**：Agent 進階操作、子代理協作與 Slash 指令的超詳細步驟手冊。
*   **[examples/](examples/)**：
    *   **[web_app/](examples/web_app/)**：場景 1 — 極致美學的 Vite + Vanilla CSS 網頁系統。
    *   **[bash_scripts/](examples/bash_scripts/)**：場景 2 — 跨平台備份與系統監控腳本。
    *   **[note_writing/](examples/note_writing/)**：場景 3 — 學霸筆記與 Markdown 高級語法範本。
    *   **[office_admin/](examples/office_admin/)**：場景 4 — 會議紀錄範本與 Python 自動生成 `.eml` 郵件腳本。
    *   **[secops/](examples/secops/)**：場景 5 — 靜態弱點掃描 (SAST) 與 SQL 注入審查工具。
    *   **[science/](examples/science/)**：場景 6 — 自動調用 PubMed/arXiv API 的文獻分析工具。
    *   **[data_science/](examples/data_science/)**：場景 7 — Pandas 銷售數據處理與 Matplotlib 圖表繪製。
    *   **[database/](examples/database/)**：場景 8 — 電商 Schema 設計與慢查詢優化手冊。
    *   **[testing/](examples/testing/)**：場景 9 — Playwright 自動化爬蟲與 UI 端對端測試。

---

## ⚔️ 第一部分：Antigravity v2 核心革新與 v1 深度對比

### IDE 模式大變革：v2 沒有傳統 IDE 怎麼辦？

> [!IMPORTANT]
> **「v1 有網頁版 IDE 可視化界面，v2 卻沒有，我要怎麼修改與檢視我的檔案？」**
> 
> 這是許多 v1 使用者升級後的第一個疑問。答案是：**v2 採用了更先進的「Agentic 本地無縫整合」模式**。
> 
> 在 v1 中，您必須在瀏覽器那窄小的網頁 IDE 中點擊與打字，效能受限，且無法使用您熟悉的 VS Code 插件、捷徑與開發環境。
> 
> **在 v2 中，Agent 本身就是您的「隱形 IDE」**：
> 1.  **檔案檢視工具 (`view_file`, `list_dir`)**：Agent 可以直接讀取並檢索專案內的任何檔案，支援一次查看最多 800 行，並在需要時將結構呈獻給您。
> 2.  **精確檔案編修工具 (`replace_file_content`, `multi_replace_file_content`)**：
>     *   Agent **不需要**您提供網頁 IDE 編輯。您只需在對話中告訴 Agent：「*請修改 OOO 檔案，將 XXX 函式改為具備防呆機制的新版本。*」
>     *   Agent 就會使用 `replace_file_content` 工具，指定行號與精確字串，在您本地的專案資料夾中完成「無縫滴入式修改」。
>     *   **這意味著您可以一邊在您最喜歡的本地 VS Code / Cursor / Fleet 中寫扣與享受極速的熱重載，一邊在側邊欄命令 Agent 幫您編修、重構或除錯。**

#### 💡 如何精確命令 Agent 修改您的檔案？
*   **錯誤示範**：`「幫我改一下 utils.py 的資料庫連線程式碼」`（太籠統，Agent 可能需要反覆猜測）。
*   **資深工程師推薦示範**：
    > 「請查看 [utils.py](utils.py)，將第 25 行開始的 `db_connect` 函式修改為使用 Try-Catch 區塊，並加入防呆的環境變數讀取檢查。修改完成後，請用 PowerShell 執行 `python utils.py` 進行驗證。」

---

### v1 vs v2 功能快速對照表

| 功能維度 | Antigravity v1 (舊版) | Antigravity v2 (新版 🚀) |
| :--- | :--- | :--- |
| **工作流模式** | 單一的「問與答」對話式 Chat，容易遺漏任務與上下文。 | **規劃驅動 (Planning Mode)**：重大任務前先撰寫並審查 `implementation_plan.md`，執行時以 `task.md` 追蹤進度，完成後以 `walkthrough.md` 驗證。 |
| **檔案編輯界面** | 網頁專屬 Web-IDE 編輯器（效能有限）。 | **本地 IDE 滴入式修改**：直接在您的 workspace 中編修，完美相容 VS Code，Agent 自動執行精準取代。 |
| **多 Agent 協作** | 無此功能，單兵作戰。 | **子代理調度 (Subagents)**：主 Agent 可定義 (`define_subagent`)、調度 (`invoke_subagent`) 專門領域子 Agent 在後台同步工作並向您回報。 |
| **任務定時排程** | 無法執行背景定時任務。 | **排程定時器 (Schedule)**：支援 one-shot timer 與 recurring cron 任務，並可使用 `manage_task` 管理後台長工。 |
| **安全防呆邊界** | 無 pre-flight 檢查，常因環境不對而報錯。 | **起手式 Pre-flight 檢查**：自動偵測 `README.md` 的專案規格與特定虛擬環境路徑（如啟動 `Activate.ps1`），遵守 OWASP / CWE 資安規範與腳本冪等性。 |
| **科學與專業工具** | 無專業領域 Skills。 | 內建 40+ 專業科學插件（PubMed, ClinicalTrials, ChEMBL, AlphaFold, OpenAlex, Playwright 等）。 |

---

## 🛡️ 第二部分：Antigravity v2 工具家族全景與協作生態

> [!IMPORTANT]
> **「Antigravity v2 僅剩 Agent，這代表我們失去了其他工具支援嗎？」**
> 
> 絕對沒有！Google 宣布將旗下所有開發者 AI 工具整合，在 v2 中解耦為更強大的**四大核心成員**：
> 1.  **Desktop App (Mission Control)**：多代理控制中樞，提供視覺化狀態監控與排程管理。
> 2.  **IDE Extensions**：無縫整合本地 VS Code / JetBrains，提供 AI 滴入式修改與行內 Diff 對比。
> 3.  **CLI (Go-based)**：高效能 Go 語言命令列工具，專為終端機自動化與 Git 鉤子 (Hooks) 設計。
> 4.  **SDK (Python-based)**：程式化調用 Agent Runtime 的開發套件，可直接嵌入自定義應用程式。
> 
> 四大成員各司其職，並且能組成完美的協作流水線（例如 pre-commit 觸發 CLI 掃描 -> SDK 呼叫 Agent 自動修補並提交 PR -> Desktop App 審查成果）。
> 
> 📖 **[點此深入閱讀：Antigravity v2 工具家族成員特色與跨工具協作指南](docs/tool_family.md)**

---

## 🛠 第三部分：九大實戰場景教學與代碼說明

為了讓您能百分之百掌握，以下我們將詳細說明這 9 個實戰場景。每個場景都有**詳細操作步驟**、**設計邏輯**與位於 `examples/` 目錄下的**實體檔案連結**。

---

### 場景 1：極致美學網頁開發
*   **目的**：摒棄簡陋的 MVP 樣式，利用現代 Vanilla CSS、漸層與微動畫，打造Wow等級的 premium 介面。
*   **設計邏輯**：使用 HSL 色調、 sleek 玻璃擬態 (glassmorphism) 質感，並嚴格防範 XSS 與 CSRF 漏洞（在 JS 中使用 `textContent` 替代 `innerHTML` 防範注入）。
*   **範例檔案**：
    *   主 HTML：[index.html](examples/web_app/index.html)
    *   美學 CSS：[index.css](examples/web_app/index.css)
    *   邏輯 JS：[main.js](examples/web_app/main.js)
*   **詳細操作步驟**：
    1.  開啟終端機（PowerShell），至專案目錄。
    2.  若要本地啟動開發伺服器，可下指令請 Agent 幫您執行 `npx -y browser-sync start --server --files "examples/web_app/*"`。
    3.  開啟瀏覽器點擊 `http://localhost:3000` 預覽極致美學的動態界面。

---

### 場景 2：跨平台 Bash/PowerShell 腳本
*   **目的**：編寫兼顧 Linux 與 Windows 的系統維護腳本，強調**安全防呆與冪等性**。
*   **設計邏輯**：
    *   Linux Bash 腳本加入 `set -euo pipefail`，確保 any 一步出錯立即中斷，並加入路徑存在檢查與鎖檔機制（防重複執行）。
    *   Windows PowerShell 腳本使用結構化 Try-Catch 錯誤處理，並遵守 `Idempotency` 原則（重覆執行不會損壞資料）。
*   **範例檔案**：
    *   Linux Bash 備份腳本：[backup_tool.sh](examples/bash_scripts/backup_tool.sh)
    *   Windows PowerShell 監控腳本：[system_monitor.ps1](examples/bash_scripts/system_monitor.ps1)
*   **詳細操作步驟**：
    *   *Linux 執行方法*：`chmod +x backup_tool.sh && ./backup_tool.sh /path/to/source /path/to/backup`
    *   *Windows 執行方法*：以管理員開啟 pwsh，執行 `.\system_monitor.ps1 -Threshold 80`

---

### 場景 3：學霸級筆記撰寫
*   **目的**：當您需要整理複雜的技術、知識或家庭決策時，自動轉為「學霸導師」模式，產出結構完整、高可讀性的筆記。
*   **設計邏輯**：嚴格遵守 `NOTE_TAKING_SKILL` 的結構規範。善用 GitHub 的 Alert 標籤、Mermaid 流程圖以及 Carousel（輪播投影片）元素來呈現資訊。
*   **範例檔案**：
    *   學霸筆記範本：[note_writing_guide.md](examples/note_writing/note_writing_guide.md)
*   **詳細操作步驟**：
    1.  對 Agent 下達指令：`「我要整理關於 Docker 網路架構的知識，請用學霸導師模式幫我撰寫筆記」`。
    2.  Agent 會自動按照筆記格式，生成富含 Mermaid 流程圖的 `NOTE_Docker網路.md`，並統一存放至 `D:\Users\148015\OneDrive - 成大醫院\Hosp\code\AgentSettings\NOTES\` 目錄下。

---

### 場景 4：行政庶務與 EML 自動化
*   **目的**：快速整理嚴謹的會議紀錄，並以 Python 腳本自動生成符合國際格式的 `.eml` 郵件，進行行政發佈與排程。
*   **設計邏輯**：遵守 `document_processor` 的規範，不破壞舊有 docx 結構。EML 生成包含標準標頭、MIME 編碼與防呆的主旨/收件人檢查。
*   **範例檔案**：
    *   黃金會議紀錄格式：[meeting_minutes_template.md](examples/office_admin/meeting_minutes_template.md)
    *   EML 生成 Python 腳本：[generate_eml_task.py](examples/office_admin/generate_eml_task.py)
*   **詳細操作步驟**：
    1.  使用 `python generate_eml_task.py`，它將在同目錄下生成一個帶有漂亮 HTML 樣式的 `meeting_release.eml` 檔案。
    2.  雙擊 `meeting_release.eml` 即可直接以 Outlook 或 Thunderbird 等郵件軟體開啟、檢視並發送。

---

### 場景 5：資安檢測與漏洞審查 (SecOps) [新增]
*   **目的**：以資安 SecOps 視角，對程式碼進行靜態弱點掃描 (SAST) 以及對 SQL Injection 等 OWASP Top 10 漏洞進行檢測與修補說明。
*   **設計邏輯**：利用 Python 實作一個簡單但精確的正規表示式弱點掃描器，並詳細解析「為何會產生 SQL 注入」以及「如何以參數化查詢（Prepared Statements）進行修補」。
*   **範例檔案**：
    *   資安弱點掃描與修補範例：[security_audit.py](examples/secops/security_audit.py)
*   **詳細操作步驟**：
    1.  點開 `security_audit.py`，裡面包含一段「含有漏洞的 PHP/Python 程式碼」與「修補後的安全程式碼」。
    2.  執行 `python security_audit.py`，該工具將會自動掃描檔案，報告出其中含有的安全性風險（如寫死的 API Key、未參數化的 SQL 語句），並給出防範建議。

---

### 場景 6：科學文獻搜尋與分析 (Science) [新增]
*   **目的**：利用醫學學術資料庫 PubMed API 進行前沿研究的檢索與綜述整理，解決「科學文獻查找費時費力」的痛點。
*   **設計邏輯**：使用 Python 的 `urllib` 封裝 PubMed Entrez Utilities，檢索指定關鍵字的文章標題與摘要，篩選出高影響力的文獻並生成精簡的 Markdown 綜述。
*   **範例檔案**：
    *   科學文獻搜尋工具：[pubmed_researcher.py](examples/science/pubmed_researcher.py)
*   **詳細操作步驟**：
    1.  執行 `python pubmed_researcher.py --query "CAR-T therapy solid tumors"`
    2.  該指令將自動向 PubMed API 請求最新的 5 篇相關論文，下載其標題、作者、PMID 與摘要，並在同目錄生成一份 `literature_review.md`。

---

### 場景 7：數據分析、CSV 處理與精美圖表繪製 (Data Science) [新增]
*   **目的**：讀取外部 CSV 數據，利用 Pandas 進行高效率的數據分組與統計，並使用 Matplotlib 繪製極具美感的視覺化圖表。
*   **設計邏輯**：確保 CSV 讀取具備異常處理（防範檔案不存在或欄位缺失），且繪製的圖表搭配和諧的色彩、乾淨的網格與圖例，可直接用於報告。
*   **範例檔案**：
    *   數據分析與繪圖腳本：[data_analyzer.py](examples/data_science/data_analyzer.py)
    *   模擬銷售數據 CSV：[sales_data.csv](examples/data_science/sales_data.csv)
*   **詳細操作步驟**：
    1.  執行 `python data_analyzer.py`
    2.  腳本將自動讀取銷售資料，計算各產品線的總銷售額與毛利率，並在目錄下生成一張漂亮的圖表 `sales_performance.png`。

---

### 場景 8：資料庫設計、SQL 效能調校與遷移 (Database) [新增]
*   **目的**：設計一個高效能、符合第3正規化（3NF）的電商資料庫架構，並針對 Slow Query 進行優化與遷移。
*   **設計邏輯**：建立包含 `users`、`orders`、`order_items` 的完整電商 SQL 設計，加入外鍵約束、唯一性限制，並示範「如何使用 EXPLAIN 分析查詢效能」以及「如何建立複合索引（Composite Index）」以提高查詢速度。
*   **範例檔案**：
    *   資料庫 Schema 與 SQL 優化手冊：[db_optimization.sql](examples/database/db_optimization.sql)
*   **詳細操作步驟**：
    1.  閱讀 `db_optimization.sql`，裡面有詳細的 SQL 設計架構。
    2.  手冊中詳細教學了如何使用 `EXPLAIN` 指令，並透過一個真實的慢查詢優化案例，展示優化前後的效能差異（查詢時間從 2.5秒 降至 0.01秒）。

---

### 場景 9：Playwright 瀏覽器自動化 (Automation) [新增]
*   **目的**：編寫 Playwright 自動化測試與爬蟲腳本，實現網頁自動化填表、截圖與狀態斷言（E2E Testing）。
*   **設計邏輯**：採用 async/await 非同步架構，具備完善的等待機制（Wait For Selector）以應對動態載入的網頁元素，並加入出錯時的防呆自動截圖保存。
*   **範例檔案**：
    *   Playwright 自動化測試腳本：[playwright_test.py](examples/testing/playwright_test.py)
*   **詳細操作步驟**：
    1.  確保已安裝 Playwright：`pip install playwright` 且 `playwright install`
    2.  執行 `python playwright_test.py`
    3.  腳本將會在背景（無頭模式）啟動瀏覽器，前往指定的網頁，自動填寫表單並點擊按鈕，最後將網頁狀態與截圖保存為 `screenshot.png` 以進行驗證。

---

## 🤖 第四部分：Agent 進階操作與 Subagents 指南

(請參考 [docs/agent_operations.md](docs/agent_operations.md))

---

## 🧠 第五部分：長期記憶引擎 (Memory Engine) 與持續進化

在 Antigravity v2 中，**您的每一次對話與開發成果都不會被遺忘**。

### 核心職責：記憶管理與 Student Loop
當一個階段性任務完成（例如 Bug 修復成功、新專案策略產出、或您設定了個人偏好），Agent 會主動向您提議：**「是否需要將此成果/偏好存入長期記憶？」**

*   **長期記憶存放處**：專案根目錄的 `MEMORY/` 資料夾中（以 Markdown 格式維護）。
*   **工作流閉環**：這確保了當您開啟一個新的對話時，新對話中的 Agent 能夠自動讀取這些記憶，繼承先前的決策與您的個人開發習慣，實現跨對話的連續性！

現在，若您準備好了，請繼續點擊閱讀 **[Agent 進階操作與 Subagents 協作指南](docs/agent_operations.md)**，讓我們一起掌握 Subagents 與 Slash Commands 的最高境界！
