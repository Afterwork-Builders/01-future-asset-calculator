def show_config(screen, config):
    budget = config["monthly_budget"]
    screen.addstr(2, 0, f"기준 시점: {config['start_month']}")
    screen.addstr(3, 0, f"현재 자산: {config['initial_cash']:,}원")
    screen.addstr(4, 0, f"월 생활비: {budget['living_expenses']:,}원")
    screen.addstr(5, 0, f"고정비: {budget['fixed_expenses']:,}원")
    annual_salary = config["annual_salary"]
    monthly_salary = annual_salary / 12
    screen.addstr(6, 0, f"연봉: {annual_salary:,}원 (월급: {monthly_salary:,.0f}원)")
