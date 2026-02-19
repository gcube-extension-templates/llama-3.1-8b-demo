# 🦙 Llama 3.1 8B Instruct Demo

> 💡 **범용 대화 모델을 직접 구동해보고 싶은 분께 추천하는 프로젝트입니다.**  
> 복잡한 설정 없이 `git clone` 후 몇 가지 명령어만으로 **Open WebUI** 기반 ChatGPT 같은 웹 인터페이스로 대형 언어 모델(LLM)을 직접 구동해볼 수 있습니다.

---

## 📌 모델 소개

**Meta Llama 3.1 8B Instruct**는 Meta(구 Facebook)에서 2024년 7월 공개한 오픈소스 대형 언어 모델입니다.

### 역사와 배경
Meta는 2023년 Llama 1을 시작으로 오픈소스 LLM 생태계를 이끌어왔습니다. Llama 3.1은 그 세 번째 세대로, 405B(4050억) 파라미터 버전이 GPT-4o와 대등한 성능을 보이며 오픈소스 LLM의 새로운 기준을 세웠습니다. 특히 Llama 3.1 공개는 "오픈소스 AI가 상용 AI를 따라잡았다"는 평가를 받으며 업계에 큰 반향을 일으켰습니다.

### 장단점

| 장점 | 단점 |
|------|------|
| 다양한 용도에 범용적으로 활용 가능 | 추론 특화 모델 대비 수학·논리 문제 약함 |
| 한국어를 포함한 다국어 지원 | 8B 모델 특성상 복잡한 지시 이행 한계 |
| 오픈소스 생태계에서 가장 광범위한 지원 | 간혹 한국어/일본어 혼용 현상 발생 |
| Meta의 지속적인 업데이트 | |

### 동작 원리
Transformer 아키텍처 기반의 디코더 전용 모델로, 입력 텍스트를 토큰으로 변환한 후 다음 토큰을 순차적으로 예측하는 방식으로 텍스트를 생성합니다. Instruct 버전은 사전학습 후 RLHF(인간 피드백 강화학습)로 미세조정되어 지시 이행 능력이 강화되어 있습니다.

| 항목 | 내용 |
|------|------|
| 개발사 | Meta AI |
| 파라미터 수 | 8B (80억) |
| 라이선스 | Meta Llama 3 License |
| Ollama | [ollama.com/library/llama3.1](https://ollama.com/library/llama3.1) |

---

## ⚙️ 시스템 요구사항

| 항목 | 최소 사양 | 권장 사양 |
|------|-----------|-----------|
| GPU | NVIDIA RTX 4060 (8GB VRAM) | NVIDIA RTX 4080 / 4090 |
| GPU 아키텍처 | Ada Lovelace (RTX 40 시리즈) | Ada Lovelace (RTX 40 시리즈) |
| CUDA | 12.1 이상 | 12.4 이상 |
| RAM | 16GB | 32GB |
| 저장공간 | 10GB 이상 | 20GB 이상 |
| Python | 3.10 이상 | 3.11 |

> ✅ Ollama가 자동으로 최적 양자화 포맷(GGUF)을 선택하므로 RTX 40 시리즈 전 라인업(RTX 4060 8GB~)에서 실행 가능합니다.  
> ✅ HuggingFace 계정 및 토큰이 **필요하지 않습니다.**

---

## 🚀 빠른 시작

### 1. 저장소 클론

> ⚠️ 워크로드 배포 직후에는 git/curl이 아직 설치 중일 수 있습니다.  
> `git: command not found` 오류가 발생하면 잠시 후 다시 시도하거나 아래 명령어로 수동 설치하세요.
> ```bash
> apt-get update && apt-get install -y git curl
> ```

```bash
git clone https://github.com/gcube-extension-templates/llama-3.1-8b-demo.git
cd llama-3.1-8b-demo
```

### 2. Setup 실행 (Ollama + Open WebUI 설치 + 모델 다운로드)

```bash
bash setup.sh
```

> ⏳ Ollama, Open WebUI 설치 및 모델 다운로드가 자동으로 진행됩니다.

### 3. 서비스 시작

```bash
bash start.sh
```

> 터미널에 **"Open WebUI 준비 완료!"** 메시지가 출력된 후 브라우저에서 접속하세요.

### 4. 브라우저에서 접속

GCUBE 워크로드의 **서비스 URL (포트 8080)** 으로 접속하면 채팅 인터페이스가 열립니다.

---

## 📁 프로젝트 구조

```
llama-3.1-8b-demo/
├── README.md        # 프로젝트 설명 (현재 파일)
├── setup.sh         # Ollama + Open WebUI 설치 + 모델 다운로드
└── start.sh         # 서비스 시작 스크립트
```

---

## ❓ 자주 묻는 질문

**Q. 처음 실행 시 시간이 오래 걸려요.**  
A. setup.sh 실행 중 Ollama, Open WebUI 설치 및 모델 다운로드가 진행됩니다. 인터넷 속도에 따라 수~수십 분이 소요될 수 있으며, 다음 실행부터는 `bash start.sh`만 실행하면 됩니다.

**Q. HuggingFace 토큰이 필요한가요?**  
A. 필요하지 않습니다. Ollama 레지스트리에서 직접 다운로드하므로 별도 인증이 없어도 됩니다.

**Q. 브라우저에서 접속이 안 돼요.**  
A. `bash start.sh` 실행 후 터미널에 "Open WebUI 준비 완료!" 메시지가 출력됐는지 확인해주세요. GCUBE 워크로드 설정에서 포트 8080이 열려 있는지도 확인하세요.

---

## 📜 라이선스

이 프로젝트의 코드는 MIT License를 따릅니다.  
모델 가중치는 [Meta Llama 3 License](https://llama.meta.com/llama3/license/)를 따릅니다.