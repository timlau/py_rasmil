#    Copyright (C) 2021 Tim Lauridsen < tla[at]rasmil.dk >
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to
#    the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

"""
Demo code for the CircularProgressBar custom Gtk3 widget
"""

import os
import sys
import threading
import time

import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

from widgets import CircularProgressBar

class GUI (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(400,400)
        self.pb = CircularProgressBar(min_diameter = 200)
        self.pb.set_text("Downloading", font = 'URW Gothic 18' )
        self.pb.set_subtext("foobar-tooteloo-1.2.3-12.fc34.noarch", font = 'Noto Sans Condensed Regular 12')
        self.connect('destroy', self.on_window_destroy)
        self.add(self.pb)
        self.show_all()
        self.start_timer()
        
    def update_progress(self):
        while not self.event.is_set():
            self.pb.set_fraction_animated(0.0, 1.0, 180, 5)
            time.sleep(1)
 
    def start_timer(self):
        print('starting thread')
        self.timer = threading.Thread(target=self.update_progress)
        self.event = threading.Event()
        self.timer.daemon=True
        self.timer.start() 
        

    def on_window_destroy(self, window):
        Gtk.main_quit()

def main():
    app = GUI()
    Gtk.main()
        
if __name__ == "__main__":
    sys.exit(main())
