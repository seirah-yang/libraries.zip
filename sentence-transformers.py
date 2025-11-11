# sentence-transformers 설치:
# 환경이 활성화된 상태에서 다음 명령 중 하나를 사용하여 패키지 설치

# 1. Conda를 사용한 설치 (권장): conda-forge 채널을 통해 설치하는 것이 가장 안정적
conda install -c conda-forge sentence-transformers

# 2. Pip을 사용한 설치: Conda로 설치가 어려운 경우 Pip 사용 가능 
pip install -U sentence-transformers

# 3. 설치 확인 : 설치가 완료되면 Python 인터프리터에서 모듈을 성공적으로 가져올 수 있는지 테스트
python -c "from sentence_transformers import SentenceTransformer; print('Success')"

# 4. PyTorch 설치 확인 (필요시)
# sentence-transformers는 PyTorch 또는 TensorFlow를 기반으로 작동하므로, 이들 중 하나가 설치되어 있어야 함
# 일반적으로 위 설치 과정에서 함께 설치되지만, 특정 버전이 필요하거나 GPU 지원이 필요한 경우 별도로 설치
conda install pytorch torchvision torchaudio -c pytorch
  # 또는 GPU 사용 시 (시스템에 맞는 CUDA 버전 확인 필요)
  # pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
