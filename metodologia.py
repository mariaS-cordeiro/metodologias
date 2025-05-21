import streamlit as st
import base64

st.set_page_config(page_title="Ambiente Educacional", layout="wide")
st.title("🎓 Ambiente Educacional: Metodologias de Pesquisa")

abas = st.tabs([
    "📋 Entrevistas",
    "👀 Observação",
    "💬 Grupos Focais",
    "🌍 Etnografia",
    "📑 Documentos",
    "📚 Estudos de Caso",
    "📊 Survey"
])

# Título, descrição e vídeo de cada metodologia
abas_textos = {
    "entrevistas": ("Técnica qualitativa baseada em conversas estruturadas, semiestruturadas ou abertas.",
                    "https://www.youtube.com/watch?v=KqgZeYsbBWU"),
    "observacao": ("Observação sistemática de comportamentos e contextos, podendo ser participante ou não.",
                   "https://www.youtube.com/watch?v=lFweX8gRuvY"),
    "grupos_focais": ("Discussão moderada entre participantes para explorar percepções e significados compartilhados.",
                      "https://www.youtube.com/watch?v=ihTQPBxZpRs"),
    "etnografia": ("Imersão prolongada do pesquisador no campo para compreender práticas culturais.",
                   "https://www.youtube.com/watch?v=zngvQobfaBo"),
    "documentos": ("Análise de textos, arquivos, registros e materiais institucionais ou históricos.",
                   "https://www.youtube.com/watch?v=5MdxS82aEdc"),
    "caso": ("Investigação profunda de um único caso contextualizado.",
             "https://www.youtube.com/watch?v=3gVjUoaeoG0"),
    "survey": ("Técnica quantitativa baseada em questionários estruturados aplicados a grandes amostras.",
               "https://www.youtube.com/watch?v=Ge52zqBLlDs")
}

# Função para gerar link de download de anotações
def gerar_download(anotacoes, nome):
    conteudo = f"Anotações sobre {nome.capitalize()}:\n\n{anotacoes}"
    b64 = base64.b64encode(conteudo.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="anotacoes_{nome}.txt">📥 Baixar anotações</a>'

# Interface única para cada aba
def interface_metodologia(nome, descricao, video_url, chave):
    st.markdown(f"### 🧭 Sobre {nome}")
    st.write(descricao)

    st.markdown("### 📂 Upload de base de dados ou materiais complementares")
    arquivo = st.file_uploader("Envie arquivos (ex: .csv, .pdf, .docx, etc)", key=f"{chave}_upload")
    if arquivo:
        st.success(f"Arquivo carregado: {arquivo.name}")

    st.markdown("### 🎥 Vídeo explicativo")
    st.video(video_url)

    st.markdown("### 📝 Bloco de notas (anotações individuais)")
    anotacoes = st.text_area("Escreva suas definições, conceitos e observações:", height=250, key=f"{chave}_notas")

    # Botão de download só aparece se há texto
    if anotacoes:
        st.markdown(gerar_download(anotacoes, chave), unsafe_allow_html=True)

# Executa a função em cada aba
for aba, (descricao, video) in zip(abas, abas_textos.items()):
    with aba:
        interface_metodologia(aba[2:], descricao, video, aba[2:])
