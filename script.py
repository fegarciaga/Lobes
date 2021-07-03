import numpy as np
import matplotlib.pyplot as plt

def read_and_interpolate(filename, l, outfile, grade1, grade2, t):
    data=np.zeros((l,6))
    dataaux=np.loadtxt(filename)

    for i in range(len(dataaux)):
        data[int(i/3),int(i%3)]=dataaux[i]

    for i in range (l-1):
        data[i, 3]=data[i+1,2]-data[i,2]
        data[l-1-i,4]=-data[l-2-i,2]+data[l-1-i,2]

    for i in range (l):
        data[i, 5]=data[i,3]-data[i,4]

    datafinal=np.zeros((int(l/3),3))
    for i in range(int(l/3)):
        datafinal[i,0]=1/data[1+3*i,0]
        datafinal[i,1]=data[1+3*i,3]
        datafinal[i,2]=data[1+3*i,4]

    plt.figure()
    plt.scatter(datafinal[:,0], datafinal[:,1])
    plt.show()
    plt.figure()
    plt.scatter(datafinal[:,0], datafinal[:,2])
    plt.show()
    z = np.polyfit(datafinal[:,0], datafinal[:,1], grade1)
    p = np.poly1d(z)
    z1 = np.polyfit(datafinal[:,0], datafinal[:,2], grade2)
    p1 = np.poly1d(z1)
    with open(outfile, "a") as text_file:
        text_file.write(str(t)+ "\t"+str(p(0))+"\t"+str(p1(0))+"\n")
    return

def plot(filename, outname):
    data=np.loadtxt(filename, delimiter='\t')
    plt.figure()
    plt.scatter(data[:,0], data[:,1], color='k', label=r'$U_{ab}/U=1.0$')
    plt.plot(data[:,0], data[:,1], color='k')
    plt.scatter(data[:,0], data[:,2], color='k')
    plt.plot(data[:,0], data[:,2], color='k')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$\mu/U$')
    plt.legend()
    plt.savefig(outname)
    return

def plothop(filename, outname, l):
    data=np.zeros((l,5))
    dataaux=np.loadtxt(filename)

    for i in range(len(dataaux)):
        data[int(i/2),int(i%2)]=dataaux[i]

    for i in range (l-1):
        data[i, 2]=data[i+1,1]-data[i,1]
        data[l-1-i,3]=-data[l-2-i,1]+data[l-1-i,1]

    for i in range (l):
        data[i, 4]=data[i,2]-data[i,3]

    plt.figure()
    plt.scatter(data[0:-1,2], data[0:-1,0]/24,  color='k', label=r'$U_{ab}/U=1.0$, $t_B=t_F=1.0$, $U_{ab}=4.0$, $A_J=0.0$, $U_{BF}=8.0$')
    plt.plot(data[0:-1,2], data[0:-1,0]/24,color='k')
    plt.xlabel(r'$\mu_{+}$')
    plt.ylabel(r'$\rho$')
    plt.legend()
    plt.savefig(outname)
    return

def plotinsec(filename, outname, l):
    data=np.zeros((l,6))
    dataaux=np.loadtxt(filename)

    for i in range(len(dataaux)):
        data[int(i/3),int(i%3)]=dataaux[i]

    for i in range (l-1):
        data[i, 3]=data[i+1,2]-data[i,2]
        data[l-1-i,4]=-data[l-2-i,2]+data[l-1-i,2]

    for i in range (l):
        data[i, 5]=data[i,3]-data[i,4]

    datafinal=np.zeros((int(l/3),3))
    for i in range(int(l/3)):
        datafinal[i,0]=1/data[1+3*i,0]
        datafinal[i,1]=data[1+3*i,3]
        datafinal[i,2]=data[1+3*i,4]

    z = np.polyfit(datafinal[:,0], datafinal[:,1], 1)
    p = np.poly1d(z)
    z1 = np.polyfit(datafinal[:,0], datafinal[:,2], 1)
    p1 = np.poly1d(z1)
    plt.figure()
    plt.scatter(datafinal[:,0], datafinal[:,1], color='k', label=r'$U_{ab}/U=1.0$, $t/U=0.35$')
    plt.plot(np.linspace(0, 0.045, 20), p(np.linspace(0, 0.045, 20)), color='k')
    plt.scatter(datafinal[:,0], datafinal[:,2], color='k')
    plt.plot(np.linspace(0, 0.045, 20), p1(np.linspace(0, 0.045, 20)), color='k')
    plt.xlabel(r'$1/L$')
    plt.ylabel(r'$\mu/U$')
    plt.legend()
    plt.savefig(outname)
    return

#read_and_interpolate("energy0.txt", 6, "Out.txt", 1, 1, 0.001)
#read_and_interpolate("energy05.txt", 12, "Out.txt", 1, 1, 0.05)
#read_and_interpolate("energy10.txt", 15, "Out.txt", 2, 2, 0.1)
#read_and_interpolate("energy15.txt", 15, "Out.txt", 2, 2, 0.15)
#read_and_interpolate("energy20.txt", 15, "Out.txt", 2, 2, 0.2)
#read_and_interpolate("energy25.txt", 9, "Out.txt", 1, 1, 0.25)
#read_and_interpolate("energy30.txt", 9, "Out.txt", 1, 1, 0.3)
#read_and_interpolate("energy35.txt", 9, "Out.txt", 1, 1, 0.35)


#plot("Out.txt", "fig.png")

#plotinsec("energy35.txt", "no_hop.png", 9)

plothop("hop.txt", "gap.png", 28)
