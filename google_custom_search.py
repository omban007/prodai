"""Simple command-line example for Custom Search.

Command-line application that does a search.
"""

__author__ = 'Datta Ban'

import pprint

from googleapiclient.discovery import build


def main():
    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build("customsearch", "v1",
                    developerKey="AIzaSyBj_t61_hnmeo8Uon88ksAPQBi8K-mJGk8")

    res = service.cse().list(
        q='what is a computer',
        cx='013763054840622769275:n8ooxh9v0lu',
    ).execute()
    pprint.pprint(res)


if __name__ == '__main__':
    main()
