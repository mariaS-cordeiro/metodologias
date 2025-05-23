import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Metodologia da pesquisa em comunicação digital", layout="wide")
st.title("🎓 Metodologia da pesquisa em comunicação digital")

metodologias = [
    "entrevistas", "observacao", "grupos_focais",
    "etnografia", "documentos", "estudo_de_caso", "survey"
]

abas = st.tabs([
    "📋 Entrevistas", "👀 Observação", "💬 Grupos focais",
    "🌍 Etnografia", "📁 Análise documental", "📚 Estudo de caso", "📊 Survey"
])

abas_textos = {
    "entrevistas": ("Metodologia qualitativa baseada em conversas estruturadas, semiestruturadas ou abertas.", "https://www.youtube.com/watch?v=wuIKfjvH6SM"),
    "observacao": ("Metodologia qualitativa baseada na observação sistemática de comportamentos e contextos.", "https://www.youtube.com/watch?v=LA3HBkH7QJE"),
    "grupos_focais": ("Discussão moderada entre participantes para explorar percepções compartilhadas.", "https://www.youtube.com/watch?v=ihTQPBxZpRs"),
    "etnografia": ("Imersão prolongada no campo para compreender práticas culturais.", "https://www.youtube.com/watch?v=6LIF2kBk1Z0"),
    "documentos": ("Análise de textos, registros e materiais institucionais ou históricos.", "https://www.youtube.com/watch?v=7rX9vBATdzc"),
    "estudo_de_caso": ("Investigação profunda de um único caso contextualizado.", "https://www.youtube.com/watch?v=YwhpLMPX58c"),
    "survey": ("Questionários estruturados aplicados a grandes amostras.", "https://www.youtube.com/watch?v=S9EJKvja96Q")
}

def salvar_ficha(tipo, chave, dados):
    arquivo = f"fichas_{tipo}_{chave}.csv"
    df = pd.read_csv(arquivo) if os.path.exists(arquivo) else pd.DataFrame(columns=dados.keys())
    df = pd.concat([df, pd.DataFrame([dados])], ignore_index=True)
    df.to_csv(arquivo, index=False)

def excluir_linha(tipo, chave, index):
    arquivo = f"fichas_{tipo}_{chave}.csv"
    df = pd.read_csv(arquivo)
    df = df.drop(index)
    df.to_csv(arquivo, index=False)

def interface_metodologia(titulo, descricao, video_url, chave):
    st.markdown(f"### 🧝‍♀️ Sobre {titulo}")
    st.write(descricao)
    st.video(video_url)

    # Ficha de Grupo
    st.markdown("### ✍️ Ficha de Grupo")
    with st.form(f"form_grupo_{chave}"):
        grupo = st.text_input("Componentes do grupo", key=f"{chave}_grupo")
        metodologia = st.text_input("Nome da metodologia", key=f"{chave}_metodologia")
        definicao = st.text_area("1. Definição", height=80, key=f"{chave}_definicao")
        etapas = st.text_area("2. Tipo de dado", height=80, key=f"{chave}_etapas")
        tipo_dado = st.text_area("3. Principais destaques", height=70, key=f"{chave}_tipo_dado")
        vantagens = st.text_area("4. Limitações", height=80, key=f"{chave}_vantagens")
        exemplo = st.text_area("5. Exemplo de aplicação", height=80, key=f"{chave}_exemplo")
        pergunta = st.text_area("6. Pergunta para os visitantes", height=70, key=f"{chave}_pergunta")
        if st.form_submit_button("📂 Salvar Ficha de Grupo"):
            salvar_ficha("grupo", chave, {
                "Componentes": grupo, "Metodologia": metodologia,
                "Definição": definicao, "Tipo de dado": etapas,
                "Destaques": tipo_dado, "Limitações": vantagens,
                "Exemplo": exemplo, "Pergunta": pergunta
            })
            st.success("Ficha de Grupo salva com sucesso!")

    arquivo_grupo = f"fichas_grupo_{chave}.csv"
    if os.path.exists(arquivo_grupo):
        st.markdown("### 📋 Fichas de Grupo salvas")
        df = pd.read_csv(arquivo_grupo)
        st.dataframe(df)
        if len(df) > 0:
            excluir = st.number_input("Índice para excluir ficha de grupo", 0, len(df)-1, key=f"{chave}_excluir_grupo")
            if st.button("🗑️ Excluir grupo", key=f"{chave}_botao_excluir_grupo"):
                excluir_linha("grupo", chave, excluir)
                st.warning("Ficha de grupo excluída.")

    # Ficha de Visitante
    st.markdown("### 👥 Ficha de Visitante")
    with st.form(f"form_visitante_{chave}"):
        metodo = st.text_input("Metodologia observada", key=f"{chave}_metodo_obs")
        grupo_visitante = st.text_input("Grupo visitante", key=f"{chave}_grupo_visitante")
        componentes = st.text_input("Componentes do grupo", key=f"{chave}_componentes")
        palavra = st.text_area("1. Palavra-chave:", height=70, key=f"{chave}_palavra")
        atencao = st.text_area("2. O que me chamou atenção:", height=80, key=f"{chave}_atencao")
        diferenca = st.text_area("3. Diferença em relação à minha metodologia:", height=80, key=f"{chave}_diferenca")
        perguntas = st.text_area("4. Perguntas ou dúvidas:", height=80, key=f"{chave}_duvidas")
        if st.form_submit_button("📂 Salvar Ficha de Visitante"):
            salvar_ficha("visitante", chave, {
                "Metodologia observada": metodo, "Grupo visitante": grupo_visitante,
                "Componentes": componentes, "Palavra-chave": palavra,
                "O que chamou atenção": atencao, "Diferença": diferenca,
                "Perguntas ou dúvidas": perguntas
            })
            st.success("Ficha de Visitante salva com sucesso!")

    arquivo_visitante = f"fichas_visitante_{chave}.csv"
    if os.path.exists(arquivo_visitante):
        st.markdown("### 📋 Fichas de Visitantes salvas")
        df_v = pd.read_csv(arquivo_visitante)
        st.dataframe(df_v)
        if len(df_v) > 0:
            excluir_v = st.number_input("Índice para excluir visitante", 0, len(df_v)-1, key=f"{chave}_excluir_v")
            if st.button("🗑️ Excluir visitante", key=f"{chave}_botao_excluir_v"):
                excluir_linha("visitante", chave, excluir_v)
                st.warning("Ficha de visitante excluída.")

    # Upload de documentos complementares
    st.markdown("### 📌 Upload de Documentos")
    pasta_documentos = f"documentos_{chave}"
    os.makedirs(pasta_documentos, exist_ok=True)

    arquivo = st.file_uploader("Carregar documento (PDF, DOCX, TXT)", key=f"{chave}_uploader")
    if arquivo is not None:
        caminho_arquivo = os.path.join(pasta_documentos, arquivo.name)
        with open(caminho_arquivo, "wb") as f:
            f.write(arquivo.read())
        st.success(f"Documento '{arquivo.name}' salvo com sucesso!")

    documentos_salvos = os.listdir(pasta_documentos)
    if documentos_salvos:
        st.markdown("### 📅 Documentos Salvos")
        for doc in documentos_salvos:
            caminho = os.path.join(pasta_documentos, doc)
            with open(caminho, "rb") as f:
                st.download_button(label=f"📄 Baixar: {doc}", data=f, file_name=doc, mime="application/octet-stream", key=f"{chave}_{doc}")

# Executar interface em cada aba
for aba, chave in zip(abas, metodologias):
    descricao, video = abas_textos[chave]
    with aba:
        interface_metodologia(chave.capitalize(), descricao, video, chave)
