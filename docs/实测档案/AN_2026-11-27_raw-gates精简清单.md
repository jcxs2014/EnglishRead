# raw-gates 精简清单（2026-11-27）

> 用户指令：「rawgates 可能还是要清理，有用的内容可以重新整理」。
> 原则：**删可再生的中间件，留人写的结论与不易重建的事实**。

## 一、删了什么 / 留了什么

| 文件名 | 性质 | 处置 | 数量 |
|---|---|---|---|
| `2-machine.json` / `.txt` / `.err` | 机器层原始输出，**重跑即得** | 删 | 3,924 |
| `3-diff.md` | 素读与 md 的逐条差异草稿，**由 1-suread + md 生成** | 删 | 3,827 |
| `t1-candidates.txt` | 断言预筛候选，`assertion_scan.py` **重跑即得** | 删 | 99 |
| `ev.txt` / `.DS_Store` | 临时证据与系统垃圾 | 删 | 98 |
| **`4-verdict.md`** | **审查员的判定表**（阻断/提示/已核实为正确）——人写的，重做要重审 | **留** | 3,832 |
| **`1-suread.json`** | **R1 素读事实 + 锚点**——重建要重读原文 | **留** | 3,800 |
| `t1-verdict.md` / `4-correspondence.md` / `1-facts.txt` | 判定与素读的其它落点 | 留 | 269 |

**合计删除 7,948 个文件 / 47.0 MB**（原 16,048 / 73 MB → 8,100 / 26 MB）。

## 二、被引用路径不受影响

删的都是「中间件」，文档与台账引用的是 `4-verdict.md`、`1-suread.json`、`2026-*-*.md` 这类**保留件**
（2026-11-27 复核：39 本书的 review 路径被 95 处引用，无一处指向本次删除的六类文件）。

## 三、逐书明细（删 / 留 md / 留 json）

| 书 | 删 | 留 md | 留 json |
|---|---|---|---|
| `victorious-by-v-e-schwab` | 253 | 255 | 252 |
| `night-calls-by-joe-hart` | 209 | 209 | 208 |
| `afternoon-delight-by-dani-collins` | 175 | 117 | 116 |
| `unspeakable-things-by-elizabeth-hand` | 167 | 167 | 166 |
| `life-out-of-order-by-audrey-niffenegger` | 164 | 148 | 144 |
| `public-access-afterworld-by-jane-schoenbrun` | 157 | 157 | 156 |
| `knife-for-hire-by-sage-relleanne` | 143 | 143 | 142 |
| `the-pickle-factory-by-sam-r-oyken` | 141 | 141 | 140 |
| `pucking-ridiculous-by-rebecca-chase` | 139 | 139 | 138 |
| `the-missing-wives-by-morgan-greene` | 131 | 131 | 130 |
| `the-house-on-ember-row-by-bill-keenan` | 130 | 87 | 86 |
| `harbour-of-hungry-ghosts-by-eliza-chan` | 126 | 128 | 124 |
| `the-sixth-faction-by-veronica-roth` | 125 | 132 | 124 |
| `a-fatal-legacy-by-charlotte-vassell` | 124 | 176 | 118 |
| `the-house-built-on-alligator-bones-by-sophia-huneycutt` | 119 | 101 | 98 |
| `a-snake-among-swans-by-hannah-kaner` | 117 | 117 | 116 |
| `bloodgrove-by-elisabeth-g-mark` | 117 | 117 | 116 |
| `the-splintered-sun-by-tad-williams` | 113 | 113 | 112 |
| `this-shattered-tempest-by-thea-guanzon` | 113 | 113 | 112 |
| `your-beloved-remains-by-quinn-connor` | 113 | 113 | 112 |
| `chasing-kaylee-kringle-by-codi-hall` | 109 | 109 | 108 |
| `all-the-way-home-by-alex-ritany` | 107 | 108 | 106 |
| `love-you-to-death-by-jenna-levine` | 106 | 72 | 70 |
| `merciless-silence-by-ines-johnson` | 103 | 103 | 102 |
| `the-dawn-throne-by-tara-sim` | 102 | 103 | 101 |
| `all-in-her-head-by-paula-johnston` | 101 | 101 | 100 |
| `carousel-by-beth-best` | 101 | 101 | 101 |
| `i-m-not-scared-omnibus-by-jaye-pratt` | 101 | 101 | 100 |
| `a-wall-is-also-a-road-by-annalee-newitz` | 97 | 97 | 96 |
| `blood-and-birthright-by-amelia-spencer` | 95 | 95 | 94 |
| `the-house-on-otley-road-by-rosa-silverman` | 90 | 90 | 90 |
| `monstera-by-delilah-s-dawson` | 88 | 60 | 58 |
| `the-labyrinthine-rule-of-lavina-theron-by-jennifer-prestage` | 87 | 87 | 86 |
| `revenge-reads-better-by-ivy-fox` | 85 | 85 | 95 |
| `sleepers-in-the-snow-by-joanne-harris` | 83 | 83 | 82 |
| `bodies-of-magic-by-freya-marske` | 81 | 81 | 80 |
| `lifeguard-by-janet-fash` | 81 | 43 | 40 |
| `our-wives-under-the-sea-by-julia-armfield` | 81 | 81 | 80 |
| `the-last-syphon-by-t-j-maguire` | 81 | 81 | 80 |
| `wrong-cabin-right-time-by-c-hallman` | 79 | 79 | 78 |
| `last-looks-by-cate-holahan` | 78 | 77 | 78 |
| `a-hart-to-call-home-by-s-sidney` | 77 | 77 | 76 |
| `foolsilver-by-meg-xuemei-x` | 77 | 77 | 76 |
| `florescentia-by-i-v-ophelia` | 75 | 75 | 74 |
| `maggie-and-arthur-s-magic-moment-by-leslie-rene` | 75 | 76 | 74 |
| `magical-murmur-by-d-k-bolton` | 73 | 73 | 72 |
| `waiting-on-a-friend-by-natalie-adler` | 73 | 73 | 72 |
| `sweet-spot-by-kemper-donovan` | 72 | 77 | 71 |
| `a-lie-so-pretty-and-poisonous-by-leah-bronwyn` | 71 | 71 | 70 |
| `a-midsummer-party-by-antoni-jach` | 71 | 71 | 70 |
| `backwoods-banshee-by-david-r-slayton` | 71 | 71 | 70 |
| `embarkare-by-aubrey-nymphaea` | 67 | 68 | 66 |
| `her-vampire-his-ruin-by-bea-paige` | 67 | 67 | 66 |
| `odette-rising-by-julianne-edwards` | 67 | 67 | 66 |
| `out-of-her-genre-by-yna-martinez` | 65 | 65 | 64 |
| `the-art-lovers-by-fiona-mcintosh` | 65 | 65 | 64 |
| `homesick-by-rhiannon-grist` | 63 | 114 | 12 |
| `pumpkin-spice-promises-by-taylor-jade` | 63 | 63 | 62 |
| `cross-the-line-by-jenna-hartley` | 61 | 61 | 60 |
| `in-your-heart-a-devil-by-vanessa-santos` | 61 | 42 | 40 |
| `pan-by-francesco-dimitri` | 61 | 62 | 60 |
| `so-bad-it-s-good-by-mike-rampton` | 61 | 61 | 60 |
| `imprisoned-with-the-vampire-king-by-lola-glass` | 59 | 59 | 58 |
| `oubliette-by-l-v-russell` | 59 | 59 | 58 |
| `quaint-folk-by-bitter-karella` | 59 | 59 | 58 |
| `i-know-you-by-ranee-s-clark` | 56 | 57 | 54 |
| `a-scholar-s-guide-to-demonology-other-dark-arts-by-genevieve-cogman` | 55 | 56 | 54 |
| `before-the-encore-by-emily-wright` | 55 | 55 | 54 |
| `fated-to-the-wicked-king-by-s-l-breaker` | 55 | 55 | 54 |
| `laced-in-longing-by-dakota-monroe` | 55 | 55 | 54 |
| `paradise-by-claudia-gabel` | 55 | 55 | 54 |
| `the-hexing-miss-helena-by-darcy-mcguire` | 54 | 57 | 54 |
| `forest-of-carnage-by-candace-robinson` | 53 | 53 | 52 |
| `lessons-in-love-by-mimi-tomkins` | 53 | 53 | 52 |
| `ask-me-to-stay-by-mackenzie-osborn` | 51 | 51 | 50 |
| `the-christmas-we-built-by-kelly-collins` | 51 | 51 | 50 |
| `the-thrice-bound-fool-by-christopher-buehlman` | 48 | 87 | 48 |
| `the-corpse-collectors-by-caitlin-regencia` | 45 | 46 | 44 |
| `motherclown-by-harriet-alida-lye` | 43 | 44 | 42 |
| `the-girl-in-blue-by-doreen-carvajal` | 43 | 43 | 42 |
| `we-will-see-you-bleed-by-ron-currie` | 43 | 43 | 42 |
| `anchored-to-the-storm-by-india-r-adams` | 41 | 41 | 40 |
| `hart-by-marina-pirlimpou` | 41 | 41 | 40 |
| `off-the-reservation-by-stephen-graham-jones` | 41 | 41 | 40 |
| `the-horse-and-i-by-inc-genki-kawamura` | 41 | 41 | 40 |
| `monstrous-bitch-by-eleanor-johnson` | 40 | 28 | 26 |
| `chosen-by-monsters-by-texa-volt` | 39 | 39 | 38 |
| `forged-flight-by-c-l-blossom` | 39 | 39 | 39 |
| `the-art-of-inquiry-by-andrew-taggart` | 39 | 39 | 38 |
| `the-scarlet-ball-by-nghi-vo` | 39 | 39 | 38 |
| `what-feeds-below-by-tatiana-schlote-bonne` | 39 | 39 | 38 |
| `don-t-leave-her-alone-by-desiree-de-fez` | 38 | 38 | 36 |
| `red-ants-by-kimberly-blaeser` | 35 | 35 | 34 |
| `the-enchanted-cherry-blossom-inn-by-ella-cook` | 31 | 31 | 30 |
| `the-intrigue-by-silvia-moreno-garcia` | 26 | 3 | 48 |
| `habits-of-the-sea-by-shea-ernshaw` | 24 | 40 | 20 |
| `home-for-the-holidays-by-sarah-morgan` | 23 | 23 | 22 |
| `the-king-s-captive-by-v-blackwell` | 23 | 23 | 22 |
| `our-later-years-by-lucy-brazier` | 21 | 21 | 20 |
| `artificial-intimacy-by-sherry-turkle` | 19 | 19 | 18 |
| `raising-ai-by-chirag-shah` | 19 | 19 | 18 |
| `an-eye-for-property-by-tania-fordwalker` | 15 | 15 | 14 |
| `a-labyrinth-of-honeybees-by-fawcett-heather` | 13 | 16 | 12 |
| `john-grebble-is-gone-by-peter-james` | 11 | 12 | 10 |
| `fitcher-s-bird-by-a-g-slatter` | 5 | 8 | 2 |
| `fabulous-bodies-by-chuck-tingle` | 1 | 1 | 4 |
| `the-dues-don-ts-of-magic-by-delemhach` | 1 | 1 | 3 |
| `the-last-bride-by-lexy-night` | 1 | 1 | 0 |
| `the-mysterious-affair-of-judith-potts-by-robert-thorogood` | 1 | 2 | 0 |
| `the-neighbors-are-watching-by-aggie-blum-thompson` | 1 | 1 | 0 |
| `the-secret-thread-by-eve-chase` | 1 | 1 | 0 |
