# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#
import io
from sys import version_info as _python

# introduced in python 3.9
from importlib.resources import files
# .select() was introduced in 3.10
from importlib.metadata import entry_points, EntryPoint as _EntryPoint


def resource_stream(pkg, path):
    print(list(files(pkg).joinpath(f'{path}').iterdir()))
    return io.BytesIO(files(pkg).joinpath(f'{path}').read_bytes())


def iter_entry_points(group, **kwargs):
    return entry_points().select(group=group, **kwargs)


class EntryPoint(_EntryPoint):
    @staticmethod
    def parse(eps):
        return EntryPoint(*map(str.strip, eps.split('=')), None)

    def resolve(self):
        return self.load()
