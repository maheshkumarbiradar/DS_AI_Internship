#task 1

import numpy as np
stdl = ([[58,59,85],[85,53,94],[75,84,55],[75,85,65],[75,76,87]])

stdl_avg = np.mean(stdl, axis = 0)
print(stdl_avg)
sml = stdl-stdl_avg
print(stdl)
print(sml)

#task 2

rs = np.arange(24)
print(rs)
rs.reshape(4,3,2)
rs.reshape(4,2,3)
