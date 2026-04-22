# 🎯 나만의 Python 퀴즈 게임

터미널(콘솔) 환경에서 실행되는 객체지향 기반의 파이썬 퀴즈 게임 프로젝트입니다.

---

## 1. 프로젝트 개요
사용자가 직접 문제를 풀고, 새로운 퀴즈를 등록하며 최고 점수를 관리할 수 있는 콘솔 기반 애플리케이션입니다.

## 2. 퀴즈 주제 선정 이유
파이썬의 기초 문법인 리스트, 클래스, 예외 처리, 파일 입출력이 실제 프로그램에서 어떻게 유기적으로 작동하는지 이해하고, 데이터의 영속성(저장 및 불러오기)을 직접 구현해보기 위해 선정했습니다.

## 3. 실행 방법
파이썬이 설치된 환경의 터미널에서 프로젝트 폴더로 이동한 뒤 아래 명령어를 입력합니다.

```bash
python main.py
```

## 4. 기능 목록
* **퀴즈 풀기**: 등록된 퀴즈를 무작위 순서로 풀고 실시간으로 정답 여부를 확인합니다.
* **퀴즈 추가**: 문제, 4개의 선택지, 정답 번호를 입력하여 새로운 문제를 시스템에 등록합니다.
* **퀴즈 목록**: 현재 저장된 모든 퀴즈의 질문 리스트를 확인합니다.
* **점수 확인**: 역대 최고 기록(정답 수, 총 문제 수, 정답률)을 확인합니다.

## 5. 파일 구조
```text
.
├── main.py          # 프로그램의 진입점 (게임 실행)
├── game.py          # 전체 게임 로직, 메뉴 시스템, 파일 저장/로드 제어
├── quiz.py          # 퀴즈 객체 구조(Class) 및 데이터 변환 정의
├── state.json       # 데이터 저장소 (퀴즈 목록 및 최고 점수 보관)
├── .gitignore       # Git 관리 제외 파일 설정
└── README.md        # 프로젝트 설명 문서
```

## 6. 데이터 파일 설명 (`state.json`)
본 프로젝트는 프로그램 종료 후에도 데이터가 유지되도록 `state.json` 파일을 활용합니다.

* **경로**: 프로젝트 루트 디렉토리 (`./state.json`)
* **역할**: 퀴즈 리스트와 최고 점수 기록을 JSON 포맷으로 영구 저장합니다.
* **필드 구조**:
    * `quizzes`: 각 퀴즈의 정보(`question`, `choices`, `answer`)를 담은 리스트입니다.
    * `best_score`: 최고 기록 정보(`correct`, `total`, `percent`)를 담은 객체입니다.

---

**💡 Tip**: `state.json` 파일이 없더라도 실행 시 자동으로 기본 10문제가 생성되어 안전하게 시작할 수 있습니다.

<img width="689" height="452" alt="quiz start" src="https://github.com/user-attachments/assets/23498506-a4ce-4ab3-932c-452bd2dd2003" />
<img width="1056" height="393" alt="quiz add" src="https://github.com/user-attachments/assets/368aba20-ad0a-4df3-82ce-252b10c86c3a" />
<img width="944" height="423" alt="quiz list" src="https://github.com/user-attachments/assets/3c1e5937-aa71-4cfe-9379-8d4d7a48b074" />
<img width="474" height="248" alt="score check" src="https://github.com/user-attachments/assets/06413748-8057-4580-9382-bb42f5c4a287" />
