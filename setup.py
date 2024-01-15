from cx_Freeze import setup, Executable

setup(
    name="FloatingClock",
    version="1.0",
    description="Floating Clock App",
    executables=[Executable("floating_clock.py")],
)
