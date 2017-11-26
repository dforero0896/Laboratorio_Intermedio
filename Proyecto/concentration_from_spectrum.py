#!/usr/bin/env python
"""concentration_from_spectrum.py: This script takes an absorption spectrum (tuned to those exported from SPECORD 50) and returns the concentration of the sample of either RhB in Methanol or ZnTPP in toluene."""

__author__ = "Daniel Forero and Juan Sebastian Parada"
import numpy as np
zntpp_slope_1 = 2.34481581e-06
zntpp_slope_unc_1 = 7.13334313474e-07
zntpp_intercept_1 = -1.01998899e-06
zntpp_intercept_unc_1 = 1.13702188394e-06



zntpp_slope_2 =  6.04353620e-05
zntpp_slope_unc_2 = 1.23647744083e-05
zntpp_intercept_2 = -2.86658404e-06
zntpp_intercept_unc_2 = 1.12340251676e-06


rhob_slope_1 = 1.86993237e-05
rhob_slope_unc_1 = 3.38038188574e-07
rhob_intercept_1 = 3.11751602e-07
rhob_intercept_unc_1 = 5.39838249624e-08


rhob_slope_2 = 6.56464123e-05
rhob_slope_unc_2 = 1.62953214353e-06
rhob_intercept_2 =  3.00696048e-07
rhob_intercept_unc_2 = 7.42920359869e-08


rhob_slope_3 = 2.08950781e-04
rhob_slope_unc_3 = 2.18451827247e-05
rhob_intercept_3 = 2.02322034e-07
rhob_intercept_unc_3 = 2.20594627954e-07
substance = raw_input("Please type: ZnTPP or RhB? ")
filename = raw_input("Please type the filename (with extension) ")

spectrum = np.loadtxt(filename, dtype=float, delimiter=';', skiprows =2)

if(substance=='RhB'):
    cut_min_2 = min(np.where(spectrum[:,0]>220)[0])
    cut_max_2 = max(np.where(spectrum[:,0]<300)[0])

    cut_min_3 = min(np.where(spectrum[:,0]>320)[0])
    cut_max_3 = max(np.where(spectrum[:,0]<400)[0])

    cut_min_1 = min(np.where(spectrum[:,0]>450)[0])
    cut_max_1 = max(np.where(spectrum[:,0]<600)[0])

    A_1 = max(spectrum[cut_min_1:cut_max_1,1])
    A_2 = max(spectrum[cut_min_2:cut_max_2,1])
    A_3 = max(spectrum[cut_min_3:cut_max_3,1])
    def cfromA_1(A):
        slope_arr = np.array([rhob_slope_1, rhob_slope_1+rhob_slope_unc_1, rhob_slope_1-rhob_slope_unc_1])
        intercept_arr = np.array([rhob_intercept_1,rhob_intercept_1+rhob_intercept_unc_1,rhob_intercept_1-rhob_intercept_unc_1])
        conc_arr = slope_arr*A+intercept_arr
        return np.array([np.mean(conc_arr), np.std(conc_arr)])
    def cfromA_2(A):
        slope_arr = np.array([rhob_slope_2, rhob_slope_2+rhob_slope_unc_2, rhob_slope_2-rhob_slope_unc_2])
        intercept_arr = np.array([rhob_intercept_2,rhob_intercept_2+rhob_intercept_unc_2,rhob_intercept_2-rhob_intercept_unc_2])
        conc_arr = slope_arr*A+intercept_arr
        return np.array([np.mean(conc_arr), np.std(conc_arr)])
    def cfromA_3(A):
        slope_arr = np.array([rhob_slope_3, rhob_slope_3+rhob_slope_unc_3, rhob_slope_3-rhob_slope_unc_3])
        intercept_arr = np.array([rhob_intercept_3,rhob_intercept_3+rhob_intercept_unc_3,rhob_intercept_3-rhob_intercept_unc_3])
        conc_arr = slope_arr*A+intercept_arr
        return np.array([np.mean(conc_arr), np.std(conc_arr)])

    def give_result(res1, res2, res3):
        return np.mean([res1[0], res2[0], res3[0]]), np.mean([res1[1], res2[1], res3[1]])
    print "The concentration of the sample is: (concentration, uncertainty)\n ",give_result(cfromA_1(A_1), cfromA_2(A_2), cfromA_3(A_3))
    
elif(substance=='ZnTPP'):
    cut_min_2 = min(np.where(spectrum[:,0]>500)[0])
    cut_max_2 = max(np.where(spectrum[:,0]<600)[0])

    cut_min_1 = min(np.where(spectrum[:,0]>400)[0])
    cut_max_1 = max(np.where(spectrum[:,0]<450)[0])

    A_1 = max(spectrum[cut_min_1:cut_max_1,1])
    A_2 = max(spectrum[cut_min_2:cut_max_2,1])
    def cfromA_1(A):
        slope_arr = np.array([zntpp_slope_1, zntpp_slope_1+zntpp_slope_unc_1, zntpp_slope_1-zntpp_slope_unc_1])
        intercept_arr = np.array([zntpp_intercept_1,zntpp_intercept_1+zntpp_intercept_unc_1,zntpp_intercept_1-zntpp_intercept_unc_1])
        conc_arr = slope_arr*A+intercept_arr
        return np.array([np.mean(conc_arr), np.std(conc_arr)])
    def cfromA_2(A):
        slope_arr = np.array([zntpp_slope_2, zntpp_slope_2+zntpp_slope_unc_2, zntpp_slope_2-zntpp_slope_unc_2])
        intercept_arr = np.array([zntpp_intercept_2,zntpp_intercept_2+zntpp_intercept_unc_2,zntpp_intercept_2-zntpp_intercept_unc_2])
        conc_arr = slope_arr*A+intercept_arr
        return np.array([np.mean(conc_arr), np.std(conc_arr)])

    def give_result(res1, res2):
        return np.mean([res1[0], res2[0]]), np.mean([res1[1], res2[1]])
  #  print "The concentration of the sample is: (concentration, uncertainty)\n ",give_result(cfromA_1(A_1), cfromA_2(A_2))
    print "The concentration of the sample is: (concentration, uncertainty)\n ",cfromA_2(A_2)
else:
    print "Please rerun and choose a substance.\n"
