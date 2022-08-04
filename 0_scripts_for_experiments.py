import os

#if you want to clean the data, run this block of code, remember to change the parameters first
data_type = 'KDD99'
success_or_failure = os.system(
    'python '+'1_data_cleaning_'+data_type+'.py')
print(success_or_failure)

#if you want to do a benchmark resampling, run this block of code, remember to change the parameters first
data_type = 'kdd99'
resampling_type = 'smote'
resampling_ratio = 0.01
success_or_failure = os.system(
    'python '+'2_benchmark_data_resampling.py'+' '+data_type+' '+resampling_type+' '+str(resampling_ratio))
print(success_or_failure)

#if you want to do all types of benchmark resampling, run this block of code, remember to change the parameters first
data_type_list = ['kdd99','nb15']
resampling_type_list = ['no_resampling', 'random_oversampling', 'smote', 'borderlinesmote', 'adasyn']
resampling_ratio_list = [0.01, 0.05, 0.1]
for data_type in data_type_list:
    for resampling_type in resampling_type_list:
        for resampling_ratio in resampling_ratio_list:
            success_or_failure = os.system(
                'python '+'2_benchmark_data_resampling.py'+' '+data_type+' '+resampling_type+' '+str(resampling_ratio))
            print(success_or_failure)

#if you want to do vae resampling, run this block of code, remember to change the parameters first
data_type_list = ['kdd99']
resampling_type_list = ['vae']
resampling_ratio_list = [0.01]
version = '20220803_1'
for data_type in data_type_list:
    for resampling_type in resampling_type_list:
        for resampling_ratio in resampling_ratio_list:
            success_or_failure = os.system(
                'python '+'3_vae_data_resampling.py'+' '+data_type+' '+resampling_type+' '+str(resampling_ratio)+' '+version)
            print(success_or_failure)

#if you want to do a classification, run this block of code, remember to change the parameters first
data_type_list = ['kdd99']
resampling_type_list = ['no_resampling']
resampling_ratio_list = [0.01]
version = '20220803_1'
for data_type in data_type_list:
    for resampling_type in resampling_type_list:
        for resampling_ratio in resampling_ratio_list:
            success_or_failure = os.system(
                'python '+'4_data_classification.py'+' '+data_type+' '+resampling_type+' '+str(resampling_ratio)+' '+version)
            print(success_or_failure)


#if you want to do all types of classification, run this block of code, remember to change the parameters first
data_type_list = ['kdd99','nb15']
resampling_type_list = ['no_resampling', 'random_oversampling', 'smote', 'borderlinesmote', 'adasyn']
resampling_ratio_list = [0.01, 0.1]
version = '20220803_1'
for data_type in data_type_list:
    for resampling_type in resampling_type_list:
        for resampling_ratio in resampling_ratio_list:
            success_or_failure = os.system(
                'python '+'4_data_classification.py'+' '+data_type+' '+resampling_type+' '+str(resampling_ratio)+' '+version)
            print(success_or_failure)