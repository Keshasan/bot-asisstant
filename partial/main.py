import sys

from partial.Jarvis import JarvisCLI

jarvis = JarvisCLI()

commands = sys.argv[1:]

if "record" in sys.argv:  # TODO: change command
    if "add" in sys.argv:
        jarvis.add_record()
    elif "show" in sys.argv:
        jarvis.adress_book.show_all_records()

elif "note" in sys.argv:
    pass
else:
    print("Unknown command.")
