#set up matplotlib and the figure
import matplotlib.pyplot as plt
import math

#create data
def main():
	x_series = []
	# x=1
	# while x<=50:
	# 	x_series.append(0.005+(0.001*(x-1)))
	# 	x=x+1
	# print x_series
	y_series =[]
	# y=1
	# i=iter(x_series)
	# while y<=50:
	# 	throughput=((1.22/0.1)*(1/math.sqrt(i.next()))*512*8)
	# 	y_series.append(throughput)
	# 	y=y+1
	# print y_series
	# 10mb upload 0.030 sec download 0.010sec
	# 1mb upload 0.020 sec download 0.010 sec
	# 100mb upload 0.170 sec download 0.040sec
	# 200mb upload 0.370 sec download 0.060sec
	# 300mb  upload 0.570 sec download 0.080 sec
 	x_series.append(1)
 	x_series.append(10)
 	x_series.append(50)
 	x_series.append(100)
 	x_series.append(150)
 	x_series.append(200)
 	x_series.append(250)
 	x_series.append(300)
 	y_series.append(0.050)
 	y_series.append(0.060)
 	y_series.append(0.160)
 	y_series.append(0.190)
 	y_series.append(0.470)
 	y_series.append(0.550)
 	y_series.append(0.670)
 	y_series.append(0.910)

 #plot data
	plt.plot(x_series, y_series,label=" ")
#plt.plot(x_series, y_series_2, label="x^3")
 
# #add in labels and title
	plt.xlabel("File Size in MB")
	plt.ylabel("Time taken to sync across 3 accounts in seconds")
	plt.title("Time for sync vs File size")
 
# #add limits to the x and y axis
	plt.xlim(1,300)
	plt.ylim(0,1) 
 
# #create legend
	plt.legend(loc="upper right")
 
# #save figure to png
	plt.savefig("DCgraph.png")

if __name__ == '__main__':
 	main() 