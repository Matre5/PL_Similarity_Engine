import streamlit as st

st.set_page_config(page_title="About", page_icon="📈", layout="wide")

st.sidebar.header("About❔")

progress_bar = st.sidebar.progress(0)


# Define columns: adjust the ratios as needed (e.g., [10, 0.2, 10])
col1, col2, col3 = st.columns([10, 0.2, 10])

with col1:
    st.subheader("Left Side")
    st.write("Content for the left side of the divider goes here. You can add widgets, text, etc.")
    st.image("https://static.streamlit.io/examples/cat.jpg") # Example image

with col2:
    # Use st.markdown to inject HTML/CSS for the vertical line
    st.markdown(
        """
        <div class="divider-vertical-line"></div>
        <style>
        .divider-vertical-line {
            border-left: 2px solid rgba(49, 51, 63, 0.2);
            height: 300px; /* Adjust height as needed to cover your content */
            margin: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.subheader("Right Side")
    st.write("Content for the right side goes here. The height of the divider may need adjustment to match the height of the surrounding elements.")
    st.button("An example button")
