# Quiz data for the Learning Management System

MODULES = {
    1: {
        'title': 'Introdução ao Python',
        'description': 'Fundamentos da linguagem Python, variáveis, tipos de dados e funções básicas',
        'content': '''<div class="module-header">
            <h3>🚀 Módulo 1 - Introdução ao Python</h3>
            <p class="module-intro"><strong>Bem-vindo ao mundo Python!</strong> Uma linguagem poderosa, elegante e versátil que conquista desenvolvedores ao redor do mundo. Prepare-se para uma jornada incrível no universo da programação!</p>
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai aprender:</h4>
            <ul class="learning-objectives">
                <li>História detalhada e filosofia do Python</li>
                <li>Configuração completa do ambiente de desenvolvimento</li>
                <li>Variáveis, tipos de dados e conversões</li>
                <li>Operadores matemáticos, lógicos e de comparação</li>
                <li>Entrada, saída e formatação de dados</li>
                <li>Comentários e documentação de código</li>
                <li>Primeiro programa completo</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico Detalhado:</h4>
            
            <h5>1. História e Filosofia do Python</h5>
            <p>Python foi criado por <strong>Guido van Rossum</strong> em 1989 na Holanda. Mais que uma linguagem, Python é uma filosofia de programação que prioriza:</p>
            
            <div class="alert alert-info">
                <strong>O Zen do Python (PEP 20):</strong>
                <ul class="mb-0">
                    <li><em>"Bonito é melhor que feio"</em></li>
                    <li><em>"Explícito é melhor que implícito"</em></li>
                    <li><em>"Simples é melhor que complexo"</em></li>
                    <li><em>"Legibilidade conta"</em></li>
                    <li><em>"Se a implementação é difícil de explicar, é uma má ideia"</em></li>
                </ul>
            </div>
            
            <h5>2. Por que Python é Especial?</h5>
            <div class="row">
                <div class="col-md-6">
                    <h6>✅ Vantagens:</h6>
                    <ul>
                        <li><strong>Sintaxe Clean:</strong> Parece inglês!</li>
                        <li><strong>Multipropósito:</strong> Web, IA, automação, ciência</li>
                        <li><strong>Grande Comunidade:</strong> Milhões de desenvolvedores</li>
                        <li><strong>Bibliotecas Ricas:</strong> 400.000+ no PyPI</li>
                        <li><strong>Cross-platform:</strong> Roda em qualquer sistema</li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <h6>⚠️ Considerações:</h6>
                    <ul>
                        <li>Mais lento que C/C++ (mas otimizável)</li>
                        <li>Não ideal para apps móveis nativos</li>
                        <li>Consome mais memória</li>
                    </ul>
                </div>
            </div>
            
            <h5>3. Tipos de Dados Fundamentais</h5>
            
            <h6>📊 Números em Python:</h6>
            <div class="code-example">
                <pre><code># Inteiros (int) - números sem casas decimais
idade = 25
ano_nascimento = 1998
pontos = -50  # Pode ser negativo
numero_grande = 1_000_000  # Use _ para facilitar leitura

# Decimais (float) - números com casas decimais
altura = 1.75
temperatura = -10.5
pi = 3.14159
notacao_cientifica = 2.5e6  # 2.500.000

# Números complexos (complex) - usados em matemática avançada
numero_complexo = 3 + 4j
print(f"Parte real: {numero_complexo.real}")
print(f"Parte imaginária: {numero_complexo.imag}")

# Operações matemáticas
resultado = 10 + 5   # Adição = 15
resultado = 10 - 3   # Subtração = 7
resultado = 4 * 5    # Multiplicação = 20
resultado = 15 / 3   # Divisão = 5.0 (sempre retorna float)
resultado = 15 // 3  # Divisão inteira = 5
resultado = 10 % 3   # Resto da divisão = 1
resultado = 2 ** 3   # Exponenciação = 8

# Verificando tipos
print(type(25))        # <class 'int'>
print(type(25.0))      # <class 'float'>
print(isinstance(25, int))  # True</code></pre>
            </div>
            
            <h6>📝 Strings (Texto) em Detalhes:</h6>
            <div class="code-example">
                <pre><code># Diferentes formas de criar strings
nome = "João Silva"           # Aspas duplas
cidade = 'São Paulo'          # Aspas simples
texto_multilinha = """Este é um texto
que pode ocupar várias
linhas sem problemas"""

# Escape characters (caracteres especiais)
texto_especial = "Ele disse: \"Olá!\" e foi embora"
caminho = "C:\\Users\\Nome\\Documentos"  # \\ para barra invertida
quebra_linha = "Primeira linha\nSegunda linha"
tab = "Nome\tIdade\tCidade"

# String methods (métodos úteis)
nome = "joão silva santos"
print(nome.upper())          # JOÃO SILVA SANTOS
print(nome.lower())          # joão silva santos
print(nome.title())          # João Silva Santos
print(nome.capitalize())     # João silva santos
print(nome.count('a'))       # 4 (conta ocorrências)
print(nome.find('silva'))    # 5 (posição da substring)
print(nome.replace('silva', 'pedro'))  # joão pedro santos

# Verificações booleanas de strings
print(nome.startswith('joão'))   # True
print(nome.endswith('santos'))   # True
print(nome.isalpha())           # False (tem espaços)
print("12345".isdigit())        # True
print("abc123".isalnum())       # True

# Formatação de strings (f-strings - método moderno)
nome = "Maria"
idade = 30
altura = 1.65
print(f"Olá, eu sou {nome}, tenho {idade} anos e {altura:.1f}m de altura")

# Formatação com format() (método clássico)
template = "Nome: {}, Idade: {}, Profissão: {}"
print(template.format("Pedro", 28, "Programador"))

# Fatiamento de strings (slicing)
palavra = "Python"
print(palavra[0])      # P (primeiro caractere)
print(palavra[-1])     # n (último caractere)
print(palavra[0:3])    # Pyt (do 0 ao 2)
print(palavra[2:])     # thon (do 2 ao final)
print(palavra[:4])     # Pyth (do início ao 3)
print(palavra[::2])    # Pto (pula de 2 em 2)
print(palavra[::-1])   # nohtyP (inverte a string)</code></pre>
            </div>
            
            <h6>🔄 Booleanos e Lógica:</h6>
            <div class="code-example">
                <pre><code># Valores booleanos
verdadeiro = True
falso = False

# Operadores de comparação
print(5 > 3)    # True
print(5 < 3)    # False
print(5 == 5)   # True (igual)
print(5 != 3)   # True (diferente)
print(5 >= 5)   # True (maior ou igual)
print(3 <= 5)   # True (menor ou igual)

# Operadores lógicos
print(True and True)   # True
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Valores que são considerados False em Python
print(bool(0))         # False
print(bool(""))        # False (string vazia)
print(bool([]))        # False (lista vazia)
print(bool(None))      # False

# Valores que são considerados True
print(bool(1))         # True
print(bool("texto"))   # True
print(bool([1, 2]))    # True</code></pre>
            </div>
            
            <h5>4. Variáveis e Convenções</h5>
            <div class="code-example">
                <pre><code># Convenções de nomenclatura (PEP 8)
# ✅ CORRETO:
nome_usuario = "João"        # snake_case para variáveis
CONSTANTE_MAXIMA = 100       # UPPER_CASE para constantes
idade_minima = 18

# ❌ EVITE:
nomeUsuario = "João"         # camelCase (reservado para classes)
nome-usuario = "João"        # hífen não é permitido
2nome = "João"               # não pode começar com número

# Múltiplas atribuições
x, y, z = 1, 2, 3
a = b = c = 0

# Troca de variáveis (pythônico!)
a, b = b, a

# Atribuição com operadores
contador = 0
contador += 1    # equivale a: contador = contador + 1
contador -= 1    # equivale a: contador = contador - 1
contador *= 2    # equivale a: contador = contador * 2</code></pre>
            </div>
            
            <h5>5. Entrada e Saída de Dados</h5>
            <div class="code-example">
                <pre><code># Função input() sempre retorna string
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# Convertendo entrada para números
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))
salario = float(input("Digite seu salário: "))

# Validação básica de entrada
try:
    numero = int(input("Digite um número: "))
    print(f"Você digitou: {numero}")
except ValueError:
    print("Erro: Isso não é um número válido!")

# Formatação avançada de saída
preco = 29.99
print(f"Preço: R$ {preco:.2f}")           # R$ 29.99
print(f"Preço: R$ {preco:>10.2f}")        # R$     29.99 (alinhado à direita)
print(f"Produto: {'Notebook':<15} R$ {preco:>8.2f}")  # Notebook          R$    29.99

# Saída com separadores personalizados
print("A", "B", "C", sep=" - ")           # A - B - C
print("Primeira linha", end=" ")          # Não quebra linha
print("mesma linha")                      # Primeira linha mesma linha</code></pre>
            </div>
            
            <h5>6. Comentários e Documentação</h5>
            <div class="code-example">
                <pre><code># Comentário de linha simples
nome = "João"  # Comentário no final da linha

"""
Comentário de múltiplas linhas
Usado para documentação extensa
ou para desabilitar blocos de código
"""

# Docstrings - documentação de funções (veremos mais adiante)
def saudacao(nome):
    """
    Exibe uma saudação personalizada.
    
    Args:
        nome (str): O nome da pessoa a ser cumprimentada
        
    Returns:
        None
    """
    print(f"Olá, {nome}!")

# Comentários informativos
valor_em_reais = 100
taxa_dolar = 5.20  # Taxa do dólar em 27/08/2025
valor_em_dolares = valor_em_reais / taxa_dolar</code></pre>
            </div>
            
            <h5>7. Primeiro Programa Completo</h5>
            <div class="code-example">
                <pre><code># Programa: Calculadora de IMC
print("=" * 40)
print("    CALCULADORA DE IMC")
print("=" * 40)

# Coletando dados do usuário
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Calculando o IMC
imc = peso / (altura ** 2)

# Determinando a classificação
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

# Exibindo resultado
print(f"\n{nome}, seu IMC é {imc:.1f}")
print(f"Classificação: {classificacao}")
print("=" * 40)</code></pre>
            </div>
            
            <div class="alert alert-success">
                <h6><i class="fas fa-lightbulb"></i> Dicas Profissionais:</h6>
                <ul class="mb-0">
                    <li><strong>Use f-strings</strong> para formatação (mais legível que .format())</li>
                    <li><strong>Siga o PEP 8</strong> para convenções de código Python</li>
                    <li><strong>Python é case-sensitive:</strong> 'nome' ≠ 'Nome'</li>
                    <li><strong>Use nomes descritivos:</strong> 'idade_usuario' > 'x'</li>
                    <li><strong>Teste sempre:</strong> Use print() para verificar valores</li>
                </ul>
            </div>
            
            <div class="alert alert-warning">
                <h6><i class="fas fa-exclamation-triangle"></i> Erros Comuns:</h6>
                <ul class="mb-0">
                    <li>Esquecer de converter input() para int/float</li>
                    <li>Usar = ao invés de == para comparação</li>
                    <li>Não considerar espaços em branco em strings</li>
                    <li>Dividir por zero sem verificação</li>
                </ul>
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
            <p class="module-intro"><strong>Dê inteligência aos seus programas!</strong> Aprenda a tomar decisões complexas e criar repetições eficientes. Este módulo transformará seus programas de simples para verdadeiramente inteligentes!</p>
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai dominar:</h4>
            <ul class="learning-objectives">
                <li>Estruturas condicionais avançadas (if, elif, else aninhados)</li>
                <li>Operadores de comparação, lógicos e de identidade</li>
                <li>Loops for e while com controle total</li>
                <li>Função range() em todos os cenários</li>
                <li>Controle de fluxo avançado (break, continue, else)</li>
                <li>Loops aninhados e otimização</li>
                <li>Condições complexas e operadores ternários</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico Completo:</h4>
            
            <h5>1. Estruturas Condicionais Detalhadas</h5>
            <p>As estruturas condicionais são o cérebro dos seus programas, permitindo tomar decisões baseadas em dados e situações específicas.</p>
            
            <div class="code-example">
                <h6>🔸 If Simples - Tomando uma decisão:</h6>
                <pre><code># Sintaxe básica
idade = 18
if idade >= 18:
    print("Você pode votar!")
    print("Você tem direitos plenos!")

# Múltiplas ações no if
salario = 5000
if salario > 3000:
    print("Salário acima da média")
    desconto_ir = salario * 0.275
    print(f"Desconto do IR: R$ {desconto_ir:.2f}")
    salario_liquido = salario - desconto_ir
    print(f"Salário líquido: R$ {salario_liquido:.2f}")</code></pre>
                
                <h6>🔸 If-Else - Duas possibilidades:</h6>
                <pre><code>nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("🎉 Parabéns! Você foi aprovado!")
    if nota >= 9:
        print("👑 Nota excelente! Você está entre os melhores!")
else:
    print("😔 Infelizmente você foi reprovado")
    print(f"Você precisava de {7 - nota:.1f} pontos a mais")
    print("Não desista! Estude mais e tente novamente!")</code></pre>
                
                <h6>🔸 If-Elif-Else - Múltiplas condições:</h6>
                <pre><code>nota = float(input("Digite sua nota (0-10): "))

if nota >= 9:
    conceito = "A"
    mensagem = "Excelente! Performance excepcional!"
elif nota >= 8:
    conceito = "B"
    mensagem = "Muito bom! Continue assim!"
elif nota >= 7:
    conceito = "C"
    mensagem = "Bom trabalho! Aprovado!"
elif nota >= 5:
    conceito = "D"
    mensagem = "Regular. Precisa melhorar"
else:
    conceito = "F"
    mensagem = "Insuficiente. Reprovado"

print(f"Conceito: {conceito} - {mensagem}")</code></pre>
            </div>
            
            <h5>2. Operadores de Comparação e Lógicos</h5>
            
            <div class="alert alert-info">
                <h6>🔍 Operadores de Comparação:</h6>
                <ul class="mb-0">
                    <li><code>==</code> - Igual a (atenção: não confundir com =)</li>
                    <li><code>!=</code> - Diferente de</li>
                    <li><code>&gt;</code> - Maior que</li>
                    <li><code>&lt;</code> - Menor que</li>
                    <li><code>&gt;=</code> - Maior ou igual</li>
                    <li><code>&lt;=</code> - Menor ou igual</li>
                    <li><code>in</code> - Pertence à sequência</li>
                    <li><code>not in</code> - Não pertence à sequência</li>
                    <li><code>is</code> - Identidade de objeto</li>
                    <li><code>is not</code> - Não é o mesmo objeto</li>
                </ul>
            </div>
            
            <div class="code-example">
                <h6>🔸 Operadores Lógicos - Combinando Condições:</h6>
                <pre><code># AND - Todas as condições devem ser verdadeiras
idade = 25
salario = 4000
tem_carteira = True

if idade >= 21 and salario >= 3000 and tem_carteira:
    print("Aprovado para financiamento do carro!")
else:
    print("Não atende aos critérios do financiamento")

# OR - Pelo menos uma condição deve ser verdadeira
dia_semana = "sábado"
feriado = False

if dia_semana in ["sábado", "domingo"] or feriado:
    print("Hoje não é dia de trabalho!")
else:
    print("Dia de trabalho!")

# NOT - Inverte o valor lógico
usuario_logado = False

if not usuario_logado:
    print("Por favor, faça login para continuar")
else:
    print("Bem-vindo ao sistema!")

# Combinações complexas
temperatura = 25
chuva = False
vento_forte = False

if temperatura > 20 and not chuva and not vento_forte:
    print("Dia perfeito para atividades ao ar livre!")
elif temperatura > 15 and not chuva:
    print("Dia bom para uma caminhada")
else:
    print("Melhor ficar em casa hoje")</code></pre>
            </div>
            
            <h5>3. Operadores de Pertencimento e Identidade</h5>
            <div class="code-example">
                <pre><code># Operador IN - verifica se elemento está em sequência
frutas = ["maçã", "banana", "laranja", "uva"]
fruta_escolhida = input("Digite uma fruta: ").lower()

if fruta_escolhida in frutas:
    print(f"Temos {fruta_escolhida} disponível!")
else:
    print(f"Desculpe, não temos {fruta_escolhida}")
    print(f"Frutas disponíveis: {', '.join(frutas)}")

# Verificando caracteres em string
email = input("Digite seu email: ")
if "@" in email and "." in email:
    print("Email parece válido")
else:
    print("Email inválido")

# Operador IS - verifica identidade de objeto
a = None
if a is None:
    print("Variável 'a' não foi definida")
    
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 == lista2)    # True (mesmo conteúdo)
print(lista1 is lista2)    # False (objetos diferentes)
print(lista1 is lista3)    # True (mesmo objeto)</code></pre>
            </div>
            
            <h5>4. Loops - Repetições Inteligentes</h5>
            
            <h6>🔄 Loop FOR - Quando sabemos quantas repetições:</h6>
            <div class="code-example">
                <pre><code># Range básico
print("Contando de 0 a 4:")
for i in range(5):
    print(f"Número: {i}")

# Range com início e fim
print("\nContando de 1 a 10:")
for numero in range(1, 11):
    print(f"Número: {numero}")

# Range com passo (step)
print("\nNúmeros pares de 0 a 20:")
for par in range(0, 21, 2):
    print(par, end=" ")

print("\n\nContagem regressiva:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("🚀 Decolagem!")

# Loop em strings
nome = "Python"
print("\nLetras da palavra Python:")
for letra in nome:
    print(f"Letra: {letra}")

# Loop em listas
frutas = ["maçã", "banana", "laranja"]
print("\nFrutas disponíveis:")
for fruta in frutas:
    print(f"- {fruta.title()}")

# Enumerate - obter índice e valor
print("\nFrutas com posição:")
for indice, fruta in enumerate(frutas, 1):
    print(f"{indice}. {fruta.title()}")

# Calculando a tabuada
numero = int(input("\nDigite um número para a tabuada: "))
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2d} = {resultado:2d}")</code></pre>
            </div>
            
            <h6>🔄 Loop WHILE - Quando a condição define o fim:</h6>
            <div class="code-example">
                <pre><code># While básico
contador = 0
print("Contando até 5:")
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1

# Loop até entrada válida
while True:
    idade = input("Digite sua idade (ou 'sair'): ")
    if idade.lower() == 'sair':
        break
    try:
        idade = int(idade)
        if idade < 0:
            print("Idade não pode ser negativa!")
        elif idade > 150:
            print("Idade muito alta!")
        else:
            print(f"Idade válida: {idade} anos")
            break
    except ValueError:
        print("Por favor, digite um número válido!")

# Acumulador - somando números
soma = 0
contador = 0
print("\nDigite números para somar (0 para parar):")

while True:
    try:
        numero = float(input("Número: "))
        if numero == 0:
            break
        soma += numero
        contador += 1
        print(f"Soma atual: {soma}")
    except ValueError:
        print("Digite um número válido!")

if contador > 0:
    media = soma / contador
    print(f"\nEstatísticas:")
    print(f"Total de números: {contador}")
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")</code></pre>
            </div>
            
            <h5>5. Controle de Fluxo Avançado</h5>
            
            <div class="code-example">
                <h6>🔸 BREAK - Saindo do loop:</h6>
                <pre><code># Procurando um número específico
numeros = [1, 5, 3, 8, 2, 7, 4]
procurado = 8

for i, numero in enumerate(numeros):
    print(f"Verificando posição {i}: {numero}")
    if numero == procurado:
        print(f"✅ Encontrei o número {procurado} na posição {i}!")
        break
else:
    print(f"❌ Número {procurado} não encontrado na lista")

# Sistema de login com tentativas limitadas
tentativas = 3
senha_correta = "python123"

while tentativas > 0:
    senha = input(f"Digite a senha ({tentativas} tentativas restantes): ")
    if senha == senha_correta:
        print("🎉 Login realizado com sucesso!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"❌ Senha incorreta! {tentativas} tentativas restantes")
        else:
            print("🚫 Muitas tentativas inválidas. Acesso bloqueado!")
            break</code></pre>
                
                <h6>🔸 CONTINUE - Pular para próxima iteração:</h6>
                <pre><code># Processando apenas números pares
print("Números pares de 1 a 20:")
for numero in range(1, 21):
    if numero % 2 != 0:  # Se é ímpar
        continue  # Pula para próxima iteração
    print(f"Par: {numero}")

# Validando dados de uma lista
nomes = ["João", "", "Maria", "123", "Pedro", "Ana"]
nomes_validos = []

for nome in nomes:
    if not nome:  # Nome vazio
        print("❌ Nome vazio ignorado")
        continue
    if nome.isdigit():  # Nome só com números
        print(f"❌ '{nome}' não é um nome válido")
        continue
    if len(nome) < 2:  # Nome muito curto
        print(f"❌ '{nome}' é muito curto")
        continue
    
    # Se chegou aqui, o nome é válido
    nomes_validos.append(nome.title())
    print(f"✅ '{nome.title()}' adicionado")

print(f"\nNomes válidos: {nomes_validos}")</code></pre>
                
                <h6>🔸 ELSE em Loops - Executado se não houver break:</h6>
                <pre><code># Verificando se uma lista contém apenas números positivos
numeros = [1, 5, 3, 8, 2, 7, 4]

for numero in numeros:
    if numero <= 0:
        print(f"❌ Encontrado número não positivo: {numero}")
        break
else:
    print("✅ Todos os números são positivos!")

# Procurando usuário em sistema
usuarios = ["admin", "joão", "maria", "pedro"]
usuario_procurado = input("Digite o nome do usuário: ").lower()

for usuario in usuarios:
    if usuario == usuario_procurado:
        print(f"✅ Usuário '{usuario}' encontrado!")
        break
else:
    print(f"❌ Usuário '{usuario_procurado}' não está cadastrado")</code></pre>
            </div>
            
            <h5>6. Loops Aninhados - Loops dentro de Loops</h5>
            <div class="code-example">
                <pre><code># Tabuada completa (1 a 10)
print("TABUADA COMPLETA")
print("=" * 40)

for numero in range(1, 11):
    print(f"\nTabuada do {numero}:")
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador:2d} = {resultado:2d}")

# Padrão de estrelas
print("\nPadrão de estrelas:")
for linha in range(1, 6):
    for estrela in range(linha):
        print("*", end="")
    print()  # Quebra de linha

# Sistema de coordenadas
print("\nMapa de coordenadas 5x5:")
for y in range(5):
    for x in range(5):
        print(f"({x},{y})", end=" ")
    print()  # Nova linha após cada linha</code></pre>
            </div>
            
            <h5>7. Operador Ternário - If em Uma Linha</h5>
            <div class="code-example">
                <pre><code># Sintaxe: valor_se_verdadeiro if condição else valor_se_falso

idade = 20
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)

# Comparando com if normal
if idade >= 18:
    status = "Maior de idade"
else:
    status = "Menor de idade"

# Exemplos práticos
nota = 8.5
resultado = "Aprovado" if nota >= 7 else "Reprovado"

numero = -5
absoluto = numero if numero >= 0 else -numero

salario = 3000
categoria = "Alto" if salario > 5000 else "Médio" if salario > 2000 else "Baixo"

# Em função
def classificar_temperatura(temp):
    return "Quente" if temp > 30 else "Agradável" if temp > 20 else "Frio"

print(classificar_temperatura(25))  # Agradável</code></pre>
            </div>
            
            <h5>8. Projeto Prático Completo</h5>
            <div class="code-example">
                <pre><code># JOGO DE ADIVINHAÇÃO AVANÇADO
import random

print("🎯 JOGO DE ADIVINHAÇÃO")
print("=" * 40)

# Configurações do jogo
numero_secreto = random.randint(1, 100)
tentativas_maximas = 7
tentativas = 0
acertou = False

print("Pensei em um número entre 1 e 100!")
print(f"Você tem {tentativas_maximas} tentativas para acertar.")
print("💡 Dicas: 'maior' ou 'menor' te ajudarão!")

while tentativas < tentativas_maximas and not acertou:
    try:
        # Entrada do usuário
        chute = int(input(f"\nTentativa {tentativas + 1}: "))
        tentativas += 1
        
        # Verificação
        if chute == numero_secreto:
            acertou = True
            print(f"🎉 PARABÉNS! Você acertou em {tentativas} tentativas!")
            
            # Classificação da performance
            if tentativas <= 3:
                print("👑 Performance EXCEPCIONAL!")
            elif tentativas <= 5:
                print("⭐ Performance ÓTIMA!")
            else:
                print("👍 Performance BOA!")
        
        elif chute < numero_secreto:
            print("📈 O número é MAIOR que", chute)
        else:
            print("📉 O número é MENOR que", chute)
        
        # Dicas baseadas na proximidade
        diferenca = abs(chute - numero_secreto)
        if diferenca <= 5 and not acertou:
            print("🔥 MUITO QUENTE! Você está bem próximo!")
        elif diferenca <= 15 and not acertou:
            print("🌡️ Quente! Está no caminho certo!")
        
        # Aviso de tentativas restantes
        if tentativas < tentativas_maximas and not acertou:
            restantes = tentativas_maximas - tentativas
            print(f"⏰ Restam {restantes} tentativas")
    
    except ValueError:
        print("❌ Por favor, digite apenas números!")

# Resultado final
if not acertou:
    print(f"\n💔 Game Over! O número era {numero_secreto}")
    print("🔄 Tente novamente!")

print("\n📊 ESTATÍSTICAS DO JOGO:")
print(f"Número secreto: {numero_secreto}")
print(f"Tentativas usadas: {tentativas}")
print(f"Taxa de acerto: {(1/tentativas)*100:.1f}%")
print("=" * 40)</code></pre>
            </div>
            
            <div class="alert alert-success">
                <h6><i class="fas fa-lightbulb"></i> Dicas Profissionais:</h6>
                <ul class="mb-0">
                    <li><strong>Use elif</strong> ao invés de múltiplos if quando as condições são mutuamente exclusivas</li>
                    <li><strong>Combine condições</strong> com and/or para lógica mais complexa</li>
                    <li><strong>For vs While:</strong> Use for quando souber o número de iterações, while quando depender de condição</li>
                    <li><strong>Evite loops infinitos:</strong> Sempre garanta que a condição do while eventualmente seja False</li>
                    <li><strong>Use break e continue</strong> para controlar o fluxo com precisão</li>
                    <li><strong>Operador ternário</strong> torna o código mais conciso para condições simples</li>
                </ul>
            </div>
            
            <div class="alert alert-warning">
                <h6><i class="fas fa-exclamation-triangle"></i> Armadilhas Comuns:</h6>
                <ul class="mb-0">
                    <li><strong>= vs ==:</strong> = é atribuição, == é comparação</li>
                    <li><strong>Indentação:</strong> Python usa indentação para definir blocos</li>
                    <li><strong>range(10):</strong> vai de 0 a 9, não até 10</li>
                    <li><strong>input() sempre retorna string:</strong> converta com int() ou float()</li>
                    <li><strong>Loop infinito:</strong> certifique-se de que a condição mude dentro do loop</li>
                </ul>
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
            <p class="module-intro"><strong>Domine a persistência de dados!</strong> Aprenda a ler, escrever e processar arquivos de forma profissional. Transforme seus programas em sistemas que lembram e processam informações!</p>
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai dominar:</h4>
            <ul class="learning-objectives">
                <li>Manipulação avançada de arquivos de texto</li>
                <li>Todos os modos de abertura e suas aplicações</li>
                <li>Gerenciamento seguro e tratamento de erros</li>
                <li>Processamento completo de CSV e planilhas</li>
                <li>Trabalhando com JSON e configurações</li>
                <li>Operações com diretórios e caminhos</li>
                <li>Encoding e arquivos internacionais</li>
                <li>Backup automático e versionamento</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico Avançado:</h4>
            
            <h5>1. Fundamentos de Arquivos</h5>
            <p>Arquivos são a ponte entre seus programas e o mundo real. Dominar sua manipulação é essencial para qualquer aplicação profissional.</p>
            
            <div class="alert alert-info">
                <h6>🔧 Modos de Abertura Completos:</h6>
                <ul class="mb-0">
                    <li><code>'r'</code> - Leitura (padrão, arquivo deve existir)</li>
                    <li><code>'w'</code> - Escrita (sobrescreve ou cria novo)</li>
                    <li><code>'a'</code> - Anexar (adiciona ao final)</li>
                    <li><code>'x'</code> - Criação exclusiva (falha se já existir)</li>
                    <li><code>'r+'</code> - Leitura e escrita</li>
                    <li><code>'w+'</code> - Escrita e leitura (trunca arquivo)</li>
                    <li><code>'a+'</code> - Anexar e leitura</li>
                    <li><code>'b'</code> - Modo binário (combina com outros)</li>
                    <li><code>'t'</code> - Modo texto (padrão)</li>
                </ul>
            </div>
            
            <h5>2. Leitura Avançada de Arquivos</h5>
            <div class="code-example">
                <pre><code># Diferentes formas de ler arquivos
import os

# Verificando se arquivo existe
if os.path.exists('dados.txt'):
    print("Arquivo encontrado!")
else:
    print("Arquivo não existe")

# Lendo arquivo completo
with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    conteudo_completo = arquivo.read()
    print("Conteúdo completo:")
    print(conteudo_completo)

# Lendo linha por linha (economiza memória)
with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    numero_linha = 1
    for linha in arquivo:
        print(f"Linha {numero_linha}: {linha.strip()}")
        numero_linha += 1

# Lendo todas as linhas em uma lista
with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    print(f"Total de linhas: {len(linhas)}")
    for i, linha in enumerate(linhas, 1):
        print(f"{i:2d}: {linha.strip()}")

# Lendo quantidade específica de caracteres
with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    primeiros_100_chars = arquivo.read(100)
    print(f"Primeiros 100 caracteres: {primeiros_100_chars}")

# Lendo com tratamento de erro robusto
def ler_arquivo_seguro(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"❌ Arquivo '{nome_arquivo}' não encontrado")
        return None
    except PermissionError:
        print(f"❌ Sem permissão para ler '{nome_arquivo}'")
        return None
    except UnicodeDecodeError:
        print(f"❌ Erro de codificação em '{nome_arquivo}'")
        try:
            # Tenta com encoding diferente
            with open(nome_arquivo, 'r', encoding='latin-1') as arquivo:
                return arquivo.read()
        except:
            return None

conteudo = ler_arquivo_seguro('exemplo.txt')</code></pre>
            </div>
            
            <h5>3. Escrita Profissional de Arquivos</h5>
            <div class="code-example">
                <pre><code># Escrevendo dados estruturados
import datetime

def criar_log(mensagem, nivel="INFO"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {nivel}: {mensagem}\n"
    
    with open('sistema.log', 'a', encoding='utf-8') as arquivo:
        arquivo.write(log_entry)

# Salvando dados de usuários
usuarios = [
    {"nome": "João", "idade": 30, "email": "joao@email.com"},
    {"nome": "Maria", "idade": 25, "email": "maria@email.com"},
    {"nome": "Pedro", "idade": 35, "email": "pedro@email.com"}
]

# Salvando como texto formatado
with open('usuarios.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("RELATÓRIO DE USUÁRIOS\n")
    arquivo.write("=" * 50 + "\n")
    arquivo.write(f"Gerado em: {datetime.datetime.now()}\n\n")
    
    for i, usuario in enumerate(usuarios, 1):
        arquivo.write(f"{i}. Nome: {usuario['nome']}\n")
        arquivo.write(f"   Idade: {usuario['idade']} anos\n")
        arquivo.write(f"   Email: {usuario['email']}\n")
        arquivo.write("-" * 30 + "\n")

# Backup automático
def criar_backup(arquivo_original):
    import shutil
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_backup = f"{arquivo_original}.backup_{timestamp}"
    try:
        shutil.copy2(arquivo_original, nome_backup)
        print(f"✅ Backup criado: {nome_backup}")
        return nome_backup
    except Exception as e:
        print(f"❌ Erro ao criar backup: {e}")
        return None

# Escrevendo com backup automático
def escrever_com_backup(nome_arquivo, conteudo):
    # Cria backup se arquivo já existe
    if os.path.exists(nome_arquivo):
        criar_backup(nome_arquivo)
    
    # Escreve novo conteudo
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
    print(f"✅ Arquivo '{nome_arquivo}' atualizado")</code></pre>
            </div>
            
            <h5>4. Trabalhando com CSV - Dados Tabulares</h5>
            <div class="code-example">
                <pre><code>import csv

# Lendo arquivo CSV
def ler_vendas_csv(nome_arquivo):
    vendas = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                # Convertendo tipos apropriados
                venda = {
                    'produto': linha['produto'],
                    'quantidade': int(linha['quantidade']),
                    'preco': float(linha['preco']),
                    'data': linha['data']
                }
                vendas.append(venda)
    except FileNotFoundError:
        print("❌ Arquivo de vendas não encontrado")
    except ValueError as e:
        print(f"❌ Erro de conversão: {e}")
    
    return vendas

# Criando arquivo CSV com dados
def salvar_vendas_csv(vendas, nome_arquivo):
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
        campos = ['produto', 'quantidade', 'preco', 'data', 'total']
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        
        # Escreve cabeçalho
        escritor.writeheader()
        
        # Escreve dados com cálculo automático
        for venda in vendas:
            venda['total'] = venda['quantidade'] * venda['preco']
            escritor.writerow(venda)

# Exemplo de uso
vendas_exemplo = [
    {'produto': 'Notebook', 'quantidade': 2, 'preco': 2500.00, 'data': '2025-01-15'},
    {'produto': 'Mouse', 'quantidade': 5, 'preco': 45.00, 'data': '2025-01-15'},
    {'produto': 'Teclado', 'quantidade': 3, 'preco': 120.00, 'data': '2025-01-16'}
]

salvar_vendas_csv(vendas_exemplo, 'vendas.csv')

# Analisando dados CSV
def analisar_vendas(nome_arquivo):
    vendas = ler_vendas_csv(nome_arquivo)
    
    if not vendas:
        return
    
    # Estatísticas
    total_vendas = sum(v['quantidade'] * v['preco'] for v in vendas)
    total_produtos = sum(v['quantidade'] for v in vendas)
    ticket_medio = total_vendas / len(vendas)
    
    print(f"📊 ANÁLISE DE VENDAS")
    print(f"Total de transações: {len(vendas)}")
    print(f"Total em vendas: R$ {total_vendas:,.2f}")
    print(f"Total de produtos: {total_produtos}")
    print(f"Ticket médio: R$ {ticket_medio:.2f}")
    
    # Produto mais vendido
    produtos = {}
    for venda in vendas:
        produto = venda['produto']
        quantidade = venda['quantidade']
        produtos[produto] = produtos.get(produto, 0) + quantidade
    
    mais_vendido = max(produtos.items(), key=lambda x: x[1])
    print(f"Produto mais vendido: {mais_vendido[0]} ({mais_vendido[1]} unidades)")

analisar_vendas('vendas.csv')</code></pre>
            </div>
            
            <h5>5. JSON - Formato Moderno de Dados</h5>
            <div class="code-example">
                <pre><code>import json
from datetime import datetime

# Estrutura de dados complexa
sistema_config = {
    "aplicacao": {
        "nome": "Sistema de Vendas",
        "versao": "2.1.0",
        "desenvolvedor": "Python Dev Team"
    },
    "database": {
        "host": "localhost",
        "porta": 5432,
        "nome": "vendas_db",
        "ssl": True
    },
    "usuarios": [
        {"id": 1, "nome": "Admin", "perfil": "administrador", "ativo": True},
        {"id": 2, "nome": "João", "perfil": "vendedor", "ativo": True},
        {"id": 3, "nome": "Maria", "perfil": "gerente", "ativo": False}
    ],
    "configuracoes": {
        "tema": "escuro",
        "idioma": "pt-BR",
        "timezone": "America/Sao_Paulo",
        "backup_automatico": True,
        "ultima_atualizacao": datetime.now().isoformat()
    }
}

# Salvando JSON formatado
def salvar_config(config, nome_arquivo):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(config, arquivo, indent=4, ensure_ascii=False)
        print(f"✅ Configuração salva em '{nome_arquivo}'")
    except Exception as e:
        print(f"❌ Erro ao salvar: {e}")

salvar_config(sistema_config, 'config.json')

# Carregando e modificando JSON
def carregar_config(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("❌ Arquivo de configuração não encontrado")
        return {}
    except json.JSONDecodeError as e:
        print(f"❌ JSON inválido: {e}")
        return {}

# Sistema de configuração dinâmica
class ConfigManager:
    def __init__(self, arquivo_config):
        self.arquivo = arquivo_config
        self.config = carregar_config(arquivo_config)
    
    def get(self, chave, padrao=None):
        """Obtém valor de configuração usando notação de ponto"""
        keys = chave.split('.')
        valor = self.config
        
        for key in keys:
            if isinstance(valor, dict) and key in valor:
                valor = valor[key]
            else:
                return padrao
        return valor
    
    def set(self, chave, valor):
        """Define valor de configuração"""
        keys = chave.split('.')
        config_atual = self.config
        
        for key in keys[:-1]:
            if key not in config_atual:
                config_atual[key] = {}
            config_atual = config_atual[key]
        
        config_atual[keys[-1]] = valor
        self.salvar()
    
    def salvar(self):
        """Salva configurações no arquivo"""
        salvar_config(self.config, self.arquivo)

# Usando o gerenciador
config = ConfigManager('config.json')
print(f"Nome da aplicação: {config.get('aplicacao.nome')}")
print(f"Porta do banco: {config.get('database.porta')}")

# Modificando configuração
config.set('configuracoes.tema', 'claro')
config.set('aplicacao.versao', '2.1.1')</code></pre>
            </div>
            
            <h5>6. Operações com Diretórios</h5>
            <div class="code-example">
                <pre><code>import os
import glob
from pathlib import Path

# Trabalhando com caminhos
def organizar_arquivos():
    # Criando estrutura de diretórios
    diretorios = ['documentos', 'imagens', 'videos', 'arquivos']
    
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            print(f"📁 Diretório '{diretorio}' criado")
    
    # Listando arquivos por extensão
    arquivos_txt = glob.glob("*.txt")
    arquivos_csv = glob.glob("*.csv")
    arquivos_json = glob.glob("*.json")
    
    print(f"Arquivos .txt encontrados: {len(arquivos_txt)}")
    print(f"Arquivos .csv encontrados: {len(arquivos_csv)}")
    print(f"Arquivos .json encontrados: {len(arquivos_json)}")
    
    # Movendo arquivos (simulação)
    import shutil
    for arquivo in arquivos_txt:
        destino = os.path.join('documentos', arquivo)
        print(f"Moveria {arquivo} para {destino}")
        # shutil.move(arquivo, destino)  # Descomente para mover de verdade

# Informações detalhadas de arquivos
def info_arquivo(nome_arquivo):
    if os.path.exists(nome_arquivo):
        stat = os.stat(nome_arquivo)
        tamanho = stat.st_size
        
        # Convertendo tamanho para formato legível
        if tamanho < 1024:
            tamanho_str = f"{tamanho} bytes"
        elif tamanho < 1024**2:
            tamanho_str = f"{tamanho/1024:.1f} KB"
        elif tamanho < 1024**3:
            tamanho_str = f"{tamanho/(1024**2):.1f} MB"
        else:
            tamanho_str = f"{tamanho/(1024**3):.1f} GB"
        
        modificado = datetime.fromtimestamp(stat.st_mtime)
        
        print(f"📋 Informações do arquivo '{nome_arquivo}':")
        print(f"   Tamanho: {tamanho_str}")
        print(f"   Modificado: {modificado.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"   Legível: {'Sim' if os.access(nome_arquivo, os.R_OK) else 'Não'}")
        print(f"   Escrevível: {'Sim' if os.access(nome_arquivo, os.W_OK) else 'Não'}")

organizar_arquivos()
info_arquivo('config.json')</code></pre>
            </div>
            
            <h5>7. Sistema Completo de Logs</h5>
            <div class="code-example">
                <pre><code>import logging
from datetime import datetime
import os

class SistemaLog:
    def __init__(self, nome_arquivo="sistema.log", nivel=logging.INFO):
        # Cria diretório de logs se não existir
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        # Configura o sistema de log
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(nivel)
        
        # Formato das mensagens
        formato = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Handler para arquivo
        arquivo_handler = logging.FileHandler(
            f'logs/{nome_arquivo}', 
            encoding='utf-8'
        )
        arquivo_handler.setFormatter(formato)
        self.logger.addHandler(arquivo_handler)
        
        # Handler para console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formato)
        self.logger.addHandler(console_handler)
    
    def info(self, mensagem):
        self.logger.info(mensagem)
    
    def erro(self, mensagem):
        self.logger.error(mensagem)
    
    def aviso(self, mensagem):
        self.logger.warning(mensagem)
    
    def debug(self, mensagem):
        self.logger.debug(mensagem)

# Usando o sistema de log
log = SistemaLog("aplicacao.log")

log.info("Sistema iniciado")
log.aviso("Configuração de rede não encontrada")
log.erro("Falha ao conectar com banco de dados")
log.info("Sistema finalizado")</code></pre>
            </div>
            
            <div class="alert alert-success">
                <h6><i class="fas fa-lightbulb"></i> Boas Práticas Profissionais:</h6>
                <ul class="mb-0">
                    <li><strong>Sempre use 'with open()'</strong> para garantir fechamento automático</li>
                    <li><strong>Especifique encoding='utf-8'</strong> para caracteres especiais</li>
                    <li><strong>Trate erros específicos</strong> (FileNotFoundError, PermissionError)</li>
                    <li><strong>Faça backup</strong> antes de modificar arquivos importantes</li>
                    <li><strong>Use pathlib</strong> para operações modernas com caminhos</li>
                    <li><strong>Implemente logs</strong> para rastrear operações importantes</li>
                </ul>
            </div>
            
            <div class="alert alert-warning">
                <h6><i class="fas fa-exclamation-triangle"></i> Cuidados Importantes:</h6>
                <ul class="mb-0">
                    <li><strong>Modo 'w' apaga</strong> todo o conteúdo do arquivo</li>
                    <li><strong>Verifique permissões</strong> antes de tentar acessar arquivos</li>
                    <li><strong>Cuidado com encoding</strong> ao trabalhar com caracteres especiais</li>
                    <li><strong>Grandes arquivos</strong> podem consumir muita memória com read()</li>
                    <li><strong>Sempre valide dados</strong> ao ler de arquivos externos</li>
                </ul>
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
            <p class="module-intro"><strong>Transforme-se em um arquiteto de código!</strong> Domine funções avançadas, escopo, decoradores e modularização. Construa código profissional, reutilizável e elegante!</p>
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai dominar:</h4>
            <ul class="learning-objectives">
                <li>Funções avançadas com argumentos flexíveis</li>
                <li>Escopo de variáveis e closures</li>
                <li>Funções lambda e funcionais</li>
                <li>Decoradores e metaprogramação</li>
                <li>Módulos personalizados e packages</li>
                <li>Geradores e funções assíncronas</li>
                <li>Documentação profissional de código</li>
                <li>Testes unitários básicos</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico Completo:</h4>
            
            <h5>1. Funções Fundamentais e Avançadas</h5>
            
            <div class="code-example">
                <h6>🔸 Funções Básicas - Construindo Blocos:</h6>
                <pre><code># Função simples sem parâmetros
def saudacao():
    """Exibe uma saudação padrão"""
    print("🎉 Bem-vindo ao Sistema Python!")
    print("Vamos programar juntos!")

# Função com parâmetro único
def saudacao_personalizada(nome):
    """Exibe saudação personalizada"""
    print(f"Olá, {nome}! Que bom te ver aqui! 😊")

# Função com múltiplos parâmetros
def calcular_area_retangulo(largura, altura):
    """
    Calcula a área de um retângulo
    
    Args:
        largura (float): Largura do retângulo
        altura (float): Altura do retângulo
    
    Returns:
        float: Área calculada
    """
    area = largura * altura
    perimetro = 2 * (largura + altura)
    
    print(f"📐 Dimensões: {largura} x {altura}")
    print(f"📏 Área: {area}")
    print(f"⭕ Perímetro: {perimetro}")
    
    return area

# Chamando as funções
saudacao()
saudacao_personalizada("Maria")
resultado = calcular_area_retangulo(5.0, 3.0)</code></pre>
            </div>
            
            <h5>2. Parâmetros Avançados e Flexibilidade</h5>
            <div class="code-example">
                <pre><code># Parâmetros com valores padrão
def criar_perfil(nome, idade=25, cidade="São Paulo", ativo=True):
    """Cria perfil de usuário com valores padrão"""
    perfil = {
        'nome': nome,
        'idade': idade,
        'cidade': cidade,
        'ativo': ativo,
        'id': hash(nome) % 10000  # ID simples baseado no nome
    }
    return perfil

# Diferentes formas de chamar
perfil1 = criar_perfil("João")  # Usa valores padrão
perfil2 = criar_perfil("Maria", 30)  # Sobrescreve idade
perfil3 = criar_perfil("Pedro", cidade="Rio de Janeiro")  # Argumentos nomeados
perfil4 = criar_perfil(nome="Ana", idade=28, ativo=False)  # Todos nomeados

# *args - Argumentos posicionais variáveis
def calcular_media(*numeros):
    """Calcula média de qualquer quantidade de números"""
    if not numeros:
        return 0
    
    total = sum(numeros)
    quantidade = len(numeros)
    media = total / quantidade
    
    print(f"📊 Números: {numeros}")
    print(f"📈 Soma: {total}")
    print(f"🎯 Média: {media:.2f}")
    
    return media

# Exemplos de uso
media1 = calcular_media(10, 20, 30)
media2 = calcular_media(5, 7, 9, 11, 13, 15)
media3 = calcular_media(100)

# **kwargs - Argumentos nomeados variáveis
def criar_relatorio(**dados):
    """Cria relatório com informações dinâmicas"""
    print("📋 RELATÓRIO GERADO")
    print("=" * 30)
    
    for chave, valor in dados.items():
        chave_formatada = chave.replace('_', ' ').title()
        print(f"{chave_formatada}: {valor}")
    
    print("=" * 30)
    return dados

# Exemplos de uso
relatorio1 = criar_relatorio(
    vendas_hoje=1500,
    clientes_novos=23,
    ticket_medio=65.50
)

relatorio2 = criar_relatorio(
    temperatura_maxima=32,
    umidade=75,
    pressao_atmosferica=1013
)

# Combinando *args e **kwargs
def funcao_completa(obrigatorio, padrao=10, *args, **kwargs):
    """Demonstra todos os tipos de parâmetros"""
    print(f"Obrigatório: {obrigatorio}")
    print(f"Padrão: {padrao}")
    print(f"Args extras: {args}")
    print(f"Kwargs: {kwargs}")

funcao_completa("teste", 20, "extra1", "extra2", nome="João", idade=30)</code></pre>
            </div>
            
            <h5>3. Escopo de Variáveis e Closures</h5>
            <div class="code-example">
                <pre><code># Escopo local vs global
contador_global = 0  # Variável global

def incrementar_contador():
    global contador_global  # Modifica variável global
    contador_global += 1
    contador_local = 100  # Variável local
    print(f"Local: {contador_local}, Global: {contador_global}")

def demonstrar_escopo():
    x = "local"  # Variável local
    
    def funcao_interna():
        nonlocal x  # Modifica variável do escopo envolvente
        x = "modificada"
        y = "muito local"  # Só existe aqui
        print(f"Dentro da função interna: x={x}, y={y}")
    
    print(f"Antes: x={x}")
    funcao_interna()
    print(f"Depois: x={x}")

# Closures - Funções que "lembram" do ambiente
def criar_multiplicador(fator):
    """Cria função que multiplica por um fator específico"""
    def multiplicar(numero):
        return numero * fator  # 'fator' é "lembrado"
    return multiplicar

# Criando multiplicadores específicos
dobrar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
multiplicar_por_10 = criar_multiplicador(10)

print(f"Dobrar 5: {dobrar(5)}")  # 10
print(f"Triplicar 4: {triplicar(4)}")  # 12
print(f"Multiplicar 7 por 10: {multiplicar_por_10(7)}")  # 70

# Closure prático - Contador privado
def criar_contador():
    """Cria contador com estado privado"""
    count = 0
    
    def incrementar():
        nonlocal count
        count += 1
        return count
    
    def decrementar():
        nonlocal count
        count -= 1
        return count
    
    def obter_valor():
        return count
    
    def resetar():
        nonlocal count
        count = 0
        return count
    
    return {
        'incrementar': incrementar,
        'decrementar': decrementar,
        'valor': obter_valor,
        'resetar': resetar
    }

# Usando o contador
contador = criar_contador()
print(f"Valor inicial: {contador['valor']()}")  # 0
print(f"Incrementar: {contador['incrementar']()}")  # 1
print(f"Incrementar: {contador['incrementar']()}")  # 2
print(f"Decrementar: {contador['decrementar']()}")  # 1</code></pre>
            </div>
            
            <h5>4. Funções Lambda e Programação Funcional</h5>
            <div class="code-example">
                <pre><code># Funções lambda - Funções anônimas
# Sintaxe: lambda argumentos: expressão

# Lambda simples
quadrado = lambda x: x ** 2
print(f"Quadrado de 5: {quadrado(5)}")  # 25

# Lambda com múltiplos argumentos
somar = lambda a, b: a + b
print(f"Soma 3 + 7: {somar(3, 7)}")  # 10

# Usando lambda com funções built-in
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() - Aplica função a cada elemento
quadrados = list(map(lambda x: x**2, numeros))
print(f"Quadrados: {quadrados}")

# filter() - Filtra elementos com base em condição
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")

# Exemplo mais complexo com dados estruturados
funcionarios = [
    {'nome': 'João', 'salario': 5000, 'departamento': 'TI'},
    {'nome': 'Maria', 'salario': 6000, 'departamento': 'Vendas'},
    {'nome': 'Pedro', 'salario': 4500, 'departamento': 'TI'},
    {'nome': 'Ana', 'salario': 7000, 'departamento': 'Gerência'}
]

# Filtrando funcionários de TI
funcionarios_ti = list(filter(
    lambda f: f['departamento'] == 'TI', 
    funcionarios
))

# Calculando salários com aumento de 10%
salarios_aumento = list(map(
    lambda f: {**f, 'salario_novo': f['salario'] * 1.1},
    funcionarios
))

# Ordenando por salário (descendente)
funcionarios_ordenados = sorted(
    funcionarios,
    key=lambda f: f['salario'],
    reverse=True
)

print("Funcionários de TI:", funcionarios_ti)
print("Primeiro funcionário ordenado:", funcionarios_ordenados[0])</code></pre>
            </div>
            
            <h5>5. Decoradores - Metaprogramação</h5>
            <div class="code-example">
                <pre><code>import time
import functools

# Decorador simples para medir tempo de execução
def medir_tempo(func):
    """Decorador que mede tempo de execução de função"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"⏱️ {func.__name__} executou em {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

# Decorador para log de função
def log_funcao(func):
    """Decorador que registra chamadas de função"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        params = ', '.join(filter(None, [args_str, kwargs_str]))
        
        print(f"📝 Chamando {func.__name__}({params})")
        resultado = func(*args, **kwargs)
        print(f"✅ {func.__name__} retornou: {resultado}")
        return resultado
    return wrapper

# Decorador com parâmetros
def repetir(vezes):
    """Decorador que repete execução de função"""
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(vezes):
                print(f"🔄 Execução {i+1}/{vezes}")
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

# Usando os decoradores
@medir_tempo
@log_funcao
def calcular_fibonacci(n):
    """Calcula número de Fibonacci"""
    if n <= 1:
        return n
    return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

@repetir(3)
def saudacao_especial(nome):
    """Saudação que será repetida"""
    print(f"🎉 Olá, {nome}!")

# Testando decoradores
resultado_fib = calcular_fibonacci(10)
saudacao_especial("Python")

# Decorador de cache para otimização
def cache(func):
    """Decorador que cacheia resultados de função"""
    cache_dict = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Cria chave única para argumentos
        chave = str(args) + str(sorted(kwargs.items()))
        
        if chave in cache_dict:
            print(f"💾 Cache hit para {func.__name__}")
            return cache_dict[chave]
        
        print(f"🔄 Calculando {func.__name__}")
        resultado = func(*args, **kwargs)
        cache_dict[chave] = resultado
        return resultado
    
    return wrapper

@cache
@medir_tempo
def fibonacci_otimizado(n):
    """Fibonacci com cache para melhor performance"""
    if n <= 1:
        return n
    return fibonacci_otimizado(n-1) + fibonacci_otimizado(n-2)

print(f"Fibonacci de 35: {fibonacci_otimizado(35)}")</code></pre>
            </div>
            
            <h5>6. Módulos e Packages</h5>
            <div class="code-example">
                <pre><code># Criando módulo personalizado (salvar como 'calculadora.py')
# ===========================================

"""
Módulo de Calculadora Avançada
Contém funções matemáticas úteis para cálculos diversos
"""

import math

# Constantes do módulo
PI = 3.14159265359
E = 2.71828182846

def somar(a, b):
    """Soma dois números"""
    return a + b

def subtrair(a, b):
    """Subtrai dois números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dois números"""
    return a * b

def dividir(a, b):
    """Divide dois números com tratamento de erro"""
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal
    
    Args:
        peso (float): Peso em quilogramas
        altura (float): Altura em metros
    
    Returns:
        dict: IMC e classificação
    """
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    
    return {
        'imc': round(imc, 2),
        'classificacao': classificacao
    }

def calcular_juros_compostos(capital, taxa, tempo):
    """
    Calcula juros compostos
    
    Args:
        capital (float): Valor inicial
        taxa (float): Taxa de juros (decimal)
        tempo (int): Período em anos
    
    Returns:
        dict: Montante final e juros ganhos
    """
    montante = capital * (1 + taxa) ** tempo
    juros = montante - capital
    
    return {
        'capital_inicial': capital,
        'montante_final': round(montante, 2),
        'juros_ganhos': round(juros, 2),
        'rentabilidade': round((juros / capital) * 100, 2)
    }

class Calculadora:
    """Classe calculadora com histórico"""
    
    def __init__(self):
        self.historico = []
    
    def calcular(self, operacao, a, b=None):
        """Executa operação e salva no histórico"""
        try:
            if operacao == '+':
                resultado = a + b
                expressao = f"{a} + {b} = {resultado}"
            elif operacao == '-':
                resultado = a - b
                expressao = f"{a} - {b} = {resultado}"
            elif operacao == '*':
                resultado = a * b
                expressao = f"{a} * {b} = {resultado}"
            elif operacao == '/':
                resultado = dividir(a, b)
                expressao = f"{a} / {b} = {resultado}"
            elif operacao == '^':
                resultado = a ** b
                expressao = f"{a} ^ {b} = {resultado}"
            elif operacao == 'sqrt':
                resultado = math.sqrt(a)
                expressao = f"√{a} = {resultado}"
            else:
                raise ValueError(f"Operação '{operacao}' não reconhecida")
            
            self.historico.append(expressao)
            return resultado
            
        except Exception as e:
            error_msg = f"Erro: {e}"
            self.historico.append(error_msg)
            raise
    
    def obter_historico(self):
        """Retorna histórico de cálculos"""
        return self.historico.copy()
    
    def limpar_historico(self):
        """Limpa histórico de cálculos"""
        self.historico.clear()

# Variável global para demonstração
versao_modulo = "1.0.0"

if __name__ == "__main__":
    # Código que só executa se módulo for executado diretamente
    print("Testando módulo calculadora...")
    
    calc = Calculadora()
    print(f"5 + 3 = {calc.calcular('+', 5, 3)}")
    print(f"10 / 2 = {calc.calcular('/', 10, 2)}")
    print(f"Histórico: {calc.obter_historico()}")

# ===========================================
# Usando o módulo (em outro arquivo)

# import calculadora
# from calculadora import Calculadora, calcular_imc
# import calculadora as calc

# # Usando funções do módulo
# resultado = calculadora.somar(10, 20)
# imc_info = calcular_imc(70, 1.75)

# # Usando classe do módulo
# minha_calc = Calculadora()
# resultado = minha_calc.calcular('+', 15, 25)</code></pre>
            </div>
            
            <h5>7. Geradores e Funções Avançadas</h5>
            <div class="code-example">
                <pre><code># Geradores - Funções que produzem valores sob demanda
def fibonacci_generator():
    """Gerador infinito de números de Fibonacci"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usando o gerador
fib = fibonacci_generator()
primeiros_10_fib = [next(fib) for _ in range(10)]
print(f"Primeiros 10 Fibonacci: {primeiros_10_fib}")

# Gerador com parâmetros
def gerar_numeros_pares(limite):
    """Gera números pares até o limite"""
    numero = 0
    while numero <= limite:
        if numero % 2 == 0:
            yield numero
        numero += 1

pares_ate_20 = list(gerar_numeros_pares(20))
print(f"Pares até 20: {pares_ate_20}")

# Generator expression
quadrados = (x**2 for x in range(10))
print(f"Soma dos quadrados: {sum(quadrados)}")

# Função recursiva
def fatorial(n):
    """Calcula fatorial de forma recursiva"""
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

print(f"Fatorial de 5: {fatorial(5)}")

# Função que retorna múltiplos valores
def analisar_numeros(lista):
    """Analisa lista de números e retorna estatísticas"""
    if not lista:
        return 0, 0, 0, 0
    
    total = sum(lista)
    media = total / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    
    return total, media, maximo, minimo

# Desempacotando retorno múltiplo
numeros = [10, 20, 30, 40, 50]
soma, media, max_val, min_val = analisar_numeros(numeros)
print(f"Soma: {soma}, Média: {media}, Max: {max_val}, Min: {min_val}")</code></pre>
            </div>
            
            <div class="alert alert-success">
                <h6><i class="fas fa-lightbulb"></i> Boas Práticas Profissionais:</h6>
                <ul class="mb-0">
                    <li><strong>Princípio DRY:</strong> "Don't Repeat Yourself" - Evite duplicação</li>
                    <li><strong>Função única:</strong> Cada função deve ter uma responsabilidade específica</li>
                    <li><strong>Nomes descritivos:</strong> Use nomes que expliquem o que a função faz</li>
                    <li><strong>Docstrings:</strong> Documente todas as funções importantes</li>
                    <li><strong>Parâmetros padrão:</strong> Use valores padrão para maior flexibilidade</li>
                    <li><strong>Type hints:</strong> Use anotações de tipo para clareza</li>
                    <li><strong>Testes:</strong> Teste suas funções com diferentes entradas</li>
                </ul>
            </div>
            
            <div class="alert alert-warning">
                <h6><i class="fas fa-exclamation-triangle"></i> Armadilhas Comuns:</h6>
                <ul class="mb-0">
                    <li><strong>Mutáveis como padrão:</strong> Evite listas/dicts como valores padrão</li>
                    <li><strong>Escopo global:</strong> Minimize uso de variáveis globais</li>
                    <li><strong>Funções muito grandes:</strong> Divida funções complexas em menores</li>
                    <li><strong>Recursão infinita:</strong> Sempre defina caso base</li>
                    <li><strong>Efeitos colaterais:</strong> Funções devem ser previsíveis</li>
                </ul>
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
        'title': 'Estruturas de Dados',
        'description': 'Domine listas, tuplas, dicionários e conjuntos para organizar dados de forma eficiente',
        'content': '''<div class="module-header">
            <h3>📊 Módulo 5 - Estruturas de Dados</h3>
            <p class="module-intro"><strong>Organize dados como um profissional!</strong> Descubra as estruturas fundamentais do Python: listas, tuplas, dicionários e conjuntos. Aprenda a escolher a estrutura ideal para cada situação!</p>
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai dominar:</h4>
            <ul class="learning-objectives">
                <li>Listas avançadas: criação, manipulação e métodos especiais</li>
                <li>Tuplas e imutabilidade: quando e como usar</li>
                <li>Dicionários: chaves, valores e aplicações práticas</li>
                <li>Conjuntos (sets): operações matemáticas e unicidade</li>
                <li>List comprehensions e geração dinâmica</li>
                <li>Aninhamento e estruturas complexas</li>
                <li>Performance e escolha da estrutura ideal</li>
                <li>Iteração avançada e enumerate/zip</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico Completo:</h4>
            
            <h5>1. Listas - A Estrutura Mais Versátil</h5>
            <p>Listas são coleções ordenadas e mutáveis que podem armazenar qualquer tipo de dado. São a estrutura mais usada em Python!</p>
            
            <div class="code-example">
                <h6>🔸 Criação e Manipulação Básica:</h6>
                <pre><code># Diferentes formas de criar listas
numeros = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "laranja"]
mista = [1, "texto", 3.14, True, [1, 2, 3]]  # Lista com tipos diferentes
vazia = []  # Lista vazia
gerada = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Números: {numeros}")
print(f"Primeira fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")
print(f"Tamanho da lista: {len(frutas)}")

# Modificando elementos
frutas[1] = "uva"  # Substituir banana por uva
print(f"Lista modificada: {frutas}")

# Fatiamento (slicing) avançado
print(f"Primeiros 3 números: {numeros[:3]}")
print(f"Últimos 2 números: {numeros[-2:]}")
print(f"Números pares (passo 2): {numeros[::2]}")
print(f"Lista invertida: {numeros[::-1]}")</code></pre>
                
                <h6>🔸 Métodos Essenciais de Listas:</h6>
                <pre><code># Adicionando elementos
compras = ["leite", "pão"]
compras.append("ovos")  # Adiciona no final
compras.insert(1, "manteiga")  # Adiciona na posição 1
compras.extend(["café", "açúcar"])  # Adiciona múltiplos elementos
print(f"Lista de compras: {compras}")

# Removendo elementos
compras.remove("pão")  # Remove a primeira ocorrência
ultimo_item = compras.pop()  # Remove e retorna o último
segundo_item = compras.pop(1)  # Remove e retorna da posição 1
print(f"Removido: {ultimo_item}, {segundo_item}")

# Encontrando elementos
if "leite" in compras:
    posicao = compras.index("leite")
    print(f"Leite está na posição: {posicao}")

# Contando e organizando
numeros_repetidos = [1, 2, 2, 3, 2, 4, 2]
print(f"O número 2 aparece {numeros_repetidos.count(2)} vezes")

numeros_repetidos.sort()  # Ordena a lista original
print(f"Ordenada: {numeros_repetidos}")

numeros_ordenados = sorted(numeros, reverse=True)  # Cria nova lista ordenada
print(f"Decrescente: {numeros_ordenados}")</code></pre>
            </div>
            
            <h5>2. Tuplas - Dados Imutáveis e Seguros</h5>
            <p>Tuplas são coleções ordenadas e <strong>imutáveis</strong>. Ideais para dados que não devem mudar, como coordenadas, configurações ou retorno de múltiplos valores de funções.</p>
            
            <div class="code-example">
                <pre><code># Criando tuplas
coordenadas = (10, 20)  # Ponto no plano cartesiano
dados_pessoa = ("João", 25, "Engenheiro", True)  # Nome, idade, profissão, ativo
cores_rgb = (255, 128, 0)  # Cor laranja em RGB
tupla_unitaria = ("único",)  # Note a vírgula obrigatória!

# Acessando elementos (igual às listas)
nome = dados_pessoa[0]
profissao = dados_pessoa[2]
print(f"{nome} trabalha como {profissao}")

# Desempacotamento (unpacking) - muito útil!
x, y = coordenadas  # x=10, y=20
nome, idade, prof, status = dados_pessoa
r, g, b = cores_rgb
print(f"Coordenadas: x={x}, y={y}")
print(f"Cor RGB: R={r}, G={g}, B={b}")

# Tuplas como chaves de dicionários (listas não podem!)
pontos_mapa = {
    (0, 0): "origem",
    (10, 20): "ponto A", 
    (30, 40): "ponto B"
}
print(f"No ponto (10, 20) temos: {pontos_mapa[(10, 20)]}")

# Função retornando múltiplos valores
def calcular_circulo(raio):
    import math
    area = math.pi * raio ** 2
    perimetro = 2 * math.pi * raio
    return area, perimetro  # Retorna uma tupla!

area_resultado, perimetro_resultado = calcular_circulo(5)
print(f"Círculo raio 5: Área={area_resultado:.2f}, Perímetro={perimetro_resultado:.2f}")</code></pre>
            </div>
            
            <h5>3. Dicionários - Mapeamento Chave-Valor</h5>
            <p>Dicionários são coleções que armazenam pares chave-valor. Extremamente eficientes para busca e fundamentais em programação moderna!</p>
            
            <div class="code-example">
                <pre><code># Criando dicionários
pessoa = {
    "nome": "Ana Silva",
    "idade": 28,
    "profissao": "Desenvolvedora",
    "salario": 8500.00,
    "ativo": True
}

# Diferentes formas de criar
vazio = {}
usando_dict = dict(a=1, b=2, c=3)
de_listas = dict([("x", 10), ("y", 20)])

print(f"Pessoa: {pessoa['nome']}, {pessoa['idade']} anos")

# Acessando com segurança
salario = pessoa.get("salario", 0)  # Retorna 0 se não existir
bonus = pessoa.get("bonus", "Não definido")
print(f"Salário: R$ {salario}, Bônus: {bonus}")

# Modificando e adicionando
pessoa["idade"] = 29  # Modificar existente
pessoa["cidade"] = "São Paulo"  # Adicionar novo
pessoa.update({"telefone": "11999999999", "email": "ana@email.com"})

# Removendo elementos
departamento = pessoa.pop("departamento", "TI")  # Remove e retorna, ou valor padrão
print(f"Departamento: {departamento}")

# Iterando sobre dicionários
print("\n=== Dados da Pessoa ===")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")

print(f"\nChaves disponíveis: {list(pessoa.keys())}")
print(f"Valores: {list(pessoa.values())}")

# Dicionário aninhado - estruturas complexas
empresa = {
    "nome": "TechCorp",
    "funcionarios": {
        "001": {"nome": "João", "cargo": "Dev", "salario": 7000},
        "002": {"nome": "Maria", "cargo": "Designer", "salario": 6500},
        "003": {"nome": "Pedro", "cargo": "Manager", "salario": 12000}
    },
    "departamentos": ["TI", "RH", "Vendas"]
}

# Acessando dados aninhados
funcionario_001 = empresa["funcionarios"]["001"]
print(f"\nFuncionário 001: {funcionario_001['nome']} - {funcionario_001['cargo']}")

# Calculando estatísticas
salarios = [func["salario"] for func in empresa["funcionarios"].values()]
salario_medio = sum(salarios) / len(salarios)
print(f"Salário médio da empresa: R$ {salario_medio:.2f}")</code></pre>
            </div>
            
            <h5>4. Conjuntos (Sets) - Valores Únicos</h5>
            <p>Sets são coleções de elementos únicos, ideais para eliminar duplicatas e realizar operações matemáticas como união, interseção e diferença.</p>
            
            <div class="code-example">
                <pre><code># Criando conjuntos
numeros_unicos = {1, 2, 3, 4, 5}
frutas_set = {"maçã", "banana", "laranja"}
de_lista = set([1, 2, 2, 3, 3, 4])  # Remove duplicatas automaticamente!
print(f"De lista com duplicatas: {de_lista}")  # {1, 2, 3, 4}

# Adicionando e removendo
frutas_set.add("uva")
frutas_set.discard("banana")  # Remove se existir
# frutas_set.remove("banana")  # Erro se não existir
print(f"Frutas: {frutas_set}")

# Operações de conjuntos - muito poderosas!
funcionarios_ti = {"Ana", "Bruno", "Carlos", "Diana"}
funcionarios_vendas = {"Bruno", "Elena", "Fabio", "Ana"}

# União - todos os funcionários
todos = funcionarios_ti | funcionarios_vendas
# ou: todos = funcionarios_ti.union(funcionarios_vendas)
print(f"Todos os funcionários: {todos}")

# Interseção - funcionários que trabalham nos dois departamentos
ambos_depto = funcionarios_ti & funcionarios_vendas
print(f"Trabalham em ambos: {ambos_depto}")

# Diferença - só em TI
so_ti = funcionarios_ti - funcionarios_vendas
print(f"Apenas em TI: {so_ti}")

# Diferença simétrica - em um ou outro, mas não ambos
xor_depto = funcionarios_ti ^ funcionarios_vendas
print(f"Apenas em um departamento: {xor_depto}")

# Verificações úteis
print(f"Ana trabalha em TI? {'Ana' in funcionarios_ti}")
print(f"TI é subconjunto de todos? {funcionarios_ti.issubset(todos)}")

# Removendo duplicatas de listas grandes
lista_com_duplicatas = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
lista_unica = list(set(lista_com_duplicatas))
print(f"Lista sem duplicatas: {lista_unica}")</code></pre>
            </div>
            
            <h5>5. List Comprehensions - Geração Elegante</h5>
            <p>List comprehensions permitem criar listas de forma concisa e pythônica, combinando criação e filtros em uma linha!</p>
            
            <div class="code-example">
                <pre><code># Forma tradicional vs List Comprehension
# Tradicional
quadrados_tradicional = []
for x in range(10):
    quadrados_tradicional.append(x ** 2)

# List Comprehension - muito mais elegante!
quadrados = [x ** 2 for x in range(10)]
print(f"Quadrados: {quadrados}")

# Com condições (filtros)
pares = [x for x in range(20) if x % 2 == 0]
numeros_grandes = [x for x in range(100) if x > 50 and x % 3 == 0]
print(f"Pares: {pares}")
print(f"Grandes múltiplos de 3: {numeros_grandes}")

# Transformações de strings
nomes = ["joão", "maria", "pedro", "ana"]
nomes_formatados = [nome.title() for nome in nomes]
iniciais = [nome[0].upper() for nome in nomes]
print(f"Nomes formatados: {nomes_formatados}")
print(f"Iniciais: {iniciais}")

# List comprehensions aninhadas
matriz = [[i + j for j in range(3)] for i in range(3)]
print(f"Matriz 3x3: {matriz}")

# Achatando listas aninhadas
listas_aninhadas = [[1, 2], [3, 4], [5, 6]]
achatada = [item for sublista in listas_aninhadas for item in sublista]
print(f"Lista achatada: {achatada}")

# Dict e Set comprehensions também existem!
quadrados_dict = {x: x**2 for x in range(5)}
print(f"Dicionário de quadrados: {quadrados_dict}")

letras_unicas = {letra for palavra in ["python", "programacao"] for letra in palavra}
print(f"Letras únicas: {letras_unicas}")</code></pre>
            </div>
            
            <h5>6. Técnicas Avançadas de Iteração</h5>
            <div class="code-example">
                <pre><code># Enumerate - índice + valor
frutas = ["maçã", "banana", "laranja"]
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# Enumerate com início personalizado
for indice, fruta in enumerate(frutas, start=1):
    print(f"Fruta #{indice}: {fruta}")

# Zip - combinando listas
nomes = ["Ana", "Bruno", "Carlos"]
idades = [25, 30, 35]
cidades = ["SP", "RJ", "BH"]

for nome, idade, cidade in zip(nomes, idades, cidades):
    print(f"{nome}, {idade} anos, mora em {cidade}")

# Criando dicionário com zip
pessoas_info = dict(zip(nomes, idades))
print(f"Idades: {pessoas_info}")

# Iteração paralela em dicionários
pontuacoes = {"Ana": 95, "Bruno": 87, "Carlos": 92}
posicoes = {"Ana": 1, "Bruno": 3, "Carlos": 2}

for nome in pontuacoes:
    print(f"{nome}: {pontuacoes[nome]} pontos, posição {posicoes[nome]}")</code></pre>
            </div>
            
            <div class="alert alert-info">
                <h6>🎯 Guia de Escolha: Qual Estrutura Usar?</h6>
                <ul class="mb-0">
                    <li><strong>Lista:</strong> Quando precisar de ordem, modificação e permitir duplicatas</li>
                    <li><strong>Tupla:</strong> Para dados imutáveis, coordenadas, retorno de funções</li>
                    <li><strong>Dicionário:</strong> Para mapeamento chave-valor, busca rápida por identificador</li>
                    <li><strong>Set:</strong> Para eliminar duplicatas e operações matemáticas de conjuntos</li>
                </ul>
            </div>
            
            <div class="alert alert-success">
                <h6>💡 Dicas de Performance:</h6>
                <ul class="mb-0">
                    <li>Dicionários têm busca O(1) - muito rápidos para chaves</li>
                    <li>Sets têm verificação O(1) para membership (in)</li>
                    <li>Listas têm busca O(n) - evite em listas muito grandes</li>
                    <li>Use list comprehensions - são mais rápidas que loops tradicionais</li>
                </ul>
            </div>
            
            <div class="alert alert-warning">
                <h6>⚠️ Pegadinhas Comuns:</h6>
                <ul class="mb-0">
                    <li>Dicionários mantêm ordem de inserção (Python 3.7+)</li>
                    <li>Sets não têm ordem garantida</li>
                    <li>Tupla de um elemento precisa de vírgula: (1,)</li>
                    <li>Chaves de dicionário devem ser imutáveis (int, str, tupla)</li>
                </ul>
            </div>
        </div>''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Como adicionar um elemento ao final de uma lista?',
                'options': ['lista.add(elemento)', 'lista.append(elemento)', 'lista.insert(elemento)', 'lista.push(elemento)'],
                'correct_answer': 'lista.append(elemento)'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual é a principal diferença entre listas e tuplas?',
                'options': ['Listas são maiores', 'Tuplas são imutáveis', 'Listas são mais rápidas', 'Tuplas não têm métodos'],
                'correct_answer': 'Tuplas são imutáveis'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como acessar um valor em um dicionário de forma segura?',
                'options': ['dict[chave]', 'dict.get(chave)', 'dict.value(chave)', 'dict.access(chave)'],
                'correct_answer': 'dict.get(chave)'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual estrutura elimina automaticamente elementos duplicados?',
                'options': ['Lista', 'Tupla', 'Dicionário', 'Conjunto (set)'],
                'correct_answer': 'Conjunto (set)'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual é a saída de: [x**2 for x in range(3)]?',
                'options': ['[0, 1, 4]', '[1, 4, 9]', '[0, 2, 4]', '[1, 2, 3]'],
                'correct_answer': '[0, 1, 4]'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como verificar se uma chave existe em um dicionário?',
                'options': ['chave in dict', 'dict.has(chave)', 'dict.exists(chave)', 'dict.contains(chave)'],
                'correct_answer': 'chave in dict'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual método une duas listas em Python?',
                'options': ['lista.join(outra)', 'lista.concat(outra)', 'lista.extend(outra)', 'lista.merge(outra)'],
                'correct_answer': 'lista.extend(outra)'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como criar uma tupla com apenas um elemento?',
                'options': ['(elemento)', '(elemento,)', '[elemento]', '{elemento}'],
                'correct_answer': '(elemento,)'
            }
        ]
    },
    6: {
        'title': 'Programação Orientada a Objetos',
        'description': 'Domine classes, objetos, herança e encapsulamento para criar código profissional e reutilizável',
        'content': '''<div class="module-header">
            <h3>🏢 Módulo 6 - Programação Orientada a Objetos</h3>
            <p class="module-intro"><strong>Construa código como um arquiteto profissional!</strong> Domine os pilares da POO: classes, objetos, herança, encapsulamento e polimorfismo. Transforme-se em um desenvolvedor que pensa em objetos!</p>
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai dominar:</h4>
            <ul class="learning-objectives">
                <li>Conceitos fundamentais de classes e objetos</li>
                <li>Atributos de instância e de classe</li>
                <li>Métodos especiais e mágicos (__init__, __str__, etc.)</li>
                <li>Herança simples e múltipla</li>
                <li>Encapsulamento e propriedades</li>
                <li>Polimorfismo e sobrescrita de métodos</li>
                <li>Composição vs Herança</li>
                <li>Design patterns básicos</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico Completo:</h4>
            
            <h5>1. Fundamentos de Classes e Objetos</h5>
            <p>A Programação Orientada a Objetos é um paradigma que organiza código em "objetos" que representam entidades do mundo real, cada uma com características (atributos) e comportamentos (métodos).</p>
            
            <div class="alert alert-info">
                <h6>🧠 Conceitos Essenciais:</h6>
                <ul class="mb-0">
                    <li><strong>Classe:</strong> Um molde/template para criar objetos</li>
                    <li><strong>Objeto:</strong> Uma instância específica de uma classe</li>
                    <li><strong>Atributo:</strong> Características/dados do objeto</li>
                    <li><strong>Método:</strong> Ações/comportamentos que o objeto pode realizar</li>
                </ul>
            </div>
            
            <div class="code-example">
                <h6>🔸 Criando sua Primeira Classe:</h6>
                <pre><code># Definindo uma classe Pessoa
class Pessoa:
    """Classe que representa uma pessoa com nome, idade e profissão"""
    
    # Atributo de classe (compartilhado por todas as instâncias)
    especie = "Homo sapiens"
    
    def __init__(self, nome, idade, profissao="Estudante"):
        """Construtor da classe - inicializa os atributos de instância"""
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.energia = 100
    
    def apresentar(self):
        """Método que faz a pessoa se apresentar"""
        return f"Olá! Eu sou {self.nome}, tenho {self.idade} anos e sou {self.profissao}."
    
    def fazer_aniversario(self):
        """Método que aumenta a idade em 1 ano"""
        self.idade += 1
        print(f"🎉 Parabéns, {self.nome}! Agora você tem {self.idade} anos!")
    
    def trabalhar(self, horas):
        """Método que simula trabalho e reduz energia"""
        if self.energia >= horas * 10:
            self.energia -= horas * 10
            print(f"{self.nome} trabalhou {horas} horas. Energia restante: {self.energia}")
        else:
            print(f"{self.nome} está muito cansado para trabalhar!")
    
    def dormir(self):
        """Método que restaura a energia"""
        self.energia = 100
        print(f"{self.nome} dormiu e está revigorado!")

# Criando objetos (instâncias da classe)
pessoa1 = Pessoa("Maria Silva", 28, "Engenheira")
pessoa2 = Pessoa("João Santos", 35, "Professor")
pessoa3 = Pessoa("Ana Costa", 22)  # Usa valor padrão "Estudante"

# Usando os objetos
print(pessoa1.apresentar())
print(f"Espécie: {pessoa1.especie}")  # Atributo de classe

pessoa1.trabalhar(8)
pessoa1.fazer_aniversario()
pessoa1.dormir()</code></pre>
                
                <h6>🔸 Atributos de Instância vs Classe:</h6>
                <pre><code>class Contador:
    """Classe que demonstra atributos de instância e classe"""
    
    # Atributo de classe - compartilhado por todas as instâncias
    total_objetos = 0
    
    def __init__(self, valor_inicial=0):
        # Atributo de instância - único para cada objeto
        self.valor = valor_inicial
        
        # Incrementa contador global
        Contador.total_objetos += 1
        self.id_objeto = Contador.total_objetos
    
    def incrementar(self, quantidade=1):
        self.valor += quantidade
    
    def info(self):
        return f"Contador #{self.id_objeto}: valor={self.valor}"
    
    @classmethod
    def quantos_objetos(cls):
        """Método de classe - opera sobre a classe, não instância"""
        return f"Total de contadores criados: {cls.total_objetos}"

# Testando atributos de classe
c1 = Contador(10)
c2 = Contador(20)
c3 = Contador()

print(c1.info())  # Contador #1: valor=10
print(c2.info())  # Contador #2: valor=20
print(Contador.quantos_objetos())  # Total de contadores criados: 3

c1.incrementar(5)
print(c1.info())  # Contador #1: valor=15</code></pre>
            </div>
            
            <h5>2. Métodos Especiais (Magic Methods)</h5>
            <p>Python possui métodos especiais que começam e terminam com duplo underscore (__). Eles definem como objetos se comportam em operações específicas.</p>
            
            <div class="code-example">
                <pre><code>class ContaBancaria:
    """Classe que demonstra métodos especiais importantes"""
    
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.historico = []
    
    def __str__(self):
        """Como o objeto aparece em print()"""
        return f"Conta de {self.titular}: R$ {self.saldo:.2f}"
    
    def __repr__(self):
        """Representação técnica do objeto para desenvolvedores"""
        return f"ContaBancaria('{self.titular}', {self.saldo})"
    
    def __len__(self):
        """Define comportamento para len(objeto)"""
        return len(self.historico)
    
    def __eq__(self, outra):
        """Define igualdade entre objetos"""
        return self.titular == outra.titular and self.saldo == outra.saldo
    
    def __lt__(self, outra):
        """Define comparação menor que (<)"""
        return self.saldo < outra.saldo
    
    def __add__(self, valor):
        """Define soma com + """
        if isinstance(valor, (int, float)):
            return ContaBancaria(self.titular, self.saldo + valor)
        return NotImplemented
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: +R$ {valor:.2f}")
        else:
            raise ValueError("Valor de depósito deve ser positivo")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: -R$ {valor:.2f}")
        else:
            raise ValueError("Saldo insuficiente ou valor inválido")

# Testando métodos especiais
conta1 = ContaBancaria("Maria", 1000)
conta2 = ContaBancaria("João", 1500)

print(conta1)  # Usa __str__: Conta de Maria: R$ 1000.00
print(repr(conta1))  # Usa __repr__: ContaBancaria('Maria', 1000)

conta1.depositar(500)
conta1.sacar(200)
print(f"Histórico tem {len(conta1)} transações")  # Usa __len__

# Comparações
print(f"Conta1 < Conta2? {conta1 < conta2}")  # Usa __lt__
print(f"Contas iguais? {conta1 == conta2}")   # Usa __eq__

# Soma
conta3 = conta1 + 100  # Usa __add__
print(f"Nova conta: {conta3}")</code></pre>
            </div>
            
            <h5>3. Herança - Reutilizando e Especializando Código</h5>
            <p>Herança permite criar novas classes baseadas em classes existentes, reutilizando código e adicionando funcionalidades específicas.</p>
            
            <div class="code-example">
                <pre><code># Classe base (superclasse)
class Veiculo:
    """Classe base para todos os veículos"""
    
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self.velocidade = 0
    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.marca} {self.modelo} foi ligado!")
        else:
            print("Veículo já está ligado!")
    
    def desligar(self):
        if self.ligado and self.velocidade == 0:
            self.ligado = False
            print(f"{self.marca} {self.modelo} foi desligado!")
        else:
            print("Pare o veículo antes de desligar!")
    
    def acelerar(self, incremento):
        if self.ligado:
            self.velocidade += incremento
            print(f"Velocidade: {self.velocidade} km/h")
        else:
            print("Ligue o veículo primeiro!")
    
    def info(self):
        status = "Ligado" if self.ligado else "Desligado"
        return f"{self.marca} {self.modelo} ({self.ano}) - {status} - {self.velocidade} km/h"

# Classes filhas (subclasses)
class Carro(Veiculo):
    """Classe específica para carros"""
    
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)  # Chama construtor da classe pai
        self.portas = portas
        self.combustivel = 100
    
    def acelerar(self, incremento):
        """Sobrescreve método da classe pai com comportamento específico"""
        if self.combustivel > 0:
            super().acelerar(incremento)  # Chama método da classe pai
            self.combustivel -= incremento * 0.1  # Consome combustível
            print(f"Combustível: {self.combustivel:.1f}%")
        else:
            print("Sem combustível!")
    
    def abastecer(self):
        self.combustivel = 100
        print("Tanque cheio!")
    
    def info(self):
        base_info = super().info()
        return f"{base_info} - {self.portas} portas - Combustível: {self.combustivel:.1f}%"

class Bicicleta(Veiculo):
    """Classe específica para bicicletas"""
    
    def __init__(self, marca, modelo, ano, marchas):
        super().__init__(marca, modelo, ano)
        self.marchas = marchas
        self.marcha_atual = 1
    
    def ligar(self):
        """Bicicleta não tem motor - sobrescreve comportamento"""
        print("Bicicletas não precisam ser ligadas! Apenas pedale!")
        self.ligado = True
    
    def trocar_marcha(self, nova_marcha):
        if 1 <= nova_marcha <= self.marchas:
            self.marcha_atual = nova_marcha
            print(f"Marcha alterada para {nova_marcha}")
        else:
            print(f"Marcha inválida! Use 1-{self.marchas}")
    
    def info(self):
        base_info = super().info()
        return f"{base_info} - {self.marchas} marchas - Marcha atual: {self.marcha_atual}"

# Usando herança
carro = Carro("Toyota", "Corolla", 2022, 4)
bike = Bicicleta("Caloi", "Mountain", 2021, 21)

print("=== CARRO ===")
print(carro.info())
carro.ligar()
carro.acelerar(50)
carro.abastecer()

print("\n=== BICICLETA ===")
print(bike.info())
bike.ligar()  # Comportamento diferente!
bike.trocar_marcha(5)
bike.acelerar(15)</code></pre>
            </div>
            
            <h5>4. Encapsulamento e Propriedades</h5>
            <p>Encapsulamento protege dados internos e controla como são acessados e modificados, usando convenções de nomenclatura e propriedades.</p>
            
            <div class="code-example">
                <pre><code>class Produto:
    """Classe que demonstra encapsulamento com propriedades"""
    
    def __init__(self, nome, preco, categoria):
        self._nome = nome  # Convenção: _ indica "privado"
        self._preco = 0
        self._categoria = categoria
        self.__codigo = self._gerar_codigo()  # __ é "muito privado"
        self.preco = preco  # Usa o setter para validar
    
    def _gerar_codigo(self):
        """Método privado para gerar código interno"""
        import random
        return f"{self._categoria[:3].upper()}{random.randint(1000, 9999)}"
    
    @property
    def nome(self):
        """Getter para nome"""
        return self._nome.title()
    
    @nome.setter
    def nome(self, valor):
        """Setter para nome com validação"""
        if isinstance(valor, str) and len(valor) >= 2:
            self._nome = valor
        else:
            raise ValueError("Nome deve ser string com pelo menos 2 caracteres")
    
    @property
    def preco(self):
        """Getter para preço"""
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        """Setter para preço com validação"""
        if isinstance(valor, (int, float)) and valor >= 0:
            self._preco = float(valor)
        else:
            raise ValueError("Preço deve ser número positivo")
    
    @property
    def codigo(self):
        """Propriedade somente leitura"""
        return self.__codigo
    
    def aplicar_desconto(self, percentual):
        """Método público para aplicar desconto"""
        if 0 <= percentual <= 50:  # Máximo 50% desconto
            desconto = self._preco * (percentual / 100)
            self._preco -= desconto
            print(f"Desconto de {percentual}% aplicado! Novo preço: R$ {self._preco:.2f}")
        else:
            raise ValueError("Desconto deve estar entre 0% e 50%")
    
    def __str__(self):
        return f"{self.nome} ({self.codigo}) - R$ {self.preco:.2f}"

# Demonstrando encapsulamento
produto = Produto("notebook gamer", 2500.00, "eletrônicos")

print(produto)  # notebook gamer (ELE1234) - R$ 2500.00
print(f"Código: {produto.codigo}")  # Acesso somente leitura

# Usando setters com validação
produto.nome = "Notebook Gamer RGB"
produto.preco = 2200.00

# Tentativas inválidas causarão erros
try:
    produto.preco = -100  # ValueError!
except ValueError as e:
    print(f"Erro: {e}")

produto.aplicar_desconto(10)  # Método controlado para mudanças</code></pre>
            </div>
            
            <h5>5. Polimorfismo - Uma Interface, Múltiplos Comportamentos</h5>
            <p>Polimorfismo permite que objetos de diferentes classes sejam tratados de forma uniforme através de uma interface comum.</p>
            
            <div class="code-example">
                <pre><code>class Animal:
    """Classe base para demonstrar polimorfismo"""
    
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    def fazer_som(self):
        """Método que será sobrescrito pelas subclasses"""
        return "Som genérico de animal"
    
    def mover(self):
        return f"{self.nome} se move"

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Canino")
        self.raca = raca
    
    def fazer_som(self):
        return "Au au!"
    
    def mover(self):
        return f"{self.nome} corre e pula"

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, "Felino")
        self.cor = cor
    
    def fazer_som(self):
        return "Miau!"
    
    def mover(self):
        return f"{self.nome} caminha silenciosamente"

class Pato(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Ave")
    
    def fazer_som(self):
        return "Quack!"
    
    def mover(self):
        return f"{self.nome} nada e voa"

# Lista com diferentes tipos de animais
animais = [
    Cachorro("Rex", "Labrador"),
    Gato("Mimi", "Branco"),
    Pato("Donald"),
    Cachorro("Bolt", "Pastor Alemão")
]

# Polimorfismo em ação - mesmo código, comportamentos diferentes
print("=== FAZENDO SONS ===")
for animal in animais:
    print(f"{animal.nome}: {animal.fazer_som()}")

print("\n=== MOVIMENTOS ===")
for animal in animais:
    print(animal.mover())

# Função que aceita qualquer animal (polimorfismo)
def apresentar_animal(animal):
    """Função polimórfica - funciona com qualquer subclasse de Animal"""
    print(f"Este é {animal.nome}, um {animal.especie}")
    print(f"Ele faz: {animal.fazer_som()}")
    print(f"Movimento: {animal.mover()}")
    print("-" * 30)

# Testando polimorfismo
for animal in animais:
    apresentar_animal(animal)</code></pre>
            </div>
            
            <h5>6. Composição vs Herança</h5>
            <p>Nem sempre herança é a melhor solução. Composição permite construir objetos complexos combinando objetos mais simples.</p>
            
            <div class="code-example">
                <pre><code># Composição - "tem um" relacionamento
class Motor:
    def __init__(self, potencia, tipo_combustivel):
        self.potencia = potencia
        self.tipo_combustivel = tipo_combustivel
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
        return f"Motor {self.potencia}HP ligado!"
    
    def desligar(self):
        self.ligado = False
        return "Motor desligado!"

class GPS:
    def __init__(self):
        self.destino = None
    
    def definir_destino(self, local):
        self.destino = local
        return f"Destino definido: {local}"
    
    def navegar(self):
        if self.destino:
            return f"Navegando para {self.destino}..."
        return "Defina um destino primeiro!"

class CarroCompleto:
    """Classe que usa composição em vez de herança"""
    
    def __init__(self, marca, modelo, potencia_motor):
        self.marca = marca
        self.modelo = modelo
        # Composição - carro "tem um" motor e "tem um" GPS
        self.motor = Motor(potencia_motor, "Gasolina")
        self.gps = GPS()
        self.velocidade = 0
    
    def ligar(self):
        return self.motor.ligar()
    
    def acelerar(self, incremento):
        if self.motor.ligado:
            self.velocidade += incremento
            return f"Acelerando... Velocidade: {self.velocidade} km/h"
        return "Ligue o motor primeiro!"
    
    def navegar_para(self, destino):
        self.gps.definir_destino(destino)
        return self.gps.navegar()
    
    def info_completa(self):
        motor_status = "Ligado" if self.motor.ligado else "Desligado"
        gps_info = f"GPS: {self.gps.destino}" if self.gps.destino else "GPS sem destino"
        return f"{self.marca} {self.modelo} - Motor: {motor_status} - {gps_info}"

# Usando composição
carro = CarroCompleto("Honda", "Civic", 150)
print(carro.info_completa())
print(carro.ligar())
print(carro.acelerar(30))
print(carro.navegar_para("Shopping Center"))
print(carro.info_completa())</code></pre>
            </div>
            
            <div class="alert alert-success">
                <h6>🎯 Vantagens da POO:</h6>
                <ul class="mb-0">
                    <li><strong>Reutilização:</strong> Classes podem ser reutilizadas em diferentes projetos</li>
                    <li><strong>Manutenibilidade:</strong> Código organizado é mais fácil de manter</li>
                    <li><strong>Modularidade:</strong> Cada classe tem responsabilidade específica</li>
                    <li><strong>Extensibilidade:</strong> Fácil adicionar novas funcionalidades</li>
                </ul>
            </div>
            
            <div class="alert alert-info">
                <h6>🧭 Quando Usar Herança vs Composição:</h6>
                <ul class="mb-0">
                    <li><strong>Herança:</strong> Quando há relacionamento "é um" (Carro é um Veículo)</li>
                    <li><strong>Composição:</strong> Quando há relacionamento "tem um" (Carro tem um Motor)</li>
                    <li><strong>Regra geral:</strong> Prefira composição quando possível</li>
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
                'question': 'O que significa "self" em Python?',
                'options': ['Referência ao objeto atual', 'Nome da classe', 'Método especial', 'Variável global'],
                'correct_answer': 'Referência ao objeto atual'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que é herança em POO?',
                'options': ['Copiar código', 'Uma classe filha herda características da classe pai', 'Deletar classes', 'Renomear métodos'],
                'correct_answer': 'Uma classe filha herda características da classe pai'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como indicar que um atributo é "privado" por convenção?',
                'options': ['Usar maiúscula', 'Começar com _', 'Usar @private', 'Começar com #'],
                'correct_answer': 'Começar com _'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual método especial define como um objeto aparece em print()?',
                'options': ['__repr__', '__str__', '__print__', '__show__'],
                'correct_answer': '__str__'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como chamar o construtor da classe pai?',
                'options': ['parent().__init__()', 'super().__init__()', 'base().__init__()', 'father().__init__()'],
                'correct_answer': 'super().__init__()'
            },
            {
                'type': 'multiple_choice',
                'question': 'O que é polimorfismo?',
                'options': ['Múltiplos construtores', 'Múltiplas heranças', 'Mesma interface, comportamentos diferentes', 'Métodos privados'],
                'correct_answer': 'Mesma interface, comportamentos diferentes'
            }
        ]
    },
    7: {
        'title': 'Tratamento de Exceções',
        'description': 'Aprenda a lidar com erros de forma profissional usando try, except, finally e raise',
        'content': '''<div class="module-header">
            <h3>⚠️ Módulo 7 - Tratamento de Exceções</h3>
            <p class="module-intro"><strong>Torne seus programas à prova de erros!</strong> Domine o tratamento profissional de exceções, antecipe problemas e crie aplicações robustas que nunca quebram inesperadamente!</p>
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai dominar:</h4>
            <ul class="learning-objectives">
                <li>Tipos de exceções e hierarquia completa</li>
                <li>Blocos try, except, else, finally avançados</li>
                <li>Captura específica vs genérica de exceções</li>
                <li>Lançamento controlado com raise</li>
                <li>Criação de exceções personalizadas</li>
                <li>Context managers e with statement</li>
                <li>Debugging e logging de erros</li>
                <li>Estratégias de recuperação de erros</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico Completo:</h4>
            
            <h5>1. Por que Tratar Exceções é Fundamental?</h5>
            <p>Exceções são eventos que interrompem o fluxo normal do programa. Em aplicações profissionais, tratar exceções adequadamente é a diferença entre um software confiável e um que "quebra" constantemente.</p>
            
            <div class="alert alert-warning">
                <h6>🚨 Exceções Comuns e Suas Causas:</h6>
                <ul class="mb-0">
                    <li><code>ZeroDivisionError</code> - Divisão por zero</li>
                    <li><code>ValueError</code> - Valor inadequado para o tipo</li>
                    <li><code>TypeError</code> - Operação com tipo incorreto</li>
                    <li><code>FileNotFoundError</code> - Arquivo não encontrado</li>
                    <li><code>KeyError</code> - Chave inexistente em dicionário</li>
                    <li><code>IndexError</code> - Índice fora dos limites</li>
                    <li><code>AttributeError</code> - Atributo inexistente</li>
                    <li><code>ImportError</code> - Módulo não encontrado</li>
                </ul>
            </div>
            
            <div class="code-example">
                <h6>🔸 Tratamento Básico vs Avançado:</h6>
                <pre><code># ❌ Código sem tratamento - PERIGOSO!
def dividir_perigoso(a, b):
    return a / b  # Pode gerar ZeroDivisionError!

# ✅ Código com tratamento básico
def dividir_basico(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Erro: Divisão por zero!")
        return None

# 🎯 Código com tratamento profissional
def dividir_profissional(a, b):
    """
    Divisão segura com tratamento completo de exceções
    
    Args:
        a: Dividendo (número)
        b: Divisor (número) 
        
    Returns:
        float: Resultado da divisão ou None se inválida
        
    Raises:
        TypeError: Se argumentos não forem números
        ValueError: Se divisor for zero
    """
    # Validação de tipos
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Argumentos devem ser números")
    
    # Validação de valor
    if b == 0:
        raise ValueError("Divisor não pode ser zero")
    
    try:
        resultado = a / b
        print(f"✅ Divisão realizada: {a} ÷ {b} = {resultado}")
        return resultado
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return None

# Testando as versões
print(dividir_profissional(10, 2))   # ✅ 5.0
print(dividir_profissional(10, 0))   # ❌ ValueError
print(dividir_profissional("10", 2)) # ❌ TypeError</code></pre>
            </div>
            
            <h5>2. Blocos Try-Except Avançados</h5>
            <p>Domine todas as possibilidades dos blocos de tratamento para criar código robusto e informativo.</p>
            
            <div class="code-example">
                <pre><code># Estrutura completa do tratamento de exceções
def processar_arquivo_completo(nome_arquivo):
    """Demonstra tratamento completo com try-except-else-finally"""
    
    arquivo = None
    dados_processados = 0
    
    try:
        print(f"🔍 Tentando abrir arquivo: {nome_arquivo}")
        arquivo = open(nome_arquivo, 'r', encoding='utf-8')
        
        print("📖 Lendo conteúdo...")
        conteudo = arquivo.read()
        
        print("🔢 Processando dados...")
        linhas = conteudo.split('\n')
        dados_processados = len([linha for linha in linhas if linha.strip()])
        
        # Simular possível erro de processamento
        if dados_processados == 0:
            raise ValueError("Arquivo vazio ou apenas com linhas em branco")
            
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{nome_arquivo}' não encontrado!")
        return None
        
    except PermissionError:
        print(f"❌ Erro: Sem permissão para ler '{nome_arquivo}'!")
        return None
        
    except UnicodeDecodeError:
        print(f"❌ Erro: Problema de encoding no arquivo '{nome_arquivo}'!")
        return None
        
    except ValueError as e:
        print(f"❌ Erro de valor: {e}")
        return None
        
    except Exception as e:
        print(f"❌ Erro inesperado: {type(e).__name__}: {e}")
        return None
        
    else:
        # Executado APENAS se NÃO houve exceções
        print(f"✅ Arquivo processado com sucesso!")
        print(f"📊 Total de linhas válidas: {dados_processados}")
        
    finally:
        # Executado SEMPRE, independente de exceções
        if arquivo and not arquivo.closed:
            arquivo.close()
            print("🔒 Arquivo fechado com segurança")
        
        print("🏁 Processamento finalizado")
    
    return dados_processados

# Testando diferentes cenários
print("=== Teste 1: Arquivo existente ===")
resultado1 = processar_arquivo_completo("dados.txt")

print("\n=== Teste 2: Arquivo inexistente ===")
resultado2 = processar_arquivo_completo("inexistente.txt")</code></pre>
                
                <h6>🔸 Capturando Múltiplas Exceções:</h6>
                <pre><code>def converter_numero_robusto(entrada):
    """Converte string para número com múltiplas validações"""
    
    try:
        # Tentativa 1: Converter para inteiro
        if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
            return int(entrada)
        
        # Tentativa 2: Converter para float
        return float(entrada)
        
    except (ValueError, TypeError) as e:
        # Capturando múltiplas exceções em uma linha
        print(f"❌ Erro de conversão: {e}")
        return None
        
    except AttributeError:
        # entrada não é string (não tem método isdigit)
        print("❌ Entrada deve ser uma string")
        return None

# Função mais complexa com validações aninhadas
def calcular_media_notas():
    """Calcula média de notas com tratamento robusto"""
    
    notas = []
    
    while True:
        try:
            entrada = input("Digite uma nota (ou 'fim' para calcular): ")
            
            if entrada.lower() == 'fim':
                break
                
            nota = float(entrada)
            
            # Validação de range
            if not 0 <= nota <= 10:
                raise ValueError(f"Nota deve estar entre 0 e 10, recebido: {nota}")
            
            notas.append(nota)
            print(f"✅ Nota {nota} adicionada")
            
        except ValueError as e:
            if "could not convert" in str(e):
                print("❌ Digite um número válido!")
            else:
                print(f"❌ {e}")
                
        except KeyboardInterrupt:
            print("\n❌ Operação cancelada pelo usuário")
            return None
            
        except EOFError:
            print("\n❌ Entrada finalizada inesperadamente")
            break
    
    if not notas:
        print("❌ Nenhuma nota foi inserida")
        return None
    
    try:
        media = sum(notas) / len(notas)
        print(f"📊 Média das {len(notas)} notas: {media:.2f}")
        return media
        
    except ZeroDivisionError:  # Teoricamente impossível aqui, mas boa prática
        print("❌ Erro: Divisão por zero (sem notas)")
        return None

# Exemplo de uso (comentado para não interromper execução)
# calcular_media_notas()</code></pre>
            </div>
            
            <h5>3. Lançamento Controlado de Exceções</h5>
            <p>Use <code>raise</code> para lançar exceções em situações específicas, controlando o fluxo do programa.</p>
            
            <div class="code-example">
                <pre><code>class ValidadorDados:
    """Classe que demonstra uso profissional de raise"""
    
    @staticmethod
    def validar_email(email):
        """Valida formato de email"""
        if not isinstance(email, str):
            raise TypeError("Email deve ser uma string")
        
        if not email:
            raise ValueError("Email não pode estar vazio")
        
        if '@' not in email:
            raise ValueError("Email deve conter @")
        
        if email.count('@') != 1:
            raise ValueError("Email deve conter exatamente um @")
        
        partes = email.split('@')
        if not partes[0] or not partes[1]:
            raise ValueError("Email deve ter usuário e domínio")
        
        if '.' not in partes[1]:
            raise ValueError("Domínio deve conter pelo menos um ponto")
        
        return True
    
    @staticmethod  
    def validar_idade(idade):
        """Valida idade com regras específicas"""
        if not isinstance(idade, int):
            raise TypeError(f"Idade deve ser inteiro, recebido {type(idade).__name__}")
        
        if idade < 0:
            raise ValueError("Idade não pode ser negativa")
        
        if idade > 150:
            raise ValueError("Idade não pode ser maior que 150 anos")
        
        return True
    
    @staticmethod
    def validar_senha(senha):
        """Valida força da senha"""
        if not isinstance(senha, str):
            raise TypeError("Senha deve ser string")
        
        if len(senha) < 8:
            raise ValueError("Senha deve ter pelo menos 8 caracteres")
        
        if not any(c.isupper() for c in senha):
            raise ValueError("Senha deve ter pelo menos uma maiúscula")
        
        if not any(c.islower() for c in senha):
            raise ValueError("Senha deve ter pelo menos uma minúscula")
        
        if not any(c.isdigit() for c in senha):
            raise ValueError("Senha deve ter pelo menos um número")
        
        return True

# Sistema de cadastro usando validações
def cadastrar_usuario(email, idade, senha):
    """Cadastra usuário com validações completas"""
    
    try:
        print("🔍 Validando dados...")
        
        ValidadorDados.validar_email(email)
        print("✅ Email válido")
        
        ValidadorDados.validar_idade(idade)
        print("✅ Idade válida")
        
        ValidadorDados.validar_senha(senha)
        print("✅ Senha válida")
        
        # Simular salvamento no banco
        print(f"💾 Usuário cadastrado: {email}, {idade} anos")
        return True
        
    except (TypeError, ValueError) as e:
        print(f"❌ Erro de validação: {e}")
        return False
        
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

# Testando validações
print("=== Teste de Cadastro ===")
sucesso = cadastrar_usuario("user@email.com", 25, "MinhaSenh@123")
print(f"Cadastro {'bem-sucedido' if sucesso else 'falhou'}")

print("\n=== Teste com Dados Inválidos ===")
sucesso = cadastrar_usuario("email_invalido", -5, "123")</code></pre>
            </div>
            
            <h5>4. Exceções Personalizadas</h5>
            <p>Crie suas próprias exceções para situações específicas do seu domínio de aplicação.</p>
            
            <div class="code-example">
                <pre><code># Hierarquia de exceções personalizadas
class ErroSistemaFinanceiro(Exception):
    """Exceção base para sistema financeiro"""
    pass

class ErroContaInexistente(ErroSistemaFinanceiro):
    """Exceção para conta não encontrada"""
    pass

class ErroSaldoInsuficiente(ErroSistemaFinanceiro):
    """Exceção para saldo insuficiente"""
    
    def __init__(self, saldo_atual, valor_tentativa):
        self.saldo_atual = saldo_atual
        self.valor_tentativa = valor_tentativa
        super().__init__(f"Saldo insuficiente: R$ {saldo_atual:.2f}, tentativa: R$ {valor_tentativa:.2f}")

class ErroLimiteCredito(ErroSistemaFinanceiro):
    """Exceção para limite de crédito excedido"""
    
    def __init__(self, limite, valor_tentativa):
        self.limite = limite
        self.valor_tentativa = valor_tentativa
        mensagem = f"Limite de crédito excedido. Limite: R$ {limite:.2f}, Tentativa: R$ {valor_tentativa:.2f}"
        super().__init__(mensagem)

class ContaBancaria:
    """Sistema bancário com exceções personalizadas"""
    
    def __init__(self, numero, titular, saldo_inicial=0, limite_credito=1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial
        self.limite_credito = limite_credito
        self.historico = []
    
    def depositar(self, valor):
        """Deposita valor na conta"""
        if valor <= 0:
            raise ValueError("Valor de depósito deve ser positivo")
        
        self.saldo += valor
        self.historico.append(f"Depósito: +R$ {valor:.2f}")
        print(f"✅ Depósito realizado: R$ {valor:.2f}")
        
    def sacar(self, valor):
        """Saca valor da conta com verificações"""
        if valor <= 0:
            raise ValueError("Valor de saque deve ser positivo")
        
        # Verificar se há saldo suficiente
        if valor > self.saldo:
            raise ErroSaldoInsuficiente(self.saldo, valor)
        
        self.saldo -= valor
        self.historico.append(f"Saque: -R$ {valor:.2f}")
        print(f"✅ Saque realizado: R$ {valor:.2f}")
    
    def usar_credito(self, valor):
        """Usa crédito pré-aprovado"""
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        
        # Verificar limite de crédito
        if valor > self.limite_credito:
            raise ErroLimiteCredito(self.limite_credito, valor)
        
        # Usar crédito (saldo pode ficar negativo)
        self.saldo -= valor
        self.historico.append(f"Crédito usado: -R$ {valor:.2f}")
        print(f"✅ Crédito utilizado: R$ {valor:.2f}")
    
    def extrato(self):
        """Exibe extrato da conta"""
        print(f"\n=== EXTRATO - Conta {self.numero} ===")
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print(f"Limite de crédito: R$ {self.limite_credito:.2f}")
        print("\nHistórico:")
        for transacao in self.historico:
            print(f"  {transacao}")

# Sistema bancário usando exceções personalizadas
def simular_operacoes_bancarias():
    """Simula operações bancárias com tratamento de exceções"""
    
    conta = ContaBancaria("12345", "João Silva", 1000, 500)
    
    operacoes = [
        ("depositar", 200),
        ("sacar", 300),
        ("sacar", 1500),      # Vai dar erro de saldo
        ("usar_credito", 400),
        ("usar_credito", 200), # Vai dar erro de limite
    ]
    
    for operacao, valor in operacoes:
        try:
            print(f"\n🔄 Tentando {operacao} R$ {valor:.2f}")
            
            if operacao == "depositar":
                conta.depositar(valor)
            elif operacao == "sacar":
                conta.sacar(valor)
            elif operacao == "usar_credito":
                conta.usar_credito(valor)
                
        except ErroSaldoInsuficiente as e:
            print(f"❌ Erro específico: {e}")
            print(f"💡 Sugestão: Use crédito ou deposite R$ {e.valor_tentativa - e.saldo_atual:.2f}")
            
        except ErroLimiteCredito as e:
            print(f"❌ Erro de limite: {e}")
            print(f"💡 Disponível no crédito: R$ {e.limite:.2f}")
            
        except ErroSistemaFinanceiro as e:
            print(f"❌ Erro financeiro: {e}")
            
        except ValueError as e:
            print(f"❌ Erro de valor: {e}")
    
    conta.extrato()

# Executar simulação
simular_operacoes_bancarias()</code></pre>
            </div>
            
            <h5>5. Context Managers e With Statement</h5>
            <p>Use context managers para garantir limpeza de recursos, mesmo quando exceções ocorrem.</p>
            
            <div class="code-example">
                <pre><code># Context manager para arquivos - automático
def processar_arquivo_seguro(nome_arquivo):
    """Usando with para garantir fechamento do arquivo"""
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            print(f"📖 Arquivo {nome_arquivo} aberto")
            conteudo = arquivo.read()
            
            # Arquivo é fechado automaticamente, mesmo se houver exceção
            if not conteudo.strip():
                raise ValueError("Arquivo está vazio")
            
            return len(conteudo.split('\n'))
            
    except FileNotFoundError:
        print(f"❌ Arquivo {nome_arquivo} não encontrado")
        return 0
    except ValueError as e:
        print(f"❌ Erro de conteúdo: {e}")
        return 0

# Context manager personalizado
class GerenciadorConexao:
    """Simula uma conexão que precisa ser fechada"""
    
    def __init__(self, servidor):
        self.servidor = servidor
        self.conectado = False
    
    def __enter__(self):
        """Método chamado ao entrar no bloco with"""
        print(f"🔌 Conectando ao servidor {self.servidor}")
        self.conectado = True
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Método chamado ao sair do bloco with (sempre executado)"""
        if self.conectado:
            print(f"🔌 Desconectando do servidor {self.servidor}")
            self.conectado = False
        
        # Se retornar True, suprime a exceção
        if exc_type:
            print(f"❌ Exceção capturada: {exc_type.__name__}: {exc_value}")
            return False  # Não suprimir exceção
    
    def enviar_dados(self, dados):
        """Simula envio de dados"""
        if not self.conectado:
            raise RuntimeError("Não conectado ao servidor")
        
        if not dados:
            raise ValueError("Dados não podem estar vazios")
        
        print(f"📤 Enviando: {dados}")

# Usando context manager personalizado
def exemplo_context_manager():
    """Demonstra uso de context manager personalizado"""
    
    try:
        with GerenciadorConexao("servidor-api.com") as conexao:
            conexao.enviar_dados("Dados importantes")
            conexao.enviar_dados("")  # Vai gerar erro
            
    except (RuntimeError, ValueError) as e:
        print(f"❌ Erro durante operação: {e}")
    
    print("✅ Context manager garantiu limpeza")

exemplo_context_manager()</code></pre>
            </div>
            
            <div class="alert alert-success">
                <h6>🎯 Melhores Práticas para Exceções:</h6>
                <ul class="mb-0">
                    <li><strong>Seja específico:</strong> Capture exceções específicas, não Exception genérica</li>
                    <li><strong>Falhe rápido:</strong> Valide entrada no início das funções</li>
                    <li><strong>Documente:</strong> Use docstrings para documentar exceções possíveis</li>
                    <li><strong>Log erros:</strong> Registre exceções para debugging futuro</li>
                    <li><strong>Recupere-se:</strong> Ofereça alternativas quando possível</li>
                </ul>
            </div>
            
            <div class="alert alert-warning">
                <h6>⚠️ Armadilhas Comuns:</h6>
                <ul class="mb-0">
                    <li>Nunca use <code>except:</code> sem especificar a exceção</li>
                    <li>Não ignore exceções silenciosamente (<code>pass</code>)</li>
                    <li>Cuidado com <code>except Exception</code> - muito genérico</li>
                    <li>Sempre feche recursos manualmente ou use context managers</li>
                </ul>
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
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual exceção ocorre ao tentar dividir por zero?',
                'options': ['ValueError', 'TypeError', 'ZeroDivisionError', 'ArithmeticError'],
                'correct_answer': 'ZeroDivisionError'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como capturar múltiplas exceções em um bloco except?',
                'options': ['except ValueError, TypeError:', 'except (ValueError, TypeError):', 'except ValueError and TypeError:', 'except ValueError or TypeError:'],
                'correct_answer': 'except (ValueError, TypeError):'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual a principal vantagem de usar "with" para abrir arquivos?',
                'options': ['É mais rápido', 'Garante fechamento automático', 'Permite múltiplos arquivos', 'Evita erros de sintaxe'],
                'correct_answer': 'Garante fechamento automático'
            }
        ]
    },
    8: {
        'title': 'Bibliotecas e APIs',
        'description': 'Expanda o poder do Python com bibliotecas externas e integração com APIs para criar aplicações modernas',
        'content': '''<div class="module-header">
            <h3>📚 Módulo 8 - Bibliotecas e APIs</h3>
            <p class="module-intro"><strong>Desbloqueie o poder infinito do Python!</strong> Descubra como usar milhares de bibliotecas externas e integrar com APIs para criar aplicações incríveis. Do básico ao avançado!</p>
        </div>
        
        <div class="module-content">
            <h4>🎯 O que você vai dominar:</h4>
            <ul class="learning-objectives">
                <li>Gerenciamento avançado de pacotes com pip</li>
                <li>Requisições HTTP profissionais com requests</li>
                <li>Consumo e criação de APIs REST</li>
                <li>Autenticação e tokens de API</li>
                <li>Processamento avançado de JSON</li>
                <li>Bibliotecas essenciais do ecossistema Python</li>
                <li>Web scraping ético e responsável</li>
                <li>Criação de clientes para APIs populares</li>
            </ul>
            
            <h4>📚 Conteúdo Teórico Completo:</h4>
            
            <h5>1. Ecossistema Python e Gerenciamento de Pacotes</h5>
            <p>O Python possui um dos maiores ecossistemas de bibliotecas do mundo, com mais de 400.000 pacotes no PyPI. Saber gerenciá-los é fundamental!</p>
            
            <div class="alert alert-info">
                <h6>🌟 Principais Repositórios:</h6>
                <ul class="mb-0">
                    <li><strong>PyPI:</strong> Python Package Index - repositório oficial</li>
                    <li><strong>Anaconda:</strong> Foco em ciência de dados</li>
                    <li><strong>GitHub:</strong> Desenvolvimento colaborativo</li>
                    <li><strong>pip:</strong> Gerenciador padrão de pacotes</li>
                </ul>
            </div>
            
            <div class="code-example">
                <h6>🔸 Gerenciamento Avançado com pip:</h6>
                <pre><code># Comandos essenciais do pip
# Instalar bibliotecas
pip install requests                    # Versão mais recente
pip install requests==2.28.1           # Versão específica
pip install requests>=2.25.0           # Versão mínima
pip install requests~=2.28.0           # Versão compatível

# Instalar múltiplas bibliotecas
pip install requests pandas numpy matplotlib

# Instalar de arquivo requirements.txt
pip install -r requirements.txt

# Gerar arquivo de dependências
pip freeze > requirements.txt

# Atualizar bibliotecas
pip install --upgrade requests         # Atualizar específica
pip list --outdated                   # Listar desatualizadas
pip install --upgrade pip             # Atualizar o próprio pip

# Informações sobre pacotes
pip show requests                      # Detalhes do pacote
pip list                              # Todos os pacotes instalados
pip check                             # Verificar dependências

# Desinstalar
pip uninstall requests
pip uninstall -r requirements.txt     # Desinstalar do arquivo

# Buscar pacotes
pip search machine-learning           # Buscar por termo (depreciado)

# Instalar de repositórios Git
pip install git+https://github.com/user/repo.git</code></pre>
                
                <h6>🔸 Ambiente Virtual (Melhor Prática):</h6>
                <pre><code># Criar ambiente virtual
python -m venv meu_projeto_env

# Ativar ambiente virtual
# Windows:
meu_projeto_env\Scripts\activate
# Linux/Mac:
source meu_projeto_env/bin/activate

# Instalar dependências no ambiente isolado
pip install requests pandas

# Desativar ambiente
deactivate

# Exemplo de estrutura de projeto profissional
meu_projeto/
├── requirements.txt          # Dependências
├── requirements-dev.txt      # Dependências de desenvolvimento
├── src/                      # Código fonte
├── tests/                    # Testes
├── docs/                     # Documentação
└── venv/                     # Ambiente virtual</code></pre>
            </div>
            
            <h5>2. Biblioteca Requests - HTTP para Humanos</h5>
            <p>A biblioteca requests é o padrão para fazer requisições HTTP em Python. Simples, elegante e poderosa!</p>
            
            <div class="code-example">
                <pre><code>import requests
import json
from datetime import datetime

# GET - Buscar dados
def exemplo_get_basico():
    """Requisição GET básica"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        response = requests.get(url)
        
        # Verificar se a requisição foi bem-sucedida
        response.raise_for_status()  # Lança exceção para códigos 4xx/5xx
        
        # Acessar dados JSON
        data = response.json()
        print(f"📄 Post ID: {data['id']}")
        print(f"📝 Título: {data['title']}")
        print(f"✍️ Autor: Usuário {data['userId']}")
        
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
        return None

# GET com parâmetros
def buscar_posts_por_usuario(user_id):
    """Busca posts de um usuário específico"""
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Parâmetros da URL
    params = {
        'userId': user_id,
        '_limit': 5  # Limitar resultados
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        posts = response.json()
        print(f"📊 Encontrados {len(posts)} posts do usuário {user_id}")
        
        for post in posts:
            print(f"  📌 [{post['id']}] {post['title'][:50]}...")
            
        return posts
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro: {e}")
        return []

# POST - Criar dados
def criar_post(titulo, conteudo, user_id):
    """Cria um novo post"""
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Dados para enviar
    data = {
        'title': titulo,
        'body': conteudo,
        'userId': user_id
    }
    
    # Headers para JSON
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'MeuApp/1.0'
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        
        novo_post = response.json()
        print(f"✅ Post criado com ID: {novo_post['id']}")
        return novo_post
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao criar post: {e}")
        return None

# PUT - Atualizar dados
def atualizar_post(post_id, titulo, conteudo):
    """Atualiza um post existente"""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    data = {
        'id': post_id,
        'title': titulo,
        'body': conteudo,
        'userId': 1
    }
    
    try:
        response = requests.put(url, json=data)
        response.raise_for_status()
        
        post_atualizado = response.json()
        print(f"✅ Post {post_id} atualizado com sucesso")
        return post_atualizado
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao atualizar: {e}")
        return None

# DELETE - Remover dados
def deletar_post(post_id):
    """Remove um post"""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    try:
        response = requests.delete(url)
        response.raise_for_status()
        
        print(f"✅ Post {post_id} removido com sucesso")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao deletar: {e}")
        return False

# Sessões - Reutilizar conexões
def exemplo_sessao():
    """Usando sessões para múltiplas requisições"""
    
    with requests.Session() as session:
        # Configurar headers padrão para toda a sessão
        session.headers.update({
            'User-Agent': 'MeuApp/1.0',
            'Accept': 'application/json'
        })
        
        # Múltiplas requisições reutilizando a conexão
        urls = [
            "https://jsonplaceholder.typicode.com/posts/1",
            "https://jsonplaceholder.typicode.com/posts/2",
            "https://jsonplaceholder.typicode.com/posts/3"
        ]
        
        results = []
        for url in urls:
            try:
                response = session.get(url, timeout=5)
                response.raise_for_status()
                results.append(response.json())
                print(f"✅ Dados obtidos de {url}")
            except requests.exceptions.RequestException as e:
                print(f"❌ Erro em {url}: {e}")
        
        return results

# Testando as funções
print("=== Testando Requests ===")
exemplo_get_basico()
buscar_posts_por_usuario(1)
criar_post("Meu Post Python", "Conteúdo incrível sobre Python!", 1)</code></pre>
            </div>
            
            <h5>3. Trabalhando com APIs Reais</h5>
            <p>Vamos integrar com APIs populares para criar aplicações úteis e práticas!</p>
            
            <div class="code-example">
                <pre><code>import requests
import os
from datetime import datetime

class ViaCEPClient:
    """Cliente para API ViaCEP - busca informações de CEP"""
    
    BASE_URL = "https://viacep.com.br/ws"
    
    def buscar_cep(self, cep):
        """Busca informações de um CEP"""
        # Limpar CEP (remover caracteres especiais)
        cep_limpo = ''.join(filter(str.isdigit, cep))
        
        if len(cep_limpo) != 8:
            raise ValueError("CEP deve ter 8 dígitos")
        
        url = f"{self.BASE_URL}/{cep_limpo}/json/"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Verificar se CEP foi encontrado
            if 'erro' in data:
                raise ValueError(f"CEP {cep} não encontrado")
            
            return {
                'cep': data['cep'],
                'logradouro': data['logradouro'],
                'bairro': data['bairro'],
                'cidade': data['localidade'],
                'uf': data['uf'],
                'ddd': data['ddd']
            }
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao consultar CEP: {e}")

class GitHubClient:
    """Cliente para API do GitHub"""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token=None):
        self.session = requests.Session()
        
        # Headers padrão
        self.session.headers.update({
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'PythonApp/1.0'
        })
        
        # Autenticação opcional
        if token:
            self.session.headers['Authorization'] = f'token {token}'
    
    def buscar_usuario(self, username):
        """Busca informações de um usuário"""
        url = f"{self.BASE_URL}/users/{username}"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            
            user = response.json()
            
            return {
                'nome': user['name'],
                'username': user['login'],
                'bio': user['bio'],
                'repositorios_publicos': user['public_repos'],
                'seguidores': user['followers'],
                'seguindo': user['following'],
                'criado_em': user['created_at'],
                'avatar': user['avatar_url']
            }
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao buscar usuário: {e}")
    
    def listar_repositorios(self, username, limit=10):
        """Lista repositórios de um usuário"""
        url = f"{self.BASE_URL}/users/{username}/repos"
        
        params = {
            'sort': 'updated',
            'direction': 'desc',
            'per_page': limit
        }
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            
            repos = response.json()
            
            repositorios = []
            for repo in repos:
                repositorios.append({
                    'nome': repo['name'],
                    'descricao': repo['description'],
                    'linguagem': repo['language'],
                    'estrelas': repo['stargazers_count'],
                    'forks': repo['forks_count'],
                    'url': repo['html_url'],
                    'atualizado_em': repo['updated_at']
                })
            
            return repositorios
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao listar repositórios: {e}")

class OpenWeatherClient:
    """Cliente para API OpenWeatherMap"""
    
    BASE_URL = "https://api.openweathermap.org/data/2.5"
    
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key é obrigatória")
        self.api_key = api_key
    
    def clima_atual(self, cidade):
        """Busca clima atual de uma cidade"""
        url = f"{self.BASE_URL}/weather"
        
        params = {
            'q': cidade,
            'appid': self.api_key,
            'units': 'metric',  # Celsius
            'lang': 'pt_br'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                'cidade': data['name'],
                'pais': data['sys']['country'],
                'temperatura': data['main']['temp'],
                'sensacao_termica': data['main']['feels_like'],
                'humidade': data['main']['humidity'],
                'pressao': data['main']['pressure'],
                'descricao': data['weather'][0]['description'],
                'nuvens': data['clouds']['all'],
                'vento_velocidade': data['wind']['speed'],
                'visibilidade': data.get('visibility', 'N/A')
            }
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao buscar clima: {e}")

# Exemplo de uso prático
def demonstrar_apis():
    """Demonstra uso de múltiplas APIs"""
    
    print("=== Consultando CEP ===")
    via_cep = ViaCEPClient()
    try:
        endereco = via_cep.buscar_cep("01310-100")
        print(f"📍 {endereco['logradouro']}, {endereco['bairro']}")
        print(f"🏙️ {endereco['cidade']}/{endereco['uf']} - CEP: {endereco['cep']}")
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    print("\n=== Consultando GitHub ===")
    github = GitHubClient()
    try:
        usuario = github.buscar_usuario("octocat")
        print(f"👤 {usuario['nome']} (@{usuario['username']})")
        print(f"📊 {usuario['repositorios_publicos']} repos públicos")
        print(f"👥 {usuario['seguidores']} seguidores")
        
        repos = github.listar_repositorios("octocat", 3)
        print(f"\n🗂️ Repositórios recentes:")
        for repo in repos:
            print(f"  ⭐ {repo['nome']} ({repo['estrelas']} estrelas) - {repo['linguagem']}")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

demonstrar_apis()</code></pre>
            </div>
            
            <h5>4. Bibliotecas Essenciais do Ecossistema Python</h5>
            <p>Conheça as bibliotecas mais importantes para diferentes domínios de aplicação.</p>
            
            <div class="code-example">
                <pre><code># Principais categorias de bibliotecas Python

# 📊 CIÊNCIA DE DADOS
"""
pandas - Manipulação de dados tabulares
numpy - Computação numérica
matplotlib - Gráficos e visualizações
seaborn - Visualizações estatísticas
scipy - Algoritmos científicos
scikit-learn - Machine learning
"""

# 🌐 WEB DEVELOPMENT
"""
flask - Framework web minimalista
django - Framework web completo
fastapi - APIs modernas e rápidas
requests - Cliente HTTP
beautifulsoup4 - Web scraping
scrapy - Framework de scraping
"""

# 🗄️ BANCO DE DADOS
"""
sqlalchemy - ORM para SQL
pymongo - Cliente MongoDB
redis - Cliente Redis
psycopg2 - Cliente PostgreSQL
"""

# 🔧 UTILIDADES GERAIS
"""
python-dateutil - Manipulação de datas
pillow - Processamento de imagens
openpyxl - Manipulação de Excel
python-dotenv - Variáveis de ambiente
click - Interfaces de linha de comando
"""

# Exemplo prático: Manipulação de dados com pandas
import pandas as pd
import requests

def exemplo_pandas_com_api():
    """Combina API com análise de dados usando pandas"""
    
    # Buscar dados de uma API
    print("📥 Buscando dados da API...")
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Converter JSON para DataFrame
        users_data = response.json()
        df = pd.DataFrame(users_data)
        
        print(f"📊 Dados carregados: {len(df)} usuários")
        print(f"📋 Colunas: {list(df.columns)}")
        
        # Análises básicas
        print("\n=== Análise dos Dados ===")
        print(f"🌐 Websites únicos: {df['website'].nunique()}")
        print(f"🏢 Empresas únicas: {df['company'].apply(lambda x: x['name']).nunique()}")
        
        # Extrair informações aninhadas
        df['empresa_nome'] = df['company'].apply(lambda x: x['name'])
        df['cidade'] = df['address'].apply(lambda x: x['city'])
        
        # Agrupar por cidade
        usuarios_por_cidade = df.groupby('cidade').size()
        print(f"\n🏙️ Usuários por cidade:")
        for cidade, count in usuarios_por_cidade.items():
            print(f"  {cidade}: {count} usuários")
        
        # Salvar dados processados
        df[['name', 'email', 'empresa_nome', 'cidade']].to_csv('usuarios.csv', index=False)
        print(f"\n💾 Dados salvos em 'usuarios.csv'")
        
        return df
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na API: {e}")
        return None
    except Exception as e:
        print(f"❌ Erro no processamento: {e}")
        return None

# Exemplo: Web scraping ético com BeautifulSoup
from bs4 import BeautifulSoup
import time

def exemplo_web_scraping():
    """Exemplo de web scraping responsável"""
    
    # URL de exemplo (sempre verificar robots.txt!)
    url = "https://quotes.toscrape.com/"
    
    try:
        # Headers para parecer um navegador real
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parsear HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontrar citações
        quotes = soup.find_all('div', class_='quote')
        
        print(f"📜 Encontradas {len(quotes)} citações:")
        
        citacoes_data = []
        for quote in quotes[:5]:  # Primeiras 5
            texto = quote.find('span', class_='text').text
            autor = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            
            citacoes_data.append({
                'texto': texto,
                'autor': autor,
                'tags': ', '.join(tags)
            })
            
            print(f"\n💭 \"{texto}\"")
            print(f"✍️ — {autor}")
            print(f"🏷️ Tags: {', '.join(tags)}")
        
        # Converter para DataFrame
        df_quotes = pd.DataFrame(citacoes_data)
        df_quotes.to_json('citacoes.json', orient='records', indent=2)
        print(f"\n💾 Citações salvas em 'citacoes.json'")
        
        return citacoes_data
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro no scraping: {e}")
        return None

# Executar exemplos (comentado para não causar erro se dependências não estiverem instaladas)
# exemplo_pandas_com_api()
# exemplo_web_scraping()</code></pre>
            </div>
            
            <div class="alert alert-success">
                <h6>🎯 Melhores Práticas para APIs:</h6>
                <ul class="mb-0">
                    <li><strong>Rate Limiting:</strong> Respeite limites de requisições</li>
                    <li><strong>Timeouts:</strong> Sempre defina timeouts para evitar travamentos</li>
                    <li><strong>Tratamento de Erros:</strong> Capture e trate exceções adequadamente</li>
                    <li><strong>Autenticação:</strong> Mantenha tokens seguros e nunca no código</li>
                    <li><strong>Cache:</strong> Cache respostas quando apropriado</li>
                </ul>
            </div>
            
            <div class="alert alert-warning">
                <h6>⚠️ Considerações Éticas:</h6>
                <ul class="mb-0">
                    <li>Sempre leia e respeite o robots.txt</li>
                    <li>Não sobrecarregue servidores com muitas requisições</li>
                    <li>Use delays entre requisições em web scraping</li>
                    <li>Respeite termos de uso das APIs</li>
                    <li>Considere custos de APIs pagas</li>
                </ul>
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
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual método verifica se uma requisição HTTP foi bem-sucedida?',
                'options': ['response.check()', 'response.raise_for_status()', 'response.validate()', 'response.verify()'],
                'correct_answer': 'response.raise_for_status()'
            },
            {
                'type': 'multiple_choice',
                'question': 'Como converter resposta JSON em dicionário Python?',
                'options': ['response.to_dict()', 'response.json()', 'json.loads(response)', 'response.parse()'],
                'correct_answer': 'response.json()'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual header é importante para enviar dados JSON?',
                'options': ['Content-Type: application/json', 'Data-Type: json', 'Format: json', 'Type: application/json'],
                'correct_answer': 'Content-Type: application/json'
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