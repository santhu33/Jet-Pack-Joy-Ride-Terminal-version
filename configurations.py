import time


# color escape sequences
colors = {
    'Blue': '\x1b[0;34m',
    'Green': '\x1b[0;32m',
    'Cyan': '\x1b[0;36m',
    'Red': '\x1b[0;31m',
    'Purple': '\x1b[0;35m',
    'Brown': '\x1b[0;33m',
    'Gray': '\x1b[0;37m',
    'Light Green': '\x1b[1;32m',
    'Light Cyan': '\x1b[1;36m',
    'Yellow': '\x1b[1;33m',
    'White': '\x1b[1;37m'
}
RESET = '\x1b[0m'

num_magnet= -1

coinpos = []
beamsh=[]
beamsv=[]
beamss=[]
magnets=[]
boost=[]
bulletpos=[]
iceball=[]


coin=colors['Yellow']+'$'+RESET
beam1=colors['Red'] +'*' +RESET
beam2=colors['Blue']+'%' + RESET
ground=colors['Brown']+'#' + RESET
magnet=colors['Red']+'%'+RESET
powerup=colors['Light Cyan']+'>'+RESET
bullet=colors['Gray']+'-'+RESET
iceballcolor=colors['Blue']+"o"+RESET

head = colors['Yellow'] + chr(213) + RESET
mid = colors['Red'] + '|' + RESET
left = colors['Purple'] + '/' + RESET
right = colors['Purple'] + '\\' + RESET
