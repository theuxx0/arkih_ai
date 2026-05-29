from themes.dark_blue import STYLE as DARK_BLUE
from themes.neon_purple import STYLE as NEON_PURPLE


def apply_theme(window, theme_name):

    themes = {
        "dark_blue": DARK_BLUE,
        "neon_purple": NEON_PURPLE
    }

    style = themes.get(theme_name, DARK_BLUE)

    window.setStyleSheet(style)