pie = 3.14
half = 1/2

def cylindertsa():
    b = int(input("Enter The Radius Of The Cylinder => "))
    c = int(input("Enter The Height Of The Cylinder => "))
    f1 = 2*pie*b*c
    f2 = 2*pie*b**2
    TSurfaceAreaOfCylinder = f1+f2
    print("The Total Surface Area Of The Cylinder is : ", TSurfaceAreaOfCylinder)

def cylindercsa():
    b = int(input("Enter The Radius Of The Cylinder => "))
    c = int(input("Enter The Height Of The Cylinder => "))
    f1 = 2*pie*b*c
    TSurfaceAreaOfCylinder = f1
    print("The Curved Surface Area Of The Cylinder is : ", TSurfaceAreaOfCylinder)

def cubetsa():
    d = int(input("Enter The Side Of The Cube => "))
    TSurfaceAreaOfCube = 6*d**2
    print("The Total Surface Area Of The Cube is : ", TSurfaceAreaOfCube)

def cubecsa():
    d = int(input("Enter The Side Of The Cube => "))
    CSurfaceAreaOfCube = 4*d**2
    print("The Lateral Surface Area Of The Cube is : ", CSurfaceAreaOfCube)

def cuboidtsa():
    e = int(input("Enter The Length Of The Cuboid => "))
    f = int(input("Enter The Breadth Of The Cuboid => "))
    g = int(input("Enter The Height Of The Cuboid => "))
    f3 = e*f
    f4 = f*g
    f5 = g*e
    f6 = f3+f4+f5
    TSurfaceAreaOfCuboid = 2*f6
    print("The Total Surface Area Of The Cuboid is : ", TSurfaceAreaOfCuboid)

def cuboidcsa():
    j = int(input("Enter The Length Of The Cuboid => "))
    k = int(input("Enter The Breadth Of The Cuboid => "))
    l = int(input("Enter The Height Of The Cuboid => "))
    f7 = 2*l
    f8 = j+k
    CSurfaceAreaOfCuboid = 2*l*f8
    print("The Lateral Surface Area Of The Cuboid is : ", CSurfaceAreaOfCuboid)

def spheretsa():
    m = int(input("Enter The Radius Of The Sphere => "))
    f7 = 4*pie
    f8 = m**2
    TSurfaceAreaOfSphere = f7*f8
    print("The Total Surface Area Of The Sphere is : ", TSurfaceAreaOfSphere)

def spherecsa():
    n = int(input("Enter The Radius Of The Sphere => "))
    f7 = 4*pie
    f8 = n**2
    CSurfaceAreaOfSphere = f7*f8
    print("The Lateral Surface Area Of The Sphere is : ", CSurfaceAreaOfSphere)

def hemispheretsa():
    o = int(input("Enter The Radius Of The Hemisphere => "))
    f7 = 3*pie
    f8 = o**2
    TSurfaceAreaOfHemisphere = f7*f8
    print("The Total Surface Area Of The Hemisphere is : ", TSurfaceAreaOfHemisphere)

def hemispherecsa():
    p = int(input("Enter The Radius Of The Hemisphere => "))
    f9 = half*4
    f10 = pie*p**2
    CSurfaceAreaOfHemisphere = f9*f10
    print("The Lateral Surface Area Of The Hemisphere is : ", CSurfaceAreaOfHemisphere)

def conetsa():
    q = int(input("Enter The Radius Of The Cone => "))
    r = int(input("Enter The Length Of The Cone => "))
    f11 = pie*q*r
    TSurfaceAreaOfCone = f11
    print("The Total Surface Area Of The Cone is : ", TSurfaceAreaOfCone)

def conecsa():
    s = int(input("Enter The Radius Of The Cone => "))
    t = int(input("Enter The Length Of The Cone => "))
    f12 = pie*s
    f13 = t+s
    CSurfaceAreaOfCone = f12*f13
    print("The Total Surface Area Of The Cone is : ", CSurfaceAreaOfCone)