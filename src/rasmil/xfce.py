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

from dasbus.connection import SessionMessageBus
from dasbus.identifier import DBusServiceIdentifier
from gi.repository import GLib

# Constants
XFCONF = DBusServiceIdentifier(
    namespace=("org", "xfce", "Xfconf"),
    message_bus=SessionMessageBus()
)

# Classes


class Xfconf:
    """Wrapper class for the org.xfce.Xfconf Dbus object"""

    def __init__(self):
        self.proxy = XFCONF.get_proxy()

    def get_property(self, channel: str, property: str):
        """ Read a Xfconf property"""
        return self.proxy.GetProperty(channel, property)

    def set_property(self, channel: str, proberty: str, value):
        """ Write a Xfconf property"""
        self.proxy.SetProperty(channel, proberty, value)

    def get_all_properties(self, channel: str, property_base: str):
        """ List all properties under a give property base
        return 
        """
        return self.proxy.GetAllProperties(channel, property_base)
