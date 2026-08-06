import itertools
from logic import Symbol, And, Or, Not, Biconditional
from model_check import model_check

def is_satisfiable(knowledge):
    """Check if there's at least ONE model where knowledge is True.
    (Brute force: try every True/False combo for every symbol.)"""
    symbols = list(knowledge.symbols())
    for values in itertools.product([True, False], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        if knowledge.evaluate(model):
            return True
    return False

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

base = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
)

def show_results(name, knowledge):
    print(f"--- {name} ---")
    if not is_satisfiable(knowledge):
        print("No valid solution exists — the statements contradict themselves (a paradox).")
        print()
        return
    print("A is Knight:", model_check(knowledge, AKnight))
    print("A is Knave: ", model_check(knowledge, AKnave))
    print("B is Knight:", model_check(knowledge, BKnight))
    print("B is Knave: ", model_check(knowledge, BKnave))
    print()

# Puzzle 1: A says I am a knave. B says We are different.

a_statement_1 = AKnave
b_statement_1 = Not(Biconditional(AKnight, BKnight))
puzzle1 = And(
    base,
    Biconditional(AKnight, a_statement_1), 
    Biconditional(BKnight, b_statement_1),
)
show_results("Puzzle 1", puzzle1)

# Puzzle 2: A says We are both knaves. B says nothing.

a_statement_2 = And(AKnave, BKnave)
puzzle2 = And(
    base,
    Biconditional(AKnight, a_statement_2),
)
show_results("Puzzle 2", puzzle2)

# Puzzle 3: A says We are the same kind. B says We are different kinds.

a_statement_3 = Biconditional(AKnight, BKnight)     
b_statement_3 = Not(Biconditional(AKnight, BKnight)) 
puzzle3 = And(
    base,
    Biconditional(AKnight, a_statement_3),
    Biconditional(BKnight, b_statement_3),
)
show_results("Puzzle 3", puzzle3)