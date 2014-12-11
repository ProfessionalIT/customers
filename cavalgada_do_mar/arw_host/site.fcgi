#! /usr/bin/env python
import sys
altpath=sys.path
sys.path = ['/home/cavalgad/webapps']
sys.path += altpath

import code
code.webapp.run()
