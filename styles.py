"""カスタムCSSとスタイル定義"""

CATEGORY_COLORS = {
    "igneous": {
        "primary": "#C0392B",
        "light": "#FADBD8",
        "border": "#E74C3C",
        "emoji": "🌋",
    },
    "sedimentary": {
        "primary": "#784212",
        "light": "#FAD7A0",
        "border": "#E59866",
        "emoji": "🪨",
    },
    "metamorphic": {
        "primary": "#1A5276",
        "light": "#D6EAF8",
        "border": "#2E86C1",
        "emoji": "💎",
    },
}


def get_css() -> str:
    return """
<style>
    /* 全体 */
    .main .block-container {
        padding-top: 1.5rem;
        max-width: 1200px;
    }

    /* ヘッダー */
    .app-header {
        text-align: center;
        padding: 1.5rem 0 1rem;
        border-bottom: 2px solid #e0e0e0;
        margin-bottom: 1.5rem;
    }
    .app-header h1 {
        font-size: 2.4rem;
        margin-bottom: 0.3rem;
    }
    .app-header p {
        color: #666;
        font-size: 1rem;
    }

    /* 岩石カード */
    .rock-card {
        border-radius: 12px;
        padding: 1.1rem 1.2rem;
        margin-bottom: 1rem;
        border-left: 5px solid #ccc;
        background: #fafafa;
        box-shadow: 0 2px 6px rgba(0,0,0,0.07);
        transition: box-shadow 0.2s;
    }
    .rock-card:hover {
        box-shadow: 0 4px 14px rgba(0,0,0,0.13);
    }
    .rock-card-igneous {
        border-left-color: #E74C3C;
        background: #fff9f9;
    }
    .rock-card-sedimentary {
        border-left-color: #E59866;
        background: #fffaf5;
    }
    .rock-card-metamorphic {
        border-left-color: #2E86C1;
        background: #f5faff;
    }

    /* カードのタイトル */
    .rock-name {
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 0.15rem;
    }
    .rock-name-en {
        font-size: 0.82rem;
        color: #888;
        margin-bottom: 0.5rem;
    }
    .rock-desc {
        font-size: 0.88rem;
        color: #444;
        margin-bottom: 0.6rem;
        line-height: 1.5;
    }

    /* バッジ */
    .badge {
        display: inline-block;
        border-radius: 999px;
        padding: 0.18rem 0.7rem;
        font-size: 0.78rem;
        font-weight: 600;
        margin-right: 0.4rem;
        margin-bottom: 0.25rem;
    }
    .badge-hardness { background: #eee; color: #333; }
    .badge-color   { background: #f0f0f0; color: #333; }
    .badge-uses    { background: #e8f4f8; color: #1a5276; }

    /* サイドバー */
    .sidebar-section {
        background: #f7f7f7;
        border-radius: 8px;
        padding: 0.8rem 1rem;
        margin-bottom: 1rem;
    }

    /* フッター */
    .app-footer {
        text-align: center;
        color: #aaa;
        font-size: 0.8rem;
        padding: 2rem 0 0.5rem;
        border-top: 1px solid #eee;
        margin-top: 2rem;
    }

    /* レスポンシブ: 狭い画面では1列 */
    @media (max-width: 640px) {
        .app-header h1 { font-size: 1.6rem; }
        .rock-card { padding: 0.8rem; }
    }
</style>
"""


def rock_card_html(rock: dict, category: str) -> str:
    """岩石1枚分のカードHTMLを返す。"""
    colors = CATEGORY_COLORS.get(category, {})
    emoji = colors.get("emoji", "🪨")
    css_class = f"rock-card rock-card-{category}"
    return f"""
<div class="{css_class}">
  <div class="rock-name">{emoji} {rock['name']}</div>
  <div class="rock-name-en">{rock['name_en']}</div>
  <div class="rock-desc">{rock['description']}</div>
  <span class="badge badge-hardness">硬度 {rock['hardness']}</span>
  <span class="badge badge-color">🎨 {rock['color']}</span>
  <br>
  <span class="badge badge-uses">🔧 {rock['uses']}</span>
</div>
"""
