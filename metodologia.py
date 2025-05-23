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
    "🌍 Etnografia", "📑 Análise documental", "📚 Estudo de caso", "📊 Survey"
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
    "estudo_de_caso": (
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

def excluir_linha(arquivo, index):
    df = pd.read_csv(arquivo)
    df = df.drop(index)
    df.to_csv(arquivo, index=False)

def interface_metodologia(titulo, descricao, video_url, chave):
    st.markdown(f"### 🧭 Sobre {titulo}")
    st.write(descricao)

    st.markdown("### 🎥 Vídeo explicativo")
    st.video(video_url)

    st.markdown("### ✍️ Ficha de Grupo")
    with st.form(f"form_{chave}"):
        grupo = st.text_input("Componentes do grupo", key=f"{chave}_grupo")
        metodologia = st.text_input("Nome da metodologia", key=f"{chave}_metodologia")
        definicao = st.text_area("1. Definição", height=80, key=f"{chave}_definicao")
        etapas = st.text_area("2. Tipo de dado", height=80, key=f"{chave}_etapas")
        tipo_dado = st.text_area("3. Principais destaques", height=70, key=f"{chave}_tipo_dado")
        vantagens = st.text_area("4. Limitações", height=80, key=f"{chave}_vantagens")
        exemplo = st.text_area("5. Exemplo de aplicação", height=80, key=f"{chave}_exemplo")
        pergunta = st.text_area("6. Pergunta para os visitantes", height=70, key=f"{chave}_pergunta")

        submitted = st.form_submit_button("💾 Salvar Ficha de Grupo")
        if submitted:
            dados = {
                "Componentes do grupo": grupo,
                "Nome da metodologia": metodologia,
                "Definição": definicao,
                "Tipo de dado": etapas,
                "Principais destaques": tipo_dado,
                "Limitações": vantagens,
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

        if len(df) > 0:
            excluir = st.number_input(
                "Digite o índice da linha que deseja excluir",
                min_value=0,
                max_value=len(df) - 1,
                step=1,
                key=f"{chave}_excluir"
            )
            if st.button("🗑️ Excluir linha selecionada", key=f"{chave}_botao_excluir"):
                excluir_linha(arquivo, excluir)
                st.warning("Linha excluída. Recarregue a página para atualizar a tabela.")
        else:
            st.info("Nenhuma ficha cadastrada para excluir.")

# Executa interface em cada aba
for aba, chave in zip(abas, metodologias):
    descricao, video = abas_textos[chave]
    with aba:
        interface_metodologia(chave.capitalize(), descricao, video, chave)

import streamlit as st
import pandas as pd
import os

def salvar_ficha_visitante(chave, dados):
    arquivo = f"fichas_visitante_{chave}.csv"
    if os.path.exists(arquivo):
        df = pd.read_csv(arquivo)
    else:
        df = pd.DataFrame(columns=dados.keys())
    df = pd.concat([df, pd.DataFrame([dados])], ignore_index=True)
    df.to_csv(arquivo, index=False)

def excluir_linha_visitante(arquivo, index):
    df = pd.read_csv(arquivo)
    df = df.drop(index)
    df.to_csv(arquivo, index=False)

def ficha_visitante_interface(chave):
    st.markdown("### 👥 Ficha de Visitante")
    with st.form(f"form_visitante_{chave}"):
        metodologia = st.text_input("Metodologia observada", key=f"{chave}_metodologia_v")
        grupo_visitante = st.text_input("Grupo visitante", key=f"{chave}_grupo_visitante")
        componentes = st.text_input("Componentes do grupo", key=f"{chave}_componentes")
        palavra_chave = st.text_area("1. Palavra-chave:", height=70, key=f"{chave}_palavra")
        atencao = st.text_area("2. O que me chamou atenção:", height=80, key=f"{chave}_atencao")
        diferenca = st.text_area("3. Diferença em relação à minha metodologia:", height=80, key=f"{chave}_diferenca")
        perguntas = st.text_area("4. Perguntas ou dúvidas:", height=80, key=f"{chave}_duvidas")

        submitted = st.form_submit_button("💾 Salvar Ficha de Visitante")
        if submitted:
            dados = {
                "Metodologia observada": metodologia,
                "Grupo visitante": grupo_visitante,
                "Componentes": componentes,
                "Palavra-chave": palavra_chave,
                "O que chamou atenção": atencao,
                "Diferença": diferenca,
                "Perguntas ou dúvidas": perguntas
            }
            salvar_ficha_visitante(chave, dados)
            st.success("Ficha de Visitante salva com sucesso!")

    # Visualização e exclusão
    arquivo = f"fichas_visitante_{chave}.csv"
    if os.path.exists(arquivo):
        st.markdown("### 📋 Fichas de Visitantes salvas")
        df = pd.read_csv(arquivo)
        st.dataframe(df)

        if len(df) > 0:
            excluir = st.number_input(
                "Índice da ficha de visitante que deseja excluir",
                min_value=0,
                max_value=len(df) - 1,
                step=1,
                key=f"{chave}_excluir_visitante"
            )
            if st.button("🗑️ Excluir visitante selecionado", key=f"{chave}_botao_excluir_visitante"):
                excluir_linha_visitante(arquivo, excluir)
                st.warning("Linha excluída. Recarregue a página para atualizar a tabela.")
        else:
            st.info("Nenhuma ficha de visitante cadastrada para excluir.")

