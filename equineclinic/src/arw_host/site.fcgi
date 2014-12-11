#! /usr/bin/env python
import sys
altpath=sys.path
sys.path = ['/home/equinecl/webapps']
sys.path += altpath

import code
code.webapp.run()
