🏗️ Nerum Engenharia – Site Profissional

Este é o repositório do site profissional da Nerum Engenharia, desenvolvido para apresentar serviços, projetos executados e oferecer um canal direto para solicitação de orçamentos.
O site foi construído com foco em engenharia hidrossanitária, performance, identidade visual própria e navegação intuitiva.

🔧 Tecnologias Utilizadas

Django 4 / 5 / 6 (dependendo da sua versão)

Python

Bootstrap 5

HTML5 / CSS3

JavaScript

PostgreSQL (opcional)

Sistema de mídia dinâmica para imagens e documentos

📌 Funcionalidades Principais
👤 1. Página Sobre Mim

Apresenta um resumo profissional do engenheiro, incluindo:

Foto de perfil

Biografia resumida

Experiência em projetos hidrossanitários

Links para redes sociais (LinkedIn, GitHub, Instagram)

🏗️ 2. Lista de Projetos

O site possui uma página dedicada aos projetos com:

Cards dinâmicos com imagem, título e descrição curta

Organização visual para fácil navegação

Sistemas de banners e destaques

🖼️ 3. Página Individual do Projeto (Template Próprio)

Cada projeto possui uma página personalizada, contendo:

Galeria de imagens ilimitadas

Descrição detalhada

Informações técnicas

Possibilidade de adicionar vídeos

Layout projetado para engenharia civil (azul escuro, cinza e branco)

💬 4. Campo de Solicitação de Orçamento

Formulário profissional onde o cliente pode enviar:

Nome

Email

Telefone

Descrição do projeto

Anexos (opcional)

As mensagens podem ser enviadas para:

Banco de dados

Email do engenheiro (dependendo da configuração)

🎨 Identidade Visual

O site segue uma identidade visual profissional baseada em:

Azul escuro (engenharia)

Cinza técnico

Branco limpo

Seções com sombras suaves e espaçamento moderno

Design responsivo para celular, tablet e desktop.

🗂️ Estrutura do Projeto
/project_root
    /app
        /templates
        /static
        /models.py
        /views.py
        /urls.py
    /media
        /perfil
        /logo
        /projetos
    settings.py
    urls.py
    requirements.txt
    README.md

🚀 Como Rodar o Projeto Localmente
git clone https://github.com/seuusuario/nerum-engenharia.git
cd nerum-engenharia

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Acesse:
http://127.0.0.1:8000/

