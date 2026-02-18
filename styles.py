"""事典風カスタムCSSとスタイル定義"""

CATEGORY_COLORS = {
    "igneous": {
        "primary": "#8B1A1A",
        "accent": "#C0392B",
        "light": "#FDF0EE",
        "border": "#C0392B",
        "tab_bg": "#F5E6E6",
        "emoji": "🌋",
        "label": "火成岩",
    },
    "sedimentary": {
        "primary": "#6B4226",
        "accent": "#A0522D",
        "light": "#FDF6EE",
        "border": "#A0522D",
        "tab_bg": "#F5EEE6",
        "emoji": "🪨",
        "label": "堆積岩",
    },
    "metamorphic": {
        "primary": "#1A3A5C",
        "accent": "#2471A3",
        "light": "#EEF4FD",
        "border": "#2471A3",
        "tab_bg": "#E6EEF5",
        "emoji": "💎",
        "label": "変成岩",
    },
}


def get_css() -> str:
    return """
<style>
    /* ── 基本フォント・背景 ────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@400;600;700&family=Noto+Sans+JP:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', sans-serif;
    }

    .main {
        background-color: #FDFAF5;
    }

    .main .block-container {
        padding-top: 1.2rem;
        max-width: 1280px;
        background: #FDFAF5;
    }

    /* ── ヘッダー ───────────────────────────────────────────── */
    .encyclopedia-header {
        background: linear-gradient(135deg, #2C1810 0%, #5C2D0A 50%, #2C1810 100%);
        border-radius: 4px;
        padding: 2rem 2.5rem;
        margin-bottom: 1.5rem;
        text-align: center;
        border-top: 4px solid #C9A84C;
        border-bottom: 4px solid #C9A84C;
        box-shadow: 0 4px 20px rgba(0,0,0,0.25);
        position: relative;
    }
    .encyclopedia-header::before,
    .encyclopedia-header::after {
        content: '◆';
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        color: #C9A84C;
        font-size: 1.5rem;
    }
    .encyclopedia-header::before { left: 1.5rem; }
    .encyclopedia-header::after  { right: 1.5rem; }

    .encyclopedia-header h1 {
        font-family: 'Noto Serif JP', serif;
        color: #F5E6C0;
        font-size: 2.6rem;
        font-weight: 700;
        margin: 0 0 0.4rem;
        letter-spacing: 0.12em;
        text-shadow: 1px 2px 8px rgba(0,0,0,0.5);
    }
    .encyclopedia-header .subtitle {
        color: #C9A84C;
        font-size: 0.95rem;
        letter-spacing: 0.15em;
        margin: 0;
    }
    .encyclopedia-header .edition {
        display: inline-block;
        margin-top: 0.6rem;
        font-size: 0.78rem;
        color: #A08060;
        border-top: 1px solid #5C3D1A;
        border-bottom: 1px solid #5C3D1A;
        padding: 0.2rem 1.2rem;
        letter-spacing: 0.2em;
    }

    /* ── 岩石エントリー（事典スタイル） ─────────────────────── */
    .rock-entry {
        background: #FFFEF9;
        border: 1px solid #DDD5C0;
        border-radius: 2px;
        margin-bottom: 1.2rem;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        transition: box-shadow 0.2s, transform 0.2s;
    }
    .rock-entry:hover {
        box-shadow: 0 6px 20px rgba(0,0,0,0.14);
        transform: translateY(-2px);
    }

    /* エントリーヘッダー */
    .rock-entry-header {
        padding: 0.7rem 1rem 0.5rem;
        border-bottom: 2px solid currentColor;
    }
    .rock-entry-header-igneous    { background: #F9EEEE; border-bottom-color: #C0392B; }
    .rock-entry-header-sedimentary{ background: #F9F3EE; border-bottom-color: #A0522D; }
    .rock-entry-header-metamorphic{ background: #EEF1F9; border-bottom-color: #2471A3; }

    .rock-title-row {
        display: flex;
        align-items: baseline;
        gap: 0.5rem;
        flex-wrap: wrap;
    }
    .rock-name-ja {
        font-family: 'Noto Serif JP', serif;
        font-size: 1.3rem;
        font-weight: 700;
        color: #1A0A00;
        letter-spacing: 0.04em;
    }
    .rock-name-en {
        font-size: 0.95rem;
        font-weight: 600;
        color: #555;
    }
    .rock-name-kana {
        font-size: 0.78rem;
        color: #888;
        background: #F0EDE8;
        border-radius: 2px;
        padding: 0.08rem 0.45rem;
        letter-spacing: 0.05em;
    }

    /* エントリー本文 */
    .rock-entry-body {
        padding: 0.8rem 1rem 0.9rem;
    }

    /* 短い説明（定義文） */
    .rock-short-desc {
        font-size: 0.88rem;
        color: #333;
        line-height: 1.6;
        margin-bottom: 0.6rem;
        padding-left: 0.6rem;
        border-left: 3px solid #C9A84C;
    }

    /* 詳細説明 */
    .rock-detail-desc {
        font-size: 0.84rem;
        color: #444;
        line-height: 1.75;
        margin-top: 0.5rem;
    }

    /* スペック表 */
    .rock-specs {
        display: flex;
        flex-wrap: wrap;
        gap: 0.35rem;
        margin-top: 0.7rem;
    }
    .rock-spec-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.25rem;
        background: #F5F0E8;
        border: 1px solid #DDD5C0;
        border-radius: 2px;
        padding: 0.18rem 0.55rem;
        font-size: 0.76rem;
        color: #4A3828;
    }
    .rock-spec-badge strong {
        color: #2C1810;
        font-weight: 600;
    }

    /* 画像 */
    .rock-image-wrap {
        background: #EEE9DF;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        min-height: 160px;
        border-bottom: 1px solid #DDD5C0;
    }
    .rock-image-wrap img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        display: block;
    }
    .rock-image-caption {
        font-size: 0.72rem;
        color: #888;
        text-align: center;
        padding: 0.25rem 0.5rem;
        background: #F5F0E8;
        border-top: 1px solid #DDD5C0;
    }

    /* ── カテゴリ見出し ──────────────────────────────────────── */
    .category-heading {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        font-family: 'Noto Serif JP', serif;
        font-size: 1.4rem;
        font-weight: 700;
        padding: 0.5rem 0 0.5rem 0.8rem;
        margin-bottom: 1.2rem;
        border-left: 6px solid currentColor;
        letter-spacing: 0.04em;
    }
    .category-heading-sub {
        font-size: 0.82rem;
        font-weight: 400;
        font-family: 'Noto Sans JP', sans-serif;
        opacity: 0.75;
    }

    /* ── サイドバー ──────────────────────────────────────────── */
    [data-testid="stSidebar"] {
        background: #F5F0E8;
        border-right: 1px solid #DDD5C0;
    }
    [data-testid="stSidebar"] .stMarkdown h2,
    [data-testid="stSidebar"] .stMarkdown h3 {
        font-family: 'Noto Serif JP', serif;
        color: #2C1810;
    }

    /* ── フッター ────────────────────────────────────────────── */
    .encyclopedia-footer {
        text-align: center;
        margin-top: 2.5rem;
        padding: 1rem 0 0.5rem;
        border-top: 2px solid #C9A84C;
        color: #A08060;
        font-size: 0.78rem;
        letter-spacing: 0.1em;
    }
    .encyclopedia-footer .ornament {
        color: #C9A84C;
        font-size: 1rem;
    }

    /* ── レスポンシブ ────────────────────────────────────────── */
    @media (max-width: 640px) {
        .encyclopedia-header h1 { font-size: 1.7rem; }
        .rock-name-ja { font-size: 1.1rem; }
    }
</style>
"""


def rock_entry_html(rock: dict, category: str) -> str:
    """岩石1件分の事典エントリーHTMLを返す（画像込み）。"""
    info = CATEGORY_COLORS[category]

    # 画像 + onerror フォールバック（壊れた場合は絵文字を表示）
    fallback_style = (
        f"background:{info['light']};height:180px;display:flex;"
        f"align-items:center;justify-content:center;font-size:3rem;"
        f"border-bottom:1px solid {info['border']};"
    )
    img_html = (
        f'<div class="rock-image-wrap">'
        f'<img src="{rock["image_url"]}" alt="{rock["name_en"]}"'
        f' style="width:100%;height:180px;object-fit:cover;display:block"'
        f' onerror="this.onerror=null;this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\';" />'
        f'<div style="{fallback_style}display:none">{info["emoji"]}</div>'
        f'<div class="rock-image-caption">{rock["name"]} / {rock["name_en"]}</div>'
        f'</div>'
    )

    specs = (
        f'<div class="rock-specs">'
        f'<span class="rock-spec-badge">&#x2B21; 硬度&nbsp;<strong>{rock["hardness"]}</strong></span>'
        f'<span class="rock-spec-badge">&#127912;&nbsp;<strong>{rock["color"]}</strong></span>'
        f'<span class="rock-spec-badge">&#128295;&nbsp;{rock["uses"]}</span>'
        f'</div>'
    )

    return (
        f'<div class="rock-entry">'
        f'<div class="rock-entry-header rock-entry-header-{category}">'
        f'<div class="rock-title-row">'
        f'<span class="rock-name-ja">{rock["name"]}</span>'
        f'<span class="rock-name-en">{rock["name_en"]}</span>'
        f'<span class="rock-name-kana">/{rock["name_kana"]}/</span>'
        f'</div>'
        f'</div>'
        f'{img_html}'
        f'<div class="rock-entry-body">'
        f'<p class="rock-short-desc">{rock["description"]}</p>'
        f'<p class="rock-detail-desc">{rock["description_detail"]}</p>'
        f'{specs}'
        f'</div>'
        f'</div>'
    )


def category_heading_html(category: str, count: int) -> str:
    info = CATEGORY_COLORS[category]
    return f"""
<div class="category-heading" style="color:{info['primary']}; border-left-color:{info['primary']}">
  {info['emoji']} {info['label']}
  <span class="category-heading-sub">— {count} 種収録</span>
</div>
"""
