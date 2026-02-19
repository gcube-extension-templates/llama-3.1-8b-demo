"""
Llama 3.1 8B Instruct — Text Generation Demo
=============================================
Meta의 Llama 3.1 8B Instruct 모델을 사용한 텍스트 생성 데모입니다.
AI를 처음 접하는 분도 쉽게 실행해볼 수 있도록 구성되어 있습니다.
"""

import torch
import transformers

# =============================================
# 설정 (원하는 대로 수정 가능)
# =============================================

# 모델 경로 (setup.sh 실행 후 로컬 경로 사용)
# setup.sh를 실행하지 않은 경우 Hugging Face Hub에서 자동 다운로드
MODEL_ID = "/workspace/models/llama-3.1-8b-instruct"
FALLBACK_MODEL_ID = "meta-llama/Meta-Llama-3.1-8B-Instruct"

# 여기에 원하는 질문을 입력하세요!
USER_PROMPT = "인공지능이란 무엇인가요? 쉽게 설명해 주세요."

# 생성할 최대 토큰 수 (길이 조절)
MAX_NEW_TOKENS = 512

# 4-bit 양자화 사용 여부 (VRAM 8GB 환경에서 True로 설정)
USE_4BIT = False

# =============================================


def load_model(model_id: str, use_4bit: bool):
    """모델과 토크나이저를 로드합니다."""
    import os
    # 로컬 경로에 모델이 없으면 Hugging Face Hub에서 다운로드
    if not os.path.exists(model_id):
        print(f"⚠️  로컬 모델 경로({model_id})를 찾을 수 없습니다.")
        print(f"   Hugging Face Hub에서 다운로드합니다: {FALLBACK_MODEL_ID}")
        model_id = FALLBACK_MODEL_ID
    print(f"모델 로딩 중... ({model_id})")

    model_kwargs = {
        "torch_dtype": torch.bfloat16,
        "device_map": "auto",
    }

    # 4-bit 양자화 설정 (VRAM 부족 시 활성화)
    if use_4bit:
        from transformers import BitsAndBytesConfig
        model_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
        )
        print("  ℹ️  4-bit 양자화 모드로 실행합니다 (VRAM 절약)")

    pipeline = transformers.pipeline(
        "text-generation",
        model=model_id,
        model_kwargs=model_kwargs,
    )

    print("✅ 모델 로딩 완료!\n")
    return pipeline


def generate_response(pipeline, user_prompt: str, max_new_tokens: int) -> str:
    """모델에 질문을 전달하고 응답을 생성합니다."""
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Please respond in Korean.",
        },
        {
            "role": "user",
            "content": user_prompt,
        },
    ]

    outputs = pipeline(
        messages,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
    )

    # 마지막 메시지(assistant의 응답) 추출
    response = outputs[0]["generated_text"][-1]["content"]
    return response


def main():
    print("=" * 50)
    print("  🦙 Llama 3.1 8B Instruct — Demo")
    print("=" * 50)

    # GPU 상태 확인
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
        vram = torch.cuda.get_device_properties(0).total_memory / 1024**3
        print(f"🖥️  GPU: {gpu_name} ({vram:.1f}GB VRAM)")
    else:
        print("⚠️  GPU를 찾을 수 없습니다. CPU로 실행합니다 (매우 느릴 수 있음)")

    print()

    # 모델 로드
    pipeline = load_model(MODEL_ID, USE_4BIT)

    # 응답 생성
    print(f"[질문] {USER_PROMPT}\n")
    print("[답변]")
    print("-" * 50)

    response = generate_response(pipeline, USER_PROMPT, MAX_NEW_TOKENS)
    print(response)

    print("-" * 50)
    print("\n✅ 완료! run.py의 USER_PROMPT를 수정해서 다른 질문을 해보세요.")


if __name__ == "__main__":
    main()