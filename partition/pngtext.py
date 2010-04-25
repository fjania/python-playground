import Image, ImageDraw, ImageFont


class PNGText():
	def __init__(self, text, fontfamily, size):
		self.rectangle_count = 0
		self.bounds, self.imagedata = self.generate_text_png(text, fontfamily, size)
		self.w, self.h = self.bounds
		self.blankpixel = self.imagedata[0]
		print [text, fontfamily, str(size)]
		print "Blank Pixel: %s"  % (self.blankpixel)
		print "Bounds: %s, %s" % (self.bounds)
	
	def generate_text_png(self, text, fontfamily, size):
		f = ImageFont.truetype("fonts/"+ fontfamily +".ttf", size)
		w, h = f.getsize(text)
		edge = max(w, h)
		i = Image.new('L', (w, h), 255)
		d = ImageDraw.Draw(i)

		d.text((0,0), text, fill=0, font=f)

		i.save(open('output/' + text + '_' + fontfamily + '_' + str(size) + '.png', 'w'), format='PNG')
		return i.size, list(i.getdata())
		
	def is_box_filled(self, x, y, w, h):
		
		for b in range(y, y+h):
			for a in range(x, x+w):
				if self.imagedata[b*self.w + a] != self.blankpixel:
					return True
		return False