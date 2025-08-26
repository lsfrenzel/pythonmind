# Python Learning Modules and Quiz Data
MODULES = {
    1: {
        'title': 'Fundamentos da Programação em Python',
        'description': 'Base para quem está começando a programar, com foco em lógica e sintaxe.',
        'video_url': '',  # Admin can set this
        'content': '''
        <h3>🧱 Módulo 1 – Fundamentos da Programação em Python</h3>
        <p><strong>Base para quem está começando a programar, com foco em lógica e sintaxe.</strong></p>
        
        <h4>📚 1. Instalação do Python e VSCode</h4>
        <p>Python é uma linguagem de programação interpretada e de alto nível. Para começar:</p>
        <pre><code># Verificar se o Python está instalado
python --version
# ou
python3 --version</code></pre>
        <p><strong>VSCode:</strong> Editor de código gratuito com excelente suporte para Python através de extensões.</p>
        
        <h4>🔢 2. Variáveis e Tipos de Dados</h4>
        <p>Em Python, você não precisa declarar o tipo da variável. Ela é definida automaticamente:</p>
        <pre><code># Tipos básicos
nome = "João"           # String (texto)
idade = 25              # Integer (número inteiro)
altura = 1.75           # Float (número decimal)
ativo = True            # Boolean (verdadeiro/falso)

# Verificar o tipo
print(type(nome))       # &lt;class 'str'&gt;
print(type(idade))      # &lt;class 'int'&gt;</code></pre>
        
        <h4>⚡ 3. Operadores</h4>
        <p><strong>Aritméticos:</strong></p>
        <pre><code>a = 10
b = 3

print(a + b)    # 13 (soma)
print(a - b)    # 7 (subtração)
print(a * b)    # 30 (multiplicação)
print(a / b)    # 3.333... (divisão)
print(a // b)   # 3 (divisão inteira)
print(a % b)    # 1 (resto da divisão)
print(a ** b)   # 1000 (potência)</code></pre>
        
        <p><strong>Relacionais:</strong></p>
        <pre><code>x = 5
y = 10

print(x == y)   # False (igual)
print(x != y)   # True (diferente)
print(x < y)    # True (menor que)
print(x > y)    # False (maior que)
print(x <= y)   # True (menor ou igual)
print(x >= y)   # False (maior ou igual)</code></pre>
        
        <h4>🔀 4. Estruturas Condicionais</h4>
        <pre><code>idade = 18

if idade >= 18:
    print("Maior de idade")
elif idade >= 16:
    print("Pode trabalhar como menor aprendiz")
else:
    print("Menor de idade")

# Operador ternário
status = "adulto" if idade >= 18 else "menor"</code></pre>
        
        <h4>🔄 5. Laços de Repetição</h4>
        <p><strong>Loop while:</strong></p>
        <pre><code>contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1</code></pre>
        
        <p><strong>Loop for:</strong></p>
        <pre><code># Iterando sobre uma sequência
for numero in range(5):
    print(numero)  # 0, 1, 2, 3, 4

# Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)</code></pre>
        
        <h4>📦 6. Estruturas de Dados</h4>
        <p><strong>Listas (mutáveis):</strong></p>
        <pre><code>numeros = [1, 2, 3, 4, 5]
numeros.append(6)        # Adiciona elemento
numeros.remove(3)        # Remove elemento
print(numeros[0])        # Acessa primeiro elemento</code></pre>
        
        <p><strong>Tuplas (imutáveis):</strong></p>
        <pre><code>coordenadas = (10, 20)
x, y = coordenadas      # Desempacotamento</code></pre>
        
        <p><strong>Dicionários:</strong></p>
        <pre><code>pessoa = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "São Paulo"
}
print(pessoa["nome"])   # Ana
pessoa["profissao"] = "Engenheira"  # Adiciona nova chave</code></pre>
        
        <h4>🔧 7. Funções</h4>
        <pre><code>def saudacao(nome, sobrenome=""):
    """Função que retorna uma saudação personalizada"""
    if sobrenome:
        return f"Olá, {nome} {sobrenome}!"
    return f"Olá, {nome}!"

# Chamando a função
mensagem = saudacao("Carlos", "Silva")
print(mensagem)  # Olá, Carlos Silva!</code></pre>
        
        <h4>📁 8. Módulos e Pacotes</h4>
        <pre><code># Importando módulos
import math
from datetime import datetime

# Usando funções do módulo
raiz = math.sqrt(16)    # 4.0
agora = datetime.now()  # Data/hora atual</code></pre>
        
        <h4>⚠️ 9. Tratamento de Erros</h4>
        <pre><code>try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: Digite apenas números!")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    print("Operação finalizada.")</code></pre>
        
        <h4>🎯 Objetivos de Aprendizagem</h4>
        <p>Ao final deste módulo, você será capaz de:</p>
        <ul>
            <li>Criar e executar programas Python básicos</li>
            <li>Trabalhar com variáveis e diferentes tipos de dados</li>
            <li>Usar estruturas condicionais e loops</li>
            <li>Manipular listas, tuplas e dicionários</li>
            <li>Criar funções reutilizáveis</li>
            <li>Tratar erros adequadamente</li>
        </ul>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual é a extensão padrão para arquivos Python?',
                'options': ['.python', '.py', '.pt', '.pyt', '.pyc'],
                'correct_answer': '.py'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como você declara uma variável em Python?',
                'options': [
                    'var nome = "João"',
                    'String nome = "João"',
                    'nome = "João"',
                    'declare nome = "João"',
                    'int nome = "João"'
                ],
                'correct_answer': 'nome = "João"'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual é a principal diferença entre uma lista e uma tupla?',
                'options': [
                    'Listas usam [] e tuplas usam ()',
                    'Listas são mutáveis e tuplas são imutáveis',
                    'Ambas as anteriores estão corretas',
                    'Não há diferença entre elas',
                    'Tuplas são mais rápidas que listas'
                ],
                'correct_answer': 'Ambas as anteriores estão corretas'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual operador é usado para potenciação em Python?',
                'options': ['^', '**', 'pow', '*', '//'],
                'correct_answer': '**'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que acontece quando você usa "try/except" em Python?',
                'options': [
                    'Executa código apenas uma vez',
                    'Repete o código várias vezes',
                    'Trata erros e exceções',
                    'Define uma função',
                    'Importa um módulo'
                ],
                'correct_answer': 'Trata erros e exceções'
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
        
        <h4>🎮 1. Jogo da Adivinhação</h4>
        <p>Vamos criar um jogo onde o usuário deve adivinhar um número:</p>
        <pre><code>import random

# Gera número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 7

print("🎯 Jogo da Adivinhação!")
print(f"Tente adivinhar o número entre 1 e 100. Você tem {max_tentativas} tentativas.")

while tentativas < max_tentativas:
    try:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        
        if palpite == numero_secreto:
            print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas!")
            break
        elif palpite < numero_secreto:
            print("📈 Muito baixo! Tente um número maior.")
        else:
            print("📉 Muito alto! Tente um número menor.")
            
        restantes = max_tentativas - tentativas
        if restantes > 0:
            print(f"Tentativas restantes: {restantes}")
    except ValueError:
        print("❌ Digite apenas números!")

if tentativas == max_tentativas:
    print(f"😞 Que pena! O número era {numero_secreto}").</code></pre>
        
        <h4>🧮 2. Calculadora Avançada</h4>
        <pre><code>def calculadora():
    print("🧮 Calculadora Python")
    print("Operações: +, -, *, /, ** (potência), // (divisão inteira), % (resto)")
    
    while True:
        try:
            # Input da expressão
            expressao = input("\nDigite a operação (ou 'sair' para terminar): ")
            
            if expressao.lower() == 'sair':
                break
                
            # Avalia a expressão matemática
            resultado = eval(expressao)
            print(f"Resultado: {resultado}")
            
        except ZeroDivisionError:
            print("❌ Erro: Divisão por zero!")
        except Exception as e:
            print(f"❌ Erro na expressão: {e}")
    
    print("Calculadora encerrada!")

# Executar calculadora
calculadora()</code></pre>
        
        <h4>🔐 3. Gerador de Senhas Seguras</h4>
        <pre><code>import random
import string

def gerar_senha(tamanho=12, incluir_simbolos=True):
    """Gera uma senha aleatória segura"""
    
    # Caracteres disponíveis
    minusculas = string.ascii_lowercase
    maiusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Monta conjunto de caracteres
    caracteres = minusculas + maiusculas + numeros
    if incluir_simbolos:
        caracteres += simbolos
    
    # Gera senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def validar_senha(senha):
    """Valida a força da senha"""
    pontos = 0
    feedback = []
    
    if len(senha) >= 8:
        pontos += 1
    else:
        feedback.append("Use pelo menos 8 caracteres")
    
    if any(c.islower() for c in senha):
        pontos += 1
    else:
        feedback.append("Inclua letras minúsculas")
    
    if any(c.isupper() for c in senha):
        pontos += 1
    else:
        feedback.append("Inclua letras maiúsculas")
    
    if any(c.isdigit() for c in senha):
        pontos += 1
    else:
        feedback.append("Inclua números")
    
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in senha):
        pontos += 1
    else:
        feedback.append("Inclua símbolos especiais")
    
    # Classifica força
    if pontos >= 4:
        nivel = "🔒 Forte"
    elif pontos >= 3:
        nivel = "🔓 Média"
    else:
        nivel = "⚠️ Fraca"
    
    return nivel, feedback

# Exemplo de uso
print("🔐 Gerador de Senhas")
senha = gerar_senha(16, True)
print(f"Senha gerada: {senha}")

nivel, dicas = validar_senha(senha)
print(f"Força da senha: {nivel}")</code></pre>
        
        <h4>📱 4. Agenda de Contatos</h4>
        <pre><code>import json

class AgendaContatos:
    def __init__(self, arquivo='contatos.json'):
        self.arquivo = arquivo
        self.contatos = self.carregar_contatos()
    
    def carregar_contatos(self):
        """Carrega contatos do arquivo"""
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def salvar_contatos(self):
        """Salva contatos no arquivo"""
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.contatos, f, ensure_ascii=False, indent=2)
    
    def adicionar_contato(self, nome, telefone, email=""):
        """Adiciona novo contato"""
        self.contatos[nome] = {
            'telefone': telefone,
            'email': email
        }
        self.salvar_contatos()
        print(f"✅ Contato {nome} adicionado!")
    
    def buscar_contato(self, nome):
        """Busca contato por nome"""
        if nome in self.contatos:
            contato = self.contatos[nome]
            print(f"📞 {nome}")
            print(f"   Telefone: {contato['telefone']}")
            print(f"   Email: {contato['email']}")
        else:
            print(f"❌ Contato {nome} não encontrado")
    
    def listar_contatos(self):
        """Lista todos os contatos"""
        if not self.contatos:
            print("📭 Agenda vazia")
            return
        
        print("📋 Lista de Contatos:")
        for nome, dados in self.contatos.items():
            print(f"   {nome} - {dados['telefone']}")

# Exemplo de uso
agenda = AgendaContatos()
agenda.adicionar_contato("João", "(11) 99999-9999", "joao@email.com")
agenda.listar_contatos()</code></pre>
        
        <h4>🏦 5. Sistema Bancário Simples</h4>
        <pre><code>class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.historico = []
        self.adicionar_historico(f"Conta criada - Saldo inicial: R$ {saldo_inicial:.2f}")
    
    def adicionar_historico(self, operacao):
        """Adiciona operação ao histórico"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.historico.append(f"{timestamp} - {operacao}")
    
    def depositar(self, valor):
        """Realiza depósito"""
        if valor > 0:
            self.saldo += valor
            self.adicionar_historico(f"Depósito: R$ {valor:.2f}")
            print(f"✅ Depósito de R$ {valor:.2f} realizado. Saldo: R$ {self.saldo:.2f}")
        else:
            print("❌ Valor deve ser maior que zero")
    
    def sacar(self, valor):
        """Realiza saque"""
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                self.adicionar_historico(f"Saque: R$ {valor:.2f}")
                print(f"✅ Saque de R$ {valor:.2f} realizado. Saldo: R$ {self.saldo:.2f}")
            else:
                print("❌ Saldo insuficiente")
        else:
            print("❌ Valor deve ser maior que zero")
    
    def transferir(self, conta_destino, valor):
        """Transfere para outra conta"""
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            
            self.adicionar_historico(f"Transferência enviada para {conta_destino.titular}: R$ {valor:.2f}")
            conta_destino.adicionar_historico(f"Transferência recebida de {self.titular}: R$ {valor:.2f}")
            
            print(f"✅ Transferência de R$ {valor:.2f} realizada para {conta_destino.titular}")
        else:
            print("❌ Valor inválido ou saldo insuficiente")
    
    def extrato(self):
        """Mostra extrato da conta"""
        print(f"\n💳 Extrato - {self.titular}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("\n📋 Histórico:")
        for operacao in self.historico[-10:]:  # Últimas 10 operações
            print(f"   {operacao}")

# Exemplo de uso
conta1 = ContaBancaria("Maria Silva", 1000)
conta2 = ContaBancaria("João Santos", 500)

conta1.depositar(200)
conta1.sacar(150)
conta1.transferir(conta2, 300)
conta1.extrato()</code></pre>
        
        <h4>🎯 Conceitos Importantes</h4>
        <ul>
            <li><strong>Algoritmos:</strong> Sequência de passos para resolver problemas</li>
            <li><strong>Modularização:</strong> Dividir código em funções e classes</li>
            <li><strong>Validação:</strong> Verificar se os dados de entrada são válidos</li>
            <li><strong>Persistência:</strong> Salvar dados em arquivos para usar depois</li>
            <li><strong>Interface do usuário:</strong> Interação clara e intuitiva</li>
        </ul>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Qual módulo do Python é usado para gerar números aleatórios?',
                'options': ['math', 'random', 'os', 'sys', 'datetime'],
                'correct_answer': 'random'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como você converte uma string para inteiro em Python?',
                'options': ['integer(string)', 'int(string)', 'convert(string)', 'parse(string)', 'string.to_int()'],
                'correct_answer': 'int(string)'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual função é usada para avaliar uma expressão matemática em string?',
                'options': ['eval()', 'exec()', 'calculate()', 'math()', 'compute()'],
                'correct_answer': 'eval()'
            },
            {
                'type': 'multiple_choice',
                'question': 'Para salvar dados em formato JSON, qual módulo você deve importar?',
                'options': ['file', 'json', 'data', 'save', 'pickle'],
                'correct_answer': 'json'
            },
            {
                'type': 'multiple_choice',
                'question': 'Em programação orientada a objetos, o que é uma classe?',
                'options': [
                    'Um tipo de variável',
                    'Uma função especial',
                    'Um modelo para criar objetos',
                    'Um tipo de lista',
                    'Um arquivo de dados'
                ],
                'correct_answer': 'Um modelo para criar objetos'
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
                'options': ['r', 'w', 'r+', 'a', 'x'],
                'correct_answer': 'r+'
            },
            {
                'type': 'multiple_choice',
                'question': 'Que formato JSON usa para representar dados?',
                'options': ['XML', 'Texto simples', 'Chave-valor', 'Binário', 'Tabular'],
                'correct_answer': 'Chave-valor'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual módulo Python é usado para trabalhar com arquivos CSV?',
                'options': ['csv', 'file', 'pandas', 'json', 'excel'],
                'correct_answer': 'csv'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como você abre um arquivo para escrita em Python?',
                'options': [
                    'open("arquivo.txt", "w")',
                    'file("arquivo.txt", "write")',
                    'create("arquivo.txt")',
                    'write("arquivo.txt")',
                    'new_file("arquivo.txt")'
                ],
                'correct_answer': 'open("arquivo.txt", "w")'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual é a principal vantagem do formato CSV?',
                'options': [
                    'Suporta imagens',
                    'É compatível com Excel e outros programas',
                    'Permite criptografia',
                    'É mais rápido que JSON',
                    'Ocupa menos espaço que TXT'
                ],
                'correct_answer': 'É compatível com Excel e outros programas'
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
                    'Create, Relate, Use, Drop',
                    'Control, Read, Update, Data'
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
                    'Recursos avançados de segurança',
                    'É mais rápido que PostgreSQL'
                ],
                'correct_answer': 'Não precisa de servidor separado'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual comando SQL é usado para buscar dados?',
                'options': ['INSERT', 'UPDATE', 'DELETE', 'SELECT', 'CREATE'],
                'correct_answer': 'SELECT'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual biblioteca Python é um ORM popular?',
                'options': ['sqlite3', 'psycopg2', 'SQLAlchemy', 'mysql', 'dbapi'],
                'correct_answer': 'SQLAlchemy'
            },
            {
                'type': 'multiple_choice',
                'question': 'Em bancos relacionais, o que é uma chave primária?',
                'options': [
                    'Um campo que pode ser nulo',
                    'Um identificador único para cada registro',
                    'Um campo de texto longo',
                    'Uma tabela secundária',
                    'Um tipo de dados especial'
                ],
                'correct_answer': 'Um identificador único para cada registro'
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
                    'Um protocolo de rede',
                    'Um arquivo de configuração'
                ],
                'correct_answer': 'Uma URL mapeada para uma função Python'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual template engine o Flask usa por padrão?',
                'options': ['Django Templates', 'Jinja2', 'Mustache', 'Handlebars', 'Blade'],
                'correct_answer': 'Jinja2'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como você define uma rota no Flask?',
                'options': [
                    '@app.route("/caminho")',
                    '@route("/caminho")',
                    'app.add_route("/caminho")',
                    'route("/caminho")',
                    'app.path("/caminho")'
                ],
                'correct_answer': '@app.route("/caminho")'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual método HTTP é usado para enviar dados de formulário?',
                'options': ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
                'correct_answer': 'POST'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que significa HTTP?',
                'options': [
                    'HyperText Transfer Protocol',
                    'HyperText Transport Protocol',
                    'HyperText Transmission Protocol',
                    'HyperText Transfer Process',
                    'HyperText Transport Process'
                ],
                'correct_answer': 'HyperText Transfer Protocol'
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
                'options': ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
                'correct_answer': 'POST'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que significa REST?',
                'options': [
                    'Representational State Transfer',
                    'Remote Execution State Transfer',
                    'Resource Execution State Transfer',
                    'Relational State Transfer',
                    'Request State Transfer'
                ],
                'correct_answer': 'Representational State Transfer'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual código de status HTTP indica sucesso?',
                'options': ['200', '404', '500', '301', '400'],
                'correct_answer': '200'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual formato é mais usado para troca de dados em APIs?',
                'options': ['XML', 'JSON', 'CSV', 'HTML', 'TXT'],
                'correct_answer': 'JSON'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual método HTTP é usado para atualizar um recurso?',
                'options': ['GET', 'POST', 'PUT', 'DELETE', 'HEAD'],
                'correct_answer': 'PUT'
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
                    'Testes de interface',
                    'Testes de banco de dados'
                ],
                'correct_answer': 'Testes de funções isoladas'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual biblioteca é mais moderna para testes em Python?',
                'options': ['unittest', 'pytest', 'nose', 'doctest', 'testify'],
                'correct_answer': 'pytest'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual é o comando para executar testes com pytest?',
                'options': ['python test', 'pytest', 'run tests', 'test.py', 'python -m test'],
                'correct_answer': 'pytest'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que é um mock em testes?',
                'options': [
                    'Um tipo de erro',
                    'Uma simulação de dependência externa',
                    'Um teste que falha',
                    'Um banco de dados de teste',
                    'Uma função de validação'
                ],
                'correct_answer': 'Uma simulação de dependência externa'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual é a principal vantagem dos testes automatizados?',
                'options': [
                    'Tornam o código mais rápido',
                    'Reduzem bugs e garantem qualidade',
                    'Economizam espaço em disco',
                    'Facilitam a instalação',
                    'Melhoram a interface gráfica'
                ],
                'correct_answer': 'Reduzem bugs e garantem qualidade'
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
                    'Lista de funcionalidades',
                    'Lista de usuários do sistema'
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
                    'Para facilitar o desenvolvimento',
                    'Para organizar melhor os arquivos'
                ],
                'correct_answer': 'Para ocultar informações sensíveis'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual comando gera o arquivo requirements.txt?',
                'options': [
                    'pip install requirements',
                    'pip freeze > requirements.txt',
                    'python requirements.txt',
                    'pip requirements',
                    'pip list > requirements.txt'
                ],
                'correct_answer': 'pip freeze > requirements.txt'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que é HTTPS?',
                'options': [
                    'HTTP com segurança adicional',
                    'Uma versão mais rápida do HTTP',
                    'Um novo protocolo que substitui HTTP',
                    'Um servidor web especializado',
                    'Uma biblioteca Python'
                ],
                'correct_answer': 'HTTP com segurança adicional'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual plataforma é especializada em hospedar aplicações Python?',
                'options': [
                    'GitHub',
                    'AWS',
                    'PythonAnywhere',
                    'Google Drive',
                    'Dropbox'
                ],
                'correct_answer': 'PythonAnywhere'
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
                'options': ['Codificação', 'Planejamento', 'Testes', 'Deploy', 'Documentação'],
                'correct_answer': 'Planejamento'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que é um wireframe?',
                'options': [
                    'Código do projeto',
                    'Prototipo da interface',
                    'Documentação técnica',
                    'Teste automatizado',
                    'Banco de dados'
                ],
                'correct_answer': 'Prototipo da interface'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual tecnologia é usada para o frontend em projetos web?',
                'options': [
                    'Python',
                    'SQL',
                    'HTML/CSS/JavaScript',
                    'Flask',
                    'PostgreSQL'
                ],
                'correct_answer': 'HTML/CSS/JavaScript'
            },
            {
                'type': 'multiple_choice',
                'question': 'Por que é importante fazer testes em um projeto?',
                'options': [
                    'Para tornar o código mais lento',
                    'Para garantir qualidade e funcionamento',
                    'Para ocupar mais espaço',
                    'Para impressionar o cliente',
                    'Para complicar o desenvolvimento'
                ],
                'correct_answer': 'Para garantir qualidade e funcionamento'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual é o objetivo final de um projeto de software?',
                'options': [
                    'Escrever o máximo de código possível',
                    'Resolver um problema real para usuários',
                    'Usar todas as tecnologias disponíveis',
                    'Criar um código complexo',
                    'Gastar o máximo de tempo possível'
                ],
                'correct_answer': 'Resolver um problema real para usuários'
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