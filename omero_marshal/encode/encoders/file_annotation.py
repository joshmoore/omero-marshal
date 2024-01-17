#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2024 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from ... import SCHEMA_VERSION
from .annotation import AnnotationEncoder
from omero.model import FileAnnotationI


class FileAnnotation201501Encoder(AnnotationEncoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01' \
        '#FileAnnotation'

    def encode(self, obj):
        v = super(FileAnnotation201501Encoder, self).encode(obj)
        if obj.file is not None and obj.file.isLoaded():
            # TODO: if not loaded, list ID?
            encoder = self.ctx.get_encoder(obj.file.__class__)
            self.set_if_not_none(
                v, 'Value', encoder.encode(obj.file)
            )
        return v

class FileAnnotation201606Encoder(FileAnnotation201501Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06' \
        '#FileAnnotation'


if SCHEMA_VERSION == '2015-01':
    encoder = (FileAnnotationI, FileAnnotation201501Encoder)
elif SCHEMA_VERSION == '2016-06':
    encoder = (FileAnnotationI, FileAnnotation201606Encoder)
FileAnnotationEncoder = encoder[1]
