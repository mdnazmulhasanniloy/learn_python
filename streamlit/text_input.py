import streamlit as st

st.title("my first web in streamlit", anchor=False)
st.header("this is a header", anchor=False)
st.subheader("this is a subheader", anchor=False)
st.text("this is a text")
st.markdown(":orange[this] **is** a :yellow-background[markdown]")
st.latex("this is a latex")
st.code("this is a code")
st.error("this is a error")
st.warning("this is a warning")
st.info("this is a info")
st.success("this is a success")
st.exception("this is a exception" , )