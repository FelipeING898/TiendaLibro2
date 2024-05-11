class Libro: 
    def __init__(self, isbn, titulo, precioVenta, precioCompra, cantidadActual, rutaImagen):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__precioVenta = precioVenta
        self.__precioCompra = precioCompra
        self.__cantidadActual = cantidadActual
        self.__rutaImagen = rutaImagen

    def getTitulo(self):
        return self.__titulo

    def getIsbn(self):
        return self.__isbn
    
    def getPrecioVenta(self):
        return self.__precioVenta
    
    def getPrecioCompra(self):
        return self.__precioCompra

    def getcantidadActual(self):
        return self.__cantidadActual 

    def rutaImagen(self):
        return self.__rutaImagenb

