#!/bin/bash
# @jhCOR
# 이 피일은 
# bash automatic_experiment_setup.bash 
# 명령어로 실행하면 됩니다. 

# 현재 실행 중인 OS 확인
OS_TYPE=$(uname)

# 가상환경 생성
python -m venv .venv

# OS에 따라 가상환경 활성화
if [[ "$OS_TYPE" == "Linux" || "$OS_TYPE" == "Darwin" ]]; then
    source .venv/bin/activate
elif [[ "$OS_TYPE" == "CYGWIN"* || "$OS_TYPE" == "MINGW"* || "$OS_TYPE" == "MSYS"* ]]; then
    .venv\Scripts\activate
else
    echo "Unsupported OS: $OS_TYPE"
    exit 1
fi

# 패키지 설치
pip install -r requirements.txt

echo "Virtual environment setup complete!"
