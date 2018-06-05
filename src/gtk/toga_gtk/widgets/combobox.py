from gi.repository import Gtk
from travertino.size import at_least

from .base import Widget


class ComboBox(Widget):

    def create(self):
        self.native = Gtk.ComboBoxText.new_with_entry()
        self.native.interface = self.interface
        self.native.connect('changed', self._on_change)
        self.native.connect('show', lambda event: self.rehint())

    def _on_change(self, widget):
        if self.interface.on_change:
            self.interface.on_change(self.interface)

    def remove_all_items(self):
        self.native.remove_all()

    def add_item(self, item):
        self.native.append_text(item)

    def set_placeholder(self, value):
        entry = self.native.get_child()
        entry.set_placeholder_text(value)

    def get_value(self):
        return self.native.get_active_text()

    def set_value(self, value):
        entry = self.native.get_child()
        entry.set_text(value)

    def set_font(self, value):
        self.interface.factory.not_implemented('ComboBox.set_font()')

    def set_alignment(self, value):
        self.interface.factory.not_implemented('ComboBox.set_alignment()')

    def rehint(self):
        width = self.native.get_preferred_width()
        height = self.native.get_preferred_height()

        self.interface.intrinsic.width = at_least(self.interface.MIN_WIDTH)
        self.interface.intrinsic.height = height[1]

    def set_on_change(self, handler):
        '''No special handling required'''
