
# Work Health System 🏥💼

O **Work Health System** é um sistema de consulta e gestão de dados técnicos para a medicina do trabalho. Ao contrário de sistemas de prontuários individuais, esta plataforma foca na **padronização de funções laborais**, utilizando a base da **CBO (Classificação Brasileira de Ocupações)** para definir e exibir os requisitos de saúde, riscos e exames necessários para cada cargo de forma genérica e normativa.

## 🌐 Demonstração Online (Acesso Rápido)

O sistema está hospedado e pronto para visualização no link abaixo:

🔗 [**Acesse o Work Health System**](https://healthworksystem.pythonanywhere.com/)

Para explorar as áreas administrativas e de cadastro, utilize as seguintes credenciais:

-   **Usuário:** `admin`
    
-   **Senha:** `admin`
    

## 🚀 Funcionalidades Principais

-   **Catálogo de Funções Laborais:** Listagem detalhada de cargos baseada na estrutura oficial da CBO.
    
-   **Matriz de Exames por Função:** Exibição dos exames médicos recomendados (Admissionais, Periódicos, etc.) para cada ocupação, facilitando a padronização do SESMT.
    
-   **Mapeamento de Riscos:** Identificação genérica de riscos associados a cada CBO.
    

## 🛠️ Tecnologias Utilizadas

-   **Backend:** Python com o framework **Django** (Arquitetura MVT).
    
-   **Frontend:** HTML5, CSS3 e **Bootstrap 5** para uma interface limpa e responsiva.
    
-   **Banco de Dados:** SQLite (Desenvolvimento) / Preparado para instâncias robustas em produção.
    
-   **Autenticação:** Sistema de permissões do Django para gestão do catálogo técnico.
    
-   **Hospedagem:** PythonAnywhere.
    

## 🧠 Lógica e Diferenciais Técnicos

Neste projeto, o foco foi a precisão na estruturação de dados normativos:

1.  **Modelagem Baseada em CBO:** A estrutura de dados foi projetada para suportar a hierarquia das ocupações brasileiras, permitindo que uma função laboral carregue consigo um "pacote" de exames padrão.
    
2.  **Lógica de Relacionamento N-para-N:** Implementação de relações complexas onde múltiplos exames podem pertencer a várias funções, garantindo que o gerenciamento de exames comuns (como o clínico) seja centralizado.
    
3.  **Abstração de Dados Ocupacionais:** Diferente de sistemas de RH comuns, a lógica aqui é puramente técnica e consultiva, focando em "O que a função exige" em vez de "Quem é o funcionário".
    
4.  **Interface Orientada à Consulta:** O frontend foi otimizado para que médicos do trabalho e profissionais de RH encontrem normas de saúde de forma ágil, com layout adaptável para uso em campo via tablets ou celulares.
    

## 🔧 Como rodar o projeto localmente

1.  **Clone o repositório:**
    
    ```
    git clone [https://github.com/Leonardo-P-Monteiro/WORK_HEALTH_SYSTEM.git](https://github.com/Leonardo-P-Monteiro/WORK_HEALTH_SYSTEM.git)
    
    ```
    
2.  **Crie e ative um ambiente virtual:**
    
    ```
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    
    ```
    
3.  **Instale as dependências:**
    
    ```
    pip install -r requirements.txt
    
    ```
    
4.  **Execute as migrações e o servidor:**
    
    ```
    python manage.py migrate
    python manage.py runserver
    
    ```
    

## ✒️ Autor

Desenvolvido por **Leonardo P. Monteiro**. Este projeto demonstra competência no desenvolvimento de sistemas de gestão de dados estruturados e conhecimento aplicado em fluxos de medicina ocupacional.

_Este projeto foi desenvolvido com fins acadêmicos e profissionais para demonstrar proficiência em desenvolvimento FullStack e arquitetura de sistemas baseados em normas técnicas._
