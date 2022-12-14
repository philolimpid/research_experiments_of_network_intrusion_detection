# Introduction of the research of network intrusion detection and imbalanced learning

This is a code repository of a research of network intrusion detection. Our paper is published on Journal of Big Data. 
Please refer to https://doi.org/10.1186/s40537-020-00390-x

## Abstract of our paper
Machine learning plays an increasingly significant role in the building of Network Intrusion Detection Systems. 
However, machine learning models trained with imbalanced 
cyber-security data cannot recognize minority data, hence attacks, effectively. One way 
to address this issue is to use resampling, which adjusts the ratio between the different 
classes, making the data more balanced.  

This research looks at resampling’s influence on the performance of Artificial Neural Network 
multi-class classifiers. The resampling methods, random undersampling, random oversampling, 
random undersampling and random oversampling, random undersampling with Synthetic Minority Oversampling 
Technique, and random undersampling with Adaptive Synthetic Sampling Method 
were used on benchmark Cyber-security datasets, KDD99, UNSW-NB15, UNSW-NB17 
and UNSW-NB18. Macro precision, macro recall, macro F1-score were used to evaluate the results. 

The patterns found were: First, oversampling increases the training 
time and undersampling decreases the training time; second, if the data is extremely 
imbalanced, both oversampling and undersampling increase recall signifcantly; third, 
if the data is not extremely imbalanced, resampling will not have much of an impact; 
fourth, with resampling, mostly oversampling, more of the minority data (attacks) were 
detected.

Keywords: Oversampling, Undersampling, Resampling, Imbalanced Data, Network 
Intrusion Detection Systems, SMOTE, ADASYN, Artifcial Neural Networks, Macro 
precision, Macro recall

## Code description

This comparative study are based on 6 datasets, which are KDD99, UNSW-NB15, UNSW-NB18, UNSW-NB17 danmini, UNSW-NB17 ecobee, UNSW-NB17 philips. 
The latter three datasets are sub-datasets of UNSW-NB17. We regard the three sub-datasets as independent datasets in this research.

There are four stages of this experiment. The following codes illustrate how to conduct this comparative study using the code.

First, define the research scope. Please run the following codes in a python console.
```python
import os

data_type_list = ['kdd99','nb15','nb17_danmini','nb18']
resampling_type_list = ['no_resampling', 'random_oversampling', 'smote', 'adasyn']
resampling_ratio_list = [0.001,0.01, 0.05]
classifier_list = ['ANN','DTR']
```

Second, do data cleaning for all datasets. Every dataset has a exclusive preprocess code. After the preproessing stage, all the data are processed into the same format.
And the rest codes can be used commonly for all the datasets
```python
for data_type in data_type_list:
    os.system('python '+'1_data_cleaning_'+data_type+'.py')
```

Third, do resampling for all datasets.
```python
for data_type in data_type_list:
    for resampling_type in resampling_type_list:
        for resampling_ratio in resampling_ratio_list:
            success_or_failure = os.system(
                'python '+'2_benchmark_data_resampling.py'+' '+data_type+' '+resampling_type+' '+str(resampling_ratio))
            print(success_or_failure)
```

Fourth, do classification for all datasets.
```python
version = '20220811_1'
for data_type in data_type_list:
    for resampling_type in resampling_type_list:
        for resampling_ratio in resampling_ratio_list:
            for classifier in classifier_list:
                success_or_failure = os.system(
                'python '+'4_data_classification.py'+' '+data_type+' '+resampling_type+' '+
                str(resampling_ratio)+' '+classifier+' '+version)
            print(success_or_failure)
```

The experiment above is large. If you only want to do a demo experiment. please run this block of code directly in your terminal.
The following scripts will do smote resampling on KDD99 dataset, and using ANN to classify the data.
```
python 1_data_clean_KDD99.py
python 2_benchmark_data_resampling.py KDD99 smote 0.01
python 4_data_classification.py KDD99 smote 0.01 ANN temp
```

## Other notes
If you find our paper and our code are helpful, please cite our paper: <br/>
Bagui, S., Li, K. Resampling imbalanced data for network intrusion detection datasets. J Big Data 8, 6 (2021). https://doi.org/10.1186/s40537-020-00390-x