#!/usr/bin/env python3
"""
Module: lsclib
The library for LSC dynamical regime analysis.
"""

### Histories:
### 2024/10/02 -- Bicheng Chen (bchen@xmu.edu.cn) -- First created



## Prerequisite Module
import numpy as np



## Class
class caseClass:
    def __init__(self, Laₜ, χ, kH, ustar, H, fmt_key="Lat{Lat:s}_X{X:s}_kH{kH:s}"):
        self.Laₜ = Laₜ
        self.χ = χ
        if self.Laₜ == np.inf:
            self.kH = np.nan
        else:
            self.kH = kH
        self.ustar = ustar
        self.H = H
        
        if Laₜ != np.inf:
            self.key_Laₜ = "{:03d}".format(int(Laₜ*100))
            self.key_kH = "{:d}_{:d}".format(kH.numerator, kH.denominator)
        else:
            self.key_Laₜ = "Inf"
            self.key_kH = "nan"

        self.key_χ = "{:d}_{:d}".format(χ.numerator, χ.denominator)
        self.key_case = fmt_key.format(Lat=self.key_Laₜ, X=self.key_χ, kH=self.key_kH)



## Function
# Find the key for a case based on La_t, \chi, kH
def find_caseKey(Laₜ, χ, kH, fmt_key="Lat{Lat:s}_X{X:s}_kH{kH:s}"):
    if Laₜ != np.inf:
        key_Laₜ = "{:03d}".format(int(Laₜ*100))
        key_kH = "{:d}_{:d}".format(kH.numerator, kH.denominator)
    else:
        key_Laₜ = "Inf"
        key_kH = "nan"

    key_χ = "{:d}_{:d}".format(χ.numerator, χ.denominator)
    key_case = fmt_key.format(Lat=key_Laₜ, X=key_χ, kH=key_kH)

    return key_case