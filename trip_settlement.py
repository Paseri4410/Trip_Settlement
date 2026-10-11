import streamlit as st

st.title("旅費精算アプリ")

TripMemberNum = st.number_input("旅行参加人数を入力")
TripMemberName = [None] * int(TripMemberNum)
# それぞれの立て替え金額一覧
TripMemberAdvancePaymentSum = [0] * int(TripMemberNum)
# それぞれがそれぞれに支払う金額一覧
TripMemberPayList = [[0] * int(TripMemberNum) for _ in range(int(TripMemberNum))]


# それぞれの立て替え額計算
for TripMember in TripMemberNum:
    TripMemberName = st.text_input("旅行参加者の名前を入力")
    while True:
        TripMemberAdvancePayment = st.number_input(f"{TripMemberName[TripMember]}が立て替えた金額を入力")
        TripMemberAdvancePaymentSum[TripMember] += TripMemberAdvancePayment
        if st.button("合計を計算"):
            break
    st.write(f"{TripMemberName[TripMember]}が立て替えた合計金額：{TripMemberAdvancePaymentSum[TripMember]} 円") 

for TripMemberPay in TripMemberNum:
    for TripMemberGet in TripMemberNum:
        TripMemberPayList[TripMemberPay][TripMemberGet] = TripMemberAdvancePaymentSum[TripMemberGet] / TripMemberNum
        if TripMemberPay == TripMemberGet:
                    TripMemberPayList[TripMemberPay][TripMemberGet] = 0

for TripMember_1 in TripMemberNum:
    for TripMember_2 in TripMemberNum:
          TripMemberPayList[TripMember_1][TripMember_2] -= TripMemberPayList[TripMember_2][TripMember_1]
    st.dataframe(TripMemberPayList)

