def pathFinder(A,B):
    # A[] and B[] are long and lat coordinates
    if len(A)!=2 or len(B)!=2:
        return -1

    buf = 0.0001
    xmin = min(A[0],B[0]) - buf
    ymin = min(A[1],B[1]) - buf
    xmax = max(A[0],B[0]) + buf
    ymax = max(A[1],B[1]) + buf
    step = (xmax-xmin)/9

    m = (float)(A[1]-B[1])/(float)(A[0]-B[0])
    c = A[1] - m*A[0]

    # y = upper + m * x
    # y = lower + m * x

    C = []
    x = xmin
    while x<xmax:
        if x>xmin+4*step and x<xmax-4*step:
            C.append([x,m*x+(c-buf*2)])
            C.append([x,m*x+(c-buf)])
            C.append([x,m*x+c])
            C.append([x,m*x+(c+buf)])
            C.append([x,m*x+(c+buf*2)])
        elif x>xmin+2*step and x<xmax-2*step:
            C.append([x,m*x+(c-buf)])
            C.append([x,m*x+c])
            C.append([x,m*x+(c+buf)])
        else:
            C.append([x,m*x+c])
        x+=step
    return C