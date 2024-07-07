def LoadObj(fileName):
    data = open(fileName, "r", encoding="utf-8")
    
    dataDict = {"Vertices":[], "Vertex Normals":[], "Faces":[]}

    while 1:
        read = data.readline()
        readlen = len(read)
        prefix = read[0:2]
        partlist = []
        
        for i in range(readlen):
            if read[i] == ' ' or read[i] == '/':
                partlist.append(i)
        
        if prefix == 'v ':
            
            vertex = []
            
            vertex.append(float(read[partlist[0]+1:partlist[1]]))
            vertex.append(float(read[partlist[1]+1:partlist[2]]))
            vertex.append(float(read[partlist[2]+1:-1]))
            
            dataDict["Vertices"].append(vertex)
            
            
        elif prefix == 'vn':
            vertexNormal = []
            
            vertexNormal.append(float(read[partlist[0]:partlist[1]]))
            vertexNormal.append(float(read[partlist[1]+1:partlist[2]]))
            vertexNormal.append(float(read[partlist[2]+1:-1]))
            
            dataDict["Vertex Normals"].append(vertexNormal)


        elif prefix == 'f ':
            facevals = []
            faceVerts = []
            faceNormal = [0.0, 0.0, 0.0]
            partlist.append(-1)
            for p in range(int((len(partlist)-1)/3)):
                facevallist = []
                
                for n in range(2):
                    facevallist.append(int(read[partlist[p*3+n*2]+1:partlist[p*3+n*2+1]]))
                    
                for i in range(3):
                    faceNormal[i] += dataDict["Vertex Normals"][facevallist[1] - 1][i]
                
                faceVerts.append(facevallist[0])
                
            facevals.append(faceVerts)
            facevals.append(faceNormal)
            dataDict["Faces"].append(facevals)
            

        elif prefix == "":
            dataDict.pop("Vertex Normals")
            return dataDict
