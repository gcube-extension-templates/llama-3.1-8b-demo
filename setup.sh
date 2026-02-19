#!/bin/bash
# ==============================================
#  Llama 3.1 8B Instruct — Setup Script
#  실행: bash setup.sh
# ==============================================

set -e  # 오류 발생 시 즉시 중단

echo "======================================"
echo "  🦙 Llama 3.1 8B Instruct Setup"
echo "======================================"

# ----------------------------------------------
# 1. 패키지 설치
# ----------------------------------------------
echo ""
echo "[1/3] 패키지 설치 중..."
pip install -r requirements.txt --quiet
echo "✅ 패키지 설치 완료"

# ----------------------------------------------
# 2. Hugging Face 인증
# ----------------------------------------------
echo ""
echo "[2/3] Hugging Face 인증 확인 중..."

attempt_login() {
    local token="$1"
    huggingface-cli login --token "$token" 2>&1
}

check_model_access() {
    python -c "
from huggingface_hub import HfApi
api = HfApi()
try:
    api.model_info('meta-llama/Meta-Llama-3.1-8B-Instruct')
    print('ok')
except Exception as e:
    if 'GatedRepoError' in str(type(e)) or '403' in str(e):
        print('gated')
    else:
        print('error')
" 2>/dev/null
}

# 토큰이 없으면 터미널에서 입력받기
if [ -z "$HF_TOKEN" ]; then
    echo "⚠️  HF_TOKEN 환경변수가 설정되어 있지 않습니다."
    echo ""
    read -s -p "   Hugging Face 토큰을 직접 입력해주세요 (입력 내용은 보이지 않습니다): " HF_TOKEN
    echo ""
fi

# 토큰으로 로그인 시도
echo "   토큰 검증 중..."
LOGIN_RESULT=$(attempt_login "$HF_TOKEN")

if echo "$LOGIN_RESULT" | grep -q "Login successful\|Token is valid"; then
    echo "✅ Hugging Face 인증 완료"

    # 모델 접근 권한 확인
    ACCESS=$(check_model_access)
    if [ "$ACCESS" = "gated" ]; then
        echo ""
        echo "❌ 모델 접근 권한이 없습니다."
        echo ""
        echo "   아래 URL에서 Meta 라이선스에 동의 후 다시 실행해주세요:"
        echo "   https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct"
        echo ""
        echo "   ※ 동의 후 보통 수 분 내로 승인됩니다."
        exit 1
    fi
else
    echo ""
    echo "❌ 토큰 인증에 실패했습니다."
    echo "   - HuggingFace 계정의 유효한 토큰인지 확인해주세요"
    echo "   - https://huggingface.co/settings/tokens 에서 토큰을 확인할 수 있습니다"
    exit 1
fi

# ----------------------------------------------
# 3. 모델 다운로드
# ----------------------------------------------
echo ""
echo "[3/3] 모델 다운로드 중... (약 16GB, 시간이 소요됩니다)"

MODEL_DIR="/workspace/models/llama-3.1-8b-instruct"
mkdir -p "$MODEL_DIR"

huggingface-cli download meta-llama/Meta-Llama-3.1-8B-Instruct \
    --local-dir "$MODEL_DIR" \
    --exclude "original/*"

echo "✅ 모델 다운로드 완료: $MODEL_DIR"

# ----------------------------------------------
# 완료
# ----------------------------------------------
echo ""
echo "======================================"
echo "  ✅ Setup 완료!"
echo "  이제 아래 명령어로 실행하세요:"
echo ""
echo "  python run.py"
echo "======================================"