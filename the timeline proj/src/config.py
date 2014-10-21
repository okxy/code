# Copyright (C) 2009  Rickard Lindberg, Roger Lindberg
#
# This file is part of Timeline.
#
# Timeline is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Timeline is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Timeline.  If not, see <http://www.gnu.org/licenses/>.


"""
Handle application configuration.

This module is global and can be used by all modules. Before accessing
configurations, the read function should be called. To save the current
configuration back to file, call the write method.
"""


import wx
from ConfigParser import ConfigParser
from ConfigParser import DEFAULTSECT
import os.path
from logging import error as logerror


WINDOW_WIDTH = "window_width"
WINDOW_HEIGHT = "window_height"
WINDOW_MAXIMIZED = "window_maximized"
SHOW_SIDEBAR = "show_sidebar"
SHOW_LEGEND = "show_legend"
SIDEBAR_WIDTH = "sidebar_width"
DEFAULTS = {
    WINDOW_WIDTH: "900",
    WINDOW_HEIGHT: "500",
    WINDOW_MAXIMIZED: "False",
    SHOW_SIDEBAR: "True",
    SIDEBAR_WIDTH: "200",
    SHOW_LEGEND: "False"
}


path = None
config = None


def read():
    # Note: wx.App object must have been created before calling this method.
    global path
    global config
    path = os.path.join(wx.StandardPaths.Get().GetUserConfigDir(),
                        ".thetimelineproj.cfg")
    config = ConfigParser(DEFAULTS)
    config.read(path)


def write():
    try:
        f = open(path, "w")
    except IOError, e:
        logerror("Unable to write configuration file to '%s'" % path)
    else:
        config.write(f)
        f.close()


def get_window_size():
    return (config.getint(DEFAULTSECT, WINDOW_WIDTH),
            config.getint(DEFAULTSECT, WINDOW_HEIGHT))


def set_window_size(size):
    width, height = size
    config.set(DEFAULTSECT, WINDOW_WIDTH, str(width))
    config.set(DEFAULTSECT, WINDOW_HEIGHT, str(height))


def get_window_maximized():
    return config.getboolean(DEFAULTSECT, WINDOW_MAXIMIZED)


def set_window_maximized(maximized):
    config.set(DEFAULTSECT, WINDOW_MAXIMIZED, str(maximized))


def get_show_sidebar():
    return config.getboolean(DEFAULTSECT, SHOW_SIDEBAR)


def set_show_sidebar(show):
    config.set(DEFAULTSECT, SHOW_SIDEBAR, str(show))


def get_show_legend():
    return config.getboolean(DEFAULTSECT, SHOW_LEGEND)


def set_show_legend(show):
    config.set(DEFAULTSECT, SHOW_LEGEND, str(show))


def get_sidebar_width():
    return config.getint(DEFAULTSECT, SIDEBAR_WIDTH)


def set_sidebar_width(width):
    config.set(DEFAULTSECT, SIDEBAR_WIDTH, str(width))
