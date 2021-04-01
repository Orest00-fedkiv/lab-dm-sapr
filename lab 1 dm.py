adjMatrix = [[0,0,38,95,0,1,57,0],
             [0,0,0,0,79,0,36,19],
             [38,0,0,51,0,0,44,0],
             [95,0,51,0,0,44,0,0],
             [0,79,0,0,0,93,41,48],
             [1,0,0,44,93,0,1,0],
             [57,36,44,0,41,1,0,0],
             [0,19,0,0,48,0,0,0]]
setMatrix = []
for i in range(0,len(adjMatrix)):
  setMatrix.append([i])

def combine(e):
  e0 = -1
  e1 = -1
  for i in range(0,len(setMatrix)):
    if e[0] in setMatrix[i]:
      e0 = i
    if e[1] in setMatrix[i]:
      e1 = i
  setMatrix[e0] += setMatrix[e1]
  del setMatrix[e1]



print("Initial Grouping: " + str(setMatrix))
while (len(setMatrix) > 1):
  edges = []
  for component in setMatrix:
    m = [999,[0,0]]
    for vertex in component:
      for i in range(0,len(adjMatrix[0])):
        if i not in component and adjMatrix[vertex][i] != 0:
          if (m[0] > adjMatrix[vertex][i]):
            m[0] = adjMatrix[vertex][i]
            m[1] = [vertex,i]
    if (m[1][0] > m[1][1]):
      m[1][0], m[1][1] =  m[1][1],m[1][0]
    if (m[1] not in edges):
      edges.append(m[1])
  for e in edges:
    combine(e)
  print("Edges formed: " + str(edges) + " Groupings: " + str(setMatrix))