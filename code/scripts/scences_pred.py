#FIX ALL PATHS AND CHANGE FILE NAMES SINCE NOT CORRECT
#PROBABLY WANT TO DO THIS ON CLEANED DATA 
#ADD TESTS 

#Import standard libraries
import numpy as np
import pandas as pd
import nibabel as nib
import matplotlib.pyplot as plt
import data_loading as dl
import plotting_fmri as plt_fmri
import save_files as sv
import numpy.linalg as npl

from sklearn.neighbors import KNeighborsClassifier as KNN 
from scipy.spatial.distance import hamming #MIGHT NOT NEED SOME OF THESE PACKAGES 
                                           #WHEN PUTTIING FUNCS IN UTILS 

#All file strings corresponding to BOLD data for subject 4 

files = ['task001_run001.bold_dico.nii', 'task001_run002.bold_dico.nii', 
         'task001_run003.bold_dico.nii', 'task001_run004.bold_dico.nii', 
         'task001_run005.bold_dico.nii', 'task001_run006.bold.nii',
         'task001_run007.bold.nii', 'task001_run008.bold.nii']

all_data = []
for filename in files:
	new_data = dl.load_all_data(filename) 
	all_data.append(new_data)


scenes_path = './scene_times_nums.csv' #FIX
scenes = pd.read_csv('scene_times_nums.csv', header = None) 
scenes = scenes.values #Now just numpy array

combined_runs = combine_run_arrays(all_data) #FIX AND ADD runi

#We will first check if there are any noticable differences between scenes
#occuring in 'Gump house/room/etc.' vs. all other scenes 

#In this simple example, we let 1 denote a Gump scene and 0 for all other 
#scenes 

#FIX: PUT THESE FUNCTIONS SOMEWHERE IN UTILS

###################################################################
TR = 2
NUM_VOLUMES = combined_runs.shape #3524
ONSET_TIMES = scenes[:,0] 
ONSET_TIMES_NORMED = ONSET_TIMES - 17 
DURATION = scenes[:,1] 
LABELS = scenes[:,3]

def sync_scene_times(labels, onset_times_normed, num_volumes=3524):


def combine_run_arrays(run_array_lst):
	return np.concatenate(run_array_lst, axis = 3)

def train_test_split(vox_by_time, train_times):

def get_scenes(ids):

def other_scene_ids(remove_ids):
	""" Return list of ids that do not contain any ids present in remove_ids. 
    Parameters
    ----------
    remove_ids : list
        This is a list consisting of all ids to remove from the factor 
        scene ids (which consist of ids between 1 - 90 inclusive)      
    Returns
    -------
    other_ids : list
        A list of ids that do not contain the any of the ids in remove_ids
    """
    assert max(remove_ids) < 91 and min(remove_ids) > 0
	all_ids = list(range(1, 91))
	other_ids = [i for i in all_ids if i not in remove_ids]
    return other_ids

def make_scene_design_mat(scenes, times, on_scene_ids):
	synced_times = sync_scene_times(times)

def calc_weights(X, Y):
	return npl.pinv(X).dot(Y)

def get_voxel_weight(vox_by_time, voxel_index, times, on_scene_ids):
	vox_time_course = vox_by_time[voxel_index, times]
	vox_design_mat = make_scene_design_mat(vox_by_time, voxel_index, times, on_scene_ids)
    weights = calc_weights(vox_design_mat, vox_time_course)
    return weights

def get_all_weights(vox_by_time, times, on_scene_ids):
	all_weights = []
	for i in range(vox_by_time.shape[0]):
		weight = get_voxel_weight(vox_by_time, i, times, on_scene_ids)
		all_weights.append(weight)
	all_weights = np.array(all_weights)
	return all_weights

def predict_scene(trained_weights, t_0_activity):
	#ASSERTS HERE FOR DIMENSION?
	design_mat = trained_weights.T
	raw_predicted_scenes = calc_weights(design_mat, t_0_activity)
    largest_index = np.where(raw_predicted_scenes == max(raw_predicted_scenes))
    return largest_index #FIX what if there are ties 

def predict_all_times(trained_weights, test_activities):
    predicted_indces = []
	for activity in test_activities:
		index = predict_scene(trained_weights, activity)
	return predicted_indces

def analyze_performance(predicted_labels, actual_labels): 
	normed_distance = hamming(predicted_labels, actual_labels) #between 0 - 1
	return 1 - normed_distance
    


###################################################################

GUMP_SCENES_IDS = [38, 40, 41, 42] #factor ids of Gump scenes
other_scenes = other_scene_ids(GUMP_SCENES_IDS)



#Next we will look at political scenes vs. non-political scenes 

#Here we investigate outdoors vs. indoor scenes 

#The following compares the 6 major scenes in the film 





