"""岩石図鑑 — 事典版 Streamlit アプリ"""

import requests
import streamlit as st
from concurrent.futures import ThreadPoolExecutor

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
    initial_sidebar_state="collapsed",
)
st.markdown(get_css(), unsafe_allow_html=True)


# ─── Wikipedia サムネイル取得 ──────────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def fetch_thumbnails(wiki_titles: tuple[str, ...]) -> dict[str, str]:
    def _fetch_one(title: str) -> tuple[str, str]:
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
                    return title, thumb
        except Exception:
            pass
        return title, ""

    result: dict[str, str] = {}
    with ThreadPoolExecutor(max_workers=6) as executor:
        for title, thumb in executor.map(_fetch_one, wiki_titles):
            if thumb:
                result[title] = thumb
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


# ─── 画像プリフェッチ ─────────────────────────────────────────────────────────
from data.rocks import get_all_rocks

_all_titles = tuple(r["wiki_title"] for r in get_all_rocks() if r.get("wiki_title"))
with st.spinner("画像を読み込み中…"):
    _thumbnails = fetch_thumbnails(_all_titles)


def render_rock(rock: dict, category: str) -> None:
    img_url = resolve_image_url(rock, _thumbnails)
    st.html(rock_entry_html({**rock, "image_url": img_url}, category))
    with st.expander("📖 詳しく見る"):
        detail_sentences = [s.strip() for s in rock["description_detail"].split("。") if s.strip()]
        detail_html = "。<br>".join(detail_sentences) + "。"
        st.html(f'<p class="rock-detail-desc" style="margin:0.3rem 0">{detail_html}</p>')
        field_sentences = [s.strip() for s in rock.get("field_id", "").split("。") if s.strip()]
        if field_sentences:
            field_content = "。<br>".join(field_sentences) + "。"
            st.html(
                f'<div class="rock-field-id">'
                f'<span class="rock-field-id-label">🔎 露頭での見分け方</span>'
                f'{field_content}</div>'
            )


# ─── 検索 ─────────────────────────────────────────────────────────────────────
_search_query = st.text_input(
    "🔍 岩石を検索",
    placeholder="例：花崗岩、赤い、セメント、硬い…",
    key="rock_search",
    label_visibility="collapsed",
)
if _search_query:
    _results = search_rocks(_search_query)
    if _results:
        st.markdown(f"**「{_search_query}」の検索結果 — {len(_results)} 件**")
        _cols = st.columns(min(len(_results), 2), gap="medium")
        for _i, _rock in enumerate(_results):
            with _cols[_i % 2]:
                render_rock(_rock, _rock["category"])
    else:
        st.info(f"「{_search_query}」に一致する岩石は見つかりませんでした。")
    st.stop()


# ─── 同定チャートのデータ定義 ─────────────────────────────────────────────────
#  { 色ラベル: { 質感ラベル: [候補岩石名, ...] } }
CHART_TREE: dict[str, dict[str, list[str]]] = {
    "⬜ 白っぽい・クリーム色": {
        "粒や結晶がはっきり見える": ["花崗岩", "大理石"],
        "ざらざらして砂粒っぽい": ["砂岩"],
        "水に浮くほど軽い": ["軽石"],
        "お酢をかけると泡が出る": ["石灰岩", "大理石"],
        "とても硬くガラスのように光る": ["チャート", "石英岩"],
        "なめると塩辛い": ["岩塩"],
    },
    "⬛ 黒っぽい": {
        "ガラスのように光り、断面が鋭い": ["黒曜石"],
        "重くて緻密、柱状に割れている": ["玄武岩"],
        "硬くて角ばり、叩くと金属音": ["ホルンフェルス"],
        "軽くてスポンジのような穴がある": ["軽石"],
    },
    "🔲 灰色・褐灰色": {
        "白い粒がまばらに混じっている": ["安山岩"],
        "層状の縞があってざらざらする": ["砂岩", "泥岩"],
        "薄い板状に割れてキラキラ光る": ["片岩", "泥岩"],
        "硬くて均質、ずっしり重い": ["ホルンフェルス", "玄武岩"],
        "太い明暗の縞で粒が見える": ["片麻岩"],
    },
    "🟥 赤・ピンク・茶色": {
        "流れたような縞模様がある": ["流紋岩"],
        "ざらざらして砂粒っぽい": ["砂岩"],
        "ピンク色でなめると塩辛い": ["岩塩"],
        "とても硬くガラスのように光る": ["チャート"],
        "粒が大きく石英・長石・雲母が見える": ["花崗岩"],
    },
    "🟩 緑系": {
        "つるつるして脂っぽい光沢がある": ["蛇紋岩"],
        "薄く剥がれてキラキラ（雲母光沢）": ["片岩"],
        "赤・緑・灰の細かい縞で硬い": ["チャート"],
    },
    "🌈 縞模様・混合色": {
        "砂利（礫）が埋め込まれている": ["礫岩"],
        "太い明暗の縞で粒が大きい": ["片麻岩"],
        "細かい赤・緑・灰の縞で硬い": ["チャート"],
        "白・ピンク・赤が流れるような縞": ["流紋岩"],
    },
}

COLOR_LABELS = list(CHART_TREE.keys())

# ─── Step 3 絞り込みデータ ────────────────────────────────────────────────────
#  { (色ラベル, 質感ラベル): { "q": 質問文, "opts": {選択肢: 岩石名} } }
STEP3_TREE: dict[tuple[str, str], dict] = {
    ("⬜ 白っぽい・クリーム色", "粒や結晶がはっきり見える"): {
        "q": "お酢をかけると泡が出る？",
        "opts": {
            "泡が出る": "大理石",
            "泡が出ない（石英・長石・雲母の粒が混じる）": "花崗岩",
        },
    },
    ("⬜ 白っぽい・クリーム色", "お酢をかけると泡が出る"): {
        "q": "砂糖状の結晶が見えるほど粗い？",
        "opts": {
            "はい（結晶が見える）": "大理石",
            "いいえ（緻密か化石が含まれる）": "石灰岩",
        },
    },
    ("⬜ 白っぽい・クリーム色", "とても硬くガラスのように光る"): {
        "q": "粒が見えず、縞模様や緻密な質感がある？",
        "opts": {
            "はい（緻密・縞あり）": "チャート",
            "いいえ（砂糖状の粒が見える）": "石英岩",
        },
    },
    ("🔲 灰色・褐灰色", "層状の縞があってざらざらする"): {
        "q": "砂粒が指に感じる？",
        "opts": {
            "はい（ザラザラする）": "砂岩",
            "いいえ（とても細かくツルッとしている）": "泥岩",
        },
    },
    ("🔲 灰色・褐灰色", "薄い板状に割れてキラキラ光る"): {
        "q": "雲母のキラキラした光沢がある？",
        "opts": {
            "はい（雲母がキラキラしている）": "片岩",
            "いいえ（光沢がなく爪で傷つく）": "泥岩",
        },
    },
    ("🔲 灰色・褐灰色", "硬くて均質、ずっしり重い"): {
        "q": "叩くと高い金属音がする？",
        "opts": {
            "はい（金属音）": "ホルンフェルス",
            "いいえ（鈍い音・小さな気泡の跡がある）": "玄武岩",
        },
    },
}


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
        f'<span class="chart-cand-name">{name}</span>'
        f'<span class="chart-cand-sub">{rock["name_en"]} / {rock["name_kana"]}</span>'
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

    # スペックバッジ
    st.html(
        f'<div class="rock-specs" style="margin:0.3rem 0">'
        f'<span class="rock-spec-badge">&#x2B21; 硬度&nbsp;<strong>{rock["hardness"]}</strong></span>'
        f'<span class="rock-spec-badge">&#127912;&nbsp;<strong>{rock["color"]}</strong></span>'
        f'<span class="rock-spec-badge">&#128295;&nbsp;{rock["uses"]}</span>'
        f'</div>'
    )

    # 詳しい説明
    detail_sentences = [s.strip() for s in rock["description_detail"].split("。") if s.strip()]
    detail_html = "。<br>".join(detail_sentences) + "。"
    st.html(f'<p class="rock-detail-desc" style="margin-top:0.3rem">{detail_html}</p>')

    # 露頭の見分け方（最初の1文のみ）
    first_tip = rock.get("field_id", "").split("。")[0]
    if first_tip:
        st.html(f'<div class="chart-cand-tip">🔎 {first_tip}。</div>')

    st.divider()


@st.fragment
def render_identification_chart() -> None:
    """露頭での岩石同定チャートを表示。"""
    st.html("""
    <div style="margin-bottom:1rem">
      <h3 class="chart-header-title">🔍 露頭での岩石同定チャート</h3>
      <p class="chart-header-sub">観察できる特徴を最大 3 ステップで選ぶと候補岩石を表示します。</p>
    </div>
    """)

    # ── リセットボタン ────────────────────────────────────────
    _reset_col, _ = st.columns([1, 4])
    with _reset_col:
        if st.button("🔄 最初からやり直す", key="chart_reset"):
            for _k in [k for k in st.session_state if k.startswith("id_chart_")]:
                del st.session_state[_k]
            st.rerun()

    col_q, col_r = st.columns([1, 1], gap="large")

    with col_q:
        # ── Step 1: 色 ────────────────────────────────────────
        st.markdown("#### Step 1　— 色の印象は？")
        color_choice = st.radio(
            "色の印象",
            options=COLOR_LABELS,
            index=None,
            label_visibility="collapsed",
            key="id_chart_color",
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
                key=f"id_chart_texture_{color_choice}",
            )

        # ── Step 3: 追加の特徴（絞り込みが必要なときのみ表示） ──
        step3_choice = None
        if color_choice and texture_choice:
            step3_entry = STEP3_TREE.get((color_choice, texture_choice))
            if step3_entry:
                st.markdown(f"#### Step 3　— {step3_entry['q']}")
                step3_choice = st.radio(
                    "追加の特徴",
                    options=list(step3_entry["opts"].keys()),
                    index=None,
                    label_visibility="collapsed",
                    key=f"id_chart_step3_{color_choice}_{texture_choice}",
                )

        # ── ヒント ────────────────────────────────────────────
        st.html("""
        <div class="chart-hint-box">
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
            <div class="chart-empty">
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
                f'<span class="chart-cand-tag">{n}</span>'
                for n in all_candidates
            )
            st.html(f'<div style="line-height:2">{tags}</div>')
        else:
            # Step 1 & 2 完了
            candidates = CHART_TREE[color_choice].get(texture_choice, [])
            step3_entry = STEP3_TREE.get((color_choice, texture_choice))

            if step3_entry:
                if step3_choice is None:
                    # Step 3 未回答 → 候補2種をタグ表示して促す
                    st.markdown(
                        f"**候補 {len(candidates)} 種** — Step 3 で 1 種に絞り込んでください"
                    )
                    tags = "".join(
                        f'<span class="chart-cand-tag">{n}</span>'
                        for n in candidates
                    )
                    st.html(f'<div style="line-height:2">{tags}</div>')
                else:
                    # Step 3 回答済み → 1種に確定
                    final = step3_entry["opts"][step3_choice]
                    st.html(f"""
                    <div class="chart-verdict">
                      <div class="verdict-label">それはおそらく</div>
                      <div class="verdict-name">{final}</div>
                      <div class="verdict-label">です</div>
                    </div>
                    """)
                    render_chart_candidate(final)
            elif candidates:
                # Step 3 不要で1種に確定
                [name] = candidates
                st.html(f"""
                <div class="chart-verdict">
                  <div class="verdict-label">それはおそらく</div>
                  <div class="verdict-name">{name}</div>
                  <div class="verdict-label">です</div>
                </div>
                """)
                render_chart_candidate(name)
            else:
                st.info("該当する岩石が見つかりませんでした。Step 1・2 を見直してください。")


# ─── タブ表示 ─────────────────────────────────────────────────────────────────
categories = list(CATEGORY_LABELS.keys())
tab_labels = ["🔍 この石なに？"] + [
    f"{CATEGORY_COLORS[c]['emoji']} {CATEGORY_LABELS[c]}" for c in categories
]

tab_chart, tab_igneous, tab_sedimentary, tab_metamorphic = st.tabs(tab_labels)

with tab_chart:
    render_identification_chart()

with tab_igneous:
    rocks = get_rocks_by_category("igneous")
    st.html(category_heading_html("igneous", len(rocks)))
    cols = st.columns(2, gap="medium")
    for i, rock in enumerate(rocks):
        with cols[i % 2]:
            render_rock(rock, "igneous")

with tab_sedimentary:
    rocks = get_rocks_by_category("sedimentary")
    st.html(category_heading_html("sedimentary", len(rocks)))
    cols = st.columns(2, gap="medium")
    for i, rock in enumerate(rocks):
        with cols[i % 2]:
            render_rock(rock, "sedimentary")

with tab_metamorphic:
    rocks = get_rocks_by_category("metamorphic")
    st.html(category_heading_html("metamorphic", len(rocks)))
    cols = st.columns(2, gap="medium")
    for i, rock in enumerate(rocks):
        with cols[i % 2]:
            render_rock(rock, "metamorphic")

# ─── フッター ─────────────────────────────────────────────────────────────────
st.html("""
<div class="encyclopedia-footer">
  <span class="ornament">◆</span>&ensp;岩石図鑑 事典版&ensp;<span class="ornament">◆</span>
  <br>データは教育目的のサンプルです。画像は Wikipedia より引用。
</div>
""")
