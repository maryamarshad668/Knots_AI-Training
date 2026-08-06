from logic import Symbol, And, Or, Not
from model_check import model_check

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
knife = Symbol("Knife")
candlestick = Symbol("Candlestick")
revolver = Symbol("Revolver")
ballroom = Symbol("Ballroom")
library = Symbol("Library")
study = Symbol("Study")
suspects = [mustard, plum, scarlet]
weapons = [knife, candlestick, revolver]
rooms = [ballroom, library, study]

knowledge = And(
    Or(mustard, plum, scarlet),    
    Or(knife, candlestick, revolver),
    Or(ballroom, library, study),
)
my_cards = [mustard, knife, ballroom, plum]
for card in my_cards:
    knowledge = And(knowledge, Not(card))
knowledge = And(knowledge, Not(study))
print(" ******* Clue Solver Results *******")
all_symbols = suspects + weapons + rooms
for symbol in all_symbols:
    if model_check(knowledge, symbol):
        print(f"{symbol}: definitely the answer")
    elif model_check(knowledge, Not(symbol)):
        print(f"{symbol}: definitelynot the answer")
    else:
        print(f"{symbol}: unknown so far")