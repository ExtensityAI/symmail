from symai import Expression, Function


MAIL_CONTEXT = """Improve the writing style, grammar and spelling issue in the following email.
Also properly format the structure of the email with subject, signature, etc.
Make the email have more `{0}` reading language:
"""


class EmailWriter(Expression):
    def __init__(self):
        super().__init__()
        self.fn = Function(MAIL_CONTEXT)

    def forward(self, x, style='formal', *args, **kwargs):
        x = self._to_symbol(x)
        self.fn.prompt.format(style)
        return self.fn(x, *args, **kwargs)
