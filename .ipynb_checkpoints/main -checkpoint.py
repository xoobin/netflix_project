import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#주제
st.title("넷플릭스에게 제안하는 새로운 요금제") 
st.subheader("")

# 데이터 정리
data = {
    "구분": ["20대", "30대", "40대", "50대"],
    "사례수": [59, 66, 104, 116],
    "있다": [50.8, 65.2, 35.6, 38.8],
    "없다": [49.2, 34.8, 64.4, 61.2],
}

df = pd.DataFrame(data)

#제목
st.header("1.연령대별 과거 넷플릭스 이용 경험")

# 그래프 그리기
plt.rcParams['font.family'] = 'NanumGothic'  
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="구분", y="있다", color="skyblue", label="있다")
sns.barplot(data=df, x="구분", y="없다", color="salmon", label="없다", bottom=df["있다"])
plt.title("과거 넷플릭스 이용 경험", fontsize=16)
plt.xlabel("구분", fontsize=12)
plt.ylabel("비율 (%)", fontsize=12)
plt.legend(title="이용 여부", fontsize=10)
plt.xticks(rotation=45)

# Streamlit에 그래프 출력
st.pyplot(plt)

st.subheader("")
st.subheader("")

#두번째 항목_넷플릭스 중단 사유 설문
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.header("2.2030 넷플릭스 구독 중단 사유")

# 데이터프레임 생성
data = {
    "구분": ["20대", "30대"],
    "이용 요금이 부담돼서": [63.3, 55.8],
    "요금을 계속 올리는 넷플릭스의 정책이 마음에 안들어서": [46.7, 30.2],
    "계정을 공유해 사용하는 것이 어려워져서": [6.7, 6.9],
    "유튜브 등 대체 가능한 무료 서비스를 이용하면 돼서": [16.7, 16.7],
    "다른 OTT 서비스로 갈아타려고": [3.3, 6.9],
    "재밌는 콘텐츠가 별로 없어서": [26.7, 27.9],
    "별로 더 볼만한 게 없어서": [46.7, 30.2],
    "동영상 시청할 시간이 잘 안나서": [16.7, 15.6],
}

df = pd.DataFrame(data)

# 데이터프레임을 Streamlit 표로 표시
st.dataframe(df)

# 데이터 변환: 세로 막대 그래프에 적합하게 melt
df_melted = df.melt(id_vars=["구분"], var_name="이유", value_name="비율")

# 그래프 생성
plt.figure(figsize=(14, 8))
sns.barplot(data=df_melted, x="비율", y="이유", hue="구분", palette="muted")
plt.title("넷플릭스 이용 중단 이유 (연령대별)", fontsize=16)
plt.xlabel("비율 (%)", fontsize=12)
plt.ylabel("이유", fontsize=12)
plt.legend(title="연령대", fontsize=10)
plt.tight_layout()

# Streamlit에서 그래프 표시
st.pyplot(plt)

st.subheader("=>가장 높은 비중을 차지하는 사유 1,2위가 비용과 관련")
st.subheader("")
st.subheader("")


#세번째
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Streamlit 제목 추가
st.header("3.광고요금제 도입과 가입자 증감 예상") 

# 데이터 생성
data = {
    "구분": ["20대", "30대"],
    "크게 늘 것이다": [5.6, 6.4],
    "오히려 줄 것이다": [24.0, 23.2]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 데이터프레임을 Streamlit에 표시
st.dataframe(df)

# 데이터 준비
categories = df["구분"]  # x축 레이블
labels = ["크게 늘 것이다", "오히려 줄 것이다"]  # 각 항목
values = df.iloc[:, 1:].values.T  # 각 항목에 대한 값 (Transpose 필요)

# 막대 그래프 생성
x = np.arange(len(categories))  # x 위치 설정
width = 0.15  # 막대 너비

fig, ax = plt.subplots(figsize=(10, 6))

for i, label in enumerate(labels):
    ax.bar(x + i * width, values[i], width, label=label)

# 그래프 꾸미기
ax.set_xlabel("구분", fontsize=12)
ax.set_ylabel("비율 (%)", fontsize=12)
ax.set_title("광고요금제 도입으로 넷플릭스 가입자 증감 예상", fontsize=14)
ax.set_xticks(x + width * (len(labels) - 1) / 2)
ax.set_xticklabels(categories)
ax.legend(title="응답 항목")
ax.grid(axis="y", linestyle="--", alpha=0.7)

# Streamlit에 그래프 표시
st.pyplot(fig)

st.subheader("=>부정적 의견이 긍정적 의견의 3~4배 이상")

st.subheader("")
st.subheader("")

#네번쨰
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit 제목 추가
st.header("4.광고요금제 구성 선호도")

# 데이터 생성
data = {
    "구분": ["20대", "30대"],
    "콘텐츠 시작 전에만 광고가 붙고 기존 요금제에서 좀 덜 깎아주는 광고요금제": [79.0, 78.6],
    "콘텐츠 시작 전 + 중간중간 광고가 붙고 기존 요금제에서 좀 더 많이 깎아주는 광고요금제": [21.0, 21.4],
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 데이터프레임을 Streamlit에 표시
st.dataframe(df)

# 그래프 생성
fig, ax = plt.subplots(figsize=(8, 6))
df.set_index("구분").plot(kind="bar", ax=ax)

# 그래프 꾸미기
ax.set_title('광고요금제 구성 선호도', fontsize=14)
ax.set_xlabel('연령대', fontsize=12)
ax.set_ylabel('선호 비율 (%)', fontsize=12)
ax.set_xticklabels(df["구분"], rotation=0)  # 레이블 회전

# Streamlit에서 그래프 표시
st.pyplot(fig)

st.subheader("=>비용보다는 광고 빈도 절감을 중시")
st.subheader("  =>중대한 구독 중단 사유였던 비용보다 광고가 더 중요")

st.subheader("")
st.subheader("")


import streamlit as st

#다섯번째_대안 제시
st.title("5.대안 제시")
print("")
print("")

import streamlit as st
image_path = "./중앙일보_MAU하락기사캡첩ㄴ.png"

# 중앙일보 기사 일부 발췌 이미지
st.image(image_path, caption="출처:중앙일보 2021.05.20일자 기사", width=1000)

st.subheader("")

st.subheader("=>코로나 종식 이후 월간 순이용자(MAU) 하락세")
st.subheader("=>콘텐츠 수요량 하락으로 구독 제도의 합리성 감소")
st.title("=>콘텐츠 개수에 따른 요금제 제안") 

st.subheader("")
st.subheader("")
st.subheader("")

#원본 데이터를 확인할 수 있는 source 버튼 만들기
import streamlit as st
import webbrowser

link = "https://www.data.go.kr/data/15112345/fileData.do"  # 데이터 소스 링크

if st.button("Source"):
    webbrowser.open(link)


#기사 링크
import streamlit as st
import webbrowser

link = "https://www.joongang.co.kr/article/24062627"  # 중앙일보 기사 링크

if st.button("News"):
    webbrowser.open(link)



