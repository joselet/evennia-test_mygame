# Instalar y arrancar
crear directorio muddev y entrar dentro.

Crear un virtual environment para evennia `python3 -m venv evenv`   

Instalar/iniciar/parar

```
pip install evennia
pip install evennia[extra]
evennia --init mygame
cd mygame
evennia start
evennia restart
evennia stop
evennia reboot
```
con log:  `evennia start -l`

Después de un reinicio del host:
Cada vez que quieras activar el entorno virtual (por ejemplo depués de reiniciar)
```
source evenv/bin/activate
cd mygame
evennia start
```



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


# Personalizar el juego (básicamente temas de idioma)


## servicios
- puerto 4000 telnet  (para jugar)    telnet localhost 4000
- puerto 4001 websocket
- puerto 4002 webserver   http://localhost:4002
- administracion: http://localhost:4002/admin (entra con el usuario y contraseña de superuser)

## idioma
server/conf/settyngs.py
```
USE_I18N = True
LANGUAGE_CODE = 'es'
LOCALE_PATHS = '/home/jose/evennia/mygame/locale'
```
- Editar el fichero `locale/es/LC_MESSAGES/django.po
```
msgid "You see"
msgstr "Ves"
```
- Una vez editado, tienes que compilarlo. Para ello necesitas `apt install gettext`
```
msgfmt django.po -o django.mo
```

## la base de datos
sqlite3 evennia.db3

## mijuego/commands/command.py
Verás un ejemplo del código para "mirar". Hemos cogido el código de look, y lo hemos colocado aquí personalizando un poquito. Puedes ver el código de look original en: evennia/evennia/commands/default/general.py

Para que cargue este comando, debemos ir al fichero `commands/default_cmdsets.py` y allí añadir el comando:

- `from commands.command import CmdMirar, CmdCoger, CmdLoQueSea`, o bien: `from commands import command`
- def at_cmdset_creation(self), al final del todo pone: `self.add(CmdMirar())` o bien: `self.add(command.CmdMirar())`

## mijuego/typeclasses/objects.py
Ahí hemos sobreescrito get_numbered_name para que nos devuelva bien los números de objetos (en caso de crear dos piedras en esa room)

## mijuego/typeclasses/rooms.py
Ahí se sobreescribe el evento de cómo se devuelve lo que se ve en la habitación `return_appearance` y así hemos personalizado cómo queremos verlo, primero el nombre, despues la descripción, las salidas, etc etc.







