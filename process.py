#%% Get all the folder in Economist path
import os

def return_dirs(path):
    r_dirs = []
    for root, dirs, _ in os.walk(path):
        for name in dirs:
            if name.startswith("2020"):
                r_dirs.append(os.path.join(root,name))
        break
    return r_dirs

dir_list = return_dirs(".")

# %%
# for dir in dirs:
from pdf2image import convert_from_path

# dir_list = [".\\20190105"]
for dir in dir_list:
    for root, dirs, files in os.walk(dir):
        date = dir[2:]  # get the date from the folder name
        # Rename eupb, pdf, mobi file name
        for name in files:
            filetype = name.split(".")[-1]
            file_path = os.path.join(root, name)
            target_file_path = os.path.join(root, "The_Economist_{}.{}".format(date, filetype))
            if file_path != target_file_path:
                os.rename(file_path, target_file_path)
        # Rename the audio folder
        for name in dirs:
            folder_path = os.path.join(root, name)
            target_audio_path = os.path.join(root, "The_Economist_{}_Audio".format(date))
            os.rename(folder_path, target_audio_path)

        # get cover and special report page if any
        savePageList = [1]
        pageFlag = [""]
        # savePageList = [1, 43]
        # pageFlag = ["", "_SP"]
        pdf_path = os.path.join(root, "The_Economist_{}.{}".format(date, "pdf"))
        for i, pageNum in enumerate(savePageList):
            try:
                png_path = os.path.join(".\\Image", "The_Economist_{}{}.{}".format(date, pageFlag[i], "png"))
                if os.path.exists(png_path):
                    break
                page = convert_from_path(pdf_path, dpi=70, first_page=pageNum, last_page=pageNum+1)[0]
                page.save(png_path, 'PNG')
                print("Saved: " + png_path)
            except:
                pass
        break

# %%
