from symai import Expression, Function


MAIL_CONTEXT = """Improve the writing style, grammar and issue in the following email.
Make the email sound more {0}:
"""


class EmailWriter(Expression):
    def __init__(self):
        super().__init__()
        self.fn = Function(MAIL_CONTEXT)

    def forward(self, x, style='formal'):
        x = self._to_symbol(x)
        self.fn.prompt.format(style)
        return self.fn(x)
