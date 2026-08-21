from agents import function_tool
@function_tool
def get_hotel_price(destination: str, budget: str) -> str:
    prices = {"cheap": 50, "mid": 120, "luxury": 300}
    price = prices.get(budget.lower(), 100)
    return f"Estimated hotel price in {destination} for {budget} budget: ${price}/night"