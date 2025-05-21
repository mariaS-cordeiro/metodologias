import streamlit as st

st.set_page_config(page_title="Ambiente Educacional - Metodologias de Pesquisa", layout="wide")
st.title("🎓 Ambiente Educacional: Metodologias de Pesquisa")

abas = st.tabs([
    "📋 Entrevistas",
    "👀 Observação",
    "💬 Grupos Focais",
    "🌍 Etnografia",
    "📑 Análise de Documentos",
    "📚 Estudos de Caso",
    "📊 Survey"
])

def interface_metodologia(nome, descricao, video_url, anotacoes_key):
    st.markdown(f"### 🧭 Sobre {nome}")
    st.write(descricao)

    st.markdown("### 📂 Upload de base de dados ou materiais complementares")
    arquivo = st.file_uploader("Envie arquivos (ex: .csv, .pdf, .docx, etc)", key=f"{anotacoes_key}_upload")

    if arquivo:
        st.success(f"Arquivo carregado: {arquivo.name}")

    st.markdown("### 🎥 Vídeo explicativo")
    st.video(video_url)

    st.markdown("### 📝 Bloco de notas (espaço para anotações individuais)")
    anotacoes = st.text_area("Escreva suas definições, conceitos e observações:", height=250, key=anotacoes_key)

    if anotacoes:
        st.success("Suas anotações foram registradas localmente (não são salvas no servidor).")

# Abas com conteúdos individuais
with abas[0]:
    interface_metodologia(
        "Entrevistas",
        "As entrevistas são instrumentos centrais na pesquisa qualitativa. Podem ser estruturadas, semiestruturadas ou abertas.",
        "https://www.youtube.com/watch?v=KqgZeYsbBWU",
        "entrevistas"
    )

with abas[1]:
    interface_metodologia(
        "Observação",
        "A observação pode ser participante ou não, estruturada ou livre. É usada para captar comportamentos e interações no campo.",
        "https://www.youtube.com/watch?v=lFweX8gRuvY",
        "observacao"
    )

with abas[2]:
    interface_metodologia(
        "Grupos Focais",
        "Técnica que reúne participantes para debater um tema com moderação. Ideal para explorar percepções compartilhadas e divergentes.",
        "https://www.youtube.com/watch?v=tgkY9dIfF9I",
        "grupos_focais"
    )

with abas[3]:
    interface_metodologia(
        "Etnografia",
        "A etnografia exige imersão no campo e busca entender práticas e significados a partir do olhar dos participantes.",
        "https://www.youtube.com/watch?v=zngvQobfaBo",
        "etnografia"
    )

with abas[4]:
    interface_metodologia(
        "Análise de Documentos",
        "A análise documental permite examinar registros, textos, mídias e dados históricos como fonte para a pesquisa.",
        "https://www.youtube.com/watch?v=5MdxS82aEdc",
        "documentos"
    )

with abas[5]:
    interface_metodologia(
        "Estudo de Caso",
        "O estudo de caso aprofunda a análise de um fenômeno específico em seu contexto, com múltiplas fontes de evidência.",
        "https://www.youtube.com/watch?v=3gVjUoaeoG0",
        "caso"
    )

with abas[6]:
    interface_metodologia(
        "Survey",
        "O survey é uma técnica quantitativa baseada em questionários estruturados aplicados a grandes amostras.",
        "https://www.youtube.com/watch?v=Ge52zqBLlDs",
        "survey"
    )
