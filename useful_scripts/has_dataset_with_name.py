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
This script returns true if dataset exists with given name
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

    client = scripts.client('has_dataset_with_name.py', """This script returns true if dataset exists, false otherwise""",
 
        scripts.String(
        "dataset_name", optional=False,
        description="Dataset name",
        values=rstring('Dataset'), default=""),

        version = "0.1",
        authors = ["Ivan E. Cao-Berg"],
        institutions = ["Carnegie Mellon University"],
        contact = "icaoberg@andrew.cmu.edu",
    )

    conn = BlitzGateway(client_obj=client)

    # Do work here including calling functions
    # defined above.

    client.setOutput("Message", rstring("Success"))

    # process the list of args above.
    scriptParams = {}
    for key in client.getInputKeys():
        if client.getInput(key):
            scriptParams[key] = client.getInput(key, unwrap=True)

    print scriptParams

    if not conn.isConnected():
        message = "Unable to connect to OMERO.server" 
        raise warning( message, UserWarning )
        client.closeSession()
        
    try:
        if not conn.getObject( "Dataset", attributes={'name': name } ):
            client.closeSession()
            print False
        else:
            client.closeSession()
            print True
    except:
        message = "Found more than one dataset with the matching name" 
        raise warning( message, UserWarning )
        client.closeSession()
        print True
    finally:
        client.closeSession()
