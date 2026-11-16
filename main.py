
# PROGRAMA PRINCIPAL DE GESTION DE CONCIERTOS

from conciertos import Concierto, Usuario, EntradaPista, EntradaGrada, EntradaVIP


def main():

    # Crear los tres conciertos
    concierto1 = Concierto("Aitana", "Madrid", 50.0, 100)
    concierto2 = Concierto("Melendi", "Sevilla", 70.0, 80)
    concierto3 = Concierto("Rosalía", "Barcelona", 40.0, 120)

    conciertos = [concierto1, concierto2, concierto3]

    # Crear los tres usuarios
    usuario1 = Usuario("Lucía", 22)
    usuario2 = Usuario("Carlos", 25)
    usuario3 = Usuario("María", 20)

    # Cada usuario compra entradas para dos conciertos
    usuario1.comprar_entrada(concierto1, "pista")
    usuario1.comprar_entrada(concierto2, "grada")

    usuario2.comprar_entrada(concierto1, "VIP")
    usuario2.comprar_entrada(concierto3, "pista")

    usuario3.comprar_entrada(concierto1, "grada")
    usuario3.comprar_entrada(concierto2, "VIP")

    # Cada usuario valora uno de sus conciertos
    usuario1.valorar(concierto1, 9)
    usuario2.valorar(concierto3, 8)
    usuario3.valorar(concierto2, 10)

    # Variables para calcular las estadisticas
    total_entradas = 0
    total_pista = 0
    total_grada = 0
    total_vip = 0

    recaudacion_total = 0.0

    concierto_mas_ventas = None
    concierto_menos_ventas = None

    mayor_ventas = -1
    menor_ventas = None

    # Recorrer los conciertos utilizando un bucle
    for concierto in conciertos:

        numero_ventas = len(concierto.entradas_vendidas)

        # Sumar el total de entradas vendidas
        total_entradas += numero_ventas

        # Sumar la recaudacion de cada concierto
        recaudacion_total += concierto.calcular_recaudacion()

        # Contar las entradas vendidas de cada tipo
        for entrada in concierto.entradas_vendidas:

            if isinstance(entrada, EntradaPista):
                total_pista += 1

            elif isinstance(entrada, EntradaGrada):
                total_grada += 1

            elif isinstance(entrada, EntradaVIP):
                total_vip += 1

        # Buscar el concierto con mas entradas vendidas
        if numero_ventas > mayor_ventas:
            mayor_ventas = numero_ventas
            concierto_mas_ventas = concierto

        # Buscar el concierto con menos entradas vendidas
        if menor_ventas is None or numero_ventas < menor_ventas:
            menor_ventas = numero_ventas
            concierto_menos_ventas = concierto

    # Calcular el precio medio de todas las entradas
    if total_entradas > 0:
        precio_medio = recaudacion_total / total_entradas
    else:
        precio_medio = 0.0

    # Mostrar las estadisticas finales
    print("=== ESTADISTICAS DE LOS CONCIERTOS ===")

    print(f"Numero total de entradas vendidas: {total_entradas}")

    print(f"Entradas de pista: {total_pista}")
    print(f"Entradas de grada: {total_grada}")
    print(f"Entradas VIP: {total_vip}")

    print(f"Recaudacion total: {recaudacion_total:.2f} €")

    print(f"Precio medio de todas las entradas: {precio_medio:.2f} €")

    print(f"Concierto con mas entradas vendidas: {concierto_mas_ventas} ({mayor_ventas})")

    print(f"Concierto con menos entradas vendidas: {concierto_menos_ventas} ({menor_ventas})")


# Ejecutar el programa
if __name__ == "__main__":
    main()
