# Module and quiz data
MODULES = {
    1: {
        'title': 'Introduction to Web Development',
        'content': '''
        <h3>Welcome to Web Development!</h3>
        <p>Web development is the process of creating websites and web applications. It involves both frontend (what users see) and backend (server-side) development.</p>
        
        <h4>Key Concepts:</h4>
        <ul>
            <li><strong>HTML:</strong> The structure of web pages</li>
            <li><strong>CSS:</strong> Styling and layout</li>
            <li><strong>JavaScript:</strong> Interactive functionality</li>
            <li><strong>Responsive Design:</strong> Making websites work on all devices</li>
        </ul>
        
        <h4>Why Learn Web Development?</h4>
        <p>Web development is one of the fastest-growing fields in technology. Every business needs a web presence, making web developers highly sought after.</p>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'What does HTML stand for?',
                'options': [
                    'HyperText Markup Language',
                    'High Tech Modern Language',
                    'Home Tool Markup Language',
                    'Hyperlink and Text Markup Language'
                ],
                'correct_answer': 'HyperText Markup Language'
            },
            {
                'type': 'multiple_choice',
                'question': 'Which technology is primarily used for styling web pages?',
                'options': ['HTML', 'CSS', 'JavaScript', 'Python'],
                'correct_answer': 'CSS'
            },
            {
                'type': 'open_answer',
                'question': 'Name two benefits of responsive web design.',
                'correct_keywords': ['mobile', 'devices', 'accessibility', 'user', 'experience', 'compatibility']
            }
        ]
    },
    2: {
        'title': 'HTML Fundamentals',
        'content': '''
        <h3>HTML Fundamentals</h3>
        <p>HTML (HyperText Markup Language) is the backbone of all web pages. It provides structure and content using a system of tags and elements.</p>
        
        <h4>Basic HTML Structure:</h4>
        <pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Page Title&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;My First Heading&lt;/h1&gt;
    &lt;p&gt;My first paragraph.&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        
        <h4>Common HTML Elements:</h4>
        <ul>
            <li><strong>&lt;h1&gt; to &lt;h6&gt;:</strong> Headings</li>
            <li><strong>&lt;p&gt;:</strong> Paragraphs</li>
            <li><strong>&lt;a&gt;:</strong> Links</li>
            <li><strong>&lt;img&gt;:</strong> Images</li>
            <li><strong>&lt;div&gt; and &lt;span&gt;:</strong> Generic containers</li>
        </ul>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Which HTML tag is used for the largest heading?',
                'options': ['<h6>', '<h1>', '<header>', '<title>'],
                'correct_answer': '<h1>'
            },
            {
                'type': 'multiple_choice',
                'question': 'What is the correct HTML element for inserting a line break?',
                'options': ['<break>', '<br>', '<lb>', '<newline>'],
                'correct_answer': '<br>'
            },
            {
                'type': 'open_answer',
                'question': 'What does the DOCTYPE declaration do in HTML?',
                'correct_keywords': ['document', 'type', 'browser', 'rendering', 'mode']
            }
        ]
    },
    3: {
        'title': 'CSS Styling',
        'content': '''
        <h3>CSS Styling</h3>
        <p>CSS (Cascading Style Sheets) is used to style and layout web pages. It allows you to control colors, fonts, spacing, and positioning.</p>
        
        <h4>CSS Syntax:</h4>
        <pre><code>selector {
    property: value;
    property: value;
}</code></pre>
        
        <h4>Types of CSS Selectors:</h4>
        <ul>
            <li><strong>Element Selector:</strong> p { color: blue; }</li>
            <li><strong>Class Selector:</strong> .my-class { font-size: 16px; }</li>
            <li><strong>ID Selector:</strong> #my-id { background: red; }</li>
        </ul>
        
        <h4>The Box Model:</h4>
        <p>Every element in CSS is essentially a box consisting of: content, padding, border, and margin.</p>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Which CSS property is used to change the text color?',
                'options': ['text-color', 'color', 'font-color', 'text-style'],
                'correct_answer': 'color'
            },
            {
                'type': 'multiple_choice',
                'question': 'What does CSS stand for?',
                'options': [
                    'Cascading Style Sheets',
                    'Computer Style Sheets',
                    'Creative Style Sheets',
                    'Colorful Style Sheets'
                ],
                'correct_answer': 'Cascading Style Sheets'
            },
            {
                'type': 'open_answer',
                'question': 'Name the four components of the CSS box model.',
                'correct_keywords': ['content', 'padding', 'border', 'margin']
            }
        ]
    },
    4: {
        'title': 'JavaScript Basics',
        'content': '''
        <h3>JavaScript Basics</h3>
        <p>JavaScript is a programming language that makes web pages interactive. It can respond to user actions, manipulate content, and communicate with servers.</p>
        
        <h4>Variables and Data Types:</h4>
        <pre><code>let name = "John";        // String
let age = 25;             // Number
let isStudent = true;     // Boolean
let hobbies = ["reading", "coding"];  // Array</code></pre>
        
        <h4>Functions:</h4>
        <pre><code>function greetUser(name) {
    return "Hello, " + name + "!";
}

let message = greetUser("Alice");</code></pre>
        
        <h4>DOM Manipulation:</h4>
        <p>JavaScript can change HTML content and CSS styles dynamically:</p>
        <pre><code>document.getElementById("myElement").innerHTML = "New content";</code></pre>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'Which keyword is used to declare a variable in modern JavaScript?',
                'options': ['var', 'let', 'const', 'Both let and const'],
                'correct_answer': 'Both let and const'
            },
            {
                'type': 'multiple_choice',
                'question': 'What does DOM stand for?',
                'options': [
                    'Document Object Model',
                    'Data Object Management',
                    'Dynamic Object Method',
                    'Document Oriented Model'
                ],
                'correct_answer': 'Document Object Model'
            },
            {
                'type': 'open_answer',
                'question': 'What is the difference between let and const in JavaScript?',
                'correct_keywords': ['reassignment', 'mutable', 'immutable', 'constant', 'variable']
            }
        ]
    },
    5: {
        'title': 'Responsive Design & Best Practices',
        'content': '''
        <h3>Responsive Design & Best Practices</h3>
        <p>Responsive design ensures your website works well on all devices - from mobile phones to desktop computers.</p>
        
        <h4>Key Principles:</h4>
        <ul>
            <li><strong>Flexible Grid Systems:</strong> Use relative units like percentages</li>
            <li><strong>Media Queries:</strong> Apply different styles for different screen sizes</li>
            <li><strong>Flexible Images:</strong> Images that scale with their container</li>
        </ul>
        
        <h4>Media Query Example:</h4>
        <pre><code>@media screen and (max-width: 768px) {
    .container {
        width: 100%;
        padding: 10px;
    }
}</code></pre>
        
        <h4>Best Practices:</h4>
        <ul>
            <li>Mobile-first approach</li>
            <li>Optimize images and assets</li>
            <li>Use semantic HTML</li>
            <li>Test across different devices</li>
            <li>Ensure accessibility</li>
        </ul>
        ''',
        'quiz': [
            {
                'type': 'multiple_choice',
                'question': 'What is the mobile-first approach in responsive design?',
                'options': [
                    'Design for mobile devices only',
                    'Design for mobile first, then enhance for larger screens',
                    'Test on mobile devices first',
                    'Use mobile frameworks only'
                ],
                'correct_answer': 'Design for mobile first, then enhance for larger screens'
            },
            {
                'type': 'multiple_choice',
                'question': 'Which CSS feature is primarily used for responsive design?',
                'options': ['Flexbox', 'Media Queries', 'Grid', 'All of the above'],
                'correct_answer': 'All of the above'
            },
            {
                'type': 'open_answer',
                'question': 'Why is accessibility important in web development?',
                'correct_keywords': ['users', 'disabilities', 'inclusive', 'everyone', 'equal', 'access']
            }
        ]
    }
}

FINAL_EXAM = {
    'title': 'Final Comprehensive Exam',
    'description': 'This exam covers all the modules you have completed. You need 70% to pass.',
    'questions': [
        {
            'type': 'multiple_choice',
            'question': 'Which of the following is NOT a semantic HTML element?',
            'options': ['<article>', '<section>', '<div>', '<nav>'],
            'correct_answer': '<div>'
        },
        {
            'type': 'multiple_choice',
            'question': 'In CSS, which property is used to control the space between elements?',
            'options': ['padding', 'margin', 'spacing', 'gap'],
            'correct_answer': 'margin'
        },
        {
            'type': 'multiple_choice',
            'question': 'What is the correct way to link an external CSS file?',
            'options': [
                '<link rel="stylesheet" href="style.css">',
                '<style src="style.css">',
                '<css link="style.css">',
                '<import css="style.css">'
            ],
            'correct_answer': '<link rel="stylesheet" href="style.css">'
        },
        {
            'type': 'multiple_choice',
            'question': 'Which JavaScript method is used to add an event listener?',
            'options': ['addEventListener()', 'attachEvent()', 'addEvent()', 'listenEvent()'],
            'correct_answer': 'addEventListener()'
        },
        {
            'type': 'multiple_choice',
            'question': 'What is the viewport meta tag used for?',
            'options': [
                'Setting the page title',
                'Controlling how the page is displayed on mobile devices',
                'Adding keywords for SEO',
                'Loading external scripts'
            ],
            'correct_answer': 'Controlling how the page is displayed on mobile devices'
        },
        {
            'type': 'open_answer',
            'question': 'Explain the difference between block and inline elements in HTML.',
            'correct_keywords': ['width', 'height', 'newline', 'flow', 'content', 'display']
        },
        {
            'type': 'open_answer',
            'question': 'What are the advantages of using external CSS files over inline styles?',
            'correct_keywords': ['reusable', 'maintainable', 'separation', 'caching', 'organization']
        },
        {
            'type': 'open_answer',
            'question': 'Describe what happens when a user clicks a button on a webpage.',
            'correct_keywords': ['event', 'handler', 'function', 'DOM', 'browser', 'response']
        }
    ]
}
