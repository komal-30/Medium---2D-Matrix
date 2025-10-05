#Ideal
def spiral_matrix(mat):
    ans=[]
    n = len(mat)  #Row
    m = len(mat[0]) #Column

    srow=0
    erow=n-1
    scol=0
    ecol=m-1

    while(srow<=erow and scol <= ecol):
        #Top
        for i in range(scol,ecol+1):
            ans.append(mat[srow][i])
        srow+=1
        
        #Right
        for j in range(srow,erow+1):
            ans.append(mat[j][ecol])
        ecol-=1

        #Bottom
        if srow <= erow:
            for k in range(ecol,scol-1,-1):
                ans.append(mat[erow][k])
            erow-=1

        #Left
        if scol<=ecol:
            for l in range(erow,srow-1,-1):
                ans.append(mat[l][scol])
            scol+=1

    return ans





