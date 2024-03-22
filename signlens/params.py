import os
import numpy as np

##################  VARIABLES  ##################
 # Number of classes to analyze
if os.environ.get("NUM_CLASSES") == 'all':
    NUM_CLASSES = 250
else:
    NUM_CLASSES = int(os.environ.get("NUM_CLASSES"))

# Max number of frames in a sequence. Used to pad sequences, and also filter out sequences
MAX_SEQ_LEN = int(os.environ.get("MAX_SEQ_LEN"))

# Percentage of the data to load
DATA_FRAC = float(os.environ.get("DATA_FRAC"))

##################  CONSTANTS  #####################

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # go 2 levels up
TRAIN_DATA_DIR          = os.path.join(BASE_DIR, 'raw_data', 'asl-signs')
TRAIN_CSV_PATH          = os.path.join(TRAIN_DATA_DIR, 'train.csv')
TRAIN_TRAIN_CSV_PATH    = os.path.join(TRAIN_DATA_DIR, 'train_train.csv')
TRAIN_TEST_CSV_PATH     = os.path.join(TRAIN_DATA_DIR, 'train_test.csv')
LANDMARK_DIR            = os.path.join(TRAIN_DATA_DIR,'train_landmark_files')
LABEL_MAP_PATH          = os.path.join(TRAIN_DATA_DIR,'sign_to_prediction_index_map.json')
GLOSSARY_CSV_PATH       = os.path.join(TRAIN_DATA_DIR, 'glossary.csv')

TRAIN_OUTPUT_DIR        = os.path.join(BASE_DIR, 'training_outputs')


N_LANDMARKS_HAND    = 21
N_LANDMAKRS_POSE    = 33
N_LANDMARKS_FACE    = 468
N_LANDMARKS_ALL     = 543   # N_LANDMARKS_HAND * 2 +  N_LANDMAKRS_POSE + N_LANDMARKS_FACE
N_LANDMARKS_NO_FACE = 75    # N_LANDMAKRS_POSE + 2 * N_LANDMARKS_HAND
