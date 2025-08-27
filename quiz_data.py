# Quiz data for the Learning Management System

MODULES = {
    1: {
        'title': 'Introdução ao Python',
        'description': 'Fundamentos da linguagem Python, variáveis, tipos de dados e funções básicas',
        'content': '''<div class="module-header">
            <h3>🚀 Módulo 1 - Introdução ao Python</h3>
            <p class="module-intro"><strong>Bem-vindo ao mundo Python!</strong> Uma linguagem poderosa, elegante e versátil que conquista desenvolvedores ao redor do mundo. Prepare-se para uma jornada incrível!</p>
        </div>''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual é a função usada para exibir texto na tela em Python?',
                'options': ['show()', 'display()', 'print()', 'output()'],
                'correct_answer': 'print()'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como criar uma variável em Python?',
                'options': ['var nome = "João"', 'nome = "João"', 'string nome = "João"', 'nome := "João"'],
                'correct_answer': 'nome = "João"'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual tipo de dado representa números inteiros?',
                'options': ['float', 'string', 'int', 'number'],
                'correct_answer': 'int'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como capturar dados do usuário?',
                'options': ['get()', 'input()', 'read()', 'scan()'],
                'correct_answer': 'input()'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual símbolo é usado para comentários em Python?',
                'options': ['//', '/* */', '#', '--'],
                'correct_answer': '#'
            }
        ]
    },
    2: {
        'title': 'Estruturas Condicionais e Loops',
        'description': 'Aprenda a usar if, elif, else, for e while para controlar o fluxo do programa',
        'content': '''<div class="module-header">
            <h3>🎯 Módulo 2 - Estruturas Condicionais e Loops</h3>
            <p class="module-intro"><strong>Dê inteligência aos seus programas!</strong> Aprenda a tomar decisões e repetir ações de forma eficiente.</p>
        </div>''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual palavra-chave é usada para estruturas condicionais?',
                'options': ['when', 'if', 'check', 'condition'],
                'correct_answer': 'if'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como criar um loop que repete 5 vezes?',
                'options': ['for i in range(5):', 'loop 5 times:', 'repeat(5):', 'while 5:'],
                'correct_answer': 'for i in range(5):'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual a diferença entre "if" e "elif"?',
                'options': ['São iguais', 'elif é usado para condições adicionais', 'elif é mais rápido', 'if é obrigatório'],
                'correct_answer': 'elif é usado para condições adicionais'
            },
            {
                'type': 'multiple_choice',
                'question': 'Quando usar while ao invés de for?',
                'options': ['Sempre', 'Nunca', 'Quando não sabemos quantas repetições', 'When é mais rápido'],
                'correct_answer': 'Quando não sabemos quantas repetições'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que faz range(1, 6)?',
                'options': ['Números de 1 a 6', 'Números de 1 a 5', 'Números de 0 a 6', 'Números de 0 a 5'],
                'correct_answer': 'Números de 1 a 5'
            }
        ]
    },
    3: {
        'title': 'Manipulação de Arquivos',
        'description': 'Domine leitura, escrita e processamento de arquivos e formatos como CSV e JSON',
        'content': '''<div class="module-header">
            <h3>📁 Módulo 3 - Manipulação de Arquivos</h3>
            <p class="module-intro"><strong>Domine o mundo dos dados!</strong> Aprenda a ler, escrever e processar diferentes tipos de arquivos.</p>
        </div>''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Como abrir um arquivo para leitura em Python?',
                'options': ['open("file.txt", "r")', 'read("file.txt")', 'file.open("r")', 'load("file.txt")'],
                'correct_answer': 'open("file.txt", "r")'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual é a vantagem de usar "with open()"?',
                'options': ['É mais rápido', 'Fecha o arquivo automaticamente', 'Usa menos memória', 'É obrigatório'],
                'correct_answer': 'Fecha o arquivo automaticamente'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual modo de abertura sobrescreve um arquivo existente?',
                'options': ['"r"', '"a"', '"w"', '"x"'],
                'correct_answer': '"w"'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual biblioteca é usada para trabalhar com arquivos CSV?',
                'options': ['json', 'csv', 'pandas', 'file'],
                'correct_answer': 'csv'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como converter um dicionário Python para JSON?',
                'options': ['json.loads()', 'json.dump()', 'json.save()', 'json.convert()'],
                'correct_answer': 'json.dump()'
            }
        ]
    },
    4: {
        'title': 'Funções e Módulos',
        'description': 'Organize seu código com funções reutilizáveis e modularização',
        'content': '''<div class="module-header">
            <h3>⚡ Módulo 4 - Funções e Módulos</h3>
            <p class="module-intro"><strong>Organize e reutilize seu código!</strong> Aprenda a criar funções poderosas e modular seu código.</p>
        </div>''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Como definir uma função em Python?',
                'options': ['def funcao():', 'function funcao():', 'create funcao():', 'func funcao():'],
                'correct_answer': 'def funcao():'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que a palavra-chave "return" faz em uma função?',
                'options': ['Inicia a função', 'Retorna um valor', 'Para a execução', 'Imprime na tela'],
                'correct_answer': 'Retorna um valor'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como importar uma função específica de um módulo?',
                'options': ['import modulo.funcao', 'from modulo import funcao', 'get modulo.funcao', 'use modulo.funcao'],
                'correct_answer': 'from modulo import funcao'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual é a diferença entre parâmetros e argumentos?',
                'options': ['São a mesma coisa', 'Parâmetros são na definição, argumentos na chamada', 'Argumentos são na definição, parâmetros na chamada', 'Parâmetros são obrigatórios'],
                'correct_answer': 'Parâmetros são na definição, argumentos na chamada'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como criar um parâmetro com valor padrão?',
                'options': ['def func(x=10):', 'def func(x:10):', 'def func(x->10):', 'def func(x default 10):'],
                'correct_answer': 'def func(x=10):'
            }
        ]
    },
    5: {
        'title': 'Programação Orientada a Objetos',
        'description': 'Domine classes, objetos, herança e encapsulamento em Python',
        'content': '''<div class="module-header">
            <h3>🏢 Módulo 5 - Programação Orientada a Objetos</h3>
            <p class="module-intro"><strong>Construa código mais inteligente!</strong> Descubra o poder das classes e objetos.</p>
        </div>''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Como definir uma classe em Python?',
                'options': ['class MinhaClasse:', 'create MinhaClasse:', 'def MinhaClasse:', 'object MinhaClasse:'],
                'correct_answer': 'class MinhaClasse:'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual método é chamado automaticamente ao criar um objeto?',
                'options': ['__create__', '__init__', '__new__', '__start__'],
                'correct_answer': '__init__'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que é herança em POO?',
                'options': ['Copiar código', 'Uma classe filha herda características da classe pai', 'Deletar classes', 'Renomear métodos'],
                'correct_answer': 'Uma classe filha herda características da classe pai'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que significa "self" em Python?',
                'options': ['Referência ao objeto atual', 'Nome da classe', 'Método especial', 'Variável global'],
                'correct_answer': 'Referência ao objeto atual'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como indicar que um atributo é privado por convenção?',
                'options': ['Usar maiúscula', 'Começar com _', 'Usar @private', 'Começar com #'],
                'correct_answer': 'Começar com _'
            }
        ]
    },
    6: {
        'title': 'Tratamento de Exceções',
        'description': 'Aprenda a lidar com erros usando try, except, finally e raise',
        'content': '''<div class="module-header">
            <h3>⚠️ Módulo 6 - Tratamento de Exceções</h3>
            <p class="module-intro"><strong>Torne seus programas à prova de erros!</strong> Aprenda a antecipar e tratar erros.</p>
        </div>''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual palavra-chave inicia um bloco de tratamento de exceção?',
                'options': ['try', 'catch', 'except', 'handle'],
                'correct_answer': 'try'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual palavra-chave captura uma exceção?',
                'options': ['catch', 'except', 'handle', 'grab'],
                'correct_answer': 'except'
            },
            {
                'type': 'multiple_choice',
                'question': 'Quando o bloco "finally" é executado?',
                'options': ['Apenas se houver erro', 'Apenas se não houver erro', 'Sempre', 'Nunca'],
                'correct_answer': 'Sempre'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como lançar uma exceção manualmente?',
                'options': ['throw Exception', 'raise Exception', 'error Exception', 'exception Exception'],
                'correct_answer': 'raise Exception'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que acontece se uma exceção não for tratada?',
                'options': ['O programa continua', 'O programa para com erro', 'O erro é ignorado', 'Nada acontece'],
                'correct_answer': 'O programa para com erro'
            }
        ]
    },
    7: {
        'title': 'Bibliotecas e APIs',
        'description': 'Use bibliotecas externas e integre com APIs para expandir funcionalidades',
        'content': '''<div class="module-header">
            <h3>📚 Módulo 7 - Bibliotecas e APIs</h3>
            <p class="module-intro"><strong>Expanda o poder do Python!</strong> Descubra como usar bibliotecas externas e APIs.</p>
        </div>''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Como instalar uma biblioteca externa?',
                'options': ['pip install nome_biblioteca', 'python install nome_biblioteca', 'import install nome_biblioteca', 'get nome_biblioteca'],
                'correct_answer': 'pip install nome_biblioteca'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual biblioteca é popular para fazer requisições HTTP?',
                'options': ['http', 'requests', 'urllib', 'web'],
                'correct_answer': 'requests'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que é uma API?',
                'options': ['Um tipo de variável', 'Interface de Programação de Aplicações', 'Uma biblioteca Python', 'Um banco de dados'],
                'correct_answer': 'Interface de Programação de Aplicações'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual método HTTP é usado para buscar dados de uma API?',
                'options': ['POST', 'PUT', 'GET', 'DELETE'],
                'correct_answer': 'GET'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como listar todas as bibliotecas instaladas?',
                'options': ['pip show', 'pip list', 'pip install', 'pip check'],
                'correct_answer': 'pip list'
            }
        ]
    },
    8: {
        'title': 'Banco de Dados',
        'description': 'Conecte e manipule bancos de dados usando SQLite e operações CRUD',
        'content': '''<div class="module-header">
            <h3>🗄️ Módulo 8 - Banco de Dados</h3>
            <p class="module-intro"><strong>Persista seus dados!</strong> Aprenda a armazenar e gerenciar dados usando bancos de dados.</p>
        </div>''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual biblioteca é comumente usada para conectar ao SQLite?',
                'options': ['sqlite3', 'database', 'sqlconnector', 'dbapi'],
                'correct_answer': 'sqlite3'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual comando SQL é usado para criar uma tabela?',
                'options': ['MAKE TABLE', 'CREATE TABLE', 'NEW TABLE', 'ADD TABLE'],
                'correct_answer': 'CREATE TABLE'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que significa CRUD em banco de dados?',
                'options': ['Create, Read, Update, Delete', 'Connect, Run, Update, Drop', 'Copy, Rename, Upload, Download', 'Create, Remove, Use, Data'],
                'correct_answer': 'Create, Read, Update, Delete'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual método é usado para executar comandos SQL?',
                'options': ['cursor.run()', 'cursor.execute()', 'cursor.query()', 'cursor.command()'],
                'correct_answer': 'cursor.execute()'
            },
            {
                'type': 'multiple_choice',
                'question': 'Para que serve o comando "commit()"?',
                'options': ['Conectar ao banco', 'Salvar as mudanças', 'Fechar a conexão', 'Criar tabelas'],
                'correct_answer': 'Salvar as mudanças'
            }
        ]
    },
    9: {
        'title': 'Projeto Final',
        'description': 'Integre todos os conceitos aprendidos em um projeto Python completo',
        'content': '''<div class="module-header">
            <h3>🎆 Módulo 9 - Projeto Final</h3>
            <p class="module-intro"><strong>Integre todos os conceitos!</strong> Crie um projeto completo que demonstra domínio em Python.</p>
        </div>''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'O que é mais importante em um projeto Python?',
                'options': ['Código limpo e organizado', 'Usar muitas bibliotecas', 'Ter muitas linhas', 'Ser complexo'],
                'correct_answer': 'Código limpo e organizado'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual é a melhor prática para organizar um projeto Python?',
                'options': ['Tudo em um arquivo', 'Separar em módulos temáticos', 'Usar apenas funções', 'Evitar comentarios'],
                'correct_answer': 'Separar em módulos temáticos'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que significa SOLID em programação?',
                'options': ['Um tipo de banco de dados', 'Princípios de design de software', 'Uma biblioteca Python', 'Um framework web'],
                'correct_answer': 'Princípios de design de software'
            },
            {
                'type': 'multiple_choice',
                'question': 'Por que é importante tratar exceções em um projeto?',
                'options': ['Para o programa rodar mais rápido', 'Para evitar que o programa pare inesperadamente', 'Para usar menos memória', 'Não é importante'],
                'correct_answer': 'Para evitar que o programa pare inesperadamente'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que é refatoração de código?',
                'options': ['Deletar o código', 'Melhorar a estrutura sem mudar a funcionalidade', 'Adicionar novos recursos', 'Corrigir bugs'],
                'correct_answer': 'Melhorar a estrutura sem mudar a funcionalidade'
            }
        ]
    }
}

# Final exam questions covering all modules
FINAL_EXAM = {
    'title': 'Exame Final - Python Completo',
    'description': 'Teste seus conhecimentos em todos os módulos do curso',
    'questions': [
        {
            'type': 'multiple_choice',
            'question': 'Qual é a saída do código: print(type(42))?',
            'options': ['<class "number">', '<class "integer">', '<class "int">', '<class "num">'],
            'correct_answer': '<class "int">'
        },
        {
            'type': 'multiple_choice',
            'question': 'Como você criaria uma lista com números de 0 a 4?',
            'options': ['list(range(5))', 'list(0,4)', 'range(0,5)', 'list(range(0,4))'],
            'correct_answer': 'list(range(5))'
        },
        {
            'type': 'multiple_choice',
            'question': 'Qual método é usado para adicionar um elemento ao final de uma lista?',
            'options': ['add()', 'append()', 'insert()', 'push()'],
            'correct_answer': 'append()'
        },
        {
            'type': 'multiple_choice',
            'question': 'Como você abriria um arquivo chamado "dados.txt" para escrita?',
            'options': ['open("dados.txt", "w")', 'file("dados.txt", "write")', 'open("dados.txt", "write")', 'write("dados.txt")'],
            'correct_answer': 'open("dados.txt", "w")'
        },
        {
            'type': 'multiple_choice',
            'question': 'Qual palavra-chave é usada para definir uma função?',
            'options': ['function', 'def', 'func', 'define'],
            'correct_answer': 'def'
        },
        {
            'type': 'multiple_choice',
            'question': 'Como você criaria uma classe chamada "Pessoa" em Python?',
            'options': ['class Pessoa():', 'create class Pessoa:', 'def class Pessoa:', 'new Pessoa():'],
            'correct_answer': 'class Pessoa():'
        },
        {
            'type': 'multiple_choice',
            'question': 'Qual bloco de código é executado quando uma exceção NÃO ocorre?',
            'options': ['except', 'finally', 'else', 'catch'],
            'correct_answer': 'else'
        },
        {
            'type': 'multiple_choice',
            'question': 'Como você instalaria a biblioteca "requests"?',
            'options': ['python install requests', 'pip install requests', 'install requests', 'get requests'],
            'correct_answer': 'pip install requests'
        },
        {
            'type': 'multiple_choice',
            'question': 'Qual biblioteca Python é padrão para trabalhar com bancos SQLite?',
            'options': ['sqlite', 'sqlite3', 'database', 'sql'],
            'correct_answer': 'sqlite3'
        },
        {
            'type': 'multiple_choice',
            'question': 'Qual é uma característica importante de um código bem escrito?',
            'options': ['Ser o mais longo possível', 'Usar variáveis com nomes confusos', 'Ser legível e bem documentado', 'Evitar comentários'],
            'correct_answer': 'Ser legível e bem documentado'
        }
    ]
}