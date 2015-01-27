
"""\
SVG.py - Construct/display SVG scenes.

credit goes to Rick Muller at:
http://code.activestate.com/recipes/325823-draw-svg-images-in-python/

The following code is a lightweight wrapper around SVG files. The metaphor
is to construct a scene, add objects to it, and then write it to a file
to display it.

This program uses ImageMagick to display the SVG files. ImageMagick also
does a remarkable job of converting SVG files into other formats.
"""

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
               "<svg height=\"%d\" width=\"%d\" xmlns=\"http://www.w3.org/2000/svg\" >\n" % (self.height,self.width),
               " <g style=\"fill-opacity:1.0; stroke:none;\n", #stroke:black
               "  stroke-width:1;\">\n"]
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


class Circle:
    def __init__(self,center,radius,color,opacity=1.0):
        self.center = center #xy tuple
        self.radius = radius #xy tuple

        if len(color) <=3:
            color = color + (255 * opacity,) #supporting rgb and rgba color inputs

        self.color = color   #rgb tuple in range(0,256)
        self.opacity = opacity
        return

    def strarray(self):
        return ["  <circle cx=\"%d\" cy=\"%d\" r=\"%d\"\n" %\
                (self.center[0],self.center[1],self.radius),
                "    style=\"fill:%s; fill-opacity:%s;\" />\n" % colortuple(self.color)]



def colortuple(rgba): return ("#%x%x%x" % (rgba[0]/16,rgba[1]/16,rgba[2]/16,), str(rgba[3]/255.0))
