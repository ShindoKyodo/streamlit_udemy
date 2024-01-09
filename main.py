import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



"start"
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.01)

"Doon!!"


st.write("Interactive Widgets")

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
  right_column.write("ここは右カラム")

expander1= st.expander("問い合わせ内容1")
expander1.write("回答")
expander1= st.expander("問い合わせ内容1")
expander1.write("回答")
expander1= st.expander("問い合わせ内容1")
expander1.write("回答")


text = st.text_input("あなたの趣味を教えてください")
"あなたの趣味：",text

condtion = st.slider("あなたの今の調子は？",0 ,100, 50)
"コンディション：",condtion

st.write("Display Image")
if st.checkbox("Show Image"):
  img = Image.open("sample.jpg")
  st.image(img, caption="K", use_column_width=True)

option = st.selectbox(
  "あなたが好きな数字を教えてください",
  list(range(1,11))

  ) 
"あなたが好きな数字は", option,"です"


# 正しい関数名は 'st.write' です
st.write("DataFrame")

# DataFrame の作成
df = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] +[35.69, 139.70],
    columns=["lat","lon"]
)



st.map(df)
st.area_chart(df)
st.bar_chart(df)



# DataFrame の表示
st.write(df)
st.dataframe(df.style.highlight_max(axis=0),width=500, height=500)
st.table(df.style.highlight_max(axis=0))
"""
#章
##節
##項
```Python
import streamlit as st
import numpy as np
import pandas as pd
```

"""
