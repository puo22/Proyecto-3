# interpreter/ExecutorVisitor.py
from grammar.DeepLangVisitor import DeepLangVisitor
from runtime.memory import MEMORY
from runtime.matrix import mat_add, mat_sub, mat_mul, transpose, inverse
from runtime.tensor import tensor_add, tensor_shape
from runtime.ml import linear_regression, mlp_predict
from runtime.files import read_file, write_file
from runtime.plots import plot_line, plot_scatter, plot_bar, plot_hist


class ExecutorVisitor(DeepLangVisitor):
    def __init__(self):
        super().__init__()
        self.scope = {}
        self.functions = {}

    # -------------------------
    # UTILIDADES
    # -------------------------
    def _visit_maybe(self, node):
        if node is None:
            return None
        return self.visit(node)

    def _get_list(self, ctx_list):
        if ctx_list is None:
            return []
        return [self.visit(x) for x in ctx_list]

    # -------------------------
    # PROGRAM / STATEMENTS
    # -------------------------
    def visitProgram(self, ctx):
        return self.visit(ctx.stmtList())

    def visitStmtList(self, ctx):
        for s in ctx.stmt():
            self.visit(s)
        return None

    # simple_stmt → assign / return / import / print / expr
    def visitSimple_stmt(self, ctx):
        return self.visit(ctx.small_stmt())

    # -------------------------
    # ASSIGNMENTS
    # -------------------------
    def visitAssign_stmt(self, ctx):
        """
        Detecta si es:
            A = expr              → asignación normal
            A[1] = expr           → asignación por indexación
            A[1,2] = expr         → indexación multidimensional
        """
        if ctx.indexing():
            return self.visitAssignIndexing(ctx)

        # Asignación normal
        name = ctx.ID().getText()
        val = self._visit_maybe(ctx.expr())
        stored = MEMORY.alloc(name, val)
        self.scope[name] = stored
        return stored

    def visitAssignIndexing(self, ctx):
        """
        Maneja:
            A[0] = 10
            A[1][2] = 99
            A[1,2,3] = x
        """
        name = ctx.indexing().ID().getText()
        base = self.scope.get(name)

        if base is None:
            raise Exception(f"Variable '{name}' no definida")

        indexes = [self.visit(e) for e in ctx.indexing().expr()]
        new_value = self.visit(ctx.expr())

        # Navegar hasta el penúltimo nivel
        target = base
        for i in range(len(indexes) - 1):
            idx = indexes[i]
            target = target[idx]

        # Último índice
        final_index = indexes[-1]

        # Asignación real
        target[final_index] = new_value

        # Guardar en memoria (mutación)
        MEMORY.alloc(f"{name}_index_update", base)
        self.scope[name] = base
        return new_value

    # -------------------------
    # STATEMENTS: return, import, print, expr
    # -------------------------
    def visitReturn_stmt(self, ctx):
        return self._visit_maybe(ctx.expr())

    def visitImport_stmt(self, ctx):
        if ctx.ID():
            modname = ctx.ID().getText()
            print(f"[import] módulo '{modname}' ignorado (simulado)")
        return None

    def visitPrint_stmt(self, ctx):
        if ctx.expr():
            val = self.visit(ctx.expr())
            print(val)
            return val
        print()
        return None

    def visitExpr_stmt(self, ctx):
        return self.visit(ctx.expr())

    # -------------------------
    # COMPOUND STATEMENTS
    # -------------------------
    def visitFuncdef(self, ctx):
        name = ctx.ID().getText()
        params = []

        if ctx.paramList():
            params = [p.ID().getText() for p in ctx.paramList().param()]

        body = ctx.stmtList()
        self.functions[name] = {"params": params, "body": body}
        return None

    def visitIf_stmt(self, ctx):
        cond = self.visit(ctx.expr(0))
        if cond:
            return self.visit(ctx.stmtList(0))

        n_expr = len(ctx.expr())
        for i in range(1, n_expr):
            if self.visit(ctx.expr(i)):
                return self.visit(ctx.stmtList(i))

        if len(ctx.stmtList()) > n_expr:
            return self.visit(ctx.stmtList(-1))

        return None

    def visitWhile_stmt(self, ctx):
        while self.visit(ctx.expr()):
            self.visit(ctx.stmtList())
        return None

    def visitFor_stmt(self, ctx):
        var = ctx.ID().getText()
        iterable = self.visit(ctx.expr())
        if iterable is None:
            return None

        for item in iterable:
            self.scope[var] = item
            self.visit(ctx.stmtList())
        return None

    def visitClassdef(self, ctx):
        name = ctx.ID().getText()
        body = ctx.stmtList()
        self.scope[name] = {"__class_body__": body}
        return None

    # -------------------------
    # EXPRESSIONS
    # -------------------------
    def visitExpr(self, ctx):
        return self.visit(ctx.orExpr())

    def visitOrExpr(self, ctx):
        vals = [self.visit(x) for x in ctx.andExpr()]
        res = vals[0] if vals else False
        for v in vals[1:]:
            res = res or v
        return res

    def visitAndExpr(self, ctx):
        vals = [self.visit(x) for x in ctx.notExpr()]
        res = vals[0] if vals else True
        for v in vals[1:]:
            res = res and v
        return res

    def visitNotExpr(self, ctx):
        if ctx.getChildCount() >= 2 and ctx.getChild(0).getText() == 'not':
            return not self.visit(ctx.notExpr())
        return self.visit(ctx.comparison())

    def visitComparison(self, ctx):
        items = [self.visit(a) for a in ctx.arithExpr()]
        ops = []

        for ch in ctx.getChildren():
            txt = ch.getText()
            if txt in ("==", "!=", "<", "<=", ">", ">=", "in", "is"):
                ops.append(txt)

        if not ops:
            return items[0]

        left = items[0]
        idx = 1
        result = True

        for op in ops:
            right = items[idx]
            if op == "==": result = (left == right)
            elif op == "!=": result = (left != right)
            elif op == "<": result = (left < right)
            elif op == "<=": result = (left <= right)
            elif op == ">": result = (left > right)
            elif op == ">=": result = (left >= right)
            elif op == "in": result = (left in right)
            elif op == "is": result = (left is right)

            left = right
            idx += 1

        return result

    def visitArithExpr(self, ctx):
        terms = ctx.term()
        vals = [self.visit(t) for t in terms]
        ops = []

        for ch in ctx.getChildren():
            if ch.getText() in ('+', '-'):
                ops.append(ch.getText())

        if not vals:
            return 0

        res = vals[0]
        j = 1

        for op in ops:
            right = vals[j]
            if op == '+':
                if isinstance(res, list) and isinstance(right, list):
                    res = mat_add(res, right)
                else:
                    res = res + right
            else:
                if isinstance(res, list) and isinstance(right, list):
                    res = mat_sub(res, right)
                else:
                    res = res - right
            j += 1

        return res

    def visitTerm(self, ctx):
        facts = ctx.factor()
        vals = [self.visit(f) for f in facts]
        ops = []

        for ch in ctx.getChildren():
            if ch.getText() in ('*', '/', '%', '//'):
                ops.append(ch.getText())

        if not vals:
            return 0

        res = vals[0]
        j = 1

        for op in ops:
            right = vals[j]

            if op == '*':
                if isinstance(res, list) and isinstance(right, list):
                    res = mat_mul(res, right)
                else:
                    res = res * right
            elif op == '/':
                res = res / right
            elif op == '//':
                res = res // right
            elif op == '%':
                res = res % right

            j += 1

        return res

    def visitFactor(self, ctx):
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() in ('+', '-'):
            op = ctx.getChild(0).getText()
            val = self.visit(ctx.factor())
            return +val if op == '+' else -val
        return self.visit(ctx.power())

    def visitPower(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '**':
            return self.visit(ctx.atom()) ** self.visit(ctx.factor())
        return self.visit(ctx.atom())

    # -------------------------
    # ATOMS
    # -------------------------
    def visitAtom(self, ctx):
        if ctx.ID():
            return self.scope.get(ctx.ID().getText(), None)
        if ctx.TK_INT():
            return int(ctx.TK_INT().getText())
        if ctx.TK_FLOAT():
            return float(ctx.TK_FLOAT().getText())
        if ctx.TK_STRING():
            return ctx.TK_STRING().getText()[1:-1]
        if ctx.getText() == 'None':
            return None
        if ctx.getText() == 'True':
            return True
        if ctx.getText() == 'False':
            return False
        if ctx.getChildCount() >= 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expr())
        if ctx.listLiteral():
            return self.visit(ctx.listLiteral())
        if ctx.matrixLiteral():
            return self.visit(ctx.matrixLiteral())
        if ctx.callExpr():
            return self.visit(ctx.callExpr())
        if ctx.indexing():
            return self.visit(ctx.indexing())
        return None

    # -------------------------
    # LIST / MATRIX
    # -------------------------
    def visitListLiteral(self, ctx):
        return [self.visit(e) for e in ctx.expr()] if ctx.expr() else []

    def visitMatrixLiteral(self, ctx):
        rows = []
        for child in ctx.getChildren():
            try:
                if child.getText().startswith('[') and hasattr(child, "expr"):
                    rows.append([self.visit(e) for e in child.expr()])
            except:
                pass
        return rows

    # -------------------------
    # FUNCTION CALLS
    # -------------------------
    def visitCallExpr(self, ctx):
        name = ctx.ID().getText()

        args = []
        if ctx.argList():
            args = [self.visit(a) for a in ctx.argList().expr()]

        # Built-ins
        if name == "len": return len(args[0])
        if name == "read": return read_file(args[0])
        if name == "write": return write_file(args[0], args[1])

        # Plots
        if name == "plot_line": return plot_line(*args)
        if name == "plot_scatter": return plot_scatter(*args)
        if name == "plot_bar": return plot_bar(*args)
        if name == "plot_hist": return plot_hist(*args)

        # Matrix ops
        if name == "transpose": return transpose(args[0])
        if name == "inverse": return inverse(args[0])

        # ML
        if name == "linreg": return linear_regression(args[0], args[1])
        if name == "mlp": return mlp_predict(args[0], args[1])

        # User-defined
        if name in self.functions:
            fn = self.functions[name]

            saved = dict(self.scope)
            for i, pname in enumerate(fn["params"]):
                self.scope[pname] = args[i] if i < len(args) else None

            result = self.visit(fn["body"])
            self.scope = saved
            return result

        return None

    # -------------------------
    # INDEXING
    # -------------------------
    def visitIndexing(self, ctx):
        name = ctx.ID().getText()
        base = self.scope.get(name)

        if base is None:
            raise Exception(f"Variable '{name}' no definida")

        indexes = [self.visit(e) for e in ctx.expr()]
        result = base

        for idx in indexes:
            result = result[idx]

        return result
