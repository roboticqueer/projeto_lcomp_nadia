class Formula:

    def __init__(self):
        pass


# ÁTOMOS

class Atom(Formula):

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return (
            isinstance(other, Atom)
            and other.name == self.name
        )

    def __hash__(self):
        return hash((self.name, 'atom'))


# IMPLICAÇÃO

class Implies(Formula):

    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return (
            "("
            + str(self.left)
            + " → "
            + str(self.right)
            + ")"
        )

    def __eq__(self, other):
        return (
            isinstance(other, Implies)
            and other.left == self.left
            and other.right == self.right
        )

    def __hash__(self):
        return hash((
            hash(self.left),
            hash(self.right),
            'implies'
        ))


# NEGAÇÃO

class Not(Formula):

    def __init__(self, inner: Formula):
        super().__init__()
        self.inner = inner

    def __str__(self):
        return "(¬" + str(self.inner) + ")"

    def __eq__(self, other):
        return (
            isinstance(other, Not)
            and other.inner == self.inner
        )

    def __hash__(self):
        return hash((
            hash(self.inner),
            'not'
        ))


# CONJUNÇÃO

class And(Formula):

    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return (
            "("
            + str(self.left)
            + " ∧ "
            + str(self.right)
            + ")"
        )

    def __eq__(self, other):
        return (
            isinstance(other, And)
            and other.left == self.left
            and other.right == self.right
        )

    def __hash__(self):
        return hash((
            hash(self.left),
            hash(self.right),
            'and'
        ))


# DISJUNÇÃO

class Or(Formula):

    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return (
            "("
            + str(self.left)
            + " ∨ "
            + str(self.right)
            + ")"
        )

    def __eq__(self, other):
        return (
            isinstance(other, Or)
            and other.left == self.left
            and other.right == self.right
        )

    def __hash__(self):
        return hash((
            hash(self.left),
            hash(self.right),
            'or'
        ))


# BICONDICIONAL

class Iff(Formula):

    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return (
            "("
            + str(self.left)
            + " ↔ "
            + str(self.right)
            + ")"
        )

    def __eq__(self, other):
        return (
            isinstance(other, Iff)
            and other.left == self.left
            and other.right == self.right
        )

    def __hash__(self):
        return hash((
            hash(self.left),
            hash(self.right),
            'iff'
        ))


# XOR
class Xor(Formula):

    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return (
            "("
            + str(self.left)
            + " ⊕ "
            + str(self.right)
            + ")"
        )

    def __eq__(self, other):
        return (
            isinstance(other, Xor)
            and other.left == self.left
            and other.right == self.right
        )

    def __hash__(self):
        return hash((
            hash(self.left),
            hash(self.right),
            'xor'
        ))