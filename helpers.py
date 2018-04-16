"""
Helper functions for displaying data and making interactive plots.
"""
import numpy as np
import matplotlib.pyplot as plt


def minmax(data, fields):
    """
    Get the minimum and maximum data values out of all fields given.
    Returns them in a dictionary with the 'vmin' and 'vmax' keys.
    """
    vmin = min(data[field].values.min() for field in fields)
    vmax = max(data[field].values.max() for field in fields)
    return dict(vmin=vmin, vmax=vmax)


def plot_field(ax, data, field, cmap=None, gridline_spacing=30, cb_pad=0.03,
               cb_aspect=50, cb_shrink=0.7, title=True, **kwargs):
    """
    Make a pcolormesh plot of the given data field.
    Set's the plot extent and includes ticks in longitude and latitude.
    """
    if title:
        ax.set_title(field)
    if 'add_colorbar' not in kwargs:
        kwargs['cbar_kwargs'] = dict(orientation='horizontal',
                                     aspect=cb_aspect, pad=cb_pad,
                                     shrink=cb_shrink)
    data[field].plot.pcolormesh(ax=ax, add_labels=False, cmap=cmap, **kwargs)
    ax.coastlines()
    w, e, s, n = [data.longitude.min(), data.longitude.max(),
                  data.latitude.min(), data.latitude.max()]
    xlocs = np.arange(w, e + 0.01, gridline_spacing)
    ylocs = np.arange(s, n + 0.01, gridline_spacing)
    ax.gridlines(color="#cccccc55", xlocs=xlocs, ylocs=ylocs)
