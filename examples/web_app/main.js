// ==========================================================================
// JavaScript 交互控制與安全程式碼實作 (符合 OWASP 防 XSS 規範)
// ==========================================================================

// 對比資料庫 (用來切換 v1/v2 的顯示)
const comparisonData = {
    v2: [
        { title: "🎯 規劃與任務追蹤模式", desc: "引進了 implementation_plan.md 與 task.md，在重大變更前會先徵求使用者同意，並全程自我追蹤進度。" },
        { title: "👥 背景子代理協作", desc: "主 Agent 可定義並調度多個子 Agent (Subagents)，在背景並行工作，極致提升效率。" },
        { title: "⚡ 響應式喚醒機制", desc: "Reactive Wakeup 允許 Agent 在背景命令或定時器執行時自動進入 Idle 狀態，完成後自動喚醒，不浪費 Token。" },
        { title: "🛠 本地 IDE 滴入式修改", desc: "無需受限於瀏覽器網頁 IDE，Agent 自動精確修改本地檔案，與本地 VS Code 完美無縫整合。" }
    ],
    v1: [
        { title: "🧊 網頁專屬 Web-IDE", desc: "檔案修改必須在網頁端窄小的編輯器進行，效率低且無法使用本地開發套件。" },
        { title: "🧊 單一 Chat 對話模式", desc: "沒有結構化的任務清單追蹤，隨意對話容易導致代碼前後矛盾、甚至破壞其他模組。" },
        { title: "🧊 單兵作戰限制", desc: "無法將複雜大任務分配給子代理，遇到跨領域的大任務時容易出現幻覺或瓶頸。" },
        { title: "🧊 Token 輪詢浪費", desc: "無法進行背景定時任務與非同步自動喚醒，使用者必須開著網頁被動等待。" }
    ]
};

// 切換頁籤 (Tabs)
function switchTab(version) {
    // 1. 切換 Button 樣式
    const buttons = document.querySelectorAll('.tab-btn');
    buttons.forEach(btn => {
        if ((version === 'v2' && btn.innerText.includes('v2')) || 
            (version === 'v1' && btn.innerText.includes('v1'))) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    // 2. 渲染內容 (安全性：使用安全 DOM 操作 API 避免 HTML 注入 XSS)
    const contentBox = document.getElementById('comparison-content');
    contentBox.innerHTML = ''; // 清空

    const gridDiv = document.createElement('div');
    gridDiv.className = 'comparison-grid';

    const items = comparisonData[version];
    items.forEach(item => {
        const itemBox = document.createElement('div');
        itemBox.className = 'feature-box';

        const titleNode = document.createElement('h4');
        titleNode.textContent = item.title; // 安全：textContent 防範 XSS

        const descNode = document.createElement('p');
        descNode.textContent = item.desc; // 安全：textContent

        itemBox.appendChild(titleNode);
        itemBox.appendChild(descNode);
        gridDiv.appendChild(itemBox);
    });

    contentBox.appendChild(gridDiv);
}

// 快速指令選取
function selectCommand(cmdText) {
    const input = document.getElementById('cmd-input');
    input.value = cmdText;
}

// 模擬指令執行日誌與 Reactive Wakeup 動畫
let isRunning = false;
function executeSimulatedCommand() {
    if (isRunning) return;
    
    const inputVal = document.getElementById('cmd-input').value;
    const consoleBox = document.getElementById('console-output');
    const statusDot = document.getElementById('status-dot');
    const statusText = document.getElementById('status-text');

    if (!inputVal) {
        alert("請先選擇或輸入一個指令！");
        return;
    }

    isRunning = true;
    consoleBox.innerHTML = ''; // 清空 console
    
    // 更新狀態為：執行中
    statusDot.className = 'status-dot pulse-running';
    statusText.textContent = '任務處理中 (Active - Planning & Running)';

    // 日誌輔助函式 (安全性：textContent)
    const log = (text, type = 'system') => {
        const line = document.createElement('span');
        line.className = `${type}-msg`;
        line.textContent = `[${new Date().toLocaleTimeString()}] ${text}`;
        consoleBox.appendChild(line);
        consoleBox.scrollTop = consoleBox.scrollHeight;
    };

    // 模擬長任務執行與非同步喚醒時間線
    log(`解析指令: ${inputVal}`, 'info');
    
    setTimeout(() => {
        log("建立 implementation_plan.md 實作計畫並自動核准", "system");
    }, 800);

    setTimeout(() => {
        log("指派子代理 SecOpsAuditor 進行代碼弱點審查...", "info");
    }, 1600);

    setTimeout(() => {
        // 進入 Reactive Wakeup 背景 Idle 狀態
        log("任務送入背景。主 Agent 進入閒置狀態，Token 暫停消耗，靜候子代理回報...", "warning");
        statusDot.className = 'status-dot';
        statusDot.style.backgroundColor = '#94a3b8'; // 灰色表示休眠
        statusDot.style.boxShadow = 'none';
        statusDot.style.animation = 'none';
        statusText.textContent = '背景休眠中 (Idle - Waiting for callback)';
    }, 2800);

    setTimeout(() => {
        // 子代理回傳訊號，喚醒主 Agent
        log("⚡ [信號接收] 子代理 SecOpsAuditor 完成任務！Reactive Wakeup 自動喚醒主 Agent！", "success");
        statusDot.className = 'status-dot pulse-running';
        statusText.textContent = '正在彙整報告中...';
    }, 4500);

    setTimeout(() => {
        log("任務順利完成！已生成 examples/secops/ 弱點審查報告！", "success");
        log("建立 walkthrough.md 成果並同步更新長期記憶庫 MEMORY/", "system");
        
        // 重設狀態為 Idle
        statusDot.className = 'status-dot pulse-idle';
        statusDot.removeAttribute('style'); // 移去灰色覆蓋
        statusText.textContent = '閒置中 (Idle - Reactive Mode)';
        isRunning = false;
    }, 6000);
}

// 網頁載入時預設初始化
window.onload = () => {
    switchTab('v2');
};
