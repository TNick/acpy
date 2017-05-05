# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AcPy
                                 A QGIS plugin
 Useful tools for cadaster and topography
                             -------------------
        begin                : 2017-05-05
        copyright            : (C) 2017 by Nicu Tofan
        email                : nicu.tofan@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AcPy class from file AcPy.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ac_py import AcPy
    return AcPy(iface)
