# Backup simples dos dados dos módulos
MODULES_SIMPLE = {
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
    }
}

FINAL_EXAM_SIMPLE = {
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