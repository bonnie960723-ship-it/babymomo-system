import json
import os
import urllib.request
import urllib.error

LINE_API = "https://api.line.me/v2/bot/message/push"


def _destinations(to_user=None):
    dests = []
    t1 = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "").strip()
    u1 = (to_user or os.getenv("LINE_USER_ID", "")).strip()
    if t1 and u1:
        dests.append((os.getenv("LINE_OA_ID", "").strip() or "OA1", t1, u1))
    t2 = os.getenv("LINE_CHANNEL_ACCESS_TOKEN_2", "").strip()
    u2 = os.getenv("LINE_USER_ID_2", "").strip()
    if t2 and u2:
        dests.append((os.getenv("LINE_OA_ID_2", "").strip() or "OA2", t2, u2))
    return dests


def line_configured():
    return bool(_destinations())


def _push(token, user_id, text):
    body = json.dumps({
        "to": user_id,
        "messages": [{"type": "text", "text": text[:4900]}],
    }).encode("utf-8")
    req = urllib.request.Request(
        LINE_API,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return {"ok": True, "status": resp.status}
    except urllib.error.HTTPError as e:
        return {"ok": False, "status": e.code, "error": e.read().decode("utf-8", "ignore")}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def send_line_text(text, to_user=None):
    dests = _destinations(to_user)
    if not dests:
        return {"ok": False, "simulated": True, "reason": "尚未設定 LINE 變數", "preview": text}
    results = []
    all_ok = True
    for oa, token, user_id in dests:
        r = _push(token, user_id, text)
        r["oa"] = oa
        results.append(r)
        if not r.get("ok"):
            all_ok = False
    return {"ok": all_ok, "simulated": False, "preview": text, "results": results}
