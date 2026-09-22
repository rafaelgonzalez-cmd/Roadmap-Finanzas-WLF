# -*- coding: utf-8 -*-
"""
Roadmap Mensual – Departamento de Finanzas
Presentación ejecutiva para el CEO
"""

import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# ──────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Roadmap Finanzas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────
# ESTILOS
# ──────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif !important; }

    .hero-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e40af 60%, #2563eb 100%);
        color: white;
        padding: 2.8rem 2.2rem;
        border-radius: 1rem;
        margin-bottom: 1.8rem;
        text-align: center;
    }
    .hero-box h1 { font-size: 2.4rem; font-weight: 800; margin: 0; letter-spacing: -0.5px; color: white; }
    .hero-box p  { font-size: 1.1rem; opacity: .85; margin-top: .5rem; color: white; }

    .kpi-card {
        background: #f8fafc;
        border-radius: 0.85rem;
        padding: 1.1rem 0.8rem;
        text-align: center;
        box-shadow: 0 1px 6px rgba(0,0,0,.07);
        border: 1px solid #e2e8f0;
    }
    .kpi-card .kpi-num { font-size: 2.4rem; font-weight: 800; color: #2563eb; line-height: 1.1; }
    .kpi-card .kpi-lab { font-size: 0.82rem; color: #64748b; margin-top: 0.25rem; }

    .card {
        background: #ffffff;
        border-radius: 0.85rem;
        padding: 1.4rem 1.6rem;
        margin-bottom: 1.2rem;
        border-left: 5px solid #2563eb;
        box-shadow: 0 2px 10px rgba(0,0,0,.05);
    }
    .card h3 { margin: 0 0 0.4rem 0; color: #0f172a; font-weight: 700; font-size: 1.05rem; }
    .card .badge {
        display: inline-block;
        background: #2563eb;
        color: white;
        padding: 2px 14px;
        border-radius: 99px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .card ul { margin: 0; padding-left: 1.2rem; color: #334155; font-size: 0.9rem; line-height: 1.65; }

    .card.blue   { border-left-color: #2563eb; }
    .card.blue .badge { background: #2563eb; }
    .card.indigo { border-left-color: #6366f1; }
    .card.indigo .badge { background: #6366f1; }
    .card.purple { border-left-color: #7c3aed; }
    .card.purple .badge { background: #7c3aed; }
    .card.green  { border-left-color: #059669; }
    .card.green .badge { background: #059669; }
    .card.amber  { border-left-color: #d97706; }
    .card.amber .badge { background: #d97706; }
    .card.rose   { border-left-color: #e11d48; }
    .card.rose .badge { background: #e11d48; }
    .card.cyan   { border-left-color: #0891b2; }
    .card.cyan .badge { background: #0891b2; }

    .deliverable-box {
        background: linear-gradient(90deg, #059669 0%, #10b981 100%);
        color: white;
        padding: 1rem 1.4rem;
        border-radius: 0.85rem;
        margin: 0.8rem 0 1.2rem 0;
        font-weight: 600;
        font-size: 0.95rem;
        text-align: center;
        box-shadow: 0 2px 10px rgba(5,150,105,.2);
    }

    .req-box {
        background: #fffbeb;
        border-left: 5px solid #f59e0b;
        border-radius: 0.85rem;
        padding: 1.2rem 1.4rem;
        margin-bottom: 0.9rem;
        box-shadow: 0 1px 6px rgba(0,0,0,.04);
    }
    .req-box h4 { margin: 0 0 0.25rem 0; color: #92400e; font-size: 0.95rem; }
    .req-box p  { margin: 0; color: #78350f; font-size: 0.88rem; line-height: 1.55; }

    .rec-box {
        background: #eff6ff;
        border-left: 5px solid #3b82f6;
        border-radius: 0.85rem;
        padding: 1.2rem 1.4rem;
        margin-bottom: 0.9rem;
        box-shadow: 0 1px 6px rgba(0,0,0,.04);
    }
    .rec-box h4 { margin: 0 0 0.25rem 0; color: #1e3a5f; font-size: 0.95rem; }
    .rec-box p  { margin: 0; color: #1e40af; font-size: 0.88rem; line-height: 1.55; }

    .entregable-card {
        background: #ffffff;
        border-radius: 0.85rem;
        padding: 1.6rem 1.8rem;
        border-left: 5px solid #7c3aed;
        box-shadow: 0 2px 12px rgba(0,0,0,.06);
        min-height: 260px;
    }
    .entregable-card.e2 { border-left-color: #0891b2; }
    .entregable-card h3 { margin: 0 0 0.6rem 0; color: #0f172a; font-weight: 700; font-size: 1.05rem; }
    .entregable-card .badge-e1 {
        display: inline-block; background: #7c3aed; color: white;
        padding: 2px 14px; border-radius: 99px; font-size: 0.75rem;
        font-weight: 600; margin-bottom: 0.5rem;
    }
    .entregable-card .badge-e2 {
        display: inline-block; background: #0891b2; color: white;
        padding: 2px 14px; border-radius: 99px; font-size: 0.75rem;
        font-weight: 600; margin-bottom: 0.5rem;
    }
    .entregable-card ul { margin: 0; padding-left: 1.2rem; color: #334155; font-size: 0.9rem; line-height: 1.65; }
    .entregable-card .status { margin-top: 0.8rem; font-weight: 600; font-size: 0.88rem; }
    .entregable-card .status.s1 { color: #6b21a8; }
    .entregable-card .status.s2 { color: #155e75; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────
# SIDEBAR
# ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📊 Navegación")
    slide = st.radio(
        "Ir a sección:",
        [
            "🏠 Portada",
            "🗺️ Roadmap Visual",
            "📋 Plan de Trabajo",
            "📌 Entregables",
            "📝 Requerimientos",
            "💡 Recomendaciones",
        ],
    )
    st.divider()
    st.caption(f"Generado el {datetime.now().strftime('%d/%m/%Y')}")


# ══════════════════════════════════════════════
#  PORTADA
# ══════════════════════════════════════════════
if slide == "🏠 Portada":

    st.markdown(
        '<div class="hero-box">'
        "<h1>Reestructuración del Departamento de Finanzas</h1>"
        "<p>Roadmap Mensual &middot; Plan de Trabajo Operativo</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown(
            '<div class="kpi-card"><div class="kpi-num">23</div>'
            '<div class="kpi-lab">Días hábiles del ciclo</div></div>',
            unsafe_allow_html=True,
        )
    with k2:
        st.markdown(
            '<div class="kpi-card"><div class="kpi-num">7</div>'
            '<div class="kpi-lab">Fases operativas</div></div>',
            unsafe_allow_html=True,
        )
    with k3:
        st.markdown(
            '<div class="kpi-card"><div class="kpi-num">2</div>'
            '<div class="kpi-lab">Entregables clave</div></div>',
            unsafe_allow_html=True,
        )
    with k4:
        st.markdown(
            '<div class="kpi-card"><div class="kpi-num">5</div>'
            '<div class="kpi-lab">Requerimientos</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown("")
    st.info(
        "**Objetivo:** Definir un proceso mensual estandarizado, escalable y progresivamente "
        "automatizado para el cierre financiero, análisis gerencial y pronóstico.",
        icon="🎯",
    )

    st.markdown("")
    st.markdown("#### 🧭 Visión General del Ciclo")
    st.markdown(
        """
| Bloque | Días | Alcance |
|--------|------|---------|
| **Recepción y limpieza** | 1 – 3 | Datos crudos → datos limpios |
| **Conciliación y clasificación** | 4 – 6 | Datos limpios → datos conciliados |
| **Cifras finales EEFF** | 7 – 10 | Consolidación → **Entregable 1** |
| **Indicadores y análisis** | 11 – 18 | KPIs, variaciones, causas raíz |
| **Pronóstico** | 19 – 20 | Modelo cuantitativo + ajuste cualitativo |
| **Reporte gerencial** | 21 – 23 | Reporte integral → **Entregable 2** |
        """
    )


# ══════════════════════════════════════════════
#  ROADMAP VISUAL (Gantt)
# ══════════════════════════════════════════════
elif slide == "🗺️ Roadmap Visual":

    st.markdown("## 🗺️ Roadmap – Línea de Tiempo")
    st.caption("Gantt del ciclo mensual (23 días hábiles)")

    phases = [
        ("Recepción y Limpieza",         1,  3, "#2563eb"),
        ("Conciliación y Clasificación", 4,  6, "#6366f1"),
        ("Cifras finales para EEFF",     7, 10, "#7c3aed"),
        ("Indicadores y Análisis",      11, 14, "#059669"),
        ("Análisis de Variaciones",     15, 18, "#d97706"),
        ("Pronóstico mes siguiente",    19, 20, "#e11d48"),
        ("Reporte Gerencial",           21, 23, "#0891b2"),
    ]

    fig = go.Figure()
    for name, start, end, color in phases:
        fig.add_trace(
            go.Bar(
                y=[name],
                x=[end - start + 1],
                base=[start - 1],
                orientation="h",
                marker=dict(color=color, cornerradius=6),
                text=f"Días {start}–{end}",
                textposition="inside",
                textfont=dict(color="white", size=13, family="Inter"),
                hovertemplate=f"<b>{name}</b><br>Días {start}–{end}<extra></extra>",
                showlegend=False,
            )
        )

    fig.add_vline(
        x=10, line_dash="dot", line_color="#059669", line_width=2,
        annotation_text="📦 Entregable 1", annotation_position="top",
        annotation_font=dict(size=11, color="#059669", family="Inter"),
    )
    fig.add_vline(
        x=23, line_dash="dot", line_color="#0891b2", line_width=2,
        annotation_text="📦 Entregable 2", annotation_position="top",
        annotation_font=dict(size=11, color="#0891b2", family="Inter"),
    )

    fig.update_layout(
        xaxis=dict(title="Día hábil del mes", dtick=1, range=[0, 24], gridcolor="#e2e8f0"),
        yaxis=dict(autorange="reversed"),
        height=420,
        margin=dict(l=20, r=20, t=50, b=40),
        plot_bgcolor="white",
        font=dict(family="Inter"),
    )
    st.plotly_chart(fig, use_container_width=True, key="gantt_chart")

    st.divider()

    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            '<div class="deliverable-box">🎯 ENTREGABLE 1 (Día 10): Vista previa de EEFF — datos listos, sin análisis</div>',
            unsafe_allow_html=True,
        )
    with e2:
        st.markdown(
            '<div class="deliverable-box">🎯 ENTREGABLE 2 (Día 23): Reporte Gerencial completo — cifras, KPIs y proyección</div>',
            unsafe_allow_html=True,
        )


# ══════════════════════════════════════════════
#  PLAN DE TRABAJO
# ══════════════════════════════════════════════
elif slide == "📋 Plan de Trabajo":

    st.markdown("## 📋 Plan de Trabajo Detallado")
    st.markdown("")

    col_l, col_r = st.columns(2)

    with col_l:
        # Fase 1
        st.markdown(
            '<div class="card blue">'
            '<span class="badge">Días 1 – 3</span>'
            "<h3>1. Recepción de datos y limpieza</h3>"
            "<ul>"
            "<li>Recepción de información en Excel / PDF adjuntos</li>"
            "<li><b>Fase 1:</b> Limpieza manual en Excel, Google Sheets y Power Query</li>"
            "<li><b>Fase 2:</b> Automatización progresiva del proceso de limpieza</li>"
            "</ul></div>",
            unsafe_allow_html=True,
        )

        # Fase 2
        st.markdown(
            '<div class="card indigo">'
            '<span class="badge">Días 4 – 6</span>'
            "<h3>2. Conciliación y clasificación</h3>"
            "<ul>"
            "<li><b>Fase 1:</b> Ejecutable en Excel, Google Sheets, Claude y GPT (versiones gratuitas)</li>"
            "<li><b>Fase 2:</b> IA de paga para mayor volumen de datos</li>"
            "<li>Claude → más potente &nbsp;|&nbsp; GPT → más económico</li>"
            "</ul></div>",
            unsafe_allow_html=True,
        )

        # Fase 3
        st.markdown(
            '<div class="card purple">'
            '<span class="badge">Días 7 – 10</span>'
            "<h3>3. Cifras finales para EEFF</h3>"
            "<ul>"
            "<li><b>Fase 1:</b> Visualización en Excel / Google Sheets</li>"
            "<li><b>Fase 2:</b> Automatización del envío de resultados preliminares por correo</li>"
            "</ul></div>",
            unsafe_allow_html=True,
        )

    with col_r:
        # Fase 4
        st.markdown(
            '<div class="card green">'
            '<span class="badge">Días 11 – 14</span>'
            "<h3>4. Indicadores y vaciado en plantilla</h3>"
            "<ul>"
            "<li><b>Fase 1:</b> Cálculos en Excel / Google Sheets</li>"
            "<li>Indicadores pendientes de definición conjunta con dirección</li>"
            "</ul></div>",
            unsafe_allow_html=True,
        )

        # Fase 5
        st.markdown(
            '<div class="card amber">'
            '<span class="badge">Días 15 – 18</span>'
            "<h3>5. Análisis de variaciones</h3>"
            "<ul>"
            "<li>Comparativa: Proyección vs. Real</li>"
            "<li>Análisis de causas raíz de las variaciones detectadas</li>"
            "</ul></div>",
            unsafe_allow_html=True,
        )

        # Fase 6
        st.markdown(
            '<div class="card rose">'
            '<span class="badge">Días 19 – 20</span>'
            "<h3>6. Pronóstico del mes siguiente</h3>"
            "<ul>"
            "<li>Modelos en R / Python para el pronóstico cuantitativo</li>"
            "<li>Ajuste cualitativo (factores no cuantificables) y consolidación</li>"
            "</ul></div>",
            unsafe_allow_html=True,
        )

    # Fase 7 — ancho completo
    st.markdown(
        '<div class="card cyan">'
        '<span class="badge">Días 21 – 23</span>'
        "<h3>7. Reporte Gerencial</h3>"
        "<ul>"
        "<li>Cifras finales por proyecto</li>"
        "<li>KPIs de proyectos</li>"
        "<li>Proyección consolidada del mes siguiente</li>"
        "<li><b>Herramienta de visualización por definir:</b> Looker Studio, Power BI, Streamlit o HTML + Looker Studio</li>"
        "</ul></div>",
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════
#  ENTREGABLES
# ══════════════════════════════════════════════
elif slide == "📌 Entregables":

    st.markdown("## 📌 Entregables del Ciclo Mensual")
    st.markdown("")

    e1, e2 = st.columns(2)

    with e1:
        st.markdown(
            '<div class="entregable-card">'
            '<span class="badge-e1">Día 10</span>'
            "<h3>🔖 Entregable 1 — Vista Previa de EEFF</h3>"
            "<ul>"
            "<li>Datos recibidos, limpiados y conciliados</li>"
            "<li>Cifras consolidadas listas para los Estados Financieros</li>"
            "<li>Datos <b>listos pero no analizados</b></li>"
            "<li>Permite revisión temprana antes del cierre</li>"
            "</ul>"
            '<p class="status s1">✅ Checkpoint de control intermedio</p>'
            "</div>",
            unsafe_allow_html=True,
        )

    with e2:
        st.markdown(
            '<div class="entregable-card e2">'
            '<span class="badge-e2">Día 23</span>'
            "<h3>🔖 Entregable 2 — Reporte Gerencial</h3>"
            "<ul>"
            "<li>Cifras finales desglosadas por proyecto</li>"
            "<li>KPIs operativos y financieros de cada proyecto</li>"
            "<li>Proyección cuantitativa del mes siguiente</li>"
            "<li>Análisis de variaciones y causas raíz</li>"
            "</ul>"
            '<p class="status s2">✅ Entregable final para la toma de decisiones</p>'
            "</div>",
            unsafe_allow_html=True,
        )

    st.divider()
    st.markdown("### 📐 Flujo del ciclo mensual")

    flow = go.Figure()
    labels = [
        "Recepción<br>Días 1-3",
        "Conciliación<br>Días 4-6",
        "Cifras EEFF<br>Días 7-10",
        "ENTREGABLE 1<br>Día 10",
        "Indicadores<br>Días 11-14",
        "Variaciones<br>Días 15-18",
        "Pronóstico<br>Días 19-20",
        "Reporte<br>Días 21-23",
        "ENTREGABLE 2<br>Día 23",
    ]
    node_colors = [
        "#2563eb", "#6366f1", "#7c3aed", "#059669",
        "#059669", "#d97706", "#e11d48", "#0891b2", "#0891b2",
    ]
    flow.add_trace(go.Sankey(
        node=dict(
            pad=25, thickness=28,
            label=labels,
            color=node_colors,
            line=dict(color="#94a3b8", width=0.5),
        ),
        link=dict(
            source=[0, 1, 2, 3, 4, 5, 6, 7],
            target=[1, 2, 3, 4, 5, 6, 7, 8],
            value=[5, 5, 5, 5, 5, 5, 5, 5],
            color=[
                "rgba(37,99,235,0.15)", "rgba(99,102,241,0.15)",
                "rgba(124,58,237,0.15)", "rgba(5,150,105,0.15)",
                "rgba(5,150,105,0.15)", "rgba(217,119,6,0.15)",
                "rgba(225,29,72,0.15)", "rgba(8,145,178,0.15)",
            ],
        ),
    ))
    flow.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=10, b=10),
        font=dict(size=11, family="Inter"),
    )
    st.plotly_chart(flow, use_container_width=True, key="sankey_flow")


# ══════════════════════════════════════════════
#  REQUERIMIENTOS
# ══════════════════════════════════════════════
elif slide == "📝 Requerimientos":

    st.markdown("## 📝 Requerimientos y Solicitudes")
    st.caption("Recursos necesarios para la ejecución exitosa del roadmap")
    st.markdown("")

    reqs = [
        (
            "🤖 1. Licencia de IA",
            "Evaluar adquisición de Claude Pro o ChatGPT Plus/Team. Claude ofrece mayor potencia analítica "
            "y ventana de contexto más amplia; GPT es más económico y tiene un ecosistema más amplio de plugins e integraciones.",
        ),
        (
            "💰 2. Incremento salarial",
            "Negociación pendiente acorde a las nuevas responsabilidades, carga de trabajo y perfil técnico requerido "
            "para operar herramientas de IA, programación (R/Python) y análisis avanzado.",
        ),
        (
            "🏠 3. Home Office (1 día/semana)",
            "Un día semanal de trabajo remoto destinado a tareas de alta concentración: análisis de datos, "
            "desarrollo de pronósticos, elaboración de reportes gerenciales.",
        ),
        (
            "⏰ 4. Respeto a tiempos acordados",
            "Cumplimiento estricto de los plazos definidos en el roadmap, tanto por parte del equipo de finanzas "
            "como de las áreas operativas que proveen la información base.",
        ),
        (
            "🎓 5. Cursos y certificaciones",
            "Plan de capacitación para los 4 integrantes del equipo en: herramientas de BI, analítica avanzada, "
            "IA aplicada a finanzas, y programación en R/Python.",
        ),
    ]

    for title, desc in reqs:
        st.markdown(
            f'<div class="req-box"><h4>{title}</h4><p>{desc}</p></div>',
            unsafe_allow_html=True,
        )

    st.divider()
    st.markdown("### 📊 Resumen de inversión")
    st.markdown(
        """
| Recurso | Tipo | Frecuencia | Notas |
|---------|------|-----------|-------|
| Licencia IA | Monetario | Mensual | ~\\$20 USD/mes por usuario |
| Incremento salarial | Monetario | Mensual | A negociar |
| Home Office | Operativo | Semanal | 1 día/semana |
| Respeto de tiempos | Cultural | Continuo | SLA internos |
| Capacitación | Monetario + Tiempo | Trimestral | 4 integrantes |
        """
    )


# ══════════════════════════════════════════════
#  RECOMENDACIONES
# ══════════════════════════════════════════════
elif slide == "💡 Recomendaciones":

    st.markdown("## 💡 Recomendaciones Adicionales")
    st.caption("Sugerencias para fortalecer la propuesta ante el CEO")
    st.markdown("")

    recs = [
        (
            "📑 Definir indicadores (KPIs) antes de arrancar",
            "El roadmap menciona 'indicadores pendientes de definir'. Recomiendo que antes de la presentación "
            "se acuerde un set mínimo de KPIs (margen bruto, EBITDA, ratio de liquidez, días de cobro/pago, "
            "burn rate por proyecto) para que el CEO vea claridad en lo que se va a medir.",
        ),
        (
            "🔄 Agregar un ciclo de retroalimentación (feedback loop)",
            "Después del Entregable 2, programar una sesión de retroalimentación con el CEO / Dirección. "
            "Esto cierra el ciclo y permite ajustar el proceso mes a mes. Sin esto, se pierde la mejora continua.",
        ),
        (
            "🛡️ Incluir un plan de contingencia / días buffer",
            "El roadmap es compacto (23 días exactos). Considerar 1-2 días de holgura o un protocolo "
            "claro de escalación cuando las áreas no entreguen información a tiempo (días 1-3).",
        ),
        (
            "📊 Elegir herramienta de visualización ahora",
            "La indefinición de la herramienta de reporte (Looker, Power BI, Streamlit…) puede generar retrasos. "
            "Recomiendo Looker Studio como MVP (gratuito, integrado con Google) y migrar a Power BI o Streamlit "
            "si se necesitan dashboards más avanzados o interactivos.",
        ),
        (
            "🤖 Claude Pro > ChatGPT Plus para finanzas",
            "Para tareas de conciliación y clasificación con contexto largo (estados financieros, pólizas), "
            "Claude tiene ventana de contexto más grande y mejor seguimiento de instrucciones complejas. "
            "GPT es mejor para integraciones (Zapier, Make, plugins). Considerar un equipo mixto.",
        ),
        (
            "📈 Versionamiento y trazabilidad",
            "Implementar control de versiones en los archivos financieros (Google Sheets con historial, o "
            "un repositorio Git para scripts de R/Python). Esto es clave para auditoría y para que el CEO "
            "tenga confianza en la integridad de los datos.",
        ),
        (
            "🎯 SLA internos con áreas proveedoras",
            "Formalizar con las áreas operativas una fecha límite de entrega de información (idealmente día 1). "
            "Sin un SLA, los retrasos en la recepción de datos comprometen todo el ciclo.",
        ),
        (
            "🧪 Piloto de 2 meses antes de formalizar",
            "Sugerir al CEO un periodo de prueba de 2 meses donde se ejecute el roadmap tal cual, "
            "se midan los tiempos reales de cada fase y se ajuste antes de hacerlo permanente.",
        ),
    ]

    for title, desc in recs:
        st.markdown(
            f'<div class="rec-box"><h4>{title}</h4><p>{desc}</p></div>',
            unsafe_allow_html=True,
        )

    st.divider()
    st.success(
        "**En resumen:** El roadmap es sólido y bien estructurado. Las recomendaciones buscan "
        "cerrar los puntos abiertos, agregar resiliencia al proceso y dar mayor confianza al CEO "
        "en la madurez de la propuesta.",
        icon="✅",
    )
