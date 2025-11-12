#지금처럼 여러 라이브러리를 설치·업데이트하면서 충돌 가능성이 있을 때,
#한 번 환경 전체 캐시 정리(clean-up) 를 해두면 정말 좋아요.

#아래는 pip, conda, VSCode, Python, 터미널 전체 정리 루틴입니다.
#순서대로 따라 하시면 됩니다 👇

#🧹 ① pip 캐시 정리
pip cache purge


#PyPI에서 받은 wheel 파일(.whl)과 빌드 캐시를 전부 삭제합니다.

#~/.cache/pip/ 내부가 비워집니다.

# ② conda 캐시 정리
conda clean --all --yes


#이 명령은 다음을 모두 삭제합니다:

#패키지 tarballs / 압축 해제된 패키지 캐시 / 패키지 인덱스 캐시 / 오래된 환경 빌드 캐시

# ⚠️ 처음 재설치할 때 다운로드 시간이 조금 늘어납니다 (정상입니다).
# ③ Python 자체 캐시(pycache) 정리

# 프로젝트 루트에서 실행하세요 👇

find . -type d -name "__pycache__" -exec rm -rf {} +


# .pyc 바이트코드 캐시를 모두 지워 새로 컴파일하도록 합니다.

# ④ VS Code Python 환경 캐시 정리

# VSCode 메뉴 → 명령 팔레트(Ctrl+Shift+P)
# 입력: Python: Clear Cache and Reload Window
# 선택 후 VSCode 재시작

#  또는 수동으로:

rm -rf ~/.config/Code/User/workspaceStorage
rm -rf ~/.vscode-server/data/User/workspaceStorage

# ⑤ 터미널 세션 / 환경 변수 초기화
hash -r
source ~/.bashrc


#  또는 zsh 사용 시:

source ~/.zshrc


이 명령은 PATH, alias, env 변수를 새로 읽어옵니다.
