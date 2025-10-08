# 🚀 PowerEra Website - Deployment Guide

Guía completa para retomar desarrollo y deployment del sitio web de PowerEra.

## 📋 Información General

- **URL Producción:** https://www.powerera.com
- **URL Test:** https://wwwtest.powerera.com
- **Repositorio:** https://github.com/earaizapowerera/PowerEraWebsite
- **Stack:** HTML5, CSS3, JavaScript (sitio estático)
- **Tema:** Dark mode, estilo Apple
- **Servidor:** wk2.waykee.com (Azure VM)

## 🚀 Deployment a Producción

### Servidor y Configuración

**Servidor:** wk2.waykee.com
**Usuario:** earaiza
**SSH Key:** `~/.ssh/id_claude_automation`
**Carpeta del sitio:** `/var/www/powerera-website`
**Puerto interno:** 5070 (Python HTTP Server)
**Puerto externo:** 443 (HTTPS via Nginx)

### Conexión SSH

```bash
ssh -i ~/.ssh/id_claude_automation earaiza@wk2.waykee.com
```

### Servicio Systemd

El sitio corre como servicio systemd: `powerera-web.service`

**Archivo de servicio:** `/etc/systemd/system/powerera-web.service`

```ini
[Unit]
Description=PowerEra Website
After=network.target

[Service]
Type=simple
User=earaiza
WorkingDirectory=/var/www/powerera-website
ExecStart=/usr/bin/python3 -m http.server 5070
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Comandos útiles:**

```bash
# Ver status del servicio
sudo systemctl status powerera-web

# Reiniciar servicio
sudo systemctl restart powerera-web

# Ver logs
sudo journalctl -u powerera-web -f
```

### Nginx Reverse Proxy

**Configuración:** `/etc/nginx/sites-available/www.powerera.com.conf`

```nginx
server {
    listen 80;
    server_name www.powerera.com;

    location / {
        proxy_pass http://localhost:5070;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

# HTTPS config added automatically by certbot
```

**Recargar Nginx:**

```bash
sudo nginx -t  # Test configuration
sudo systemctl reload nginx
```

### SSL/HTTPS

**Certificado:** Let's Encrypt (certbot)
**Expira:** 2026-01-05
**Renovación:** Automática

**Generar certificado para nuevo dominio:**

```bash
sudo certbot --nginx -d nuevo.dominio.com --non-interactive --agree-tos --email enrique@powerera.com --redirect
```

### DNS (GoDaddy)

**Script para crear CNAMEs:** `/Users/enrique/create_cname.sh`
**Credenciales:** `/Users/enrique/.godaddy_credentials`

```bash
# Crear CNAME
bash /Users/enrique/create_cname.sh SUBDOMINIO DESTINO

# Ejemplo
bash /Users/enrique/create_cname.sh www wk2.waykee.com
```

## 📤 Subir Cambios a Producción

### Método 1: Subir archivos específicos

```bash
# Subir archivo individual
scp -i ~/.ssh/id_claude_automation /ruta/local/archivo.html earaiza@wk2.waykee.com:/var/www/powerera-website/ruta/archivo.html

# Subir página de producto
scp -i ~/.ssh/id_claude_automation /Users/enrique/PowerEraWebSite/products/actif/index.html earaiza@wk2.waykee.com:/var/www/powerera-website/products/actif/

# Subir homepage
scp -i ~/.ssh/id_claude_automation /Users/enrique/PowerEraWebSite/index.html earaiza@wk2.waykee.com:/var/www/powerera-website/

# Subir imágenes
scp -i ~/.ssh/id_claude_automation /Users/enrique/PowerEraWebSite/assets/images/products/*.png earaiza@wk2.waykee.com:/var/www/powerera-website/assets/images/products/
```

### Método 2: Sincronizar carpeta completa

```bash
# Sincronizar todo el sitio (excluye archivos innecesarios)
rsync -avz --exclude 'venv' --exclude 'node_modules' --exclude '.git' --exclude 'Dalle.txt' --exclude '.godaddy_credentials' -e "ssh -i ~/.ssh/id_claude_automation" /Users/enrique/PowerEraWebSite/ earaiza@wk2.waykee.com:/var/www/powerera-website/
```

### Método 3: Deploy desde GitHub

```bash
# En el servidor
ssh -i ~/.ssh/id_claude_automation earaiza@wk2.waykee.com
cd /var/www/powerera-website
git pull origin main
```

## 📝 Workflow de Desarrollo

### 1. Hacer cambios locales

Edita archivos en `/Users/enrique/PowerEraWebSite/`

### 2. Subir a servidor

```bash
scp -i ~/.ssh/id_claude_automation archivo.html earaiza@wk2.waykee.com:/var/www/powerera-website/ruta/
```

### 3. Commit a GitHub

```bash
git add .
git commit -m "Descripción de cambios

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
git push origin main
```

## 🎨 Generación de Imágenes con DALL-E 3

**Script:** `generate_images.py`
**API Key:** Archivo `Dalle.txt` (crear en raíz del proyecto)

### Configuración

1. Crear archivo con API key:
```bash
echo "tu-api-key-aqui" > Dalle.txt
```

2. El archivo ya está en `.gitignore`

### Uso

```bash
# Generar imagen específica
python3 generate_images.py waykee-hero

# Generar todas las imágenes (requiere confirmación)
python3 generate_images.py

# Ver imágenes disponibles
python3 generate_images.py nombre-invalido
```

### Imágenes disponibles

- `main-hero` - Hero principal del homepage
- `ai-development-hero` - Producto AI Development
- `ai-bots-hero` - Producto AI Bots
- `actif-hero` - Producto Actif (activos fijos reales)
- `waykee-hero` - Producto Waykee (chat/email/tasks)
- `helppo-hero` - Producto Helppo (CFDI)
- `team` - Equipo / About

**Costo:** ~$0.12 USD por imagen (calidad HD, 1792x1024)

### Después de generar imágenes

```bash
# Subir al servidor
scp -i ~/.ssh/id_claude_automation assets/images/products/*.png earaiza@wk2.waykee.com:/var/www/powerera-website/assets/images/products/

# Commit a GitHub
git add assets/images/
git commit -m "Update product images"
git push origin main
```

## 📁 Estructura del Proyecto

```
PowerEraWebSite/
├── index.html              # Homepage
├── sitemap.xml            # Sitemap para SEO
├── robots.txt             # Robots.txt para crawlers
├── README.md              # Documentación del proyecto
├── DEPLOYMENT.md          # Esta guía de deployment
├── generate_images.py     # Script DALL-E 3
├── Dalle.txt             # API key (no en git)
├── assets/
│   ├── css/
│   │   └── main.css      # Estilos principales
│   ├── js/
│   │   └── main.js       # JavaScript
│   └── images/
│       ├── favicon.svg   # Favicon SVG
│       ├── hero/         # Imágenes hero
│       └── products/     # Imágenes de productos
└── products/
    ├── ai-development/
    │   └── index.html
    ├── ai-bots/
    │   └── index.html
    ├── actif/
    │   └── index.html
    ├── waykee/
    │   └── index.html
    └── helppo/
        └── index.html
```

## 🎯 Productos

### 1. AI Development
**URL:** /products/ai-development/
**Descripción:** Desarrollo de software empresarial con IA
**Stack:** .NET Core, Python, React, Node.js, iOS/Android

### 2. AI Bots
**URL:** /products/ai-bots/
**Descripción:** Chatbots inteligentes con IA
**Características:** WhatsApp Business API, conversaciones naturales 24/7

### 3. Actif
**URL:** /products/actif/
**Descripción:** Sistema de control de activos fijos
**Características:**
- Cumplimiento SAT (Art 31 LISR)
- Multi-empresa
- Depreciación contable/fiscal/USGAAP
- RFID/QR/Código de Barras
- App Android/iOS
- Cartas responsivas
- Inventario físico
- Póliza contable
- Centros de costos

### 4. Waykee
**URL:** /products/waykee/
**Descripción:** Correo + WhatsApp + Gestión de Tareas + Agentes IA
**Características:** Plataforma de colaboración unificada

### 5. Helppo
**URL:** /products/helppo/
**Descripción:** Automatización con CFDI
**Módulos:**
- Conciliación Bancaria automática
- Portal de Proveedores
- Control de Pagos (REP)
- ExpenseHub (control de gastos)

## 🔍 SEO

### Optimizaciones implementadas

- ✅ Meta descriptions optimizadas con keywords México
- ✅ Canonical URLs en todas las páginas
- ✅ JSON-LD structured data (Organization, WebSite)
- ✅ Open Graph y Twitter Cards
- ✅ Robots meta tags
- ✅ Sitemap.xml
- ✅ Robots.txt
- ✅ Geo-targeting México (es_MX)
- ✅ Favicon SVG

### Keywords principales

- Desarrollo software IA México
- Chatbots WhatsApp México
- Sistema activos fijos SAT
- Facturación electrónica CFDI
- Colaboración empresarial México

### Google Search Console

Para agregar el sitio a Google Search Console:

1. Ir a https://search.google.com/search-console
2. Agregar propiedad: www.powerera.com
3. Verificar con tag HTML o archivo
4. Subir sitemap: https://www.powerera.com/sitemap.xml

## 🎨 Diseño

**Tema:** Dark mode, inspirado en Apple
**Colores principales:**
- Primary: `#00D9FF` (cyan)
- Dark: `#0A0E27` (navy oscuro)
- Gray: `#6B7280`

**Tipografía:** System fonts (-apple-system, BlinkMacSystemFont, Segoe UI)

## 📞 Contacto

**Email:** contacto@powerera.com
**Teléfono:** +52 (55) 4630-8046
**GitHub:** https://github.com/earaizapowerera/PowerEraWebsite

## 🔧 Troubleshooting

### El sitio no carga

1. Verificar que el servicio esté corriendo:
```bash
ssh -i ~/.ssh/id_claude_automation earaiza@wk2.waykee.com "sudo systemctl status powerera-web"
```

2. Si está detenido, iniciarlo:
```bash
ssh -i ~/.ssh/id_claude_automation earaiza@wk2.waykee.com "sudo systemctl start powerera-web"
```

3. Verificar Nginx:
```bash
ssh -i ~/.ssh/id_claude_automation earaiza@wk2.waykee.com "sudo nginx -t && sudo systemctl status nginx"
```

### Certificado SSL expirado

```bash
ssh -i ~/.ssh/id_claude_automation earaiza@wk2.waykee.com "sudo certbot renew"
```

### Puerto 5070 en uso

```bash
# Verificar qué está usando el puerto
ssh -i ~/.ssh/id_claude_automation earaiza@wk2.waykee.com "sudo lsof -i :5070"

# Cambiar puerto en systemd service
ssh -i ~/.ssh/id_claude_automation earaiza@wk2.waykee.com "sudo nano /etc/systemd/system/powerera-web.service"
# Editar ExecStart para usar otro puerto
# Recargar y reiniciar
ssh -i ~/.ssh/id_claude_automation earaiza@wk2.waykee.com "sudo systemctl daemon-reload && sudo systemctl restart powerera-web"
```

### Cambios no se reflejan

1. Limpiar cache del navegador (Ctrl+Shift+R o Cmd+Shift+R)
2. Verificar que archivos se subieron correctamente:
```bash
ssh -i ~/.ssh/id_claude_automation earaiza@wk2.waykee.com "ls -la /var/www/powerera-website/"
```

## 📊 Puertos Documentados en Uso

Ver `/Users/enrique/readme.md` para lista completa de puertos en el servidor.

**Puerto PowerEra:** 5070

## 🔐 Archivos Sensibles (NO subir a GitHub)

- `Dalle.txt` - API key de OpenAI
- `.godaddy_credentials` - API credentials de GoDaddy
- `venv/` - Entorno virtual Python
- `node_modules/` - Dependencias Node (si las hay)
- `.env*` - Variables de entorno

Todos estos están en `.gitignore`

## 📝 Notas de Desarrollo

### Historial de Cambios Importantes

**2025-10-07:**
- ✅ Sitio inicial creado con 5 productos
- ✅ Deploy a wwwtest.powerera.com
- ✅ Deploy a www.powerera.com
- ✅ Optimización SEO completa
- ✅ Favicon SVG creado
- ✅ Sitemap y robots.txt
- ✅ Imágenes DALL-E 3 generadas
- ✅ Compliance checklist Actif (SAT)
- ✅ Portal de Proveedores en Helppo
- ✅ Fix colores en AI Development

### Stack de Generación de Imágenes

- **DALL-E 3** vía OpenAI API
- Resolución: 1792x1024 (landscape)
- Calidad: HD
- Estilo: Fotográfico realista, profesional, dark theme

### Comandos Rápidos

```bash
# Deploy completo
rsync -avz --exclude 'venv' --exclude 'node_modules' --exclude '.git' --exclude 'Dalle.txt' -e "ssh -i ~/.ssh/id_claude_automation" /Users/enrique/PowerEraWebSite/ earaiza@wk2.waykee.com:/var/www/powerera-website/ && git add . && git commit -m "Deploy" && git push

# Solo subir HTML
for file in products/*/index.html; do scp -i ~/.ssh/id_claude_automation /Users/enrique/PowerEraWebSite/$file earaiza@wk2.waykee.com:/var/www/powerera-website/$file; done

# Verificar sitio
curl -I https://www.powerera.com
```

## 🤖 Información para IA/Robots

### Contexto del Proyecto

Este es un sitio web corporativo estático para PowerEra, empresa mexicana de desarrollo de software con IA. El sitio presenta 5 productos principales y está optimizado para SEO en México.

### Arquitectura de Deployment

- **Hosting:** Python HTTP server (http.server) en puerto 5070
- **Reverse Proxy:** Nginx en puerto 443 (HTTPS)
- **SSL:** Let's Encrypt automático con certbot
- **Servidor:** Azure VM (wk2.waykee.com)
- **DNS:** GoDaddy con automatización via API

### Para actualizar contenido

1. Leer archivos HTML en `/Users/enrique/PowerEraWebSite/`
2. Hacer cambios necesarios usando Edit tool
3. Subir a servidor usando `scp` con SSH key `~/.ssh/id_claude_automation`
4. Commit a GitHub con mensaje estándar
5. NO es necesario reiniciar servicio (archivos estáticos se sirven directamente)

### Generación de imágenes

Si necesitas generar nuevas imágenes:
1. Verificar que existe `Dalle.txt` con API key
2. Ejecutar `python3 generate_images.py nombre-imagen`
3. Subir imagen generada a servidor
4. Commit a GitHub

### Configuración de nuevo dominio

```bash
# 1. Crear CNAME en GoDaddy
bash /Users/enrique/create_cname.sh SUBDOMINIO wk2.waykee.com

# 2. Crear config Nginx
ssh -i ~/.ssh/id_claude_automation earaiza@wk2.waykee.com "sudo tee /etc/nginx/sites-available/SUBDOMINIO.powerera.com.conf" <<'EOF'
server {
    listen 80;
    server_name SUBDOMINIO.powerera.com;
    location / {
        proxy_pass http://localhost:5070;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
EOF

# 3. Habilitar sitio
ssh -i ~/.ssh/id_claude_automation earaiza@wk2.waykee.com "sudo ln -s /etc/nginx/sites-available/SUBDOMINIO.powerera.com.conf /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx"

# 4. Generar SSL
ssh -i ~/.ssh/id_claude_automation earaiza@wk2.waykee.com "sudo certbot --nginx -d SUBDOMINIO.powerera.com --non-interactive --agree-tos --email enrique@powerera.com --redirect"
```

### Variables importantes

- `SERVER`: wk2.waykee.com
- `USER`: earaiza
- `SSH_KEY`: ~/.ssh/id_claude_automation
- `WEBROOT`: /var/www/powerera-website
- `PORT`: 5070
- `SERVICE`: powerera-web
- `REPO`: https://github.com/earaizapowerera/PowerEraWebsite

---

**Última actualización:** 2025-10-07
**Mantenido por:** Claude Code + PowerEra Team
