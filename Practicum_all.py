import numpy as np
import matplotlib.pyplot as plt
from pynverse import inversefunc


F_val = np.array([0.1, 0.2, 0.3, 0.4, 0.8, 1, 3, 5, 6])


# Problem #1

# The relation between force (F) and the elongation of DNA (L_ext)
#  Lc is the contour length and is equal to bp x 0.34 nm.
def F_vs_L(L_ext):
    kB = 1.3806*10**(-23)  # [J/K]
    T = 273.15 + 20  # [K]
    Lp = 47*10**(-9)  # [m] # persistence length of DNA.
    # [m] # contour length of DNA = no. of bp * 0.34 nm
    Lc = 20600*0.34*10**(-9)
    L_ext = L_ext*10**(-9)
    F_L_ext = kB*T*(1/(4*(1-(L_ext/Lc))**2) - 1/4 + L_ext/Lc)/Lp
    # F_L_ext = lambda L_ext: 1.38**-23*298*(1/(4*(1-L_ext/Lc)**2)-1/4+L_ext/Lc)/Lp*10**-9
    # L_val = inversefunc(F_L_ext, y_values=F_val*10**-12)
    return F_L_ext

def get_L_ext(F_val):
    kB = 1.3806*10**(-23)  # [J/K]
    T = 273.15 + 20  # [K]
    Lp = 47*10**(-9)  # [m] # persistence length of DNA.
    # [m] # contour length of DNA = no. of bp * 0.34 nm
    Lc = 20600*0.34*10**(-9)
    # L_ext = L_ext*10**(-9)
    F_L_ext = lambda L_ext: kB*T*(1/(4*(1-(L_ext/Lc))**2) - 1/4 + L_ext/Lc)/Lp
    L_val = inversefunc(F_L_ext, y_values=F_val*10**-12)
    return L_val



L_ext = np.arange(100, 7000, 100)
# y_F = np.arange(0, 9, 0.1)
# x_L = F_vs_L(F_val)
F_ = F_vs_L(L_ext)*10**12
L_ = get_L_ext(F_val)*10**9
print(F_, L_)

plt.figure(1)
# plt.plot(F_val, x_L, "bo-")
plt.plot(F_, L_ext, "b-")
plt.plot(F_val, L_, "ro")
plt.ylabel('L_ext (nm)')
plt.xlabel('Force (pN)')
plt.show()
