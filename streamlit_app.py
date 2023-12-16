import streamlit as st
import random

# 乱数を生成して運勢を返す関数
def get_fortune(random_number):
    fortunes = ["超ウルトラスーパー大吉","ミラクル大吉", "ラッキー中吉", "ハッピー小吉", "末吉","青いものを持ってると吉", "ゴミを拾うと吉","凶……元気をだして強くいきなはれ"]
    return fortunes[random_number % 8]

# Webアプリケーションのタイトルを設定
st.title('今日の運勢を占う')

# 乱数の入力フォームを作成
random_number = st.number_input('1から100の間で好きな数字を入力してください', min_value=1, max_value=100)

# 占いボタンが押されたときの処理
if st.button('占う'):
    # 乱数に応じた運勢を取得
    fortune = get_fortune(random_number)
    st.write(f'あなたの今日の運勢は{fortune}！')
