import subprocess
import sys
import elevate

def abrir_powershell_admin():
    elevate.elevate()

    titulo = "ubuntu server"

    subprocess.run([
        "powershell.exe",
        "-NoExit",
        "-Command",
        f"$Host.UI.RawUI.WindowTitle = '{titulo}'; Set-Location -Path '{sys.path[0]}'"
    ])

if __name__ == "__main__":
    abrir_powershell_admin()

