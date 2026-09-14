"""LINE Messaging API 推播。

無法用一般 LINE ID（例如 chrischuang1118）直接傳訊。
需要：
1. LINE Official Account + Messaging API
2. Channel access token
3. 對方加入官方帳號好友後的 userId（U 開頭）
"""
import json
import os
import urllib.request
import urllib.error


LINE_API = "https://api.line.me/v2/bot/message/push"


def line_configured() -> bool:
    return bool(os.getenv("LINE_CHANNEL_ACCESS_TOKEN") and os.getenv("LINE_USER_ID"))


def send_line_text(text: str, to_user: str | None = None) -> dict:
    token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "").strip()
    user_id = (to_user or os.getenv("LINE_USER_ID", "")).strip()
    if not token or not user_id:
        return {
            "ok": False,
            "simulated": True,
            "reason": "尚未設定 LINE_CHANNEL_ACCESS_TOKEN 或 LINE_USER_ID",
            "preview": text,
        }
    body = json.dumps({
        "to": user_id,
        "messages": [{"type": "text", "text": text[:4900]}],
    }).encode("utf-8")
    req = urllib.request.Request(
        LINE_API,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return {"ok": True, "simulated": False, "status": resp.status, "preview": text}
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="ignore")
        return {"ok": False, "simulated": False, "status": e.code, "error": err, "preview": text}
    except Exception as e:
        return {"ok": False, "simulated": False, "error": str(e), "preview": text}
