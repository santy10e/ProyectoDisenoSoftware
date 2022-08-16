from ast import If
from multiprocessing import context
from django.shortcuts import render,redirect
from . models import Cliente, Factura, Producto


def vistaPrincipal(request):
    listaClientes = Cliente.objects.all()
    context = {'listaClientes':listaClientes}
    print('ingreso al registar', listaClientes)
    if request.method == 'POST':
        print('ingreso al registar if')
        datos = request.POST.dict()
        cliente = Cliente()
        cliente.tipo_identificacion = datos.get('Identificacion')
        cliente.nombre = datos.get('nombre')
        cliente.apellido = datos.get('apellido')
        cliente.direccion = datos.get('direccion')
        cliente.telefono = datos.get('telefono')
        cliente.correo = datos.get('correo')
        if(cliente.save() != False ):
            print ("Se creó")
            return redirect('/facturacion')
    return render(request,'principal.html',context)

def registrarProducto(request):
    if request.method == 'POST':
        print('ingreso al registar if')
        datos = request.POST.dict()
        producto = Producto()
        producto.codigo = datos.get('nro')
        producto.nombre = datos.get('nombreProducto')
        producto.costoUnitario = datos.get('costoUnitario')
        if(producto.save() != False ):
            print ("Se creó Producto" )
            return redirect('/facturacion')
    return render(request,'principal.html')

def registrarFactura(request):
    listaProducto = Producto.objects.all()
    listaClientes = Cliente.objects.all()
    listaFactura = Factura.objects.all()
    context = {
        'listaProducto':listaProducto,
        'listaPersona': listaClientes,
        'listaFactura' : listaFactura           
        }
    if request.method == 'POST':
        print('ingreso al registar if')
        datos = request.POST.dict()
        factura = Factura()
        factura.nro = datos.get('nro')
        factura.cantidad = datos.get('cantidad')
        factura.costo = datos.get('costo')
        factura.fecha = datos.get('fecha')
        buscarProducto = Producto.objects.get(nombre = datos.get('nombreProducto'))
        factura.producto = buscarProducto
        buscarCliente = Cliente.objects.get(tipo_identificacion = datos.get('nombreCliente'))
        factura.cliente = buscarCliente
        if(factura.save() != False ):
            print ("Se creó")
            return redirect('/facturacion')
    return render(request,'factura.html', context)
