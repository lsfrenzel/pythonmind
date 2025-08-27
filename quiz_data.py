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
        <div class="module-header">
            <h3>Módulo 1 - Fundamentos do Python</h3>
            <p class="module-intro"><strong>Bem-vindo ao mundo da programação Python!</strong> Neste módulo, você descobrirá os conceitos fundamentais que formam a base de toda programação em Python.</p>
        </div>
        
        <div class="content-section">
            <h4>1. Variáveis e Tipos de Dados</h4>
            <p>Python é uma linguagem dinamicamente tipada, o que significa que você não precisa declarar o tipo de uma variável explicitamente. O Python determina automaticamente o tipo baseado no valor atribuído.</p>
            
            <div class="code-example">
                <h5>Tipos Numéricos:</h5>
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
print(type(idade))        # <class 'int'>
print(type(altura))       # <class 'float'>
print(type(numero_complexo))  # <class 'complex'></code></pre>
            </div>
            
            <div class="code-example">
                <h5>Strings (Texto):</h5>
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
                <h5>Booleanos:</h5>
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
            <h4>2. Estruturas de Dados</h4>
            
            <div class="code-example">
                <h5>Listas - Coleções Ordenadas e Mutáveis:</h5>
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
                <h5>Dicionários - Coleções de Chave-Valor:</h5>
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
        </div>
        
        <div class="content-section">
            <h4>3. Operadores e Expressões</h4>
            
            <div class="code-example">
                <h5>Operadores Aritméticos:</h5>
                <pre><code># Operações básicas
a = 15
b = 4

print(f"Soma: {a} + {b} = {a + b}")           # 19
print(f"Subtração: {a} - {b} = {a - b}")     # 11
print(f"Multiplicação: {a} * {b} = {a * b}") # 60
print(f"Divisão: {a} / {b} = {a / b}")       # 3.75
print(f"Divisão inteira: {a} // {b} = {a // b}") # 3
print(f"Resto: {a} % {b} = {a % b}")          # 3
print(f"Potência: {a} ** {b} = {a ** b}")    # 50625

# Operadores de atribuição
x = 10
x += 5   # x = x + 5, agora x = 15
x *= 2   # x = x * 2, agora x = 30
x //= 3  # x = x // 3, agora x = 10
print(f"Valor final de x: {x}")</code></pre>
            </div>
            
            <div class="code-example">
                <h5>Operadores de Comparação:</h5>
                <pre><code># Comparações numéricas
nota1 = 8.5
nota2 = 7.0

print(f"{nota1} > {nota2}: {nota1 > nota2}")    # True
print(f"{nota1} == {nota2}: {nota1 == nota2}")  # False
print(f"{nota1} != {nota2}: {nota1 != nota2}")  # True
print(f"{nota1} >= 8.0: {nota1 >= 8.0}")        # True

# Comparações com strings
nome1 = "Ana"
nome2 = "Bruno"
print(f"'{nome1}' < '{nome2}': {nome1 < nome2}")  # True (ordem alfabética)</code></pre>
            </div>
        </div>
        
        <div class="content-section">
            <h4>4. Entrada e Saída de Dados</h4>
            
            <div class="code-example">
                <h5>Função input() - Recebendo Dados do Usuário:</h5>
                <pre><code># Entrada básica (sempre retorna string)
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# Convertendo tipos
try:
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura (em metros): "))
    
    print(f"Você tem {idade} anos e {altura}m de altura")
    
    # Calculando IMC
    peso = float(input("Digite seu peso (em kg): "))
    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")
    
except ValueError:
    print("Por favor, digite apenas números válidos!")

# Entrada com validação
while True:
    resposta = input("Deseja continuar? (s/n): ").lower()
    if resposta in ['s', 'sim', 'n', 'não']:
        break
    print("Por favor, responda com 's' ou 'n'")</code></pre>
            </div>
            
            <div class="code-example">
                <h5>Função print() - Exibindo Dados:</h5>
                <pre><code># Print básico
print("Hello, World!")

# Print com múltiplos valores
nome = "João"
idade = 25
print("Nome:", nome, "| Idade:", idade)

# Formatação com f-strings (recomendado)
print(f"Meu nome é {nome} e tenho {idade} anos")

# Controle de separador e fim de linha
print("Python", "é", "incrível", sep="-")  # Python-é-incrível
print("Primeira linha", end=" ")
print("mesma linha")  # Primeira linha mesma linha

# Formatação de números
preco = 1234.56789
print(f"Preço: R$ {preco:.2f}")      # R$ 1234.57
print(f"Inteiro: {preco:.0f}")       # 1235
print(f"Científico: {preco:.2e}")    # 1.23e+03

# Formatação de strings
texto = "python"
print(f"Maiúsculo: {texto.upper()}")
print(f"Centralizado: '{texto:^20}'")  # Centraliza em 20 caracteres
print(f"Alinhado à direita: '{texto:>15}'")</code></pre>
            </div>
        </div>
        
        <div class="content-section">
            <h4>5. Exercício Prático Completo</h4>
            <div class="code-example">
                <h5>Sistema de Cadastro Simples:</h5>
                <pre><code># Sistema de cadastro de estudante
print("=== SISTEMA DE CADASTRO DE ESTUDANTE ===")

# Coletando informações
nome = input("Nome completo: ")
idade = int(input("Idade: "))
curso = input("Curso: ")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))

# Processando dados
media = (nota1 + nota2 + nota3) / 3
situacao = "Aprovado" if media >= 7.0 else "Reprovado"

# Criando perfil do estudante
estudante = {
    "nome": nome,
    "idade": idade,
    "curso": curso,
    "notas": [nota1, nota2, nota3],
    "media": media,
    "situacao": situacao
}

# Exibindo resultado
print("\n" + "="*50)
print("PERFIL DO ESTUDANTE")
print("="*50)
print(f"Nome: {estudante['nome']}")
print(f"Idade: {estudante['idade']} anos")
print(f"Curso: {estudante['curso']}")
print(f"Notas: {estudante['notas']}")
print(f"Média: {estudante['media']:.2f}")
print(f"Situação: {estudante['situacao']}")

# Feedback adicional
if media >= 9.0:
    print("Parabéns! Excelente desempenho!")
elif media >= 7.0:
    print("Bom trabalho! Você foi aprovado.")
else:
    print("Precisa estudar mais. Tente novamente!")
    
print("="*50)</code></pre>
            </div>
        </div>
        
        <div class="tips-section">
            <h4>Dicas Importantes</h4>
            <ul class="tips-list">
                <li><strong>Convenções de nomenclatura:</strong> Use snake_case para variáveis (ex: nome_completo)</li>
                <li><strong>Comentários:</strong> Use # para comentários de linha única e """ """ para múltiplas linhas</li>
                <li><strong>Indentação:</strong> Python usa indentação (4 espaços) para estruturar o código</li>
                <li><strong>Case-sensitive:</strong> Python distingue maiúsculas de minúsculas (Nome ≠ nome)</li>
                <li><strong>Palavras reservadas:</strong> Evite usar palavras como if, for, class como nomes de variáveis</li>
            </ul>
        </div>
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
        'content': '''
        <div class="module-header">
            <h3>Módulo 2 - Estruturas de Controle</h3>
            <p class="module-intro"><strong>Domine o fluxo do seu programa!</strong> As estruturas de controle são fundamentais para criar programas dinâmicos e interativos. Aqui você aprenderá a tomar decisões e repetir ações de forma inteligente.</p>
        </div>

        <div class="content-section">
            <h4>1. Estruturas Condicionais - Tomando Decisões</h4>
            <p>As estruturas condicionais permitem que seu programa execute diferentes códigos baseado em condições específicas.</p>
            
            <div class="code-example">
                <h5>IF Simples:</h5>
                <pre><code># Estrutura básica
idade = 20
if idade >= 18:
    print("Você é maior de idade!")
    print("Pode tirar CNH")

# Exemplo prático: Sistema de acesso
usuario_ativo = True
if usuario_ativo:
    print("Bem-vindo ao sistema!")
    print("Acesso liberado")

# Condições com operadores lógicos
temperatura = 25
chuva = False

if temperatura > 20 and not chuva:
    print("Ótimo dia para um passeio!")
    
# Verificando membership
frutas_disponiveis = ["maçã", "banana", "laranja"]
fruta_escolhida = "maçã"

if fruta_escolhida in frutas_disponiveis:
    print(f"Temos {fruta_escolhida} disponível!")</code></pre>
            </div>

            <div class="code-example">
                <h5>IF-ELSE - Duas Alternativas:</h5>
                <pre><code># Exemplo básico
idade = 16
if idade >= 18:
    print("Pode votar!")
    status = "eleitor"
else:
    print("Ainda não pode votar")
    status = "menor de idade"

print(f"Status: {status}")

# Exemplo prático: Calculadora de desconto
valor_compra = 150.00
if valor_compra >= 100:
    desconto = valor_compra * 0.1  # 10% de desconto
    valor_final = valor_compra - desconto
    print(f"Parabéns! Você ganhou R$ {desconto:.2f} de desconto!")
else:
    valor_final = valor_compra
    print("Compre mais R$ {:.2f} para ganhar desconto!".format(100 - valor_compra))

print(f"Valor final: R$ {valor_final:.2f}")

# Sistema de login
usuario = "admin"
senha = "123456"

if usuario == "admin" and senha == "123456":
    print("Login realizado com sucesso!")
    acesso_liberado = True
else:
    print("Usuário ou senha incorretos!")
    acesso_liberado = False</code></pre>
            </div>

            <div class="code-example">
                <h5>IF-ELIF-ELSE - Múltiplas Condições:</h5>
                <pre><code># Sistema de notas
nota = 8.7

if nota >= 9.0:
    conceito = "A"
    mensagem = "Excelente trabalho!"
elif nota >= 8.0:
    conceito = "B"
    mensagem = "Muito bom!"
elif nota >= 7.0:
    conceito = "C"
    mensagem = "Bom trabalho!"
elif nota >= 6.0:
    conceito = "D"
    mensagem = "Precisa melhorar"
else:
    conceito = "F"
    mensagem = "Reprovado"

print(f"Nota: {nota} | Conceito: {conceito}")
print(mensagem)

# Sistema de faixas de IMC
peso = 70
altura = 1.75
imc = peso / (altura ** 2)

print(f"Seu IMC: {imc:.1f}")

if imc < 18.5:
    categoria = "Abaixo do peso"
    recomendacao = "Consulte um nutricionista"
elif imc < 25:
    categoria = "Peso normal"
    recomendacao = "Continue mantendo hábitos saudáveis!"
elif imc < 30:
    categoria = "Sobrepeso"
    recomendacao = "Considere uma dieta equilibrada"
elif imc < 35:
    categoria = "Obesidade grau I"
    recomendacao = "Procure orientação médica"
else:
    categoria = "Obesidade grau II ou III"
    recomendacao = "Procure um médico urgentemente"

print(f"Categoria: {categoria}")
print(f"Recomendação: {recomendacao}")

# Classificação de idade
idade = 25

if idade < 13:
    faixa_etaria = "Criança"
    atividades = ["brincar", "estudar", "desenhar"]
elif idade < 18:
    faixa_etaria = "Adolescente"
    atividades = ["estudar", "esportes", "socializar"]
elif idade < 60:
    faixa_etaria = "Adulto"
    atividades = ["trabalhar", "família", "hobbies"]
else:
    faixa_etaria = "Idoso"
    atividades = ["relaxar", "família", "viagens"]

print(f"Faixa etária: {faixa_etaria}")
print(f"Atividades recomendadas: {', '.join(atividades)}")</code></pre>
            </div>
        </div>

        <div class="content-section">
            <h4>2. Loops FOR - Repetição Controlada</h4>
            <p>O loop FOR é usado quando você sabe quantas vezes quer repetir uma ação ou quando quer iterar sobre uma coleção de dados.</p>

            <div class="code-example">
                <h5>FOR com range():</h5>
                <pre><code># Range básico - de 0 até n-1
print("Contagem de 0 a 4:")
for i in range(5):
    print(f"Número: {i}")

# Range com início e fim
print("\nContagem de 1 a 10:")
for numero in range(1, 11):
    print(f"Número: {numero}")

# Range com passo
print("\nNúmeros pares de 0 a 20:")
for par in range(0, 21, 2):
    print(par, end=" ")
print()

# Range decrescente
print("\nContagem regressiva:")
for i in range(10, 0, -1):
    print(f"{i}...", end=" ")
print("ZERO!")

# Exemplo prático: Tabuada
numero = 7
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Calculando fatorial
n = 5
fatorial = 1
print(f"\nCalculando {n}!:")
for i in range(1, n + 1):
    fatorial *= i
    print(f"Passo {i}: {fatorial}")
print(f"Resultado: {n}! = {fatorial}")</code></pre>
            </div>

            <div class="code-example">
                <h5>FOR com Listas e Strings:</h5>
                <pre><code># Iterando sobre lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "manga"]
print("Frutas disponíveis:")
for fruta in frutas:
    print(f"- {fruta.title()}")

# Usando enumerate para ter índice
print("\nFrutas numeradas:")
for indice, fruta in enumerate(frutas, 1):
    print(f"{indice}. {fruta}")

# Iterando sobre string
palavra = "Python"
print(f"\nLetras da palavra '{palavra}':")
for letra in palavra:
    print(f"Letra: {letra}")

# Exemplo prático: Análise de vendas
vendas_mensais = [1200, 1500, 1100, 1800, 1400, 1600]
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

total_vendas = 0
melhor_mes = ""
maior_venda = 0

print("Relatório de Vendas:")
for mes, venda in zip(meses, vendas_mensais):
    total_vendas += venda
    print(f"{mes}: R$ {venda:.2f}")
    
    if venda > maior_venda:
        maior_venda = venda
        melhor_mes = mes

print(f"\nTotal de vendas: R$ {total_vendas:.2f}")
print(f"Média mensal: R$ {total_vendas/len(vendas_mensais):.2f}")
print(f"Melhor mês: {melhor_mes} (R$ {maior_venda:.2f})")

# Processando lista de números
numeros = [15, 23, 8, 42, 7, 31, 19]
pares = []
impares = []
maiores_que_20 = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    
    if numero > 20:
        maiores_que_20.append(numero)

print(f"\nNúmeros originais: {numeros}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
print(f"Maiores que 20: {maiores_que_20}")</code></pre>
            </div>
        </div>

        <div class="content-section">
            <h4>3. Loops WHILE - Repetição com Condição</h4>
            <p>O loop WHILE executa enquanto uma condição for verdadeira. É útil quando você não sabe exatamente quantas vezes precisará repetir.</p>

            <div class="code-example">
                <h5>WHILE Básico:</h5>
                <pre><code># Contador simples
contador = 0
print("Contagem com while:")
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Importante: incrementar para evitar loop infinito!

print("Loop finalizado!")

# Exemplo: Acumulador
soma = 0
numero = 1
print("\nSomando números de 1 a 100:")
while numero <= 100:
    soma += numero
    numero += 1

print(f"Soma: {soma}")

# Validação de entrada
print("\n=== Sistema de Login ===")
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = input("Digite a senha: ")
    
    if senha == "python123":
        print("Login realizado com sucesso!")
        break
    else:
        tentativas += 1
        restantes = max_tentativas - tentativas
        if restantes > 0:
            print(f"Senha incorreta! Restam {restantes} tentativas.")
        else:
            print("Número máximo de tentativas excedido!")
            print("Conta bloqueada!")

# Jogo de adivinhação
import random

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("\n=== JOGO DE ADIVINHAÇÃO ===")
print("Estou pensando em um número entre 1 e 100...")

while not acertou:
    try:
        palpite = int(input("Seu palpite: "))
        tentativas += 1
        
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas!")
            acertou = True
        elif palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        else:
            print("Muito alto! Tente um número menor.")
            
        if tentativas >= 10 and not acertou:
            print(f"Que pena! O número era {numero_secreto}")
            break
            
    except ValueError:
        print("Digite apenas números!")</code></pre>
            </div>
        </div>

        <div class="content-section">
            <h4>4. Controle de Fluxo: BREAK e CONTINUE</h4>
            
            <div class="code-example">
                <h5>BREAK - Interrompendo Loops:</h5>
                <pre><code># Break em FOR
print("Procurando número par maior que 15:")
numeros = [3, 7, 12, 18, 21, 25, 30]

for numero in numeros:
    print(f"Verificando: {numero}")
    if numero > 15 and numero % 2 == 0:
        print(f"Encontrado: {numero}")
        break
else:
    print("Nenhum número encontrado")

# Break em WHILE - Menu de programa
print("\n=== CALCULADORA SIMPLES ===")
while True:
    print("\n1. Somar")
    print("2. Subtrair") 
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "5":
        print("Saindo do programa...")
        break
    
    if opcao in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))
            
            if opcao == "1":
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcao == "2":
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcao == "3":
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif opcao == "4":
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
                else:
                    print("Erro: Divisão por zero!")
        except ValueError:
            print("Erro: Digite apenas números!")
    else:
        print("Opção inválida!")</code></pre>
            </div>

            <div class="code-example">
                <h5>CONTINUE - Pulando Iterações:</h5>
                <pre><code># Continue em FOR
print("Números ímpares de 1 a 20:")
for numero in range(1, 21):
    if numero % 2 == 0:  # Se for par, pula
        continue
    print(numero, end=" ")
print()

# Processando lista com continue
notas = [8.5, 3.2, 9.1, 6.7, 4.8, 10.0, 2.1, 7.5]
print("\nNotas acima da média (7.0):")

for i, nota in enumerate(notas, 1):
    if nota < 7.0:
        continue  # Pula notas baixas
    print(f"Aluno {i}: {nota}")

# Exemplo prático: Processamento de pedidos
pedidos = [
    {"id": 1, "status": "pendente", "valor": 150.00},
    {"id": 2, "status": "cancelado", "valor": 200.00},
    {"id": 3, "status": "pendente", "valor": 75.00},
    {"id": 4, "status": "enviado", "valor": 300.00},
    {"id": 5, "status": "pendente", "valor": 120.00}
]

print("\n=== PROCESSANDO PEDIDOS PENDENTES ===")
total_pendentes = 0
quantidade_pendentes = 0

for pedido in pedidos:
    if pedido["status"] != "pendente":
        continue  # Pula pedidos que não estão pendentes
    
    print(f"Processando pedido {pedido['id']}: R$ {pedido['valor']:.2f}")
    total_pendentes += pedido["valor"]
    quantidade_pendentes += 1

print(f"\nTotal de {quantidade_pendentes} pedidos pendentes")
print(f"Valor total: R$ {total_pendentes:.2f}")

# Validação de dados com continue
dados_usuarios = [
    {"nome": "João", "email": "joao@email.com", "idade": 25},
    {"nome": "", "email": "maria@email.com", "idade": 30},
    {"nome": "Pedro", "email": "", "idade": 28},
    {"nome": "Ana", "email": "ana@email.com", "idade": -5},
    {"nome": "Carlos", "email": "carlos@email.com", "idade": 35}
]

print("\n=== VALIDANDO USUÁRIOS ===")
usuarios_validos = []

for usuario in dados_usuarios:
    # Verificações de validação
    if not usuario["nome"]:
        print(f"Usuário ignorado: nome vazio")
        continue
    
    if not usuario["email"] or "@" not in usuario["email"]:
        print(f"Usuário {usuario['nome']} ignorado: email inválido")
        continue
    
    if usuario["idade"] < 0 or usuario["idade"] > 120:
        print(f"Usuário {usuario['nome']} ignorado: idade inválida")
        continue
    
    # Se chegou aqui, o usuário é válido
    usuarios_validos.append(usuario)
    print(f"Usuário {usuario['nome']} validado com sucesso!")

print(f"\nTotal de usuários válidos: {len(usuarios_validos)}")</code></pre>
            </div>
        </div>

        <div class="content-section">
            <h4>5. Loops Aninhados e Padrões</h4>
            <div class="code-example">
                <h5>Criando Padrões com Loops Aninhados:</h5>
                <pre><code># Padrão de estrelas
print("Triângulo de estrelas:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # Nova linha

# Tabuada completa
print("\nTabuada completa (1 a 10):")
for i in range(1, 11):
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j:2d}")

# Matriz de números
print("\nMatriz 5x5:")
for linha in range(5):
    for coluna in range(5):
        numero = linha * 5 + coluna + 1
        print(f"{numero:2d}", end=" ")
    print()

# Processando dados bidimensionais
vendas_trimestrais = [
    [1200, 1300, 1100],  # Q1
    [1400, 1500, 1300],  # Q2
    [1600, 1700, 1500],  # Q3
    [1800, 1900, 1700]   # Q4
]

trimestres = ["Q1", "Q2", "Q3", "Q4"]
meses_por_trimestre = ["Mês 1", "Mês 2", "Mês 3"]

print("\n=== RELATÓRIO ANUAL DE VENDAS ===")
total_anual = 0

for i, vendas_trim in enumerate(vendas_trimestrais):
    print(f"\n{trimestres[i]}:")
    total_trimestre = 0
    
    for j, venda_mensal in enumerate(vendas_trim):
        print(f"  {meses_por_trimestre[j]}: R$ {venda_mensal:.2f}")
        total_trimestre += venda_mensal
        total_anual += venda_mensal
    
    media_trimestre = total_trimestre / 3
    print(f"  Total {trimestres[i]}: R$ {total_trimestre:.2f}")
    print(f"  Média {trimestres[i]}: R$ {media_trimestre:.2f}")

print(f"\nTOTAL ANUAL: R$ {total_anual:.2f}")
print(f"MÉDIA MENSAL: R$ {total_anual/12:.2f}")</code></pre>
            </div>
        </div>

        <div class="tips-section">
            <h4>Dicas Importantes sobre Estruturas de Controle</h4>
            <ul class="tips-list">
                <li><strong>Indentação:</strong> Python usa 4 espaços para delimitar blocos de código</li>
                <li><strong>Comparações:</strong> Use == para igualdade e != para diferença</li>
                <li><strong>Operadores lógicos:</strong> and, or, not (ao invés de &&, ||, !)</li>
                <li><strong>Loop infinito:</strong> Sempre certifique-se de que a condição do while pode se tornar False</li>
                <li><strong>Break vs Continue:</strong> break sai do loop, continue pula para próxima iteração</li>
                <li><strong>Else em loops:</strong> O bloco else executa se o loop completar normalmente (sem break)</li>
            </ul>
        </div>
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
            },
            {
                'type': 'multiple_choice',
                'question': 'O que faz o comando "break" em um loop?',
                'options': [
                    'Pula para a próxima iteração',
                    'Interrompe o loop completamente',
                    'Reinicia o loop do início',
                    'Pausa o loop temporariamente',
                    'Não faz nada'
                ],
                'correct_answer': 'Interrompe o loop completamente'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual a diferença entre range(5) e range(1, 6)?',
                'options': [
                    'Não há diferença, ambos geram os mesmos números',
                    'range(5) gera 0-4, range(1,6) gera 1-5',
                    'range(5) gera 1-5, range(1,6) gera 0-4',
                    'range(5) é inválido',
                    'range(1,6) é inválido'
                ],
                'correct_answer': 'range(5) gera 0-4, range(1,6) gera 1-5'
            },
            {
                'type': 'multiple_choice',
                'question': 'Em qual situação você deveria usar WHILE ao invés de FOR?',
                'options': [
                    'Quando sabe exatamente quantas iterações precisa',
                    'Quando quer iterar sobre uma lista',
                    'Quando não sabe quantas iterações serão necessárias',
                    'Quando quer usar break ou continue',
                    'WHILE e FOR são sempre intercambiáveis'
                ],
                'correct_answer': 'Quando não sabe quantas iterações serão necessárias'
            }
        ]
    },
    3: {
        'title': 'Manipulação de Arquivos e Dados',
        'description': 'Trabalhando com diferentes formatos de arquivo e dados.',
        'video_url': '',
        'content': '''
        <div class="module-header">
            <h3>Módulo 3 - Manipulação de Arquivos e Dados</h3>
            <p class="module-intro"><strong>Desbrave o mundo dos dados!</strong> Aprenda a ler, escrever e processar diferentes tipos de arquivos. Domine CSV, JSON, XML e muito mais para transformar seu programa em um poderoso manipulador de dados.</p>
        </div>

        <div class="content-section">
            <h4>1. Fundamentos de Arquivos em Python</h4>
            <p>Python oferece ferramentas poderosas para trabalhar com arquivos. O gerenciamento adequado de arquivos é essencial para criar aplicações robustas que persistem dados.</p>
            
            <div class="code-example">
                <h5>Abrindo e Fechando Arquivos:</h5>
                <pre><code># Método tradicional (não recomendado)
arquivo = open('exemplo.txt', 'r')
conteudo = arquivo.read()
arquivo.close()  # Importante não esquecer!

# Método recomendado - with statement
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

# Verificando se arquivo existe
import os

nome_arquivo = 'dados.txt'
if os.path.exists(nome_arquivo):
    print(f"Arquivo {nome_arquivo} existe!")
    # Informações do arquivo
    tamanho = os.path.getsize(nome_arquivo)
    print(f"Tamanho: {tamanho} bytes")
else:
    print(f"Arquivo {nome_arquivo} não encontrado")</code></pre>
            </div>

            <div class="code-example">
                <h5>Lendo Arquivos - Diferentes Métodos:</h5>
                <pre><code># 1. Lendo arquivo inteiro
with open('historia.txt', 'r', encoding='utf-8') as arquivo:
    conteudo_completo = arquivo.read()
    print("Conteúdo completo:")
    print(conteudo_completo)

# 2. Lendo linha por linha
print("\nLendo linha por linha:")
with open('historia.txt', 'r', encoding='utf-8') as arquivo:
    for numero_linha, linha in enumerate(arquivo, 1):
        print(f"Linha {numero_linha}: {linha.strip()}")

# 3. Lendo todas as linhas em uma lista
with open('historia.txt', 'r', encoding='utf-8') as arquivo:
    todas_linhas = arquivo.readlines()
    print(f"\nTotal de linhas: {len(todas_linhas)}")
    
# 4. Lendo uma linha específica
with open('historia.txt', 'r', encoding='utf-8') as arquivo:
    primeira_linha = arquivo.readline()
    segunda_linha = arquivo.readline()
    print(f"Primeira linha: {primeira_linha.strip()}")
    print(f"Segunda linha: {segunda_linha.strip()}")

# Exemplo prático: Contador de palavras
def contar_palavras(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
            palavras = texto.split()
            caracteres = len(texto)
            linhas = texto.count('\n') + 1 if texto else 0
            
            print(f"Estatísticas do arquivo '{nome_arquivo}':")
            print(f"Palavras: {len(palavras)}")
            print(f"Caracteres: {caracteres}")
            print(f"Linhas: {linhas}")
            
            # Palavras mais comuns
            from collections import Counter
            palavras_limpas = [p.lower().strip('.,!?;:"()[]') for p in palavras]
            mais_comuns = Counter(palavras_limpas).most_common(5)
            
            print("Palavras mais comuns:")
            for palavra, freq in mais_comuns:
                print(f"  {palavra}: {freq} vezes")
                
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado!")
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")

# Uso da função
contar_palavras('meu_texto.txt')</code></pre>
            </div>

            <div class="code-example">
                <h5>Escrevendo Arquivos:</h5>
                <pre><code># 1. Escrevendo texto simples (sobrescreve)
with open('saida.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")

# 2. Anexando texto ao arquivo
with open('saida.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write("Terceira linha (anexada)\n")

# 3. Escrevendo lista de linhas
linhas = [
    "Esta é a primeira linha\n",
    "Esta é a segunda linha\n",
    "Esta é a terceira linha\n"
]

with open('multiplas_linhas.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.writelines(linhas)

# Exemplo prático: Logger simples
import datetime

def log_evento(mensagem, nivel='INFO'):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha_log = f"[{timestamp}] {nivel}: {mensagem}\n"
    
    with open('aplicacao.log', 'a', encoding='utf-8') as arquivo:
        arquivo.write(linha_log)
    
    print(f"Log registrado: {linha_log.strip()}")

# Usando o logger
log_evento("Sistema iniciado", "INFO")
log_evento("Usuário fez login", "INFO")
log_evento("Erro de conexão com BD", "ERROR")
log_evento("Sistema encerrado", "INFO")

# Sistema de notas estudantis
def salvar_notas_estudante():
    estudantes = []
    
    print("=== SISTEMA DE NOTAS ===")
    while True:
        nome = input("Nome do estudante (ou 'fim' para terminar): ")
        if nome.lower() == 'fim':
            break
            
        try:
            nota = float(input(f"Nota de {nome}: "))
            estudantes.append({'nome': nome, 'nota': nota})
        except ValueError:
            print("Nota inválida! Digite um número.")
    
    # Salvando no arquivo
    with open('notas_estudantes.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write("RELATÓRIO DE NOTAS\n")
        arquivo.write("=" * 30 + "\n\n")
        
        total = 0
        for estudante in estudantes:
            nome = estudante['nome']
            nota = estudante['nota']
            status = "APROVADO" if nota >= 7.0 else "REPROVADO"
            
            linha = f"{nome:<20} | Nota: {nota:5.2f} | {status}\n"
            arquivo.write(linha)
            total += nota
        
        if estudantes:
            media = total / len(estudantes)
            arquivo.write("\n" + "-" * 50 + "\n")
            arquivo.write(f"Média da turma: {media:.2f}\n")
            arquivo.write(f"Total de estudantes: {len(estudantes)}\n")
    
    print(f"Notas salvas em 'notas_estudantes.txt'")

# Descomente para usar:
# salvar_notas_estudante()</code></pre>
            </div>
        </div>

        <div class="content-section">
            <h4>2. Trabalhando com CSV (Comma-Separated Values)</h4>
            <p>CSV é um formato muito comum para dados tabulares. Python oferece o módulo csv que facilita muito o trabalho com esse tipo de arquivo.</p>
            
            <div class="code-example">
                <h5>Lendo Arquivos CSV:</h5>
                <pre><code>import csv

# Exemplo 1: Lendo CSV básico
print("=== LENDO CSV BÁSICO ===")
with open('vendas.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    
    # Primeira linha geralmente contém cabeçalhos
    cabecalhos = next(leitor_csv)
    print(f"Cabeçalhos: {cabecalhos}")
    
    print("\nDados:")
    for linha in leitor_csv:
        print(linha)

# Exemplo 2: Usando DictReader (mais conveniente)
print("\n=== USANDO DICTREADER ===")
with open('vendas.csv', 'r', encoding='utf-8') as arquivo:
    leitor_dict = csv.DictReader(arquivo)
    
    for linha in leitor_dict:
        print(f"Vendedor: {linha['vendedor']}")
        print(f"Produto: {linha['produto']}")
        print(f"Valor: R$ {linha['valor']}")
        print(f"Data: {linha['data']}")
        print("-" * 30)

# Exemplo 3: Processando dados de vendas
def analisar_vendas(arquivo_csv):
    vendas_por_vendedor = {}
    total_geral = 0
    
    with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        
        for linha in leitor:
            vendedor = linha['vendedor']
            valor = float(linha['valor'].replace('R$', '').replace(',', '.'))
            
            if vendedor not in vendas_por_vendedor:
                vendas_por_vendedor[vendedor] = 0
            
            vendas_por_vendedor[vendedor] += valor
            total_geral += valor
    
    print("RELATÓRIO DE VENDAS")
    print("=" * 40)
    for vendedor, total in vendas_por_vendedor.items():
        percentual = (total / total_geral) * 100
        print(f"{vendedor:<15}: R$ {total:8.2f} ({percentual:5.1f}%)")
    
    print("-" * 40)
    print(f"{'TOTAL GERAL':<15}: R$ {total_geral:8.2f}")
    
    # Melhor vendedor
    melhor = max(vendas_por_vendedor, key=vendas_por_vendedor.get)
    print(f"Melhor vendedor: {melhor}")

# Exemplo de uso (descomente para testar)
# analisar_vendas('vendas.csv')</code></pre>
            </div>

            <div class="code-example">
                <h5>Escrevendo Arquivos CSV:</h5>
                <pre><code># Exemplo 1: Escrevendo CSV básico
dados_funcionarios = [
    ['Nome', 'Cargo', 'Salario', 'Departamento'],
    ['Ana Silva', 'Analista', 5000, 'TI'],
    ['Carlos Santos', 'Gerente', 8000, 'Vendas'],
    ['Maria Oliveira', 'Desenvolvedora', 6500, 'TI'],
    ['João Pereira', 'Assistente', 3000, 'RH']
]

with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados_funcionarios)

print("Arquivo funcionarios.csv criado!")

# Exemplo 2: Usando DictWriter
funcionarios_dict = [
    {'nome': 'Ana Silva', 'cargo': 'Analista', 'salario': 5000, 'depto': 'TI'},
    {'nome': 'Carlos Santos', 'cargo': 'Gerente', 'salario': 8000, 'depto': 'Vendas'},
    {'nome': 'Maria Oliveira', 'cargo': 'Desenvolvedora', 'salario': 6500, 'depto': 'TI'},
    {'nome': 'João Pereira', 'cargo': 'Assistente', 'salario': 3000, 'depto': 'RH'}
]

with open('funcionarios_dict.csv', 'w', newline='', encoding='utf-8') as arquivo:
    campos = ['nome', 'cargo', 'salario', 'depto']
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    
    escritor.writeheader()  # Escreve cabeçalhos
    escritor.writerows(funcionarios_dict)

print("Arquivo funcionarios_dict.csv criado!")

# Sistema completo de gestão de produtos
def sistema_produtos():
    produtos = []
    
    # Carregando produtos existentes
    try:
        with open('produtos.csv', 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            produtos = list(leitor)
        print(f"Carregados {len(produtos)} produtos existentes")
    except FileNotFoundError:
        print("Arquivo de produtos não existe, criando novo...")
    
    while True:
        print("\n=== GESTÃO DE PRODUTOS ===")
        print("1. Listar produtos")
        print("2. Adicionar produto")
        print("3. Buscar produto")
        print("4. Salvar e sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            if not produtos:
                print("Nenhum produto cadastrado")
            else:
                print(f"{'ID':<5} {'Nome':<20} {'Preço':<10} {'Estoque':<8}")
                print("-" * 45)
                for produto in produtos:
                    print(f"{produto['id']:<5} {produto['nome']:<20} "
                          f"R${produto['preco']:<9} {produto['estoque']:<8}")
        
        elif opcao == '2':
            produto_id = str(len(produtos) + 1)
            nome = input("Nome do produto: ")
            preco = input("Preço: R$ ")
            estoque = input("Quantidade em estoque: ")
            
            novo_produto = {
                'id': produto_id,
                'nome': nome,
                'preco': preco,
                'estoque': estoque
            }
            produtos.append(novo_produto)
            print("Produto adicionado com sucesso!")
        
        elif opcao == '3':
            busca = input("Nome do produto a buscar: ").lower()
            encontrados = [p for p in produtos if busca in p['nome'].lower()]
            
            if encontrados:
                print("Produtos encontrados:")
                for produto in encontrados:
                    print(f"ID: {produto['id']}, Nome: {produto['nome']}, "
                          f"Preço: R$ {produto['preco']}, Estoque: {produto['estoque']}")
            else:
                print("Nenhum produto encontrado")
        
        elif opcao == '4':
            # Salvando produtos
            with open('produtos.csv', 'w', newline='', encoding='utf-8') as arquivo:
                if produtos:
                    campos = ['id', 'nome', 'preco', 'estoque']
                    escritor = csv.DictWriter(arquivo, fieldnames=campos)
                    escritor.writeheader()
                    escritor.writerows(produtos)
            
            print("Produtos salvos! Saindo...")
            break
        
        else:
            print("Opção inválida!")

# Descomente para usar o sistema:
# sistema_produtos()</code></pre>
            </div>
        </div>

        <div class="content-section">
            <h4>3. Trabalhando com JSON (JavaScript Object Notation)</h4>
            <p>JSON é um formato leve e popular para intercâmbio de dados, especialmente em aplicações web e APIs.</p>
            
            <div class="code-example">
                <h5>Básico de JSON em Python:</h5>
                <pre><code>import json
from datetime import datetime

# 1. Python para JSON (serialização)
dados_python = {
    "nome": "Maria Santos",
    "idade": 28,
    "cidade": "São Paulo",
    "casada": False,
    "filhos": None,
    "hobbies": ["leitura", "natação", "viagem"],
    "endereco": {
        "rua": "Rua das Flores, 123",
        "cep": "01234-567",
        "bairro": "Centro"
    },
    "salario": 5500.75
}

# Convertendo para string JSON
json_string = json.dumps(dados_python, indent=2, ensure_ascii=False)
print("Dados em JSON:")
print(json_string)

# Salvando em arquivo
with open('pessoa.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados_python, arquivo, indent=2, ensure_ascii=False)

print("\nArquivo pessoa.json criado!")

# 2. JSON para Python (desserialização)
print("\n=== LENDO JSON ===")
with open('pessoa.json', 'r', encoding='utf-8') as arquivo:
    dados_carregados = json.load(arquivo)

print(f"Nome: {dados_carregados['nome']}")
print(f"Idade: {dados_carregados['idade']}")
print(f"Hobbies: {', '.join(dados_carregados['hobbies'])}")
print(f"Endereço: {dados_carregados['endereco']['rua']}")

# 3. Trabalhando com JSON de string
json_texto = '''
{
    "produtos": [
        {"id": 1, "nome": "Notebook", "preco": 2500.99},
        {"id": 2, "nome": "Mouse", "preco": 45.50},
        {"id": 3, "nome": "Teclado", "preco": 120.00}
    ]
}
'''

dados_produtos = json.loads(json_texto)
print("\n=== PRODUTOS ===")
for produto in dados_produtos['produtos']:
    print(f"ID: {produto['id']} | {produto['nome']} - R$ {produto['preco']:.2f}")

# Calculando total
total = sum(p['preco'] for p in dados_produtos['produtos'])
print(f"Valor total: R$ {total:.2f}")</code></pre>
            </div>

            <div class="code-example">
                <h5>Sistema de Configuração com JSON:</h5>
                <pre><code># Sistema de configurações da aplicação
import json
import os
from datetime import datetime

class GerenciadorConfig:
    def __init__(self, arquivo_config='config.json'):
        self.arquivo_config = arquivo_config
        self.config_padrao = {
            "aplicacao": {
                "nome": "Minha Aplicação Python",
                "versao": "1.0.0",
                "debug": True,
                "porta": 5000
            },
            "banco_dados": {
                "host": "localhost",
                "porta": 5432,
                "nome_db": "minha_app",
                "usuario": "admin",
                "ssl": False
            },
            "email": {
                "servidor_smtp": "smtp.gmail.com",
                "porta_smtp": 587,
                "usar_ssl": True,
                "remetente": "app@exemplo.com"
            },
            "logs": {
                "nivel": "INFO",
                "arquivo": "app.log",
                "rotacionar": True,
                "max_tamanho_mb": 10
            },
            "ultima_atualizacao": None
        }
        self.carregar_configuracoes()
    
    def carregar_configuracoes(self):
        """Carrega configurações do arquivo ou cria com padrões"""
        if os.path.exists(self.arquivo_config):
            try:
                with open(self.arquivo_config, 'r', encoding='utf-8') as arquivo:
                    self.config = json.load(arquivo)
                print("Configurações carregadas com sucesso!")
            except json.JSONDecodeError:
                print("Erro ao ler configurações, usando padrões...")
                self.config = self.config_padrao.copy()
        else:
            print("Arquivo de configuração não existe, criando padrão...")
            self.config = self.config_padrao.copy()
            self.salvar_configuracoes()
    
    def salvar_configuracoes(self):
        """Salva configurações no arquivo"""
        self.config['ultima_atualizacao'] = datetime.now().isoformat()
        
        try:
            with open(self.arquivo_config, 'w', encoding='utf-8') as arquivo:
                json.dump(self.config, arquivo, indent=2, ensure_ascii=False)
            print("Configurações salvas com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar configurações: {e}")
    
    def obter_config(self, chave, padrao=None):
        """Obtém valor de configuração usando notação de ponto"""
        keys = chave.split('.')
        valor = self.config
        
        try:
            for key in keys:
                valor = valor[key]
            return valor
        except KeyError:
            return padrao
    
    def definir_config(self, chave, valor):
        """Define valor de configuração usando notação de ponto"""
        keys = chave.split('.')
        config = self.config
        
        # Navega até o penúltimo nível
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
        
        # Define o valor final
        config[keys[-1]] = valor
        print(f"Configuração '{chave}' definida como: {valor}")
    
    def exibir_configuracoes(self):
        """Exibe todas as configurações formatadas"""
        print("\n=== CONFIGURAÇÕES ATUAIS ===")
        print(json.dumps(self.config, indent=2, ensure_ascii=False))
    
    def resetar_configuracoes(self):
        """Volta às configurações padrão"""
        self.config = self.config_padrao.copy()
        self.salvar_configuracoes()
        print("Configurações resetadas para o padrão!")

# Exemplo de uso do gerenciador
def demo_gerenciador_config():
    # Criando instância
    config = GerenciadorConfig()
    
    # Exibindo configuração atual
    print(f"Nome da app: {config.obter_config('aplicacao.nome')}")
    print(f"Porta: {config.obter_config('aplicacao.porta')}")
    print(f"Debug: {config.obter_config('aplicacao.debug')}")
    
    # Modificando configurações
    config.definir_config('aplicacao.debug', False)
    config.definir_config('aplicacao.porta', 8080)
    config.definir_config('banco_dados.host', '192.168.1.100')
    
    # Salvando mudanças
    config.salvar_configuracoes()
    
    # Exibindo todas as configurações
    config.exibir_configuracoes()

# Descomente para testar:
# demo_gerenciador_config()

# Sistema de cache em JSON
class CacheJSON:
    def __init__(self, arquivo='cache.json'):
        self.arquivo = arquivo
        self.dados = self.carregar_cache()
    
    def carregar_cache(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def salvar_cache(self):
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.dados, f, indent=2, ensure_ascii=False)
    
    def get(self, chave, padrao=None):
        return self.dados.get(chave, padrao)
    
    def set(self, chave, valor):
        self.dados[chave] = {
            'valor': valor,
            'timestamp': datetime.now().isoformat()
        }
        self.salvar_cache()
    
    def listar_tudo(self):
        print("=== CACHE ATUAL ===")
        for chave, dados in self.dados.items():
            print(f"{chave}: {dados['valor']} (salvo em {dados['timestamp']})")

# Exemplo de uso do cache
cache = CacheJSON()
cache.set('usuario_logado', 'maria@email.com')
cache.set('ultima_consulta', 'produtos_vendas')
cache.set('contador_visitas', 42)

print(f"Usuário logado: {cache.get('usuario_logado')['valor'] if cache.get('usuario_logado') else 'Nenhum'}")
cache.listar_tudo()</code></pre>
            </div>
        </div>

        <div class="tips-section">
            <h4>Dicas Importantes para Manipulação de Arquivos</h4>
            <ul class="tips-list">
                <li><strong>Sempre use encoding:</strong> Especifique encoding='utf-8' para evitar problemas com acentos</li>
                <li><strong>Context managers:</strong> Use 'with' para garantir que arquivos sejam fechados corretamente</li>
                <li><strong>Tratamento de erros:</strong> Sempre trate FileNotFoundError e outras exceções</li>
                <li><strong>Caminhos relativos:</strong> Use os.path.join() para caminhos compatíveis com diferentes sistemas</li>
                <li><strong>Backup de dados:</strong> Sempre faça backup antes de sobrescrever arquivos importantes</li>
                <li><strong>Validação de dados:</strong> Valide dados antes de salvar, especialmente em CSV e JSON</li>
                <li><strong>Performance:</strong> Para arquivos grandes, processe linha por linha ao invés de carregar tudo na memória</li>
            </ul>
        </div>
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
                    'write("arquivo.txt")',
                    'save("arquivo.txt")'
                ],
                'correct_answer': 'open("arquivo.txt", "w")'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual é a vantagem de usar "with" ao trabalhar com arquivos?',
                'options': [
                    'Arquivos são abertos mais rapidamente',
                    'Arquivos são fechados automaticamente',
                    'Permite ler arquivos maiores',
                    'Melhora a performance de escrita',
                    'Não há diferença'
                ],
                'correct_answer': 'Arquivos são fechados automaticamente'
            },
            {
                'type': 'multiple_choice',
                'question': 'Em JSON, qual função converte um dicionário Python para string JSON?',
                'options': ['json.loads()', 'json.dump()', 'json.dumps()', 'json.load()', 'json.parse()'],
                'correct_answer': 'json.dumps()'
            },
            {
                'type': 'multiple_choice',
                'question': 'Qual modo de abertura anexa texto ao final de um arquivo existente?',
                'options': ['r', 'w', 'a', 'x', 'r+'],
                'correct_answer': 'a'
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