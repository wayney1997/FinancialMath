load 'data.txt';
d = diff(log(data));

drift=mean(d)+0.5*var(d)*var(d);
vol=var(d);
S0=data(0);

T=2;
dt=0.01;
t=0:dt:T;
sz=size(t,2);


S=zeros(sz,1);

figure; hold on;
for n=1:100
    
    S(1)=S0;
    xi=randn(sz,1);
    for i=1:sz-1
        S(i+1)=S(i)*exp( (drift-vol^2/2)*dt+ vol*sqrt(dt)*xi(i));
    end
    
    plot(t,S)

end
