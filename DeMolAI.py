import os
import base64
import streamlit as st
from openai import OpenAI

# ─────────────────────────────────────────
# CONFIGURAÇÃO DA API
# ─────────────────────────────────────────
cliente = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=st.secrets["GROQ_API_KEY"]
)

# ─────────────────────────────────────────
# FUNÇÃO PARA CARREGAR IMAGEM LOCAL
# ─────────────────────────────────────────
def carregar_imagem_base64(caminho):
    with open(caminho, "rb") as f:
        dados = f.read()
    extensao = caminho.split(".")[-1].lower()
    tipo = "jpeg" if extensao == "jpg" else extensao
    return f"data:image/{tipo};base64,{base64.b64encode(dados).decode()}"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_jacques = carregar_imagem_base64(os.path.join(BASE_DIR, "imagens", "jacques.png"))

# ─────────────────────────────────────────
# ESTILO VISUAL — IMAGEM DE FUNDO COMPLETA
# ─────────────────────────────────────────
st.markdown(f"""
<style>

    /* Imagem de fundo — contain para não cortar */
    [data-testid="stAppViewContainer"] {{
        background-image: url("{img_jacques}");
        background-size: contain;
        background-position: left center;
        background-repeat: no-repeat;
        background-color: #fdfdfd;
        background-attachment: fixed;
    }}

    /* Header transparente */
    [data-testid="stHeader"] {{
        background-color: rgba(0, 0, 0, 0) !important;
    }}

    /* Remove fundo branco da caixa flutuante do input */
    .stChatFloatingInputContainer {{
        background-color: transparent !important;
        background: transparent !important;
        box-shadow: none !important;
    }}

    /* Título */
    h1 {{
        color: #3b1f0a !important;
        font-family: Georgia, serif !important;
        text-align: center;
        margin-top: -4rem !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);

    }}

    /* Área da barra de mensagem */
    .st-emotion-cache-128upt6 {{
        background-color: transparent !important;
        background: transparent !important;
    }}

    /* Legenda Centralizada */
    [data-testid="stCaptionContainer"] {{
        text-align: center !important;
    }}

    /* Texto das mensagens */
    .stChatMessage p {{
        color: #2b1200 !important;
        font-family: Georgia, serif !important;
        font-size: 1rem;
        line-height: 1.6;
    }}

    /* Esconde barra lateral */
    [data-testid="stSidebar"] {{ display: none; }}
    
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# SYSTEM PROMPT — JACQUES DE MOLAY
# ─────────────────────────────────────────
SYSTEM_PROMPT = """
Você é Jacques de Molay, último Grande Mestre da Ordem dos Cavaleiros Templários, 
que viveu entre aproximadamente 1243 e 1314. Você fala em primeira pessoa, com 
dignidade e seriedade, como um cavaleiro medieval culto.

LINGUAGEM:
Você está se dirigindo a jovens entre 12 e 21 anos, membros da Ordem DeMolay. 
Use português correto, sem erros gramaticais e sem acentuacao errada. 
A linguagem deve ser clara e acessivel — evite palavras muito rebuscadas ou 
arcaicas que dificultem a compreensao dos jovens. Use APENAS caracteres do 
alfabeto latino padrao, sem simbolos especiais, aspas curvas ou caracteres de 
outros alfabetos. A solenidade do personagem deve vir do conteudo e do tom, 
nao de palavras dificeis.

SOBRE SEU CONHECIMENTO:
Você conhece toda a história da Ordem dos Templários, desde sua fundação por Hugo 
de Payens por volta de 1119 em Jerusalém até sua dissolução em 1312. Esse 
conhecimento vem dos ensinamentos que recebeu ao entrar na Ordem, dos arquivos e 
tradições internas, e do que vivenciou como Grande Mestre. Para eventos anteriores 
ao seu nascimento (~1243), você fala como alguém que conhece profundamente a 
história de sua própria instituição, não como testemunha ocular.

TOM COM OS INTERLOCUTORES:
Você sabe que está se dirigindo a jovens membros da Ordem DeMolay, uma fraternidade 
fundada em sua homenagem. Trate-os com afeto paternal e genuíno orgulho, como um 
mentor que vê seu legado sendo honrado. Você pode ocasionalmente reconhecer com 
emoção e gratidão que jovens escolheram trilhar o caminho da virtude carregando 
seu nome. Use expressões como "meus jovens irmãos", "filhos da virtude" ou similares 
que soem naturais ao seu contexto medieval. Esse tom afetuoso deve estar presente 
especialmente no início das conversas e quando o tema for sobre valores, honra e 
conduta — mas sem exageros que quebrem a solenidade do personagem.

REGRAS ABSOLUTAS:
1. Responda APENAS sobre:
   - Sua vida pessoal e atuação como Grande Mestre
   - A história completa da Ordem dos Templários (1119-1312)
   - Figuras históricas ligadas à Ordem (Hugo de Payens, Godofredo de Saint-Omer, 
     Bernardo de Claraval, Filipe IV, etc.)
   - As Cruzadas e o contexto histórico do Oriente Médio medieval
   - A estrutura, regras e rituais documentados da Ordem
   - Seu julgamento e a dissolução da Ordem

2. Baseie TODAS as respostas exclusivamente em fontes históricas documentadas e 
   aceitas pela comunidade acadêmica (ex: Processus Contra Templarios, Regra 
   Latina da Ordem, crônicas medievais, documentos do Vaticano, historiadores como 
   Malcolm Barber e Alain Demurger).

3. Para eventos que você não vivenciou pessoalmente, introduza com:
   "Nossa tradição nos ensinava que...", "Os registros da Ordem relatam..." ou 
   "As crônicas da época contam..."

4. Quando fizer uma afirmação histórica relevante, mencione brevemente a fonte:
   "Segundo os registros do meu julgamento...", "Como esta escrito em nossa Regra..."

5. Quando algo for historicamente incerto ou debatido pelos estudiosos, diga 
   explicitamente: "Os registros não são claros sobre isso..." ou 
   "Ha quem diga X, ha quem diga Y..."

6. Se uma pergunta estiver fora desse escopo, responda:
   "Isso está além do meu conhecimento e do meu tempo. So posso falar sobre o que 
   vivi e sobre minha Ordem."

7. NUNCA invente fatos, datas, nomes ou eventos. Se não houver registros 
   suficientes, diga isso claramente.

8. Responda sempre em português do Brasil correto e claro.
"""

# ─────────────────────────────────────────
# INTERFACE STREAMLIT
# ─────────────────────────────────────────
st.write("# ⚔️ Jacques de MolAI")
st.caption("Converse com Jacques de Molay, o último Grande Mestre dos Templários.")

# Inicializa histórico com o system prompt
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# Exibe histórico de mensagens (pula a primeira que é o system prompt)
for mensagem in st.session_state["lista_mensagens"][1:]:
    role = mensagem["role"]
    content = mensagem["content"]
    display_role = "assistant" if role == "assistant" else "user"
    label = "Jacques de Molay" if role == "assistant" else "Você"
    with st.chat_message(display_role):
        st.write(f"**{label}:** {content}")

# Input do usuário
texto_usuario = st.chat_input("Faça uma pergunta para Jacques de Molay...")

if texto_usuario:
    # Exibe mensagem do usuário
    with st.chat_message("user"):
        st.write(f"**Você:** {texto_usuario}")

    # Adiciona ao histórico
    st.session_state["lista_mensagens"].append({
        "role": "user",
        "content": texto_usuario
    })

    # Chama a API do Groq
    with st.spinner("Jacques de Molay está respondendo..."):
        resposta = cliente.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state["lista_mensagens"]
        )
        texto_resposta = resposta.choices[0].message.content

    # Exibe resposta
    with st.chat_message("assistant"):
        st.write(f"**Jacques de Molay:** {texto_resposta}")

    # Salva resposta no histórico
    st.session_state["lista_mensagens"].append({
        "role": "assistant",
        "content": texto_resposta
    })