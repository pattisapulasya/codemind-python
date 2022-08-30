x=input()
hours=int(x[:2])
mints=int(x[3:])
z=abs(1/2*(60*hours-11*mints))
if z>180:
    z=(360-z)
print(z)