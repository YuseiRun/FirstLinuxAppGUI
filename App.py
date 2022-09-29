 #!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class ourwindow(Gtk.Window):

    def __init__(self):
        self.temp = 72
        Gtk.Window.__init__(self, title="Thermostat")

        hbox = Gtk.Box(spacing= 10)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right.set_homogeneous(False)

        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)
        Gtk.Window.set_default_size(self, 400,325)
        Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)

        self.label = Gtk.Label(label=self.temp)
        self.label.set_justify(Gtk.Justification.CENTER)
        vbox_left.pack_start(self.label, True, True, 0)

        #vbox_left.pack_start(label, True, True, 0)
        buttonDecrease = Gtk.Button()
        buttonDecrease.connect("clicked", self.whenButtonDecrease_clicked)
        buttonIncrease = Gtk.Button()
        buttonIncrease.connect("clicked", self.whenButtonIncreased_clicked)
        vbox_left.pack_start(buttonDecrease, True, True, 0)
        vbox_right.pack_start(buttonIncrease, True, True, 0)

        self.add(hbox)


    def whenButtonDecrease_clicked(self, button):
        self.temp= self.temp-1
        self.label.set_text(str(self.temp))
    def whenButtonIncreased_clicked(self, button):
        self.temp+=1
        self.label.set_text(str(self.temp))


window = ourwindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
