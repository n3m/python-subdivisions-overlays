from algoritmo import AlgoritmoBarrido
from Punto import Punto
from Segmento import Segmento
from Reader import getSegments


def main():
    names = ["ejemplo_01/layer01", "ejemplo_01/layer02"]
    segmentos = getSegments(names)

    # s1 = Segmento(Punto(10, 10), Punto(0, 0))
    # s2 = Segmento(Punto(10, 0), Punto(0, 10))

    # segmentos = [s1, s2]

    # for s in segmentos:
    #     print(s)

    # barr = AlgoritmoBarrido(segmentos)
    # barr.barrer()
    # print(barr.R)


if __name__ == "__main__":
    main()
