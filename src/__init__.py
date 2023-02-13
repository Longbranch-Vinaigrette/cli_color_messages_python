# Console colors
class clr:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class palette:
    """A more complete pallete of colors"""
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    # These two actually blink, lmao
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'
    INVISIBLE = '\33[08m'
    STRIKETHROUGH = '\33[09m'

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'

    CGREYBG = '\33[100m'
    CREDBG2 = '\33[101m'
    CGREENBG2 = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2 = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2 = '\33[106m'
    CWHITEBG2 = '\33[107m'


def print_header(msg: str):
    """Print header message"""
    print(f"{clr.HEADER}{msg}{clr.ENDC}")


def print_ok_blue(msg: str):
    """Print an ok message"""
    print(f"{clr.OKBLUE}{msg}{clr.ENDC}")


def print_ok_cyan(msg: str):
    """Print ok message with cyan ocolor"""
    print(f"{clr.OKCYAN}{msg}{clr.ENDC}")


def print_ok_green(msg: str):
    """Print an ok message"""
    print(f"{clr.OKGREEN}{msg}{clr.ENDC}")


def print_warning(msg: str):
    """Print warning message"""
    print(f"{clr.WARNING}{msg}{clr.ENDC}")


def print_error(msg: str):
    """Print an error"""
    print(f"{clr.FAIL}{msg}{clr.ENDC}")


def print_bold(msg: str):
    """Print message in bold"""
    print(f"{clr.BOLD}{msg}{clr.ENDC}")


def print_underline(msg: str):
    """Print message in underline"""
    print(f"{clr.UNDERLINE}{msg}{clr.ENDC}")


def print_strikethrough(msg: str):
    """Print strikethrough"""
    print(f"{palette.STRIKETHROUGH}{msg}{clr.ENDC}")


def print_itallic(msg: str):
    """Print itallic"""
    print(f"{palette.CITALIC}{msg}{clr.ENDC}")


def print_blink(msg: str):
    """Print a message that actually blinks"""
    print(f"{palette.CBLINK}{msg}{clr.ENDC}")




























