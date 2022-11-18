import streamlit as st

from utilities.inputs import write_text_from_file

# ----- Page setup -----
# The following options set up the display in the tab in your browser.
# Set page to widescreen must be first call to st.
st.set_page_config(
    page_title='Template project',
    page_icon=':thumbsup:',
    # layout='wide'
    )

write_text_from_file('pages/text_for_pages/5_Citation.txt',
                     head_lines_to_skip=2)
