# System Specifications
WIDTH = 800
HEIGHT = 640
FPS = 120
TITLE = "Malaking TITE"
FONT = "Determination.otf"

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
ORANGE = (255,165,0)
GREY = (155,155,155)

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
BULLET_SPEED = 350 
BULLET_SPAN = 1500
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

ZOMBIE_WALK_N_0 = "zombie_0u.png"
ZOMBIE_WALK_N_1 = "zombie_1u.png"
ZOMBIE_WALK_N_2 = "zombie_2u.png"
ZOMBIE_WALK_N_3 = "zombie_3u.png"

ZOMBIE_WALK_S_0 = "zombie_0d.png"
ZOMBIE_WALK_S_1 = "zombie_1d.png"
ZOMBIE_WALK_S_2 = "zombie_2d.png"
ZOMBIE_WALK_S_3 = "zombie_3d.png"

ZOMBIE_WALK_W_0 = "zombie_0l.png"
ZOMBIE_WALK_W_1 = "zombie_1l.png"
ZOMBIE_WALK_W_2 = "zombie_2l.png"
ZOMBIE_WALK_W_3 = "zombie_3l.png"

ZOMBIE_WALK_E_0 = "zombie_0r.png"
ZOMBIE_WALK_E_1 = "zombie_1r.png"
ZOMBIE_WALK_E_2 = "zombie_2r.png"
ZOMBIE_WALK_E_3 = "zombie_3r.png"

# Turret Sprites
TURRET_STAND = "turret.png"
BULLET_IMG = "bullet.png"
# TURRET_ACTIVE_# = "turret_#s.png"

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

# Block Sprites
BLOCK = "block.png"
CHEST = "chest.png"
KEY = "key.png"

# Finish Sprites
FINISH_LOCKED = "finish_l.png"
FINISH_OPENED = "finish_o.png"

# Lives Sprites
LIVES3 = "3lives.png"
LIVES2 = "2lives.png"
LIVES1 = "1lives.png"
MORELIVES = "morelives.png"
FLASHLIGHT = "flashlight.png"

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


# Music Files
TITLEBGM = "title.ogg"
BGM = "mus_core.ogg"
GAMEOVER = "gameover.ogg"