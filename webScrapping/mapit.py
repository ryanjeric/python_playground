# mapit.py
import webbrowser,sys,pyperclip
#webbrowser.open('http://automatetheboringstuff.com')
# True
sys.argv # ['mapit.py','870','Valencia','St.]

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py','870','Valencia','St.] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    # Clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)