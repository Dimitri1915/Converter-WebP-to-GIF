from PIL import Image

def convert_webp_to_gif(webp_file_path, gif_file_path):
    img = Image.open(webp_file_path)
    
    if not img.is_animated:
        print("La imagen WebP proporcionada no está animada.")
        return
    
    frames = []
    last_frame = img.n_frames - 1
    for i in range(img.n_frames):
        img.seek(i)
        frames.append(img.convert("RGB"))

    frames[0].save(gif_file_path, format="GIF", append_images=frames[1:],
                   save_all=True, duration=img.info["duration"],
                   loop=0)

    print(f"Convertido con éxito {webp_file_path} a {gif_file_path}")

# Para usar tienes que poner las imágenes del WebP en la carpeta de Importar.
webp_file_path = "Importar/el_nombre_del_archivo.webp"
gif_file_path = "Exportado/aqui_el_nombre_del_gif.gif"

convert_webp_to_gif(webp_file_path, gif_file_path)