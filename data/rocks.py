"""岩石分類データモジュール"""

ROCKS = {
    "igneous": [
        {
            "name": "花崗岩",
            "name_en": "Granite",
            "description": "石英・長石・黒雲母などからなる深成岩。地殻の大部分を構成する。",
            "hardness": 6.5,
            "color": "灰白色・ピンク",
            "uses": "建築材・墓石・カウンタートップ",
        },
        {
            "name": "玄武岩",
            "name_en": "Basalt",
            "description": "鉄・マグネシウムに富む暗色の火山岩。海洋地殻の主な構成岩石。",
            "hardness": 6.0,
            "color": "黒・暗灰色",
            "uses": "道路舗装・建築石材・石畳",
        },
        {
            "name": "黒曜石",
            "name_en": "Obsidian",
            "description": "急冷された溶岩が固まったガラス質の火山岩。非常に鋭い断口を持つ。",
            "hardness": 5.5,
            "color": "黒・暗褐色",
            "uses": "装飾品・外科用メス（先史時代）・宝飾品",
        },
        {
            "name": "軽石",
            "name_en": "Pumice",
            "description": "無数の気泡を含む多孔質の火山岩。水に浮くほど軽い。",
            "hardness": 6.0,
            "color": "白・薄灰色",
            "uses": "研磨剤・コンクリート混合材・スキンケア",
        },
        {
            "name": "安山岩",
            "name_en": "Andesite",
            "description": "中程度のシリカ含有量を持つ火山岩。火山の斜面に多く見られる。",
            "hardness": 6.0,
            "color": "灰色・褐灰色",
            "uses": "建築材・砂利・路盤材",
        },
        {
            "name": "流紋岩",
            "name_en": "Rhyolite",
            "description": "花崗岩と同じ成分を持つ火山岩。流れ模様（流理構造）が特徴。",
            "hardness": 6.5,
            "color": "ピンク・赤・灰色",
            "uses": "装飾石材・研磨材",
        },
    ],
    "sedimentary": [
        {
            "name": "砂岩",
            "name_en": "Sandstone",
            "description": "砂粒が堆積・固結した岩石。粒の大きさが0.06〜2mmの岩石。",
            "hardness": 6.0,
            "color": "黄・赤・茶・灰色",
            "uses": "建築材・舗装材・フィルタリング材",
        },
        {
            "name": "石灰岩",
            "name_en": "Limestone",
            "description": "炭酸カルシウムを主成分とする堆積岩。サンゴや貝殻が起源のことが多い。",
            "hardness": 3.0,
            "color": "白・灰・黄",
            "uses": "セメント原料・建築材・農業用石灰",
        },
        {
            "name": "泥岩",
            "name_en": "Mudstone",
            "description": "泥が固まった岩石。粒径が0.06mm以下の細粒堆積岩。",
            "hardness": 2.5,
            "color": "灰・黒・茶",
            "uses": "陶芸原料・レンガ材料・陶器",
        },
        {
            "name": "礫岩",
            "name_en": "Conglomerate",
            "description": "礫（2mm以上の粒）が泥や砂で固められた堆積岩。",
            "hardness": 6.0,
            "color": "混合色",
            "uses": "建築骨材・装飾石材",
        },
        {
            "name": "チャート",
            "name_en": "Chert",
            "description": "放散虫などの珪酸質生物の遺骸が堆積した緻密な岩石。",
            "hardness": 7.0,
            "color": "赤・緑・灰・黒",
            "uses": "火打石（先史時代）・研磨材",
        },
        {
            "name": "岩塩",
            "name_en": "Rock Salt",
            "description": "塩化ナトリウムを主成分とする蒸発岩。海水の蒸発により形成される。",
            "hardness": 2.5,
            "color": "白・透明・ピンク",
            "uses": "食塩・化学工業原料・道路の融雪剤",
        },
    ],
    "metamorphic": [
        {
            "name": "大理石",
            "name_en": "Marble",
            "description": "石灰岩が熱や圧力で変成した岩石。美しい模様と光沢が特徴。",
            "hardness": 3.0,
            "color": "白・灰・黒・色多様",
            "uses": "彫刻・建築内装・床材・カウンタートップ",
        },
        {
            "name": "片岩",
            "name_en": "Schist",
            "description": "強い変成作用を受け、雲母などの板状鉱物が平行に並んだ岩石。",
            "hardness": 5.0,
            "color": "銀灰色・緑・茶",
            "uses": "装飾石材・建築外装",
        },
        {
            "name": "片麻岩",
            "name_en": "Gneiss",
            "description": "高温高圧の変成作用を受けた岩石。縞状の模様が特徴。",
            "hardness": 6.5,
            "color": "灰白色・縞模様",
            "uses": "建築石材・舗装材",
        },
        {
            "name": "石英岩",
            "name_en": "Quartzite",
            "description": "砂岩が変成してできた非常に硬い岩石。石英が主成分。",
            "hardness": 7.0,
            "color": "白・灰・ピンク",
            "uses": "耐火材・研磨材・装飾石材",
        },
        {
            "name": "ホルンフェルス",
            "name_en": "Hornfels",
            "description": "マグマの熱によって接触変成を受けた緻密で硬い岩石。",
            "hardness": 6.5,
            "color": "黒・暗灰・茶",
            "uses": "砕石・道路材料",
        },
        {
            "name": "蛇紋岩",
            "name_en": "Serpentinite",
            "description": "橄欖岩などが低温高圧の変成を受けた岩石。蛇の皮に似た模様が特徴。",
            "hardness": 3.5,
            "color": "緑・黄緑・黒",
            "uses": "装飾石材・宝飾品（翡翠と混同されることも）",
        },
    ],
}

CATEGORY_LABELS = {
    "igneous": "火成岩",
    "sedimentary": "堆積岩",
    "metamorphic": "変成岩",
}


def get_rocks_by_category(category: str) -> list[dict]:
    """カテゴリ名（英語）で岩石リストを返す。"""
    return ROCKS.get(category, [])


def get_all_rocks() -> list[dict]:
    """全カテゴリの岩石をカテゴリ情報付きで返す。"""
    result = []
    for category, rocks in ROCKS.items():
        for rock in rocks:
            result.append({**rock, "category": category})
    return result


def search_rocks(query: str) -> list[dict]:
    """岩石名・説明文で検索する。"""
    query = query.lower()
    result = []
    for category, rocks in ROCKS.items():
        for rock in rocks:
            if (
                query in rock["name"].lower()
                or query in rock["name_en"].lower()
                or query in rock["description"].lower()
            ):
                result.append({**rock, "category": category})
    return result
