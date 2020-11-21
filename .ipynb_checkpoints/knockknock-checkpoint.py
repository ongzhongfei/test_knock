import streamlit as st
import base64

st.header("Knock Knock Hello..?")

# st.markdown("<h1 style='text-align: right; color: red;'>Some title</h1>", unsafe_allow_html=True)


# st.image("download.png")
# st.markdown("![test Text](https://media.tenor.com/images/0283f8169ce766913c3bb8c615dd6ec7/tenor.gif)", unsafe_allow_html=True)

# st.image("https://media.tenor.com/images/0283f8169ce766913c3bb8c615dd6ec7/tenor.gif")

# if st.checkbox("Someone is knocking on the door..."):
#     st.write(
#         f"""<img src="https://media.tenor.com/images/81bbe0d73234b6a6f96cb79870ffe592/tenor.gif" style="float:left">""",
#         unsafe_allow_html=True,
#     )
#     if st.checkbox("Open the door"):
#         st.write(
#             f"""<img src="https://i.pinimg.com/originals/0d/a5/cb/0da5cbca5d728a789100439958f50235.gif" style="float:right">""",
#             unsafe_allow_html=True,
#         )

#         st.write(
#             f"""<img src="https://media.tenor.com/images/0283f8169ce766913c3bb8c615dd6ec7/tenor.gif" style="float:left">""", #style="vertical-align:middle"
#             unsafe_allow_html=True,
#         )


col1, col2 = st.beta_columns(2)
if col1.checkbox("Sounds like someone is knocking on the door..."):
    col1.write(
        f"""<img src="https://media.tenor.com/images/81bbe0d73234b6a6f96cb79870ffe592/tenor.gif" style="float:left">""",
        unsafe_allow_html=True,
    )

    if col2.checkbox("Go and open the door and say Hi!"):
        col2.write(
            f"""<img src="https://i.pinimg.com/originals/0d/a5/cb/0da5cbca5d728a789100439958f50235.gif" style="float:right">""",
            unsafe_allow_html=True,
        )
        st.write( "<p style='text-align: right;'>(This is Kakak Eilyn btw. Very beautiful)</p>",
            unsafe_allow_html=True)


        col3, col4 = st.beta_columns(2)

        if col3.checkbox("Hello..."):
            col3.write(
                f"""<img src="https://media.tenor.com/images/c91f491657656ef79b69080c06768306/tenor.gif" style="float:left">""",
                unsafe_allow_html=True,
            )
            col3.write( "<p style='text-align: left;'>(This is me. Cutie)</p>",    unsafe_allow_html=True)

            if col4.checkbox("WHAT YOU WANT??"):
                # """### gif from local file"""
                file_ = open("angry.gif", "rb")
                contents = file_.read()
                data_url = base64.b64encode(contents).decode("utf-8")
                file_.close()

                col4.write(
                    f'<img src="data:image/gif;base64,{data_url}" style="float:right">',
                    unsafe_allow_html=True,
                )

                col5, col6 = st.beta_columns(2)
                if col5.checkbox("Sorriee..."):
                    col5.write(
                        f"""<img src="https://media1.tenor.com/images/7f030fc5351142d303f081db14b914ca/tenor.gif?itemid=10086712" style="float:left">""",
                        unsafe_allow_html=True,
                    )
                    if col6.checkbox("???"):
                        col6.write(
                            f"""<img src="https://toppng.com/uploads/preview/confused-anime-png-anime-question-png-gif-11563638774vp3mpnwbez.png" style="float:right" width="240" height="240">""",
                            unsafe_allow_html=True,
                        )

                        col7, col8 = st.beta_columns(2)
                        if col7.checkbox("For all the trouble..."):
                            col7.write(
                                f"""<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7ir_TizdZ7vXZS8V98g2Lll6YREYYqdYt7A&usqp=CAU" style="float:left">""",
                                unsafe_allow_html=True,
                            )
                            if col8.checkbox("..."):
                                col8.write(
                                    f"""<img src="https://qph.fs.quoracdn.net/main-qimg-6ed14162acb25116839c2bc2d601e4e3" style="float:right" width="360" height="250" >""",
                                    unsafe_allow_html=True,
                                )
                                col9, col10 = st.beta_columns(2)
                                if col9.checkbox("(I shall leave Kakak alone...) 拜拜"):
                                    col9.write(
                                        f"""<img src="https://media2.giphy.com/media/COYGe9rZvfiaQ/giphy.gif" style="float:left">""",
                                        unsafe_allow_html=True,
                                    )
                                    # st.write( "<p style='text-align: left;'>(This is me. Cutie)</p>",    unsafe_allow_html=True)  
                                    if col10.checkbox("Niceee. Good boy."):
                                        col10.write(
                                            f"""<img src="https://i.pinimg.com/736x/3b/20/33/3b2033cd7657842acb28440b90ade3ee.jpg" style="float:right" width="360" height="250" >""",
                                            unsafe_allow_html=True,
                                        )



