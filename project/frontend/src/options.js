// 데이터(CO2 Emissions_Canada.csv, 7,385행)에서 뽑은 입력 선택지. 학습에 쓴 값과 동일해야 합니다.
export const OPTIONS = {
  "make": [
    "ACURA",
    "ALFA ROMEO",
    "ASTON MARTIN",
    "AUDI",
    "BENTLEY",
    "BMW",
    "BUGATTI",
    "BUICK",
    "CADILLAC",
    "CHEVROLET",
    "CHRYSLER",
    "DODGE",
    "FIAT",
    "FORD",
    "GENESIS",
    "GMC",
    "HONDA",
    "HYUNDAI",
    "INFINITI",
    "JAGUAR",
    "JEEP",
    "KIA",
    "LAMBORGHINI",
    "LAND ROVER",
    "LEXUS",
    "LINCOLN",
    "MASERATI",
    "MAZDA",
    "MERCEDES-BENZ",
    "MINI",
    "MITSUBISHI",
    "NISSAN",
    "PORSCHE",
    "RAM",
    "ROLLS-ROYCE",
    "SCION",
    "SMART",
    "SRT",
    "SUBARU",
    "TOYOTA",
    "VOLKSWAGEN",
    "VOLVO"
  ],
  "vehicle_class": [
    "COMPACT",
    "FULL-SIZE",
    "MID-SIZE",
    "MINICOMPACT",
    "MINIVAN",
    "PICKUP TRUCK - SMALL",
    "PICKUP TRUCK - STANDARD",
    "SPECIAL PURPOSE VEHICLE",
    "STATION WAGON - MID-SIZE",
    "STATION WAGON - SMALL",
    "SUBCOMPACT",
    "SUV - SMALL",
    "SUV - STANDARD",
    "TWO-SEATER",
    "VAN - CARGO",
    "VAN - PASSENGER"
  ],
  "transmission": [
    "A10",
    "A4",
    "A5",
    "A6",
    "A7",
    "A8",
    "A9",
    "AM5",
    "AM6",
    "AM7",
    "AM8",
    "AM9",
    "AS10",
    "AS4",
    "AS5",
    "AS6",
    "AS7",
    "AS8",
    "AS9",
    "AV",
    "AV10",
    "AV6",
    "AV7",
    "AV8",
    "M5",
    "M6",
    "M7"
  ],
  "fuel_type": [
    "D",
    "E",
    "N",
    "X",
    "Z"
  ],
  "engine_size": [
    0.9,
    8.4
  ],
  "cylinders": [
    3,
    4,
    5,
    6,
    8,
    10,
    12,
    16
  ]
};

export const CO2_STATS = {"min": 96, "max": 522, "mean": 250.6};  // g/km, 데이터 전체 기준


const BRAND_KO = {
  HYUNDAI: '현대', KIA: '기아', GENESIS: '제네시스', TOYOTA: '토요타', HONDA: '혼다',
  NISSAN: '닛산', MAZDA: '마쓰다', SUBARU: '스바루', LEXUS: '렉서스', BMW: 'BMW',
  'MERCEDES-BENZ': '벤츠', AUDI: '아우디', VOLKSWAGEN: '폭스바겐', VOLVO: '볼보',
  FORD: '포드', CHEVROLET: '쉐보레', JEEP: '지프', PORSCHE: '포르쉐', MINI: '미니',
};

const CLASS_KO = {
  'COMPACT': '준중형', 'FULL-SIZE': '대형', 'MID-SIZE': '중형', 'MINICOMPACT': '초소형',
  'MINIVAN': '미니밴', 'PICKUP TRUCK - SMALL': '소형 픽업', 'PICKUP TRUCK - STANDARD': '표준 픽업',
  'SPECIAL PURPOSE VEHICLE': '특수 목적', 'STATION WAGON - MID-SIZE': '중형 왜건',
  'STATION WAGON - SMALL': '소형 왜건', 'SUBCOMPACT': '소형', 'SUV - SMALL': '소형 SUV',
  'SUV - STANDARD': '표준 SUV', 'TWO-SEATER': '2인승', 'VAN - CARGO': '화물 밴',
  'VAN - PASSENGER': '승합 밴',
};

const FUEL_KO = { X: '일반 휘발유', Z: '프리미엄 휘발유', D: '디젤', E: '에탄올(E85)', N: '천연가스' };

const TRANS_KO = { A: '자동', AM: '자동화 수동', AS: '자동(수동 모드)', AV: '무단변속(CVT)', M: '수동' };

export const brandLabel = (v) => (BRAND_KO[v] ? `${BRAND_KO[v]} (${v})` : v);
export const classLabel = (v) => (CLASS_KO[v] ? `${CLASS_KO[v]} · ${v}` : v);
export const fuelLabel = (v) => (FUEL_KO[v] ? `${FUEL_KO[v]} (${v})` : v);
export const transLabel = (v) => {
  const m = /^([A-Z]+)(\d+)?$/.exec(v);
  if (!m) return v;
  const kind = TRANS_KO[m[1]] ?? m[1];
  return m[2] ? `${v} · ${kind} ${m[2]}단` : `${v} · ${kind}`;
};
