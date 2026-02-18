"""岩石分類データモジュール"""

ROCKS = {
    "igneous": [
        {
            "name": "花崗岩",
            "name_en": "Granite",
            "name_kana": "グラナイト",
            "description": "石英・長石・黒雲母などからなる深成岩。地殻の大部分を構成する。",
            "description_detail": (
                "花崗岩は、マグマが地下深部でゆっくりと冷却・固結してできた深成岩の代表格です。"
                "石英・カリ長石・斜長石・黒雲母の4鉱物を主体とし、それぞれの結晶が肉眼で識別できる粗粒な組織（等粒状組織）を持ちます。"
                "地球大陸地殻の構成岩石として最も重要であり、日本でも中国地方や近畿・九州に広く分布します。"
                "硬く耐久性に優れるため、古代から石材・墓石・建築基礎に利用されてきました。"
                "その美しい模様は磨くと光沢を放ち、カウンタートップや記念碑にも珍重されます。"
            ),
            "hardness": 6.5,
            "color": "灰白色・ピンク",
            "uses": "建築材・墓石・カウンタートップ",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Granite_Yosemite_P1160483.jpg/480px-Granite_Yosemite_P1160483.jpg",
        },
        {
            "name": "玄武岩",
            "name_en": "Basalt",
            "name_kana": "バサルト",
            "description": "鉄・マグネシウムに富む暗色の火山岩。海洋地殻の主な構成岩石。",
            "description_detail": (
                "玄武岩は、低粘性の玄武岩質マグマが噴出して急冷されることで形成される火山岩です。"
                "鉄・マグネシウムを多く含む斜長石・輝石・かんらん石を主成分とし、暗緑色〜黒色を呈します。"
                "海洋地殻のほぼ全体と、ホットスポット火山（ハワイ・アイスランドなど）の大部分を構成しています。"
                "冷却時に六角柱状に割れる「柱状節理」を形成することがあり、壮観な景観を作り出します。"
                "月の海（暗い平原）も玄武岩質の溶岩流で形成されており、地球外でも最も普遍的な岩石の一つです。"
            ),
            "hardness": 6.0,
            "color": "黒・暗灰色",
            "uses": "道路舗装・建築石材・石畳",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Vesicular_basalt.jpg/480px-Vesicular_basalt.jpg",
        },
        {
            "name": "黒曜石",
            "name_en": "Obsidian",
            "name_kana": "オブシディアン",
            "description": "急冷された溶岩が固まったガラス質の火山岩。非常に鋭い断口を持つ。",
            "description_detail": (
                "黒曜石は、珪酸分に富む流紋岩質マグマが急速に冷却され、結晶化する暇なくガラス状に固まった天然ガラスです。"
                "貝殻状断口を持ち、割れた断面は鋭利な刃を形成するため、先史時代から石器・矢じり・ナイフとして世界中で利用されました。"
                "ガラスとしての均質性が高く、現代の外科手術でも黒曜石の刃が使われることがあります。"
                "産地が限られるため先史時代の交易品としても重要であり、産地分析によって古代の交易ルートを解明する手がかりになります。"
                "日本では北海道・長野・神津島などが主要産地で、縄文時代の遺跡から各地に搬出された黒曜石が出土しています。"
            ),
            "hardness": 5.5,
            "color": "黒・暗褐色",
            "uses": "装飾品・外科用メス（先史時代）・宝飾品",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/ObsidianOregon.jpg/480px-ObsidianOregon.jpg",
        },
        {
            "name": "軽石",
            "name_en": "Pumice",
            "name_kana": "ピューミス",
            "description": "無数の気泡を含む多孔質の火山岩。水に浮くほど軽い。",
            "description_detail": (
                "軽石は、ガス成分を多く含む粘性の高い珪長質マグマが爆発的に噴出し、発泡しながら急冷されることで形成される多孔質の火山ガラスです。"
                "内部の無数の気泡（気孔率60〜90%）により、岩石としては異例なほど低密度で水に浮くことで知られます。"
                "2021年の福徳岡ノ場（小笠原）海底火山噴火では大量の軽石が太平洋を漂流し、沖縄・奄美の漁港に漂着して大きな問題になりました。"
                "研磨材として古くから利用され、現代でも洗顔料・角質ケア・ジーンズのウォッシュ加工（ストーンウォッシュ）に使われています。"
                "軽量骨材としてコンクリートや断熱建材に混合されることもあります。"
            ),
            "hardness": 6.0,
            "color": "白・薄灰色",
            "uses": "研磨剤・コンクリート混合材・スキンケア",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Pumice_from_Mono_Craters.jpg/480px-Pumice_from_Mono_Craters.jpg",
        },
        {
            "name": "安山岩",
            "name_en": "Andesite",
            "name_kana": "アンデサイト",
            "description": "中程度のシリカ含有量を持つ火山岩。火山の斜面に多く見られる。",
            "description_detail": (
                "安山岩は、シリカ含有量が52〜63%程度の中間的な組成を持つ火山岩で、沈み込み帯の火山弧（島弧・大陸弧）に特徴的な岩石です。"
                "名称は南米アンデス山脈に由来し、太平洋を取り巻く「環太平洋火山帯」の火山の多くが安山岩質マグマを噴出します。"
                "日本の成層火山（富士山・浅間山・桜島など）も主に安山岩〜デイサイトで構成されています。"
                "斜長石・輝石・角閃石を主成分とし、灰色〜褐灰色の細粒な岩石です。"
                "建築用砕石・路盤材として広く利用されるほか、石臼や砥石にも使われてきました。"
            ),
            "hardness": 6.0,
            "color": "灰色・褐灰色",
            "uses": "建築材・砂利・路盤材",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Andesite_with_white_plagioclase_phenocrysts.jpg/480px-Andesite_with_white_plagioclase_phenocrysts.jpg",
        },
        {
            "name": "流紋岩",
            "name_en": "Rhyolite",
            "name_kana": "ライオライト",
            "description": "花崗岩と同じ成分を持つ火山岩。流れ模様（流理構造）が特徴。",
            "description_detail": (
                "流紋岩は、花崗岩と同じ化学組成（シリカ70%以上）を持つ火山岩で、粘性が極めて高いマグマが噴出・急冷したものです。"
                "高い粘性のため溶岩流は短距離しか流れず、ドーム状の溶岩円頂丘（溶岩ドーム）を形成することが多いです。"
                "その名の通り、溶岩が流動した際の縞模様（流理構造）が観察され、白・ピンク・赤・灰色など様々な色調を示します。"
                "超高温（900℃前後）のガスを多量に含む場合は爆発的な噴火（プリニー式噴火）を引き起こし、広大な火砕流堆積物を残します。"
                "装飾石材としての利用のほか、細かく砕いた流紋岩質凝灰岩は古くから建築材（大谷石など）として使われてきました。"
            ),
            "hardness": 6.5,
            "color": "ピンク・赤・灰色",
            "uses": "装飾石材・研磨材",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Rhyolite.jpg/480px-Rhyolite.jpg",
        },
    ],
    "sedimentary": [
        {
            "name": "砂岩",
            "name_en": "Sandstone",
            "name_kana": "サンドストーン",
            "description": "砂粒が堆積・固結した岩石。粒の大きさが0.06〜2mmの岩石。",
            "description_detail": (
                "砂岩は、砂粒（主に石英・長石）が水流・風によって運搬・堆積し、上位の地層の圧力や鉱物の膠結作用によって固結した堆積岩です。"
                "粒径0.06〜2mmの砂が主体であり、粒子間の膠結物（シリカ・炭酸カルシウム・鉄酸化物など）の種類によって色や強度が大きく変わります。"
                "地層として堆積するため、地層の境目に「成層構造」が見られ、河川・海岸・砂漠などの環境で形成されます。"
                "世界各地の壮大な峡谷（アメリカのアンテロープキャニオンなど）は砂岩の侵食によって形成されたものです。"
                "建築石材として非常に普及しており、古代の神殿や中世の大聖堂にも広く用いられてきました。"
            ),
            "hardness": 6.0,
            "color": "黄・赤・茶・灰色",
            "uses": "建築材・舗装材・フィルタリング材",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Navajo_Sandstone.jpg/480px-Navajo_Sandstone.jpg",
        },
        {
            "name": "石灰岩",
            "name_en": "Limestone",
            "name_kana": "ライムストーン",
            "description": "炭酸カルシウムを主成分とする堆積岩。サンゴや貝殻が起源のことが多い。",
            "description_detail": (
                "石灰岩は、炭酸カルシウム（CaCO₃）を50%以上含む堆積岩で、主にサンゴ・貝殻・有孔虫などの生物遺骸が浅海底に堆積して形成されます。"
                "塩酸をかけると二酸化炭素の気泡を出すことで容易に識別でき、これが野外での簡易判定に使われます。"
                "雨水（弱酸性）や地下水に溶けやすく、長年の侵食でカルスト地形（鍾乳洞・石灰岩台地・ドリーネなど）を形成します。"
                "日本最大の鍾乳洞である秋芳洞（山口県）や、石灰岩採掘で有名な秩父・三重・山口などの産地が知られています。"
                "セメントの主原料として現代の建設業を支えるほか、製鉄の溶剤・農業用石灰・化学工業原料として不可欠な岩石です。"
            ),
            "hardness": 3.0,
            "color": "白・灰・黄",
            "uses": "セメント原料・建築材・農業用石灰",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/LimestoneSample.jpg/480px-LimestoneSample.jpg",
        },
        {
            "name": "泥岩",
            "name_en": "Mudstone",
            "name_kana": "マッドストーン",
            "description": "泥が固まった岩石。粒径が0.06mm以下の細粒堆積岩。",
            "description_detail": (
                "泥岩は、粒径0.06mm以下の粘土・シルト粒子が静かな水環境（深海底・湖底・河川氾濫原）に堆積・固結した堆積岩です。"
                "葉状にはがれる性質（葉理）を持つものは特に「頁岩（けつがん／シェール）」と呼ばれます。"
                "有機物を豊富に含む黒色頁岩は石油・天然ガスの根源岩となり、現代の「シェール革命」では採掘対象のガス源岩でもあります。"
                "粘土鉱物が主成分であるため陶器・タイル・レンガの原料として古くから利用され、文明の発展に重要な役割を果たしてきました。"
                "最も地球上に豊富な堆積岩であり、地球の堆積岩全体の約60%を占めるとされます。"
            ),
            "hardness": 2.5,
            "color": "灰・黒・茶",
            "uses": "陶芸原料・レンガ材料・陶器",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Mudstone_%28lithified_mudstone%29.jpg/480px-Mudstone_%28lithified_mudstone%29.jpg",
        },
        {
            "name": "礫岩",
            "name_en": "Conglomerate",
            "name_kana": "コングロメリット",
            "description": "礫（2mm以上の粒）が泥や砂で固められた堆積岩。",
            "description_detail": (
                "礫岩は、粒径2mm以上の礫が砂や泥とともに固結した堆積岩で、高エネルギーの堆積環境（河川上流・扇状地・海岸）に形成されます。"
                "礫の形状が丸みを帯びているほど長距離を輸送された証拠であり、産地や輸送距離の推定に役立ちます。"
                "日本では関東平野北部の荒川流域や、各地の河川段丘などに分布し、古代の河川環境を復元する手がかりになります。"
                "礫の岩石の種類（岩相）を調べることで、その地域の過去の地質環境や侵食の歴史を読み解くことができます。"
                "建築用の骨材として利用されるほか、庭石としても活用されます。"
            ),
            "hardness": 6.0,
            "color": "混合色",
            "uses": "建築骨材・装飾石材",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Conglomerate_8577.jpg/480px-Conglomerate_8577.jpg",
        },
        {
            "name": "チャート",
            "name_en": "Chert",
            "name_kana": "チャート",
            "description": "放散虫などの珪酸質生物の遺骸が堆積した緻密な岩石。",
            "description_detail": (
                "チャートは、珪酸（SiO₂）を骨格に持つ放散虫・海綿・珪藻などの微小生物遺骸が深海底に堆積し、固結した岩石です。"
                "炭酸カルシウムが溶解する深度（炭酸塩補償深度）以深の深海でも溶けずに堆積できる珪酸質の岩石です。"
                "非常に緻密で硬く（モース硬度7）、石器時代の打製石器（火打石）として最も重要な材料の一つでした。"
                "ナイフのような鋭い断口を生じるため、黒曜石と並んで世界各地の先史文化で広く利用されています。"
                "赤色チャートは鉄酸化物を含むもので、日本の丹波・美濃などの付加体地層に典型的に見られます。"
            ),
            "hardness": 7.0,
            "color": "赤・緑・灰・黒",
            "uses": "火打石（先史時代）・研磨材",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Jasper_chert.jpg/480px-Jasper_chert.jpg",
        },
        {
            "name": "岩塩",
            "name_en": "Rock Salt",
            "name_kana": "ロックソルト",
            "description": "塩化ナトリウムを主成分とする蒸発岩。海水の蒸発により形成される。",
            "description_detail": (
                "岩塩は、閉鎖的な内海や干上がった湖に海水・塩水が流れ込み、蒸発・濃縮を繰り返すことでハライト（塩化ナトリウム）が晶出・堆積した蒸発岩です。"
                "ポーランドのヴィエリチカ岩塩坑やパキスタンのヒマラヤ岩塩（ピンク岩塩）が世界的に有名で、特にヒマラヤ岩塩は微量の鉄分による美しいピンク色で知られます。"
                "人類の歴史において塩は最重要の食料保存剤・調味料であり、岩塩の産地は経済的・政治的に極めて重要でした。"
                "密度が小さく可塑性があるため、地下深部では「ダイアピル」と呼ばれるドーム状の貫入構造を形成し、石油・天然ガスのトラップを作ることがあります。"
                "現代では化学工業（ソーダ工業）の基幹原料であり、融雪剤・動物用ミネラル補給としても大量に利用されます。"
            ),
            "hardness": 2.5,
            "color": "白・透明・ピンク",
            "uses": "食塩・化学工業原料・道路の融雪剤",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Halite_crystals.jpg/480px-Halite_crystals.jpg",
        },
    ],
    "metamorphic": [
        {
            "name": "大理石",
            "name_en": "Marble",
            "name_kana": "マーブル",
            "description": "石灰岩が熱や圧力で変成した岩石。美しい模様と光沢が特徴。",
            "description_detail": (
                "大理石は、石灰岩（または苦灰岩）が熱変成・接触変成作用を受け、方解石が再結晶化することで形成される変成岩です。"
                "変成過程で不純物が再配列・再結晶し、美しい縞模様・雲状模様を生み出します。"
                "古代ギリシャのパルテノン神殿・ローマの建築物・ミケランジェロの彫刻（ダビデ像など）に使用された最も著名な芸術・建築用石材の一つです。"
                "中国・雲南省の大理市が産地として有名であったため「大理石」の名が付きましたが、現在はイタリア（カッラーラ）・スペイン・トルコなどが主要産地です。"
                "研磨すると美しい光沢が出るため、床材・カウンタートップ・彫刻・インテリアとして今日も世界中で愛用されています。"
            ),
            "hardness": 3.0,
            "color": "白・灰・黒・色多様",
            "uses": "彫刻・建築内装・床材・カウンタートップ",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Marble_sample.jpg/480px-Marble_sample.jpg",
        },
        {
            "name": "片岩",
            "name_en": "Schist",
            "name_kana": "シスト",
            "description": "強い変成作用を受け、雲母などの板状鉱物が平行に並んだ岩石。",
            "description_detail": (
                "片岩は、泥岩・砂岩などが中程度〜高度の変成作用を受け、雲母（白雲母・黒雲母）・緑泥石などの板状鉱物が圧力に直交する方向に揃って並んだ岩石です。"
                "葉状に薄くはがれる「片理（へんり）」と呼ばれる構造が最大の特徴で、これにより板状に割れます。"
                "含まれる鉱物によって「緑色片岩」「青色片岩」「石英片岩」など多くの種類があり、変成温度・圧力条件の違いを反映しています。"
                "青色片岩（グローコファン片岩）は低温高圧の変成環境（沈み込み帯）で形成され、プレートテクトニクスの証拠として地質学的に重要です。"
                "銀色の光沢を持つ雲母を多量に含む片岩は装飾石材や板材として利用され、屋根材・石塀にも用いられます。"
            ),
            "hardness": 5.0,
            "color": "銀灰色・緑・茶",
            "uses": "装飾石材・建築外装",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Schist.jpg/480px-Schist.jpg",
        },
        {
            "name": "片麻岩",
            "name_en": "Gneiss",
            "name_kana": "ナイス",
            "description": "高温高圧の変成作用を受けた岩石。縞状の模様が特徴。",
            "description_detail": (
                "片麻岩は、高温高圧の変成作用（広域変成作用）を受けた岩石で、明色帯（石英・長石）と暗色帯（雲母・角閃石）が交互に縞状に並ぶ「片麻状構造」を持ちます。"
                "花崗岩や泥岩が原岩となることが多く、原岩の種類によって「花崗岩質片麻岩」「泥質片麻岩」などに分類されます。"
                "地球最古の岩石のいくつかは片麻岩であり、カナダのアカスタ片麻岩（約40億年前）は地球上で最も古い岩石として知られます。"
                "大陸地殻の深部を構成する岩石として重要で、山地の隆起・侵食によって地表に露出します。"
                "硬く耐久性が高いため建築石材・舗装材として利用されており、磨いた表面の縞模様が装飾的な美しさを持ちます。"
            ),
            "hardness": 6.5,
            "color": "灰白色・縞模様",
            "uses": "建築石材・舗装材",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Gneiss_in_hand.jpg/480px-Gneiss_in_hand.jpg",
        },
        {
            "name": "石英岩",
            "name_en": "Quartzite",
            "name_kana": "クォーツァイト",
            "description": "砂岩が変成してできた非常に硬い岩石。石英が主成分。",
            "description_detail": (
                "石英岩は、石英を主体とする砂岩が変成作用を受け、石英粒子が再結晶・融合して隙間なく緻密に結合した変成岩です。"
                "モース硬度7と非常に硬く、化学的にも安定しているため風化・侵食に対する抵抗が大きく、山頂部や山稜に残留しやすいです。"
                "純粋な石英岩は白色〜半透明で、鉄やマンガンなどの不純物によってピンク・赤・紫・緑などの様々な色調を示します。"
                "砂岩と異なり粒子の境界が消滅しているため、割れても粒子の境界ではなく粒子を横切って破壊されます。"
                "耐火材・研磨材・建築装飾材のほか、高純度のものは電子産業用珪素（シリコン）の原料として重要です。"
            ),
            "hardness": 7.0,
            "color": "白・灰・ピンク",
            "uses": "耐火材・研磨材・装飾石材",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Quartzite_in_a_hand_sample.jpg/480px-Quartzite_in_a_hand_sample.jpg",
        },
        {
            "name": "ホルンフェルス",
            "name_en": "Hornfels",
            "name_kana": "ホルンフェルス",
            "description": "マグマの熱によって接触変成を受けた緻密で硬い岩石。",
            "description_detail": (
                "ホルンフェルスは、マグマが貫入した際の熱によって周囲の岩石が「焼かれて」変成された接触変成岩です。"
                "「ホルンフェルス」はドイツ語で「角岩」を意味し、緻密で硬く角状に割れる性質から名付けられました。"
                "マグマの貫入体（貫入岩体）の周囲に形成される「コンタクトオーレオール（接触変成帯）」の代表的な岩石です。"
                "原岩の種類（泥岩・砂岩・石灰岩）によって生成される鉱物が異なり、andalusite・cordierite・wollastoniteなどの特徴的な変成鉱物を含みます。"
                "硬くて丈夫なため砕石・道路材料として利用されるほか、地質学的には花崗岩類の貫入年代を推定する手がかりになります。"
            ),
            "hardness": 6.5,
            "color": "黒・暗灰・茶",
            "uses": "砕石・道路材料",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Hornfels_in_hand_sample.jpg/480px-Hornfels_in_hand_sample.jpg",
        },
        {
            "name": "蛇紋岩",
            "name_en": "Serpentinite",
            "name_kana": "サーペンティナイト",
            "description": "橄欖岩などが低温高圧の変成を受けた岩石。蛇の皮に似た模様が特徴。",
            "description_detail": (
                "蛇紋岩は、かんらん岩（ペリドタイト）などのマントル由来の岩石が、水を多く含む低温高圧の環境で変成（蛇紋岩化）することで形成されます。"
                "主成分の蛇紋石鉱物群（クリソタイル・リザーダイト・アンチゴライト）により、緑〜黄緑の基調に暗色の網状模様（蛇の皮に似た模様）を呈します。"
                "オフィオライト（海洋地殻・マントルの断片）として陸上に露出することが多く、プレートテクトニクスの証拠として地質学的に重要です。"
                "蛇紋岩土壌は重金属（ニッケル・クロム）が多く栄養分が少ないため、特殊な植物群落（蛇紋岩植生）が発達します。"
                "磨くと独特の光沢と模様が美しく、装飾石材・インテリア素材として珍重され、古くからフォールス翡翠（ニューヒスイ）として宝飾品にも使われてきました。"
            ),
            "hardness": 3.5,
            "color": "緑・黄緑・黒",
            "uses": "装飾石材・宝飾品",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Serpentinite.jpg/480px-Serpentinite.jpg",
        },
    ],
}

CATEGORY_LABELS = {
    "igneous": "火成岩",
    "sedimentary": "堆積岩",
    "metamorphic": "変成岩",
}


def get_rocks_by_category(category: str) -> list[dict]:
    return ROCKS.get(category, [])


def get_all_rocks() -> list[dict]:
    result = []
    for category, rocks in ROCKS.items():
        for rock in rocks:
            result.append({**rock, "category": category})
    return result


def search_rocks(query: str) -> list[dict]:
    query_lower = query.lower()
    result = []
    for category, rocks in ROCKS.items():
        for rock in rocks:
            if (
                query_lower in rock["name"].lower()
                or query_lower in rock["name_en"].lower()
                or query_lower in rock["name_kana"].lower()
                or query_lower in rock["description"].lower()
                or query_lower in rock["description_detail"].lower()
            ):
                result.append({**rock, "category": category})
    return result
