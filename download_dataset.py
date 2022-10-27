import dlutils

try:
    dlutils.download.from_google_drive('1pCEBqzQDTJ3PlgdIRBY65jOugJ4xpFi6', directory='/home/t/tianqi/CS4243_proj/dataset')
    # download from segmentation mask from drive
    # dlutils.download.from_google_drive('1pCEBqzQDTJ3PlgdIRBY65jOugJ4xpFi6', directory='/home/t/tianqi/CS4243_proj/dataset')
    # download pose from drive
except IOError:
    print("download failed")