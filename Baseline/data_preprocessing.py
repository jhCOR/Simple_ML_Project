# JiHyeok Jung
# 저는 python파일로 작성했지만 아래의 코드를 가져다가 주피터 노트북에서 써도 됩니다. 

import pandas as pd
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(CURRENT_DIR, "..", "Data", "train.csv")
save_path = os.path.join(CURRENT_DIR, "..", "Result", "preprocessed_train.csv")

CONSTANT = {
    "file_path": file_path,
}


if __name__ == "__main__":

    print("데이터 로드")
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        print("🚨 파일을 찾을 수 없습니다. 파일 경로를 확인하세요!")

    print("데이터 시각화 시작")
    df = pd.read_csv(CONSTANT['file_path'])
    print(df.head())

    print("데이터 전처리 시작")
    df["Mileage"] = df["Mileage"].str.replace(" km", "", regex=True).astype(int)
    print(df.head())

    df.to_csv(save_path)