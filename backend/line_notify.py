import json
import os
import urllib.request
import urllib.error

LINE_API = "https://api.line.me/v2/bot/message/push"


def _destinations(to_user=None):
    dests = []
    pairs = [
        ("LINE_CHANNEL_ACCESS_TOKEN", "LINE_USER_ID", "LINE_OA_ID"),
        ("LINE_CHANNEL_ACCESS_TOKEN_2", "LINE_USER_ID_2", "LINE_OA_ID_2"),
        ("LINE_CHANNEL_ACCESS_TOKEN_3", "LINE_USER_ID_3", "LINE_OA_ID_3"),
        ("LINE_CHANNEL_ACCESS_TOKEN_4", "LINE_USER_ID_4", "LINE_OA_ID_4"),
        ("LINE_CHANNEL_ACCESS_TOKEN_5", "LINE_USER_ID_5", "LINE_OA_ID_5"),
    ]
    for i, (tk, uid, oa) in enumerate(pairs, start=1):
        token = os.getenv(tk, "").strip()
        user = os.getenv(uid, "").strip()
        if i == 1 and to_user:
            user = to_user.strip()
        if token and user:
            dests.append((os.getenv(oa, "").strip() or ("OA" + str(i)), token, user))
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
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + token},
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
