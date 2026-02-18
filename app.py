"""岩石図鑑 — 事典版 Streamlit アプリ"""

import requests
import streamlit as st

from data.rocks import (
    CATEGORY_LABELS,
    get_rock_by_name,
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


# ─── Wikipedia サムネイル取得 ──────────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def fetch_thumbnails(wiki_titles: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for title in wiki_titles:
        try:
            url = (
                "https://en.wikipedia.org/api/rest_v1/page/summary/"
                + title.replace(" ", "_")
            )
            resp = requests.get(
                url, timeout=6,
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
    st.markdown("## 🔍 検索")
    search_query = st.text_input(
        "岩石名で検索",
        placeholder="例: 花崗岩、Marble、マーブル …",
    )
    st.markdown("---")
    st.markdown("### 凡例")
    for cat, info in CATEGORY_COLORS.items():
        st.markdown(
            f"<span style='color:{info['primary']};font-weight:700;font-size:0.95rem'>"
            f"{info['emoji']} {info['label']}</span>",
            unsafe_allow_html=True,
        )


# ─── 画像プリフェッチ ─────────────────────────────────────────────────────────
from data.rocks import get_all_rocks

_all_titles = tuple(r["wiki_title"] for r in get_all_rocks() if r.get("wiki_title"))
with st.spinner("画像を読み込み中…"):
    _thumbnails = fetch_thumbnails(_all_titles)


def render_rock(rock: dict, category: str) -> None:
    img_url = resolve_image_url(rock, _thumbnails)
    st.html(rock_entry_html({**rock, "image_url": img_url}, category))


# ─── 同定チャートのデータ定義 ─────────────────────────────────────────────────
#  { 色ラベル: { 質感ラベル: [候補岩石名, ...] } }
CHART_TREE: dict[str, dict[str, list[str]]] = {
    "⬜ 白っぽい・クリーム色": {
        "粗粒：粒（結晶）が肉眼で見える": ["花崗岩", "大理石"],
        "砂粒感がある（ザラザラ）": ["砂岩"],
        "水に浮く・多孔質": ["軽石"],
        "食酢をかけると泡立つ": ["石灰岩", "大理石"],
        "非常に硬くガラス質の光沢": ["チャート", "石英岩"],
        "塩辛い・立方体に割れる": ["岩塩"],
    },
    "⬛ 黒っぽい": {
        "ガラス光沢・貝殻状断口（断面が鋭利）": ["黒曜石"],
        "重く緻密・柱状の割れ目（柱状節理）": ["玄武岩"],
        "緻密・角状に割れる・金属音がする": ["ホルンフェルス"],
        "軽い・多孔質（スポンジ状）": ["軽石"],
    },
    "🔲 灰色・褐灰色": {
        "白い斑晶（白い粒）が散在している": ["安山岩"],
        "縞状の地層構造・砂粒感がある": ["砂岩", "泥岩"],
        "板状に薄く割れる・キラキラ光る": ["片岩", "泥岩"],
        "緻密・硬く均質・重い": ["ホルンフェルス", "玄武岩"],
        "明暗の太い縞・粗粒（結晶が見える）": ["片麻岩"],
    },
    "🟥 赤・ピンク・茶色": {
        "流れた縞模様（流理構造）がある": ["流紋岩"],
        "砂粒感がある（ザラザラ）": ["砂岩"],
        "ピンク色・塩辛い": ["岩塩"],
        "緻密・非常に硬い・ガラス光沢": ["チャート"],
        "粗粒：石英・長石・雲母が見える": ["花崗岩"],
    },
    "🟩 緑系": {
        "ツルツル・脂ぎった光沢・蛇皮模様": ["蛇紋岩"],
        "板状剥離・銀色のキラキラ（雲母光沢）": ["片岩"],
        "赤・緑・灰の細かい縞・非常に硬い": ["チャート"],
    },
    "🌈 縞模様・混合色": {
        "礫（砂利）が基質に埋まっている": ["礫岩"],
        "明暗の太い縞・粗粒（長石・石英が見える）": ["片麻岩"],
        "細かい赤・緑・灰の縞（緻密・硬い）": ["チャート"],
        "白・ピンク・赤の流れ縞": ["流紋岩"],
    },
}

COLOR_LABELS = list(CHART_TREE.keys())


def render_chart_candidate(name: str) -> None:
    """同定チャートの候補岩石をコンパクトカードで表示。"""
    result = get_rock_by_name(name)
    if result is None:
        return
    rock, category = result
    info = CATEGORY_COLORS[category]
    img_url = resolve_image_url(rock, _thumbnails)

    # 画像
    if img_url:
        st.image(img_url, use_container_width=True)
    else:
        st.html(
            f'<div style="background:{info["light"]};height:120px;display:flex;'
            f'align-items:center;justify-content:center;font-size:2.5rem;'
            f'border-radius:4px;border:1px solid {info["border"]}">'
            f'{info["emoji"]}</div>'
        )

    # タイトル行
    st.html(
        f'<div style="margin:0.4rem 0 0.1rem">'
        f'<span style="font-size:1.1rem;font-weight:700;font-family:serif;color:#1A0A00">'
        f'{name}</span>'
        f'<span style="font-size:0.8rem;color:#888;margin-left:0.4rem">'
        f'{rock["name_en"]} / {rock["name_kana"]}</span>'
        f'</div>'
    )

    # カテゴリバッジ
    st.html(
        f'<span style="background:{info["light"]};color:{info["primary"]};'
        f'border:1px solid {info["border"]};border-radius:2px;'
        f'padding:0.1rem 0.5rem;font-size:0.75rem;font-weight:600">'
        f'{info["emoji"]} {info["label"]}</span>'
    )

    # 短い説明
    st.caption(rock["description"])

    # 露頭の見分け方（最初の1文のみ）
    first_tip = rock.get("field_id", "").split("。")[0]
    if first_tip:
        st.html(
            f'<div style="background:#FFFDF0;border-left:3px solid #C9A84C;'
            f'padding:0.3rem 0.5rem;font-size:0.78rem;color:#4A3000;margin-top:0.3rem">'
            f'🔎 {first_tip}。</div>'
        )

    st.divider()


def render_identification_chart() -> None:
    """露頭での岩石同定チャートを表示。"""
    st.html("""
    <div style="margin-bottom:1rem">
      <h3 style="font-family:serif;color:#2C1810;margin-bottom:0.2rem">
        🔍 露頭での岩石同定チャート
      </h3>
      <p style="color:#666;font-size:0.9rem;margin:0">
        観察できる特徴を 2 ステップで選ぶと候補岩石を表示します。
      </p>
    </div>
    """)

    col_q, col_r = st.columns([1, 1], gap="large")

    with col_q:
        # ── Step 1: 色 ────────────────────────────────────────
        st.markdown("#### Step 1　— 色の印象は？")
        color_choice = st.radio(
            "色の印象",
            options=COLOR_LABELS,
            index=None,
            label_visibility="collapsed",
        )

        # ── Step 2: 質感（色が選ばれたとき表示） ───────────────
        texture_choice = None
        if color_choice:
            options_2 = list(CHART_TREE[color_choice].keys())
            st.markdown("#### Step 2　— 質感・特徴は？")
            texture_choice = st.radio(
                "質感・特徴",
                options=options_2,
                index=None,
                label_visibility="collapsed",
            )

        # ── ヒント ────────────────────────────────────────────
        st.html("""
        <div style="margin-top:1.5rem;background:#F5F0E8;border-radius:4px;
                    padding:0.8rem 1rem;font-size:0.8rem;color:#5C3D1A;line-height:1.8">
          <strong>📋 識別に役立つテスト</strong><br>
          ⬡ <b>酸テスト</b>：食酢をかけて泡立てば炭酸塩岩（石灰岩・大理石）<br>
          ⬡ <b>浮力テスト</b>：水に浮けば軽石<br>
          ⬡ <b>塩味テスト</b>：舌先に乗せて塩辛ければ岩塩<br>
          ⬡ <b>硬度テスト</b>：爪で傷つく（軟）→ コインで傷つく（中）→ 鉄で傷つかない（硬）<br>
          ⬡ <b>音テスト</b>：打つと金属音がすれば緻密な変成岩（ホルンフェルスなど）
        </div>
        """)

    with col_r:
        if color_choice is None:
            st.html("""
            <div style="height:300px;display:flex;align-items:center;justify-content:center;
                        background:#FDFAF5;border:2px dashed #DDD5C0;border-radius:8px;
                        color:#A08060;font-size:1rem;text-align:center;padding:2rem">
              ← Step 1 の色を選択すると<br>候補岩石が表示されます
            </div>
            """)
        elif texture_choice is None:
            # Step 1 完了・Step 2 未選択 → このカテゴリの全候補を薄く表示
            all_candidates: list[str] = []
            for names in CHART_TREE[color_choice].values():
                for n in names:
                    if n not in all_candidates:
                        all_candidates.append(n)
            st.markdown(
                f"**{color_choice}** に該当する可能性がある岩石（Step 2 で絞り込み）："
            )
            tags = "".join(
                f'<span style="display:inline-block;background:#EEE;border-radius:3px;'
                f'padding:0.15rem 0.6rem;margin:0.2rem;font-size:0.85rem">{n}</span>'
                for n in all_candidates
            )
            st.html(f'<div style="line-height:2">{tags}</div>')
        else:
            # Step 1 & 2 完了 → 候補表示
            candidates = CHART_TREE[color_choice].get(texture_choice, [])
            if candidates:
                st.markdown(
                    f"**候補岩石 {len(candidates)} 種**"
                    f"（{color_choice.split(' ', 1)[-1]} × {texture_choice}）"
                )
                for name in candidates:
                    render_chart_candidate(name)
            else:
                st.info("該当する岩石が見つかりませんでした。Step 1・2 を見直してください。")


# ─── 検索モード ───────────────────────────────────────────────────────────────
if search_query:
    results = search_rocks(search_query)
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
    ] + ["🔍 同定チャート"]

    tabs = st.tabs(tab_labels)

    for tab, category in zip(tabs[:3], categories):
        with tab:
            rocks = get_rocks_by_category(category)
            st.html(category_heading_html(category, len(rocks)))
            cols = st.columns(2, gap="medium")
            for i, rock in enumerate(rocks):
                with cols[i % 2]:
                    render_rock(rock, category)

    with tabs[3]:
        render_identification_chart()

# ─── フッター ─────────────────────────────────────────────────────────────────
st.html("""
<div class="encyclopedia-footer">
  <span class="ornament">◆</span>&ensp;岩石図鑑 事典版&ensp;<span class="ornament">◆</span>
  <br>データは教育目的のサンプルです。画像は Wikipedia より引用。
</div>
""")
