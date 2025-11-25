# Proyecto-3
# DeepLang – DSL para Deep Learning usando ANTLR4 + Python

DeepLang es un lenguaje de dominio específico creado para realizar operaciones matemáticas, manejo de matrices, gráficas, machine learning básico y estructuras de control, inspirado en Python.

Este proyecto implementa:
- Gramática completa en ANTLR4  
- Intérprete basado en Visitor  
- Librerías internas (`runtime/`)  
- Ejecutor por consola  
- Programas de prueba  

---

## 🚀 Ejecutar DeepLang

```bash
python3 main.py archivo.dp

python3 main.py tests/test_basico.dp

```

## Estrcutura del proyecto

```bash
 Proyecto3/
│
├── grammar/                # Gramática ANTLR4
│   ├── DeepLang.g4
│   ├── DeepLangLexer.py
│   └── DeepLangParser.py
│
├── interpreter/
│   └── ExecutorVisitor.py  # Visitor (núcleo del lenguaje)
│
├── runtime/                # Librerías internas
│   ├── matrix.py
│   ├── tensor.py
│   ├── ml.py
│   ├── files.py
│   ├── plots.py
│   ├── memory.py
│
├── tests/                  # Programas .dp de prueba
│   ├── test_basico.dp
│   ├── test_matrices.dp
│   ├── test_ml.dp
│   ├── test_plots.dp
│   └── full_test.dp
│
├── main.py                 # Intérprete
└── antlr_env.py            # Adaptador para ANTLR sin libs externas

```

✔ Funcionalidades del Lenguaje
🔢 Aritmética

+ - * / % // **

📚 Listas y matrices

[1,2,3]

[[1,2],[3,4]]

transpose(x)

inverse(x)

🔁 Control de flujo

if / elif / else

while

for x in y

📂 Archivos

read("file.txt")

write("file.txt", contenido)

📊 Gráficas

plot_line(x,y)

plot_bar(labels,values)

🤖 Machine Learning

linreg(X, Y)

mlp(X, weights)

🧪 Tests incluidos
test_basico.dp     # Variables, ciclos, funciones
test_matrices.dp   # Operaciones matriciales
test_ml.dp         # ML básico
test_plots.dp      # Gráficas
full_test.dp       # Proyecto completo

🧩 Requisitos Técnicos

Python 3.x

ANTLR 4 (generación previa del parser)

No usa librerías externas (matplotlib, numpy, etc.)

📜 Licencia
Proyecto académico – uso educativo.
