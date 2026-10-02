"""GTK4/Libadwaita viewer for GNU ddrescue map files.

Embedding::

    from ddrescue_health import show_map_window, MapHealthView, load_mapfile
"""
from .mapfile import MapFile, MapFileError, Status, load_mapfile

__all__ = [
    "MapFile", "MapFileError", "Status", "load_mapfile",
    "MapHealthView", "MapHealthWindow", "show_map_window",
]


def __getattr__(name):
    # Lazy so the parser can be used without GTK installed.
    if name in ("MapHealthView", "MapHealthWindow", "show_map_window"):
        from . import ui
        return getattr(ui, name)
    raise AttributeError(name)
