# @jhCOR

from first_data_preprocessing import CONSTANT, CURRENT_DIR  # data_preprocessing 파일에서 CONSTANT라는 변수를 가져오는 코드입니다
import pandas as pd
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    data = pd.read_csv(CONSTANT['preprocessed_path'])
    
    plt.figure(figsize=(8, 5))
    plt.plot(data["Mileage"], data["Price"], marker='o', linestyle='-', color='blue', label="Mileage vs Price")
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price ($)")
    plt.title("Mileage vs Price")
    plt.legend()
    plt.grid(True)
    
    # 그래프 저장 경로 설정
    save_dir = os.path.join(CURRENT_DIR, "..", "Result/plot")
    save_path = os.path.join(save_dir, "mileage_vs_price.png")
    
    # 저장 폴더가 없으면 생성 (exist_ok=True 옵션 추가)
    os.makedirs(save_dir, exist_ok=True)
    plt.savefig(save_path)
    plt.show()
