# Dados dos módulos do sistema
MODULES = {
    1: {
        'title': 'Fundamentos do Python',
        'description': 'Conceitos básicos da linguagem Python.',
        'video_url': '',
        'content': '<h3>Módulo 1 - Fundamentos do Python</h3><p>Conteúdo básico sobre Python.</p>',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual é o tipo de dados da variável: idade = 25',
                'options': ['string', 'float', 'int', 'boolean', 'list'],
                'correct_answer': 'int'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como você cria uma lista em Python?',
                'options': ['lista = [1, 2, 3]', 'lista = (1, 2, 3)', 'lista = {1, 2, 3}', 'lista = 1, 2, 3', 'lista = <1, 2, 3>'],
                'correct_answer': 'lista = [1, 2, 3]'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual função é usada para receber entrada do usuário?',
                'options': ['print()', 'input()', 'get()', 'read()', 'scan()'],
                'correct_answer': 'input()'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual operador é usado para exponenciação em Python?',
                'options': ['^', '**', 'exp', 'pow', '^^'],
                'correct_answer': '**'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como você acessa o último elemento de uma lista chamada "frutas"?',
                'options': ['frutas[last]', 'frutas[-1]', 'frutas[end]', 'frutas[length-1]', 'frutas.last()'],
                'correct_answer': 'frutas[-1]'
            }
        ]
    },
    2: {
        'title': 'Estruturas de Controle',
        'description': 'Condicionais, loops e estruturas de decisão.',
        'video_url': '',
        'content': '<h3>Módulo 2 - Estruturas de Controle</h3><p>Conteúdo sobre if, for, while.</p>',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual palavra-chave é usada para condições em Python?',
                'options': ['if', 'when', 'case', 'condition', 'check'],
                'correct_answer': 'if'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como você cria um loop que executa 10 vezes?',
                'options': ['for i in range(10):', 'for i = 1 to 10:', 'loop 10 times:', 'repeat(10):', 'while i <= 10:'],
                'correct_answer': 'for i in range(10):'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que faz o comando "break" em um loop?',
                'options': ['Pula para a próxima iteração', 'Interrompe o loop completamente', 'Reinicia o loop do início', 'Pausa o loop temporariamente', 'Não faz nada'],
                'correct_answer': 'Interrompe o loop completamente'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual a diferença entre range(5) e range(1, 6)?',
                'options': ['Não há diferença, ambos geram os mesmos números', 'range(5) gera 0-4, range(1,6) gera 1-5', 'range(5) gera 1-5, range(1,6) gera 0-4', 'range(5) é inválido', 'range(1,6) é inválido'],
                'correct_answer': 'range(5) gera 0-4, range(1,6) gera 1-5'
            },
            {
                'type': 'multiple_choice',
                'question': 'Em qual situação você deveria usar WHILE ao invés de FOR?',
                'options': ['Quando sabe exatamente quantas iterações precisa', 'Quando quer iterar sobre uma lista', 'Quando não sabe quantas iterações serão necessárias', 'Quando quer usar break ou continue', 'WHILE e FOR são sempre intercambiáveis'],
                'correct_answer': 'Quando não sabe quantas iterações serão necessárias'
            }
        ]
    },
    3: {
        'title': 'Manipulação de Arquivos',
        'description': 'Trabalhando com arquivos em Python.',
        'video_url': '',
        'content': '<h3>Módulo 3 - Manipulação de Arquivos</h3><p>Conteúdo sobre leitura e escrita de arquivos.</p>',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Como abrir um arquivo para leitura em Python?',
                'options': ['open("file.txt", "r")', 'read("file.txt")', 'file.open("r")', 'load("file.txt")'],
                'correct_answer': 'open("file.txt", "r")'
            }
        ]
    },
    4: {
        'title': 'Funções e Módulos',
        'description': 'Criação e uso de funções em Python.',
        'video_url': '',
        'content': '<h3>Módulo 4 - Funções e Módulos</h3><p>Conteúdo sobre funções e módulos.</p>',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Como definir uma função em Python?',
                'options': ['def funcao():', 'function funcao():', 'create funcao():', 'func funcao():'],
                'correct_answer': 'def funcao():'
            }
        ]
    },
    5: {
        'title': 'Programação Orientada a Objetos',
        'description': 'Classes e objetos em Python.',
        'video_url': '',
        'content': '<h3>Módulo 5 - POO</h3><p>Conteúdo sobre classes e objetos.</p>',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Como definir uma classe em Python?',
                'options': ['class MinhaClasse:', 'create MinhaClasse:', 'def MinhaClasse:', 'object MinhaClasse:'],
                'correct_answer': 'class MinhaClasse:'
            }
        ]
    },
    6: {
        'title': 'Tratamento de Exceções',
        'description': 'Gerenciamento de erros em Python.',
        'video_url': '',
        'content': '<h3>Módulo 6 - Exceções</h3><p>Conteúdo sobre tratamento de erros.</p>',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual palavra-chave inicia um bloco de tratamento de exceção?',
                'options': ['try', 'catch', 'except', 'handle'],
                'correct_answer': 'try'
            }
        ]
    },
    7: {
        'title': 'Bibliotecas e APIs',
        'description': 'Usando bibliotecas externas e APIs.',
        'video_url': '',
        'content': '<h3>Módulo 7 - Bibliotecas</h3><p>Conteúdo sobre bibliotecas e APIs.</p>',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Como instalar uma biblioteca externa?',
                'options': ['pip install nome_biblioteca', 'python install nome_biblioteca', 'import install nome_biblioteca', 'get nome_biblioteca'],
                'correct_answer': 'pip install nome_biblioteca'
            }
        ]
    },
    8: {
        'title': 'Banco de Dados',
        'description': 'Trabalhando com bancos de dados.',
        'video_url': '',
        'content': '<h3>Módulo 8 - Banco de Dados</h3><p>Conteúdo sobre conexão com bancos.</p>',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual biblioteca é comumente usada para conectar ao SQLite?',
                'options': ['sqlite3', 'database', 'sqlconnector', 'dbapi'],
                'correct_answer': 'sqlite3'
            }
        ]
    },
    9: {
        'title': 'Projeto Final',
        'description': 'Integração de todos os conceitos aprendidos.',
        'video_url': '',
        'content': '<h3>Módulo 9 - Projeto Final</h3><p>Aplicando todos os conhecimentos.</p>',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'O que é mais importante em um projeto Python?',
                'options': ['Código limpo e organizado', 'Usar muitas bibliotecas', 'Ter muitas linhas', 'Ser complexo'],
                'correct_answer': 'Código limpo e organizado'
            }
        ]
    }
}

FINAL_EXAM = {
    'title': 'Exame Final - Python Completo',
    'description': 'Teste seus conhecimentos em todos os módulos.',
    'questions': [
        {
            'type': 'multiple_choice',
            'question': 'Qual é a sintaxe correta para uma função em Python?',
            'options': ['function nome():', 'def nome():', 'func nome():', 'create nome():'],
            'correct_answer': 'def nome():'
        },
        {
            'type': 'multiple_choice',
            'question': 'Como você importa uma biblioteca em Python?',
            'options': ['include biblioteca', 'import biblioteca', 'use biblioteca', 'require biblioteca'],
            'correct_answer': 'import biblioteca'
        }
    ],
    'passing_score': 70
}