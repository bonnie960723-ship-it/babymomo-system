# 寶貝機系統 — 部署到雲端（24 小時開著）

部署完成後會有一個固定網址，例如：
https://babymomo-xxxx.up.railway.app

不用再開你的電腦，任何人、任何裝置都能用。

---

## 推薦平台：Railway（最簡單）

### 步驟

1. 到 https://railway.app 註冊（可用 GitHub 登入）
2. 點 **New Project** → **Deploy from GitHub repo**
   - 如果還沒把專案放到 GitHub：
     - 先到 https://github.com/new 新建一個空倉庫
     - 把整個 `babymomo-system` 資料夾上傳上去
3. Railway 偵測到專案後，會自動用 `Procfile` 啟動
4. 部署完成後，到 **Settings → Networking → Generate Domain**
5. 得到網址後，用瀏覽器打開即可

### 預設帳號（部署後一樣）
- bonnie / Aa960723
- chrisavicii / Aa0965652118

### 建議加上 PostgreSQL（資料不會因為重啟消失）

1. 在 Railway 專案點 **+ New** → **Database** → **PostgreSQL**
2. 部署完成後，PostgreSQL 的 `DATABASE_URL` 會自動注入
3. 系統會自動改用 PostgreSQL，資料永久保存

---

## 另一個選擇：Render

1. 到 https://render.com 註冊
2. New → Web Service
3. 連接你的 GitHub 倉庫
4. 設定：
   - **Root Directory**: 留空
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
5. 建立後產生網址即可使用

（Render 免費方案會在一段時間沒人用時休眠，有人訪問會再醒來）

---

## 本機測試部署指令

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 注意事項

- 如果只用 SQLite（沒加 PostgreSQL），免費平台重啟後資料可能會清空
- 正式長期使用請加上 PostgreSQL
- 密碼請在正式環境自行修改（目前寫在程式啟動邏輯中）
