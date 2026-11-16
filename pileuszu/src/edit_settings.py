import curses
import json
from datetime import datetime

from .show_config import show_config


def edit_settings(screen, config, config_path):
    fields = [
        ("시작 연월 (YYYY-MM)", config, "start_month"),
        ("시작 자산 (원)", config, "initial_cash"),
        ("연봉 (원)", config, "annual_salary"),
        ("월 생활비 (원)", config["monthly_budget"], "living_expenses"),
        ("월 고정비 (원)", config["monthly_budget"], "fixed_expenses"),
    ]
    selected = 0
    message = ""

    while True:
        screen.clear()
        screen.addstr(0, 0, "[설정 조회/수정]")
        show_config(screen, config)
        screen.addstr(8, 0, "↑↓ 선택 · Enter 확인")
        for index, (label, _, _) in enumerate(fields):
            screen.addstr(index + 10, 0, f"{index + 1}. {label}", curses.A_REVERSE if index == selected else curses.A_NORMAL)
        screen.addstr(len(fields) + 10, 0, f"{len(fields) + 1}. 돌아가기", curses.A_REVERSE if selected == len(fields) else curses.A_NORMAL)
        if message:
            screen.addstr(1, 0, message)
        screen.refresh()

        key = screen.getch()
        if key == curses.KEY_UP:
            selected = (selected - 1) % (len(fields) + 1)
        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % (len(fields) + 1)
        elif key in (curses.KEY_ENTER, 10, 13):
            if selected == len(fields):
                return
            label, values, field = fields[selected]
            screen.clear()
            screen.addstr(0, 0, f"{label} 수정 (빈 입력은 취소)")
            screen.addstr(2, 0, "새 값: ")
            screen.refresh()
            curses.echo()
            raw = screen.getstr(20).decode("utf-8").strip()
            curses.noecho()

            if not raw:
                message = "수정을 취소했습니다."
                continue
            if field == "start_month":
                new_value = datetime.strptime(raw, "%Y-%m").strftime("%Y-%m")
            else:
                new_value = int(raw)

            values[field] = new_value
            with config_path.open("w", encoding="utf-8") as file:
                json.dump(config, file, ensure_ascii=False, indent=2)
                file.write("\n")
            message = f"{label} 설정을 저장했습니다."
