import streamlit as st
from datetime import datetime

# Configurações do layout e cores
st.set_page_config(page_title="SoundAnalyser", layout="centered")
st.markdown(
    """
    <style>
    .main {
        background-color: #000000;
        padding: 10px;
    }
    .stTextInput > div > div > input {
        border-color: #00666B;
    }
    .stSelectbox > div > div > select {
        border-color: #00666B;
    }
    .stButton > button {
        background-color: #00666B;
        color: white;
    }
    .stFileUploader > div > div {
        border-color: #00666B;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.image("https://raw.githubusercontent.com/lxndrrms/soundanalyser/main/Logo_menu.webp", width=450)

# Título do sistema
st.title("SoundAnalyser")

# Campo de texto para Número de Série, Descrição, Data de Atual, Data de Montagem
serial_number = st.text_input("Número de Série do Produto", "000060041800651")
description = st.text_input("Descrição", "Sirene Veili")
current_date = st.date_input("Data Atual", datetime.today())
assembly_date = st.date_input("Data de Montagem", datetime.today())

# Listbox para seleção da linha de áudio
audio_line = st.selectbox("Selecione a linha de áudio", ["Áudio Sirene 1", "Áudio Sirene 2", "Áudio Sirene 3"])

# Upload de arquivo de áudio
uploaded_audio = st.file_uploader("Selecione um arquivo de áudio", type=["wav", "mp3"])

# Campo de texto para URL
audio_url = st.text_input("URL do servidor", "http://192.168.0.59:5000/playsirene")

# Botão para iniciar a captura do áudio
if st.button("Iniciar Captura de Áudio"):
    st.write("Captura de áudio iniciada...")

# Botão para análise comparativa dos áudios
if st.button("Geração de laudo"):
    st.write("Análise comparativa iniciada...")

# Nota de rodapé
st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <small>SoundAnalyser © 2024</small>
    </div>
    """,
    unsafe_allow_html=True,
)
