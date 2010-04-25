from svg import Scene, Rectangle, Circle
from pngtext import PNGText

def partition():
	b = BoundingBox(0, 0, t.w, t.h, first=True)
	b.partition_box()
	scene.write_svg()

	print "Box %s partitioned into %d rectangles." % (t.bounds, t.rectangle_count)
		
		
class BoundingBox():
	
	def __init__(self, x, y, w, h, first=False):
		self.x, self.y, self.w, self.h = x, y, w, h
		if first:
			self.filled = 1
			scene.add(Rectangle((x,y),w,h,(255,255,255,1.0)))
		else: 
			#self.filled = sum([sum(g[self.x:self.x+self.w]) for g in p[self.y:self.y+self.h]])
			t.rectangle_count += 1
			self.filled = t.is_box_filled(x, y, w, h)
			scene.add(Rectangle((x,y),w,h,(255,255,255,1.0)))
		
	def __str__(self):
		return "Box(%d,%d => %d,%d)" % (self.x, self.y, self.x + self.w, self.y + self.h)
	
	def __repr__(self):
		return self.__str__()
		
	def partition_box(self):
		if self.filled:
			self.a = BoundingBox(self.x, self.y, self.w/2, self.h/2)
			self.b = BoundingBox(self.x + self.w/2, self.y, self.w/2, self.h/2)
			self.c = BoundingBox(self.x + self.w/2, self.y + self.h/2, self.w/2, self.h/2)
			self.d = BoundingBox(self.x, self.y + self.h/2, self.w/2, self.h/2)
			self.children = (self.a, self.b, self.c, self.d)
		
			if self.w/2 > 2 and self.h/2 > 2:
				for c in self.children:
					c.partition_box();
			else:
				scene.add(Rectangle((self.x,self.y),self.w,self.h,(128,128,128,1.0)))
              
			return self.children
				
text, fontfamily, size = 'abcdefghijk', 'teen', 250
t = PNGText(text, fontfamily, size)
scene = Scene('output/' + text + '_' + fontfamily + '_' + str(size), t.w, t.h)
partition()
		
