#!/usr/bin/env python3
#
# Copyright (C) 2023
#			Written by Nasrun (Nas) Hayeeyama
#

########################################################
#
#	STANDARD IMPORTS
#

# uuid
from uuid import UUID

########################################################
#
#	LOCAL IMPORTS
#

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

class Entity( object ):
    ''' Base entity of this object
    '''

    def __init__( self, uuid:UUID, name:str ) -> None:
        
        # uuid, all enities should have uuid
        self.uuid = uuid

        # name of entity
        self.name = name

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}( uuid={self.uuid}, name={self.name} )'
