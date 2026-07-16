
import streamlit as st
import pandas as pd

# 2개의 열이 생성되고 열의 크기 3:1로 지정
col1, col2 = st.columns([3,1])

# 컬럼 영역 구분을 위한 css코드 추가
st.markdown(
    '''
    <style>
        .custom-column {
            background-color: lightblue;
            padding: 5px
        }
    </style>
    ''', unsafe_allow_html=True
)

labels = ['남성', '여성']
values = [20, 30]

col1.subheader("column 1")
col1.markdown('<div class="custom-column">', unsafe_allow_html=True)
col1.bar_chart(values)

data = {'Lable1' : labels, 'Values': values}
df = pd.DataFrame(data)

col2.subheader("column 2")
col2.markdown('<div class="custom-column">', unsafe_allow_html=True)
col2.table(df)
