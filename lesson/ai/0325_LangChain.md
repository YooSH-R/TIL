# Post-training(Instruction-tuning, RLHF)
## 0. 학습 시작
- 거대 언어모델의 학습 패러다임이 어떻게 되는가?
  - pre-training(사전 학습)과 post-training(사후 학습)의 개념과 차이
- 언어모델이 어떻게 사용자의 질문에 응답을 할 수 있게 되었는가?
  - Instruction-tuning에 대한 개념 이해
- 언어모델이 어떻게 사용자가 선호하는 답변을 내도록 학습이 되었는가
  - Instruction-tuning의 한계와 RLHF의 개념에 대한 이해
- RLHF 이후에 post-training 접근들은 어떤 게 있는가
  -  RLHF의 한계점과 이후 접근들에 대한 소개(DPO, RLVR)
<br>
<br>

## 1. Pre-training vs Post-training
- 거대 언어 모델 학습 두 가지 단계
  - Pre-training: 방대한 텍스트 데이터를 통해 언어와 지식 배우는 단계
    - 방대한 텍스트 데이터를 이용한 Self-supervised learning을 통해 언어 패턴, 지식 등을 배움
    - 학습 목표: 다음 단어 예측 (Next Token Prediction)
  - Post-training: 사람이 원하는 방식으로 대화하고, 안전하고, 유용하게 만드는 단계
    - 유저의 의도를 파악하고 원하는 답변을 모델이 응답하도록 사후 학습 진행
    - Instruction-tuning, RLHF, DPO, RLVR
<br>
<br>

## 2. Instruction-tuning
- 사전 학습 후에도 유저의 의도와 일치하지 않는 LLM의 문제를 해결하기 위해 진행한 파인 튜닝
- 언어모델이 사람이 내린 지시문(instruction)을 따르도록 학습하는 단계
- 정답 레이블이 요구되며, 다양한 테스크를 풀 수 있도록 적응하는 것에 중점을 둠
<br>
<br>

## 3. Reinforcement Learning from Human Feedback(RLHF)
- Instruction-tuning의 한계
  - 정답 데이터 수집하는 것이 비쌈
  - 개방형/창의적 생성과 같은 태스크는 정답 존재하지 않음
  - 언어 모델링은 모든 토큰 레벨의 오류를 동일하게 취급하지만, 어떤 오류는 다른 오류보다 크게 작용
  - 사람이 만든 답변(정답 레이블)이 최적이 아닐 수 있음

- 인간의 선호를 반영한 최적화(Optimizing for human preferences)
  - 언어모델의 응답 중 기대 인간이 준 보상을 최대화 하는 것을 목표로 한다.
  - 강화학습(Reinforcement Learning, RL) 이용해서 최적화
<br>
<br>

## 4. What's Next?
- 리워드 모델링의 한계
  - 인간의 선호도는 일관성이 부족

- Direct Preference Potimization(DPO): RLHF에서 RL을 제거
- Reinforcement Learning with Verifiable Reward(RLVR): RLHF에서 수학 문제와 같이 답이 분명한 문제들은 정답 여부로 리워드를 줌
<br>
<br>

# Retrieval-augmented Language Models(Information Retrieval, RAG)
## 0. 학습 시작
- 검색증강 언어모델이 무엇일까?
  - 검색증강 언어모델에서 사용되는 용어들에 대한 이해
- 정보 검색이 무엇일까?
  - 정보 검색의 활용에 대한 이해와 검색기(Retriever) 이해
- 검색증간 언어모델은 언제 사용해야 할까?
  - 검색증강 언에모델이 필요한 이유와 도전과제들 이해
<br>
<br>

## 1. Basic Concepts of Retrieval-augmented LM(검색증강 언어모델)
- 추론 시 외부 데이터 저장소를 불러와 활용하는 언어모델
- 구성요소: Datastore, Query, Index, Lanugage Model
- Retrieval-augmented Generation(RAG)
  - 사용자의 질문에 답하기 위해, datastore에서 관련 정보를 검색해와서, 이를 언어모델이 생성단계에 함께 활용하는 방법
<br>
<br>

## 2. Information Retrieval(정보 검색)
- IR: 사용자의 질의(Query)에 맞는 정보를 대규모 데이터에서 찾아 제공하는 과정
- 목표: 검색 질의와 가장 관련성 높은 정보 제공

- Retriver란?
  - 사용자의 질의에 맞는 후보 문서를 저장소에서 찾아오는 모듈
  - RAG에서 첫 단계 역할을 수행
  - Sparse Retriever(어휘적 유사도 기반)
    - 전통적 IR 기법, 쿼리와 문서 간 정확한 용어 일치에 기반
    - TF-IDF(Term Frequency-Inverse Document Frequency): 문서 내 특정 단어의 중요도를 나타내는 가중치 방식
    - 장점
      - Simplicity: 구현과 이해 쉬움
      - Efficiency: Inverted index 구조 덕분에 빠른 검색과 효율적 질의 처리 가능
      - Transparency: 검색 결과가 보통 해석 가능하며, 용어 매칭에 기반하기 때문에 설명 명확
    - 단점
      - 제한된 의미 이해(Limited semantic understanding)
        - 쿼리에 bad guy라는 표현 쓰였지만 실제 문서에 villain이라는 단어가 사용되어 매칭되지 않음
  - Dense Retriever(의미적 유사도 기반)
    - 쿼리와 문서를 표현하기 위해 dense vector(embeddings)을 활용해 의미적 유사도에 기반
    - Embedding Models, Bi-encoder, Cross-encoder
    - 장점
      - 의미적 이해: 동의어나 다양한 표현을 더 효과적으로 처리, 즉 글의 문맥과 의미 포착
      - 풍부한 쿼리 표현: 복잡한 쿼리와 긴 검색 쿼리의 의미 더 잘 포착
    - 단점
      - 높은 연산 비용
      - 제한된 투명성
      - 데이터 및 모델 의존성
<br>
<br>

## 3. Retrieval-augmented LM
- 추론 시 외부 데이터 저장소를 불러와 활용하는 언어모델을 RAG라 부름
- RAG: 정보 검색부터 답변 생성까지의 프레임워크

- Why Retrieval-augmented LM?
  1. 거대언어모델은 모든 지식을 다 자신의 파라미터에 저장하지 못한다
  2. 거대언어모델이 보유한 지식은 금세 시대에 뒤쳐지며, 갱신이 어렵다
  3. 거대언어모델의 답변은 해석과 검증이 어려움
  4. 기업 내부 정보와 같은 보안 정보는 언어모델 학습에 활용되지 않음

- Challenges of Retrieval-autmented LM?
  1. Context를 어떻게 구성해야 하는가?
    - 해결책:언어모델의 컨텍스트 길이를 늘려야 한다
  2. RAG의 결과는 검색 모델 성능에 의존 -> 검색 노이즈에 취약
    - 해결책: Training with Noises
  3. LLM의 사전지식과 컨텍스트 간 충돌 발생
    - 해결책: Context 위에서 Grounding 학습 강화, Context가 없을 때, 답변 회피/거절 학습
  4. 복잡한 추론 필요 & 문서가 명확한 사실에 대한 오류를 포함할 때
<br>
<br>

# LLMs with Tool Usage(LLM Agent, Tool Use, MCP)
## 1. Basic Concepts of LLM Agents
- Agent: 센서를 통해 환경을 인지하고, 액추에이터를 통해 환경에 대해 액션을 통해 영향을 미치는 것으로 간주될 수 있는 모든 것
- LLM Agent란?
  - LLM을 핵심 구조로 삼아 환경을 이해하고 행동을 수행하는 에이전트
  - LLM-first view: 기존 LLM을 활용한 시스템을 에이전트로 만든다
  - Agent-first view: LLM을 AI 에이전트에 통합하여, 언어를 활용한 추론과 의사소통을 가능케 한다
<br>
<br>

## 2. Tool Usage in LLMs
- Tool: 언어 모델 외부에서 실행되는 프로그램에 연결되는 함수 인터페이스
  - LLM은 함수 호출과 입력 인자를 생성함으로써 이 도구를 활용할 수 있다

- Tool Learning 방식
  - 모방 학습(Imitation Learning)
    - 인간의 도구 사용 행동 데이터를 기록함으로써, 언어모델이 인간의 행동을 모방하도록 학습
    - 가장 간단하고 직관적
  - 멀티 모달 툴 러닝(Multi-modal Tool Learning)
    - 멀티모달 대규모 언어모델(MLLM)을 기반으로 도구를 정의하고 활용하는 연구
  - 강화 학습
    - 지도 학습을 넘어 에이전트에서의 강화학습을 도입하는 연구
<br>
<br>

## 3. Model Context Protocol(MCP)
- Why MCP?
  - 외부 툴을 활용하는 연구가 급증하면서 회사/모델 마다 각기 다른 툴 호출 방식 및 스키마 개발
  - 문제점: 호환성 부족, 재사용 어려움

- MCP
  - 언어 모델이 회부 툴과 상호작용하기 위한 표준화된 방식으로 정의한 프로토콜
  - 툴 호출, 응답 전달, 컨택스트 공유를 하나의 공통 규격으로 처리
  - 장점: 표준화, 확장성, 호환성, 재사용성, 투명성
<br>
<br>

# AI Agents & Langchain
## 1. Environment Representation & Understanding
- 환경과 에이전트 활용 예시들
  - 챗봇
  - 로보틱스
  - 임바디드 에이전트
  - 게임
  - 소프트웨어 개발

- 에이전트가 환경을 이해하기 위해 필요한 것
  - 환경에 접근하기 위한 툴
  - 환경의 표현(Representation): 텍스트, 이미지, 텍스트 기반 웹
  - 환경을 이해/탐색하기 위한 방법론들: 환경 특화 프롬프트, 비지도 프롬프트 유도, 환경 탐색, 탐색 기반 궤적 기억
<br>
<br>

## 2. Reasoning & Planning
- Planning 종류
  - Local Planning
    - 한 단계씩 계획을 세움
    - 매 스텝마다 사용할 하나의 툴 결정
    - 단순하고 직관적이나 장기 의존성 문제 발생
  - Global Planning
    - 실행 가능한 전체 계획 경로를 한번에 생성
    - 여러 개의 툴을 조합하여 시퀀스 형태로 결정
    - 효율적이나 복잡한 환경에서는 실패 가능
- 오류 식별과 회복
- 계획 재검토
<br>
<br>

## 3. Langchain
- LLM 기반 애플리케이션을 빠르게 개발할 수 있는 오픈 소스 프레임워크
- LLM을 다양한 데이터/툴과 연결하여 강력한 애플리케이션 개발 가능
- 특징
  - 다양한 LLM provider와 통합하여 모델/회사별 API 차이를 공통 인터페이스로 관리 가능
  - Prompt, Memory, Tools와 같은 컴포넌트들이 모듈화 되어 있어 재사용성과 확장성 확보
  - LangGraph 기반으로 복잡한 워크플로우를 시각적으로 설계 및 관리 가능
- 주요 컴포넌트
  - Prompt Templates: 프롬프트 구조화
  - Chains: 여러 단계를 연결한 워크 플로우
  - Agents: 동적으로 툴 선택 및 실행
  - Memory: 대화 히스토리와 상태 유지
  - Tools: 외부 API, DB, 계산기 등 연결
  - ETC.