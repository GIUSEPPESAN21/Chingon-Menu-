import streamlit as st
import os
import base64

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Chingon Cocteles | Menú Digital",
    page_icon="💀",
    layout="centered"
)

# --- ESTILOS CSS PERSONALIZADOS (TEMA NEÓN OSCURO) ---
st.markdown("""
    <style>
    /* Fondo oscuro para que resalte el Neón */
    .stApp { background-color: #0a0a0c; color: #ffffff; }
    
    /* Título principal Neón Rosa */
    h1 { 
        color: #ffffff !important; 
        text-align: center; 
        font-family: 'Arial Black', sans-serif; 
        text-transform: uppercase; 
        letter-spacing: 3px; 
        font-size: 3.4rem !important; 
        text-shadow: 0 0 10px #ff007f, 0 0 20px #ff007f, 0 0 30px #ff007f, 0 0 40px #ff007f;
        margin-bottom: 10px;
    }
    
    /* Subtítulos de categoría Neón Azul */
    h2 { 
        color: #00f3ff !important; 
        border-bottom: 2px solid rgba(0, 243, 255, 0.3); 
        padding-bottom: 10px; 
        margin-top: 40px; 
        font-weight: 900; 
        text-align: center; 
        font-size: 2.4rem !important; 
        text-shadow: 0 0 8px rgba(0, 243, 255, 0.8);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Tarjetas de producto contenedor principal Streamlit */
    [data-testid="column"] { 
        background-color: #141419; 
        padding: 15px; 
        border-radius: 16px; 
        border: 1px solid #2a2a35; 
        box-shadow: 0 8px 16px rgba(0,0,0,0.5); 
        margin-bottom: 15px;
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    }
    
    /* Efecto al pasar el mouse por encima de una bebida */
    [data-testid="column"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(255, 0, 127, 0.2);
        border-color: #ff007f;
    }

    /* Caja de promociones (Gradiente Neón) */
    .promo-box { 
        background: linear-gradient(135deg, #ff007f 0%, #7000ff 100%); 
        color: white !important; 
        padding: 15px; 
        border-radius: 10px; 
        text-align: center; 
        margin-bottom: 20px; 
        font-weight: 900; 
        box-shadow: 0 0 20px rgba(255, 0, 127, 0.4); 
        font-size: 1.3rem; 
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Ajuste de Pestañas (Tabs) */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; justify-content: center; }
    .stTabs [data-baseweb="tab-list"] button { color: #888 !important; font-size: 1.3rem !important; background-color: transparent; }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] { 
        color: #ff007f !important; 
        font-weight: 900; 
        border-bottom: 3px solid #ff007f !important; 
        text-shadow: 0 0 10px rgba(255, 0, 127, 0.6); 
    }
    
    /* Eliminar padding extra de markdown */
    .element-container st-emotion-cache-1wmy9hl { margin-bottom: 0px !important; }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("💀 CHINGON COCTELES 💀")
st.markdown("<p style='text-align: center; color: #aaaaaa; font-size: 1.2rem; letter-spacing: 1px;'>Desliza y selecciona una categoría</p>", unsafe_allow_html=True)

# --- FUNCIÓN PARA CONVERTIR IMAGEN A BASE64 ---
def get_image_base64(filepath):
    try:
        with open(filepath, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        return ""

# --- FUNCIÓN PARA MOSTRAR PRODUCTOS ---
def mostrar_productos(lista_productos):
    for i in range(0, len(lista_productos), 2):
        cols = st.columns(2)
        
        for j in range(2):
            if i + j < len(lista_productos):
                with cols[j]:
                    prod = lista_productos[i+j]
                    prod_id = prod['id']
                    nombre = prod['nombre']
                    precio = prod['precio']
                    desc = prod.get('desc', '')
                    recomendado = prod.get('recomendado', False)
                    
                    # Limpiamos el nombre de caracteres especiales para la búsqueda
                    nombre_limpio = nombre.replace("?", "")
                    
                    # 1. BÚSQUEDA EXHAUSTIVA DE IMÁGENES LOCALES
                    posibles_rutas = [
                        f"fotos/{nombre_limpio}.jpeg", f"fotos/{nombre_limpio}.jpg", f"fotos/{nombre_limpio}.png",
                        f"fotos/{prod_id}.jpeg", f"fotos/{prod_id}.jpg", f"fotos/{prod_id}.png",
                        f"fotos/{prod_id.capitalize()}.jpeg", f"fotos/{prod_id.capitalize()}.jpg",
                        f"fotos/{nombre_limpio.lower()}.jpeg", f"fotos/{nombre_limpio.title()}.jpeg"
                    ]
                    
                    ruta_img = None
                    for ruta in posibles_rutas:
                        if os.path.exists(ruta):
                            ruta_img = ruta
                            break
                    
                    # 2. Construir el bloque HTML completo para la tarjeta
                    img_html = ""
                    if ruta_img:
                        b64_img = get_image_base64(ruta_img)
                        img_html = f'<img src="data:image/jpeg;base64,{b64_img}" style="width: 100%; max-width: 300px; height: 260px; object-fit: cover; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.6); margin-bottom: 12px;">'
                    else:
                        # Búsqueda precisa del LOGO CHINGON
                        posibles_logos = [
                            "CHINGON COCTELES.jpeg", 
                            "CHINGON COCTELES.jpg",
                            "fotos/CHINGON COCTELES.jpeg", 
                            "fotos/CHINGON COCTELES.jpg"
                        ]
                        logo_path = None
                        for ruta_logo in posibles_logos:
                            if os.path.exists(ruta_logo):
                                logo_path = ruta_logo
                                break
                                
                        if logo_path:
                            b64_logo = get_image_base64(logo_path)
                            # Logo con object-fit: contain para que no se corte
                            img_html = f'<img src="data:image/jpeg;base64,{b64_logo}" style="width: 100%; max-width: 300px; height: 260px; object-fit: contain; background-color: #050505; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.6); border: 1px solid #222; margin-bottom: 12px;">'
                        else:
                            # Respaldo visual Oscuro Neón si ni el logo se encuentra
                            img_html = f'''
                                <div style="width: 100%; max-width: 300px; height: 260px; background: #0a0a0c; border-radius: 12px; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(0,0,0,0.6); border: 1px dashed #444; margin-bottom: 12px;">
                                    <div style="font-size: 3.5rem; filter: drop-shadow(0 0 10px rgba(255,0,127,0.6));">💀</div>
                                    <div style="color: #ff007f; font-weight: 900; font-size: 1.3rem; margin-top: 5px; letter-spacing: 2px; text-shadow: 0 0 8px #ff007f;">CHINGON</div>
                                    <div style="color: #666; font-size: 0.8rem; margin-top: 5px; font-style: italic;">Foto en camino...</div>
                                </div>
                            '''

                    rec_badge = "<div style='margin-bottom: 8px;'><span style='background-color: #ff007f; color: #ffffff; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 900; box-shadow: 0 0 10px rgba(255,0,127,0.8); text-transform: uppercase; letter-spacing: 1px;'>⭐ Recomendado</span></div>" if recomendado else ""
                    desc_html = f"<div style='color: #aaaaaa; font-size: 1rem; text-align: center; margin-top: 6px; line-height: 1.3; width: 100%;'>{desc}</div>" if desc else ""
                    
                    # Ensamblamos todo en un solo contenedor centrado
                    tarjeta_completa = f"""
                        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; text-align: center;">
                            {img_html}
                            {rec_badge}
                            <div style="color: #ffffff; font-weight: 900; font-size: 1.5rem; margin-bottom: 5px; line-height: 1.2; text-shadow: 0 0 8px rgba(255, 0, 127, 0.4); text-transform: uppercase; letter-spacing: 1px;">{nombre}</div>
                            <div style="color: #00ffcc; font-size: 1.6rem; font-weight: 900; margin-bottom: 5px; text-shadow: 0 0 8px rgba(0, 255, 204, 0.6);">{precio}</div>
                            {desc_html}
                        </div>
                    """
                    
                    st.markdown(tarjeta_completa, unsafe_allow_html=True)
                    
        st.write("---")

# ==========================================
# BASE DE DATOS COMPLETA 
# ==========================================

granizados_tradicionales = [
    # --- RECOMENDADOS Y PRIMEROS ---
    {"id": "catrina", "nombre": "Catrina", "precio": "$16.000", "desc": "Vodka y whisky sabor sandía y fresa. Color negro.", "recomendado": True},
    {"id": "701", "nombre": "701", "precio": "$16.000", "desc": "Fourloko sandía, whisky y tequila. Color fucsia.", "recomendado": True},
    {"id": "belico", "nombre": "Bélico", "precio": "$16.000", "desc": "Fourloko limón, lima, naranja, frambuesa. Color azul.", "recomendado": True},
    {"id": "dia_muertos", "nombre": "Día de los Muertos", "precio": "$16.000", "desc": "Champagne, granadina, vodka, tequila y kola. Rojo.", "recomendado": True},
    
    # --- DEMÁS SABORES ---
    {"id": "sinaloa", "nombre": "Sinaloa", "precio": "$16.000", "desc": "Smirnoff de lulo con apariencia color verde selva."},
    {"id": "chido", "nombre": "Chido", "precio": "$16.000", "desc": "Cachaza, maracuyá y mango maduro. Color amarillo."},
    {"id": "no_manches", "nombre": "No Manches", "precio": "$16.000", "desc": "Ginebra y manzana. Color azul."},
    {"id": "que_onda", "nombre": "Que Onda Perdida", "precio": "$16.000", "desc": "Whisky. Color fucsia."},
    {"id": "tequilazo", "nombre": "Tequilazo", "precio": "$16.000", "desc": "Tequila y mango maduro. Color naranja."},
    {"id": "que_pedo", "nombre": "Que pedo?", "precio": "$16.000", "desc": "Vodka champagne y cereza. Color rojo."},
    {"id": "la_peda", "nombre": "La Peda", "precio": "$16.000", "desc": "Whisky y tequila. Color dorado."},
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
<div style='text-align: center; color: #555555;'>
    <h4>¡Síguenos en nuestras redes!</h4>
    <p style='font-size: 1.2rem; color: #888;'>Instagram: <b style='color: #ff007f;'>@chingon.ccteles</b></p>
    <br>
    <p style='margin-bottom: 2px; font-size: 1rem;'><b>Desarrollado por:</b></p>
    <p style='margin-bottom: 2px; font-size: 1rem;'>Joseph Javier Sánchez Acuña</p>
    <p style='margin-bottom: 15px; font-size: 0.85rem; color: #888888;'>CEO - SAVA SOFTWARE FOR ENGINEERING</p>
    <p style='font-size: 1.1rem; font-weight: 800; color: #888888;'>© 2026 Chingon Cocteles. Todos los derechos reservados.</p>
</div>
""", unsafe_allow_html=True)
