# Quiz data for the Learning Management System

MODULES = {
    1: {
        'title': 'Introdução ao Python',
        'description': 'Fundamentos da linguagem Python, variáveis, tipos de dados e funções básicas',
        'content': '''<div class="module-header">
            <h3>🚀 Módulo 1 - Introdução ao Python</h3>
            <p class="module-intro"><strong>Bem-vindo ao mundo Python!</strong> Uma linguagem poderosa, elegante e versátil que conquista desenvolvedores ao redor do mundo. Prepare-se para uma jornada incrível!</p>
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai aprender:</h4>
            <ul class="learning-objectives">
                <li>História e características do Python</li>
                <li>Como instalar e configurar o ambiente</li>
                <li>Variáveis e tipos de dados básicos</li>
                <li>Operadores matemáticos e lógicos</li>
                <li>Entrada e saída de dados</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico:</h4>
            
            <h5>1. História do Python</h5>
            <p>Python foi criado por Guido van Rossum no final dos anos 1980 na Holanda. O nome "Python" vem do grupo de comédia britânico "Monty Python". A linguagem foi projetada para ser:</p>
            <ul>
                <li><strong>Legível:</strong> Código fácil de ler e entender</li>
                <li><strong>Simples:</strong> Sintaxe clara e intuitiva</li>
                <li><strong>Versátil:</strong> Usado em web, ciência de dados, automação, IA</li>
            </ul>
            
            <h5>2. Características Principais</h5>
            <div class="alert alert-info">
                <strong>Python é uma linguagem:</strong>
                <ul class="mb-0">
                    <li>Interpretada (não precisa compilar)</li>
                    <li>Orientada a objetos</li>
                    <li>De alto nível</li>
                    <li>Com tipagem dinâmica</li>
                </ul>
            </div>
            
            <h5>3. Tipos de Dados Básicos</h5>
            <div class="code-example">
                <h6>Números:</h6>
                <pre><code># Inteiros
idade = 25
pontos = 100

# Decimais (float)
altura = 1.75
preco = 29.99</code></pre>
                
                <h6>Texto (strings):</h6>
                <pre><code># Strings
nome = "João"
mensagem = 'Olá mundo!'
texto_longo = """Texto com
múltiplas linhas"""</code></pre>
                
                <h6>Booleanos:</h6>
                <pre><code># True ou False
ativo = True
logado = False</code></pre>
            </div>
            
            <h5>4. Primeiros Comandos</h5>
            <div class="code-example">
                <h6>Exibir na tela:</h6>
                <pre><code>print("Olá, Python!")
print("Meu nome é", nome)
print(f"Tenho {idade} anos")</code></pre>
                
                <h6>Capturar dados do usuário:</h6>
                <pre><code>nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))</code></pre>
            </div>
            
            <div class="alert alert-success">
                <h6><i class="fas fa-lightbulb"></i> Dica Importante:</h6>
                <p class="mb-0">Python é case-sensitive! Isso significa que <code>nome</code> e <code>Nome</code> são variáveis diferentes.</p>
            </div>
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
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai aprender:</h4>
            <ul class="learning-objectives">
                <li>Estruturas condicionais (if, elif, else)</li>
                <li>Operadores de comparação e lógicos</li>
                <li>Loops com for e while</li>
                <li>Função range() e suas aplicações</li>
                <li>Controle de fluxo com break e continue</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico:</h4>
            
            <h5>1. Estruturas Condicionais</h5>
            <p>As estruturas condicionais permitem que o programa tome decisões baseadas em condições.</p>
            
            <div class="code-example">
                <h6>If simples:</h6>
                <pre><code>idade = 18
if idade >= 18:
    print("Você é maior de idade")</code></pre>
                
                <h6>If-else:</h6>
                <pre><code>nota = 7.5
if nota >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")</code></pre>
                
                <h6>If-elif-else:</h6>
                <pre><code>nota = 8.5
if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Bom!")
elif nota >= 5:
    print("Regular")
else:
    print("Insuficiente")</code></pre>
            </div>
            
            <h5>2. Operadores de Comparação</h5>
            <div class="alert alert-info">
                <ul class="mb-0">
                    <li><code>==</code> - Igual a</li>
                    <li><code>!=</code> - Diferente de</li>
                    <li><code>&gt;</code> - Maior que</li>
                    <li><code>&lt;</code> - Menor que</li>
                    <li><code>&gt;=</code> - Maior ou igual</li>
                    <li><code>&lt;=</code> - Menor ou igual</li>
                </ul>
            </div>
            
            <h5>3. Loops - Repetindo Ações</h5>
            
            <div class="code-example">
                <h6>Loop for com range:</h6>
                <pre><code># Conta de 0 a 4
for i in range(5):
    print(f"Número: {i}")
    
# Conta de 1 a 10
for i in range(1, 11):
    print(f"Número: {i}")
    
# Conta de 2 em 2
for i in range(0, 10, 2):
    print(f"Par: {i}")</code></pre>
                
                <h6>Loop while:</h6>
                <pre><code>contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Aumenta 1
    
# Loop até o usuário digitar 'sair'
while True:
    resposta = input("Digite 'sair' para parar: ")
    if resposta == 'sair':
        break  # Sai do loop</code></pre>
            </div>
            
            <div class="alert alert-warning">
                <h6><i class="fas fa-exclamation-triangle"></i> Cuidado com Loops Infinitos:</h6>
                <p class="mb-0">Sempre certifique-se de que a condição do while eventualmente se tornará False, senão o programa travará!</p>
            </div>
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
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai aprender:</h4>
            <ul class="learning-objectives">
                <li>Abrir, ler e escrever arquivos de texto</li>
                <li>Diferentes modos de abertura de arquivo</li>
                <li>Gerenciamento seguro com 'with'</li>
                <li>Processamento de arquivos CSV</li>
                <li>Trabalhando com arquivos JSON</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico:</h4>
            
            <h5>1. Abrindo Arquivos</h5>
            <p>Python oferece diferentes modos para trabalhar com arquivos:</p>
            
            <div class="alert alert-info">
                <strong>Modos de abertura:</strong>
                <ul class="mb-0">
                    <li><code>'r'</code> - Leitura (padrão)</li>
                    <li><code>'w'</code> - Escrita (sobrescreve)</li>
                    <li><code>'a'</code> - Anexar ao final</li>
                    <li><code>'x'</code> - Criação exclusiva</li>
                    <li><code>'b'</code> - Modo binário</li>
                </ul>
            </div>
            
            <div class="code-example">
                <h6>Lendo um arquivo:</h6>
                <pre><code># Método básico
arquivo = open('dados.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# Método recomendado com 'with'
with open('dados.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
# Arquivo é fechado automaticamente</code></pre>
                
                <h6>Escrevendo em um arquivo:</h6>
                <pre><code># Criando/sobrescrevendo arquivo
with open('resultado.txt', 'w') as arquivo:
    arquivo.write('Olá mundo!\\n')
    arquivo.write('Segunda linha')
    
# Anexando ao arquivo existente
with open('resultado.txt', 'a') as arquivo:
    arquivo.write('\\nTerceira linha')</code></pre>
            </div>
            
            <div class="alert alert-success">
                <h6><i class="fas fa-lightbulb"></i> Boa Prática:</h6>
                <p class="mb-0">Sempre use <code>with open()</code> para garantir que os arquivos sejam fechados automaticamente, mesmo se ocorrer um erro.</p>
            </div>
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
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai aprender:</h4>
            <ul class="learning-objectives">
                <li>Definindo e chamando funções</li>
                <li>Parâmetros e argumentos</li>
                <li>Valores de retorno</li>
                <li>Escopo de variáveis</li>
                <li>Importando e criando módulos</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico:</h4>
            
            <h5>1. Criando Funções</h5>
            <p>Funções são blocos de código reutilizáveis que executam uma tarefa específica.</p>
            
            <div class="code-example">
                <h6>Função simples:</h6>
                <pre><code>def saudacao():
    print("Olá, bem-vindo!")
    
# Chamando a função
saudacao()  # Olá, bem-vindo!</code></pre>
                
                <h6>Função com parâmetros:</h6>
                <pre><code>def saudacao_personalizada(nome):
    print(f"Olá, {nome}!")
    
saudacao_personalizada("Maria")  # Olá, Maria!</code></pre>
                
                <h6>Função com retorno:</h6>
                <pre><code>def calcular_area(largura, altura):
    area = largura * altura
    return area
    
resultado = calcular_area(5, 3)
print(f"A área é: {resultado}")  # A área é: 15</code></pre>
            </div>
            
            <div class="alert alert-success">
                <h6><i class="fas fa-lightbulb"></i> Princípio DRY:</h6>
                <p class="mb-0">"Don't Repeat Yourself" - Se você está escrevendo o mesmo código várias vezes, crie uma função!</p>
            </div>
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
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai aprender:</h4>
            <ul class="learning-objectives">
                <li>Conceitos de classes e objetos</li>
                <li>Métodos e atributos</li>
                <li>Construtor __init__</li>
                <li>Herança e polimorfismo</li>
                <li>Encapsulamento</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico:</h4>
            
            <h5>1. Classes e Objetos</h5>
            <p>Uma classe é um modelo para criar objetos. Um objeto é uma instância de uma classe.</p>
            
            <div class="code-example">
                <h6>Criando uma classe:</h6>
                <pre><code>class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá, eu sou {self.nome} e tenho {self.idade} anos"
    
    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} fez aniversário! Agora tem {self.idade} anos")

# Criando objetos
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

print(pessoa1.apresentar())
pessoa1.fazer_aniversario()</code></pre>
            </div>
            
            <div class="alert alert-info">
                <h6><i class="fas fa-info-circle"></i> Conceitos Importantes:</h6>
                <ul class="mb-0">
                    <li><strong>self:</strong> Referência ao objeto atual</li>
                    <li><strong>__init__:</strong> Construtor da classe</li>
                    <li><strong>_atributo:</strong> Indica atributo "privado"</li>
                </ul>
            </div>
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
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai aprender:</h4>
            <ul class="learning-objectives">
                <li>Tipos comuns de exceções</li>
                <li>Blocos try, except, else, finally</li>
                <li>Capturando exceções específicas</li>
                <li>Lançando exceções com raise</li>
                <li>Criando exceções personalizadas</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico:</h4>
            
            <h5>1. Por que Tratar Exceções?</h5>
            <p>Exceções são erros que podem ocorrer durante a execução. Tratá-las evita que o programa "quebre".</p>
            
            <div class="alert alert-warning">
                <strong>Exceções comuns:</strong>
                <ul class="mb-0">
                    <li><code>ZeroDivisionError</code> - Divisão por zero</li>
                    <li><code>ValueError</code> - Valor inadequado</li>
                    <li><code>TypeError</code> - Tipo incorreto</li>
                    <li><code>FileNotFoundError</code> - Arquivo não encontrado</li>
                    <li><code>KeyError</code> - Chave inexistente</li>
                </ul>
            </div>
            
            <div class="code-example">
                <h6>Tratamento básico:</h6>
                <pre><code>try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    print("Erro: Digite um número válido!")</code></pre>
            </div>
            
            <div class="alert alert-success">
                <h6><i class="fas fa-lightbulb"></i> Boa Prática:</h6>
                <p class="mb-0">Sempre trate exceções específicas antes de capturar Exception genérica. Isso torna o código mais robusto.</p>
            </div>
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
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai aprender:</h4>
            <ul class="learning-objectives">
                <li>Instalando bibliotecas com pip</li>
                <li>Fazendo requisições HTTP</li>
                <li>Consumindo APIs REST</li>
                <li>Processando dados JSON</li>
                <li>Bibliotecas populares do Python</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico:</h4>
            
            <h5>1. Gerenciamento de Pacotes</h5>
            <p>O pip é o gerenciador de pacotes do Python que permite instalar bibliotecas externas.</p>
            
            <div class="code-example">
                <h6>Comandos pip essenciais:</h6>
                <pre><code># Instalar uma biblioteca
pip install requests
pip install pandas numpy

# Listar bibliotecas instaladas
pip list

# Mostrar informações de uma biblioteca
pip show requests

# Atualizar uma biblioteca
pip install --upgrade requests

# Desinstalar
pip uninstall requests</code></pre>
            </div>
            
            <div class="alert alert-success">
                <h6><i class="fas fa-lightbulb"></i> Dica Profissional:</h6>
                <p class="mb-0">Sempre verifique a documentação oficial das APIs antes de usá-las. Muitas requerem autenticação via chaves API.</p>
            </div>
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
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai aprender:</h4>
            <ul class="learning-objectives">
                <li>Conceitos de banco de dados</li>
                <li>SQLite com Python</li>
                <li>Operações CRUD (Create, Read, Update, Delete)</li>
                <li>Consultas SQL básicas</li>
                <li>Boas práticas de segurança</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico:</h4>
            
            <h5>1. Introdução a Bancos de Dados</h5>
            <p>Bancos de dados são sistemas organizados para armazenar, gerenciar e recuperar informações.</p>
            
            <div class="alert alert-info">
                <strong>Conceitos importantes:</strong>
                <ul class="mb-0">
                    <li><strong>Tabela:</strong> Estrutura que organiza dados</li>
                    <li><strong>Linha/Registro:</strong> Um conjunto de dados</li>
                    <li><strong>Coluna/Campo:</strong> Um tipo de informação</li>
                    <li><strong>Chave Primária:</strong> Identificador único</li>
                </ul>
            </div>
            
            <div class="alert alert-warning">
                <h6><i class="fas fa-shield-alt"></i> Segurança:</h6>
                <p class="mb-0">Sempre use parâmetros (?) para evitar ataques de SQL Injection. Nunca concatene strings diretamente nas consultas!</p>
            </div>
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
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai aplicar:</h4>
            <ul class="learning-objectives">
                <li>Planejamento e arquitetura de projeto</li>
                <li>Integração de todos os conceitos aprendidos</li>
                <li>Boas práticas de programação</li>
                <li>Documentação e testes</li>
                <li>Versionamento com Git</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico:</h4>
            
            <h5>1. Planejamento do Projeto</h5>
            <p>Antes de começar a programar, é essencial planejar bem o projeto.</p>
            
            <div class="alert alert-info">
                <strong>Etapas do planejamento:</strong>
                <ol class="mb-0">
                    <li>Definir o problema a ser resolvido</li>
                    <li>Listar funcionalidades principais</li>
                    <li>Escolher tecnologias e bibliotecas</li>
                    <li>Criar estrutura de pastas</li>
                    <li>Definir fluxo de dados</li>
                </ol>
            </div>
            
            <div class="alert alert-success">
                <strong>Princípios importantes:</strong>
                <ul class="mb-0">
                    <li><strong>DRY:</strong> Don't Repeat Yourself</li>
                    <li><strong>KISS:</strong> Keep It Simple, Stupid</li>
                    <li><strong>SRP:</strong> Single Responsibility Principle</li>
                    <li><strong>Comentários:</strong> Explique o "porquê", não o "o quê"</li>
                    <li><strong>Nomes:</strong> Use nomes descritivos</li>
                </ul>
            </div>
            
            <div class="alert alert-warning">
                <h6><i class="fas fa-trophy"></i> Desafio Final:</h6>
                <p class="mb-0">Crie um projeto que use pelo menos: classes, arquivos, banco de dados, tratamento de exceções e uma API externa. Mostre sua evolução!</p>
            </div>
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