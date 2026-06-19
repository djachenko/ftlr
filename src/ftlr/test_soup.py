from pathlib import Path

from bs4 import BeautifulSoup
from libxmp.utils import file_to_dict



def main():
    path = Path("../../25.03.10.lampost/ZSC_2123.xmp")

    with path.open() as f:
        file = f.read()



    with path.open("w") as f:
        f.write(soup.prettify())

    a = 7


if __name__ == '__main__':
    main()
