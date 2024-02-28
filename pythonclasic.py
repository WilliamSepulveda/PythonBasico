# hacer menu que tenga 3 categorias con 10 productos cada caŧegoria
menu = {
    "productos salados": {
        "panes": [
            {"nombre": "pan de sal", "valor": 2500},
            {"nombre": "pan de nuez", "valor": 2900},
            {"nombre": "pan de baguette", "valor": 2600},
            {"nombre": "pan de redil", "valor": 2500},
            {"nombre": "pan de 7 granos", "valor": 2300},
            {"nombre": "pan de trigo", "valor": 2200},
            {"nombre": "pan de uvas", "valor": 2100},
            {"nombre": "pan de germen de trigo", "valor": 2800},
            {"nombre": "pan de avena", "valor": 2000}
        ]
    },
    "menu dulce": {
        "panesdulces": [
            {"nombre": "Pandebono", "valor": 3000},
            {"nombre": "Conchas", "valor": 2900},
            {"nombre": "Mantecadas", "valor": 3200},
            {"nombre": "Rosquillas", "valor": 2500},
            {"nombre": "Bollitos de leche", "valor": 3300},
            {"nombre": "pan muerto", "valor": 3500},
            {"nombre": "Marquesote", "valor": 3800},
            {"nombre": "Garibaldi", "valor": 3600},
            {"nombre": "Barritas de chocolate", "valor": 3700},
            {"nombre": "cuernitos", "valor": 2500}
        ]
    },
    "pasteleria": {
        "pasteles": [
            {"nombre": "Cheesecake", "valor": 5000},
            {"nombre": "Tiramisú", "valor": 5200},
            {"nombre": "Tres Leches", "valor": 6000},
            {"nombre": "Tarta de Santiago", "valor": 7000},
            {"nombre": "Ópera", "valor": 8000}
        ],
        "promocionescategoria": [
            {"indice": 0, "descuento por compras superiores a 3": 0.02}
        ]
    }
}

print("seleccione la categoria")
listacategoria = menu.keys()
listacategoria = list(listacategoria)
for i,val in enumerate(listacategoria):
    print(f"{i}.{val}")
opcioncategoria = int(input())
datoscategoria = menu.get(listacategoria[opcioncategoria])
productoscategoria = datoscategoria["menu"]

print(f"seleccione el producto de la categoria deseada {listacategoria[opcioncategoria]}")
for i, val in  enumerate(productoscategoria):
    print(f"{i}. {val}")
opcionproducto = int(input())
datoscategoria = menu.get(listacategoria[opcioncategoria])
promocionesproducto = datoscategoria.get("promociones")

promocionproductos = list()
for val in promocionesproducto: 
    if(val.get("indice") == opcionproducto):
        promocionproductos.append(val)

if(len(promocionproductos) == 0):
    print(f"no hay promociones para el producto deseado{datoscategoria.get('producto')[opcionproducto]}")
else:
   print(f"promociones del producto son {datoscategoria.get('producto')[opcionproducto]}")
   print(promocionesproducto)
