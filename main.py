# Ejecuta un archivo .dp (DeepLang)

from antlr4 import FileStream, CommonTokenStream
from grammar.DeepLangLexer import DeepLangLexer
from grammar.DeepLangParser import DeepLangParser
from interpreter.ExecutorVisitor import ExecutorVisitor


def run_file(filename):
    """Ejecuta un archivo DeepLang (.dp)"""
    
    # Crear el flujo de entrada ANTLR
    input_stream = FileStream(filename, encoding="utf-8")

    # Lexer → Tokens → Parser
    lexer = DeepLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DeepLangParser(token_stream)

    # Regla inicial de la gramática
    tree = parser.program()

    # Ejecutar el AST usando nuestro Visitor
    visitor = ExecutorVisitor()
    visitor.visit(tree)


def main():
    print("=== DeepLang Interpreter ===")
    print("Ingresa el nombre del archivo a ejecutar (ej: tests/test_basico.dp):")

    filename = input("> ").strip()

    # Validar archivo manualmente sin librerías externas
    try:
        with open(filename, "r", encoding="utf-8"):
            pass
    except:
        print("Error: archivo no encontrado o no accesible.")
        return

    # Ejecutar
    run_file(filename)



main()

