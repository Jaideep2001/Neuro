def spiktime2matrix(spike_positions):
cnt=0;
#cell array of spiketiming is stored in a matrix timeser
    for j=1:length(spike_positions):
        for i=1:size(spike_positions[j]):
            cnt=cnt+1;
            I=find(spike_positions[j][i,:)
            if(isempty(I))
                timeser(cnt,1)=0;
            else
                for k=1:I(end)
                    timeser(cnt,k)=spike_positions{j}(i,k);
    return timeser
