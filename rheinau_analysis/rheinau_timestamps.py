import os
import platform

path_to_file = '/Users/sebastian/Dropbox/Rheinau_Plant_Movies_Peter/plants-rheinau-videos'

creation_dates = []

def creation_date(path_to_file):

    stat = os.stat(path_to_file)
    try:
        print(stat.st_birthtime)
        return stat.st_birthtime
    except AttributeError:
        # We're probably on Linux. No easy way to get creation dates here,
        # so we'll settle for when its content was last modified.
        return stat.st_mtime


creation_date('/Users/sebastian/Dropbox/Rheinau_Plant_Movies_Peter/plants-rheinau-videos')