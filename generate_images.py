#!/usr/bin/env python3
"""
Script para generar imágenes del sitio PowerEra usando DALL-E 3
Uso: python3 generate_images.py [nombre_imagen]
"""

import os
import sys
import urllib.request
from openai import OpenAI

# Leer API key desde Dalle.txt
def get_api_key():
    try:
        with open("Dalle.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("❌ Error: Archivo Dalle.txt no encontrado")
        print("Crea el archivo Dalle.txt con tu API key de OpenAI")
        sys.exit(1)

API_KEY = get_api_key()
client = OpenAI(api_key=API_KEY)

# Directorio para guardar imágenes
OUTPUT_DIR = "assets/images"

# Crear directorios si no existen
os.makedirs(f"{OUTPUT_DIR}/hero", exist_ok=True)
os.makedirs(f"{OUTPUT_DIR}/products", exist_ok=True)

# Definir prompts para cada imagen
IMAGES_PROMPTS = {
    # Hero Principal
    "main-hero": {
        "path": "hero/main-hero.png",
        "prompt": """Professional corporate workspace with dark theme, modern office environment, sleek laptop on desk showing code and AI interface with dark mode, natural window lighting, clean minimalist aesthetic, technology and innovation theme, blue cyan glow accents, professional photography style similar to Apple website, high quality, photorealistic, shallow depth of field, futuristic dark ambient""",
        "size": "1792x1024",
        "quality": "hd"
    },

    # AI Development
    "ai-development-hero": {
        "path": "products/ai-development-hero.png",
        "prompt": """Software developer working with AI coding assistant in dark theme workspace, multiple monitors with code on dark background, purple and violet ambient lighting, modern tech office, futuristic yet realistic, professional technology photography, depth of field, innovation and collaboration theme, dark aesthetic, glowing screens""",
        "size": "1792x1024",
        "quality": "hd"
    },

    # AI Bots
    "ai-bots-hero": {
        "path": "products/ai-bots-hero.png",
        "prompt": """Modern smartphone and laptop displaying chat interface with dark theme, clean messaging bubbles in conversation, professional corporate setting on desk, pink and coral glow accents, soft ambient lighting, product photography style, high quality, minimalist and clean, dark background, futuristic chat interface""",
        "size": "1792x1024",
        "quality": "hd"
    },

    # Actif
    "actif-hero": {
        "path": "products/actif-hero.png",
        "prompt": """Professional corporate fixed assets in modern warehouse: industrial machinery, company vehicles (sedans and trucks), desktop computers and monitors, office furniture and equipment, manufacturing machines, warehouse shelving systems. Organized business environment, professional photography style, blue and cyan lighting accents, clean corporate aesthetic, asset management theme, photorealistic, high quality, depth of field""",
        "size": "1792x1024",
        "quality": "hd"
    },

    # Waykee
    "waykee-hero": {
        "path": "products/waykee-hero.png",
        "prompt": """Modern desktop workspace showing collaboration software interface: laptop screen displaying chat conversations with message bubbles (WhatsApp-style), split view showing email inbox on left and kanban task board on right, smartphone beside laptop showing same chat synchronized, clean modern UI with purple gradient accents, professional product photography, organized workspace aesthetic, collaboration and teamwork theme, realistic devices, natural lighting, depth of field""",
        "size": "1792x1024",
        "quality": "hd"
    },

    # Helppo
    "helppo-hero": {
        "path": "products/helppo-hero.png",
        "prompt": """Professional accountant reviewing invoices on laptop with dark theme, Mexican CFDI electronic invoice interface visible, modern office desk with organized documents, financial management and compliance theme, orange and pink ambient glow, professional business photography, natural lighting, trust and professionalism, dark sophisticated aesthetic""",
        "size": "1792x1024",
        "quality": "hd"
    },

    # Team / About
    "team": {
        "path": "hero/team.png",
        "prompt": """Diverse professional technology team in modern office, collaborative work environment, natural interaction, Mexican and Latin American team members, authentic and inclusive, not overly staged, professional corporate photography, natural lighting, innovation and teamwork, approachable yet professional, modern tech office""",
        "size": "1792x1024",
        "quality": "hd"
    },
}


def generate_image(name, prompt, size="1792x1024", quality="hd"):
    """Genera una imagen usando DALL-E 3"""
    print(f"\n🎨 Generando: {name}")
    print(f"📝 Prompt: {prompt[:80]}...")
    print(f"📐 Size: {size}, Quality: {quality}")

    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality=quality,
            n=1,
        )

        image_url = response.data[0].url
        revised_prompt = response.data[0].revised_prompt if hasattr(response.data[0], 'revised_prompt') else None

        print(f"✅ Imagen generada exitosamente")
        if revised_prompt:
            print(f"📝 DALL-E revisó el prompt a: {revised_prompt[:100]}...")

        return image_url

    except Exception as e:
        print(f"❌ Error generando imagen: {e}")
        return None


def download_image(url, filepath):
    """Descarga la imagen desde la URL"""
    try:
        full_path = os.path.join(OUTPUT_DIR, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        print(f"⬇️  Descargando a: {full_path}")
        urllib.request.urlretrieve(url, full_path)
        print(f"✅ Guardada correctamente")

        return full_path
    except Exception as e:
        print(f"❌ Error descargando: {e}")
        return None


def main():
    """Genera una imagen específica o todas"""

    if len(sys.argv) > 1:
        # Generar imagen específica
        image_name = sys.argv[1]

        if image_name not in IMAGES_PROMPTS:
            print(f"❌ Imagen '{image_name}' no encontrada")
            print("\n📋 Imágenes disponibles:")
            for name in IMAGES_PROMPTS.keys():
                print(f"  - {name}")
            sys.exit(1)

        config = IMAGES_PROMPTS[image_name]
        url = generate_image(
            image_name,
            config["prompt"],
            config["size"],
            config["quality"]
        )

        if url:
            filepath = download_image(url, config["path"])
            if filepath:
                print(f"\n✅ IMAGEN LISTA: {filepath}")
                print(f"🔗 URL temporal: {url}")

    else:
        # Generar todas las imágenes
        print("🎨 PowerEra Image Generator")
        print("=" * 50)
        print(f"Total de imágenes a generar: {len(IMAGES_PROMPTS)}")
        total_cost = len(IMAGES_PROMPTS) * 0.12
        print(f"💰 Costo estimado: ${total_cost:.2f} USD")
        print("=" * 50)

        confirm = input("\n¿Generar todas las imágenes? (y/n): ")
        if confirm.lower() != 'y':
            print("❌ Cancelado")
            return

        for name, config in IMAGES_PROMPTS.items():
            url = generate_image(
                name,
                config["prompt"],
                config["size"],
                config["quality"]
            )

            if url:
                filepath = download_image(url, config["path"])
                if filepath:
                    print(f"✅ Guardada: {filepath}")

            print("-" * 50)

        print("\n✅ Proceso completado!")


if __name__ == "__main__":
    main()
