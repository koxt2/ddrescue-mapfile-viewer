"""Standalone launcher: python -m ddrescue_health [MAPFILE]"""
import sys

import gi

gi.require_version("Adw", "1")
from gi.repository import Adw, Gio  # noqa: E402

from .ui import MapHealthWindow  # noqa: E402


class HealthApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="com.github.koxt2.datarecovery.Health",
                         flags=Gio.ApplicationFlags.HANDLES_OPEN)

    def do_activate(self):
        (self.props.active_window or MapHealthWindow(self)).present()

    def do_open(self, files, _n, _hint):
        for f in files:
            MapHealthWindow(self, path=f.get_path()).present()


def main(argv=None) -> int:
    return HealthApp().run(sys.argv if argv is None else argv)


if __name__ == "__main__":
    sys.exit(main())
