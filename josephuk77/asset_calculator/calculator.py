def calculate_future_assets(
    currnet_assets: int,
    monthly_salary: int,
    monthly_expense: int,
    months: int
) -> int:

    monthly_savings = monthly_salary - monthly_expense

    future_assets = currnet_assets + (monthly_savings * months)

    return future_assets

def calculate_rate(
    future_assets: int,
    annual_interest_rate: bool,
    welfare: bool,
    rate: float,
    months: int
) -> int:

    interest_rate = rate / 100

    if annual_interest_rate:
        monthly_rate = interest_rate / 12
    else:
        monthly_rate = interest_rate

    if welfare:
        future_assets_total = future_assets * (1 + monthly_rate) ** months

    else:
        future_assets_total = future_assets * (1 + monthly_rate * months)

    return round(future_assets_total)