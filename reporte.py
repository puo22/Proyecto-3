from sintactico import analizar, OK_MSG


def verificar_indentacion(source: str):
    """Verifica indentación: solo espacios o tabs, múltiples de 4, pila estilo Python."""
    lines = source.splitlines()
    stack = [0]
    mode = None  # "spaces" | "tabs" | None
    for ln, raw in enumerate(lines, start=1):
        stripped = raw.lstrip("\t ")
        if stripped == "" or stripped.startswith("#"):
            continue
        leading = raw[: len(raw) - len(stripped)]
        if " " in leading and "\t" in leading:
            return (ln, 1)
        if mode is None:
            if "\t" in leading:
                mode = "tabs"
            elif " " in leading:
                mode = "spaces"
        if mode == "spaces" and "\t" in leading:
            return (ln, 1)
        if mode == "tabs" and " " in leading:
            return (ln, 1)

        if "\t" in leading:
            width = 4 * len(leading)
        else:
            width = len(leading)
            if width % 4 != 0:
                return (ln, 1)

        cur = width
        top = stack[-1]
        if cur == top:
            continue
        if cur == top + 4:
            stack.append(cur)
            continue
        if cur < top:
            while stack and stack[-1] > cur:
                stack.pop()
            if not stack or stack[-1] != cur:
                return (ln, 1)
            continue
        # salto > 4
        return (ln, 1)
    return None


def correr_analisis(source: str):
    falla = verificar_indentacion(source)
    if falla:
        ln, col = falla
        return f"<{ln},{col}>Error sintactico: falla de indentacion"
    ok, err = analizar(source)
    if ok:
        return OK_MSG
    return err
