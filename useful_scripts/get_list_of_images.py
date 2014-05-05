#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2014 Ivan E. Cao-Berg
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
This script returns a list of the images associated with the current user
"""

import omero
import omero.util.script_utils as scriptUtil

from omero.gateway import BlitzGateway
from omero.rtypes import *

import omero.scripts as scripts
from cStringIO import StringIO
from numpy import *

from warnings import warn as warning
import json

if __name__ == "__main__":

    client = scripts.client('get_list_of_images.py', """This script returns a list of images""",
        version = "0.1",
        authors = ["Ivan E. Cao-Berg"],
        institutions = ["Carnegie Mellon University"],
        contact = "icaoberg@andrew.cmu.edu",
    )

    try:
        conn = BlitzGateway(client_obj=client)

        # Do work here including calling functions
        # defined above.

        client.setOutput("Message", rstring("Success"))
        if not conn.isConnected():
            message = "Unable to connect to OMERO.server" 
            raise warning( message, UserWarning )
            client.closeSession()   
            
        try:
            list_of_images = []
            # connect as above
            for project in conn.listProjects():
                for dataset in project.listChildren():
                    links = dataset.getChildLinks()
                    for image in links:
                        temp = {}
                        temp['iid'] = long(image.getId())
                        temp['name'] = image.getName()
                        list_of_images.append( temp )

            print json.dumps( list_of_images )
        except:
            message = "Unable to retrieve list of images" 
            raise warning( message, UserWarning )
            client.closeSession()   
    finally:
        client.closeSession()
