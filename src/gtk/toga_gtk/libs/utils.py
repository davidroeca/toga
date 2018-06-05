from gi.repository import Gtk
from toga.constants import *


try:
    text = unicode
except NameError:
    text = str


def gtk_alignment(alignment):
    "Convert Toga alignments in to arguments compatible with Gtk.set_alignment"
    return {
        LEFT: Gtk.Align.START,
        RIGHT: Gtk.Align.END,
        CENTER: Gtk.Align.CENTER,
        JUSTIFY: Gtk.Align.FILL,
    }[alignment]
