"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia.objects.objects import DefaultRoom

from .objects import ObjectParent


class Room(ObjectParent, DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See mygame/typeclasses/objects.py for a list of
    properties and methods available on all Objects.
    """

    pass


# en español el retorno de como se mira la habitación
from evennia.objects.objects import DefaultRoom
from .objects import ObjectParent
from evennia.utils import iter_to_str # Importante añadir esta línea arriba

class Room(ObjectParent, DefaultRoom):
    """
    Habitaciones personalizadas para mi MUD en español.
    """

    def return_appearance(self, looker, **kwargs):
        if not looker:
            return ""

        # 1. Nombre y descripción de la sala
        #if looker.is_superuser:
        #    string += f"|c{self.get_display_name(looker)}|n(#{self.id})"
        #else:
        #    string += f"|c{self.get_display_name(looker)}|n"
        string = f"|c{self.get_display_name(looker)}|n(#{self.id})"

        if self.db.desc:
            string += f"\n{self.db.desc}"

        # 2. Organizar contenidos
        users = []
        things = []
        
        # Agrupamos objetos iguales para usar tu nuevo 'get_numbered_name'
        from collections import defaultdict
        grouped_items = defaultdict(list)
        
        for obj in self.contents:
            if obj == looker:
                continue
            if obj.has_account:
                users.append(obj.get_display_name(looker))
            else:
                # Agrupamos por el nombre base para que 'get_numbered_name' funcione
                grouped_items[obj.key].append(obj)

        # Procesamos los objetos agrupados (piedras, papeles, etc.)
        for key, item_list in grouped_items.items():
            n = len(item_list)
            # Llamamos a tu función mágica que ya traduce números y plurales
            singular, plural_numerado = item_list[0].get_numbered_name(n, looker)
            things.append(plural_numerado if n > 1 else key)

        # 3. Función auxiliar para evitar el error de 'iter_to_str'
        def listar_es(lista):
            if not lista: return ""
            if len(lista) == 1: return lista[0]
            return ", ".join(lista[:-1]) + " y " + lista[-1]

        # 4. Construir el mensaje final
        if users:
            string += "\n|wPersonas aquí:|n " + listar_es(users)
        if things:
            string += "\n|wPuedes ver:|n " + listar_es(things)

        # 5. Salidas
        exits = [ex.get_display_name(looker) for ex in self.contents_get(content_type="exit")]
        if exits:
            string += "\n|wSalidas:|n " + listar_es(exits)

        return string
