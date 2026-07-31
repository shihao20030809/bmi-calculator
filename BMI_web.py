import streamlit as st

st.title("🏃 BMI 测试器")

weight = st.number_input("请输入您的体重（kg）", min_value=1.0)
height = st.number_input("请输入您的身高（m）", min_value=0.1)

if st.button("计算 BMI"):
    bmi = weight / (height ** 2)

    st.write(f"您的 BMI 为：{bmi:.2f}")

    if bmi < 18.5:
        st.success("属于偏瘦范围")
    elif bmi <= 25:
        st.success("属于正常范围")
    elif bmi <= 30:
        st.warning("属于偏胖范围")
    else:
        st.error("属于肥胖范围")