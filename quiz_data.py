# -*- coding: utf-8 -*-
"""
Dados dos módulos e quizzes para o Sistema de Aprendizado Python
"""

MODULES = {
    1: {
        'title': 'Fundamentos do Python',
        'description': 'Conceitos básicos da linguagem Python.',
        'video_url': '',
        'content': '''
        <h3>Módulo 1 - Fundamentos do Python</h3>
        <p><strong>Introdução à programação com Python</strong></p>
        
        <h4>1. Variáveis e Tipos de Dados</h4>
        <p>Python trabalha com diferentes tipos de dados:</p>
        <pre><code># Números
idade = 25
altura = 1.75
preco = 10.50

# Texto (strings)
nome = "João"
cidade = 'São Paulo'

# Booleanos
ativo = True
possui_desconto = False

# Listas
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]

# Dicionários
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "Rio de Janeiro"
}</code></pre>
        
        <h4>2. Operações Básicas</h4>
        <pre><code># Operações matemáticas
soma = 10 + 5
subtracao = 10 - 5
multiplicacao = 10 * 5
divisao = 10 / 5
potencia = 10 ** 2

# Operações com strings
saudacao = "Olá, " + nome
mensagem = f"Meu nome é {nome} e tenho {idade} anos"

# Comparações
maior = 10 > 5
igual = 10 == 10
diferente = 10 != 5</code></pre>
        
        <h4>3. Entrada e Saída de Dados</h4>
        <pre><code># Entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Saída de dados
print("Nome:", nome)
print(f"Idade: {idade}")
print("Bem-vindo ao sistema!")</code></pre>
        ''',
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
                'options': [
                    'lista = [1, 2, 3]',
                    'lista = (1, 2, 3)',
                    'lista = {1, 2, 3}',
                    'lista = 1, 2, 3',
                    'lista = <1, 2, 3>'
                ],
                'correct_answer': 'lista = [1, 2, 3]'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual função é usada para receber entrada do usuário?',
                'options': ['print()', 'input()', 'get()', 'read()', 'scan()'],
                'correct_answer': 'input()'
            }
        ]
    },
    2: {
        'title': 'Estruturas de Controle',
        'description': 'Condicionais, loops e estruturas de decisão.',
        'video_url': '',
        'content': '''
        <h3>Módulo 2 - Estruturas de Controle</h3>
        
        <h4>1. Estruturas Condicionais</h4>
        <pre><code># If simples
idade = 18
if idade >= 18:
    print("Maior de idade")

# If-else
if idade >= 18:
    print("Pode votar")
else:
    print("Não pode votar")

# If-elif-else
nota = 85
if nota >= 90:
    print("Nota A")
elif nota >= 80:
    print("Nota B")
elif nota >= 70:
    print("Nota C")
else:
    print("Precisa melhorar")</code></pre>
        
        <h4>2. Loops</h4>
        <pre><code># Loop for com range
for i in range(5):
    print(f"Contagem: {i}")

# Loop for com lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Loop while
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1</code></pre>
        
        <h4>3. Controle de Loop</h4>
        <pre><code># Break - para o loop
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue - pula para próxima iteração
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Número ímpar: {i}")</code></pre>
        ''',
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
                'options': [
                    'for i in range(10):',
                    'for i = 1 to 10:',
                    'loop 10 times:',
                    'repeat(10):',
                    'while i <= 10:'
                ],
                'correct_answer': 'for i in range(10):'
            }
        ]
    },
    3: {
        'title': 'Manipulação de Arquivos e Dados',
        'description': 'Trabalhando com diferentes formatos de arquivo e dados.',
        'video_url': '',
        'content': '''
        <h3>Módulo 3 - Manipulação de Arquivos e Dados</h3>
        
        <h4>1. Trabalhando com Arquivos</h4>
        <pre><code># Lendo arquivo
with open('dados.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Escrevendo arquivo
dados = ["Python", "é", "incrível"]
with open('saida.txt', 'w') as arquivo:
    for palavra in dados:
        arquivo.write(palavra + '\n')</code></pre>
        
        <h4>2. Trabalhando com CSV</h4>
        <pre><code>import csv

# Lendo CSV
with open('dados.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

# Escrevendo CSV
dados = [['Nome', 'Idade'], ['João', 25], ['Maria', 30]]
with open('pessoas.csv', 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)</code></pre>
        
        <h4>3. Trabalhando com JSON</h4>
        <pre><code>import json

# Dados Python para JSON
dados = {"nome": "João", "idade": 25}
with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo)

# JSON para Python
with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)
    print(dados)</code></pre>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual módulo é usado para trabalhar com arquivos CSV?',
                'options': ['csv', 'file', 'pandas', 'json', 'excel'],
                'correct_answer': 'csv'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como você abre um arquivo para escrita?',
                'options': [
                    'open("arquivo.txt", "w")',
                    'file("arquivo.txt", "write")',
                    'create("arquivo.txt")',
                    'write("arquivo.txt")'
                ],
                'correct_answer': 'open("arquivo.txt", "w")'
            }
        ]
    },
    4: {
        'title': 'Bancos de Dados com SQLite e PostgreSQL', 
        'description': 'Conceitos de banco de dados relacionais.',
        'video_url': '',
        'content': '''
        <h3>Módulo 4 - Bancos de Dados</h3>
        <p>Aprenda a trabalhar com bancos de dados usando Python.</p>
        <h4>SQLite Básico</h4>
        <pre><code>import sqlite3
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT)")
cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", ("João",))
cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall()
conn.commit()
conn.close()
        </code></pre>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual comando SQL é usado para buscar dados?',
                'options': ['INSERT', 'UPDATE', 'DELETE', 'SELECT', 'CREATE'],
                'correct_answer': 'SELECT'
            }
        ]
    },
    5: {
        'title': 'Programação Web com Flask',
        'description': 'Desenvolvimento web com Python.',
        'video_url': '',
        'content': '''
        <h3>Módulo 5 - Flask Web Development</h3>
        
        <h4>1. Aplicação Flask Básica</h4>
        <pre><code>from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, Flask!'

@app.route('/usuario/&lt;nome&gt;')
def usuario(nome):
    return f'Olá, {nome}!'

if __name__ == '__main__':
    app.run(debug=True)</code></pre>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Como você define uma rota no Flask?',
                'options': [
                    '@app.route("/caminho")',
                    '@route("/caminho")',
                    'app.add_route("/caminho")'
                ],
                'correct_answer': '@app.route("/caminho")'
            }
        ]
    },
    6: {
        'title': 'APIs REST com Flask',
        'description': 'Criando e consumindo APIs RESTful.',
        'video_url': '',
        'content': '''
        <h3>Módulo 6 - APIs REST</h3>
        
        <h4>1. API Básica com Flask</h4>
        <pre><code>from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "João"},
    {"id": 2, "nome": "Maria"}
]

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)

@app.route('/api/usuarios', methods=['POST'])
def create_usuario():
    novo_usuario = request.json
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201</code></pre>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual método HTTP é usado para criar recursos?',
                'options': ['GET', 'POST', 'PUT', 'DELETE'],
                'correct_answer': 'POST'
            }
        ]
    },
    7: {
        'title': 'Testes Automatizados',
        'description': 'Garantindo qualidade com testes.',
        'video_url': '',
        'content': '''
        <h3>Módulo 7 - Testes Automatizados</h3>
        
        <h4>1. Testes com unittest</h4>
        <pre><code>import unittest

def somar(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(somar(2, 3), 5)
    
    def test_soma_negativos(self):
        self.assertEqual(somar(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()</code></pre>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual módulo é usado para testes em Python?',
                'options': ['test', 'unittest', 'pytest', 'testing'],
                'correct_answer': 'unittest'
            }
        ]
    },
    8: {
        'title': 'Deploy e Produção',
        'description': 'Colocando aplicações em produção.',
        'video_url': '',
        'content': '''
        <h3>Módulo 8 - Deploy e Produção</h3>
        
        <h4>1. Preparando para Deploy</h4>
        <pre><code># requirements.txt
Flask==2.3.0
gunicorn==21.2.0

# Configuração de produção
import os

class Config:
    DEBUG = os.environ.get('DEBUG', False)
    DATABASE_URL = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')</code></pre>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual arquivo lista as dependências do projeto?',
                'options': ['requirements.txt', 'packages.txt', 'deps.txt'],
                'correct_answer': 'requirements.txt'
            }
        ]
    },
    9: {
        'title': 'Projeto Final',
        'description': 'Aplicando tudo que aprendeu em um projeto completo.',
        'video_url': '',
        'content': '''
        <h3>Módulo 9 - Projeto Final</h3>
        
        <p>Neste módulo final, você irá criar um projeto completo que integra todos os conceitos aprendidos:</p>
        
        <h4>Especificações do Projeto</h4>
        <ul>
            <li>Sistema web com Flask</li>
            <li>Banco de dados SQLite/PostgreSQL</li>
            <li>API REST</li>
            <li>Testes automatizados</li>
            <li>Deploy em produção</li>
        </ul>
        
        <h4>Funcionalidades</h4>
        <ul>
            <li>Autenticação de usuários</li>
            <li>CRUD completo</li>
            <li>Interface web responsiva</li>
            <li>Documentação da API</li>
        </ul>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual é o objetivo do projeto final?',
                'options': [
                    'Aprender uma nova linguagem',
                    'Integrar todos os conceitos aprendidos',
                    'Fazer um projeto simples',
                    'Testar apenas Flask'
                ],
                'correct_answer': 'Integrar todos os conceitos aprendidos'
            }
        ]
    }
}

# Exame final
FINAL_EXAM = {
    'title': 'Exame Final - Python Completo',
    'description': 'Teste seus conhecimentos em todos os módulos.',
    'questions': [
        {
            'type': 'multiple_choice',
            'question': 'Qual é a sintaxe correta para uma função em Python?',
            'options': [
                'function nome():',
                'def nome():',
                'func nome():',
                'create nome():'
            ],
            'correct_answer': 'def nome():'
        },
        {
            'type': 'multiple_choice',
            'question': 'Como você importa uma biblioteca em Python?',
            'options': [
                'include biblioteca',
                'import biblioteca',
                'use biblioteca',
                'require biblioteca'
            ],
            'correct_answer': 'import biblioteca'
        },
        {
            'type': 'multiple_choice',
            'question': 'Qual método HTTP é usado para atualizar dados?',
            'options': ['GET', 'POST', 'PUT', 'DELETE'],
            'correct_answer': 'PUT'
        },
        {
            'type': 'multiple_choice',
            'question': 'Qual é a principal vantagem dos testes automatizados?',
            'options': [
                'Tornam o código mais rápido',
                'Garantem qualidade e detectam bugs',
                'Reduzem o tamanho do código',
                'Facilitam o deploy'
            ],
            'correct_answer': 'Garantem qualidade e detectam bugs'
        }
    ],
    'passing_score': 70
}