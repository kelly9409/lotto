import streamlit as st
from lotto_utils import *

st.title('로또 번호 생성기')
n = st.number_input('게임 수를 입력하세요', min_value=1, max_value=10, value=1, step=1)

if st.button('생성'):
    games = make_games(n)

    lines = []
    for i in range(n) :
        lines.append(f'게임 {i+1} : {to_text(games[i])}')
    st.code('\n'.join(lines), language=None)
