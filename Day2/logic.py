class Symbol:
    """A basic fact, like 'ColMustard' or 'rain'."""
    def __init__(self, name):
        self.name = name
    def evaluate(self, model):
        return model[self.name]
    def symbols(self):
        return {self.name}
    def __repr__(self):
        return self.name

class Not:
    """NOT operand — flips True/False."""
    def __init__(self, operand):
        self.operand = operand
    def evaluate(self, model):
        return not self.operand.evaluate(model)
    def symbols(self):
        return self.operand.symbols()
    def __repr__(self):
        return f"Not({self.operand})"

class And:
    """AND of two or more sentences — True only if ALL are True."""
    def __init__(self, *sentences):
        self.sentences = list(sentences)
    def evaluate(self, model):
        for sentence in self.sentences:
            if not sentence.evaluate(model):
                return False
        return True
    def symbols(self):
        all_symbols = set()
        for sentence in self.sentences:
            all_symbols |= sentence.symbols()
        return all_symbols
    def __repr__(self):
        parts = ", ".join(str(s) for s in self.sentences)
        return f"And({parts})"

class Or:
    """OR of two or more sentences — True if AT LEAST ONE is True."""
    def __init__(self, *sentences):
        self.sentences = list(sentences)
    def evaluate(self, model):
        for sentence in self.sentences:
            if sentence.evaluate(model):
                return True
        return False
    def symbols(self):
        all_symbols = set()
        for sentence in self.sentences:
            all_symbols |= sentence.symbols()
        return all_symbols
    def __repr__(self):
        parts = ", ".join(str(s) for s in self.sentences)
        return f"Or({parts})"

class Implication:
    """If antecedent is True, consequent must be True.
    Only False when antecedent=True and consequent=False."""
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent
    def evaluate(self, model):
        if self.antecedent.evaluate(model) and not self.consequent.evaluate(model):
            return False
        return True
    def symbols(self):
        return self.antecedent.symbols() | self.consequent.symbols()
    def __repr__(self):
        return f"Implication({self.antecedent} => {self.consequent})"

class Biconditional:
    """True only when both sides have the SAME truth value."""
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def evaluate(self, model):
        return self.left.evaluate(model) == self.right.evaluate(model)
    def symbols(self):
        return self.left.symbols() | self.right.symbols()
    def __repr__(self):
        return f"Biconditional({self.left} <=> {self.right})"