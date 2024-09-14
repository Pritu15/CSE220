import numpy as np
import matplotlib.pyplot as plt

INF = 8

def plot(
        signal, 
        title=None, 
        y_range=(-1, 3), 
        figsize = (8, 3),
        x_label='n (Time Index)',
        y_label='x[n]',
        saveTo=None
    ):
    plt.figure(figsize=figsize)
    plt.xticks(np.arange(-INF, INF + 1, 1))
    
    y_range = (y_range[0], max(np.max(signal), y_range[1]) + 1)
    # set y range of 
    plt.ylim(*y_range)
    plt.stem(np.arange(-INF, INF + 1, 1), signal)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    if saveTo is not None:
        plt.savefig(saveTo)
    # plt.show()

def init_signal():
    return np.zeros(2 * INF + 1)


def time_shift_signal(x : np.ndarray, k : int) -> np.ndarray:
    # implement this function
    # a=np.array(x)
    # a=np.ones(len(x))
    # np.copyto(a,x)
    # x=np.roll(x,k)
    # if k>0:
    #     x[:k]=0
        
    # #   p=len(x);
    # #   for i in range(p):
    # #     if(i>=k):
    # #         x[i]=a[i-k]
    # #     else:
    # #         x[i]=0
    # elif k==0:
    #     return a        
    # else:
    #     x[k:]=0
    #     # return b
    # #   p=len(x);
    # #   k=(-1*k)
    # #   for i in range(p):
    # #     if((i+k)<p):
    # #         x[i]=a[i+k]
    # #     else:
    # #         x[i]=0     
    return np.roll(x,k);

    

def time_scale_signal(x : np.ndarray, k : int) -> np.ndarray:
    # implement this function
    if k==1:
     print(x)
     return x
    print("HEllo")
    p=np.zeros(len(x))
    np.copyto(p,x)
    mid=len(p)//2
    a=p[:mid]
    a=np.flip(a)
    for i in range(len(a)):
        l=(i+1)*k
        l=l-1
        if l<len(a):
            a[i]=a[l]
        else:
            a[i]=0
    b=p[mid+1:]
    for i in range(len(b)):
        l=(i+1)*k
        l=l-1
        if l<len(b):
            b[i]=b[l]
        else:
            b[i]=0

    p[:mid]=np.flip(a)
    p[mid+1:]=b
    # if(k<0):
    #     return np.flip(x)
    # return x
    return p;


def main():
    img_root_path = '.'
    signal = init_signal()
    signal[INF] = 1
    signal[INF+1] = .5
    signal[INF-1] = 2
    signal[INF + 2] = 1
    signal[INF - 2] = .5

    plot(signal, title='Original Signal(x[n])', saveTo=f'{img_root_path}/x[n].png')

    plot(time_shift_signal(signal, 2), title='x[n-2]', saveTo=f'{img_root_path}/x[n-2].png')
    
    plot(time_shift_signal(signal, -2), title='x[n+2]', saveTo=f'{img_root_path}/x[n+2].png')
    
    plot(time_shift_signal(signal, 0), title='x[n+0]', saveTo=f'{img_root_path}/x[n+0].png')
    
    plot(time_scale_signal(signal, 2), title='x[2n]', saveTo=f'{img_root_path}/x[2n].png')
    
    plot(time_scale_signal(signal, 1), title='x[1n]', saveTo=f'{img_root_path}/x[1n].png')
    
        

main()