def ingresar_formula():
    formula = input("Ingrese la formula: ")
    formula = formula.lower()
    return formula


def contar_a(formula):
    a_pos = ([pos for pos, char in enumerate(formula) if char == "a"])
    print(a_pos)


new_formula = ingresar_formula()
print(new_formula)
contar_a(new_formula)
