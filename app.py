import streamlit as st

def find_maximum(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Maximum Number Finder")

    num1 = st.number_input("Enter first number:")
    num2 = st.number_input("Enter second number:")
    num3 = st.number_input("Enter third number:")

    if st.button("Find Maximum"):
        maximum = find_maximum(num1, num2, num3)
        st.write(f"The maximum number is: {maximum}")

if __name__ == "__main__":
    main()