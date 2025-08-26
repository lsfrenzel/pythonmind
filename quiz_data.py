# Dados dos módulos do sistema
MODULES = {
    1: {
        'title': 'Fundamentos do Python',
        'description': 'Conceitos básicos da linguagem Python.',
        'video_url': '',
        'content': '''<div class="module-header">
            <h3>🚀 Módulo 1 - Fundamentos do Python</h3>
            <p class="module-intro"><strong>Bem-vindo ao mundo da programação Python!</strong> Neste módulo, você descobrirá os conceitos fundamentais que formam a base de toda programação em Python.</p>
        </div>
        
        <div class="content-section">
            <h4>💾 1. Variáveis e Tipos de Dados</h4>
            <p>Python é uma linguagem dinamicamente tipada, o que significa que você não precisa declarar o tipo de uma variável explicitamente. O Python determina automaticamente o tipo baseado no valor atribuído.</p>
            
            <div class="code-example">
                <h5>🔢 Tipos Numéricos:</h5>
                <pre><code># Inteiros (int)
idade = 25
quantidade = 100
ano = 2024

# Números decimais (float)
altura = 1.75
preco = 29.99
temperatura = -10.5

# Números complexos (complex)
numero_complexo = 3 + 4j
print(f"Parte real: {numero_complexo.real}")
print(f"Parte imaginária: {numero_complexo.imag}")

# Verificando tipos
print(type(idade))        # &lt;class 'int'&gt;
print(type(altura))       # &lt;class 'float'&gt;
print(type(numero_complexo))  # &lt;class 'complex'&gt;</code></pre>
            </div>
            
            <div class="code-example">
                <h5>📝 Strings (Texto):</h5>
                <pre><code># Diferentes formas de criar strings
nome = "João Silva"
cidade = 'São Paulo'
descricao = """Este é um texto
que ocupa múltiplas
linhas"""

# Operações com strings
nome_completo = nome + " da " + cidade
print(f"Nome completo: {nome_completo}")

# Métodos úteis de strings
print(nome.upper())          # JOÃO SILVA
print(nome.lower())          # joão silva
print(nome.title())          # João Silva
print(len(nome))             # 10 (quantidade de caracteres)

# Fatiamento de strings
print(nome[0])               # J (primeiro caractere)
print(nome[-1])              # a (último caractere)
print(nome[0:4])             # João (do índice 0 ao 3)
print(nome[:4])              # João (do início ao índice 3)
print(nome[5:])              # Silva (do índice 5 ao final)</code></pre>
            </div>
            
            <div class="code-example">
                <h5>✅ Booleanos:</h5>
                <pre><code># Valores booleanos
ativo = True
possui_desconto = False
maior_idade = idade >= 18

print(f"Usuário ativo: {ativo}")
print(f"Possui desconto: {possui_desconto}")
print(f"É maior de idade: {maior_idade}")

# Operações lógicas
tem_carteira = True
tem_veiculo = False

pode_dirigir = tem_carteira and tem_veiculo
print(f"Pode dirigir: {pode_dirigir}")  # False

tem_documento = tem_carteira or tem_veiculo
print(f"Tem documento: {tem_documento}")  # True</code></pre>
            </div>
        </div>
        
        <div class="content-section">
            <h4>🗂️ 2. Estruturas de Dados</h4>
            
            <div class="code-example">
                <h5>📋 Listas - Coleções Ordenadas e Mutáveis:</h5>
                <pre><code># Criando listas
frutas = ["maçã", "banana", "laranja", "uva"]
numeros = [1, 2, 3, 4, 5]
mista = ["Python", 3.8, True, ["sublista", "aqui"]]

# Acessando elementos
print(f"Primeira fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")

# Modificando listas
frutas.append("pêra")           # Adiciona no final
frutas.insert(1, "manga")       # Adiciona na posição 1
frutas.remove("banana")         # Remove elemento específico
fruta_removida = frutas.pop()   # Remove e retorna o último

print(f"Lista atual: {frutas}")
print(f"Fruta removida: {fruta_removida}")

# Operações úteis
print(f"Quantidade de frutas: {len(frutas)}")
print(f"A maçã está na lista: {'maçã' in frutas}")

# Fatiamento de listas
print(f"Primeiras 3 frutas: {frutas[:3]}")
print(f"Últimas 2 frutas: {frutas[-2:]}")</code></pre>
            </div>
            
            <div class="code-example">
                <h5>🔑 Dicionários - Coleções de Chave-Valor:</h5>
                <pre><code># Criando dicionários
pessoa = {
    "nome": "Maria Santos",
    "idade": 30,
    "cidade": "Rio de Janeiro",
    "profissao": "Engenheira",
    "hobbies": ["leitura", "natação", "fotografia"]
}

# Acessando valores
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa.get('idade', 'Não informado')}")

# Modificando dicionários
pessoa["telefone"] = "(21) 99999-9999"  # Adiciona nova chave
pessoa["idade"] = 31                     # Atualiza valor existente

# Métodos úteis
print(f"Chaves: {list(pessoa.keys())}")
print(f"Valores: {list(pessoa.values())}")

# Iterando sobre dicionário
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Dicionário de produtos (exemplo prático)
estoque = {
    "notebook": {"preco": 2500.00, "quantidade": 5},
    "mouse": {"preco": 50.00, "quantidade": 20},
    "teclado": {"preco": 150.00, "quantidade": 8}
}

print(f"Preço do notebook: R$ {estoque['notebook']['preco']:.2f}")</code></pre>
            </div>
        </div>''',
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
        'content': '''<div class="module-header">
            <h3>🎯 Módulo 2 - Estruturas de Controle</h3>
            <p class="module-intro"><strong>Domine o fluxo do seu código!</strong> Aprenda a controlar a execução do programa com condicionais, loops e estruturas de decisão avançadas.</p>
        </div>
        
        <div class="content-section">
            <h4>❓ 1. Estruturas Condicionais (if, elif, else)</h4>
            <p>As estruturas condicionais permitem que seu programa tome decisões baseadas em diferentes condições, tornando-o inteligente e responsivo.</p>
            
            <div class="code-example">
                <h5>🚦 Condicionais Básicas:</h5>
                <pre><code># Estrutura if simples
idade = 18

if idade >= 18:
    print("Você é maior de idade!")
    print("Pode tirar carteira de motorista")

# Estrutura if-else
nota = 7.5

if nota >= 7.0:
    print("Aprovado! 🎉")
else:
    print("Reprovado 😔")

# Estrutura if-elif-else (múltiplas condições)
temperatura = 25

if temperatura < 0:
    print("❄️ Congelando!")
elif temperatura < 15:
    print("🧥 Frio")
elif temperatura < 25:
    print("😊 Agradável")
elif temperatura < 35:
    print("☀️ Quente")
else:
    print("🔥 Muito quente!")</code></pre>
            </div>
            
            <div class="code-example">
                <h5>🔗 Operadores Lógicos:</h5>
                <pre><code># Operador AND (e)
usuario = "admin"
senha = "123456"

if usuario == "admin" and senha == "123456":
    print("✅ Login realizado com sucesso!")
else:
    print("❌ Usuário ou senha incorretos")

# Operador OR (ou)
dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("🎉 É fim de semana!")
else:
    print("💼 Dia de trabalho")

# Operador NOT (não)
chovendo = False

if not chovendo:
    print("☀️ Vamos para o parque!")
else:
    print("🌧️ Melhor ficar em casa")

# Combinando operadores
idade = 20
tem_carteira = True
tem_carro = False

pode_dirigir = idade >= 18 and tem_carteira and tem_carro
print(f"Pode dirigir: {pode_dirigir}")</code></pre>
            </div>
        </div>
        
        <div class="content-section">
            <h4>🔄 2. Loops (for e while)</h4>
            
            <div class="code-example">
                <h5>🔁 Loop FOR - Iteração Definida:</h5>
                <pre><code># Loop com range
print("Contando até 5:")
for i in range(1, 6):
    print(f"Número: {i}")

# Loop com lista
frutas = ["maçã", "banana", "laranja", "uva"]
print("\n🍎 Frutas disponíveis:")
for fruta in frutas:
    print(f"- {fruta}")

# Loop com índice e valor (enumerate)
print("\n📋 Lista numerada:")
for indice, fruta in enumerate(frutas, 1):
    print(f"{indice}. {fruta}")

# Loop com dicionário
pessoa = {"nome": "João", "idade": 25, "cidade": "SP"}
print("\n👤 Informações da pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")

# Exemplo prático: Tabuada
numero = 7
print(f"\n📊 Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2d} = {resultado:2d}")</code></pre>
            </div>
            
            <div class="code-example">
                <h5>🔄 Loop WHILE - Iteração Condicional:</h5>
                <pre><code># While básico
contador = 1
print("Contagem regressiva:")
while contador <= 5:
    print(f"⏰ {contador}")
    contador += 1
print("🚀 Decolagem!")

# Exemplo prático: Menu interativo
opcao = ""
print("\n📱 Sistema de Menu")
while opcao != "3":
    print("\n1. Ver dados")
    print("2. Cadastrar")
    print("3. Sair")
    
    # Simulando entrada (em aplicação real usaria input())
    if opcao == "": opcao = "1"
    elif opcao == "1": opcao = "2"
    elif opcao == "2": opcao = "3"
    
    if opcao == "1":
        print("📊 Mostrando dados...")
    elif opcao == "2":
        print("📝 Cadastrando novo item...")
    elif opcao == "3":
        print("👋 Saindo do sistema...")

# While com condição complexa
tentativas = 0
senha_correta = "python123"
senha_digitada = "senha_errada"  # Simulação

while senha_digitada != senha_correta and tentativas < 3:
    tentativas += 1
    print(f"❌ Tentativa {tentativas}: Senha incorreta")
    # Em aplicação real: senha_digitada = input("Digite a senha: ")
    if tentativas == 3:
        break
    senha_digitada = "python123" if tentativas == 2 else "ainda_errada"

if senha_digitada == senha_correta:
    print("✅ Acesso liberado!")
else:
    print("🔒 Acesso bloqueado - muitas tentativas")</code></pre>
            </div>
        </div>
        
        <div class="content-section">
            <h4>⚡ 3. Controle de Fluxo Avançado</h4>
            
            <div class="code-example">
                <h5>🛑 Break e Continue:</h5>
                <pre><code># BREAK - Interrompe o loop
print("🔍 Procurando número 7:")
numeros = [1, 3, 5, 7, 9, 11, 13]
for numero in numeros:
    if numero == 7:
        print(f"✅ Encontrei o {numero}!")
        break
    print(f"Verificando: {numero}")

print("\n⏭️ Usando CONTINUE:")
# CONTINUE - Pula para próxima iteração
for numero in range(1, 11):
    if numero % 2 == 0:  # Se é par, pula
        continue
    print(f"Número ímpar: {numero}")

# Exemplo prático: Validação de dados
dados = ["João", "", "Maria", "123", "Pedro", "Ana"]
usuarios_validos = []

print("\n✅ Validando usuários:")
for usuario in dados:
    if usuario == "": # Pula nomes vazios
        print("⚠️ Nome vazio - ignorando")
        continue
    if usuario.isdigit(): # Pula se for só números
        print(f"⚠️ '{usuario}' não é um nome válido - ignorando")
        continue
    usuarios_validos.append(usuario)
    print(f"✅ '{usuario}' adicionado")

print(f"\n👥 Usuários válidos: {usuarios_validos}")</code></pre>
            </div>
            
            <div class="code-example">
                <h5>🎲 Exemplo Prático - Sistema de Notas:</h5>
                <pre><code># Sistema completo de análise de notas
notas_turma = [8.5, 6.0, 9.2, 5.8, 7.5, 8.0, 6.5, 9.0, 7.8, 5.5]

print("📚 SISTEMA DE ANÁLISE DE NOTAS")
print("="*40)

# Estatísticas básicas
soma_notas = 0
aprovados = 0
reprovados = 0
maior_nota = 0
menor_nota = 10

for nota in notas_turma:
    soma_notas += nota
    
    # Atualiza maior e menor nota
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota
    
    # Conta aprovados/reprovados
    if nota >= 7.0:
        aprovados += 1
        status = "✅ APROVADO"
    else:
        reprovados += 1
        status = "❌ REPROVADO"
    
    print(f"Nota: {nota:4.1f} - {status}")

# Cálculos finais
media_turma = soma_notas / len(notas_turma)
taxa_aprovacao = (aprovados / len(notas_turma)) * 100

print("\n📊 RELATÓRIO FINAL:")
print(f"📈 Média da turma: {media_turma:.2f}")
print(f"🏆 Maior nota: {maior_nota:.1f}")
print(f"📉 Menor nota: {menor_nota:.1f}")
print(f"✅ Aprovados: {aprovados} alunos ({taxa_aprovacao:.1f}%)")
print(f"❌ Reprovados: {reprovados} alunos ({100-taxa_aprovacao:.1f}%)")

# Análise de desempenho
if media_turma >= 8.0:
    print("🎉 Turma com EXCELENTE desempenho!")
elif media_turma >= 7.0:
    print("👍 Turma com BOM desempenho!")
elif media_turma >= 6.0:
    print("⚠️ Turma com desempenho REGULAR")
else:
    print("🚨 Turma precisa de REFORÇO!")</code></pre>
            </div>
        </div>''',
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