import curses
from pathlib import Path

from src.edit_settings import edit_settings
from src.load_config import load_config
from src.show_config import show_config
from src.show_future_assets import show_future_assets
from src.show_goal_date import show_goal_date


def main(screen):
    curses.curs_set(0)

    config_path = Path(__file__).parent / "config.json"
    config = load_config(config_path)

    menus = [
        "1. 설정 조회/수정",
        "2. 미래 자산 조회",
        "3. 목표 자산 달성 시점 조회",
        "4. 종료"
    ]

    selected = 0

    while True:
        screen.clear()
        screen.addstr(0, 0, "[미래 자산 계산기]")
        show_config(screen, config)
        screen.addstr(8, 0, "↑↓ 를 이용해 메뉴를 선택하세요 → Enter")

        for index, menu in enumerate(menus):
            screen.addstr(index + 10, 0, menu, curses.A_REVERSE if index == selected else curses.A_NORMAL)

        screen.refresh()

        key = screen.getch()

        if key == curses.KEY_UP:
            selected = (selected - 1) % len(menus)
        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % len(menus)
        elif key in [curses.KEY_ENTER, 10, 13]:
            if selected == 0:
                edit_settings(screen, config, config_path)
            elif selected == 1:
                show_future_assets(screen, config)
            elif selected == 2:
                show_goal_date(screen, config)
            else:
                break


if __name__ == "__main__":
    curses.wrapper(main)
