import streamlit as st
import pandas as pd
from PIL import Image


df_webtoon = pd.read_excel('webtoon_summary.xlsx')
genre_lut = sorted(list(set(df_webtoon['장르'])))
week_lut = "월화수목금토일"

##################### 요일별 장르 통계 #####################
genre_cnt_per_week = {g: 
                        # st.bar_chart의 x축 자동 오름차순 정렬을 방지(0월, 1화, 2수, ...)
                        {str(i) + w: 0 for i, w in enumerate(week_lut)}
                    for g in genre_lut}
idx_for_week = {d: str(i) for i, d in enumerate(week_lut)}
for i in range(len(df_webtoon)):    
    day = df_webtoon.loc[i, '요일']
    # st.bar_chart의 x축 자동 오름차순 정렬을 방지(0월, 1화, 2수, ...)
    day = idx_for_week[day] + day   
    gen = df_webtoon.loc[i, '장르']
    genre_cnt_per_week[gen][day] += 1


selected_genre = st.radio("장르", genre_lut)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.bar_chart(genre_cnt_per_week[selected_genre])


##################### 장르별 웹툰 목록 #####################
df_genre = df_webtoon.loc[df_webtoon['장르'] == selected_genre]

df_genre0 = df_genre.loc[df_genre['요일'] == week_lut[0]]
df_genre0.reset_index(inplace=True)
df_genre1 = df_genre.loc[df_genre['요일'] == week_lut[1]]
df_genre1.reset_index(inplace=True)
df_genre2 = df_genre.loc[df_genre['요일'] == week_lut[2]]
df_genre2.reset_index(inplace=True)
df_genre3 = df_genre.loc[df_genre['요일'] == week_lut[3]]
df_genre3.reset_index(inplace=True)
df_genre4 = df_genre.loc[df_genre['요일'] == week_lut[4]]
df_genre4.reset_index(inplace=True)
df_genre5 = df_genre.loc[df_genre['요일'] == week_lut[5]]
df_genre5.reset_index(inplace=True)
df_genre6 = df_genre.loc[df_genre['요일'] == week_lut[6]]
df_genre6.reset_index(inplace=True)

# st.dataframe(df_genre)
tabs = st.tabs(week_lut)

def display_webtoon_list(df_genre_per_day):
    for i in range(len(df_genre_per_day)):
        idx = i % 3
        if idx == 0:
            cols = st.columns(3)
        with cols[idx]:
            st.image(Image.open(f"thumbnails/{df_genre_per_day.loc[i, '썸네일_파일명']}.png"))
            msg = f"<div style='text-align: center; font-size: 15px;'><a href='{df_genre_per_day.loc[i, '링크']}' style='color: black; text-decoration-line: none;'>{df_genre_per_day.loc[i, '제목']}</a></div>"
            st.caption(msg, unsafe_allow_html=True)
            tags = "<div style='text-align: center; font-size: 15px;'>" + df_genre_per_day.loc[i, '태그'].replace("'", "")[1:-1] + "<div>"
            st.caption(tags, unsafe_allow_html=True)

# 월요일
with tabs[0]:
    display_webtoon_list(df_genre0)

# 화요일
with tabs[1]:
    display_webtoon_list(df_genre1)

# 수요일
with tabs[2]:
    display_webtoon_list(df_genre2)

# 목요일
with tabs[3]:
    display_webtoon_list(df_genre3)

# 금요일
with tabs[4]:
    display_webtoon_list(df_genre4)

# 토요일
with tabs[5]:
    display_webtoon_list(df_genre5)

# 일요일
with tabs[6]:
    display_webtoon_list(df_genre6)
