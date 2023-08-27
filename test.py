# test_ascii_art.py

import subprocess

from video_flow.operation import activate_virtualenv_command

WRAPPER_PROGRAM = "python run.py"
TARGET_PROGRAM = "python ascii_art.py"

SOURCE = "media/images/input/milo.png"
DESTINATION = "media/images/output/ascii_milo.png"

def main() -> None:
    """Tests the main functionalities of the program."""

    commands = (
        [
            activate_virtualenv_command(),
            (
                f"{TARGET_PROGRAM} "
                f"--source_image={SOURCE} "
                f"--destination_ascii_image={DESTINATION}"
            )
        ]

    )

    command = ' & '.join(commands)
    command = f"{WRAPPER_PROGRAM} {command}"

    subprocess.Popen(command)
# end main

if __name__ == '__main__':
    main()
# end if