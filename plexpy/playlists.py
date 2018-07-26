# This file is part of Tautulli.
#
#  Tautulli is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Tautulli is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Tautulli.  If not, see <http://www.gnu.org/licenses/>.

import json
import os

import plexpy
import common
import database
import datatables
import helpers
import logger
import plextv
import pmsconnect
import session
from pprint import pprint, pformat

def refresh_playlists():
    logger.info(u"Tautulli Playlists :: Requesting playlists list refresh...")

    server_id = plexpy.CONFIG.PMS_IDENTIFIER
    if not server_id:
        logger.error(u"Tautulli Playlists :: No PMS identifier, cannot refresh playlists. Verify server in settings.")
        return

    playlists = pmsconnect.PmsConnect().get_playlists_list()

    logger.info(u"Tautulli Playlists :: " + pformat( playlists ) )