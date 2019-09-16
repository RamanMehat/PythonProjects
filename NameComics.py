# NameComics.py

""" This Python Script Will re-name Comic files """

# Import Statement
import os
import re


def main():
    """
    Main Function, which will re-name comics to desired format.
    ### Comic Name.pdf
    """
    directory = "/Users/ramanmehat/Desktop/Re-name Comics"
    remove_unwanted_stings(directory)
    rearrange_comic_issue_number(directory)


def remove_unwanted_stings(directory):
    """ This function will remove any un-wanted strings from the comic name"""
    for fileName in os.listdir(directory):
        src = os.path.join(directory, fileName)
        if "GetComics.INFO" in fileName:
            new_file_name = fileName.replace("GetComics.INFO", "").replace(' .pdf', '.pdf')
            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)

        elif "(Webrip) (The Last Kryptonian-DCP)" in fileName:
            new_file_name = fileName.replace("(Webrip) (The Last Kryptonian-DCP)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)

        elif "(The Last Kryptonian-DCP)" in fileName:
            new_file_name = fileName.replace("(The Last Kryptonian-DCP)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)

        elif "(BlackManta-Empire)" in fileName:
            new_file_name = fileName.replace("(BlackManta-Empire)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)

        elif "(Son of Ultron-Empire)" in fileName:
            new_file_name = fileName.replace("(Son of Ultron-Empire)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)

        elif "(Digital) (AnHeroGold-Empire)" in fileName:
            new_file_name = fileName.replace("(Digital) (AnHeroGold-Empire)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)

        elif "(Webrip)" in fileName:
            new_file_name = fileName.replace("(Webrip)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)

        elif "(Digital)" in fileName:
            new_file_name = fileName.replace("(Digital)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)

        elif "(digital)" in fileName:
            new_file_name = fileName.replace("(digital)", "").replace(' .pdf', '.pdf')
            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)

    for fileName in os.listdir(directory):
        src = os.path.join(directory, fileName)
        start = fileName.find('(')
        end = fileName.rfind(')')
        if start != -1:
            remove_string = fileName[start: end + 1]
            new_file_name = fileName.replace(remove_string, '').replace(' .pdf', '.pdf')
            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)

    for fileName in os.listdir(directory):
        src = os.path.join(directory, fileName)
        start = fileName.find('v')
        start2 = fileName.find('V')
        end = start + 2
        end2 = start2 + 2
        if start != -1 and int(start + 1):
            remove_string = fileName[start: end + 1]
            new_file_name = fileName.replace(remove_string, '').replace(' .pdf', '.pdf')
            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)

        elif start2 != -1 and int(start + 1):
            remove_string = fileName[start2: end2 + 1]
            new_file_name = fileName.replace(remove_string, '').replace(' .pdf', '.pdf')
            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)


def rearrange_comic_issue_number(directory):
    """ This function will put the comic issue number at the front of the comic name"""
    new_file_name = []
    for fileName in os.listdir(directory):
        src = os.path.join(directory, fileName)
        comic_issue = re.findall(r'\d+', fileName)
        if len(comic_issue) is 1:
            intermediate_file_name = fileName.replace(comic_issue[0], "").replace(' .pdf', '.pdf')
            if len(comic_issue[0]) >= 3:
                new_file_name = comic_issue[0] + ' ' + intermediate_file_name

            elif len(comic_issue[0]) is 2:
                new_file_name = '0' + comic_issue[0] + ' ' + intermediate_file_name

            elif len(comic_issue[0]) is 1:
                new_file_name = '00' + comic_issue[0] + ' ' + intermediate_file_name

            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)

        elif len(comic_issue) is 2:
            intermediate_file_name = fileName.replace(comic_issue[1], "").replace(' .pdf', '.pdf')
            if len(comic_issue[1]) >= 3:
                new_file_name = comic_issue[1] + ' ' + intermediate_file_name

            elif len(comic_issue[1]) is 2:
                new_file_name = '0' + comic_issue[1] + ' ' + intermediate_file_name

            elif len(comic_issue[1]) is 1:
                new_file_name = '00' + comic_issue[1] + ' ' + intermediate_file_name

            dst = os.path.join(directory, new_file_name)
            os.rename(src, dst)

        elif len(comic_issue) is 0:
            pass

        else:
            print("Lets Go Man To Many Numbers :p")


if __name__ == '__main__':
    # Calling main() function
    main()
