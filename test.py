# test_ascii_art.py

from ascii_art import ascii_art

SOURCE = "media/images/input/milo.png"
DESTINATION = "media/images/output/ascii_milo.png"

def main() -> None:
    """Tests the main functionalities of the program."""

    ascii_art(image=SOURCE, image_destination=DESTINATION)
# end main

if __name__ == '__main__':
    main()
# end if