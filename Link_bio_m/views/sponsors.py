import reflex as rx
import Link_bio_m.constants as const
from Link_bio_m.Componentes.title import title
from Link_bio_m.Componentes.link_sponsor import Link_sponsor
from Link_bio_m.estilo.estilo import Size as Size


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Creyente & Hijos"),
          rx.flex(
               Link_sponsor(
                    "/AvatarC.png",
                    const.CARPINTERIA, 
                    "Avatar"        
               ),
               Link_sponsor(
                    "/logocrebla.png",
                    const.CARPINTERIA, 
                    "simbolo de carpinteria"        
               ),
           spacing=Size.BIG.value,
           flex_direction=["column", "row"]

          ),
       
        width="100%",
        align_items="center",
        spacing=Size.DEFAULT.value
    )