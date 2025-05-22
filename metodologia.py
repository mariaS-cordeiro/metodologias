import streamlit as st
import base64

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

def gerar_download(texto, nome_arquivo):
    b64 = base64.b64encode(texto.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{nome_arquivo}">📥 Baixar</a>'

def interface_metodologia(titulo, descricao, video_url, chave):
    st.markdown(f"### 🧭 Sobre {titulo}")
    st.write(descricao)

    st.markdown("### 📂 Upload de base de dados")
    arquivo = st.file_uploader("Envie arquivos (.csv, .pdf, .docx etc)", key=f"{chave}_upload")
    if arquivo:
        st.success(f"Arquivo carregado: {arquivo.name}")

    st.markdown("### 🎥 Vídeo explicativo")
    st.video(video_url)

    st.markdown("### 📝 Bloco de notas")
    anotacoes = st.text_area("Escreva anotações ou conceitos:", height=200, key=f"{chave}_notas")
    if anotacoes:
        st.markdown(gerar_download(anotacoes, f"anotacoes_{chave}.txt"), unsafe_allow_html=True)

    st.markdown("### ✍️ Ficha de Grupo")
    grupo = st.text_input("Nome do Grupo", key=f"{chave}_grupo")
    metodologia = st.text_input("Metodologia", key=f"{chave}_metodologia")
    definicao = st.text_area("1. Definição", height=80, key=f"{chave}_definicao")
    etapas = st.text_area("2. Etapas de aplicação", height=80, key=f"{chave}_etapas")
    tipo_dado = st.text_area("3. Tipo de dado", height=60, key=f"{chave}_tipo_dado")
    vantagens = st.text_area("4. Vantagens e limitações", height=80, key=f"{chave}_vantagens")
    exemplo = st.text_area("5. Exemplo de aplicação", height=80, key=f"{chave}_exemplo")
    pergunta = st.text_area("6. Pergunta para os visitantes", height=60, key=f"{chave}_pergunta")

    ficha_grupo = f"""FICHA DE GRUPO
Nome do Grupo: {grupo}
Metodologia: {metodologia}

1. Definição:
{definicao}

2. Etapas de aplicação:
{etapas}

3. Tipo de dado:
{tipo_dado}

4. Vantagens e limitações:
{vantagens}

5. Exemplo de aplicação:
{exemplo}

6. Pergunta para os visitantes:
{pergunta}
"""
    st.download_button("📥 Baixar Ficha de Grupo", data=ficha_grupo, file_name=f"ficha_grupo_{chave}.txt")

    st.markdown("### 📄 Ficha de Visita")
    grupo_visitado = st.text_input("Nome do grupo visitado", key=f"{chave}_visitado")
    palavra_chave = st.text_area("1. Palavra-chave", height=50, key=f"{chave}_palavra_chave")
    atencao = st.text_area("2. O que me chamou atenção", height=60, key=f"{chave}_atencao")
    diferenca = st.text_area("3. Diferença em relação à minha metodologia", height=60, key=f"{chave}_diferenca")
    duvidas = st.text_area("4. Perguntas ou dúvidas", height=70, key=f"{chave}_duvidas")

    ficha_visita = f"""FICHA DE VISITA
Grupo visitado: {grupo_visitado}

1. Palavra-chave:
{palavra_chave}

2. O que me chamou atenção:
{atencao}

3. Diferença em relação à minha metodologia:
{diferenca}

4. Perguntas ou dúvidas:
{duvidas}
"""
    st.download_button("📥 Baixar Ficha de Visita", data=ficha_visita, file_name=f"ficha_visita_{chave}.txt")

# Executa cada aba
for aba, chave in zip(abas, metodologias):
    descricao, video = abas_textos[chave]
    with aba:
        interface_metodologia(chave.capitalize(), descricao, video, chave)
