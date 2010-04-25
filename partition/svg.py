"""\
SVG.py - Construct/display SVG scenes.

The following code is a lightweight wrapper around SVG files. The metaphor
is to construct a scene, add objects to it, and then write it to a file
to display it.

This program uses ImageMagick to display the SVG files. ImageMagick also 
does a remarkable job of converting SVG files into other formats.
"""

import os
display_prog = '/Applications/Firefox.app/Contents/MacOS/firefox-bin' # Command to execute to display images.
      
class Scene:
    def __init__(self,name="svg",height=400,width=400):
        self.name = name
        self.items = []
        self.height = height
        self.width = width
        return

    def add(self,item): self.items.append(item)

    def strarray(self):
        var = ["<?xml version=\"1.0\"?>\n",
               #"<svg height=\"%d\" width=\"%d\" >\n" % (self.height,self.width),
				"<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" baseProfile=\"full\">\n",
			   #" <image overflow=\"hidden\" xlink:href=\"text.png\" width=\"730\" height=\"320\" opacity=\"0.25\"/>\n",
               " <g style=\"fill-opacity:1.0; stroke:black;\n",
               "  stroke-width:0.5;\">\n",
			]
        for item in self.items: var += item.strarray()            
        var += [" </g>\n</svg>\n"]
        return var

    def write_svg(self,filename=None):
        if filename:
            self.svgname = filename
        else:
            self.svgname = self.name + ".svg"
        file = open(self.svgname,'w')
        file.writelines(self.strarray())
        file.close()
        return

    def write_http(self):
		print "Content-Type:image/svg+xml\n\n"
		print "".join(self.strarray())

    def display(self,prog=display_prog):
        os.system("%s %s" % (prog,self.svgname))
        return        
        

class Line:
    def __init__(self,start,end):
        self.start = start #xy tuple
        self.end = end     #xy tuple
        return

    def strarray(self):
        return ["  <line x1=\"%d\" y1=\"%d\" x2=\"%d\" y2=\"%d\" />\n" %\
                (self.start[0],self.start[1],self.end[0],self.end[1])]


class Circle:
    def __init__(self,center,radius,color):
        self.center = center #xy tuple
        self.radius = radius #xy tuple
        self.color = color   #rgb tuple in range(0,256)
        return

    def strarray(self):
        return ["  <circle cx=\"%d\" cy=\"%d\" r=\"%d\"" %\
                (self.center[0],self.center[1],self.radius),
                " %s />\n" % colorstr(self.color)]

class Rectangle:
    def __init__(self,origin,width,height,color):
        self.origin = origin
        self.height = height
        self.width = width
        self.color = color
        return

    def strarray(self):
        return ["  <rect x=\"%d\" y=\"%d\" height=\"%d\"" %\
                (self.origin[0],self.origin[1],self.height),
                " width=\"%d\" %s />\n" %\
                (self.width,colorstr(self.color))]

class Text:
    def __init__(self,origin,text,size=24):
        self.origin = origin
        self.text = text
        self.size = size
        return

    def strarray(self):
        return ["  <text x=\"%d\" y=\"%d\" font-family=\"verdana\" font-size=\"%d\">\n" %\
                (self.origin[0],self.origin[1],self.size),
                "   %s\n" % self.text,
                "  </text>\n"]
        
    
def colorstr(rgba):
	if len(rgba) == 3:
		rgba += (1.0,)
	return "fill=\"#%x%x%x\" opacity=\"%1.3f\"" % (rgba[0]/16,rgba[1]/16,rgba[2]/16,rgba[3])

def test():
    scene = Scene('test')
    scene.add(Rectangle((100,100),200,200,(0,255,255)))
    scene.add(Line((200,200),(200,300)))
    scene.add(Line((200,200),(300,200)))
    scene.add(Line((200,200),(100,200)))
    scene.add(Line((200,200),(200,100)))
    scene.add(Circle((200,200),30,(0,0,255)))
    scene.add(Circle((200,300),30,(0,255,0)))
    scene.add(Circle((300,200),30,(255,0,0)))
    scene.add(Circle((100,200),30,(255,255,0)))
    scene.add(Circle((200,100),30,(255,0,255)))
    scene.add(Text((10,100),"Testing SVG", 100))
    scene.write_svg()
    #scene.display()
    return

if __name__ == '__main__': test()
