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

# Dicionário de perguntas
perguntas = {
    "entrevistas": {
        "definicao": {
            "pergunta": "Qual das alternativas melhor define a técnica de entrevistas?",
            "opcoes": [
                "Observação direta de comportamentos",
                "Condução de questionários com escala numérica",
                "Conversa estruturada ou semiestruturada com participantes",
                "Coleta de documentos oficiais"
            ],
            "correta": 2
        },
        "exemplo": {
            "pergunta": "Qual exemplo representa uma entrevista semiestruturada?",
            "opcoes": [
                "Um pesquisador assiste a uma reunião comunitária sem intervir",
                "Um roteiro com perguntas abertas conduzido com um morador",
                "Uma planilha com respostas a perguntas fechadas",
                "Análise de postagens em redes sociais"
            ],
            "correta": 1
        }
    },
    "observacao": {
        "definicao": {
            "pergunta": "O que caracteriza a observação participante?",
            "opcoes": [
                "Coleta de depoimentos por e-mail",
                "Interação direta do pesquisador com o ambiente observado",
                "Distribuição de formulários digitais",
                "Entrevista coletiva em grupos organizados"
            ],
            "correta": 1
        },
        "exemplo": {
            "pergunta": "Qual exemplo representa observação estruturada?",
            "opcoes": [
                "O pesquisador observa livremente uma praça pública",
                "Leitura de artigos acadêmicos sobre urbanismo",
                "Análise de comentários em redes sociais",
                "Uso de um roteiro fixo para observar alunos em sala de aula"
            ],
            "correta": 3
        }
    },
    "grupos_focais": {
        "definicao": {
            "pergunta": "Para que servem os grupos focais?",
            "opcoes": [
                "Entrevistar uma única pessoa",
                "Observar comportamentos não verbais",
                "Explorar opiniões e percepções coletivas sobre um tema",
                "Analisar dados estatísticos"
            ],
            "correta": 2
        },
        "exemplo": {
            "pergunta": "Qual situação representa um grupo focal?",
            "opcoes": [
                "Análise de um discurso presidencial",
                "Entrevista com um único morador",
                "Encontro moderado com 6 pessoas discutindo saneamento",
                "Pesquisa com formulário online"
            ],
            "correta": 2
        }
    },
    "etnografia": {
        "definicao": {
            "pergunta": "Qual é o foco central da etnografia?",
            "opcoes": [
                "Estatísticas populacionais",
                "Imersão prolongada para compreender significados culturais",
                "Elaboração de roteiros estruturados",
                "Coleta de dados numéricos por amostragem"
            ],
            "correta": 1
        },
        "exemplo": {
            "pergunta": "Qual exemplo descreve uma prática etnográfica?",
            "opcoes": [
                "Aplicação de questionários em massa",
                "Levantamento de preços no comércio local",
                "Participação do pesquisador em rituais de uma comunidade",
                "Análise de dados secundários em artigos"
            ],
            "correta": 2
        }
    },
    "documentos": {
        "definicao": {
            "pergunta": "O que é analisado na pesquisa documental?",
            "opcoes": [
                "Comportamentos espontâneos em público",
                "Narrativas orais em entrevistas",
                "Textos, imagens, arquivos e registros",
                "Códigos-fonte de programas"
            ],
            "correta": 2
        },
        "exemplo": {
            "pergunta": "Qual dos itens abaixo pode ser uma fonte documental?",
            "opcoes": [
                "Uma conversa informal no mercado",
                "Transcrição de entrevista gravada",
                "Publicação oficial do governo sobre política pública",
                "Levantamento de atitudes em survey"
            ],
            "correta": 2
        }
    },
    "caso": {
        "definicao": {
            "pergunta": "O estudo de caso é caracterizado por:",
            "opcoes": [
                "Aplicação de testes laboratoriais",
                "Investigação ampla com milhares de pessoas",
                "Análise aprofundada de um fenômeno em contexto real",
                "Estudo de apenas dados estatísticos"
            ],
            "correta": 2
        },
        "exemplo": {
            "pergunta": "Qual exemplo representa um estudo de caso?",
            "opcoes": [
                "Análise de uma escola que implantou hortas urbanas",
                "Pesquisa nacional sobre o consumo de alimentos",
                "Análise de 5000 comentários no Twitter",
                "Avaliação de censo agropecuário"
            ],
            "correta": 0
        }
    },
    "survey": {
        "definicao": {
            "pergunta": "O survey é uma técnica:",
            "opcoes": [
                "Quantitativa baseada em questionários estruturados",
                "Baseada em observação etnográfica",
                "Focada em entrevistas abertas",
                "Exclusiva de estudos históricos"
            ],
            "correta": 0
        },
        "exemplo": {
            "pergunta": "Qual situação representa um survey?",
            "opcoes": [
                "Levantamento de opiniões com questionário aplicado a 500 pessoas",
                "Análise de símbolos em músicas populares",
                "Entrevista aprofundada com um líder comunitário",
                "Discussão moderada com um pequeno grupo"
            ],
            "correta": 0
        }
    }
}

# Vídeos e descrições
abas_textos = {
    "entrevistas": ("Técnica qualitativa baseada em conversas estruturadas, semiestruturadas ou abertas.",
                    "https://www.youtube.com/watch?v=KqgZeYsbBWU"),
    "observacao": ("Observação sistemática de comportamentos e contextos, podendo ser participante ou não.",
                   "https://www.youtube.com/watch?v=lFweX8gRuvY"),
    "grupos_focais": ("Discussão moderada entre participantes para explorar percepções e significados compartilhados.",
                      "https://www.youtube.com/watch?v=tgkY9dIfF9I"),
    "etnografia": ("Imersão prolongada do pesquisador no campo para compreender práticas culturais.",
                   "https://www.youtube.com/watch?v=zngvQobfaBo"),
    "documentos": ("Análise de textos, arquivos, registros e materiais institucionais ou históricos.",
                   "https://www.youtube.com/watch?v=5MdxS82aEdc"),
    "caso": ("Investigação profunda de um único caso contextualizado.",
             "https://www.youtube.com/watch?v=3gVjUoaeoG0"),
    "survey": ("Técnica quantitativa baseada em questionários estruturados aplicados a grandes amostras.",
               "https://www.youtube.com/watch?v=Ge52zqBLlDs")
}

# Funções auxiliares
def gerar_download(anotacoes, nome):
    conteudo = f"Anotações sobre {nome.capitalize()}:\n\n{anotacoes}"
    b64 = base64.b64encode(conteudo.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="anotacoes_{nome}.txt">📥 Baixar anotações</a>'

def interface_metodologia(nome, descricao, video_url, chave):
    st.markdown(f"### 🧭 Sobre {nome}")
    st.write(descricao)

    st.markdown("### 📂 Upload de base de dados")
    arquivo = st.file_uploader("Envie arquivos (ex: .csv, .pdf, .docx, etc)", key=f"{chave}_upload")
    if arquivo:
        st.success(f"Arquivo carregado: {arquivo.name}")

    st.markdown("### 🎥 Vídeo explicativo")
    st.video(video_url)

    st.markdown("### 📝 Bloco de notas")
    anotacoes = st.text_area("Anotações individuais:", height=200, key=f"{chave}_notas")
    if anotacoes:
        st.markdown(gerar_download(anotacoes, chave), unsafe_allow_html=True)

    if chave in perguntas:
        st.markdown("### ❓ Questões de múltipla escolha")
        for tipo, conteudo in perguntas[chave].items():
            st.markdown(f"**{conteudo['pergunta']}**")
            resposta = st.radio("", conteudo["opcoes"], key=f"{chave}_{tipo}")
            if conteudo["opcoes"].index(resposta) == conteudo["correta"]:
                st.success("✅ Resposta correta!")
            else:
                st.error("❌ Resposta incorreta. Tente novamente.")

# Criação das abas
for aba, (descricao, video) in zip(abas, abas_textos.items()):
    with aba:
        interface_metodologia(aba[2:], descricao, video, aba[2:])
