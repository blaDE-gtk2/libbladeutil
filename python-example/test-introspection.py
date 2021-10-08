#!/usr/bin/env python3

# You can generate python documentation with the following commands:
# g-ir-doc-tool --language Python -o ./html ../libbladeutil/libbladeutil-1.0.gir
# yelp ./html/

import gi.repository
# Set the search path to use the newly generated introspection files
gi.require_version('GIRepository', '2.0')
from gi.repository import GIRepository
GIRepository.Repository.prepend_search_path('../libbladeutil/')
# Now import 4util
gi.require_version('libbladeutil', '1.0')
from gi.repository import libbladeutil

# print out some stuff to see if it works
print("homedir: ", libbladeutil.get_homedir())
print("get_dir_localized: ", libbladeutil.get_dir_localized(libbladeutil.get_homedir()))
print("version: ", libbladeutil.version_string())
