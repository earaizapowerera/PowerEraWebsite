# 🚀 PowerEra Website

**Sitio web corporativo de nivel superior para PowerEra**
Diseño estilo Apple - Minimalista, profesional y moderno

---

## 📋 Descripción del Proyecto

Sitio web corporativo completo para PowerEra, mostrando productos de AI y tecnología:
- **AI Development** - Desarrollo a la medida asistido por IA (Producto Flagship)
- **AI Bots** - Chatbots inteligentes (Chatbot 2.5)
- **Actif** - Sistema de control de activos fijos
- **Waykee** - Plataforma de gestión de conversaciones
- **Helppo** - Sistema de facturación CFDI y gestión empresarial

---

## 📁 Estructura del Proyecto

```
PowerEraWebSite/
├── index.html                      # Página principal
├── README.md                       # Este archivo
├── docs/                           # Documentación completa
│   ├── PROYECTO_POWERERA_WEBSITE.md      # Overview del proyecto
│   ├── CONTENIDO_SITIO_PRINCIPAL.md      # Contenido sitio main
│   ├── CONTENIDO_AI_DEVELOPMENT.md       # Contenido micrositio AI Dev
│   ├── CONTENIDO_AI_BOTS.md              # Contenido micrositio AI Bots
│   ├── CONTENIDO_ACTIF.md                # Contenido micrositio Actif
│   ├── CONTENIDO_WAYKEE.md               # Contenido micrositio Waykee
│   ├── CONTENIDO_HELPPO.md               # Contenido micrositio Helppo
│   └── PROMPTS_IMAGENES_AI.md            # Prompts para generar imágenes
├── assets/
│   ├── css/
│   │   └── main.css                # Estilos principales (completo)
│   ├── js/
│   │   └── main.js                 # JavaScript interactivo (completo)
│   └── images/                     # Imágenes (pendiente de generar)
└── products/                       # Micrositios (pendiente de desarrollo)
    ├── ai-development/
    ├── ai-bots/
    ├── actif/
    ├── waykee/
    └── helppo/
```

---

## ✅ Estado Actual del Proyecto

### ✔️ Completado

- [x] **Estructura del proyecto** - Carpetas y organización
- [x] **Documentación completa** - 7 archivos de contenido detallado
- [x] **Sitio principal (index.html)** - 100% funcional
- [x] **CSS completo (main.css)** - Diseño responsive, estilo Apple
- [x] **JavaScript (main.js)** - Interacciones, animaciones, mobile menu
- [x] **Prompts para imágenes AI** - Listos para generar assets visuales

### ⏳ Pendiente

- [ ] **Generar imágenes con AI** - Usar prompts en `docs/PROMPTS_IMAGENES_AI.md`
- [ ] **Micrositios de productos** - HTML para cada producto (5 páginas)
- [ ] **Optimización de imágenes** - Convertir a WebP, responsive sizes
- [ ] **Testing cross-browser** - Chrome, Safari, Firefox, Edge
- [ ] **SEO optimization** - Meta tags, structured data
- [ ] **Analytics** - Google Analytics o alternativa
- [ ] **Deployment** - Hosting y dominio

---

## 🎨 Características de Diseño

### Paleta de Colores
- **Primary:** #0066FF (Azul vibrante)
- **Secondary:** #00C9FF (Azul claro)
- **Accent:** #FF6B6B (Rojo/coral para CTAs)
- **Dark:** #1A1A2E (Casi negro)
- **Light:** #F8F9FA (Gris muy claro)

### Tipografía
- **Display:** SF Pro Display / System Font
- **Body:** SF Pro Text / System Font
- Tamaños: 16-72px (responsive con clamp)

### Componentes Clave
✨ Hero section full-width con animaciones
📦 Product cards con hover effects
📊 Stats bar animada
🎯 Benefits grid
💬 CTA sections impactantes
📱 Responsive móvil perfecto
🎭 Scroll animations suaves

---

## 🚀 Cómo Usar

### 1. Abrir el Sitio Localmente

```bash
# Navega a la carpeta del proyecto
cd /Users/enrique/PowerEraWebSite

# Abre index.html en tu navegador preferido
# Opción 1: Doble click en index.html
# Opción 2: Desde terminal
open index.html  # macOS
```

### 2. Servidor Local (Recomendado)

Para evitar problemas de CORS y probar correctamente:

```bash
# Opción 1: Python Simple Server
python3 -m http.server 8000
# Luego abre: http://localhost:8000

# Opción 2: PHP Built-in Server
php -S localhost:8000

# Opción 3: Node.js http-server (si tienes npm)
npx http-server -p 8000
```

### 3. Live Reload (Desarrollo)

Para desarrollo con recarga automática:

```bash
# Instala Live Server globalmente
npm install -g live-server

# Ejecuta desde la carpeta del proyecto
cd /Users/enrique/PowerEraWebSite
live-server
```

---

## 📸 Próximos Pasos: Generar Imágenes

### Paso 1: Revisar Prompts

Abre `docs/PROMPTS_IMAGENES_AI.md` y revisa los prompts para cada imagen.

### Paso 2: Generar con AI

Usa Midjourney, DALL-E 3 o Stable Diffusion:

**Midjourney (Recomendado):**
```
/imagine prompt: [copia el prompt del documento]
--ar 16:9 --v 6 --style raw
```

**DALL-E 3 (ChatGPT Plus):**
- Copia el prompt directamente
- Pide "photorealistic, professional photography"

### Paso 3: Optimizar Imágenes

```bash
# Convertir a WebP para mejor performance
# Usa herramientas online:
# - squoosh.app (recomendado)
# - tinypng.com
# - imageoptim.com (macOS)
```

### Paso 4: Organizar Assets

```
/assets/images/
  /hero/
    - main-hero.webp (1920x1080)
    - main-hero@2x.webp (3840x2160)
  /products/
    - ai-development-hero.webp
    - ai-bots-hero.webp
    - actif-hero.webp
    - waykee-hero.webp
    - helppo-hero.webp
  /icons/
    - (iconos SVG o PNG)
```

---

## 🛠️ Desarrollo de Micrositios

Para cada producto, crear página siguiendo esta estructura:

```html
<!-- Ejemplo: products/ai-development/index.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>AI Development - PowerEra</title>
    <link rel="stylesheet" href="../../assets/css/main.css">
</head>
<body>
    <!-- Copiar header de index.html -->
    <header class="header">...</header>

    <!-- Hero específico del producto -->
    <section class="hero">
        <h1>AI Development</h1>
        <p>Desarrollo a la medida asistido por IA</p>
    </section>

    <!-- Secciones según CONTENIDO_AI_DEVELOPMENT.md -->

    <!-- Copiar footer de index.html -->
    <footer class="footer">...</footer>

    <script src="../../assets/js/main.js"></script>
</body>
</html>
```

**Referencia de contenido:** Ver archivos en `docs/CONTENIDO_*.md`

---

## 📱 Responsive Breakpoints

```css
/* Mobile First */
Default: < 768px (mobile)
Tablet: 768px - 1024px
Desktop: > 1024px
Wide: > 1440px
```

El CSS ya está optimizado para responsive. Todo funciona perfecto en mobile.

---

## 🔧 Personalización

### Cambiar Colores

Edita `/assets/css/main.css`:

```css
:root {
  --primary-color: #0066FF;    /* Cambia tu color principal */
  --secondary-color: #00C9FF;  /* Color secundario */
  --accent-color: #FF6B6B;     /* Color de acento para CTAs */
}
```

### Cambiar Contenido

Edita `/index.html` directamente. Todo el contenido está en texto plano y es fácil de modificar.

### Agregar Sección Nueva

```html
<section class="section">
    <div class="container">
        <div class="section-header">
            <div class="section-subtitle">Subtítulo</div>
            <h2 class="section-title">Título Principal</h2>
        </div>
        <!-- Tu contenido aquí -->
    </div>
</section>
```

---

## 🚀 Deployment

### Opciones de Hosting

**1. GitHub Pages (Gratis)**
```bash
# Crear repo en GitHub
git init
git add .
git commit -m "Initial commit - PowerEra Website"
git branch -M main
git remote add origin https://github.com/tu-usuario/powerera-website.git
git push -u origin main

# Activar GitHub Pages en Settings > Pages
# Source: main branch / root
```

**2. Vercel (Gratis, muy rápido)**
- Conecta tu repo de GitHub
- Deploy automático
- SSL gratis
- CDN global

**3. Netlify (Gratis)**
- Drag & drop la carpeta completa
- SSL automático
- Forms gratis

**4. Hosting Tradicional**
- Sube vía FTP toda la carpeta
- Apunta dominio a servidor
- Asegura SSL (Let's Encrypt)

---

## 📊 Performance Checklist

Antes de deployment:

- [ ] Optimizar todas las imágenes (WebP, compresión)
- [ ] Minificar CSS y JS (opcional para producción)
- [ ] Activar compresión Gzip en servidor
- [ ] Configurar cache headers
- [ ] Lazy loading para imágenes
- [ ] Preload de fuentes críticas
- [ ] Lighthouse score > 90

---

## 🐛 Troubleshooting

### Imágenes no cargan
- Verifica rutas relativas correctas
- Usa servidor local, no file://
- Revisa nombres de archivos (case-sensitive)

### Mobile menu no funciona
- Verifica que main.js esté cargando
- Abre Console (F12) y busca errores
- Verifica IDs de elementos (#mobileMenuToggle, #navMenu)

### Animaciones no funcionan
- Scroll animations requieren IntersectionObserver (IE no soportado)
- Verifica que elementos tengan clase .scroll-animate
- Algunos browsers antiguos pueden no soportar backdrop-filter

---

## 📞 Soporte

**Desarrollado para:** PowerEra
**Contacto:** +52 (55) 4630-8046
**Email:** contacto@powerera.com
**Website:** www.powerera.com

---

## 📝 Licencia

© 2025 PowerEra. Todos los derechos reservados.

---

## 🎯 Quick Start Commands

```bash
# Ver sitio localmente
cd /Users/enrique/PowerEraWebSite
python3 -m http.server 8000
# Abrir: http://localhost:8000

# Crear imágenes placeholder (mientras generas con AI)
mkdir -p assets/images/hero assets/images/products

# Iniciar Git
git init
git add .
git commit -m "Initial commit - PowerEra Website"
```

---

**🚀 El sitio principal está 100% listo para usar. Solo falta generar las imágenes y desarrollar los micrositios de productos!**

Para cualquier duda, consulta la documentación en `/docs/` o los comentarios en el código.
