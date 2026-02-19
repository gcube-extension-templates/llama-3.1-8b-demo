# 🦙 Llama 3.1 8B Instruct — Text Generation Demo

> 💡 **AI를 처음 접하는 분께 추천하는 프로젝트입니다.**  
> 복잡한 설정 없이 `git clone` 후 몇 가지 명령어만으로 대형 언어 모델(LLM)을 직접 구동해볼 수 있습니다.

---

## 📌 모델 소개

**Meta Llama 3.1 8B Instruct**는 Meta(구 Facebook)에서 공개한 오픈소스 대형 언어 모델입니다.  
8B(80억)개의 파라미터를 가진 모델로, 질문에 답하고 텍스트를 생성하는 데 뛰어난 성능을 보여줍니다.  
오픈소스 LLM 생태계에서 가장 보편적인 **테스트 기준 모델**로 널리 사용되고 있습니다.

| 항목 | 내용 |
|------|------|
| 개발사 | Meta AI |
| 파라미터 수 | 8B (80억) |
| 라이선스 | Meta Llama 3 License |
| Hugging Face | [meta-llama/Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) |

---

## ⚙️ 시스템 요구사항

| 항목 | 최소 사양 | 권장 사양 |
|------|-----------|-----------|
| GPU | NVIDIA RTX 4060 (8GB VRAM) | NVIDIA RTX 4080 / 4090 |
| GPU 아키텍처 | Ada Lovelace (RTX 40 시리즈) | Ada Lovelace (RTX 40 시리즈) |
| CUDA | 12.1 이상 | 12.4 이상 |
| RAM | 16GB | 32GB |
| 저장공간 | 20GB (모델 다운로드 포함) | 30GB 이상 |
| Python | 3.10 이상 | 3.11 |

> ✅ 기본값 4-bit 양자화로 RTX 40 시리즈 전 라인업(RTX 4060 8GB~)에서 실행 가능합니다.  
> VRAM 16GB 이상 환경에서는 `run.py`의 `USE_4BIT = False`로 변경 시 더 높은 품질로 실행할 수 있습니다.

> ⚠️ Hugging Face에서 모델을 다운로드하려면 **Hugging Face 계정 및 모델 사용 동의**가 필요합니다.  
> [여기](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)에서 동의 후 진행해주세요.

---

## 🚀 빠른 시작

### 1. 저장소 클론

```bash
git clone https://github.com/your-org/llama-3.1-8b-demo.git
cd llama-3.1-8b-demo
```

### 2. 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. Setup 실행 (패키지 설치 + 모델 다운로드 한번에)

```bash
bash setup.sh
```

> ⚠️ Llama 모델은 Hugging Face 인증이 필요합니다.  
> 워크로드 환경변수에 `HF_TOKEN`을 설정하거나, setup.sh 실행 중 안내에 따라 직접 로그인해주세요.  
> Token 발급: https://huggingface.co/settings/tokens

### 4. 모델 실행

```bash
python run.py
```

### 5. 실행 결과 예시

```
==============================================
  🦙 Llama 3.1 8B Instruct — Demo
==============================================
모델 로딩 중... (처음 실행 시 다운로드가 진행됩니다)
✅ 모델 로딩 완료!

[질문] 인공지능이란 무엇인가요? 쉽게 설명해 주세요.

[답변]
인공지능(AI)이란, 컴퓨터가 인간처럼 생각하고 학습하며 문제를 해결할 수 있도록
만든 기술입니다. 예를 들어, 사진 속 고양이를 인식하거나, 번역을 하거나,
여러분과 대화를 나누는 것이 모두 인공지능의 예시입니다...
==============================================
```

---

## 📁 프로젝트 구조

```
llama-3.1-8b-demo/
├── README.md          # 프로젝트 설명 (현재 파일)
├── requirements.txt   # 필요한 Python 패키지 목록
├── setup.sh           # 패키지 설치 + 모델 다운로드 자동화 스크립트
└── run.py             # 모델 실행 스크립트
```

---

## ❓ 자주 묻는 질문

**Q. 처음 실행 시 시간이 오래 걸려요.**  
A. 처음 실행 시 약 16GB의 모델 파일을 Hugging Face에서 다운로드합니다. 인터넷 속도에 따라 수~수십 분이 소요될 수 있으며, 다음 실행부터는 캐시에서 바로 로드됩니다.

**Q. CUDA out of memory 오류가 발생해요.**  
A. `run.py` 내 `load_in_4bit=True` 옵션을 활성화하면 VRAM 사용량을 줄일 수 있습니다. 코드 주석을 참고해주세요.

**Q. 질문을 바꾸고 싶어요.**  
A. `run.py` 파일 하단의 `USER_PROMPT` 변수를 원하는 내용으로 수정 후 다시 실행하세요.

---

## 📜 라이선스

이 프로젝트의 코드는 MIT License를 따릅니다.  
모델 가중치는 [Meta Llama 3 License](https://llama.meta.com/llama3/license/)를 따릅니다.