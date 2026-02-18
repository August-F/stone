"""岩石分類 Streamlit アプリ"""

import streamlit as st
from data.rocks import CATEGORY_LABELS, get_rocks_by_category, search_rocks
from styles import CATEGORY_COLORS, get_css, rock_card_html

# ─── ページ設定 ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="岩石図鑑",
    page_icon="🪨",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(get_css(), unsafe_allow_html=True)

# ─── ヘッダー ─────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="app-header">
    <h1>🪨 岩石図鑑</h1>
    <p>火成岩・堆積岩・変成岩 — 18種類の岩石データを探索しよう</p>
</div>
""",
    unsafe_allow_html=True,
)

# ─── サイドバー ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("🔍 フィルター・検索")

    search_query = st.text_input("岩石名で検索", placeholder="例: 花崗岩、Marble …")

    st.markdown("---")
    st.subheader("硬度フィルター (モース硬度)")
    hardness_range = st.slider(
        "硬度の範囲",
        min_value=1.0,
        max_value=10.0,
        value=(1.0, 10.0),
        step=0.5,
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.subheader("凡例")
    for cat, info in CATEGORY_COLORS.items():
        label = CATEGORY_LABELS[cat]
        emoji = info["emoji"]
        color = info["primary"]
        st.markdown(
            f"<span style='color:{color}; font-weight:700'>{emoji} {label}</span>",
            unsafe_allow_html=True,
        )

# ─── 検索モード ───────────────────────────────────────────────────────────────
if search_query:
    results = search_rocks(search_query)
    # 硬度フィルター適用
    results = [
        r for r in results if hardness_range[0] <= r["hardness"] <= hardness_range[1]
    ]

    st.subheader(f"検索結果: 「{search_query}」— {len(results)} 件")
    if results:
        cols = st.columns(3)
        for i, rock in enumerate(results):
            with cols[i % 3]:
                st.markdown(
                    rock_card_html(rock, rock["category"]), unsafe_allow_html=True
                )
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

            # 硬度フィルター適用
            filtered = [
                r
                for r in rocks
                if hardness_range[0] <= r["hardness"] <= hardness_range[1]
            ]

            label = CATEGORY_LABELS[category]
            color = CATEGORY_COLORS[category]["primary"]
            st.markdown(
                f"<h3 style='color:{color}'>{label} — {len(filtered)} 種</h3>",
                unsafe_allow_html=True,
            )

            if not filtered:
                st.warning("選択した硬度範囲に該当する岩石がありません。")
            else:
                cols = st.columns(3)
                for i, rock in enumerate(filtered):
                    with cols[i % 3]:
                        st.markdown(
                            rock_card_html(rock, category), unsafe_allow_html=True
                        )

# ─── フッター ─────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="app-footer">
    岩石図鑑 | データは教育目的のサンプルです
</div>
""",
    unsafe_allow_html=True,
)
