import streamlit as st
import os
import hashlib

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
    
    /* Títulos y textos principales */
    h1 { color: #1a1a1a !important; text-align: center; font-family: 'Arial Black', sans-serif; text-transform: uppercase; letter-spacing: 1px; font-size: 2.8rem !important; }
    h2 { color: #d81b60 !important; border-bottom: 2px solid #e0e0e0; padding-bottom: 10px; margin-top: 30px; font-weight: 800; text-align: center; font-size: 2.2rem !important; }
    
    /* Precios resaltados (Rosa profundo) */
    .precio-highlight { color: #d81b60 !important; font-size: 1.8rem; font-weight: 900; margin-bottom: 5px; text-align: center; }
    
    /* Tarjetas de producto */
    [data-testid="column"] { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #eaeaea; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.04); 
        margin-bottom: 15px;
    }

    /* Forzar centrado absoluto */
    [data-testid="column"] [data-testid="stMarkdownContainer"] {
        text-align: center !important;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
    }
    
    /* Caja de promociones */
    .promo-box { background-color: #d81b60; color: white !important; padding: 15px; border-radius: 10px; text-align: center; margin-bottom: 20px; font-weight: bold; box-shadow: 0 4px 10px rgba(216, 27, 96, 0.2); font-size: 1.2rem; }
    .promo-box p { color: white !important; text-align: center; }
    
    /* Ajuste de Pestañas (Tabs) */
    .stTabs [data-baseweb="tab-list"] button { color: #777 !important; font-size: 1.2rem !important; }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] { color: #d81b60 !important; font-weight: bold; border-bottom-color: #d81b60 !important; }
    
    /* Bordes redondeados para todas las imágenes */
    [data-testid="stImage"] img { border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("💀 CHINGON COCTELES 💀")
st.markdown("<p style='text-align: center; color: #777777; font-size: 1.2rem;'>Desliza y selecciona una categoría</p>", unsafe_allow_html=True)

# --- FUNCIÓN INTELIGENTE DE IMÁGENES "COOL" DE INTERNET ---
def obtener_imagen_cool(prod_id, nombre):
    # 1. Mapeo exacto para productos clave (¡Imágenes que coinciden con la descripción real y el COLOR!)
    exact_matches = {
        # --- GRANIZADOS POR COLOR ---
        "sinaloa": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80", # Cóctel Verde
        "chido": "https://images.unsplash.com/photo-1541544741938-0af808871cc0?w=600&q=80", # Cóctel Amarillo
        "belico": "https://images.unsplash.com/photo-1544145945-f9042538a7f5?w=600&q=80", # Cóctel Azul
        "701": "https://images.unsplash.com/photo-1536935338788-846bb9981813?w=600&q=80", # Cóctel Fucsia/Rojo
        "catrina": "https://images.unsplash.com/photo-1510626176961-4b57d4fbad03?w=600&q=80", # Cóctel Oscuro/Negro
        "no_manches": "https://images.unsplash.com/photo-1544145945-f9042538a7f5?w=600&q=80", # Cóctel Azul
        "que_onda": "https://images.unsplash.com/photo-1536935338788-846bb9981813?w=600&q=80", # Cóctel Fucsia
        "tequilazo": "https://images.unsplash.com/photo-1546171753-97d7676e4602?w=600&q=80", # Cóctel Naranja
        "que_pedo": "https://images.unsplash.com/photo-1551538827-9c037cb4f32a?w=600&q=80", # Cóctel Rojo
        "la_peda": "https://images.unsplash.com/photo-1587223075055-82e9a937ddff?w=600&q=80", # Cóctel Dorado/Amarillo
        "dia_muertos": "https://images.unsplash.com/photo-1551538827-9c037cb4f32a?w=600&q=80", # Cóctel Rojo
        "carnal": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80", # Cóctel Verde
        "chupeta": "https://images.unsplash.com/photo-1551538827-9c037cb4f32a?w=600&q=80", # Cóctel Rojo Imperial
        
        # --- OTROS PRODUCTOS ---
        "alitas": "https://images.unsplash.com/photo-1608039829572-78524f79c4c7?w=600&q=80", # Alitas BBQ reales
        "margarita": "https://images.unsplash.com/photo-1587223075055-82e9a937ddff?w=600&q=80", # Margarita clásica
        "cocacola": "https://images.unsplash.com/photo-1554866585-cd94860874b7?w=600&q=80", # Lata Coca-Cola
        "agua": "https://images.unsplash.com/photo-1548839140-29a749e1bc4c?w=600&q=80", # Agua
        "coronita": "https://images.unsplash.com/photo-1614316111861-c3b0dfb5e7d8?w=600&q=80", # Corona
        "corona": "https://images.unsplash.com/photo-1614316111861-c3b0dfb5e7d8?w=600&q=80",
        "monster_tradicional": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=600&q=80",
        "starbucks_g": "https://images.unsplash.com/photo-1559525839-b184a4d698c7?w=600&q=80",
        "mich_fresa": "https://images.unsplash.com/photo-1551538827-9c037cb4f32a?w=600&q=80", # Michelada fresa
        "mich_mango": "https://images.unsplash.com/photo-1546171753-97d7676e4602?w=600&q=80",
        "milo_oreo": "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=600&q=80",
        "puppy": "https://images.unsplash.com/photo-1536935338788-846bb9981813?w=600&q=80", 
        "pecera": "https://images.unsplash.com/photo-1544145945-f9042538a7f5?w=600&q=80", 
    }
    if prod_id in exact_matches:
        return exact_matches[prod_id]

    # 2. Listas de imágenes variadas para evitar repeticiones en la misma categoría
    ramenes = [
        "https://images.unsplash.com/photo-1557872943-16a5ac26437e?w=600&q=80",
        "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=600&q=80",
        "https://images.unsplash.com/photo-1591814468924-caf88d1232e1?w=600&q=80",
        "https://images.unsplash.com/photo-1614563637806-1d0e645e0940?w=600&q=80"
    ]
    cervezas = [
        "https://images.unsplash.com/photo-1567171466295-4afa63d45416?w=600&q=80",
        "https://images.unsplash.com/photo-1625750346808-1f558a2d16be?w=600&q=80",
        "https://images.unsplash.com/photo-1535958636474-b021ee887b13?w=600&q=80"
    ]
    dulces = [
        "https://images.unsplash.com/photo-1582058091505-f87a2e55a40f?w=600&q=80",
        "https://images.unsplash.com/photo-1570831739435-6601aa3fa4fb?w=600&q=80",
        "https://images.unsplash.com/photo-1499195333224-3ce974eecb47?w=600&q=80"
    ]
    cocteles = [
        "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600&q=80",
        "https://images.unsplash.com/photo-1551538827-9c037cb4f32a?w=600&q=80",
        "https://images.unsplash.com/photo-1546171753-97d7676e4602?w=600&q=80",
        "https://images.unsplash.com/photo-1587223075055-82e9a937ddff?w=600&q=80",
        "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80"
    ]
    shots_licores = [
        "https://images.unsplash.com/photo-1516531737409-f6ba6df21a16?w=600&q=80",
        "https://images.unsplash.com/photo-1560512823-829485b8bf24?w=600&q=80",
        "https://images.unsplash.com/photo-1582222308731-89a31a78d06b?w=600&q=80"
    ]
    latas_sodas = [
        "https://images.unsplash.com/photo-1629203851288-7ececa5f05c4?w=600&q=80",
        "https://images.unsplash.com/photo-1603392813589-73f1a26ae678?w=600&q=80",
        "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=600&q=80"
    ]

    # Usamos un hash matemático del ID para elegir siempre la MISMA imagen para un producto, 
    # pero distribuyendo equitativamente entre las opciones para que no se repitan unas con otras.
    idx = int(hashlib.md5(prod_id.encode('utf-8')).hexdigest(), 16)
    
    nombre_lower = nombre.lower()
    if "ramen" in nombre_lower or "buldack" in nombre_lower or "chapaguetti" in nombre_lower:
        return ramenes[idx % len(ramenes)]
    elif "michelada" in nombre_lower or "coronita" in nombre_lower or "cerveza" in nombre_lower or "aguila" in nombre_lower or "corona" in nombre_lower:
        return cervezas[idx % len(cervezas)]
    elif "gomas" in nombre_lower or "skittles" in nombre_lower or "dulce" in nombre_lower or "warheads" in nombre_lower or "jeringa" in nombre_lower:
        return dulces[idx % len(dulces)]
    elif "shot" in nombre_lower or "botella" in nombre_lower or "caneca" in nombre_lower or "jp" in nombre_lower or "aguardiente" in nombre_lower:
        return shots_licores[idx % len(shots_licores)]
    elif "monster" in nombre_lower or "soda" in nombre_lower or "agua" in nombre_lower or "coca" in nombre_lower or "prime" in nombre_lower or "postobon" in nombre_lower or "gatorade" in nombre_lower:
        return latas_sodas[idx % len(latas_sodas)]
    else:
        return cocteles[idx % len(cocteles)]


# --- FUNCIÓN PARA MOSTRAR PRODUCTOS ---
def mostrar_productos(lista_productos):
    for i in range(0, len(lista_productos), 2):
        cols = st.columns(2)
        
        for j in range(2):
            if i + j < len(lista_productos):
                with cols[j]:
                    prod = lista_productos[i+j]
                    prod_id = prod['id']
                    
                    # 1. BÚSQUEDA EXHAUSTIVA DE IMÁGENES LOCALES
                    posibles_rutas = [
                        f"fotos/{prod_id}.jpeg", f"fotos/{prod_id}.jpg", f"fotos/{prod_id}.png",
                        f"fotos/{prod_id.lower()}.jpeg", f"fotos/{prod_id.lower()}.jpg",
                        f"fotos/{prod_id.capitalize()}.jpeg", f"fotos/{prod_id.capitalize()}.jpg",
                        f"fotos/{prod_id.upper()}.jpeg", f"fotos/{prod_id.upper()}.jpg",
                    ]
                    
                    ruta_img = None
                    for ruta in posibles_rutas:
                        if os.path.exists(ruta):
                            ruta_img = ruta
                            break
                    
                    # 2. Asignar la imagen "Cool" si no encontraste foto local
                    if not ruta_img:
                        ruta_img = obtener_imagen_cool(prod_id, prod['nombre'])

                    st.image(ruta_img, use_container_width=True)
                    
                    # 3. Textos agrupados y centrados
                    desc_html = f"<div style='color: #777; font-size: 1.1rem; text-align: center; margin-top: 8px; line-height: 1.4; width: 100%;'>{prod['desc']}</div>" if prod.get("desc") else ""
                    st.markdown(f"""
                        <div style="text-align: center; width: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div style="color: #333333; font-weight: 800; font-size: 1.6rem; margin-bottom: 5px; text-align: center; width: 100%;">{prod['nombre']}</div>
                            <div class='precio-highlight' style="margin-bottom: 5px; text-align: center; width: 100%;">{prod['precio']}</div>
                            {desc_html}
                        </div>
                    """, unsafe_allow_html=True)
                    
        st.write("---")

# ==========================================
# BASE DE DATOS COMPLETA 
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
    # --- AQUÍ ESTÁ LA CORRECCIÓN DE TAMAÑOS ---
    st.markdown("<div class='promo-box'>Tamaños: 12 Oz ($16.000) | 16 Oz ($21.000) | 24 Oz ($26.000)</div>", unsafe_allow_html=True)
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
<div style='text-align: center; color: #555555;'>
    <h4>¡Síguenos en nuestras redes!</h4>
    <p style='font-size: 1.2rem;'>Instagram: <b>@chingon.ccteles</b></p>
    <br>
    <p style='margin-bottom: 2px; font-size: 1rem;'><b>Desarrollado por:</b></p>
    <p style='margin-bottom: 2px; font-size: 1rem;'>Joseph Javier Sánchez Acuña</p>
    <p style='margin-bottom: 15px; font-size: 0.85rem; color: #888888;'>CEO - SAVA SOFTWARE FOR ENGINEERING</p>
    <p style='font-size: 1.1rem; font-weight: 800; color: #333333;'>© 2026 Chingon Cocteles. Todos los derechos reservados.</p>
</div>
""", unsafe_allow_html=True)
