import numpy as np
import matplotlib.pyplot as plot


time = np.arange(0, 20, 0.1)

amplitude = np.sin(time)
plot.plot(time, amplitude)
plot.title('Sine wave')
plot.xlabel('Time')
plot.ylabel('Ampitude = sin(time)')
plot.axhline(y=0, color='k')
plot.show()
