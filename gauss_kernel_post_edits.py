from sklearn.preprocessing import MinMaxScaler
import numpy
from scipy.stats import norm
from createneuron import createneuron


#take data input as numpy array

def gauss_kern(data_input,cnt_MF):
	scaler=MinMaxScaler(feature_range=(20,255))
	
	x=numpy.linspace(-360,360,7201)
	
	mf_spiketime=numpy.empty(shape=(len(data_input),1),dtype='object')
	rows,cols=numpy.shape(data_input)
	
	res=[]
	for loop_j in range(rows):
		stor_sum_val=[]
		datapoints=numpy.zeros([1,cnt_MF]);
		new_storing_mat=numpy.zeros([1,cnt_MF]);
		mf_spike=numpy.empty(shape=(len(data_input.loc[:,"A1"]),cnt_MF));
		
		for i in range(cols):
			sd=10
			mean=data_input.iloc[loop_j,i]
			prob_density = (numpy.pi*sd) * numpy.exp(-0.5*((x-mean)/sd)**2)
			
			#norm1=conv2(norm,inp_for_sys(loop_j,i)); #doubt
			norm1=prob_density*data_input.iloc[loop_j,i]
			norm1=(norm1-min(norm1))/(max(norm1)-min(norm1));
			
			datapoints[i]=createneuron(data_input.iloc[loop_j,i],cnt_MF);
			wt=(data_input.iloc[loop_j,i]/3)*len(data_input)
			rounded_x=[round(num,1) for num in x]
			rounded_dat=[round(num,1) for num in datapoints[i]]
			l_dp=[]
			for num in rounded_x:
				if num in rounded_dat:
					l_dp.append(1)
				else:
					l_dp.append(0)
			
			
			find_dp=[]
			wt=1
			for ind in range(len(l_dp)):
				if l_dp[ind]!=0:
					find_dp.append(ind)
					stor_sum=wt*norm1[ind]
        	#stor_sum_val should be a 2d array check
			try:
				stor_sum_val=numpy.concatenate((stor_sum_val,[stor_sum]) , axis=0);
            
			except:
                #stor_sum_val(:,end+1:size(stor_sum,2))=0;
				stor_sum_val=numpy.concatenate((stor_sum_val,[stor_sum]) , axis=0);
			
			new_storing_mat=stor_sum_val
			
			for j in range(len(new_storing_mat[0])):
				mfspike=EulerAdEx(new_storing_mat[i][j]);
				mf_spike[i][j]=mfspike;

		
		celength=[]
		for i in range(len(mf_spike[0])):
			celength.append(len(i))
		m=max(max(celength)) #what
		for i in range(len(data_input[0])):#check
			temp=[]
			for j in range(len(new_storing_mat[0])):
				if len(mf_spike[i][j])<m:
					temp_zero=numpy.zeros(0,m-len(mf_spike[i][j]))
					mf_spike[i][j]=[mf_spike[i][j],temp_zero]
				
				temp=np.concatenate(temp,mf_spike[i][j])
			spike_positions[i]=temp
		
		res.append(spike_positions)
		#mf_spiketime{loop_j}=spiktime2matrix(spike_positions)
	return res

