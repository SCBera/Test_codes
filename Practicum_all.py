import numpy as np
import matplotlib.pyplot as plt
from pynverse import inversefunc


F_val = np.array([0.1, 0.2, 0.3, 0.4, 0.8, 1, 3, 5, 6])  # in pN


# Problem #1

# The relation between force (F) and the elongation of DNA (L_ext)
def F_vs_L(L_ext):
    kB = 1.3806*10**(-23)  # [J/K]
    T = 273.15 + 20  # [K]
    Lp = 47*10**(-9)  # [m] # persistence length of DNA.
    # [m] # contour length of DNA = no. of bp * 0.34 nm
    Lc = 20600*0.34*10**(-9)
    L_ext = L_ext*10**(-9)
    F_L_ext = kB*T*(1/(4*(1-(L_ext/Lc))**2) - 1/4 + L_ext/Lc)/Lp
    return F_L_ext*10**12


def get_L_ext(F_val):
    F_val = F_val*10**-12
    kB = 1.3806*10**(-23)  # [J/K]
    T = 273.15 + 20  # [K]
    Lp = 47*10**(-9)  # [m] # persistence length of DNA.
    # # Lc contour length of DNA = no. of bp * 0.34 nm converted to meter
    # Lc = 100*10**(-9)
    Lc = 20600*0.34*10**(-9)
    # L_ext = L_ext*10**(-9)
    F_L_ext = lambda L_ext: kB*T*(1/(4*(1-((L_ext*10**-9)/Lc))**2) - 1/4 + (L_ext*10**-9)/Lc)/Lp
    L_val = inversefunc(F_L_ext, y_values=F_val)
    return L_val#*10**9???????????????????

L_ext = np.arange(100, 7000, 100)
# y_F = np.arange(0, 9, 0.1)
# x_L = F_vs_L(F_val)
F_ = F_vs_L(L_ext)
L_ = get_L_ext(F_val)
# print(F_, L_)

plt.figure(1)
# plt.plot(F_val, x_L, "bo-")
# plt.plot(F_, L_ext, "b-")
plt.plot(F_val, L_, "bo-")
plt.ylabel('L_ext (nm)')
plt.xlabel('Force (pN)')
# plt.show()

#########################################################################################
# Problem  # 2 Correlation time


def corr_t(F, L):
    # t_c,x = 6*PI*eta*R*L/F
    # return 6*np.pi*0.001*0.5*10**-6*L*10**-9/(F*10**-12)
    return 6 * np.pi * 0.001 * 0.5 * 10**(-6) * (L * 10**-9) / (F * 10**-12)


# x_F = np.array([0.1, 0.2, 0.3, 0.4, 0.8, 1, 3, 5, 6])


ydata = corr_t(F_val, L_)

tc_by_tsh = ydata*10**3/17

# print(ydata)
plt.figure(2)
plt.plot(F_val, ydata, "bs-")
plt.xlabel('F (pN)')
plt.ylabel('Corr_t (sec)')
# plt.plot(x_F, tc_by_tsh, "bo")
# plt.show()


######################################################################
# Problem #3 Varriaence
def var_x(F, L_ext):
    var_ = 1.3806*10**-23*298*(L_ext*10**-9)/(F*10**-12)
    return var_*10**18

y_var = var_x(F_val, L_)

# print(y_var)

plt.figure(3)
plt.plot(F_val, y_var, "b^-")
plt.xlabel('F (pN)')
plt.ylabel('x_var (nm*nm)')


##############################################################################
# Problem # 4 Z position
Fz = lambda z_pos: 5.7061*np.exp(-1.0203*z_pos) + 3.1215*np.exp(-0.5843*z_pos)
z_val = inversefunc(Fz, y_values=F_val)

print(z_val)

plt.figure(4)
plt.plot(F_val, z_val, "b--")
plt.xlabel('F (pN)')
plt.ylabel('z_val (mm)')


# plt.show()
