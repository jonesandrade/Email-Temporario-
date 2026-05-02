# Email-Temporario-
Este projeto é um sistema de E-mail Temporário desenvolvido para demonstrar habilidades em desenvolvimento backend, manipulação de bancos de dados relacionais e integração de serviços em nuvem. A aplicação permite a geração de endereços de e-mail fictícios e a visualização de mensagens em tempo real.

Tecnologias Utilizadas
Linguagem: Python 3.x

Framework Web: Flask (Micro-framework)

Banco de Dados: SQLite (Persistência local de mensagens)

Servidor Web: Gunicorn (WSGI para produção)

Hospedagem: Render (PaaS)

Interface: HTML5, CSS3 (Dark Mode) e JavaScript Vanilla

Arquitetura e Funcionalidades
O sistema foi desenhado seguindo princípios de arquitetura RESTful, focado em automação e processamento de dados:

Geração Dinâmica: Criação de identidades únicas para caixas de entrada.

Polling em Tempo Real: O frontend consulta o servidor automaticamente a cada 4 segundos para buscar novas mensagens sem recarregar a página.

Endpoint de Webhook: Rota /enviar preparada para receber requisições POST de serviços externos ou simulações internas.

Banco de Dados: Armazenamento seguro de remetente, assunto e corpo da mensagem utilizando SQLite.

Como Executar o Projeto
Para rodar este projeto localmente para testes:

Clone o repositório:

Bash
git clone https://github.com/seu-usuario/seu-repositorio.git
Instale as dependências:

Bash
pip install -r requirements.txt
Inicie o servidor:

Bash
python app.py
Acesse http://localhost:5000 no seu navegador.

Roadmap e Escalabilidade
Atualmente, o projeto opera como uma demonstração técnica. Para uso em ambiente de produção (uso ativo), a infraestrutura está preparada para:

Domínio Próprio: Integração com domínios personalizados via registros MX ou serviços de Webhook (ex: CloudMailin).

Dockerização: Criação de imagens Docker para orquestração em clusters (alinhado com práticas de DevOps).

Segurança: Implementação de limpeza automática de banco de dados (auto-delete) após X minutos.

Autor
Felipe

Tecnólogo em TI

Foco em Automação, Docker e Integrações de API
