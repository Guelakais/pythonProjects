#!/usr/bin/env python
#%%
import matplotlib.pyplot as plt

veranstaltungen = {
    "Ausgefallen": 13,
    "Durchwachsen_stattgefunden":5,
    "Planmäßig_Stattgefunden":4,
}
vProzent = {}
def dictMod(dict a):
    g = 0
    for v in a:
        g += v

    for k, u in a.items:
    vpValue = u/g
    vpKey = f"{k}in Prozent"
    vProzent[vpKey] = vpValue

x = np.array([m = vProzent.get(x) for x in vProzent])
label = [n for n in vProzent]

plt.pie(x, labels=label)
plt.show()

# %%
