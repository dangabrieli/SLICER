import simplex
import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#STL file import
file_path = str(input('Please enter the path of your stl file: \n'))
your_mesh = mesh.Mesh.from_file(file_path)
temp = your_mesh.points
triangles = []

for node in temp:

	triangles.append(simplex.Triangle(simplex.Point(node[0],node[1],node[2]),simplex.Point(node[3],node[4],node[5]),simplex.Point(node[6],node[7],node[8])))


a = triangles[0].min()
b = triangles[0].max()

for t in triangles:

	if t.min() < a:
		a = t.min()

	if b < t.max():
		b = t.max()

dz = float(input('Please enter vertical increment: '))

z_range = np.arange(a, b, dz)

layers = []

for z in z_range:

	z_layer = []

	for triangle in triangles:

		if triangle.inrange(z):

			z_layer.append(triangle.tp_int(z))

	layers.append(z_layer)

ax = plt.gca(projection="3d")

for layer in layers:

	for line in layer:

		graph = [[], [], []]

		graph[0].append(line.A.X)
		graph[1].append(line.A.Y)
		graph[2].append(line.A.Z)
		graph[0].append(line.B.X)
		graph[1].append(line.B.Y)
		graph[2].append(line.B.Z)

		#ax.scatter(graph[0], graph[1], graph[2], c='r', s=1)
		ax.plot(graph[0], graph[1], graph[2], color='b')

plt.show()