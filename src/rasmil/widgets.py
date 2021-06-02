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
Module with custom Gtk3 Widgets
"""

import os
import sys
import math
import cairo
import time

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('PangoCairo', '1.0')

from gi.repository import Gtk, Gdk, GObject, Pango, PangoCairo

class CircularProgressBar (Gtk.Bin):
    """ Circular Progressbar with text and subtext custom Gtk3 widget """
    
    def __init__ (self, min_diameter: int = 300, line_width: int = 10, paint_center: bool = False):
        """
        :param min_diameter: Minimum diameter of the progressbar
        :param line_width: the thickness of the progress bar
        :param paint_center: paint the inner circle with a custom color       
        """
        Gtk.Bin.__init__(self)
        self._min_diameter = min_diameter
        self._line_width = line_width
        self._fraction = 0.0
        self._text = ""
        self._subtext = ""
        self._center_color = "#000000"
        self._progress_bg_color = "#d3d3d3"
        self._progress_fg_color = "#4a90d9"
        self._paint_center = paint_center
        self._text_font = 'URW Gothic 18'
        self._subtext_font = 'URW Gothic 10'
        self._line_cap = cairo.LineCap.BUTT

    @property
    def radius (self) :
        """ get the effective radius """
        width = float(self.get_allocated_width ()) / 2
        height = (float(self.get_allocated_height ()) / 2) - 1
        return int(min(width, height)) 

    @property
    def diameter (self) :
        """ get the effective diameter """
        return 2 * self.radius
                
    def get_fraction(self):
        """ get the current progress fraction (0.0 -> 1.0) """
        return self._fraction

    def set_fraction_animated(self, from_value: float, to_value: float, frames: int, run_time: float):
        """ Animated progress between 2 fractions 
        
        :param from_value: the start fraction (0.0 - 1.0)
        :param to_value: the end fraction (0.0 - 1.0)
        :param frames: the number for frames
        :param run_time: the total time of the animation
        """
        
        if 0.0 <= from_value <= 1.0 and 0.0 <= to_value <= 1.0:
            delta = (to_value - from_value) / frames
            delay = run_time / frames
            self._fraction = from_value
            self.queue_draw()
            time.sleep(delay)
            for i in range(frames-2):
                self._fraction += delta
                self.queue_draw()
                time.sleep(delay)
            self._fraction = to_value
            self.queue_draw()
        
    def set_fraction(self, value: float):
        """ set the fraction (0.0 -> 1.0)  """
        if 0.0 <= value <= 1.0:
            self._fraction = value
            self.queue_draw()
        else:
            print(f'CircularProgressBar: Illegal fraction : {value}')

    def set_text(self, txt: str, font=None):
        """ Set the main text 
        
        :param txt: the text to write
        :param font: optional font to use Ex. 'URW Gothic 18'
        """
        self._text = txt
        if font:
            self._text_font = font
        self.queue_draw()
        
    def get_text(self) -> str:
        """ get the main text """
        return self._text
    
    def set_subtext(self, txt: str, font=None):
        """ Set the sub text 
        
        :param txt: the text to write
        :param font: optional font to use Ex. 'URW Gothic 18'
        """
        self._subtext = txt
        if font:
            self._subtext_font = font
        self.queue_draw()
        
    def calc_fontsize(self, font: str) -> int: 
        """ get the font size from a font string """
        try:
            fs = font.rsplit(' ', maxsplit=1)[-1]
            size = int(fs)
        except ValueError as e:
            print(f'cant convert : {fs} to an int  ({font})')
            size = 20
        return size
        
    def get_subtext(self) -> str:
        """ Get the current subtext """
        return self._subtext

 #================= Implementation of Gtk.Widget virtual methods ==================
 # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/Widget.html#virtual-methods
 #---------------------------------------------------------------------------------
 
    def do_get_request_mode (self) :
        """ The widget's Size Request Mode  """
        return Gtk.SizeRequestMode.CONSTANT_SIZE

    def do_get_preferred_width (self) :
        """ The widget's preferred width """
        d = self.diameter
        min_w = self._min_diameter
        if d > self._min_diameter :
            natural_w = d
        else :
            natural_w = self._min_diameter
        if d == 0:
            d = self._min_diameter
        return d, natural_w

    def do_get_preferred_height (self) :
        """ The widget's preferred height """
        d = self.diameter
        min_h = self._min_diameter
        if d > self._min_diameter :
            natural_h = d
        else :
            natural_h = self._min_diameter
        if d == 0:
            d = self._min_diameter
        return d, natural_h

    def do_draw (self, cr) :
        """ Draw the widget """
        w = h = 0
        delta = 0
        color = Gdk.RGBA ()
        layout = PangoCairo.create_layout (cr) 
        desc = Pango.FontDescription() 
        
        cr.save ()

        color = Gdk.RGBA ()

        center_x = self.get_allocated_width () / 2
        center_y = self.get_allocated_height () / 2
        radius =  self.radius
        d = radius - self._line_width
        delta = radius - self._line_width / 2
        if d < 0 :
            delta = 0
            self._line_width = radius
        
        color = Gdk.RGBA ()
        cr.set_line_cap  (self._line_cap)
        cr.set_line_width(self._line_width)

        # paint inner cicle
        if self._paint_center == True:
            cr.arc (center_x, center_y, delta, 0, 2 * math.pi)
            color.parse (self._center_color)
            Gdk.cairo_set_source_rgba (cr, color)
            cr.fill ()

        # paint the progress background
        cr.arc (center_x, center_y, delta, 0, 2 * math.pi)
        color.parse (self._progress_bg_color)
        Gdk.cairo_set_source_rgba (cr, color)
        cr.stroke ()

        # paint the progress bar
        progress = float(self._fraction)
        if progress > 0:
            cr.arc (center_x,
                    center_y,
                    delta, 
                    1.5  * math.pi,
                    (1.5 + progress * 2 ) * math.pi)
            color.parse (self._progress_fg_color)
            Gdk.cairo_set_source_rgba (cr, color)
            cr.stroke ()

        # Textual information
        context = self.get_style_context ()
        context.save ()
        context.add_class (Gtk.STYLE_CLASS_TROUGH)
        color = context.get_color (context.get_state ())
        Gdk.cairo_set_source_rgba (cr, color)

        # paint text
        layout = PangoCairo.create_layout (cr)
        layout.set_text (self._text, -1)
        desc = Pango.FontDescription.from_string (self._text_font)
        font_height = self.calc_fontsize(self._text_font)
        layout.set_font_description (desc)
        PangoCairo.update_layout (cr, layout)
        w, h = layout.get_size () 
        cr.move_to (center_x - ((w / Pango.SCALE) / 2), center_y - font_height )
        PangoCairo.show_layout (cr, layout)

        # paint sub-text
        layout.set_text (self._subtext, -1)
        desc = Pango.FontDescription.from_string (self._subtext_font)
        font_height = self.calc_fontsize(self._subtext_font)
        layout.set_font_description (desc)
        PangoCairo.update_layout (cr, layout)
        w, h = layout.get_size () 
        cr.move_to (center_x - ((w / Pango.SCALE) / 2), center_y + font_height)
        PangoCairo.show_layout (cr, layout)

        context.restore ()
        cr.restore ()

GObject.type_register(CircularProgressBar)

