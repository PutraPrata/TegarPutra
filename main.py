import streamlit as st
from PIL import Image, ImageFilter
import os

# Fungsi untuk menerapkan efek blur menggunakan PIL
def apply_blur(image, blur_strength):
    return image.filter(ImageFilter.GaussianBlur(blur_strength))

# Fungsi untuk mengecek keberadaan file gambar
def load_image(image_path, caption):
    if os.path.exists(image_path):
        st.image(image_path, caption=caption, use_container_width=True)
    else:
        st.error(f"File gambar tidak ditemukan: {image_path}")

# Fungsi halaman utama
def page_home():
    st.title("Aplikasi Efek Blur pada Gambar")
    
    # Menampilkan logo kampus
    load_image("logo_pu.png", "Logo Kampus")
    
    st.write("Selamat datang di aplikasi efek blur pada gambar.")
    st.subheader("Anggota Tim:") 

    # Anggota tim
    members = {
        "Erza": "images/Erza.jpg",
        "Gadizza": "images/Gadizza.jpg",
        "Tegar": "images/Tegar.jpg",
        "Wahyuni": "images/Wahyuni.jpg",
    }

    # Menampilkan anggota tim secara rapi
    for name, image_path in members.items():
        with st.expander(name):  # Menggunakan expander untuk tiap anggota tim
            st.write(f"**{name}** - Anggota Tim")
            load_image(image_path, f"Foto {name}")

# Fungsi halaman efek blur
def page_blur():
    st.title("Efek Blur pada Gambar")

    # Upload gambar
    uploaded_file = st.file_uploader("Pilih gambar yang akan diblur...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Membaca gambar menggunakan Pillow
        image = Image.open(uploaded_file)

        # Menampilkan gambar asli
        st.image(image, caption="Gambar Asli", use_column_width=True)

        # Slider untuk mengatur kekuatan blur
        blur_strength = st.slider("Atur kekuatan blur (bilangan ganjil)", 1, 25, 5, step=2)

        # Menerapkan efek blur
        blurred_image = apply_blur(image, blur_strength)

        # Menampilkan gambar dengan efek blur
        st.image(blurred_image, caption="Gambar dengan Efek Blur", use_column_width=True)

# Fungsi halaman tentang
def page_about():
    st.title("Tentang Aplikasi")
    st.write("""
    Aplikasi ini dibuat untuk:
    - Menerapkan efek blur pada gambar yang diunggah.
    
    **Teknologi**:
    - Python
    - PIL (Pillow)
    - Streamlit
    """)

# Sidebar navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Beranda", "Efek Blur", "Tentang"])

# Routing halaman
if page == "Beranda":
    page_home()
elif page == "Efek Blur":
    page_blur()
elif page == "Tentang":
    page_about()
