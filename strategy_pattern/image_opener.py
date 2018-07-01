class ImageOpener:
    @staticmethod
    def open(filename):
        raise NotImplementedError()


class PNGImageOpener(ImageOpener):
    @staticmethod
    def open(filename):
        print('PNG: open with Paint')


class JPEGImageOpener(ImageOpener):
    @staticmethod
    def open(filename):
        print('JPG/JPEG: open with ImageViewer')


class SVGImageOpener(ImageOpener):
    @staticmethod
    def open(filename):
        print('SVG: open with Illustrator')


class UnkownImageOpener(ImageOpener):
    @staticmethod
    def open(filename):
        print("You don't have a program for {} extension".
              format(filename.split('.')[-1].upper()))


class Image:
    @classmethod
    def open_file(cls, filename):
        ext = filename.split('.')[-1]
        if ext == 'png':
            opener = PNGImageOpener
        elif ext in ('jpg', 'jpeg'):
            opener = JPEGImageOpener
        elif ext == 'svg':
            opener = SVGImageOpener
        else:
            opener = UnkownImageOpener

        byterange = opener.open(filename)
        return cls(byterange, filename)

    def __init__(self, byterange, filename):
        self._byterange = byterange
        self._filename = filename


Image.open_file('picture.png')
Image.open_file('picture.jpg')
Image.open_file('picture.svg')
Image.open_file('picture.raw')
