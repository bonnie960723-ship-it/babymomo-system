# 寶貝機 長者體適能與肌少衰弱檢測分析系統（真實可用版）

這是從原本純前端 demo 重做的**完整可用系統**，具備：

- ✅ 真實後端 API（FastAPI）
- ✅ SQLite 持久化資料庫（資料不會因清瀏覽器而消失）
- ✅ 多人登入 / JWT 權限
- ✅ CSV / Excel 真實匯入
- ✅ 肌少症分期自動判斷（AWGS 簡易標準）
- ✅ 統計儀表板 + 個案趨勢圖
- ✅ 標準 RESTful API，可供 HIS / 長照平台 / 物聯網設備串接
- ✅ 自動產生 Swagger 文件

---

## 快速啟動

### 1. 安裝依賴

```bash
cd backend
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 啟動服務

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

瀏覽器開啟：http://localhost:8000

### 3. 管理員帳號

| 帳號 | 密碼 | 角色 |
|------|------|------|
| bonnie | Aa960723 | 系統管理員 |
| chrisavicii | Aa0965652118 | 超級管理員 |

---

## 匯入真實資料

1. 登入後點左側「匯入資料」
2. 上傳 CSV 或 Excel
3. 系統會自動：
   - 對應中英文欄位名稱
   - 計算 BMI
   - 判斷肌少症分期
   - 去重（同一身分證 + 同一時間）
   - 生理數值防呆

### 建議 CSV 欄位（中英文皆可）

```
身分證,姓名,性別,年齡,身高,體重,體脂率,SMI,收縮壓,舒張壓,脈搏,握力,五次坐站,走路時間,檢測時間
A123456789,王小明,男,72,168,65,22.5,7.1,128,78,72,26.5,11.2,18.5,2026-09-09 10:00:00
```

---

## API 串接

完整互動文件：http://localhost:8000/api/docs

### 取得 Token

```bash
curl -X POST http://localhost:8000/api/auth/login \
  -d "username=bonnie&password=Aa960723"
```

### 新增單筆檢測

```bash
curl -X POST http://localhost:8000/api/measurements \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "id_card": "A123456789",
    "user_name": "王小明",
    "gender": "M",
    "age": 72,
    "height": 168,
    "weight": 65,
    "grip_strength": 26.5,
    "chair_stand_time": 11.2,
    "walking_time": 18.5,
    "smi": 7.1,
    "systolic": 128,
    "diastolic": 78,
    "measure_time": "2026-09-09 10:00:00"
  }'
```

### 批次匯入

```bash
curl -X POST http://localhost:8000/api/import \
  -H "Authorization: Bearer <token>" \
  -F "file=@your_data.csv"
```

---

## 生產部署建議

1. 修改 `SECRET_KEY` 環境變數
2. 可改用 PostgreSQL：設定 `DATABASE_URL=postgresql://...`
3. 前面加 Nginx + HTTPS
4. 使用 `gunicorn` 或 `uvicorn` workers

```bash
export SECRET_KEY="your-long-random-secret"
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2
```

---

## 目錄結構

```
babymomo-system/
├── backend/
│   ├── main.py          # FastAPI 主程式
│   ├── models.py        # 資料表
│   ├── schemas.py       # Pydantic 模型
│   ├── auth.py          # JWT 認證
│   ├── utils.py         # 肌少症判斷邏輯
│   ├── database.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   └── app.js
└── README.md
```

資料庫檔案會自動產生在 `backend/babymomo.db`。
