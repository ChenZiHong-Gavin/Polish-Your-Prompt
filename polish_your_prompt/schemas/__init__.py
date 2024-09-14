from .schema import Schema
from .APE import APE
from .BROKE import BROKE
from .CARE import CARE
from .CHAT import CHAT
from .COSTAR import COSTAR
from .CREATE import CREATE
from .CRISPE import CRISPE
from .ERA import ERA
from .ICIO import ICIO
from .RACE import RACE
from .RISE import RISE
from .ROSES import ROSES
from .RTF import RTF
from .TAG import TAG
from .TRACE import TRACE

SCHEMAS = [
    APE(),
    BROKE(),
    CARE(),
    CHAT(),
    COSTAR(),
    CREATE(),
    CRISPE(),
    ERA(),
    ICIO(),
    RACE(),
    RISE(),
    ROSES(),
    RTF(),
    TAG(),
    TRACE(),
]

__all__ = [
    "Schema",
    "APE",
    "BROKE",
    "CARE",
    "CHAT",
    "COSTAR",
    "CREATE",
    "CRISPE",
    "ERA",
    "ICIO",
    "RACE",
    "RISE",
    "ROSES",
    "RTF",
    "TAG",
    "TRACE",
    "SCHEMAS",
]
