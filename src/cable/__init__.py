def say_hi():
    print("HI!")


__all__ = ["say_hi"]

try:
    from cable_cli import get_argument_parser

    __all__ += ["get_argument_parser"]
except ImportError:
    pass
try:
    from cable_experiments import science

    __all__ += ["science"]


except ImportError:
    pass
