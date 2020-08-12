import sys, webbrowser, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open(
    'https://google.com/maps/place/' + address)

