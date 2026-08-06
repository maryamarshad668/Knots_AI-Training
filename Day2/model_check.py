def model_check(knowledge, query):
    symbols = list(knowledge.symbols() | query.symbols())
    return check_all(knowledge, query, symbols, {})

def check_all(knowledge, query, symbols, model):
    if len(symbols) == 0:
        if knowledge.evaluate(model):
            return query.evaluate(model)
        else:
            return True

    symbol = symbols[0]
    remaining = symbols[1:]
    model_true = model.copy()
    model_true[symbol] = True
    result_true = check_all(knowledge, query, remaining, model_true)
    model_false = model.copy()
    model_false[symbol] = False
    result_false = check_all(knowledge, query, remaining, model_false)
    return result_true and result_false

if __name__ == "__main__":
    from logic import Symbol, And, Implication, Not
    rain = Symbol("rain")
    wet = Symbol("wet")
    KB = And(
        Implication(rain, wet),  
        rain                     
    )
    print(model_check(KB, wet))       
    print(model_check(KB, Not(wet)))  
