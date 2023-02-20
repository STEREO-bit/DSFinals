# System Specifications
WIDTH = 800
HEIGHT = 640
VOLUME = 0.5
FPS = 120
TITLE = "Bug TIME Rush"

# Fonts
UNDERTALEFONT = "Determination.otf"
LCDFONT = "LCD.ttf"


# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (200,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WIN10BLUE = (0,120,215)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
GREY = (50,50,50)

# Tile Size
TILESIZE = 64
GRIDW = WIDTH / TILESIZE
GRIDH = HEIGHT / TILESIZE

# Player Settings
PLAYER_SPEED = 200

# Zombie Settings
ZOMBIE_SPEED = 150
ZOMBIE_RADIUS = 400

# Turret Settings
TURRET_RADIUS = 400
TURRET_COOLDOWN = 2000
BULLET_SPEED = 350 
BULLET_SPAN = 3000
BULLETS_PER_TICK = 3
SHOOT_EVERY = 200

# ============= SPRITES FILES =============

# Player Sprites
PLAYER_STAND = "frisk.png"

PLAYER_WALK_N_0 = "frisk_0u.png"
PLAYER_WALK_N_1 = "frisk_1u.png"
PLAYER_WALK_N_2 = "frisk_2u.png"
PLAYER_WALK_N_3 = "frisk_3u.png"

PLAYER_WALK_S_0 = "frisk_0d.png"
PLAYER_WALK_S_1 = "frisk_1d.png"
PLAYER_WALK_S_2 = "frisk_2d.png"
PLAYER_WALK_S_3 = "frisk_3d.png"

PLAYER_WALK_W_0 = "frisk_0l.png"
PLAYER_WALK_W_1 = "frisk_1l.png"
PLAYER_WALK_W_2 = "frisk_2l.png"
PLAYER_WALK_W_3 = "frisk_3l.png"

PLAYER_WALK_E_0 = "frisk_0r.png"
PLAYER_WALK_E_1 = "frisk_1r.png"
PLAYER_WALK_E_2 = "frisk_2r.png"
PLAYER_WALK_E_3 = "frisk_3r.png"

# Zombie Sprites
ZOMBIE_STAND = "zombie.png"

ZOMBIE_FRAME_0 = "zombie_1.png"
ZOMBIE_FRAME_1 = "zombie_1.png"
ZOMBIE_FRAME_2 = "zombie_2.png"
ZOMBIE_FRAME_3 = "zombie_3.png"
ZOMBIE_FRAME_4 = "zombie_4.png"
ZOMBIE_FRAME_5 = "zombie_5.png"
ZOMBIE_FRAME_6 = "zombie_6.png"

# Turret Sprites
TURRET_STAND = "turret.png"
BULLET_IMG = "bullet.png"

# Number Tile Sprites
ZERO =  "0.png"
ONE =   "1.png"
TWO =   "2.png"
THREE = "3.png"
FOUR =  "4.png"
FIVE =  "5.png"
SIX =   "6.png"
SEVEN = "7.png"
EIGHT = "8.png"
NINE =  "9.png"
TEN =   "10.png"

# Arithmetic Tile Sprites
PLUS = "+.png"
MINUS = "-.png"
CROSS = "X.png"
OBELUS = "D.png"

# Current Equipped Arithmetic Tile Sprites
CUR_PLUS = "cur_+.png"
CUR_MINUS = "cur_-.png"
CUR_CROSS = "cur_X.png"
CUR_OBELUS = "cur_D.png"

# Score, Objective, and Timer HUD Sprites
SCORE_HUD = "cur_score.png"
TIMER_HUD = "cur_timer.png"
OBJECTIVE_HUD = "cur_objective.png"

# Block Sprites
BLOCK = "block.png"
CHEST = "chest.png"

# Key Sprites
KEY_FRAME_0 = "key_0.png"
KEY_FRAME_1 = "key_1.png"
KEY_FRAME_2 = "key_2.png"
KEY_FRAME_3 = "key_3.png"

# Finish Sprites
FINISH_LOCKED = "finish_l.png"
FINISH_OPENED = "finish_o.png"

# Lives Sprites
LIVES3 = "3lives.png"
LIVES2 = "2lives.png"
LIVES1 = "1lives.png"
MORELIVES = "morelives.png"
FLASHLIGHT = "flashlight.png"

# Radio Sprites
RADIO_ON = "portal_radio_on.png"
RADIO_OFF = "portal_radio_off.png"
RADIO_NONE = "portal_radio_none.png"

TITLE_BG = "title_bg.png"
TITLE_0 = "title_0.png"
TITLE_1 = "title_1.png"
TITLE_2 = "title_2.png"
TITLE_3 = "title_3.png"
TITLE_4 = "title_4.png"
TITLE_5 = "title_5.png"
TITLE_6 = "title_6.png"
TITLE_7 = "title_7.png"

LEVEL_0 = "lvltext_0.png"
LEVEL_1 = "lvltext_1.png"
LEVEL_2 = "lvltext_2.png"
LEVEL_3 = "lvltext_3.png"
LEVEL_4 = "lvltext_4.png"
LEVEL_5 = "lvltext_5.png"
LEVEL_6 = "lvltext_6.png"
LEVEL_7 = "lvltext_7.png"

PORT_0 = "port_0.png"
PORT_1 = "port_1.png"
PORT_2 = "port_2.png"
PORT_3 = "port_3.png"
PORT_4 = "port_4.png"
PORT_5 = "port_5.png"
PORT_6 = "port_6.png"
PORT_7 = "port_7.png"
PORT_SECRET = "port_8.png"


INSTRUCTIONS = "instructions.png"

TUTORIAL = "tutorial_hitbox.png"


# ============= SOUND FILES =============

# Sound Files
PICK = "pick.wav"
SIGN = "sign.wav"
HURT = "hurt.wav"
NOPE = "nope.wav"
NEXT = "next.wav"
DETECT = "!.wav"
KEYSPAWNED = "bell.wav"
KEYGET = "grab.wav"
SHOOT = "arrow.wav"
EXPLODE = "explode.wav"
BSOD = "bluescreen.wav"
PAUSE = "pause.wav"
START = "start.wav"
RADIOGET = "radioget.wav"
TUTORIALTIP = "tip.wav"

# Music Files
STORY = "mus_story.ogg"
TITLEBGM = "title.ogg"
BGM = "mus_core.ogg"
GAMEOVER = "gameover.ogg"
PORTAL = "85.2.wav"
MORSE = "morse.wav"