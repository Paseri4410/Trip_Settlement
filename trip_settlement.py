import streamlit as st

st.title("旅費精算アプリ")

TripMemberNum = int(st.number_input(
        "旅行参加人数を入力",
        min_value = 0,
        step = 1
    )
)
TripMemberName = [None] * TripMemberNum
# それぞれの立て替え金額一覧
TripMemberAdvancePaymentSum = [0] * TripMemberNum
# それぞれがそれぞれに支払う金額一覧
TripMemberPayList = [[0] * TripMemberNum for _ in range(TripMemberNum)]


# それぞれの立て替え額計算
for TripMember in range(TripMemberNum):
    TripMemberName[TripMember] = st.text_input("旅行参加者の名前を入力")
    while True:
        TripMemberAdvancePayment = int(st.number_input(
                f"{TripMemberName[TripMember]}が立て替えた金額を入力",
                min_value = 0,
                step = 1
            )
        )
        TripMemberAdvancePaymentSum[TripMember] += TripMemberAdvancePayment
        if st.button("合計"):
            break
    st.write(f"{TripMemberName[TripMember]}が立て替えた合計金額：{TripMemberAdvancePaymentSum[TripMember]} 円") 

for TripMemberPay in range(TripMemberNum):
    for TripMemberGet in range(TripMemberNum):
        TripMemberPayList[TripMemberPay][TripMemberGet] = TripMemberAdvancePaymentSum[TripMemberGet] / TripMemberNum
        if TripMemberPay == TripMemberGet:
                    TripMemberPayList[TripMemberPay][TripMemberGet] = 0

for TripMember_1 in range(TripMemberNum):
    for TripMember_2 in range(TripMemberNum):
          TripMemberPayList[TripMember_1][TripMember_2] -= TripMemberPayList[TripMember_2][TripMember_1]
    st.dataframe(TripMemberPayList)

