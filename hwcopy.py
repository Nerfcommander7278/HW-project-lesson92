import streamlit as st
def ce(p,n,r):
  t = n*12
  rm = r
  emi = p * rm/100 * (1+rm/100)**t / (1+rm/100)**t -1
  return emi
st.title('Emi counter Web App')
p = st.slider('Principal Loan Amount', 1000, 1000000)
while True:
  n = st.slider('Loan period in years', 1, 30)
  break
r = st.slider('Interest rate per annum', 1, 15)
m = st.slider('Period after tenure for amount to be calculated',1,n*12)
if st.button('Calculate EMI'):
  st.write(f"EMI is {ce(p,n,r)}")
def ce2(p,n,r,m):
  t = n*12
  rm = r/12
  ee = 1 + rm/100
  emi2 = p * ee**t - ee**m/ee**t - 1
  return emi2
if st.button('Outstanding Loan Balance'):
  st.write(f"Outstanding Loan Balance is {ce2(p,n,r,m)}")