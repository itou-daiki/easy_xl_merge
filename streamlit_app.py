import streamlit as st
import pandas as pd
import openpyxl

st.set_page_config(page_title="easy Excel Join")

st.title("easy Excel Join")
st.subheader("データフレーム結合Webアプリケーション")
st.caption("Created by Dit-Lab.(Daiki Ito)")

# ファイルアップロードセクション
file1 = st.file_uploader("１つ目のExcelファイルをアップロード", type=['xlsx'])
# Excelファイルをデータフレームに読み込む
df1 = pd.read_excel(file1)
# プレビュー
st.subheader("＜１つ目のExcelファイル＞")
st.dataframe(df1)

file2 = st.file_uploader("２つ目のExcelファイルをアップロード", type=['xlsx'])
# Excelファイルをデータフレームに読み込む
df2 = pd.read_excel(file2)
# プレビュー
st.subheader("＜２つ目のExcelファイル＞")
st.dataframe(df2)

if file1 and file2:
    # 共通するカラム名を取得
    common_columns = list(set(df1.columns).intersection(df2.columns))
    if common_columns:
        # キーとなるカラムをユーザーに選択させる
        key_column = st.selectbox('結合に使用するキーとなるカラムを選択してください:', common_columns)

        # データフレームの結合
        joined_df = pd.merge(df1, df2, on=key_column)

        # 結合したデータを表示
        st.write("結合されたデータ:", joined_df)
    else:
        st.warning('共通するカラムが存在しません。結合するには共通のカラムが必要です。')

# Copyright
st.markdown('© 2022-2023 Dit-Lab.(Daiki Ito). All Rights Reserved.')
