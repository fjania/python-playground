from svg import Scene, Rectangle, Circle
from random import randint
import png

filename = "ghostly-teen.png"
r = png.Reader(file=open(filename))
p = list(r.read()[2])
w = len(p[0])
h = len(p)

s = Scene(filename, w, h)
rectangle_count = 0;

class box():
	def __init__(self, x, y, w, h, first=0):
		self.x, self.y, self.w, self.h = x, y, w, h
		#self.filled = first or randint(0,1)
		if first:
			#s.add(Rectangle((x,y),w,h,(255,255,255,0.5)))
			self.filled = 1
			return
		self.filled = sum([sum(g[self.x:self.x+self.w]) for g in p[self.y:self.y+self.h]])
		#print self.filled, 
		if self.filled and not first:
			global rectangle_count 
			rectangle_count += 1
			s.add(Rectangle((x,y),w,h,(255,255,255,1.0)))
		
	def __str__(self):
		return "Box(%d,%d => %d,%d)" % (self.x, self.y, self.x + self.w, self.y + self.h)
	
	def __repr__(self):
		return self.__str__()
		
	def partition_box(self):
		if self.filled:
			self.a = box(self.x, self.y, self.w/2, self.h/2)
			self.b = box(self.x + self.w/2, self.y, self.w/2, self.h/2)
			self.c = box(self.x + self.w/2, self.y + self.h/2, self.w/2, self.h/2)
			self.d = box(self.x, self.y + self.h/2, self.w/2, self.h/2)
			self.children = (self.a, self.b, self.c, self.d)
		
			if self.w/2 > 5 and self.h/2 > 5:
				for c in self.children:
					c.partition_box();
			else:
				s.add(Rectangle((self.x,self.y),self.w,self.h,(128,128,128,1.0)))
              
			return self.children
					
		
b = box(0, 0, w, h, 1)
b.partition_box()
s.write_svg()

print "Box (%d, %d) partitioned into %d rectangles." % (w, h, rectangle_count)