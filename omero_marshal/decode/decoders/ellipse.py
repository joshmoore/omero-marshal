#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from .shape import ShapeDecoder
from omero.model import EllipseI


class EllipseDecoder(ShapeDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#Ellipse'

    OMERO_CLASS = EllipseI

    def decode(self, data):
        v = super(EllipseDecoder, self).decode(data)
        v.cx = self.to_rtype(data.get('X'))
        v.cy = self.to_rtype(data.get('Y'))
        v.rx = self.to_rtype(data.get('RadiusX'))
        v.ry = self.to_rtype(data.get('RadiusY'))
        return v

decoder = (EllipseDecoder.TYPE, EllipseDecoder)
