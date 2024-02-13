import streamlit as st
import zipfile
import base64
import os
from pathlib import Path

from common_spell import get_common_spell_matrix, serialize_matrix_plaintext, serialize_matrix_docx

# Web App Title
st.markdown('''
# **Get Common Spell**

This is the **Common Spell App** created in Python using the Streamlit library.



---
''')

# Upload examplar file
with st.sidebar.header('1. Upload your examplar file'):
    examplar_file = st.sidebar.file_uploader("Examplar file in .txt format", type=["txt"])

# Upload version files
with st.sidebar.header('2. Upload your version files ZIP file'):
    version_files = st.sidebar.file_uploader("Version files ZIP file", type=["zip"])

def get_version_texts(version_files):
    """
    Unzips a zip file and extracts all .txt files into a dictionary.

    Parameters:
    - zip_file_path: The path to the zip file.

    Returns:
    - A dictionary with keys as .txt file names and values as their content.
    """
    txt_files_content = {}
    
    with zipfile.ZipFile(version_files, 'r') as zip_ref:
        # Extract all the contents into memory (considering file sizes are manageable)
        for file_info in zip_ref.infolist():
            # Check if the file is a .txt file
            if file_info.filename.endswith('.txt'):
                with zip_ref.open(file_info) as file:
                    # Assuming the file's content is in utf-8 encoding
                    content = file.read().decode('utf-8')
                    txt_files_content[file_info.filename] = content
                    
    return txt_files_content

# File download
def filedownload(commonspell):
    b64 = base64.b64encode(commonspell.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/txt;base64,{b64}" download="common_spell.txt">Download Common spell as txt</a>'
    return href

def docx_download():
    data = open('common_spell.docx', 'rb').read()
    b64 = base64.b64encode(data).decode('UTF-8')
    #b64 = base64.b64encode(xl.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/docx;base64,{b64}" download="common_spell.docx">Download common spell docx</a>'
    return href

# Main panel
if st.sidebar.button('Submit'):
    #@st.cache
    examplar_text = examplar_file.read().decode('utf-8')
    version_texts = get_version_texts(version_files)
    common_spell_matrix = get_common_spell_matrix(examplar_text, version_texts)
    common_spell_plaintext = serialize_matrix_plaintext(common_spell_matrix)
    version_texts[examplar_file.name] = examplar_text
    common_spell_docx = serialize_matrix_docx(common_spell_matrix, version_texts)
    st.header('**Common Spell text**')
    # st.write(df)
    st.markdown(filedownload(common_spell_plaintext), unsafe_allow_html=True)
    st.markdown(docx_download(), unsafe_allow_html=True)
else:
    st.info('Awaiting for ZIP file to be uploaded.')