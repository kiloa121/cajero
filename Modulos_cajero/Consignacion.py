

def consignacion(cuentas,movimientos,localtime):
    
    print ("Ingrese su numero de cuenta o numero de documento ")
    cc = input(" = ")
    for dinero in cuentas:
      if dinero["cc"] == cc or dinero["cta"] == cc:
       print(f"La cuenta a la que va a ingresar el dinero es {dinero['cta']}")
       saldo =int(input(f"Digite el monto que desea ingresar = $ "))
       #-----------------------------------------------------------------------
       dinero["saldo"] += saldo
       for movimiento in movimientos:
         if dinero["cta"] == movimiento["cta"]:
            movimiento["movimientos"].append({
              "tipo": "consignacion",
              "referencia": "",
              "descripcion": f"se ha consignado ${saldo}",
              "saldo": f"${dinero['saldo']}",
              "fecha": f"{localtime()}",             
            })
            print("Dinero consignado con exito!")
      else:
        print("Cuenta no encontrada")