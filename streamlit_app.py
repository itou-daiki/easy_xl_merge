import streamlit as st
import pandas as pd
import openpyxl
from io import BytesIO

st.set_page_config(page_title="easy Excel Merge")

st.title("easy Excel Merge")
st.subheader("データフレーム結合Webアプリケーション")
st.caption("Created by Dit-Lab.(Daiki Ito)")

# ファイルアップロードセクション
file1 = st.file_uploader("１つ目のExcelファイルをアップロード", type=['xlsx'])
file2 = st.file_uploader("２つ目のExcelファイルをアップロード", type=['xlsx'])

if file1 and file2:
    # ファイル名取得
    file1_name = file1.name.split('.')[0]  # 拡張子を除いたファイル名
    file2_name = file2.name.split('.')[0]

    # Excelファイルをデータフレームに読み込む
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # １つ目のファイルのプレビュー
    st.subheader("＜１つ目のExcelファイル＞")
    st.dataframe(df1)

    # ２つ目のファイルのプレビュー
    st.subheader("＜２つ目のExcelファイル＞")
    st.dataframe(df2)

    # 共通するカラム名を取得
    common_columns = list(set(df1.columns).intersection(df2.columns))
    if common_columns:
        # キーとなるカラムをユーザーに選択させる
        key_column = st.selectbox('結合に使用するキーとなるカラムを選択してください:', common_columns)

        # 結合タイプの選択
        join_type = st.radio("結合の種類を選択してください:", ('inner', 'outer'))
        st.caption("inner：欠損値を削除, outer:欠損値を保持")

        # データフレームの結合
        merged_df = pd.merge(df1, df2, on=key_column, how=join_type)

        # 結合したデータを表示
        st.write("結合されたデータ:", merged_df)

        # 結合されたデータをExcelファイルとしてダウンロード
        to_excel = BytesIO()
        merged_df.to_excel(to_excel, index=False, engine='openpyxl')  # インデックスなしでExcelファイルに変換
        to_excel.seek(0)  # ファイルポインタを最初に戻す
        st.download_button(label="結合されたデータをダウンロード",
                           data=to_excel,
                           file_name=f"{file1_name}_{file2_name}_merged.xlsx",
                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    else:
        st.warning('共通するカラムが存在しません。結合するには共通のカラムが必要です。')

# Copyright
st.markdown('© 2022-2023 Dit-Lab.(Daiki Ito). All Rights Reserved.')
