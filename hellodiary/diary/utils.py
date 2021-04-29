import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()

    return graph

def plot_line_graph(data):
    x = [i for i in range(len(data))]
    
    plt.switch_backend('AGG')
    plt.title('Sentiment of user in months')
    xnew = np.linspace(1, len(x), 200) 

#define spline
    spl = make_interp_spline(x, data, k=3)
    y_smooth = spl(xnew)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    print(data[-2], data[-1])

    fig.patch.set_alpha(0.0)
    if data[-1] >= 0:
        plt.plot(xnew, y_smooth, linewidth = 4, color='green')
        emotion = 'happy'
    else:
        plt.plot(xnew, y_smooth, linewidth = 4, color='red')
        emotion = 'sad'
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()

    

    graph = get_graph()

    return graph, emotion

