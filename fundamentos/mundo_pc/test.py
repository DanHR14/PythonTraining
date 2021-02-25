from orden import Orden
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado

teclado_hp = Teclado("Hp", "usb")
raton_hp = Raton("Hp", "usb")
monitor_hp = Monitor("Hp", "15 pulgadas")
computadora_hp = Computadora("Hp", monitor_hp, teclado_hp, raton_hp)

teclado_acer = Teclado("Acer", "bluetooth")
raton_acer = Raton("Acer", "bluetooth")
monitor_acer = Monitor("Acer", "27 pulgadas")
computadora_acer = Computadora("Acer", monitor_acer, teclado_acer, raton_acer)

teclado_gamer = Teclado("Gamer", "bluetooth")
raton_gamer = Raton("Gamer", "bluetooth")
monitor_gamer = Monitor("Gamer", "45 pulgadas")
computadora_gamer = Computadora("Gamer", monitor_gamer, teclado_gamer, raton_gamer)

computadoras_orden1 = [computadora_hp, computadora_acer]
orden1 = Orden(computadoras_orden1)
print(orden1)

computadoras_orden2 = [computadora_gamer]
orden2 = Orden(computadoras_orden2)
orden2.agregar_computadora(computadora_hp)
print(orden2)
