#%% Import
import requests, zipfile, io, os
from datetime import datetime

#%%
def get_url(year, date, issue):
    # year = 2020, date = 20200620, issue = 9199
    base_url = "http://audiocdn.economist.com/sites/default/files/AudioArchive/"
    url = base_url + "{Year}/{Date}/Issue_{Issue}_{Date}_The_Economist_Full_edition.zip".format(Year = year, Date = date, Issue = issue)
    return url

def get_issue(date):
    base_issue = 9199
    base_date = datetime(2020, 6, 20)
    current_date = datetime.strptime(date, "%Y%m%d")
    return int(base_issue + (current_date - base_date).days / 7)

# print(get_issue("20200418"))
#%% Get all the folder in Economist path
def return_dirs(path):
    r_dirs = []
    for root, dirs, _ in os.walk(path):
        for name in dirs:
            if name.startswith("2020"):
                r_dirs.append(os.path.join(root,name))
        break
    return r_dirs

dir_list = return_dirs(".")

#%%
# dir_list = [".\\20200104"]
today = datetime.today()
current_date = today.strftime("%Y%m%d")
for dir in dir_list:
    for root, dirs, files in os.walk(dir):
        date = dir[2:]
        if (abs(int(current_date) - int(date)) <= 1):
            # Audio available at least Friday, choose the nearest date

            audio_path = os.path.join(dir, "The_Economist_{}_Audio".format(date))

            if not os.path.exists(audio_path):
                os.mkdir(audio_path)
                print("Path {} created!".format(audio_path))
            else:
                print("Path {} already exist!".format(audio_path))
            # Audio zip file url
            audio_url = get_url(year=2020, date=date, issue=get_issue(date))
            print("Preparing download file with url below:\n{}".format(audio_url))
            print("Download begin, please wait!")
            r = requests.get(audio_url)
            print("Download finsihed, begin extract!")
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(audio_path)
            print("Audio extract complete!")
        break
