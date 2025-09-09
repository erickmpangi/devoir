class Var:
    def __init__(self, value):
        self.value = value           # Valor de la variable
        self.children = []           # Lista de tuplas: (peso, nodo_hijo)
        self.grad_value = None       # Gradiente adjunto (cacheado)

    def __mul__(self, other):
        # z = self * other
        z = Var(self.value * other.value)
        # ∂z/∂self = other.value
        self.children.append((other.value, z))
        # ∂z/∂other = self.value
        other.children.append((self.value, z))
        return z

    def __add__(self, other):
        # z = self + other
        z = Var(self.value + other.value)
        # ∂z/∂self = 1
        self.children.append((1.0, z))
        # ∂z/∂other = 1.0
        other.children.append((1.0, z))
        return z

    def sin(self):
        # z = sin(self)
        z = Var(math.sin(self.value))
        # ∂z/∂self = cos(self.value)
        self.children.append((math.cos(self.value), z))
        return z

    def grad(self):
        if self.grad_value is None:
            # Regla de la cadena: suma sobre todos los hijos
            self.grad_value = sum(
                weight * var.grad() for weight, var in self.children
            )
        return self.grad_value
