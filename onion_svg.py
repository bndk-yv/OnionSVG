from lxml import etree
import cairosvg as csvg
import os

"""
Getting cairo to work on windows: 
    https://github.com/preshing/cairo-windows

    --> add cairo.dll to C:\Windows\System32
"""


def subdir(folder, filename):
    if not os.path.isdir(folder):
        os.mkdir(os.path.join(os.getcwd(), folder))
    return os.path.join(os.path.join(os.getcwd(), folder), filename)

class OnionSVG:
    def __init__(self, path: str):
        self.path = path

        with open(path, 'r') as f:
            data = f.read()
            data = bytes(data, encoding = 'UTF-8')

        self.original = data
        ddata = data.decode(encoding = 'UTF-8')
        self.header = bytes(ddata.split('<svg')[0], encoding = 'UTF-8')

        self.root = etree.fromstring(data)

        self.get_layers()

    def get_layers(self):
        self.layers = []
        self.slayers = []
        self.clayers = []
        for child in self.root.getchildren():
            if child.tag[-1] == 'g':  # child is a layer-level group # todo: find a nicer way to do this
                for attribute in child.attrib.keys():
                    try:
                        if attribute.split('}')[1] == 'label':
                            self.layers.append(Layer(child, child.attrib[attribute]))
                    except IndexError:
                        pass

    def tostring(self):
        return self.header + etree.tostring(self.root)

    def save(self, path, dpi = None):
        if dpi is None:
            dpi = 200

        csvg.svg2png(self.tostring(), write_to = path, scale = self.dpi2scale(dpi), unsafe = True)

    def save_all(self, folder, dpi = None):

        for layer in self.layers:
            for hidden in self.layers:
                hidden.hide()

            layer.show()
            self.save(subdir(folder, layer.label + '.png'), dpi)

    @staticmethod
    def dpi2scale(dpi):
        # todo: this is a bit hacky
        default_dpi = 96
        return dpi/default_dpi


class Layer:
    def __init__(self, root, label):
        self.root = root
        self.label = label

    def __repr__(self):
        if self.root.attrib['style'] == 'display:none':
            return f"<{self.label}: Hidden>"
        else:
            return f"<{self.label}: Displayed>"

    def hide(self):
        self.root.attrib['style'] = 'display:none'

    def show(self):
        self.root.attrib['style'] = 'display:inline'
