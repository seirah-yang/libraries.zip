# 1️. 환경 정리
conda activate <나의환경0>
pip uninstall torch torchvision torchaudio transformers accelerate -y
pip cache purge

# !! 이 단계에서 반드시 torch 관련 잔여물 다 제거되어야 한다. 

# 2️. PyTorch 재설치 (GPU or CPU 중 선택)
# (A) GPU 버전 (CUDA 12.x 지원)
pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu121
                              # 버전 변경되었는지, 호환성 고려해서 설치해야 함 
# (B) CPU 전용 버전
pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cpu
                              # 버전 변경되었는지, 호환성 고려해서 설치 해야 함

# !! (A) 또는 (B) 중 하나만 선택 : (CUDA가 설치되지 않은 머신이면 CPU 버전만 가능)

# 3. Hugging Face 관련 패키지 재설치
pip install --upgrade pip
pip install "transformers[torch]" accelerate

# 4. 설치 확인
python -c "import torch, torchvision; from transformers import Trainer; print('completed install')
