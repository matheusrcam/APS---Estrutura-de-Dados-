# 📘 APS – Estrutura de Dados

### Projeto: Painel Interativo de Ordenação e Análise de Dados

---

## 🎯 **Objetivo**

Este projeto foi desenvolvido como parte da APS da disciplina **Estrutura de Dados**.
O objetivo é **analisar o desempenho do algoritmo Bubble Sort** aplicado a **dados reais de queimadas do INPE**, permitindo compreender, de forma prática, como a **complexidade O(n²)** impacta o tempo de execução e o número de operações.

Além disso, o projeto visa unir **Computação e Sustentabilidade**, mostrando como algoritmos e análise de dados podem ser aplicados em **problemas ambientais reais**.

---

## ⚙️ **Como o sistema funciona**

O sistema é uma aplicação interativa desenvolvida com **Streamlit**.
Ele permite que o usuário envie um arquivo CSV (como o de focos de queimadas), escolha o **critério de ordenação** e visualize:

* Dados ordenados de forma crescente
* Número de **comparações** e **trocas** realizadas
* Opção de **baixar o arquivo ordenado** novamente

O algoritmo implementado é o **Bubble Sort**, escolhido por ser simples, didático e ideal para demonstrar visualmente o impacto da complexidade O(n²).

---

## 🧠 **Algoritmo Utilizado – Bubble Sort**

O **Bubble Sort** percorre repetidamente a lista de dados, comparando dois elementos adjacentes e trocando suas posições se estiverem fora de ordem.
Após cada passagem, o maior valor “sobe” para o final da lista, como uma bolha na água.
Esse processo se repete até que toda a lista esteja ordenada.

**Complexidade:** O(n²)
**Vantagem:** Fácil de entender e visualizar o processo de ordenação.
**Limitação:** Ineficiente para grandes volumes de dados.

---

## 🧩 **Tecnologias e Bibliotecas**

* **Python 3.11+**
* **Pandas** → Manipulação de dados CSV
* **Matplotlib / Plotly** → Visualização de gráficos
* **Streamlit** → Interface gráfica interativa
* **scikit-learn** → Base para futuras análises e regressões

---

## 🚀 **Como Executar o Projeto**

### 1️⃣ Clonar o repositório ou baixar os arquivos:

```bash
git clone https://github.com/seuusuario/aps-estrutura-dados.git
cd aps-estrutura-dados
```

### 2️⃣ Criar ambiente virtual e instalar dependências:

```bash
python -m venv .venv
# Ativar o ambiente virtual
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux / Mac

pip install -r requirements.txt
```

### 3️⃣ Executar o sistema:

```bash
streamlit run analise.py
```

### 4️⃣ Usar a interface:

1. Envie um arquivo CSV (ex: `focos_total_limpo.csv`);
2. Escolha o campo para ordenação (`bioma`, `data_pas` ou `municipio`);
3. Veja os dados ordenados e o número de comparações e trocas;
4. Baixe o arquivo ordenado novamente.

---

## 🧱 **Estrutura do Projeto**

```
📦 APS_Estrutura_Dados
 ┣ 📜 analise.py              # Código principal com interface e Bubble Sort
 ┣ 📜 focos_total_limpo.csv   # Base de dados de exemplo (INPE)
 ┣ 📜 README.md               # Documentação do projeto
 ┗ 📂 .venv                   # Ambiente virtual (opcional)
```

---

## 📊 **Resultados Esperados**

* Exibição dos dados ordenados de forma interativa;
* Contagem do número de **comparações** e **trocas** realizadas;
* Compreensão prática da **ineficiência do Bubble Sort** em grandes volumes;
* Possibilidade de futuras expansões (ex: QuickSort, MergeSort, Timsort ou Machine Learning).

---

## 🧾 **Licença**

Este projeto é de uso acadêmico e educacional.
Sinta-se à vontade para estudar, modificar e evoluir o código com fins didáticos.
