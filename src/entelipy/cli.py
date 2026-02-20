"""
cli.py

Provides the command-line entry function (`main`) that creates and runs the `entelipy` TUI.
"""
from .app import EntelipyTUI



def main() -> None:
    app = EntelipyTUI()
    app.run()
