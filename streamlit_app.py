import streamlit as st
import pandas as pd
import openpyxl

st.set_page_config(page_title="easy Excel Join")

# App title and creator
st.title("easy Excel Join")
st.subheader("データフレーム結合Webアプリケーション")
st.caption("Created by Dit-Lab.(Daiki Ito)")

# ファイルアップロードセクション
file1 = st.file_uploader("１つ目のExcelファイルをアップロード", type=['xlsx'])
file2 = st.file_uploader("２つ目のExcelファイルをアップロード", type=['xlsx'])

if file1 and file2:
    # Excelファイルをデータフレームに読み込む
    df1 = pd.read_excel(file1)
    # プレビュー
    st.subheader("＜１つ目のExcelファイル＞")
    st.dataframe(df1)

    df2 = pd.read_excel(file2)
    # プレビュー
    st.subheader("＜２つ目のExcelファイル＞")
    st.dataframe(df2)

    # 同じ名前のカラムがある場合の警告
    common_columns = set(df1.columns).intersection(df2.columns)
    if common_columns:
        st.warning(f'両方のファイルに以下の同じ名前のカラムが存在します: {common_columns}. 結合時のエラーを避けるため、異なるカラム名を使用してください。')

    # データフレームの結合
    joined_df = df1.join(df2, lsuffix='_left', rsuffix='_right')

    # 結合したデータを表示
    st.write("結合されたデータ:", joined_df)

# Copyright
st.markdown('© 2022-2023 Dit-Lab.(Daiki Ito). All Rights Reserved.')
