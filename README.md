# Instalar y arrancar
crear directorio muddev y entrar dentro.

Crear un virtual environment para evennia `python -m venv evenv`   

Después, cada vez que quieras activar el entorno virtual (por ejemplo depués de reiniciar), `source evenv/bin/activate`



pip install evennia
pip install evennia[extra]
evennia --init mygame

evennia start
evennia restart
evennia stop
evennia reboot

con log:  `evennia start -l`




# Conectar


convertirte en jugador `quell` superusuario `unquell`

# Crear una habitacion

`dig nombre = entrada,alias,alias;salida,alias`

`dig house = large red door;door;in,to the outside;out`

Y puede que le quieras cambiar el nombre.... verdad? si lo hiciste mal? pues `name #9 = casa` donde #9 es el id del objeto a cambiar
# Crear una salida

`open salida,alias = room`

`open north;n = house`

# Crear un objeto

`create box`

Renombrar objeto con `name box = gran caja;caja,box`

verla en el inventario con el comando `i` y  dejarla en la room con el comando `drop box`

podemos evitar que se pueda coger con `lock box = get:false()` recuerda: `unquell` para comportarte como jugador. Interesante: `set box/get_err_msg = Demasiado pesada para poder cogerla.`

# Ver un elemento

`examine house`

`examine roca`

## atributos persistentes:
set #id/propiedad = valor

`set roca/material = granito`

`examine roca/material` 

Para borrarlo: `set roca/material =`

# Transportar a un sitio

`teleport house` nos transporta a nosotros

Llevar un objeto a un sitio

`teleport #8 = here` llevará el objeto #8 a nuestra room

# borrar elementos
`del #8` o por ejemplo `delete roca` , o también `delete house` también podemos: `del 5-80` y nos eliminará los objetos del 5 al 80

# Ayuda
`sethelp History = Hubo una vez un momento que.....`







