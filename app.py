"""岩石図鑑 — 事典版 Streamlit アプリ"""

import requests
import streamlit as st

from data.rocks import (
    CATEGORY_LABELS,
    get_all_color_tokens,
    get_all_use_tokens,
    get_rocks_by_category,
    search_rocks,
)
from styles import CATEGORY_COLORS, category_heading_html, get_css, rock_entry_html

# ─── ページ設定 ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="岩石図鑑 事典版",
    page_icon="🪨",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(get_css(), unsafe_allow_html=True)


# ─── Wikipedia サムネイル取得（セッション内キャッシュ） ────────────────────────
@st.cache_data(show_spinner=False)
def fetch_thumbnails(wiki_titles: tuple[str, ...]) -> dict[str, str]:
    """Wikipedia REST API で各ページのサムネイルURLを一括取得する。"""
    result: dict[str, str] = {}
    for title in wiki_titles:
        try:
            url = (
                "https://en.wikipedia.org/api/rest_v1/page/summary/"
                + title.replace(" ", "_")
            )
            resp = requests.get(
                url,
                timeout=6,
                headers={"User-Agent": "RockEncyclopediaApp/2.0 (educational)"},
            )
            if resp.status_code == 200:
                thumb = resp.json().get("thumbnail", {}).get("source", "")
                if thumb:
                    result[title] = thumb
        except Exception:
            pass
    return result


def resolve_image_url(rock: dict, thumbnail_cache: dict[str, str]) -> str:
    """キャッシュから画像URLを返す。取得できなければ空文字。"""
    return thumbnail_cache.get(rock.get("wiki_title", ""), "")


# ─── ヘッダー ─────────────────────────────────────────────────────────────────
st.html("""
<div class="encyclopedia-header">
  <h1>🪨 岩石図鑑</h1>
  <p class="subtitle">ILLUSTRATED ENCYCLOPEDIA OF ROCKS AND MINERALS</p>
  <div class="edition">火成岩 · 堆積岩 · 変成岩　全18種収録</div>
</div>
""")

# ─── サイドバー ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🔍 検索・絞り込み")
    search_query = st.text_input(
        "岩石名で検索",
        placeholder="例: 花崗岩、Marble、マーブル …",
    )

    st.markdown("---")
    st.markdown("### ⬡ 硬度フィルター")
    st.caption("モース硬度スケール (1〜10)")
    hardness_range = st.slider(
        "硬度の範囲",
        min_value=1.0,
        max_value=10.0,
        value=(1.0, 10.0),
        step=0.5,
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown("### 凡例")
    for cat, info in CATEGORY_COLORS.items():
        st.markdown(
            f"<span style='color:{info['primary']};font-weight:700;font-size:0.95rem'>"
            f"{info['emoji']} {info['label']}</span>",
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 🎨 色で絞り込み")
    all_colors = get_all_color_tokens()
    selected_colors = st.multiselect(
        "色を選択（複数可）",
        options=all_colors,
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown("### 🔧 用途で絞り込み")
    all_uses = get_all_use_tokens()
    selected_uses = st.multiselect(
        "用途を選択（複数可）",
        options=all_uses,
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown("### モース硬度の目安")
    for h, m in [
        ("1", "滑石"), ("2", "石膏"), ("3", "方解石"), ("4", "蛍石"), ("5", "燐灰石"),
        ("6", "正長石"), ("7", "石英"), ("8", "黄玉"), ("9", "鋼玉"), ("10", "金剛石"),
    ]:
        st.caption(f"**{h}** — {m}")


# ─── 画像を一括プリフェッチ ───────────────────────────────────────────────────
from data.rocks import get_all_rocks

_all_titles = tuple(
    r["wiki_title"] for r in get_all_rocks() if r.get("wiki_title")
)
with st.spinner("画像を読み込み中…"):
    _thumbnails = fetch_thumbnails(_all_titles)


def apply_filters(
    rocks: list[dict],
    hardness_range: tuple[float, float],
    selected_colors: list[str],
    selected_uses: list[str],
) -> list[dict]:
    result = []
    for rock in rocks:
        if not (hardness_range[0] <= rock["hardness"] <= hardness_range[1]):
            continue
        if selected_colors:
            rock_colors = [c.strip() for c in rock["color"].split("・")]
            if not any(c in selected_colors for c in rock_colors):
                continue
        if selected_uses:
            rock_uses = [u.strip() for u in rock["uses"].split("・")]
            if not any(u in selected_uses for u in rock_uses):
                continue
        result.append(rock)
    return result


def render_rock(rock: dict, category: str) -> None:
    img_url = resolve_image_url(rock, _thumbnails)
    st.html(rock_entry_html({**rock, "image_url": img_url}, category))


# ─── 検索モード ───────────────────────────────────────────────────────────────
if search_query:
    results = apply_filters(
        search_rocks(search_query), hardness_range, selected_colors, selected_uses
    )
    st.html(
        f'<h3 style="color:#5C2D0A;font-family:serif">'
        f'検索結果：「{search_query}」'
        f'<span style="font-size:0.85rem;color:#888"> — {len(results)} 件</span>'
        f'</h3>'
    )
    if results:
        cols = st.columns(2, gap="medium")
        for i, rock in enumerate(results):
            with cols[i % 2]:
                render_rock(rock, rock["category"])
    else:
        st.info("該当する岩石が見つかりませんでした。")

# ─── タブ表示モード ───────────────────────────────────────────────────────────
else:
    categories = list(CATEGORY_LABELS.keys())
    tab_labels = [
        f"{CATEGORY_COLORS[c]['emoji']} {CATEGORY_LABELS[c]}" for c in categories
    ]
    tabs = st.tabs(tab_labels)

    for tab, category in zip(tabs, categories):
        with tab:
            rocks = get_rocks_by_category(category)
            filtered = apply_filters(
                rocks, hardness_range, selected_colors, selected_uses
            )

            st.html(category_heading_html(category, len(filtered)))

            if not filtered:
                st.warning("選択した硬度範囲に該当する岩石がありません。")
                continue

            cols = st.columns(2, gap="medium")
            for i, rock in enumerate(filtered):
                with cols[i % 2]:
                    render_rock(rock, category)

# ─── フッター ─────────────────────────────────────────────────────────────────
st.html("""
<div class="encyclopedia-footer">
  <span class="ornament">◆</span>&ensp;岩石図鑑 事典版&ensp;<span class="ornament">◆</span>
  <br>データは教育目的のサンプルです。画像は Wikipedia より引用。
</div>
""")
