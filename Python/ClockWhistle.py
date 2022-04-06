import sys 
import webbrowser
from datetime import datetime
def main():
    while True:
        now =datetime.now().strftime("%I:%M %p")
        if now =='08:51 PM':
            webbrowser.open('https://www.youtube.com/watch?v=3NB1unaiLPI&list=RD3NB1unaiLPI&start_radio=1')
            sys.exit(0)
if __name__ == "__main__":
    main()