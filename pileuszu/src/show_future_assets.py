import curses
from decimal import Decimal


def show_future_assets(screen, config):
    screen.clear()
    screen.addstr(0, 0, "[미래 자산 조회]")
    screen.addstr(2, 0, "조회할 개월 수: ")
    screen.refresh()
    curses.echo()
    months = int(screen.getstr(20).decode("utf-8").strip())
    curses.noecho()

    year, month = map(int, config["start_month"].split("-"))
    year_offset, month_index = divmod(month - 1 + months - 1, 12)
    date = f"{year + year_offset:04d}-{month_index + 1:02d}"
    budget = config["monthly_budget"]
    monthly_income = Decimal(config["annual_salary"]) / 12
    monthly_expenses = budget["living_expenses"] + budget["fixed_expenses"]
    total = Decimal(config["initial_cash"]) + \
        (monthly_income - monthly_expenses) * months
    screen.clear()
    screen.addstr(0, 0, "[미래 자산 조회]")
    screen.addstr(2, 0, f"{months}개월 후 ({date})")
    screen.addstr(4, 0, f"예상 자산: {total:,.0f}원")
    if total < 0:
        screen.addstr(5, 0, "주의: 자산이 부족합니다.")
    screen.addstr(6, 0, "Enter를 누르면 돌아갑니다.")
    screen.refresh()
    while screen.getch() not in (curses.KEY_ENTER, 10, 13):
        pass
