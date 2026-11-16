import curses


def show_goal_date(screen, config):
    screen.clear()
    screen.addstr(0, 0, "[목표 자산 달성 시점 조회]")
    screen.addstr(2, 0, "목표 금액 (원): ")
    screen.refresh()
    curses.echo()
    goal = int(screen.getstr(20).decode("utf-8").strip())
    curses.noecho()

    screen.clear()
    screen.addstr(0, 0, "[목표 자산 달성 시점 조회]")
    screen.addstr(2, 0, f"목표 자산: {goal:,}원")
    initial = config["initial_cash"]
    budget = config["monthly_budget"]
    annual_increase = config["annual_salary"] - 12 * \
        (budget["living_expenses"] + budget["fixed_expenses"])

    if goal <= initial:
        screen.addstr(4, 0, "현재 자산이 이미 목표를 달성했습니다. (0개월)")
    elif annual_increase <= 0:
        screen.addstr(4, 0, "현재 계획으로는 총자산이 늘지 않아 달성할 수 없습니다.")
    else:
        difference = goal - initial
        months = (difference * 12 + annual_increase - 1) // annual_increase
        year, month = map(int, config["start_month"].split("-"))
        year_offset, month_index = divmod(month - 1 + months - 1, 12)
        date = f"{year + year_offset:04d}-{month_index + 1:02d}"
        screen.addstr(4, 0, f"달성 예상: {months:,}개월 후 ({date})")
    screen.addstr(6, 0, "Enter를 누르면 돌아갑니다.")
    screen.refresh()
    while screen.getch() not in (curses.KEY_ENTER, 10, 13):
        pass
