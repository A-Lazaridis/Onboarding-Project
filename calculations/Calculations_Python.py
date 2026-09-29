

#Input voltage (V)
Vin = 12
#Output voltage (V)
Vout = 24

#Forward voltage of the 1N5819 diode, from datasheet (V)
Vf = 0.45

#Sturation voltage (V)
Vsat = 1.0

#Frequency (Hz)
f = 30*10**3

#Maximum output current (A)
I_out = 0.250

#Min ripple voltage (V)
V_ripple = 0.24

# (ton/toff)
ton_div_toff = (Vout + Vf - Vin) / (Vin - Vsat)

# (ton+toff)
ton_plus_toff = 1 / f

toff = ton_plus_toff / (ton_div_toff + 1)
ton = ton_plus_toff - toff

CT = (4*10**(-5)) * ton

# Ipk(switch)
Ipk = 2 * I_out * (ton_div_toff + 1)

Rsc = 0.3 / Ipk

L_min = ((Vin - Vsat) / Ipk) * ton

C_O = 9 * ((I_out * ton) / V_ripple)

# Vout = 1.25 * (1 + (R2/R1))
# R2 = R1 * ((Vout/1.25) - 1)
R1 = 1000
R2 = R1 * ((Vout / 1.25) - 1)



print(f"ton/toff = {ton_div_toff:.3f}")
print(f"ton      = {ton*1e6:.1f} us")
print(f"toff     = {toff*1e6:.1f} us")
print(f"CT       = {CT*1e12:.0f} pF")
print(f"Ipk      = {Ipk:.2f} A")
print(f"Rsc      = {Rsc:.2f} ohm")
print(f"L_min    = {L_min*1e6:.0f} uH")
print(f"C_O      = {C_O*1e6:.0f} uF")
print(f"R2       = {R2:.0f} ohm")


#Actual values with chosen parts
print()


ton_actual = 680e-12 / (4*10**(-5))
toff_actual = ton_actual / ton_div_toff
print(f"f actual = {1/(ton_actual + toff_actual)/1e3:.1f} kHz")
print(f"I_limit  = {0.3/0.22:.2f} A")
print(f"Ripple   = {9*I_out*ton/300e-6*1e3:.0f} mV")
print(f"Vout     = {1.25*(1 + 18000/1000):.2f} V")