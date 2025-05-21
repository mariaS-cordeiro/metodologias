import streamlit as st
import base64

st.set_page_config(page_title="Metodologia da pesquisa em comunicação digital", layout="wide")
st.title("🎓 Metodologia da pesquisa em comunicação digital")

# Lista com os nomes das metodologias (chaves)
metodologias = [
    "entrevistas", "observacao", "grupos_focais",
    "etnografia", "documentos", "caso", "survey"
]

# Gera abas com os títulos formatados
abas = st.tabs([
    "📋 Entrevistas",
    "👀 Observação",
    "💬 Grupos focais",
    "🌍 Etnografia",
    "📑 Documentos",
    "📚 Estudo de caso",
    "📊 Survey"
])

# Descrições e links de vídeo por chave
abas_textos = {
    "entrevistas": (
        "Metodologia qualitativa baseada em conversas estruturadas, semiestruturadas ou abertas.",
        "https://www.youtube.com/watch?v=wuIKfjvH6SM"
    ),
    "observacao": (
        "Metodologia qualitativa baseada na observação sistemática de comportamentos e contextos, podendo ser participante ou não.",
        "https://www.youtube.com/watch?v=lFweX8gRuvY"
    ),
    "grupos_focais": (
        "Metodologia qualitativa baseada na discussão moderada entre participantes para explorar percepções e significados compartilhados.",
        "https://www.youtube.com/watch?v=ihTQPBxZpRs"
    ),
    "etnografia": (
        "Metodologia qualitativa baseada na imersão prolongada do pesquisador no campo para compreender práticas culturais.",
        "https://www.youtube.com/watch?v=zngvQobfaBo"
    ),
    "documentos": (
        "Análise de textos, arquivos, registros e materiais institucionais ou históricos.",
        "https://www.youtube.com/watch?v=5MdxS82aEdc"
    ),
    "caso": (
        "Investigação profunda de um único caso contextualizado.",
        "https://www.youtube.com/watch?v=3gVjUoaeoG0"
    ),
    "survey": (
        "Metodologia quantitativa baseada em questionários estruturados aplicados a grandes quatidades e amostras",
        "https://www.youtube.com/watch?v=Ge52zqBLlDs"
    )
}

# Gera link para baixar anotações como .txt
def gerar_download(anotacoes, nome):
    conteudo = f"Anotações sobre {nome.capitalize()}:\n\n{anotacoes}"
    b64 = base64.b64encode(conteudo.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="anotacoes_{nome}.txt">📥 Baixar anotações</a>'

# Interface de cada aba
def interface_metodologia(titulo, descricao, video_url, chave):
    st.markdown(f"### 🧭 Sobre {titulo}")
    st.write(descricao)

    st.markdown("### 📂 Upload de base de dados ou materiais complementares")
    arquivo = st.file_uploader("Envie arquivos (ex: .csv, .pdf, .docx, etc)", key=f"{chave}_upload")
    if arquivo:
        st.success(f"Arquivo carregado: {arquivo.name}")

    st.markdown("### 🎥 Vídeo explicativo")
    st.video(video_url)

    st.markdown("### 📝 Bloco de notas (anotações individuais)")
    anotacoes = st.text_area("Escreva suas definições, conceitos e observações:", height=250, key=f"{chave}_notas")

    if anotacoes:
        st.markdown(gerar_download(anotacoes, chave), unsafe_allow_html=True)

# Executa interface para cada aba/metodologia
for aba, chave in zip(abas, metodologias):
    descricao, video = abas_textos[chave]
    with aba:
        interface_metodologia(chave.capitalize(), descricao, video, chave)
