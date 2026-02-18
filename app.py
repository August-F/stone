"""岩石図鑑 — 事典版 Streamlit アプリ"""

import streamlit as st
from data.rocks import CATEGORY_LABELS, get_rocks_by_category, search_rocks
from styles import CATEGORY_COLORS, category_heading_html, get_css, rock_entry_html

# ─── ページ設定 ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="岩石図鑑 事典版",
    page_icon="🪨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS をグローバルに注入（st.markdown のみ使用）
st.markdown(get_css(), unsafe_allow_html=True)

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
    st.markdown("### モース硬度の目安")
    for h, m in [
        ("1","滑石"),("2","石膏"),("3","方解石"),("4","蛍石"),("5","燐灰石"),
        ("6","正長石"),("7","石英"),("8","黄玉"),("9","鋼玉"),("10","金剛石"),
    ]:
        st.caption(f"**{h}** — {m}")


# ─── 検索モード ───────────────────────────────────────────────────────────────
if search_query:
    results = [
        r for r in search_rocks(search_query)
        if hardness_range[0] <= r["hardness"] <= hardness_range[1]
    ]
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
                st.html(rock_entry_html(rock, rock["category"]))
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
            filtered = [
                r for r in rocks
                if hardness_range[0] <= r["hardness"] <= hardness_range[1]
            ]

            st.html(category_heading_html(category, len(filtered)))

            if not filtered:
                st.warning("選択した硬度範囲に該当する岩石がありません。")
                continue

            cols = st.columns(2, gap="medium")
            for i, rock in enumerate(filtered):
                with cols[i % 2]:
                    st.html(rock_entry_html(rock, category))

# ─── フッター ─────────────────────────────────────────────────────────────────
st.html("""
<div class="encyclopedia-footer">
  <span class="ornament">◆</span>&ensp;岩石図鑑 事典版&ensp;<span class="ornament">◆</span>
  <br>データは教育目的のサンプルです。画像は Wikimedia Commons より引用。
</div>
""")
