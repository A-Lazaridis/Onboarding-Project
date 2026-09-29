<!-- kicad_template/calculations/README.md -->

<div align="center">
    <img src="/img/mrc.jpeg" width="200">
</div>

# Calculations

# MC34063A Boost Converter Calculations

## Constants

| Symbol | Value |
|---|---|
| $V_{in}$ | 12 V |
| $V_{out}$ | 24 V |
| $I_{out}$ | 250 mA |
| $f_{min}$ | 30 kHz |
| $V_{ripple}$ | 240 mV |
| $V_{sat}$ | 1.0 V |
| $V_F$ | 0.45 V |

## Timing

$$\frac{t_{on}}{t_{off}} = \frac{V_{out}+V_F-V_{in}}{V_{in}-V_{sat}} = \frac{24+0.45-12}{12-1} = 1.132$$

$$t_{on}+t_{off} = \frac{1}{f} = \frac{1}{30\text{ kHz}} = 33.3\ \mu s$$

$$t_{off} = \frac{33.3\ \mu s}{1.132+1} = 15.6\ \mu s$$

$$t_{on} = 33.3\ \mu s - 15.6\ \mu s = 17.7\ \mu s$$

## Timing Capacitor

$$C_T = 4\times10^{-5}\,t_{on} = 4\times10^{-5}(17.7\ \mu s) = 708\text{ pF}$$

**Chosen: 680 pF**

## Peak Current and Sense Resistor

$$I_{pk} = 2 I_{out}\left(\frac{t_{on}}{t_{off}}+1\right) = 2(0.25)(2.132) = 1.07\text{ A}$$

$$R_{SC} = \frac{0.3}{I_{pk}} = \frac{0.3}{1.07} = 0.28\ \Omega$$

**Chosen: 0.22 Ω**

## Inductor

$$L_{min} = \frac{V_{in}-V_{sat}}{I_{pk}}\,t_{on} = \frac{11}{1.07}(17.7\ \mu s) = 183\ \mu H$$

**Chosen: 220 µH**

## Output Capacitor

$$C_O = 9\,\frac{I_{out}\,t_{on}}{V_{ripple}} = 9\,\frac{(0.25)(17.7\ \mu s)}{0.24} = 166\ \mu F$$

**Chosen: 330 µF**

## Feedback Divider

$$V_{out} = 1.25\left(1+\frac{R_2}{R_1}\right)$$

$$R_2 = R_1\left(\frac{V_{out}}{1.25}-1\right) = 1000\left(\frac{24}{1.25}-1\right) = 18.2\text{ k}\Omega$$

**Chosen: R1 = 1 kΩ, R2 = 18 kΩ**

## Summary

| Part | Calculated | Chosen |
|---|---|---|
| $C_T$ | 708 pF | 680 pF |
| $R_{SC}$ | 0.28 Ω | 0.22 Ω |
| $L$ | 183 µH | 220 µH |
| $C_O$ | 166 µF | 330 µF |
| $R_2$ | 18.2 kΩ | 18 kΩ |