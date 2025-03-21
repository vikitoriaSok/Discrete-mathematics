from itertools import product

def logical_and(a, b):
    return a and b

def logical_or(a, b):
    return a or b

def logical_not(a):
    return not a

def logical_implies(a, b):
    return logical_not(a) or b

def evaluate_expression(A, B, C):
    part1 = logical_or(A, B)
    part2 = logical_and(A, C)
    return logical_not(logical_implies(part1, part2))

def get_sdnf(expression, variables):
    sdnf = []
    for values in product([False, True], repeat=len(variables)):
        if expression(*values):
            term = []
            for var, val in zip(variables, values):
                if val:
                    term.append(var)
                else:
                    term.append(f"¬{var}")
            sdnf.append(" ∧ ".join(term))
    return " ∨ ".join(f"({term})" for term in sdnf)

def simplify_expression():
    # Упрощение выражения F = ¬(A ∨ B → AC)
    # Используем законы булевой алгебры
    # F = ¬(¬(A ∨ B) ∨ (A ∧ C))
    # F = (A ∨ B) ∧ ¬(A ∧ C)
    return "(A ∨ B) ∧ (¬A ∨ ¬C)"

# Ввод значений переменных
A = input("Введите значение A: ").lower() == 'true'
B = input("Введите значение B: ").lower() == 'true'
C = input("Введите значение C: ").lower() == 'true'

# Вычисление значения выражения
result = evaluate_expression(A, B, C)

# Построение СДНФ
variables = ['A', 'B', 'C']
sdnf = get_sdnf(evaluate_expression, variables)

# Упрощение выражения
simplified_expr = simplify_expression()

# Вывод результатов
print(f"Результат выражения: {int(result)}")  # Преобразуем результат в цифру
print(f"СДНФ выражения: {sdnf}")
print(f"Упрощенное выражение: {simplified_expr}")

# Вывод таблицы истинности в цифрах
print("\nТаблица истинности:")
print("A\tB\tC\tF")
for values in product([False, True], repeat=len(variables)):
    A_val, B_val, C_val = values
    F_val = evaluate_expression(A_val, B_val, C_val)
    # Преобразуем True/False в 1/0
    print(f"{int(A_val)}\t{int(B_val)}\t{int(C_val)}\t{int(F_val)}")
