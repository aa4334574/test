#==================================================================
#首先需要导入两个文件
import  matplotlib.pyplot as plt
import  numpy as np
#==================================================================
x = np.arange(-2*np.pi,2*np.pi,0.01)#定义横轴范围
y = np.sin(3*x)/x#函数
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x
plt.plot(x,y)#绘制,matplotlib默认展示不同的颜色
plt.plot(x,y2,'--')
plt.plot(x,y3)
plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],[r'$-2\pi$',r'$\pi$','$0$','$\pi$','$2\pi$'])#显示横坐标刻度值，不加第二个参数，将显示的是数值而不是字母
plt.yticks([-1,0,1,2,3],[r'$-1$','$0$','$+1$','$+2$','$+3$'])
plt.legend(['y1','y2','y3'])
plt.title('NEO-Karl')
#添加注释，使用annotate函数，第一个参数为：latex表达式，即要现实的字符，xy是注释在图表的数据点位置，xytext表示注释与数据点距离，textcoords='offset points'似乎是必须选？使用arrowprops控制箭头
plt.annotate(r'$\lim_{x\to 0}\frac{\sin(x)}{x}=1$',xy=[0,1],xytext=[30,30],fontsize=16,textcoords='offset points',arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
ax = plt.gca()#使用gca函数获取axes对象
ax.spines['right'].set_color('none')#右侧边隐藏
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')#将底边设为横坐标
ax.spines['bottom'].set_position(('data',0))#将坐标置于坐标0处
ax.yaxis.set_ticks_position('left')#左边设置为纵坐标
ax.spines['left'].set_position(('data',0))
plt.show()