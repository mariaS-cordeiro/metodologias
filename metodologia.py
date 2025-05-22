import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Metodologia da pesquisa em comunicação digital", layout="wide")
st.title("🎓 Metodologia da pesquisa em comunicação digital")

metodologias = [
    "entrevistas", "observacao", "grupos_focais",
    "etnografia", "documentos", "Estudo de caso", "survey"
]

abas = st.tabs([
    "📋 Entrevistas", "👀 Observação", "💬 Grupos focais",
    "🌍 Etnografia", "📑 Documentos", "📚 Estudo de caso", "📊 Survey"
])

abas_textos = {
    "entrevistas": (
        "Metodologia qualitativa baseada em conversas estruturadas, semiestruturadas ou abertas.",
        "https://www.youtube.com/watch?v=wuIKfjvH6SM"
    ),
    "observacao": (
        "Metodologia qualitativa baseada na observação sistemática de comportamentos e contextos.",
        "https://www.youtube.com/watch?v=LA3HBkH7QJE"
    ),
    "grupos_focais": (
        "Discussão moderada entre participantes para explorar percepções compartilhadas.",
        "https://www.youtube.com/watch?v=ihTQPBxZpRs"
    ),
    "etnografia": (
        "Imersão prolongada no campo para compreender práticas culturais.",
        "https://www.youtube.com/watch?v=6LIF2kBk1Z0"
    ),
    "documentos": (
        "Análise de textos, registros e materiais institucionais ou históricos.",
        "https://www.youtube.com/watch?v=7rX9vBATdzc"
    ),
    "Estudo de caso": (
        "Investigação profunda de um único caso contextualizado.",
        "https://www.youtube.com/watch?v=YwhpLMPX58c"
    ),
    "survey": (
        "Questionários estruturados aplicados a grandes amostras.",
        "https://www.youtube.com/watch?v=S9EJKvja96Q"
    )
}

def salvar_ficha_grupo(chave, dados):
    arquivo = f"fichas_grupo_{chave}.csv"
    if os.path.exists(arquivo):
        df = pd.read_csv(arquivo)
    else:
        df = pd.DataFrame(columns=dados.keys())
    df = pd.concat([df, pd.DataFrame([dados])], ignore_index=True)
    df.to_csv(arquivo, index=False)

def interface_metodologia(titulo, descricao, video_url, chave):
    st.markdown(f"### 🧭 Sobre {titulo}")
    st.write(descricao)

    st.markdown("### 🎥 Vídeo explicativo")
    st.video(video_url)

    st.markdown("### ✍️ Ficha de Grupo")
    with st.form(f"form_{chave}"):
        grupo = st.text_input("Nome do Grupo", key=f"{chave}_grupo")
        metodologia = st.text_input("Metodologia", key=f"{chave}_metodologia")
        definicao = st.text_area("1. Definição", height=80, key=f"{chave}_definicao")
        etapas = st.text_area("2. Etapas de aplicação", height=80, key=f"{chave}_etapas")
        tipo_dado = st.text_area("3. Tipo de dado", height=70, key=f"{chave}_tipo_dado")
        vantagens = st.text_area("4. Vantagens e limitações", height=80, key=f"{chave}_vantagens")
        exemplo = st.text_area("5. Exemplo de aplicação", height=80, key=f"{chave}_exemplo")
        pergunta = st.text_area("6. Pergunta para os visitantes", height=70, key=f"{chave}_pergunta")

        submitted = st.form_submit_button("💾 Salvar Ficha de Grupo")
        if submitted:
            dados = {
                "Nome do Grupo": grupo,
                "Metodologia": metodologia,
                "Definição": definicao,
                "Etapas": etapas,
                "Tipo de dado": tipo_dado,
                "Vantagens": vantagens,
                "Exemplo": exemplo,
                "Pergunta": pergunta
            }
            salvar_ficha_grupo(chave, dados)
            st.success("Ficha de Grupo salva com sucesso!")

    # Exibir fichas salvas
    arquivo = f"fichas_grupo_{chave}.csv"
    if os.path.exists(arquivo):
        st.markdown("### 📋 Fichas salvas")
        df = pd.read_csv(arquivo)
        st.dataframe(df)

# Executa interface em cada aba
for aba, chave in zip(abas, metodologias):
    descricao, video = abas_textos[chave]
    with aba:
        interface_metodologia(chave.capitalize(), descricao, video, chave)
