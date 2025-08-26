# Python Learning Modules and Quiz Data
MODULES = {
    1: {
        'title': 'Fundamentos da Programação em Python',
        'description': 'Base para quem está começando a programar, com foco em lógica e sintaxe.',
        'video_url': '',  # Admin can set this
        'content': '''
        <h3>🧱 Módulo 1 – Fundamentos da Programação em Python</h3>
        <p><strong>Base para quem está começando a programar, com foco em lógica e sintaxe.</strong></p>
        
        <h4>📚 Conteúdo do Módulo:</h4>
        <ul>
            <li><strong>Instalação do Python e VSCode:</strong> Configurando seu ambiente de desenvolvimento</li>
            <li><strong>Variáveis, Tipos de Dados e Entrada/Saída:</strong> Fundamentos básicos</li>
            <li><strong>Operadores:</strong> Aritméticos, Relacionais e Lógicos</li>
            <li><strong>Estruturas Condicionais:</strong> if, elif, else</li>
            <li><strong>Laços de Repetição:</strong> while e for</li>
            <li><strong>Estruturas de Dados:</strong> Listas, Tuplas, Dicionários e Conjuntos</li>
            <li><strong>Funções e Escopo:</strong> Criando código reutilizável</li>
            <li><strong>Módulos e Pacotes:</strong> Organizando seu código</li>
            <li><strong>Tratamento de Erros:</strong> Try/Except</li>
        </ul>
        
        <h4>🎯 Objetivos de Aprendizagem:</h4>
        <p>Ao final deste módulo, você será capaz de:</p>
        <ul>
            <li>Entender a sintaxe básica do Python</li>
            <li>Criar programas simples usando variáveis e estruturas de controle</li>
            <li>Trabalhar com diferentes tipos de dados</li>
            <li>Criar e usar funções básicas</li>
        </ul>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual é a extensão padrão para arquivos Python?',
                'options': ['.python', '.py', '.pt', '.pyt'],
                'correct_answer': '.py'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como você declara uma variável em Python?',
                'options': [
                    'var nome = "João"',
                    'String nome = "João"',
                    'nome = "João"',
                    'declare nome = "João"'
                ],
                'correct_answer': 'nome = "João"'
            },
            {
                'type': 'open_answer',
                'question': 'Explique a diferença entre uma lista e uma tupla em Python.',
                'correct_keywords': ['mutável', 'imutável', 'modificar', 'alteração', 'colchetes', 'parênteses']
            }
        ]
    },
    2: {
        'title': 'Algoritmos e Problemas Reais com Python',
        'description': 'Prática com desafios e pequenos projetos do mundo real.',
        'video_url': '',
        'content': '''
        <h3>🧪 Módulo 2 – Algoritmos e Problemas Reais com Python</h3>
        <p><strong>Prática com desafios e pequenos projetos do mundo real.</strong></p>
        
        <h4>🚀 Projetos Práticos:</h4>
        <ul>
            <li><strong>Automatizando Tarefas Simples:</strong> Scripts úteis do dia a dia</li>
            <li><strong>Calculadora CLI:</strong> Interface de linha de comando</li>
            <li><strong>Jogo da Adivinhação:</strong> Lógica de programação divertida</li>
            <li><strong>Gerador de Senhas:</strong> Criando senhas seguras</li>
            <li><strong>Agenda de Contatos:</strong> Manipulação de arquivos .txt</li>
            <li><strong>Conversor de Moedas:</strong> Integração com APIs</li>
            <li><strong>CRUD de Produtos:</strong> Operações básicas em listas</li>
            <li><strong>Sistema Bancário Simples:</strong> Projeto integrador</li>
        </ul>
        
        <h4>🎯 Habilidades Desenvolvidas:</h4>
        <ul>
            <li>Resolução de problemas algorítmicos</li>
            <li>Manipulação de dados e estruturas</li>
            <li>Criação de interfaces simples</li>
            <li>Integração com APIs externas</li>
        </ul>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual função Python é usada para gerar números aleatórios?',
                'options': ['random()', 'randint()', 'choice()', 'Todas as anteriores'],
                'correct_answer': 'Todas as anteriores'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como você converte uma string para inteiro em Python?',
                'options': ['integer(string)', 'int(string)', 'convert(string)', 'parse(string)'],
                'correct_answer': 'int(string)'
            },
            {
                'type': 'open_answer',
                'question': 'Descreva o conceito de CRUD e dê exemplos de cada operação.',
                'correct_keywords': ['create', 'read', 'update', 'delete', 'criar', 'ler', 'atualizar', 'deletar']
            }
        ]
    },
    3: {
        'title': 'Manipulação de Arquivos e Dados',
        'description': 'Trabalhando com diferentes formatos de arquivo e dados.',
        'video_url': '',
        'content': '''
        <h3>🧮 Módulo 3 – Manipulação de Arquivos e Dados</h3>
        <p><strong>Trabalhando com diferentes formatos de arquivo e dados.</strong></p>
        
        <h4>📁 Tipos de Arquivo:</h4>
        <ul>
            <li><strong>Arquivos .txt:</strong> Leitura e escrita básica</li>
            <li><strong>Arquivos CSV:</strong> Dados tabulares e planilhas</li>
            <li><strong>Arquivos JSON:</strong> Dados estruturados</li>
            <li><strong>Bibliotecas Externas:</strong> Expandindo as capacidades</li>
        </ul>
        
        <h4>🔧 Ferramentas e Bibliotecas:</h4>
        <ul>
            <li><code>open()</code> - Manipulação básica de arquivos</li>
            <li><code>csv</code> - Módulo para arquivos CSV</li>
            <li><code>json</code> - Trabalho com dados JSON</li>
            <li><code>pandas</code> - Análise de dados (introdução)</li>
        </ul>
        
        <h4>🎯 Projeto Final:</h4>
        <p><strong>Analisador de Arquivo de Vendas</strong> - Um sistema completo que lê dados de vendas de diferentes formatos e gera relatórios.</p>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual modo de abertura de arquivo permite leitura e escrita?',
                'options': ['r', 'w', 'r+', 'a'],
                'correct_answer': 'r+'
            },
            {
                'type': 'multiple_choice',
                'question': 'Que formato JSON usa para representar dados?',
                'options': ['XML', 'Texto simples', 'Chave-valor', 'Binário'],
                'correct_answer': 'Chave-valor'
            },
            {
                'type': 'open_answer',
                'question': 'Explique a vantagem de usar arquivos CSV para armazenar dados tabulares.',
                'correct_keywords': ['simples', 'compatível', 'excel', 'planilha', 'estruturado', 'portável']
            }
        ]
    },
    4: {
        'title': 'Bancos de Dados com SQLite e PostgreSQL',
        'description': 'Conceitos de banco de dados relacionais e integração com Python.',
        'video_url': '',
        'content': '''
        <h3>🛢️ Módulo 4 – Bancos de Dados com SQLite e PostgreSQL</h3>
        <p><strong>Conceitos de banco de dados relacionais e integração com Python.</strong></p>
        
        <h4>🗄️ Conceitos Fundamentais:</h4>
        <ul>
            <li><strong>Banco de Dados Relacional:</strong> Tabelas, relacionamentos, chaves</li>
            <li><strong>SQL Básico:</strong> SELECT, INSERT, UPDATE, DELETE</li>
            <li><strong>Normalização:</strong> Organizando dados eficientemente</li>
        </ul>
        
        <h4>🐍 Python e Bancos:</h4>
        <ul>
            <li><strong>SQLite:</strong> Banco leve para desenvolvimento (sqlite3)</li>
            <li><strong>PostgreSQL:</strong> Banco robusto para produção</li>
            <li><strong>psycopg2:</strong> Conexão direta com PostgreSQL</li>
            <li><strong>SQLAlchemy:</strong> ORM para facilitar o desenvolvimento</li>
        </ul>
        
        <h4>🎯 Projeto Final:</h4>
        <p><strong>Sistema CRUD Completo</strong> - Aplicação que gerencia dados com operações completas de banco de dados.</p>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'O que significa CRUD em bancos de dados?',
                'options': [
                    'Create, Read, Update, Delete',
                    'Connect, Run, Update, Display',
                    'Copy, Read, Upload, Download',
                    'Create, Relate, Use, Drop'
                ],
                'correct_answer': 'Create, Read, Update, Delete'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual é a principal vantagem do SQLite?',
                'options': [
                    'Alta performance em produção',
                    'Não precisa de servidor separado',
                    'Suporte a múltiplos usuários',
                    'Recursos avançados de segurança'
                ],
                'correct_answer': 'Não precisa de servidor separado'
            },
            {
                'type': 'open_answer',
                'question': 'Explique a diferença entre um banco de dados relacional e não-relacional.',
                'correct_keywords': ['tabela', 'relação', 'estrutura', 'sql', 'nosql', 'flexível', 'esquema']
            }
        ]
    },
    5: {
        'title': 'Programação Web com Flask',
        'description': 'Introdução ao desenvolvimento web com Python.',
        'video_url': '',
        'content': '''
        <h3>🌐 Módulo 5 – Programação Web com Flask</h3>
        <p><strong>Introdução ao desenvolvimento web com Python.</strong></p>
        
        <h4>🌍 Conceitos Web:</h4>
        <ul>
            <li><strong>Web Server:</strong> Como funcionam servidores web</li>
            <li><strong>HTTP:</strong> Protocolo de comunicação</li>
            <li><strong>Frontend vs Backend:</strong> Divisão de responsabilidades</li>
        </ul>
        
        <h4>🌶️ Flask Framework:</h4>
        <ul>
            <li><strong>Rotas:</strong> Mapeamento de URLs para funções</li>
            <li><strong>Views:</strong> Lógica de apresentação</li>
            <li><strong>Templates HTML:</strong> Páginas dinâmicas com Jinja2</li>
            <li><strong>Formulários:</strong> Captura e processamento de dados</li>
            <li><strong>Integração com BD:</strong> Conectando web com dados</li>
        </ul>
        
        <h4>🎯 Projeto Final:</h4>
        <p><strong>Blog Pessoal</strong> - Site completo com posts, comentários e área administrativa.</p>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'O que é uma rota no Flask?',
                'options': [
                    'Um caminho no sistema de arquivos',
                    'Uma URL mapeada para uma função Python',
                    'Um tipo de banco de dados',
                    'Um protocolo de rede'
                ],
                'correct_answer': 'Uma URL mapeada para uma função Python'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual template engine o Flask usa por padrão?',
                'options': ['Django Templates', 'Jinja2', 'Mustache', 'Handlebars'],
                'correct_answer': 'Jinja2'
            },
            {
                'type': 'open_answer',
                'question': 'Explique a diferença entre GET e POST em requisições HTTP.',
                'correct_keywords': ['dados', 'url', 'body', 'segurança', 'parâmetros', 'formulário']
            }
        ]
    },
    6: {
        'title': 'APIs REST com Flask',
        'description': 'Criando e consumindo APIs RESTful.',
        'video_url': '',
        'content': '''
        <h3>🧩 Módulo 6 – APIs REST com Flask</h3>
        <p><strong>Criando e consumindo APIs RESTful.</strong></p>
        
        <h4>🔗 Conceitos de API:</h4>
        <ul>
            <li><strong>API REST:</strong> Princípios e arquitetura</li>
            <li><strong>Recursos:</strong> Modelagem de dados para APIs</li>
            <li><strong>Status Codes:</strong> Comunicação de estado</li>
            <li><strong>JSON:</strong> Formato de troca de dados</li>
        </ul>
        
        <h4>🛠️ Métodos HTTP:</h4>
        <ul>
            <li><strong>GET:</strong> Buscar dados</li>
            <li><strong>POST:</strong> Criar novos recursos</li>
            <li><strong>PUT:</strong> Atualizar recursos completos</li>
            <li><strong>DELETE:</strong> Remover recursos</li>
        </ul>
        
        <h4>✨ Boas Práticas:</h4>
        <ul>
            <li>Nomenclatura consistente de endpoints</li>
            <li>Tratamento adequado de erros</li>
            <li>Documentação clara da API</li>
            <li>Versionamento de APIs</li>
        </ul>
        
        <h4>🎯 Projeto Final:</h4>
        <p><strong>API de Cadastro de Usuários</strong> - Sistema completo de gerenciamento via API.</p>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual método HTTP é usado para criar um novo recurso?',
                'options': ['GET', 'POST', 'PUT', 'DELETE'],
                'correct_answer': 'POST'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que significa REST?',
                'options': [
                    'Representational State Transfer',
                    'Remote Execution State Transfer',
                    'Resource Execution State Transfer',
                    'Relational State Transfer'
                ],
                'correct_answer': 'Representational State Transfer'
            },
            {
                'type': 'open_answer',
                'question': 'Explique a importância dos códigos de status HTTP em uma API.',
                'correct_keywords': ['comunicação', 'erro', 'sucesso', 'cliente', 'servidor', 'feedback']
            }
        ]
    },
    7: {
        'title': 'Testes Automatizados e Boas Práticas',
        'description': 'Garantindo qualidade do código através de testes.',
        'video_url': '',
        'content': '''
        <h3>🐍 Módulo 7 – Testes Automatizados e Boas Práticas</h3>
        <p><strong>Garantindo qualidade do código através de testes.</strong></p>
        
        <h4>🧪 Tipos de Teste:</h4>
        <ul>
            <li><strong>Testes Unitários:</strong> Testando funções isoladamente</li>
            <li><strong>Testes de Integração:</strong> Verificando componentes juntos</li>
            <li><strong>Testes de API:</strong> Validando endpoints</li>
        </ul>
        
        <h4>🔧 Ferramentas:</h4>
        <ul>
            <li><strong>unittest:</strong> Biblioteca padrão do Python</li>
            <li><strong>pytest:</strong> Framework mais moderno e flexível</li>
            <li><strong>requests:</strong> Para testar APIs HTTP</li>
            <li><strong>mock:</strong> Simulando dependências externas</li>
        </ul>
        
        <h4>📝 Documentação:</h4>
        <ul>
            <li><strong>Docstrings:</strong> Documentando funções e classes</li>
            <li><strong>README:</strong> Documentação do projeto</li>
            <li><strong>Comentários:</strong> Explicando lógica complexa</li>
        </ul>
        
        <h4>🎯 Projeto Final:</h4>
        <p><strong>Suite de Testes para API</strong> - Testes completos para uma API de produtos.</p>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'O que são testes unitários?',
                'options': [
                    'Testes do sistema completo',
                    'Testes de funções isoladas',
                    'Testes de performance',
                    'Testes de interface'
                ],
                'correct_answer': 'Testes de funções isoladas'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual biblioteca é mais moderna para testes em Python?',
                'options': ['unittest', 'pytest', 'nose', 'doctest'],
                'correct_answer': 'pytest'
            },
            {
                'type': 'open_answer',
                'question': 'Por que é importante escrever testes automatizados?',
                'correct_keywords': ['qualidade', 'confiança', 'bugs', 'regressão', 'manutenção', 'refatoração']
            }
        ]
    },
    8: {
        'title': 'Deploy de Aplicações Python',
        'description': 'Colocando suas aplicações no ar.',
        'video_url': '',
        'content': '''
        <h3>☁️ Módulo 8 – Deploy de Aplicações Python</h3>
        <p><strong>Colocando suas aplicações no ar.</strong></p>
        
        <h4>🚀 Preparação para Deploy:</h4>
        <ul>
            <li><strong>Requirements:</strong> Gerenciando dependências</li>
            <li><strong>Variáveis de Ambiente:</strong> Configurações seguras</li>
            <li><strong>Estrutura de Projeto:</strong> Organização para produção</li>
            <li><strong>Logging:</strong> Monitoramento de aplicações</li>
        </ul>
        
        <h4>🌐 Plataformas de Deploy:</h4>
        <ul>
            <li><strong>Render:</strong> Deploy simples e gratuito</li>
            <li><strong>Railway:</strong> Plataforma moderna de deploy</li>
            <li><strong>PythonAnywhere:</strong> Especializada em Python</li>
            <li><strong>Heroku:</strong> Plataforma tradicional (conceitos)</li>
        </ul>
        
        <h4>🔧 Configurações de Produção:</h4>
        <ul>
            <li>Bancos de dados remotos</li>
            <li>Domínios customizados</li>
            <li>HTTPS e certificados SSL</li>
            <li>Monitoramento e logs</li>
        </ul>
        
        <h4>🎯 Projeto Final:</h4>
        <p><strong>API Online com Base de Dados</strong> - Aplicação completa em produção.</p>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'O que é um arquivo requirements.txt?',
                'options': [
                    'Lista de recursos necessários',
                    'Lista de dependências do projeto',
                    'Lista de requisitos do cliente',
                    'Lista de funcionalidades'
                ],
                'correct_answer': 'Lista de dependências do projeto'
            },
            {
                'type': 'multiple_choice',
                'question': 'Por que usar variáveis de ambiente em produção?',
                'options': [
                    'Para melhorar performance',
                    'Para ocultar informações sensíveis',
                    'Para reduzir o tamanho do código',
                    'Para facilitar o desenvolvimento'
                ],
                'correct_answer': 'Para ocultar informações sensíveis'
            },
            {
                'type': 'open_answer',
                'question': 'Explique a diferença entre ambiente de desenvolvimento e produção.',
                'correct_keywords': ['teste', 'real', 'usuários', 'segurança', 'performance', 'configuração']
            }
        ]
    },
    9: {
        'title': 'Projeto Final',
        'description': 'Projeto integrador aplicando todos os conhecimentos.',
        'video_url': '',
        'content': '''
        <h3>🎓 Módulo 9 – Projeto Final</h3>
        <p><strong>Projeto integrador aplicando todos os conhecimentos adquiridos.</strong></p>
        
        <h4>🎯 Propostas de Projeto:</h4>
        <ul>
            <li><strong>ERP Simples:</strong> Sistema de gestão empresarial</li>
            <li><strong>Sistema de Tarefas:</strong> Gerenciador de projetos</li>
            <li><strong>API de Filmes:</strong> Catálogo com avaliações</li>
            <li><strong>E-commerce Básico:</strong> Loja virtual completa</li>
            <li><strong>Sistema de Blog:</strong> Plataforma de conteúdo</li>
        </ul>
        
        <h4>📋 Etapas de Desenvolvimento:</h4>
        <ol>
            <li><strong>Planejamento:</strong> Definindo escopo e requisitos</li>
            <li><strong>Wireframe:</strong> Prototipação da interface</li>
            <li><strong>Modelagem:</strong> Estrutura de dados e banco</li>
            <li><strong>Desenvolvimento:</strong> Implementação em etapas</li>
            <li><strong>Testes:</strong> Validação e correções</li>
            <li><strong>Deploy:</strong> Publicação do projeto</li>
            <li><strong>Apresentação:</strong> Demonstração final</li>
        </ol>
        
        <h4>🔧 Tecnologias Integradas:</h4>
        <ul>
            <li>Python com Flask/FastAPI</li>
            <li>Banco de dados PostgreSQL</li>
            <li>Frontend com HTML/CSS/JavaScript</li>
            <li>Testes automatizados</li>
            <li>Deploy em produção</li>
            <li>Documentação completa</li>
        </ul>
        
        <h4>✨ Critérios de Avaliação:</h4>
        <ul>
            <li>Funcionalidade completa</li>
            <li>Qualidade do código</li>
            <li>Testes implementados</li>
            <li>Documentação clara</li>
            <li>Deploy funcionando</li>
            <li>Apresentação profissional</li>
        </ul>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual é a primeira etapa no desenvolvimento de um projeto?',
                'options': ['Codificação', 'Planejamento', 'Testes', 'Deploy'],
                'correct_answer': 'Planejamento'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que é um wireframe?',
                'options': [
                    'Código do projeto',
                    'Prototipo da interface',
                    'Documentação técnica',
                    'Teste automatizado'
                ],
                'correct_answer': 'Prototipo da interface'
            },
            {
                'type': 'open_answer',
                'question': 'Por que é importante documentar um projeto de software?',
                'correct_keywords': ['manutenção', 'equipe', 'futuro', 'entendimento', 'colaboração', 'conhecimento']
            }
        ]
    }
}

FINAL_EXAM = {
    'title': 'Exame Final - Curso Python Completo',
    'description': 'Este exame abrange todos os módulos que você completou. É necessário 70% para aprovação.',
    'questions': [
        {
            'type': 'multiple_choice',
            'question': 'Qual é a principal vantagem do Python para iniciantes?',
            'options': [
                'Sintaxe simples e legível',
                'Execução muito rápida',
                'Não precisa de instalação',
                'Funciona apenas no Windows'
            ],
            'correct_answer': 'Sintaxe simples e legível'
        },
        {
            'type': 'multiple_choice',
            'question': 'Em Flask, como você define uma rota?',
            'options': [
                '@app.route("/caminho")',
                '@route("/caminho")',
                'app.add_route("/caminho")',
                'route("/caminho")'
            ],
            'correct_answer': '@app.route("/caminho")'
        },
        {
            'type': 'multiple_choice',
            'question': 'Qual comando SQL é usado para buscar dados?',
            'options': ['INSERT', 'UPDATE', 'DELETE', 'SELECT'],
            'correct_answer': 'SELECT'
        },
        {
            'type': 'multiple_choice',
            'question': 'O que significa API REST?',
            'options': [
                'Application Programming Interface - Representational State Transfer',
                'Advanced Programming Interface - Remote State Transfer',
                'Application Process Interface - Resource State Transfer',
                'Advanced Process Interface - Representational State Transfer'
            ],
            'correct_answer': 'Application Programming Interface - Representational State Transfer'
        },
        {
            'type': 'multiple_choice',
            'question': 'Qual biblioteca é usada para testes em Python?',
            'options': ['requests', 'flask', 'pytest', 'json'],
            'correct_answer': 'pytest'
        },
        {
            'type': 'open_answer',
            'question': 'Explique o conceito de variáveis de ambiente e sua importância em aplicações Python.',
            'correct_keywords': ['configuração', 'segurança', 'produção', 'desenvolvimento', 'secreto', 'ambiente']
        },
        {
            'type': 'open_answer',
            'question': 'Descreva as principais etapas do desenvolvimento de um projeto Python completo.',
            'correct_keywords': ['planejamento', 'desenvolvimento', 'teste', 'deploy', 'documentação', 'wireframe']
        },
        {
            'type': 'open_answer',
            'question': 'Compare as vantagens e desvantagens do SQLite em relação ao PostgreSQL.',
            'correct_keywords': ['simples', 'produção', 'performance', 'recursos', 'servidor', 'desenvolvimento']
        }
    ]
}