list_temperatures = [28,27,30,26,34,37,39]
days_of_the_week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
count=0;
length=(len(list_temperatures));
for i in range (length)
  if list_temperatures[i]%2==0;
    count=count+1;
print(count);
good_days_count=count;
max=0;
min=0;
for i in range (length)
  if max<list_temperatures[i]
     max=list_temperatures[i];
for i in range (length)
  if min>list_temperatures[i]
      min=list_temperatures[i];
print (max, min)
sum=0;
for i in range (length)
  sum=sum+list_temperatures[i];
avg=sum/7;
print avg;
above_avg = []
count1=0;
for i in range (length)
  if temperatures[i]>avg
  list_temperatures.append(temperatures[i])
  count1=count1+1;

for i in range (6)
  print (days_of_the_week[i]":"list_temperatures[i])
print ("days with temp higher than average:")
for i in range (6)
  if temperatures[i]>avg
  print(days_of_the_week[i]":"list_temperatures[i])
