def say_hi():
    print("HI!")


__all__ = ["say_hi"]

try:
    from cable_experiments import science

    __all__ += ["science"]


except ImportError:
    pass
