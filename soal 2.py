# Menghitung Jarak Horizontal atau Vertikal pada Gerak Parabola

from numpy import sin

v0 = 10 # kecepatan awal dalam m/s
alfa = 30 # sudut yang dibentuk dalam derajat
g = 9.8 # percepatan gravitasi dalam m/s^2
pi = 3.14

# jarak horizontal dalam meter 
x = (v0**2*sin(2*alfa*pi/180))/2*g
print(x)
