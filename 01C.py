# hello_python.py

import sys
import platform

print("Hello, BonicBot!")

print(
    f"You're running Python "
    f"{sys.version_info.major}."
    f"{sys.version_info.minor}."
    f"{sys.version_info.micro}"
)

print("Operating System:", platform.system())
