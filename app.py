import streamlit as st
#from factorial import fac
def main():
    st.title('Vinh co ngu khong???')
    n=st.text_input('Yes or No')
    if st.button('Kiem Tra'):
        if n==yes:
            st.write('NGU THAT')
        else:
            st.write('SAIIII')
        st.balloons()
    # st.title('Factorial Caculate')
    # number=st.number_input("Enter a number: ",min_value=0,max_value=1000)
    # if st.button('Caculate'):
    #     result=fac(number)
    #     st.write(f'The factorial of {number} is {result}')
    #     st.balloons()
if __name__=='__main__':
    main()
