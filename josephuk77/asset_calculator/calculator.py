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
    current_assets: int,
    monthly_savings: int,
    annual_interest_rate: bool,
    is_compound: bool,
    rate: float,
    months: int
) -> int:

    interest_rate = rate / 100

    if annual_interest_rate:
        monthly_rate = interest_rate / 12
    else:
        monthly_rate = interest_rate

    balance = float(current_assets)
    accumulated_interest = 0.0

    for _ in range(months):
        if is_compound:
            balance += balance * monthly_rate
        else:
            accumulated_interest += balance * monthly_rate

        balance += monthly_savings

    return round(balance + accumulated_interest)
