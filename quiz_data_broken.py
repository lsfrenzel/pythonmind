# Quiz data for the Learning Management System

MODULES = {
    1: {
        'title': 'Introdução ao Python',
        'content': '''<div class="module-header">
            <h3>🚀 Módulo 1 - Introdução ao Python</h3>
            <p class="module-intro"><strong>Bem-vindo ao mundo Python!</strong> Uma linguagem poderosa, elegante e versátil que conquista desenvolvedores ao redor do mundo. Prepare-se para uma jornada incrível!</p>
        </div>
        
        <div class="content-section">
            <h4>⭐ 1. Por que Python?</h4>
            <p>Python é mais que uma linguagem de programação - é uma filosofia de desenvolvimento que prioriza <strong>simplicidade</strong> e <strong>legibilidade</strong>.</p>
            
            <div class="code-example">
                <h5>🎯 Características Principais:</h5>
                <ul class="features-list">
                    <li><strong>💡 Sintaxe Clara:</strong> Código que parece pseudocódigo - fácil de ler e escrever</li>
                    <li><strong>🌍 Multiplataforma:</strong> Funciona em Windows, Mac, Linux e muito mais</li>
                    <li><strong>📚 Rico Ecossistema:</strong> Milhares de bibliotecas para qualquer necessidade</li>
                    <li><strong>🏢 Usado por Gigantes:</strong> Google, Netflix, Instagram, Spotify, NASA</li>
                    <li><strong>🎓 Beginner-Friendly:</strong> Perfeito para iniciantes, poderoso para experts</li>
                </ul>
            </div>
        </div>
        
        <div class="content-section">
            <h4>⚡ 2. Primeiro Código Python</h4>
            
            <div class="code-example">
                <h5>🎉 Hello, World! - Seu Primeiro Programa:</h5>
                <pre><code># Este é seu primeiro programa Python!
print("🌟 Olá, mundo!")
print("Bem-vindo ao Python! 🐍")

# Variáveis são simples e poderosas
nome = "João"
idade = 25
altura = 1.75
programador = True

print(f"👋 Olá, {nome}!")
print(f"📊 Você tem {idade} anos e {altura}m de altura")
print(f"💻 É programador? {programador}")

# Operações matemáticas intuitivas
a = 10
b = 3

print(f"➕ {a} + {b} = {a + b}")
print(f"➖ {a} - {b} = {a - b}")
print(f"✖️ {a} * {b} = {a * b}")
print(f"➗ {a} / {b} = {a / b:.2f}")
print(f"🔢 {a} % {b} = {a % b}")  # Resto da divisão
print(f"⭐ {a} ** {b} = {a ** b}")  # Potenciação</code></pre>
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
        'content': '''<div class="module-header">
            <h3>🎯 Módulo 2 - Estruturas Condicionais e Loops</h3>
            <p class="module-intro"><strong>Dê inteligência aos seus programas!</strong> Aprenda a tomar decisões e repetir ações de forma eficiente. O poder real da programação começa aqui!</p>
        </div>
        
        <div class="content-section">
            <h4>🤔 1. Tomando Decisões com If/Else</h4>
            <p>Estruturas condicionais permitem que seu programa tome decisões baseadas em diferentes situações, tornando-o inteligente e interativo.</p>
            
            <div class="code-example">
                <h5>🎮 Sistema de Decisões Inteligente:</h5>
                <pre><code># Sistema de classificação de idade
idade = int(input("🎂 Digite sua idade: "))

if idade < 0:
    print("⚠️ Idade inválida!")
elif idade < 13:
    print("👶 Você é uma criança!")
    atividades = ["🎨 Desenhar", "🧩 Quebra-cabeças", "📚 Ler histórias"]
elif idade < 18:
    print("🧒 Você é um adolescente!")
    atividades = ["⚽ Esportes", "🎮 Jogos", "📱 Redes sociais", "📖 Estudar"]
elif idade < 65:
    print("👨‍💼 Você é um adulto!")
    atividades = ["💼 Trabalhar", "🏠 Cuidar da família", "🎯 Hobbies", "💡 Aprender"]
else:
    print("👴 Você é um idoso experiente!")
    atividades = ["🎣 Pescar", "📰 Ler jornal", "👨‍👩‍👧‍👦 Família", "🌳 Jardinagem"]

print(f"🎯 Atividades recomendadas: {', '.join(atividades)}")</code></pre>
            </div>
        </div>
        
        <div class="content-section">
            <h4>🔄 2. Loops - Repetindo Ações</h4>
            
            <div class="code-example">
                <h5>🔁 Loop FOR - Contando e Iterando:</h5>
                <pre><code># Contagem regressiva emocionante
print("🚀 Contagem regressiva para lançamento:")
for i in range(10, 0, -1):
    print(f"⏱️ {i}...")
print("🎆 LANÇAMENTO! 🚀")

# Tabuada interativa
numero = int(input("\\n🔢 Digite um número para ver a tabuada: "))
print(f"\\n📊 Tabuada do {numero}:")
print("=" * 30)

for i in range(1, 11):
    resultado = numero * i
    print(f"📐 {numero} × {i:2d} = {resultado:3d}")</code></pre>
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
        'content': '''<div class="module-header">
            <h3>📁 Módulo 3 - Manipulação de Arquivos</h3>
            <p class="module-intro"><strong>Domine o mundo dos dados!</strong> Aprenda a ler, escrever e processar diferentes tipos de arquivos. Transforme seu programa em um poderoso manipulador de dados.</p>
        </div>
        
        <div class="content-section">
            <h4>📂 1. Fundamentos de Arquivos</h4>
            <p>Python oferece ferramentas poderosas para trabalhar com arquivos. O gerenciamento adequado de arquivos é essencial para criar aplicações robustas.</p>
            
            <div class="code-example">
                <h5>🔓 Abrindo e Fechando Arquivos:</h5>
                <pre><code># Método recomendado - with statement
with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    # Arquivo é fechado automaticamente

# Modos de abertura
# 'r' - leitura (padrão)
# 'w' - escrita (sobrescreve o arquivo)
# 'a' - anexar (adiciona ao final)
# 'x' - criação exclusiva (falha se arquivo existir)
# 'r+' - leitura e escrita
# 'b' - modo binário (ex: 'rb', 'wb')

# Exemplo de escrita de arquivo
with open('dados.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("🚀 Sistema iniciado\\n")
    arquivo.write("✅ Configurações carregadas\\n")
    arquivo.write("🔄 Processamento em andamento\\n")

print("✅ Arquivo criado com sucesso!")</code></pre>
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
                'question': 'Qual é a vantagem de usar "with open()" ao trabalhar com arquivos?',
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
        'content': '''<div class="module-header">
            <h3>⚡ Módulo 4 - Funções e Módulos</h3>
            <p class="module-intro"><strong>Organize e reutilize seu código!</strong> Aprenda a criar funções poderosas e modular seu código para máxima eficiência e manutenibilidade.</p>
        </div>
        
        <div class="content-section">
            <h4>🔧 1. Criando Funções</h4>
            <p>Funções são blocos de código reutilizáveis que executam tarefas específicas, tornando seu programa mais organizado e eficiente.</p>
            
            <div class="code-example">
                <h5>🏗️ Definindo Funções:</h5>
                <pre><code># Função simples
def saudar():
    print("👋 Olá! Bem-vindo ao Python!")

# Chamando a função
saudar()

# Função com parâmetros
def saudar_pessoa(nome, sobrenome=""):
    if sobrenome:
        print(f"👋 Olá, {nome} {sobrenome}!")
    else:
        print(f"👋 Olá, {nome}!")

# Usando a função
saudar_pessoa("Maria")
saudar_pessoa("João", "Silva")

# Função com retorno
def calcular_idade(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

# Usando o retorno
idade = calcular_idade(1995)
print(f"🎂 Você tem {idade} anos")</code></pre>
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
        'content': '''<div class="module-header">
            <h3>🏢 Módulo 5 - Programação Orientada a Objetos</h3>
            <p class="module-intro"><strong>Construa código mais inteligente!</strong> Descubra o poder das classes e objetos para criar aplicações mais organizadas e escaláveis.</p>
        </div>
        
        <div class="content-section">
            <h4>💫 1. Classes e Objetos</h4>
            <p>A Programação Orientada a Objetos (POO) organiza o código em classes que representam objetos do mundo real.</p>
            
            <div class="code-example">
                <h5>🚗 Criando uma Classe:</h5>
                <pre><code>class Carro:
    """Classe que representa um carro"""
    
    def __init__(self, marca, modelo, ano, cor):
        """Construtor da classe"""
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False
        self.velocidade = 0
    
    def ligar(self):
        """Liga o carro"""
        if not self.ligado:
            self.ligado = True
            print(f"🔋 {self.modelo} ligado!")
        else:
            print(f"⚠️ {self.modelo} já está ligado!")
    
    def acelerar(self, incremento):
        """Acelera o carro"""
        if self.ligado:
            self.velocidade += incremento
            print(f"🏁 {self.modelo} acelerando: {self.velocidade} km/h")
        else:
            print("❌ Primeiro ligue o carro!")

# Criando objetos (instâncias)
meu_carro = Carro("Toyota", "Corolla", 2022, "Prata")
meu_carro.ligar()
meu_carro.acelerar(60)</code></pre>
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
        'content': '''<div class="module-header">
            <h3>⚠️ Módulo 6 - Tratamento de Exceções</h3>
            <p class="module-intro"><strong>Torne seus programas à prova de erros!</strong> Aprenda a antecipar, capturar e tratar erros de forma elegante e profissional.</p>
        </div>
        
        <div class="content-section">
            <h4>🛡️ 1. Fundamentos de Try/Except</h4>
            <p>O tratamento de exceções permite que seu programa continue funcionando mesmo quando encontra situações inesperadas.</p>
            
            <div class="code-example">
                <h5>🎯 Try/Except Básico:</h5>
                <pre><code># Exemplo COM tratamento
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"✅ Resultado: {resultado}")
except ValueError:
    print("❌ Erro: Você deve digitar um número válido!")
except ZeroDivisionError:
    print("❌ Erro: Não é possível dividir por zero!")

# Tratando múltiplas exceções
try:
    lista = [1, 2, 3]
    indice = int(input("Digite um índice (0-2): "))
    valor = lista[indice]
    print(f"🎯 Valor encontrado: {valor}")
except (ValueError, IndexError) as erro:
    print(f"❌ Erro capturado: {type(erro).__name__}")
    print(f"📝 Detalhes: {erro}")

# Finally - sempre executa
try:
    arquivo = open('teste.txt', 'r')
    conteudo = arquivo.read()
except FileNotFoundError:
    print("❌ Arquivo não encontrado!")
finally:
    print("🔄 Limpeza concluída!")</code></pre>
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
        'content': '''<div class="module-header">
            <h3>📚 Módulo 7 - Bibliotecas e APIs</h3>
            <p class="module-intro"><strong>Expanda o poder do Python!</strong> Descubra como usar bibliotecas externas e APIs para criar aplicações incríveis e conectadas.</p>
        </div>
        
        <div class="content-section">
            <h4>📦 1. Instalando e Usando Bibliotecas</h4>
            <p>Python possui um ecossistema rico de bibliotecas que facilitam o desenvolvimento de projetos complexos.</p>
            
            <div class="code-example">
                <h5>🔧 Gerenciando Bibliotecas com pip:</h5>
                <pre><code># Comandos do terminal
# pip install requests        # Instala uma biblioteca
# pip install requests==2.25.1  # Instala versão específica
# pip list                   # Lista bibliotecas instaladas
# pip show requests          # Mostra detalhes da biblioteca
# pip uninstall requests     # Remove biblioteca

# Exemplo de uso da biblioteca requests
import requests

def consultar_cep(cep):
    """Consulta informações de um CEP"""
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            dados = response.json()
            if 'erro' not in dados:
                return dados
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
        return None

# Testando a função
resultado = consultar_cep("01310-100")
if resultado:
    print(f"🏠 Endereço encontrado: {resultado['logradouro']}")
else:
    print("❌ CEP não encontrado!")

# Usando números aleatórios
import random

numero_sorteado = random.randint(1, 100)
print(f"🎲 Número sorteado: {numero_sorteado}")

frutas = ['🍎', '🍌', '🍊', '🍇', '🥝']
fruta_escolhida = random.choice(frutas)
print(f"🍓 Fruta escolhida: {fruta_escolhida}")</code></pre>
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
        'content': '''<div class="module-header">
            <h3>🗄️ Módulo 8 - Banco de Dados</h3>
            <p class="module-intro"><strong>Persista seus dados!</strong> Aprenda a armazenar, consultar e gerenciar dados usando bancos de dados relacionais com Python.</p>
        </div>
        
        <div class="content-section">
            <h4>📦 1. SQLite - Banco Local</h4>
            <p>SQLite é um banco de dados leve e embutido, perfeito para desenvolvimento e aplicações pequenas e médias.</p>
            
            <div class="code-example">
                <h5>🔗 Conectando ao SQLite:</h5>
                <pre><code>import sqlite3
from datetime import datetime

# Conectando ao banco (cria se não existir)
conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

# Criando tabela de funcionários
cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        salario REAL NOT NULL,
        data_admissao DATE,
        ativo BOOLEAN DEFAULT 1
    )
''')

conexao.commit()  # Salva as mudanças
print("🏢 Tabelas criadas com sucesso!")

# Inserindo dados
cursor.execute('''
    INSERT INTO funcionarios (nome, cargo, salario, data_admissao)
    VALUES (?, ?, ?, ?)
''', ("Ana Silva", "Desenvolvedora", 8500, datetime.now().date()))

conexao.commit()
print("✅ Funcionário adicionado!")

# Consultando dados
cursor.execute('SELECT * FROM funcionarios WHERE ativo = 1')
funcionarios = cursor.fetchall()

print("\\n👥 FUNCIONÁRIOS:")
for func in funcionarios:
    id_func, nome, cargo, salario, data_admissao, ativo = func
    print(f"👤 {nome} - {cargo} - R$ {salario:.2f}")

# Fechando conexão
conexao.close()
print("🔒 Conexão fechada.")</code></pre>
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
        'content': '''<div class="module-header">
            <h3>🎆 Módulo 9 - Projeto Final</h3>
            <p class="module-intro"><strong>Integre todos os conceitos!</strong> Crie um projeto completo que demonstra domínio em Python, desde fundamentos até conceitos avançados.</p>
        </div>
        
        <div class="content-section">
            <h4>🎯 1. Planejamento do Projeto</h4>
            <p>Um projeto bem-sucedido começa com planejamento adequado. Vamos criar um sistema de gestão de biblioteca que integra todos os conceitos aprendidos.</p>
            
            <div class="code-example">
                <h5>📋 Estrutura do Projeto:</h5>
                <pre><code># biblioteca_sistema/
# │
# ├── main.py              # Arquivo principal
# ├── models.py            # Classes e modelos
# ├── database.py          # Gerenciamento do banco
# ├── utils.py             # Funções utilitárias
# ├── config.py            # Configurações
# └── dados/
#     └── biblioteca.db     # Banco de dados

# Requisitos do sistema:
# 1. Cadastro de livros e usuários
# 2. Sistema de empréstimos
# 3. Relatórios e consultas
# 4. Interface de menu
# 5. Persistência de dados
# 6. Tratamento de erros
# 7. Documentação

class Config:
    """Configurações do sistema"""
    
    DATABASE_NAME = 'dados/biblioteca.db'
    MAX_EMPRESTIMOS_POR_USUARIO = 3
    DIAS_EMPRESTIMO = 14
    MULTA_POR_DIA_ATRASO = 2.00

class Livro:
    """Classe para representar um livro"""
    
    def __init__(self, id, titulo, autor, isbn, categoria):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.categoria = categoria
        self.disponivel = True
    
    def __str__(self):
        status = "✅ Disponível" if self.disponivel else "❌ Emprestado"
        return f"📚 {self.titulo} - {self.autor} ({status})"

class SistemaBiblioteca:
    """Sistema completo de gestão de biblioteca"""
    
    def __init__(self):
        self.livros = {}
        self.usuarios = {}
        self.emprestimos = {}
        self.proximo_id_livro = 1
    
    def adicionar_livro(self, titulo, autor, isbn, categoria):
        """Adiciona um novo livro"""
        try:
            livro = Livro(
                id=self.proximo_id_livro,
                titulo=titulo,
                autor=autor,
                isbn=isbn,
                categoria=categoria
            )
            
            self.livros[livro.id] = livro
            self.proximo_id_livro += 1
            
            print(f"✅ Livro '{titulo}' adicionado com sucesso!")
            return livro.id
            
        except Exception as e:
            print(f"❌ Erro ao adicionar livro: {e}")
            return None

# Exemplo de uso
sistema = SistemaBiblioteca()
sistema.adicionar_livro(
    "Python para Iniciantes", 
    "João Silva", 
    "978-1234567890", 
    "Programação"
)

print("✅ Sistema de biblioteca implementado!")
print("🎆 Projeto final concluído!")</code></pre>
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