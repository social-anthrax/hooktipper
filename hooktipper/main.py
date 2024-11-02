import os
import pathlib
import sys
import webbrowser
from functools import partial

from pytermgui import Button, Container, Splitter, Window, WindowManager, palette

# Setup config for TUI

palette.regenerate(primary="#87cefa")

Button.relative_width = 1


def open_payment_page(url: str, _: Button):
    webbrowser.open_new(url)
    sys.exit(0)


def run_hook_script():
    """
    This is necessary as otherwise we cannot read and write to /dev/tty, so we use this as a cursed entry point into exec.sh, which then will enter into main.sh
    """
    exec_file_path = pathlib.Path(__file__).resolve().parent / "exec.sh"
    os.system(f"{exec_file_path} {' '.join(sys.argv[1:])}")


def main():
    # Parse the amounts and donation URL
    donations = {
        a.removeprefix("--"): v for a, v in (x.split("=") for x in sys.argv[1:])
    }

    try:
        custom_url = donations.pop("custom")
    except KeyError:
        print("No Custom Tip amount specified", file=sys.stderr)
        sys.exit(1)

    # Load the UI
    with WindowManager() as manager:
        container = Container(
            "[bold] Would you like to leave a tip?",
            "",
            Splitter(
                *(
                    Button(
                        f"${amount}",
                        onclick=partial(open_payment_page, payment_url),
                    )
                    for amount, payment_url in donations.items()
                )
            ),
            "",
            Button(
                "Custom Tip Amount",
                partial(
                    open_payment_page,
                    custom_url,
                ),
                centered=True,
            ),
            "",
            Button("Skip", onclick=lambda _: sys.exit(0)),
        )
        window = Window(container).set_title("Tip").center()

        manager.add(window)


if __name__ == "__main__":
    main()
