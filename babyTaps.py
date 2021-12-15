#!usr/bin/env python
#%%
one = []
for x in range(0, 7, 1):
    one.append(x)
oneM = [(x*3%7) for x in one]

print(one)
print(oneM)
infinityM = [x for x in range(0, 200, 1)]
infinityMM = [x*x for x in range(0, 200, 1)]


# %%
