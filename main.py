from data_preprocessing import data_preprocessing
from gauss_kernel import gauss_kern

filename='tennis.xlsx';
traintest=data_preprocessing(filename)

#cnt_MF=input('Enter the number of MFneurons to be created for each feature: ');
cnt_MF=7;
mf_spiketime=gauss_kern(traintest[0],cnt_MF);
print(mf_spiketime)
