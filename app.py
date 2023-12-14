
import streamlit as st
from streamlit.logger import get_logger
from process_data import get_df
LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="10Academy",
        page_icon="👋",
    )

    st.write("# Welcome to my website! 👋")

    st.sidebar.success("memo")

    df = get_df()
    # st.write(df)

    img = st.file_uploader('please upload an image', type = ["jpg","png"])
    if img is not None:
        st.image(img)

    muti_select = st.multiselect('what is your fevourite phone?',options= ('apple','samsung','huwawi'))
    st.write(muti_select)





if __name__ == "__main__":
    run()
