import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image 
import time      
st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'

left_column,right_column = st.columns(2)
button = left_column.button('右にカラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write ('問い合わせ内容を書く')

expander2 = st.expander('問い合わせ')
expander2.write ('問い合わせ内容を書く')


expander3 = st.expander('問い合わせ')
expander3.write ('問い合わせ内容を書く')

expander4 = st.expander('問い合わせ')
expander4.write ('問い合わせ内容を書く')

expander5 = st.expander('問い合わせ')
expander5.write ('問い合わせ内容を書く')

# text = st.text_input= ('あなたの趣味を教えてください？') 
# condition = st.slider('あなたの今の調子は？',0,100,50) 

# '趣味は：' ,text
# 'コンディション' ,condition

