class OperatorPrecedenceParser:
    def _init_(self):
        self.operators = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3,
        }

    def parse(self, expression):
        tokens = expression.split()
        output = []
        stack = []
        for token in tokens:
            if token.isdigit():
                output.append(token)
            elif token in self.operators:
                while stack and stack[-1] in self.operators and self.operators[token] <= self.operators[stack[-1]]:
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if not stack:
                    raise ValueError('Mismatched parentheses')
                stack.pop()
            else:
                raise ValueError('Invalid token: %s' % token)
        while stack:
            if stack[-1] == '(':
                raise ValueError('Mismatched parentheses')
            output.append(stack.pop())
        return output
