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
st.markdown(get_css(), unsafe_allow_html=True)

# ─── ヘッダー ─────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="encyclopedia-header">
  <h1>🪨 岩石図鑑</h1>
  <p class="subtitle">ILLUSTRATED ENCYCLOPEDIA OF ROCKS AND MINERALS</p>
  <div class="edition">火成岩 · 堆積岩 · 変成岩　全18種収録</div>
</div>
""",
    unsafe_allow_html=True,
)

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
            f"<span style='color:{info['primary']}; font-weight:700; font-size:0.95rem'>"
            f"{info['emoji']} {info['label']}</span>",
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### モース硬度の目安")
    mohs = [
        ("1", "滑石"),
        ("2", "石膏"),
        ("3", "方解石"),
        ("4", "蛍石"),
        ("5", "燐灰石"),
        ("6", "正長石"),
        ("7", "石英"),
        ("8", "黄玉"),
        ("9", "鋼玉"),
        ("10", "金剛石"),
    ]
    for h, m in mohs:
        st.caption(f"**{h}** — {m}")


def show_rock_with_image(rock: dict, category: str):
    """画像＋テキストエントリーを表示。"""
    img_col, txt_col = st.columns([1, 2])
    with img_col:
        try:
            st.image(
                rock["image_url"],
                use_container_width=True,
                caption=f"{rock['name']} ({rock['name_en']})",
            )
        except Exception:
            info = CATEGORY_COLORS[category]
            st.markdown(
                f"<div style='background:{info['light']};border:1px solid {info['border']};"
                f"border-radius:4px;height:160px;display:flex;align-items:center;"
                f"justify-content:center;font-size:3rem;'>{info['emoji']}</div>",
                unsafe_allow_html=True,
            )
    with txt_col:
        st.markdown(rock_entry_html(rock, category), unsafe_allow_html=True)


# ─── 検索モード ───────────────────────────────────────────────────────────────
if search_query:
    results = [
        r for r in search_rocks(search_query)
        if hardness_range[0] <= r["hardness"] <= hardness_range[1]
    ]
    st.markdown(
        f"<h3 style='color:#5C2D0A; font-family:serif'>検索結果：「{search_query}」"
        f"&nbsp;<span style='font-size:0.85rem;color:#888'>— {len(results)} 件</span></h3>",
        unsafe_allow_html=True,
    )
    if results:
        for rock in results:
            show_rock_with_image(rock, rock["category"])
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

            st.markdown(
                category_heading_html(category, len(filtered)),
                unsafe_allow_html=True,
            )

            if not filtered:
                st.warning("選択した硬度範囲に該当する岩石がありません。")
                continue

            # 2列グリッド
            left_rocks = filtered[::2]
            right_rocks = filtered[1::2]
            col_l, col_r = st.columns(2, gap="medium")

            for col, rocks_col in ((col_l, left_rocks), (col_r, right_rocks)):
                with col:
                    for rock in rocks_col:
                        # 画像
                        try:
                            st.image(
                                rock["image_url"],
                                use_container_width=True,
                            )
                        except Exception:
                            info = CATEGORY_COLORS[category]
                            st.markdown(
                                f"<div style='background:{info['light']};border:1px solid "
                                f"{info['border']};border-radius:2px;height:140px;"
                                f"display:flex;align-items:center;justify-content:center;"
                                f"font-size:2.8rem'>{info['emoji']}</div>",
                                unsafe_allow_html=True,
                            )
                        # テキストエントリー
                        st.markdown(
                            rock_entry_html(rock, category),
                            unsafe_allow_html=True,
                        )

# ─── フッター ─────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="encyclopedia-footer">
  <span class="ornament">◆</span>&ensp;岩石図鑑 事典版&ensp;<span class="ornament">◆</span>
  <br>データは教育目的のサンプルです。画像は Wikimedia Commons より引用。
</div>
""",
    unsafe_allow_html=True,
)
