"""Funciones de análisis léxico y normalización de tokens con indentación."""

KEYWORDS = {
    "False",
    "class",
    "finally",
    "is",
    "return",
    "None",
    "continue",
    "for",
    "lambda",
    "try",
    "True",
    "def",
    "from",
    "nonlocal",
    "while",
    "and",
    "del",
    "global",
    "not",
    "with",
    "as",
    "elif",
    "if",
    "or",
    "yield",
    "assert",
    "else",
    "import",
    "pass",
    "break",
    "except",
    "in",
    "raise",
    "match",
    "case",
}

MULTI_OPS = {
    "==": "tk_igual",
    "!=": "tk_distinto",
    "<=": "tk_menor_igual",
    ">=": "tk_mayor_igual",
    "->": "tk_ejecuta",
    "+=": "tk_suma_asig",
    "-=": "tk_resta_asig",
    "*=": "tk_mult_asig",
    "/=": "tk_div_asig",
    "%=": "tk_mod_asig",
    "**": "tk_potencia",
    "//": "tk_div_entera",
}

SINGLE_OPS = {
    "(": "tk_par_izq",
    ")": "tk_par_der",
    "[": "tk_cor_izq",
    "]": "tk_cor_der",
    "{": "tk_llave_izq",
    "}": "tk_llave_der",
    ",": "tk_coma",
    ":": "tk_dos_puntos",
    ".": "tk_punto",
    "+": "tk_suma",
    "-": "tk_resta",
    "*": "tk_mult",
    "/": "tk_div",
    "%": "tk_mod",
    "=": "tk_asig",
    "<": "tk_menor",
    ">": "tk_mayor",
}

WHITESPACE = {" ", "\t", "\r", "\n"}


def es_letra(cr):
    return cr.isalpha() or cr == "_"


def es_digito(cr):
    return cr.isdigit()


def es_id_parte(cr):
    return es_letra(cr) or es_digito(cr)


def lexer(texto):
    """Autómata que convierte texto fuente en lista de strings <token,...>."""
    tokens = []
    estado = "q0"
    lexema = ""
    i, linea, columna = 0, 1, 1
    n = len(texto)

    while i < n:
        cr = texto[i]

        # Estado inicial q0
        if estado == "q0":
            lexema = ""

            if cr in WHITESPACE:
                if cr == "\n":
                    linea += 1
                    columna = 1
                else:
                    columna += 1
                i += 1
                continue

            # >>>> PRIMERO: operadores de 2 caracteres (como -=, +=, ==, etc.)
            if i + 1 < n and texto[i:i+2] in MULTI_OPS:
                tokens.append(f"<{MULTI_OPS[texto[i:i+2]]},{linea},{columna}>")
                i += 2
                columna += 2
                continue

            # Luego: operadores de 1 carácter
            if cr in SINGLE_OPS:
                tokens.append(f"<{SINGLE_OPS[cr]},{linea},{columna}>")
                i += 1
                columna += 1
                continue

            # Identificadores y palabras clave
            if es_letra(cr):
                estado = "q_id"
                lexema += cr
                start_line, start_col = linea, columna
                i += 1
                columna += 1
                continue

            # Números (incluyen + o - solo si van seguidos de dígito)
            if cr.isdigit() or (cr in "+-" and i + 1 < n and texto[i+1].isdigit()):
                estado = "q_num"
                lexema += cr
                start_line, start_col = linea, columna
                i += 1
                columna += 1
                continue

            # Cadenas
            if cr in "\"'":
                estado = "q_str"
                quote = cr
                start_line, start_col = linea, columna
                i += 1
                columna += 1
                continue

            # Comentarios
            if cr == "#":
                estado = "q_comment"
                i += 1
                columna += 1
                continue

            # Carácter no reconocido
            print(f">>> Error léxico(linea:{linea},columna:{columna})")
            return None

        elif estado == "q_id":
            if i < n and es_id_parte(cr):
                lexema += cr
                i += 1
                columna += 1
                continue
            if lexema in KEYWORDS:
                tokens.append(f"<{lexema},{start_line},{start_col}>")
            else:
                tokens.append(f"<id,{lexema},{start_line},{start_col}>")
            estado = "q0"
            continue

        elif estado == "q_num":
            if i < n and es_digito(cr):
                lexema += cr
                i += 1
                columna += 1
                continue
            tokens.append(f"<tk_entero,{lexema},{start_line},{start_col}>")
            estado = "q0"
            continue

        elif estado == "q_str":
            if i < n and texto[i] != quote and texto[i] != "\n":
                if texto[i] == "\\" and i + 1 < n:
                    lexema += texto[i : i + 2]
                    i += 2
                    columna += 2
                else:
                    lexema += texto[i]
                    i += 1
                    columna += 1
                continue
            if i >= n or texto[i] == "\n":
                print(f">>> Error léxico(linea:{start_line},columna:{start_col})")
                return None
            tokens.append(f'<tk_cadena,"{lexema}",{start_line},{start_col}>')
            i += 1
            columna += 1
            estado = "q0"
            continue

        elif estado == "q_comment":
            if i < n and texto[i] != "\n":
                i += 1
                columna += 1
                continue
            estado = "q0"
            continue

    return tokens


class Tok:
    __slots__ = ("tipo", "lex", "linea", "col")

    def __init__(self, tipo, lex, linea, col):
        self.tipo = tipo
        self.lex = lex
        self.linea = linea
        self.col = col

    def __repr__(self):
        return f"Tok({self.tipo},{self.lex},{self.linea},{self.col})"


INV_SINGLE = {v: k for k, v in SINGLE_OPS.items()}
INV_MULTI = {v: k for k, v in MULTI_OPS.items()}


def _parse_token_str(s):
    s = s.strip()
    assert s[0] == "<" and s[-1] == ">"
    inner = s[1:-1]

    parts, buf, q = [], "", False
    i = 0
    while i < len(inner):
        c = inner[i]
        if c == '"':
            q = not q
            buf += c
            i += 1
            continue
        if c == "," and not q:
            parts.append(buf)
            buf = ""
            i += 1
            continue
        buf += c
        i += 1
    parts.append(buf)

    if parts[0] in KEYWORDS:
        return Tok(parts[0], parts[0], int(parts[1]), int(parts[2]))
    if parts[0] == "id":
        return Tok("id", parts[1], int(parts[2]), int(parts[3]))
    if parts[0] == "tk_cadena":
        return Tok("tk_cadena", parts[1].strip('"'), int(parts[2]), int(parts[3]))
    if parts[0] == "tk_entero":
        return Tok("tk_entero", parts[1], int(parts[2]), int(parts[3]))

    tkn = parts[0]
    linea, col = int(parts[1]), int(parts[2])
    if tkn in INV_SINGLE:
        return Tok(tkn, INV_SINGLE[tkn], linea, col)
    if tkn in INV_MULTI:
        return Tok(tkn, INV_MULTI[tkn], linea, col)
    return Tok(tkn, tkn, linea, col)


def lex_to_tokens(source: str):
    """Convierte salida del lexer a objetos Tok."""
    ts = lexer(source)
    if ts is None:
        return None
    return [_parse_token_str(x) for x in ts]


def with_layout_tokens(source: str, base_tokens):
    """Inserta NEWLINE/INDENT/DEDENT como Python cuando no hay paréntesis abiertos."""
    lines = source.splitlines()
    indents = {}
    for ln, raw in enumerate(lines, start=1):
        stripped = raw.lstrip("\t ")
        if stripped == "" or stripped.startswith("#"):
            continue
        leading = raw[: len(raw) - len(stripped)]
        width = 4 * len(leading) if "\t" in leading else len(leading)
        indents[ln] = width

    out = []
    stack = [0]
    i = 0
    n = len(base_tokens)
    cur_line = 1
    open_count = 0  # (), [], {}
    open_map = {"(": 1, ")": -1, "[": 1, "]": -1, "{": 1, "}": -1}

    def emit_newline_for(line_no):
        if line_no not in indents:
            return
        nonlocal stack
        cur = indents[line_no]
        top = stack[-1]
        if cur == top:
            out.append(Tok("NEWLINE", "\n", line_no, 1))
            return
        if cur == top + 4:
            out.append(Tok("NEWLINE", "\n", line_no, 1))
            stack.append(cur)
            out.append(Tok("INDENT", "<INDENT>", line_no, 1))
            return
        if cur < top:
            out.append(Tok("NEWLINE", "\n", line_no, 1))
            while stack and stack[-1] > cur:
                stack.pop()
                out.append(Tok("DEDENT", "<DEDENT>", line_no, 1))
            return
        # salto > 4: el verificador de indentación lo detectará antes

    while i < n:
        t = base_tokens[i]
        if t.linea > cur_line:
            if open_count == 0:
                emit_newline_for(t.linea)
            cur_line = t.linea
        if t.lex in open_map:
            open_count += open_map[t.lex]
            if open_count < 0:
                open_count = 0
        out.append(t)
        i += 1

    last_line = len(lines) if lines else 1
    out.append(Tok("NEWLINE", "\n", last_line, 1))
    while len(stack) > 1:
        stack.pop()
        out.append(Tok("DEDENT", "<DEDENT>", last_line, 1))
    return out
