# ⚔️ Jacques de MolAI — Chat Histórico

Uma aplicação interativa desenvolvida para membros da Ordem DeMolay que desejam aprender sobre a
história dos Cavaleiros Templários de forma dinâmica — conversando diretamente com Jacques de Molay,
último Grande Mestre da Ordem, e personagem que serviu de inspiração para a fraternidade DeMolay.

🌐 **Acesse:** [demolai.streamlit.app](https://demolai.streamlit.app)

## 💡 Motivação

Anualmente, no calendário DeMolay, temos um dia chamado "Dia em Memória a Jacques de Molay",
que é um dia em que os Capítulos DeMolays são convidados a enaltecer a história de nosso mártir.
Sem saber exatamente o que fazer nesse dia, surpreendi meus irmãos com esse LLM que simula um chat
com de Molay, que certamente já foi um sonho de todo jovem membro de nossa organização centenária. 

A história dos Cavaleiros Templários é rica e complexa, mas muitas vezes é
distorcida por teorias conspiratórias e ficções populares. Quais eram os ideais
reais da Ordem? O que levou à sua dissolução em 1312? Como foi o julgamento de
Jacques de Molay perante a Inquisição francesa?

Esta aplicação permite explorar essas perguntas em conversa direta com o próprio
Jacques de Molay — reconstruído com base na historiografia consolidada, de Malcolm
Barber a Alain Demurger, e em documentos como o *Processus Contra Templarios* e
a *Regra Latina da Ordem*.

## 🗺️ O que você pode perguntar

- A fundação da Ordem por Hugo de Payens em 1119 em Jerusalém
- A estrutura, regras e rituais documentados dos Templários
- A atuação da Ordem nas Cruzadas e no Oriente Médio medieval
- As tensões entre a Ordem e o rei Filipe IV da França
- Os bastidores do julgamento e as acusações contra os Templários
- A dissolução da Ordem no Concílio de Vienne (1312)
- A execução de Jacques de Molay em 1314 e seu legado

## ⚠️ Limites do personagem

Jacques de Molay viveu entre aproximadamente 1243 e 1314. Sobre eventos, conceitos
ou contextos posteriores à sua época, o personagem não responde — esse limite é
intencional e faz parte da proposta histórica da aplicação.

## 📚 Aviso educacional

Esta aplicação foi desenvolvida **exclusivamente para fins educacionais**, como
um ponto de partida para o estudo da história dos Cavaleiros Templários.

**O personagem é gerado por inteligência artificial e está sujeito a erros.**
Modelos de linguagem podem cometer imprecisões históricas, confundir datas ou
apresentar interpretações parciais. Por isso:

- Trate as respostas como um ponto de partida, não como fonte definitiva
- Verifique informações importantes em obras acadêmicas
- Em caso de dúvida, consulte historiadores como Malcolm Barber (*The New
  Knighthood*) e Alain Demurger (*Os Templários*)

A inteligência artificial não substitui o estudo — ela pode torná-lo mais
curioso e envolvente.

## 🛠️ Tecnologias utilizadas

- [Streamlit](https://streamlit.io/) — interface do chat
- [Groq API](https://console.groq.com/) — inferência do modelo de linguagem
- [Llama 3.3 70B](https://groq.com/) — modelo de linguagem utilizado
- [Sora](https://openai.com/sora) — geração da imagem de fundo
- Python 3.11+

## 🚀 Como rodar localmente

**1. Clone o repositório**
```bash
git clone https://github.com/felipe-roch/DeMolAI.git
cd DeMolAI
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Configure sua chave da Groq**

Crie o arquivo `.streamlit/secrets.toml` na raiz do projeto:
```toml
GROQ_API_KEY = "sua_chave_aqui"
```

**4. Rode a aplicação**
```bash
streamlit run DeMolAI.py
```

## 🔑 Deploy no Streamlit Cloud

Na tela de configuração do app, acesse **Advanced settings → Secrets** e adicione:
```toml
GROQ_API_KEY = "sua_chave_aqui"
```

## Autor

Felipe da Rocha  
[LinkedIn](https://www.linkedin.com/in/felipedarochaferreira/) · [GitHub](http://github.com/felipe-roch)