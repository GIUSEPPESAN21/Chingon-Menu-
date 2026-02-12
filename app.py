import streamlit as st
import os

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Chingon Cocteles | Menú",
    page_icon="🍹",
    layout="centered" # Ideal para visualización en celulares
)

# --- ESTILOS CSS PERSONALIZADOS ---
# Esto le da un toque moderno, oscuro y con estilo neon/mexicano
st.markdown("""
    <style>
    /* Estilo general del fondo y texto */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    /* Títulos principales */
    h1 {
        color: #00ffcc;
        text-align: center;
        font-family: 'Arial Black', sans-serif;
        text-transform: uppercase;
    }
    /* Precios resaltados */
    .precio-highlight {
        color: #ff007f;
        font-size: 1.3rem;
        font-weight: 900;
        margin-bottom: 5px;
    }
    /* Tarjetas de producto */
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] {
        background-color: #1a1c23;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #333;
        box-shadow: 0 4px 8px rgba(0,0,0,0.5);
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("💀 CHINGON COCTELES 💀")
st.markdown("<p style='text-align: center; color: #aaaaaa;'>Selecciona una categoría para ver nuestros productos</p>", unsafe_allow_html=True)

# --- FUNCIÓN INTELIGENTE PARA MOSTRAR PRODUCTOS ---
# Si la foto no existe en la carpeta, pone una imagen por defecto
DEFAULT_IMG = "https://via.placeholder.com/500x500/1a1c23/ffffff?text=Foto+Proximamente"

def mostrar_productos(lista_productos):
    # Mostrar productos en 2 columnas
    for i in range(0, len(lista_productos), 2):
        cols = st.columns(2)
        
        # Producto Columna 1
        with cols[0]:
            prod = lista_productos[i]
            ruta_img = f"fotos/{prod['id']}.jpg"
            img_mostrar = ruta_img if os.path.exists(ruta_img) else DEFAULT_IMG
            
            st.image(img_mostrar, use_container_width=True)
            st.subheader(prod["nombre"])
            st.markdown(f"<p class='precio-highlight'>{prod['precio']}</p>", unsafe_allow_html=True)
            if prod.get("desc"):
                st.caption(prod["desc"])
                
        # Producto Columna 2 (si existe)
        if i + 1 < len(lista_productos):
            with cols[1]:
                prod2 = lista_productos[i+1]
                ruta_img2 = f"fotos/{prod2['id']}.jpg"
                img_mostrar2 = ruta_img2 if os.path.exists(ruta_img2) else DEFAULT_IMG
                
                st.image(img_mostrar2, use_container_width=True)
                st.subheader(prod2["nombre"])
                st.markdown(f"<p class='precio-highlight'>{prod2['precio']}</p>", unsafe_allow_html=True)
                if prod2.get("desc"):
                    st.caption(prod2["desc"])
        st.write("---")

# --- BASE DE DATOS DEL MENÚ ---
# Aquí puedes editar textos y precios fácilmente
granizados = [
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
    {"id": "dia_muertos", "nombre": "Dia de los Muertos", "precio": "$16.000", "desc": "Champagne, granadina, vodka, tequila y kola. Rojo."},
    {"id": "carnal", "nombre": "Carnal", "precio": "$16.000", "desc": "Tequila y mango biche. Color verde."},
    {"id": "chupeta", "nombre": "Chupeta", "precio": "$16.000", "desc": "Whisky y fresa. Color rojo imperial."}
]

micheladas = [
    {"id": "mich_fresa", "nombre": "Michelada de Fresa", "precio": "$15.000", "desc": "Michelado con sal, fresas, zumo de limón y hielo."},
    {"id": "mich_enchilada", "nombre": "Michelada Enchilada", "precio": "$19.000", "desc": "Mango biche, Tajín, Takis, zumo de limón y hielo."},
    {"id": "mich_mango", "nombre": "Michelada de Mango", "precio": "$15.000", "desc": "Michelado con sal, mango, zumo de limón y hielo."},
    {"id": "mich_maracumango", "nombre": "Michelada Maracumango", "precio": "$15.000", "desc": "Mango biche, maracuyá, zumo de limón y hielo."},
    {"id": "mich_sencilla", "nombre": "Michelada Sencilla", "precio": "$8.000", "desc": "Tradicional."},
    {"id": "milo_oreo", "nombre": "Milo Oreo", "precio": "$13.000", "desc": "Crema de chocolate, chantilly y galletas Oreo."},
    {"id": "milo_ramo", "nombre": "Milo Ramito", "precio": "$13.000", "desc": "Crema de chocolate, chantilly y Chocoramo."}
]

compartir = [
    {"id": "nevecon_peq", "nombre": "Nevecon de Chela (Pequeño)", "precio": "$45.000", "desc": "Ideal para 3 a 4 personas."},
    {"id": "nevecon_gde", "nombre": "Nevecon de Chela (Grande)", "precio": "$70.000", "desc": "Ideal para 7 a 8 personas."},
    {"id": "nevecon_chingon", "nombre": "Nevecon Chingon", "precio": "$60.000", "desc": "La especialidad de la casa."},
    {"id": "puppy", "nombre": "Puppy", "precio": "$100.000", "desc": "Granizado con gomitas, perlas explosivas y 2 JP."},
    {"id": "pecera", "nombre": "La Pecera", "precio": "$50.000", "desc": "Granizado azul, fresas, naranja, gomitas y cerveza Coronita. (2-3 Personas)"},
    {"id": "cuatazo", "nombre": "Cuatazo", "precio": "$50.000", "desc": "Tequila, limón, sirope cósmico, soda. Botella exclusiva (2 Personas)."},
    {"id": "alitas", "nombre": "Combo Alitas", "precio": "$16.000", "desc": "5 Alitas + Porción de papas + Jugo Hit."}
]

ramen = [
    {"id": "ramen_b_negro", "nombre": "Buldack Bolsa Negro", "precio": "$25.000", "desc": "Incluye bowl y palitos chinos."},
    {"id": "ramen_b_carbonara", "nombre": "Buldack Carbonara", "precio": "$27.000", "desc": "Incluye bowl y palitos chinos."},
    {"id": "ramen_b_rojo", "nombre": "Buldack Bolsa Rojo", "precio": "$26.000", "desc": "Incluye bowl y palitos chinos."},
    {"id": "ramen_chapa", "nombre": "Chapaguetti", "precio": "$25.000", "desc": "Incluye bowl y palitos chinos."},
    {"id": "ramen_hello", "nombre": "Ramen Hello Kitty", "precio": "$28.000", "desc": "Incluye palitos chinos."},
    {"id": "ramen_maruchan", "nombre": "Ramen Maruchan", "precio": "$12.000", "desc": "Incluye palitos chinos."}
]

importados = [
    {"id": "skittles", "nombre": "Skittles Sour", "precio": "$35.000", "desc": ""},
    {"id": "warheads", "nombre": "Warheads Lata", "precio": "$25.000", "desc": ""},
    {"id": "starbucks_g", "nombre": "Starbucks Grande / Pink / Energy", "precio": "$40.000", "desc": "Bebida importada Starbucks."},
    {"id": "monster", "nombre": "Monster Rosado / Java", "precio": "$40.000", "desc": "Energizante importado."},
    {"id": "prime", "nombre": "Prime", "precio": "$35.000", "desc": "Bebida hidratante."}
]

# --- NAVEGACIÓN POR PESTAÑAS (TABS) ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🍹 Granizados", 
    "🌶️ Micheladas", 
    "🍻 Pa' Compartir", 
    "🍜 Ramen", 
    "🇺🇸 Importados"
])

with tab1:
    st.header("Granizados y Cócteles")
    st.info("Opciones de Tamaño: 14Oz ($16k) | 16Oz ($21k) | 24Oz ($26k)")
    mostrar_productos(granizados)

with tab2:
    st.header("Micheladas y Bebidas Dulces")
    mostrar_productos(micheladas)

with tab3:
    st.header("Para Compartir y Picar")
    mostrar_productos(compartir)

with tab4:
    st.header("Menú de Ramen Oriental")
    mostrar_productos(ramen)

with tab5:
    st.header("Dulces y Bebidas Importadas")
    mostrar_productos(importados)

# --- PIE DE PÁGINA ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown("""
<div style='text-align: center; color: #888;'>
    <h4>¡Síguenos en nuestras redes!</h4>
    <p>Instagram: <b>@chingon.ccteles</b></p>
    <p style='font-size: 10px;'>Desarrollado con 💻 por Joseph Sánchez</p>
</div>
""", unsafe_allow_html=True)
