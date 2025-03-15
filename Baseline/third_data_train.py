# @jhCOR

from first_data_preprocessing import CONSTANT # data_preprocessing파일에서 CONSTANT라는 변수를 가져오는 코드입니다
import pandas as pd
import os

if __name__ == "__main__":
    print("데이터 로드")
    if os.path.exists(CONSTANT['preprocessed_path']):
        df = pd.read_csv(CONSTANT['preprocessed_path'])
    else:
        print("🚨 파일을 찾을 수 없습니다. 파일 경로를 확인하세요!")

    