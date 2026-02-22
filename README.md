# Tech Challenge 4 - Data Analytics (Obesidade)

Este projeto é uma aplicação interativa desenvolvida em Streamlit para análise e predição de níveis de obesidade, conforme requisitos do Tech Challenge - Fase 4.

## 📋 Pré-requisitos

Para garantir a compatibilidade de todas as bibliotecas, é necessário utilizar a versão específica do Python:

*   **Python 3.13.x** (Recomendado: 3.13.1 ou superior)

## 🛠️ Configuração do Ambiente

Siga os passos abaixo para configurar o ambiente virtual (`.venv`) e instalar as dependências.

### 1. Criar o Ambiente Virtual
Se você tiver múltiplas versões do Python instaladas, use o comando abaixo para garantir que o ambiente use a versão 3.13:

```bash
# No Windows (usando o launcher 'py')
py -3.13 -m venv .venv

# Ou se o python 3.13 for seu padrão
python -m venv .venv
```

### 2. Ativar o Ambiente Virtual
Escolha o comando de acordo com o seu terminal no Windows:

*   **Git Bash / WSL / Linux:**
    ```bash
    source .venv/Scripts/activate
    ```
*   **PowerShell:**
    ```powershell
    .\.venv\Scripts\Activate.ps1
    ```
*   **Prompt de Comando (CMD):**
    ```cmd
    .\.venv\Scripts\activate.bat
    ```

### 3. Instalar Dependências
Com o ambiente ativado, instale o Streamlit e outras bibliotecas necessárias:

```bash
pip install streamlit
```

## 🚀 Como Rodar o Projeto

Após ativar o ambiente virtual, execute o comando abaixo na pasta raiz do projeto:

```bash
streamlit run home.py
```

O navegador abrirá automaticamente no endereço `http://localhost:8501`.

---