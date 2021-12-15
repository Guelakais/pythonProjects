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
    vProzent[f"{k}in Prozent"] = u/g

x = np.array([m = vProzent.get(x) for x in vProzent])
label = [n for n in vProzent]

plt.pie(x, labels=label)
plt.show()

# %%
