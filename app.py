import streamlit as st
import os

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Chingon Cocteles | Menú Digital",
    page_icon="💀",
    layout="centered"
)

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    /* Fondo claro general */
    .stApp { background-color: #f8f9fa; }
    
    /* Títulos y textos principales - MÁS GRANDES Y CENTRADOS */
    h1 { color: #1a1a1a !important; text-align: center; font-family: 'Arial Black', sans-serif; text-transform: uppercase; letter-spacing: 1px; font-size: 2.8rem !important; }
    h2 { color: #d81b60 !important; border-bottom: 2px solid #e0e0e0; padding-bottom: 10px; margin-top: 30px; font-weight: 800; text-align: center; font-size: 2.2rem !important; }
    h3 { color: #333333 !important; font-weight: 700 !important; text-align: center; font-size: 1.6rem !important; }
    p, .stMarkdown p { color: #555555 !important; text-align: center; font-size: 1.2rem !important; }
    
    /* Precios resaltados (Rosa profundo) - MÁS GRANDES Y CENTRADOS */
    .precio-highlight { color: #d81b60 !important; font-size: 1.8rem; font-weight: 900; margin-bottom: 5px; text-align: center; }
    
    /* Tarjetas de producto (estilo "Card" limpio y blanco) */
    [data-testid="column"] { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #eaeaea; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.04); 
        margin-bottom: 15px;
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        justify-content: center;
    }

    /* Centrar imágenes de Streamlit */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 10px;
    }
    
    /* Caja de promociones */
    .promo-box { background-color: #d81b60; color: white !important; padding: 15px; border-radius: 10px; text-align: center; margin-bottom: 20px; font-weight: bold; box-shadow: 0 4px 10px rgba(216, 27, 96, 0.2); font-size: 1.2rem; }
    .promo-box p { color: white !important; text-align: center; }
    
    /* Ajuste de Pestañas (Tabs) */
    .stTabs [data-baseweb="tab-list"] button { color: #777 !important; font-size: 1.2rem !important; }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] { color: #d81b60 !important; font-weight: bold; border-bottom-color: #d81b60 !important; }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("💀 CHINGON COCTELES 💀")
st.markdown("<p style='text-align: center; color: #777777; font-size: 1.2rem;'>Desliza y selecciona una categoría</p>", unsafe_allow_html=True)

# --- FUNCIÓN INTELIGENTE PARA MOSTRAR PRODUCTOS ---
# Placeholder adaptado al nuevo fondo claro (URL más confiable)
DEFAULT_IMG = "https://placehold.co/500x500/f4f4f4/888888?text=Foto+Proximamente"

def mostrar_productos(lista_productos):
    for i in range(0, len(lista_productos), 2):
        cols = st.columns(2)
        
        # Producto Columna 1
        with cols[0]:
            prod = lista_productos[i]
            ruta_img = f"fotos/{prod['id']}.jpg"
            img_mostrar = ruta_img if os.path.exists(ruta_img) else DEFAULT_IMG
            
            st.image(img_mostrar, use_container_width=True)
            
            desc_html = f"<p style='color: #777; font-size: 1.1rem; text-align: center; margin-top: 5px;'>{prod['desc']}</p>" if prod.get("desc") else ""
            
            # Todo el texto agrupado y forzado al centro perfecto
            st.markdown(f"""
                <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 100%;">
                    <h3 style="color: #333333; font-weight: 700; font-size: 1.6rem; margin-bottom: 0px; margin-top: 10px;">{prod['nombre']}</h3>
                    <p class='precio-highlight' style="margin-top: 5px; margin-bottom: 5px;">{prod['precio']}</p>
                    {desc_html}
                </div>
            """, unsafe_allow_html=True)
                
        # Producto Columna 2
        if i + 1 < len(lista_productos):
            with cols[1]:
                prod2 = lista_productos[i+1]
                ruta_img2 = f"fotos/{prod2['id']}.jpg"
                img_mostrar2 = ruta_img2 if os.path.exists(ruta_img2) else DEFAULT_IMG
                
                st.image(img_mostrar2, use_container_width=True)
                
                desc_html2 = f"<p style='color: #777; font-size: 1.1rem; text-align: center; margin-top: 5px;'>{prod2['desc']}</p>" if prod2.get("desc") else ""
                
                # Todo el texto agrupado y forzado al centro perfecto
                st.markdown(f"""
                    <div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 100%;">
                        <h3 style="color: #333333; font-weight: 700; font-size: 1.6rem; margin-bottom: 0px; margin-top: 10px;">{prod2['nombre']}</h3>
                        <p class='precio-highlight' style="margin-top: 5px; margin-bottom: 5px;">{prod2['precio']}</p>
                        {desc_html2}
                    </div>
                """, unsafe_allow_html=True)
        st.write("---")

# ==========================================
# BASE DE DATOS COMPLETA (Extraída del PDF)
# ==========================================

granizados_tradicionales = [
    {"id": "sinaloa", "nombre": "Sinaloa", "precio": "$16.000", "desc": "Smirnoff de lulo con apariencia color verde selva."},
    {"id": "chido", "nombre": "Chido", "precio": "$16.000", "desc": "Cachaza, maracuyá y mango maduro. Color amarillo."},
    {"id": "belico", "nombre": "Bélico", "precio": "$16.000", "desc": "Fourloko limón, lima, naranja, frambuesa. Color azul."},
    {"id": "701", "nombre": "701", "precio": "$16.000", "desc": "Fourloko sandía, whisky y tequila. Color fucsia."},
    {"id": "catrina", "nombre": "Catrina", "precio": "$16.000", "desc": "Vodka y whisky sabor sandía y fresa. Color negro."},
    {"id": "no_manches", "nombre": "No Manches", "precio": "$16.000", "desc": "Ginebra y manzana. Color azul."},
    {"id": "que_onda", "nombre": "Que Onda Perdida", "precio": "$16.000", "desc": "Whisky. Color fucsia."},
    {"id": "tequilazo", "nombre": "Tequilazo", "precio": "$16.000", "desc": "Tequila y mango maduro. Color naranja."},
    {"id": "que_pedo", "nombre": "Que Pedo?", "precio": "$16.000", "desc": "Vodka champagne y cereza. Color rojo."},
    {"id": "la_peda", "nombre": "La Peda", "precio": "$16.000", "desc": "Whisky y tequila. Color dorado."},
    {"id": "dia_muertos", "nombre": "Día de los Muertos", "precio": "$16.000", "desc": "Champagne, granadina, vodka, tequila y kola. Rojo."},
    {"id": "carnal", "nombre": "Carnal", "precio": "$16.000", "desc": "Tequila y mango viche. Color verde."},
    {"id": "chupeta", "nombre": "Chupeta", "precio": "$16.000", "desc": "Whisky y fresa. Color rojo imperial."},
    {"id": "sin_alcohol", "nombre": "Granizado Sin Alcohol", "precio": "$16.000", "desc": "Preguntar disponibilidad."}
]

granizados_cremosos = [
    {"id": "crema_pina", "nombre": "Crema de Piña", "precio": "$18.000", "desc": "Granizado cremoso."},
    {"id": "crema_whisky", "nombre": "Crema de Whisky", "precio": "$18.000", "desc": "Granizado cremoso."},
    {"id": "explosion_fresas", "nombre": "Explosión de Fresas", "precio": "$25.000", "desc": "Smirnoff con fresas y leche condensada."}
]

compartir_y_cocteles = [
    {"id": "nevecon_peq", "nombre": "Nevecon de Chela (Pequeño)", "precio": "$45.000", "desc": "Para 3 a 4 Personas."},
    {"id": "nevecon_gde", "nombre": "Nevecon de Chela (Grande)", "precio": "$70.000", "desc": "Para 7 a 8 Personas."},
    {"id": "nevecon_chingon", "nombre": "Nevecon Chingon", "precio": "$60.000", "desc": "Especialidad de la casa."},
    {"id": "nevecon_chingon_gde", "nombre": "Nevecon Chingon Grande", "precio": "$90.000", "desc": "Especialidad tamaño familiar."},
    {"id": "puppy", "nombre": "Puppy", "precio": "$100.000", "desc": "Granizado con gomitas, perlas explosivas, bombombum y 2 JP."},
    {"id": "pecera", "nombre": "La Pecera", "precio": "$50.000", "desc": "Granizado azul, fresas, gomitas y Cerveza Coronita (2 a 3 Personas)."},
    {"id": "cuatazo", "nombre": "Cuatazo", "precio": "$50.000", "desc": "Tequila, limón, sirope cósmico, soda. Botella Exclusiva (2 Personas)."},
    {"id": "margarita", "nombre": "Margarita", "precio": "$20.000", "desc": "Cóctel tradicional."},
    {"id": "alitas", "nombre": "Combo Alitas", "precio": "$16.000", "desc": "5 Alitas + Porción de papas + Jugo Hit en caja."}
]

micheladas_milos = [
    {"id": "mich_fresa", "nombre": "Michelada de Fresa", "precio": "$15.000", "desc": "Sal, fresas, zumo de limón y hielo."},
    {"id": "mich_sencilla", "nombre": "Michelada Sencilla", "precio": "$8.000", "desc": "Tradicional."},
    {"id": "mich_enchilada", "nombre": "Michelada Enchilada", "precio": "$19.000", "desc": "Sal, pimienta, mango biche en tajín, Takis."},
    {"id": "mich_luli", "nombre": "Michelada Luli Chela", "precio": "$16.000", "desc": "Lulo, sirope de lulo, limón y choclitos."},
    {"id": "mich_mango", "nombre": "Michelada de Mango", "precio": "$15.000", "desc": "Sal, mango, zumo de limón y hielo."},
    {"id": "mich_maracumango", "nombre": "Michelada Maracumango", "precio": "$15.000", "desc": "Mango biche, maracuyá, limón y hielo."},
    {"id": "mich_cereza", "nombre": "Michelada de Cereza", "precio": "$15.000", "desc": "Cereza, limón y hielo."},
    {"id": "mich_maracuya", "nombre": "Michelada de Maracuyá", "precio": "$15.000", "desc": "Maracuyá, limón y hielo."},
    {"id": "milo_oreo", "nombre": "Milo Oreo", "precio": "$13.000", "desc": "Crema de chocolate, chantilly y galletas Oreo."},
    {"id": "milo_ramo", "nombre": "Milo Ramito", "precio": "$13.000", "desc": "Crema de chocolate, chantilly y Chocoramo."}
]

ramen = [
    {"id": "ramen_b_negro", "nombre": "Buldack Bolsa Negro", "precio": "$25.000", "desc": "Incluye bowl y palitos chinos."},
    {"id": "ramen_b_carbonara", "nombre": "Buldack Carbonara", "precio": "$27.000", "desc": "Incluye bowl y palitos chinos."},
    {"id": "ramen_b_rojo", "nombre": "Buldack Bolsa Rojo", "precio": "$26.000", "desc": "Incluye bowl y palitos chinos."},
    {"id": "ramen_chapa", "nombre": "Chapaguetti Bolsa", "precio": "$25.000", "desc": "Incluye bowl y palitos chinos."},
    {"id": "ramen_hello", "nombre": "Ramen Hello Kitty", "precio": "$28.000", "desc": "Incluye palitos chinos."},
    {"id": "ramen_maruchan", "nombre": "Ramen Maruchan", "precio": "$12.000", "desc": "Incluye palitos chinos."},
    {"id": "ramen_nissi", "nombre": "Ramen Nissi", "precio": "$10.000", "desc": "Incluye bowl y palitos chinos."},
    {"id": "ramen_ajinomen_tarro", "nombre": "Ramen Ajinomen Tarro", "precio": "$12.000", "desc": "Incluye palitos chinos."},
    {"id": "ramen_ajinomen_bolsa", "nombre": "Ramen Ajinomen Bolsa", "precio": "$10.000", "desc": "Incluye bowl y palitos chinos."},
    {"id": "ramen_kimchi", "nombre": "Ramen Kimchi", "precio": "$17.000", "desc": "Incluye palitos chinos."},
    {"id": "ramen_nudels", "nombre": "Ramen Nudels", "precio": "$14.000", "desc": "Incluye palitos chinos."}
]

importados = [
    {"id": "skittles", "nombre": "Skittles Sour", "precio": "$35.000", "desc": ""},
    {"id": "warheads", "nombre": "Warheads Lata", "precio": "$25.000", "desc": ""},
    {"id": "starbucks_g", "nombre": "Starbucks Grande", "precio": "$40.000", "desc": ""},
    {"id": "starbucks_pink", "nombre": "Starbucks Pink", "precio": "$40.000", "desc": ""},
    {"id": "starbucks_energy", "nombre": "Starbucks Energy", "precio": "$40.000", "desc": ""},
    {"id": "starbucks_p", "nombre": "Star Bucks Pequeño", "precio": "$25.000", "desc": ""},
    {"id": "dunkin", "nombre": "Dunkin", "precio": "$35.000", "desc": ""},
    {"id": "pacman", "nombre": "Pacman Lata", "precio": "$35.000", "desc": ""},
    {"id": "monster_rosado", "nombre": "Monster Rosado", "precio": "$40.000", "desc": ""},
    {"id": "monster_java", "nombre": "Monster Java", "precio": "$40.000", "desc": ""},
    {"id": "prime", "nombre": "Prime", "precio": "$35.000", "desc": ""},
    {"id": "rockstar", "nombre": "Rockstar", "precio": "$35.000", "desc": ""},
    {"id": "mtn_dew", "nombre": "Mtn Dew", "precio": "$24.000", "desc": ""},
    {"id": "coffi", "nombre": "Coffi Lata", "precio": "$12.000", "desc": ""}
]

otras_bebidas_licores = [
    {"id": "coronita", "nombre": "Coronita", "precio": "$6.000", "desc": ""},
    {"id": "aguila", "nombre": "Aguila", "precio": "$6.000", "desc": ""},
    {"id": "corona", "nombre": "Corona", "precio": "$12.000", "desc": ""},
    {"id": "gatorade", "nombre": "Gatorade", "precio": "$6.000", "desc": ""},
    {"id": "electrolit", "nombre": "Electrolit", "precio": "$12.000", "desc": ""},
    {"id": "postobon", "nombre": "Gaseosa Postobon", "precio": "$5.000", "desc": ""},
    {"id": "cocacola", "nombre": "Coca-Cola", "precio": "$6.000", "desc": ""},
    {"id": "agua", "nombre": "Agua", "precio": "$4.000", "desc": ""},
    {"id": "sodas", "nombre": "Sodas", "precio": "$4.000", "desc": ""},
    {"id": "soda_italiana", "nombre": "Soda Italiana", "precio": "$14.000", "desc": ""},
    {"id": "smirnoff_botella", "nombre": "Smirnoff", "precio": "$16.000", "desc": ""},
    {"id": "four_loko", "nombre": "Four Loko", "precio": "$24.000", "desc": ""},
    {"id": "jp", "nombre": "JP", "precio": "$16.000", "desc": ""},
    {"id": "monster_tradicional", "nombre": "Monster Tradicional", "precio": "$14.000", "desc": ""},
    {"id": "speed_max", "nombre": "Speed Max", "precio": "$5.000", "desc": ""},
    {"id": "caneca_aguardiente", "nombre": "Caneca Aguardiente", "precio": "$40.000", "desc": ""},
    {"id": "botella_aguardiente", "nombre": "Botella Aguardiente", "precio": "$70.000", "desc": ""},
    {"id": "shot_chivas", "nombre": "Shot Chivas", "precio": "$24.000", "desc": ""},
    {"id": "shot_vodka", "nombre": "Shot Vodka", "precio": "$16.000", "desc": ""},
    {"id": "shot_jager", "nombre": "Shot Jägermeister", "precio": "$18.000", "desc": ""}
]

dulceria_extras = [
    {"id": "gomas_s", "nombre": "Gomas Enchiladas Tamaño S", "precio": "$10.000", "desc": ""},
    {"id": "gomas_m", "nombre": "Gomas Enchiladas Tamaño M", "precio": "$15.000", "desc": ""},
    {"id": "gomas_l", "nombre": "Gomas Enchiladas Tamaño L", "precio": "$19.000", "desc": ""},
    {"id": "jeringa_peq", "nombre": "Jeringas de Veneno Pequeña", "precio": "$3.000", "desc": ""},
    {"id": "jeringa_gde", "nombre": "Jeringas de Veneno Grande", "precio": "$5.000", "desc": ""},
]


# --- NAVEGACIÓN POR PESTAÑAS (TABS) ---
tabs = st.tabs([
    "🍹 Granizados", 
    "🌶️ Micheladas", 
    "🍻 Compartir", 
    "🍜 Ramen", 
    "🇺🇸 Importados",
    "🍺 Bebidas",
    "🎉 Promos"
])

with tabs[0]:
    st.markdown("<div class='promo-box'>Tamaños: 14 Oz ($16.000) | 16 Oz ($21.000) | 24 Oz ($26.000)</div>", unsafe_allow_html=True)
    st.header("Granizados Tradicionales")
    mostrar_productos(granizados_tradicionales)
    
    st.header("Granizados Cremosos y Dulces")
    mostrar_productos(granizados_cremosos)

with tabs[1]:
    st.header("Micheladas y Milos")
    mostrar_productos(micheladas_milos)

with tabs[2]:
    st.header("Pa' Compartir y Picar")
    mostrar_productos(compartir_y_cocteles)

with tabs[3]:
    st.header("Menú de Ramen Oriental")
    mostrar_productos(ramen)

with tabs[4]:
    st.header("Bebidas Importadas")
    mostrar_productos(importados)

with tabs[5]:
    st.header("Otras Bebidas y Licores")
    mostrar_productos(otras_bebidas_licores)
    
    st.header("Dulcería y Extras")
    mostrar_productos(dulceria_extras)

with tabs[6]:
    st.header("Experiencias y Promociones")
    st.success("🎨 **¡SOMOS ARTE!** Podrás también pintar mientras disfrutas de un granizado. Pintura en cerámica + Pincel + Vinilo.")
    st.info("🔥 **LUNES DE AMIGOS:** ¡Compra 2 granizados y llevas el 3ro GRATIS!")
    st.warning("💉 **MARTES DE VENENO:** ¡Jeringa GRATIS para todos los granizados!")
    st.error("🛍️ ¡Contamos con Dulcería Mexicana y Oriental! Ya disponibles TERMOS.")

# --- PIE DE PÁGINA ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown("""
<div style='text-align: center; color: #888;'>
    <h4>¡Síguenos en nuestras redes!</h4>
    <p>Instagram: <b>@chingon.ccteles</b></p>
    <p style='font-size: 10px;'>Desarrollo Web y Menú QR por Joseph Sánchez</p>
</div>
""", unsafe_allow_html=True)
