#!/usr/bin/env python3

# File: constants.py 
# Description: Basic program constants.
# Author: Pavel Bena?ek <pavel.benacek@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from pygame.locals import *

# Configuration of building shape block
# Width of the shape block
BWIDTH     = 40
# Height of the shape block
BHEIGHT    = 40
# Width of the line around the block
MESH_WIDTH = 2

import screeninfo

# Configuration of the player board
# Board line height
BOARD_HEIGHT     = 10
# Margin of upper line (for score)
BOARD_UP_MARGIN  = 40
# Margins around all lines
BOARD_MARGIN     = 1

# Color declarations in the RGB notation
WHITE    = (255,255,255)
RED      = (247,70,98)
GREEN    = (141,226,71)
BLUE     = (74,125,242)
ORANGE   = (235,129,45)
YELLOW     = (255,255,0)
PURPLE   = (223,82,194)
CYAN     = (66,223,255) 
MAGENTA    = (255,0,255)

# Timing constraints
# Time for the generation of TIME_MOVE_EVENT (ms)
MOVE_TICK          = 500
# Allocated number for the move dowon event
TIMER_MOVE_EVENT   = USEREVENT+1
# Speed up ratio of the game (integer values)
GAME_SPEEDUP_RATIO = 1.5
# Score LEVEL - first threshold of the score
SCORE_LEVEL        = 2000
# Score level ratio
SCORE_LEVEL_RATIO  = 2 

# Configuration of score
# Number of points for one building block
POINT_VALUE       = 100
# Margin of the SCORE string
POINT_MARGIN      = 10

# Font size for all strings (score, pause, game over)
FONT_SIZE           = 25
