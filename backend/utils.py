"""業務邏輯：肌少症分期判斷、BMI 計算、異常項目統計"""

from typing import Optional, Tuple


def calc_bmi(height_cm: Optional[float], weight_kg: Optional[float]) -> Optional[float]:
    if not height_cm or not weight_kg or height_cm <= 0:
        return None
    h = height_cm / 100.0
    return round(weight_kg / (h * h), 1)


def judge_sarcopenia(
    gender: str,
    grip: Optional[float],
    chair: Optional[float],
    walk: Optional[float],
    smi: Optional[float],
) -> Tuple[str, int, str]:
    """
    依衛福部 / AWGS 2019 簡易標準判斷肌少症分期。
    回傳 (stage, abnormal_count, status_text)
    """
    is_male = gender.upper() in ("M", "男")
    grip_std = 28.0 if is_male else 18.0
    smi_std = 7.0 if is_male else 5.7

    issues = []
    low_muscle = False   # 肌力或肌肉量不足
    low_function = False # 身體功能不足

    if grip is not None:
        if grip < grip_std:
            issues.append(f"握力不足 ({grip:.1f} kg)")
            low_muscle = True

    if smi is not None:
        if smi < smi_std:
            issues.append(f"SMI肌肉量偏低 ({smi:.1f})")
            low_muscle = True

    if chair is not None:
        if chair >= 12.0:
            issues.append(f"坐站偏慢 ({chair:.2f} s)")
            low_function = True

    if walk is not None:
        if walk >= 20.0:  # 約等於 6 公尺 < 0.8 m/s 的簡化
            issues.append(f"步速偏慢 ({walk:.2f} s)")
            low_function = True

    # 分期邏輯（簡化版）
    if low_muscle and low_function:
        stage = "嚴重肌少症"
    elif low_muscle:
        stage = "肌少症"
    elif low_function:
        stage = "肌少症前期"
    else:
        stage = "正常"

    # 血壓額外提示（不影響分期）
    # 這裡只在 status 顯示

    status = " / ".join(issues) if issues else "各項指標正常"
    return stage, len(issues), status


def normalize_measure_time(raw: Optional[str]) -> Tuple[str, str]:
    """回傳 (measure_date, measure_time)"""
    from datetime import datetime
    if not raw:
        now = datetime.now()
        return now.strftime("%Y-%m-%d"), now.strftime("%Y-%m-%d %H:%M:%S")

    raw = str(raw).strip().replace("/", "-")
    for fmt in (
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d",
        "%Y/%m/%d %H:%M:%S",
        "%Y/%m/%d",
    ):
        try:
            dt = datetime.strptime(raw, fmt)
            return dt.strftime("%Y-%m-%d"), dt.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
    # fallback
    now = datetime.now()
    return now.strftime("%Y-%m-%d"), now.strftime("%Y-%m-%d %H:%M:%S")
