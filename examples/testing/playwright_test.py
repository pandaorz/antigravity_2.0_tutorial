#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Antigravity v2 - Playwright 瀏覽器自動化與 E2E UI 測試 (Secure & Robust)
------------------------------------------------------------------
功能：
1. 使用 Playwright 啟動 Chromium 背景無頭 (Headless) 瀏覽器。
2. 前往 Hacker News (https://news.ycombinator.com) 進行資訊爬取。
3. 抓取排名前 5 的熱門技術文章標題與連結。
4. 自動將瀏覽器頁面截圖並儲存為 'screenshot.png' 以供視覺驗證。
5. 包含完美的環境防呆檢查與安裝步驟提示。
"""

import os
import sys
import asyncio

# 1. Playwright 套件防呆檢查
try:
    from playwright.async_api import async_playwright
except ImportError:
    print("❌ [錯誤] 您的環境尚未安裝 Playwright！")
    print("💡 請執行以下步驟來安裝並配置 Playwright 環境：")
    print("------------------------------------------")
    print("  pip install playwright")
    print("  playwright install")
    print("------------------------------------------")
    sys.exit(1)

async def run_automation(target_url="https://news.ycombinator.com", output_screenshot="screenshot.png"):
    print("==========================================")
    print("🤖 Antigravity Playwright 瀏覽器自動化引擎啟動")
    print("==========================================")
    print(f"目標網址: {target_url}")
    
    # 2. 啟動 Playwright 非同步上下文
    async with async_playwright() as p:
        print("[RUN] 正在啟動背景 Chromium 瀏覽器...")
        browser = await p.chromium.launch(headless=True)
        
        # 3. 建立獨立的瀏覽器上下文與頁面
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        try:
            # 4. 導向目標網頁
            print(f"[RUN] 正在載入頁面...")
            await page.goto(target_url, timeout=30000, wait_until="domcontentloaded")
            
            # 5. 等待關鍵 DOM 元素載入 (防呆：防範非同步載入延遲)
            print("[RUN] 等待文章標題元素渲染...")
            await page.wait_for_selector(".titleline > a", timeout=10000)
            
            # 6. 爬取前 5 篇熱門文章標題與 URL
            print("[RUN] 正在解析前 5 篇熱門文章中介資料...")
            articles = await page.locator(".titleline > a").all()
            
            print("\n🔥 Hacker News 當前熱門排行前 5：")
            print("------------------------------------------")
            for idx, article in enumerate(articles[:5], 1):
                title = await article.text_content()
                href = await article.get_attribute("href")
                print(f"{idx}. 標題: {title}")
                print(f"   連結: {href}")
            print("------------------------------------------\n")
            
            # 7. 自動擷取頁面畫面以供 UI 驗證
            print(f"[RUN] 正在擷取頁面並儲存為: {output_screenshot} ...")
            await page.screenshot(path=output_screenshot)
            
            print(f"✅ [成功] 瀏覽器自動化任務完美完成！")
            print(f"截圖已保存至: {os.path.abspath(output_screenshot)}")
            
        except Exception as e:
            print(f"❌ [錯誤] 瀏覽器自動化執行時發生異常: {str(e)}", file=sys.stderr)
            
        finally:
            # 8. 安全關閉瀏覽器，防範內存洩漏 (Idempotency / Resource Cleanup)
            print("[RUN] 正在釋放瀏覽器資源...")
            await browser.close()
            print("==========================================")

if __name__ == "__main__":
    # 使用 asyncio 啟動協程事件循環
    try:
        # 相容 Windows 平台下的 ProactorEventLoop 限制
        if sys.platform == 'win32':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(run_automation())
    except KeyboardInterrupt:
        print("\n[INFO] 使用者手動中斷任務。")
