print('Faliure Theories Fos Calculator')

print('Sigma x?')

x = float(input('Enter value:'))

print('Sigma y?')

y = float(input('Enter value:'))

print('Sigma z?')

z = float(input('Enter value:'))

print('Tao?')

t = float(input('Enter value:'))

print('Brittle (type "1") or Ductile (type "2")?')

BD = float(input('Enter value (1 or 2):'))

if BD != 2 and BD != 1:
    print('Invalid Character for Brittle ')
    exit()

print('Conservative? ( 1 = yes, 2= no)')

C = float(input('Enter value (1 or 2):'))

if C != 1 and C != 2:
    print('Invalid Character for Conservative ')
    exit()


sp = float((x**2-x*y+y**2+3*t**2)**(1/2))

oa = float(((x+y)/2)+(((x-y)/2)**2+t**2)**(1/2))

ob = float(((x+y)/2)-(((x-y)/2)**2+t**2)**(1/2))

if BD == 2 and C == 1:  # MSS
    print('>>>>>Max Shear Stress')
    print("Sy?")
    sy = float(input('Enter value:'))
    print("Sy is %d " % sy)
    print("Tao is %d " % t)
    g = (sy/2)/t
    print("%.4f" % g)

elif BD == 2 and C == 2:  # DE
    print('>>>>>Distortion Energy')
    print("Sy?")
    sy = float(input('Enter value:'))
    g = sy/sp
    print("%.4f" % g)

elif BD == 1 and C == 1 and oa >= ob >= 0:
    # BCM
    print('>>>>>Brittle Coulumb Mohr')
    print('Sut?')
    sut = float(input('Enter value:'))
    g = sut/oa
    print("%.4f" % g)

elif BD == 1 and C == 1 and oa >= 0 >= ob:
    # BCM
    print('>>>>>Brittle Coulumb Mohr')
    print('Sut?')
    sut = float(input('Enter value:'))
    print('Suc?')
    suc = float(input('Enter value:'))
    g = ((oa/sut)-(ob/suc))**-1
    print("%.4f" % g)

elif BD == 1 and C == 1 and 0 >= oa >= ob:
    # BCM
    print('>>>>>Brittle Coulumb Mohr')
    print('Suc?')
    suc = float(input('Enter value:'))
    g = -(suc/ob)
    print("%.4f" % g)

elif BD == 1 and C == 2 and oa >= ob >= 0:
    # MM
    print('>>>>>Modified Mohr')
    print('Sut?')
    sut = float(input('Enter value:'))
    g = sut/oa
    print("%.4f" % g)

elif BD == 1 and C == 2 and oa >= 0 >= ob and abs(ob/oa) <= 0:
    # MM
    print('>>>>>Modified Mohr')
    print('Sut?')
    sut = float(input('Enter value:'))
    g = sut/oa
    print("%.4f" % g)

elif BD == 1 and C == 2 and oa >= 0 >= ob and abs(ob/oa) >= 0:
    # MM
    print('>>>>>Modified Mohr')
    print('Sut?')
    sut = float(input('Enter value:'))
    print('Suc?')
    suc = float(input('Enter value:'))
    g = ((((suc-sut)*oa)/(suc*sut)) - (ob/suc))**(-1)
    print("%.4f" % g)


elif BD == 1 and C == 2 and 0 >= oa >= ob:
    # MM
    print('>>>>>Modified Mohr')
    print('Suc?')
    suc = float(input('Enter value:'))
    g = -(suc/ob)
    print("%.4f" % g)