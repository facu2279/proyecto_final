#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021
"""

""" IMPORTS EXTERN MODULES """

import os
import time

""" IMPORTS FILES """
import persistence

""" CALCULA CAMBIO EN 24hs  BTC"""
def porcentaje_btc_24():
    viejo = 1
    nuevo = 1
    viejo = persistence.traer_masviejo_precio_btc()
    nuevo = persistence.traer_ultimo_precio_btc()
    viejo = int(viejo)
    nuevo = int(nuevo)
    return 100 * (nuevo - viejo) / viejo

""" CALCULA CAMBIO EN 24hs DOGE"""
def porcentaje_doge_24():
    viejo = 1
    nuevo = 1
    viejo = persistence.traer_masviejo_precio_doge()
    nuevo = persistence.traer_ultimo_precio_doge()
    viejo = int(viejo)
    nuevo = int(nuevo)
    return 100 * (nuevo - viejo) / viejo

""" CALCULA CAMBIO EN 24hs ETH"""
def porcentaje_eth_24():
    viejo = 1
    nuevo = 1
    viejo = persistence.traer_masviejo_precio_eth()
    nuevo = persistence.traer_ultimo_precio_eth()
    viejo = int(viejo)
    nuevo = int(nuevo)
    return 100 * (nuevo - viejo) / viejo

""" recive two numbers and return the percent """
def caclular_porcentaje(viejo, nuevo):
    viejo = int(viejo)
    nuevo = int(nuevo)
    return 100 * (nuevo - viejo) / viejo

""" detectar constantes btc cada una hora """
def detectar_constantes_btc():
    ultimos_precios = persistence.traer_ultimos_precios_btc()
    prev = int(ultimos_precios[0])
    porcentaje = 0
    for i in range(1,60):
        if prev < int(ultimos_precios[i]):
            porcentaje = porcentaje + caclular_porcentaje(prev, ultimos_precios[i])
        elif prev > int(ultimos_precios[i]):
            porcentaje = porcentaje - caclular_porcentaje(prev, ultimos_precios[i])
        prev = int(ultimos_precios[i])
    print(porcentaje)
