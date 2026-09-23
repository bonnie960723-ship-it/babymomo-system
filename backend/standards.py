"""61-96歲男女各項檢測標準值（依年齡＋性別）"""
from typing import Optional, Dict, Any, List

# key: "{age}_{M|F}"
AGE_GENDER_STANDARDS = {
  "61_M": {
    "age": 61,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 61.3,
      "max": 79.5
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 8.6,
      "max": 19.8
    },
    "fat_free_mass": {
      "op": "range",
      "min": 53.0,
      "max": 60.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "61.3~79.5",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "8.6~19.8",
      "fat_free_mass": "53~60",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "61_F": {
    "age": 61,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "62_M": {
    "age": 62,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 60.6,
      "max": 78.5
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 8.5,
      "max": 19.5
    },
    "fat_free_mass": {
      "op": "range",
      "min": 52.0,
      "max": 59.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "60.6~78.5",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "8.5~19.5",
      "fat_free_mass": "52~59",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "62_F": {
    "age": 62,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "63_M": {
    "age": 63,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 59.9,
      "max": 77.6
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 8.4,
      "max": 19.3
    },
    "fat_free_mass": {
      "op": "range",
      "min": 52.0,
      "max": 58.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "59.9~77.6",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "8.4~19.3",
      "fat_free_mass": "52~58",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "63_F": {
    "age": 63,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "64_M": {
    "age": 64,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 59.1,
      "max": 76.6
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 8.3,
      "max": 19.1
    },
    "fat_free_mass": {
      "op": "range",
      "min": 51.0,
      "max": 57.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "59.1~76.6",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "8.3~19.1",
      "fat_free_mass": "51~57",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "64_F": {
    "age": 64,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "65_M": {
    "age": 65,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 58.4,
      "max": 75.7
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 8.2,
      "max": 18.8
    },
    "fat_free_mass": {
      "op": "range",
      "min": 50.0,
      "max": 57.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "58.4~75.7",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "8.2~18.8",
      "fat_free_mass": "50~57",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "65_F": {
    "age": 65,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "66_M": {
    "age": 66,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 57.7,
      "max": 74.7
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 8.1,
      "max": 18.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 50.0,
      "max": 56.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "57.7~74.7",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "8.1~18.6",
      "fat_free_mass": "50~56",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "66_F": {
    "age": 66,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "67_M": {
    "age": 67,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 57.0,
      "max": 73.7
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 8.0,
      "max": 18.4
    },
    "fat_free_mass": {
      "op": "range",
      "min": 49.0,
      "max": 55.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "57~73.7",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "8.0~18.4",
      "fat_free_mass": "49~55",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "67_F": {
    "age": 67,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "68_M": {
    "age": 68,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 56.3,
      "max": 72.8
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.9,
      "max": 18.1
    },
    "fat_free_mass": {
      "op": "range",
      "min": 48.0,
      "max": 55.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "56.3~72.8",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.9~18.1",
      "fat_free_mass": "48~55",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "68_F": {
    "age": 68,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "69_M": {
    "age": 69,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 55.5,
      "max": 71.8
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.8,
      "max": 17.9
    },
    "fat_free_mass": {
      "op": "range",
      "min": 48.0,
      "max": 54.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "55.5~71.8",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.8~17.9",
      "fat_free_mass": "48~54",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "69_F": {
    "age": 69,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "70_M": {
    "age": 70,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 54.8,
      "max": 70.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.7,
      "max": 17.7
    },
    "fat_free_mass": {
      "op": "range",
      "min": 47.0,
      "max": 53.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "54.8~70.9",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.7~17.7",
      "fat_free_mass": "47~53",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "70_F": {
    "age": 70,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "71_M": {
    "age": 71,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 54.1,
      "max": 69.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.6,
      "max": 17.4
    },
    "fat_free_mass": {
      "op": "range",
      "min": 46.0,
      "max": 53.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "54.1~69.9",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.6~17.4",
      "fat_free_mass": "46~53",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "71_F": {
    "age": 71,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "72_M": {
    "age": 72,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 53.7,
      "max": 69.4
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.5,
      "max": 17.3
    },
    "fat_free_mass": {
      "op": "range",
      "min": 46.0,
      "max": 52.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "53.7~69.4",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.5~17.3",
      "fat_free_mass": "46~52",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "72_F": {
    "age": 72,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "73_M": {
    "age": 73,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 53.3,
      "max": 68.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.5,
      "max": 17.2
    },
    "fat_free_mass": {
      "op": "range",
      "min": 46.0,
      "max": 52.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "53.3~68.9",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.5~17.2",
      "fat_free_mass": "46~52",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "73_F": {
    "age": 73,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "74_M": {
    "age": 74,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 53.0,
      "max": 68.5
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.4,
      "max": 17.1
    },
    "fat_free_mass": {
      "op": "range",
      "min": 46.0,
      "max": 51.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "53~68.5",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.4~17.1",
      "fat_free_mass": "46~51",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "74_F": {
    "age": 74,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "75_M": {
    "age": 75,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 52.6,
      "max": 68.0
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.4,
      "max": 16.9
    },
    "fat_free_mass": {
      "op": "range",
      "min": 45.0,
      "max": 51.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "52.6~68",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.4~16.9",
      "fat_free_mass": "45~51",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "75_F": {
    "age": 75,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 40.5,
      "max": 52.4
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.3,
      "max": 19.3
    },
    "fat_free_mass": {
      "op": "range",
      "min": 31.0,
      "max": 33.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "40.5~52.4",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "9.3~19.3",
      "fat_free_mass": "31~33",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "76_M": {
    "age": 76,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 52.2,
      "max": 67.5
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.3,
      "max": 16.8
    },
    "fat_free_mass": {
      "op": "range",
      "min": 45.0,
      "max": 51.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "52.2~67.5",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.3~16.8",
      "fat_free_mass": "45~51",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "76_F": {
    "age": 76,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 41.3,
      "max": 53.4
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.5,
      "max": 19.7
    },
    "fat_free_mass": {
      "op": "range",
      "min": 32.0,
      "max": 34.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "41.3~53.4",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "9.5~19.7",
      "fat_free_mass": "32~34",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "77_M": {
    "age": 77,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 52.0,
      "max": 67.2
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.3,
      "max": 16.7
    },
    "fat_free_mass": {
      "op": "range",
      "min": 45.0,
      "max": 50.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "52~67.2",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.3~16.7",
      "fat_free_mass": "45~50",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "77_F": {
    "age": 77,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 42.1,
      "max": 54.4
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.7,
      "max": 20.1
    },
    "fat_free_mass": {
      "op": "range",
      "min": 32.0,
      "max": 34.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "42.1~54.4",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "9.7~20.1",
      "fat_free_mass": "32~34",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "78_M": {
    "age": 78,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 51.7,
      "max": 66.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.2,
      "max": 16.7
    },
    "fat_free_mass": {
      "op": "range",
      "min": 44.0,
      "max": 50.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "51.7~66.9",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.2~16.7",
      "fat_free_mass": "44~50",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "78_F": {
    "age": 78,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 42.8,
      "max": 55.4
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.8,
      "max": 20.4
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "42.8~55.4",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "9.8~20.4",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "79_M": {
    "age": 79,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 51.5,
      "max": 66.5
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.2,
      "max": 16.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 44.0,
      "max": 50.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "51.5~66.5",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.2~16.6",
      "fat_free_mass": "44~50",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "79_F": {
    "age": 79,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.6,
      "max": 56.4
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.8
    },
    "fat_free_mass": {
      "op": "range",
      "min": 34.0,
      "max": 36.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "43.6~56.4",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.8",
      "fat_free_mass": "34~36",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "80_M": {
    "age": 80,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 51.2,
      "max": 66.2
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.2,
      "max": 16.5
    },
    "fat_free_mass": {
      "op": "range",
      "min": 44.0,
      "max": 50.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "51.2~66.2",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.2~16.5",
      "fat_free_mass": "44~50",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "80_F": {
    "age": 80,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 44.4,
      "max": 57.4
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.2,
      "max": 21.2
    },
    "fat_free_mass": {
      "op": "range",
      "min": 34.0,
      "max": 36.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "44.4~57.4",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.2~21.2",
      "fat_free_mass": "34~36",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "81_M": {
    "age": 81,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 51.0,
      "max": 65.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.1,
      "max": 16.4
    },
    "fat_free_mass": {
      "op": "range",
      "min": 44.0,
      "max": 50.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "51~65.9",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.1~16.4",
      "fat_free_mass": "44~50",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "81_F": {
    "age": 81,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.1,
      "max": 55.7
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.9,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "43.1~55.7",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "9.9~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "82_M": {
    "age": 82,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 49.2,
      "max": 63.5
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 6.9,
      "max": 15.8
    },
    "fat_free_mass": {
      "op": "range",
      "min": 42.0,
      "max": 48.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "49.2~63.5",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "6.9~15.8",
      "fat_free_mass": "42~48",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "82_F": {
    "age": 82,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 41.8,
      "max": 54.1
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.6,
      "max": 20.0
    },
    "fat_free_mass": {
      "op": "range",
      "min": 32.0,
      "max": 34.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "41.8~54.1",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "9.6~20.0",
      "fat_free_mass": "32~34",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "83_M": {
    "age": 83,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 42.7,
      "max": 55.2
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 6.0,
      "max": 13.7
    },
    "fat_free_mass": {
      "op": "range",
      "min": 37.0,
      "max": 42.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "42.7~55.2",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "6.0~13.7",
      "fat_free_mass": "37~42",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "83_F": {
    "age": 83,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 40.5,
      "max": 52.4
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.3,
      "max": 19.3
    },
    "fat_free_mass": {
      "op": "range",
      "min": 31.0,
      "max": 33.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "40.5~52.4",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "9.3~19.3",
      "fat_free_mass": "31~33",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "84_M": {
    "age": 84,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 43.0,
      "max": 55.6
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 6.0,
      "max": 13.8
    },
    "fat_free_mass": {
      "op": "range",
      "min": 37.0,
      "max": 42.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "43~55.6",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "6.0~13.8",
      "fat_free_mass": "37~42",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "84_F": {
    "age": 84,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 42.4,
      "max": 54.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.8,
      "max": 20.3
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "42.4~54.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "9.8~20.3",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "85_M": {
    "age": 85,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 6.1,
      "max": 13.9
    },
    "fat_free_mass": {
      "op": "range",
      "min": 37.0,
      "max": 42.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "6.1~13.9",
      "fat_free_mass": "37~42",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "85_F": {
    "age": 85,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 44.4,
      "max": 57.4
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.2,
      "max": 21.2
    },
    "fat_free_mass": {
      "op": "range",
      "min": 34.0,
      "max": 36.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "44.4~57.4",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.2~21.2",
      "fat_free_mass": "34~36",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "86_M": {
    "age": 86,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 48.6,
      "max": 62.7
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 6.8,
      "max": 15.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 42.0,
      "max": 47.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "48.6~62.7",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "6.8~15.6",
      "fat_free_mass": "42~47",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "86_F": {
    "age": 86,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 44.2,
      "max": 57.2
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.2,
      "max": 21.1
    },
    "fat_free_mass": {
      "op": "range",
      "min": 34.0,
      "max": 36.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "44.2~57.2",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.2~21.1",
      "fat_free_mass": "34~36",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "87_M": {
    "age": 87,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 6.1,
      "max": 13.9
    },
    "fat_free_mass": {
      "op": "range",
      "min": 37.0,
      "max": 42.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "6.1~13.9",
      "fat_free_mass": "37~42",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "87_F": {
    "age": 87,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 44.0,
      "max": 56.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.1,
      "max": 21.0
    },
    "fat_free_mass": {
      "op": "range",
      "min": 34.0,
      "max": 36.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "44~56.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.1~21.0",
      "fat_free_mass": "34~36",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "88_M": {
    "age": 88,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 47.4,
      "max": 61.2
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 6.6,
      "max": 15.2
    },
    "fat_free_mass": {
      "op": "range",
      "min": 41.0,
      "max": 46.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "47.4~61.2",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "6.6~15.2",
      "fat_free_mass": "41~46",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "88_F": {
    "age": 88,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.8,
      "max": 56.6
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.1,
      "max": 20.9
    },
    "fat_free_mass": {
      "op": "range",
      "min": 34.0,
      "max": 36.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "43.8~56.6",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.1~20.9",
      "fat_free_mass": "34~36",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "89_M": {
    "age": 89,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 51.5,
      "max": 66.5
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.2,
      "max": 16.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 44.0,
      "max": 50.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "51.5~66.5",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.2~16.6",
      "fat_free_mass": "44~50",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "89_F": {
    "age": 89,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.7,
      "max": 56.4
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.1,
      "max": 20.8
    },
    "fat_free_mass": {
      "op": "range",
      "min": 34.0,
      "max": 36.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 15.0
    },
    "labels": {
      "weight": "43.7~56.4",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.1~20.8",
      "fat_free_mass": "34~36",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<15"
    }
  },
  "90_M": {
    "age": 90,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 55.6,
      "max": 71.8
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 7.8,
      "max": 17.9
    },
    "fat_free_mass": {
      "op": "range",
      "min": 48.0,
      "max": 54.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "55.6~71.8",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "7.8~17.9",
      "fat_free_mass": "48~54",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "90_F": {
    "age": 90,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.5,
      "max": 56.2
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.7
    },
    "fat_free_mass": {
      "op": "range",
      "min": 34.0,
      "max": 36.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "43.5~56.2",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.7",
      "fat_free_mass": "34~36",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "91_M": {
    "age": 91,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 59.7,
      "max": 77.1
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 8.4,
      "max": 19.2
    },
    "fat_free_mass": {
      "op": "range",
      "min": 51.0,
      "max": 58.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "59.7~77.1",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "8.4~19.2",
      "fat_free_mass": "51~58",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "91_F": {
    "age": 91,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.3,
      "max": 55.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.0,
      "max": 20.6
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "43.3~55.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "10.0~20.6",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "92_M": {
    "age": 92,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 63.8,
      "max": 82.4
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 8.9,
      "max": 20.5
    },
    "fat_free_mass": {
      "op": "range",
      "min": 55.0,
      "max": 62.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "63.8~82.4",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "8.9~20.5",
      "fat_free_mass": "55~62",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "92_F": {
    "age": 92,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 43.0,
      "max": 55.6
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.9,
      "max": 20.5
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "43~55.6",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "9.9~20.5",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "93_M": {
    "age": 93,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 67.9,
      "max": 87.7
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.5,
      "max": 21.8
    },
    "fat_free_mass": {
      "op": "range",
      "min": 58.0,
      "max": 66.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "67.9~87.7",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "9.5~21.8",
      "fat_free_mass": "58~66",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "93_F": {
    "age": 93,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 42.7,
      "max": 55.2
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.8,
      "max": 20.4
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "42.7~55.2",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "9.8~20.4",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "94_M": {
    "age": 94,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 72.0,
      "max": 93.0
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.1,
      "max": 23.2
    },
    "fat_free_mass": {
      "op": "range",
      "min": 62.0,
      "max": 70.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "72~93",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "10.1~23.2",
      "fat_free_mass": "62~70",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "94_F": {
    "age": 94,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 42.4,
      "max": 54.9
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.8,
      "max": 20.3
    },
    "fat_free_mass": {
      "op": "range",
      "min": 33.0,
      "max": 35.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "42.4~54.9",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "9.8~20.3",
      "fat_free_mass": "33~35",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "95_M": {
    "age": 95,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 76.1,
      "max": 98.3
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 10.7,
      "max": 24.5
    },
    "fat_free_mass": {
      "op": "range",
      "min": 65.0,
      "max": 74.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "76.1~98.3",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "10.7~24.5",
      "fat_free_mass": "65~74",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "95_F": {
    "age": 95,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 42.1,
      "max": 54.5
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.7,
      "max": 20.1
    },
    "fat_free_mass": {
      "op": "range",
      "min": 32.0,
      "max": 34.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "42.1~54.5",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "9.7~20.1",
      "fat_free_mass": "32~34",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "96_M": {
    "age": 96,
    "gender": "M",
    "weight": {
      "op": "range",
      "min": 80.2,
      "max": 103.6
    },
    "body_fat_pct": {
      "op": "range",
      "min": 14.0,
      "max": 24.9
    },
    "fat_mass": {
      "op": "range",
      "min": 11.2,
      "max": 25.8
    },
    "fat_free_mass": {
      "op": "range",
      "min": 69.0,
      "max": 78.0
    },
    "smi": {
      "op": "gte",
      "value": 7.0
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 28.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "80.2~103.6",
      "body_fat_pct": "14%~24.9%",
      "fat_mass": "11.2~25.8",
      "fat_free_mass": "69~78",
      "smi": "≧7.0",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧28",
      "chair_stand": "<12",
      "walking": "<20"
    }
  },
  "96_F": {
    "age": 96,
    "gender": "F",
    "weight": {
      "op": "range",
      "min": 41.8,
      "max": 54.2
    },
    "body_fat_pct": {
      "op": "range",
      "min": 23.0,
      "max": 36.9
    },
    "fat_mass": {
      "op": "range",
      "min": 9.6,
      "max": 20.0
    },
    "fat_free_mass": {
      "op": "range",
      "min": 32.0,
      "max": 34.0
    },
    "smi": {
      "op": "gte",
      "value": 5.7
    },
    "bmi": {
      "op": "range",
      "min": 18.5,
      "max": 24.0,
      "label": "18.5≦BMI＜24"
    },
    "visceral_fat": {
      "op": "range",
      "min": 1.0,
      "max": 9.0
    },
    "systolic": {
      "op": "range",
      "min": 100.0,
      "max": 120.0
    },
    "diastolic": {
      "op": "range",
      "min": 60.0,
      "max": 80.0
    },
    "pulse": {
      "op": "range",
      "min": 60.0,
      "max": 100.0
    },
    "grip": {
      "op": "gte",
      "value": 18.0
    },
    "chair_stand": {
      "op": "lt",
      "value": 12.0
    },
    "walking": {
      "op": "lt",
      "value": 20.0
    },
    "labels": {
      "weight": "41.8~54.2",
      "body_fat_pct": "23%~36.9%",
      "fat_mass": "9.6~20.0",
      "fat_free_mass": "32~34",
      "smi": "≧5.7",
      "bmi": "18.5≦BMI＜24",
      "visceral_fat": "1~9",
      "systolic": "100-120",
      "diastolic": "60-80",
      "pulse": "60-100",
      "grip": "≧18",
      "chair_stand": "<12",
      "walking": "<20"
    }
  }
}


def _clamp_age(age: Optional[int]) -> Optional[int]:
    if age is None:
        return None
    try:
        a = int(age)
    except Exception:
        return None
    if a < 61:
        return 61
    if a > 96:
        return 96
    return a


def _gender_key(gender: Optional[str]) -> str:
    g = str(gender or "").upper()
    if g in ("M", "男"):
        return "M"
    return "F"


def get_standards(age: Optional[int], gender: Optional[str]) -> Optional[Dict[str, Any]]:
    """取得該年齡性別標準值；年齡超出 61-96 時取最接近邊界。"""
    a = _clamp_age(age)
    if a is None:
        return None
    key = f"{a}_{_gender_key(gender)}"
    return AGE_GENDER_STANDARDS.get(key)


def _check(value, rule: dict) -> Optional[bool]:
    if value is None or rule is None:
        return None
    try:
        v = float(value)
    except Exception:
        return None
    op = rule.get("op")
    if op == "gte":
        return v >= rule["value"]
    if op == "lte":
        return v <= rule["value"]
    if op == "lt":
        return v < rule["value"]
    if op == "gt":
        return v > rule["value"]
    if op == "range":
        return rule["min"] <= v <= rule["max"]
    return None


def compare_to_standards(
    age: Optional[int],
    gender: Optional[str],
    *,
    weight=None,
    body_fat=None,
    smi=None,
    bmi=None,
    systolic=None,
    diastolic=None,
    pulse=None,
    grip_strength=None,
    chair_stand_time=None,
    walking_time=None,
) -> Dict[str, Any]:
    """回傳各項與標準值對照結果。"""
    std = get_standards(age, gender)
    if not std:
        return {"available": False, "items": []}

    mapping = [
        ("體重 kg", weight, "weight"),
        ("體脂率 %", body_fat, "body_fat_pct"),
        ("SMI", smi, "smi"),
        ("BMI", bmi, "bmi"),
        ("收縮壓", systolic, "systolic"),
        ("舒張壓", diastolic, "diastolic"),
        ("脈搏", pulse, "pulse"),
        ("握力 kg", grip_strength, "grip"),
        ("五次坐站 秒", chair_stand_time, "chair_stand"),
        ("走路時間 秒", walking_time, "walking"),
    ]
    items = []
    for label, val, key in mapping:
        rule = std.get(key)
        labels = std.get("labels") or {}
        ok = _check(val, rule) if rule else None
        items.append({
            "label": label,
            "value": val,
            "standard": labels.get(key, ""),
            "pass": ok,
        })
    return {
        "available": True,
        "age": std["age"],
        "gender": std["gender"],
        "items": items,
    }


def walking_threshold(age: Optional[int], gender: Optional[str]) -> float:
    """依年齡性別回傳走路時間上限（秒），預設 20。"""
    std = get_standards(age, gender)
    if not std:
        return 20.0
    rule = std.get("walking") or {}
    if rule.get("op") == "lt":
        return float(rule["value"])
    return 20.0


def grip_threshold(gender: Optional[str]) -> float:
    g = _gender_key(gender)
    return 28.0 if g == "M" else 18.0
