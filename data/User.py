#!/usr/bin/env python3
#
# Copyright (C) 2023
#			Written by Nasrun (Nas) Hayeeyama
#

########################################################
#
#	STANDARD IMPORTS
#

########################################################
#
#	LOCAL IMPORTS
#

from uuid import UUID
from .Entity import Entity

########################################################
#
#	GLOBALS
#

########################################################
#
#	EXCEPTION DEFINITIONS
#

########################################################
#
#	HELPER FUNCTIONS
#

########################################################
#
#	CLASS DEFINITIONS
#

class User( Entity ):
    ''' User entity
    '''

    def __init__( self, uuid: UUID, name: str ) -> None:
        super().__init__( uuid, name )
