#KC_Wang
import allrecipes_scraping
import cookpad_scraping
import icookweb_scrapin
import os
import threading
import time

def updated():
    allprogram = {'1':'allrecipes_scraping','2':'cookpad_scraping','3':'icookweb_scrapin'}
    try:
        i=1
        allrecipes_scraping()
        i=2
        cookpad_scraping()
        i=3
        icookweb_scrapin()
    except Exception as g:
        pass
        print("There is an error in this")
        print(allprogram[i])
        print(g)

if __name__ == "__main__":
    main()