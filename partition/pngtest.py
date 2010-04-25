import png
from svg import Scene, Rectangle, Circle

r = png.Reader(file=open("text.png"))
p = list(r.read()[2])

s = Scene("a2d")

for y in range(0,599,10):
	for x in range(0,799,10):
		if sum([sum(g[x:x+10]) for g in p[y:y+10]]):
		#if p[y][x] > 0:
			#s.add(Rectangle((x,y),10,10,(255,255,255,1.0)))
			s.add(Circle((x+5,y+5),5,(255,255,255,1.0)))

s.write_svg()