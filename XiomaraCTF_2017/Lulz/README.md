# Lulz

Category: Web Exploitation

Point: 50



## Question

Heavy sarcasm awaits. Are you a person who finds opportunities even in trolls? Well, let's find out.

[http://139.59.61.220:23456](http://139.59.61.220:23456)


## Answer

#### **THE クソ問**

上記リンクのページ（ページAとする）に移動すると，まずアラートが表示されプロンプト内のボタンをクリックすると，
違うページにリダイレクトされる．
リダイレクト後のページ（ページBとする）は，不愉快なトロールの画像をランダムで表示した後，
一定時間が経過したらページをリロードするといったものだった．

問題文の内容から，**トロールの画像のなかにフラグが書かれた画像があるのかなあ**と推定したため，
ページBで読み込んでいる[`main.js`](./main.js)をダウンロードした後，そのスクリプトを以下のように書き換えた．

```js
n = 0
b = new Array()
b[n++]="9TxGepNycwU/UqfHResYxyI/AAAAAAAAF10/23OGwKfLsOs/s1600/DAN-HOWELL-licking-pickle-dance-crew-dancing-banana.gif"
b[n++]="wj7r_LnIDSw/UqANWoGJ10I/AAAAAAAAFTk/2onqoUzAwo8/s1600/1001-morphing-merging-trolls-troll-faces-trollface.gif"
b[n++]="JpCMmirInBo/UqANVhoUByI/AAAAAAAAFSs/foC8J3t4QK8/s1600/3D-dancing-baby-cha-cha-hooked-on-feeling-ally-meme-mcbeal.gif"
b[n++]="-_QXAMNvVJ4/UqANV3Ni-uI/AAAAAAAAFS0/Z-XiKnjc_Ug/s1600/3d-relief-mapping-earth-map-planet-mountains-hills-trollface.gif"
b[n++]="MgDIhKCsums/UqANXcoGpQI/AAAAAAAAFTM/4gN58QsjlFA/s1600/3d-trollface-troll-face-flaming-fire-mad-hot-headed.gif"
b[n++]="EriSYNp-jpk/UqANX1buIRI/AAAAAAAAFTY/VZEenD-gE2Q/s1600/3d-trollface-troll-face-weird-stalactite-stalagmite-cave-.gif"
b[n++]="GWLRpesX4lo/UqANYoI1UYI/AAAAAAAAFTg/qoDCjcBeuJA/s1600/Chris-Pirillo-Meta-Kevin-Staff-troll-face-nerd-geek.gif"
b[n++]="Thrz93gr0D0/UqANWupIZYI/AAAAAAAAFS8/v7k1H4XPx2Q/s1600/3d-trollface-nodding-ok-yes-agree-troll-face.gif"
b[n++]="8FU2EoGeNz4/UqANXNCnCrI/AAAAAAAAFTI/SVnSMJ-fhaw/s1600/3d-trollface-troll-face-experimental-art-trollart.gif"
b[n++]="mFJdJN62DHk/UqANY3DmQBI/AAAAAAAAFTs/K6KpSc5R9lA/s1600/Chris-Pirillo_first-time-nerd-sees-boobs-boobies-geek.gif"
b[n++]="ArMjdj1ikZg/UqANZjNvAQI/AAAAAAAAFT0/9XeWKX_VqUw/s1600/Chris-Pirillo_live-gay-christmas-chat-cheer.gif"
b[n++]="5CD0Ko2gcfo/UqANaDxICrI/AAAAAAAAFT8/zaG_kJRNLdA/s1600/Chris_Pirillo_loves_trolls_like_crazy_geek_computer_nerd.gif"
b[n++]="XPY073HWOCQ/UqANatBkLtI/AAAAAAAAFUE/nPUWpes38gs/s1600/Colbert_Nation_Report_Comedy_Central_troll_face_trollface_funny_dancing.gif"
b[n++]="bocmbrZz4Kk/UqANbQ5i_AI/AAAAAAAAFUQ/zfBPMKLJM7w/s1600/Emma-Watson-troll-face-trollface.gif"
b[n++]="zfCOOEEnOCc/UqANbmU25bI/AAAAAAAAFUU/6Jo0-82Igm4/s1600/GUMBY-kids-tv-show-high-school-troll-face-trollface.gif"
b[n++]="EEr-N0vWlLE/UqANbs2JDJI/AAAAAAAAFUY/MOw7YfCDGNw/s1600/Hypnotoad-Trollface-troll-face-remix-futurama-Animated.gif"
b[n++]="Uz3JROkQneY/UqANdgkjMhI/AAAAAAAAFVA/RTTd6XNzK7A/s1600/Joker-Clapping2.gif"
b[n++]="23iBpACxIQc/UqANdFDWEPI/AAAAAAAAFUk/C0O9NmIjwnc/s1600/Leonardo-da-Vinci-The-Vitruvian-Man-troll-face-masterbate-jerk-off.gif"
b[n++]="be5-ib453p0/UqANdnDI3QI/AAAAAAAAFUw/7HHetuzth1o/s1600/OMG-WTF-troll-face-thats-too-fugly-to-look-at.gif"
b[n++]="0x7UnJKxhxQ/UqANeP07adI/AAAAAAAAFU8/Ve7EVnwyoCo/s1600/ScrollTroll-5sets-scrolling-infinite-troll-faces-trollface.gif"
b[n++]="owGPxaLBg1E/UqANekuUmEI/AAAAAAAAFVE/PFlA4NhMh7Y/s1600/ScrollTroll-scrolling-infinite-troll-faces-trollface.gif"
b[n++]="_f4m9MedUnA/UqANenMDXWI/AAAAAAAAFVI/Vg1NISEBXEI/s1600/SuperTroll-flying-through-clouds-trollface-troll-face.gif"
b[n++]="--WiLFefjHw/UqANe5WP0tI/AAAAAAAAFVY/0Mir2DqHERw/s1600/TROLL-FACE-OPTICAL-ILLUSION-TUNNEL-EFFECT.gif"
b[n++]="jEPGYv8VATo/UqANf4hlD4I/AAAAAAAAFVc/LxxN08Tq0M8/s1600/TROLL-FACES-OPTICAL-ILLUSION-TUNNEL-EFFECT.gif"
b[n++]="ip3AbhLJOdY/UqANf_4QGZI/AAAAAAAAFVk/n5x55qEGwBw/s1600/TROLL-TRAIN-FARE-TICKETS-TO-RIDE-trollface-rolling.gif"
b[n++]="NcDrEGPkLBo/UqANg90MZWI/AAAAAAAAFV0/oihrh5T7sP4/s1600/Try_This_At_Home_Jumping_Over_Car_Troll_Safety_Tips.gif"
b[n++]="GSbiEVDE6CY/UqANg9mpAhI/AAAAAAAAFWE/Vcq2iuCZP98/s1600/WTF-OMG-troll-face-trollface.gif"
b[n++]="mM-tcDWDqYY/UqANheStY-I/AAAAAAAAFWA/2PnfMlfDItg/s1600/american-freedom-flag-troll-face-dancing-like-a-sir.gif"
b[n++]="Layt16itJZw/UqANhj_AuTI/AAAAAAAAFV8/RFVi8Yfgqhc/s1600/animated-gif-troll-face-bugging-cat-wtf-trollface.gif"
b[n++]="y3U3F2ppP-0/UqANh8ZzehI/AAAAAAAAFWI/i8KVhvOoaxQ/s1600/animated-meme-troll-face-animated.gif"
b[n++]="fNKXbXaFd9c/UqANiW8LwzI/AAAAAAAAFWY/X12rz8eaUyU/s1600/anorexic-ethiopian-troll-face-trollface-excercising-excersizing-excersising.gif"
b[n++]="oGLGt2nvnO4/UqANjWA0BzI/AAAAAAAAFWs/sO5G-tdug0s/s1600/atheist-atheism-troll-jesus-christ-dinosaur-creation-god.gif"
b[n++]="XTHUl7s6rjc/UqANjfCLp4I/AAAAAAAAFWk/qCDjR6Pn8ls/s1600/atomic-bomb-blast-explosion-trollface-troll-face.gif"
b[n++]="kgVBzByEKwk/UqANkHkYbDI/AAAAAAAAFXM/lDBAWpCBd5c/s1600/avatar-troll.gif"
b[n++]="sgXf5P-HCEA/UqANkBw805I/AAAAAAAAFWo/JCT2-l0ImZo/s1600/bart-simpson-male-stripper-older-man-trollface.gif"
b[n++]="h9UWsmea9WA/UqANkXcPaMI/AAAAAAAAFWw/oMoJbuSP9Ik/s1600/benhams_disc_optical_illusion_see_colors.gif"
b[n++]="-R7TcsDCmos/UqANlUzda_I/AAAAAAAAFXI/k-YVwqCqPNU/s1600/beware-trolls-are-trolling-here-trollface-warning.gif"
b[n++]="Cnyv6fi1XUQ/UqANlfOexvI/AAAAAAAAFXE/1Kf4GNufVIU/s1600/blah-blah-blah-trolling-annoying-animated.gif"
b[n++]="9vaK0EdW2pA/UqANmLKR7dI/AAAAAAAAFXQ/v7rYtEAlEt4/s1600/bouncing_boobs_breasts_tits_troll_faces_trollface.gif"
b[n++]="bimwLolb8QA/UqANmHCcjbI/AAAAAAAAFXg/DkQbFn8oy2Y/s1600/cant-troll-anonymous-hackers-group-trollface-face.gif"
b[n++]="u3kX4SwneMQ/UqANm351X-I/AAAAAAAAFXs/8yv_9T94TJQ/s1600/carlton-banks-fresh-prince-bel-air-trollface-troll-face.gif"
b[n++]="xpU1UgHcze4/UqANmyRokwI/AAAAAAAAFXo/TxUddG4D4_8/s1600/cattroll-trolcats-trollcats-troll-cat-caturday-face-head.gif"
b[n++]="zlMwa4DWrb4/UqANn3w5ZhI/AAAAAAAAFX8/iGWk68ienN0/s1600/caturday-lol-cat-troll-dancing-WTF-what-the-fuck.gif"
b[n++]="eSnEAn8QCNc/UqANnwClBRI/AAAAAAAAFX0/5g1frByudxE/s1600/chris-farley-saturday-night-live-tv-troll-face-trollface.gif"
b[n++]="wXOraRKU3CM/UqANoqvr1GI/AAAAAAAAFYM/O0PuE72y-sA/s1600/christening-pope-peeing-on-holy-wall-troll-face-trollface.gif"
b[n++]="afipYBu8QM0/UqANoqJKV-I/AAAAAAAAFYI/oOfGFvxsHb4/s1600/clapping-crowd-live-show-clap-hands-troll-face-trollface.gif"
b[n++]="HXe8aOeNkXE/UqANpYqAVrI/AAAAAAAAFYU/4465vpD_d_c/s1600/clapping-gay-homosexual-queer-gblt-troll-face-trollface.gif"
b[n++]="_oixvukyFOM/UqANp48OChI/AAAAAAAAFYc/260rj-xncQ4/s1600/clapping-only-one-audience-clap-hands-troll-face-trollface.gif"
b[n++]="gXEnMiHUpyw/UqANqSg2rjI/AAAAAAAAFYk/2Q2VICNftE4/s1600/creepy-troll-face-weird-strange-unusual.gif"
b[n++]="zSKMW3yg7-0/UqANqw1yiYI/AAAAAAAAFY4/JrBiJTY53pQ/s1600/cunt-troll-control-freak-bitch-psycho-feminist-cat-lovers-pussy-face.gif"
b[n++]="FB-dbs8D1QA/UqANq5gWJWI/AAAAAAAAFYs/chT-57yrTzg/s1600/dance-party-weird-odd-dancing-fool-trollface-troll-face.gif"
b[n++]="hTFeRwz1NaQ/UqANrlPFghI/AAAAAAAAFY8/BVk8dJXjfCg/s1600/dancing-mr-pickle-troll-banana-meme-characters.gif"
b[n++]="R1abvHgMCs0/UqANsGpXP6I/AAAAAAAAFZA/xP9UcEqRA4o/s1600/dancing-pickle-troll-face-dance-party-meme-wars.gif"
b[n++]="wl-Q8Uve8pc/UqANtErlZZI/AAAAAAAAFZk/P1431_ov5FU/s1600/dancing-pumpkinparty3.gif"
b[n++]="MjETFEMkI7Q/UqANtCM31tI/AAAAAAAAFZY/uwMk_dX4FxU/s1600/dancing-troll-face-trollface-trolls-dance.gif"
b[n++]="Y6kug3W5vys/UqANs2vmwAI/AAAAAAAAFZM/Ura1ariaF_M/s1600/dnr-did-not-read-troll-face-shaking-head.gif"
b[n++]="Wd6kgVXVCQ8/UqANtg2WkWI/AAAAAAAAFZg/zI3zwi_Q8gM/s1600/drunk-laughing-barney-gumble-simpsons-trollface-troll-face.gif"
b[n++]="_-RBmQayiyY/UqANt45KiDI/AAAAAAAAFZo/AsqxnIHKFDc/s1600/eric-cartman-south-park-fuck-you-troll-off-trollface.gif"
b[n++]="Of5TlkF4NCs/UqANuWbeWLI/AAAAAAAAFZ4/Q5vc4kgoMWE/s1600/eric-cartman-south-park-is-your-catfish-troll-in-real-life-online-love.gif"
b[n++]="cQvwyjgZJP8/UqANvIDnT9I/AAAAAAAAFZ8/SN8l-WhhC5A/s1600/ewok-pedobear-pedophile-pedo-bear-troll-face.gif"
b[n++]="HjIzRZM90y8/UqANvBnuBvI/AAAAAAAAFaE/1WOsuQvVrSE/s1600/falling-down-endless-bottomless-troll-face-meme.gif"
b[n++]="uWThCjxXJxY/UqANv9kma8I/AAAAAAAAFaU/BDeEMd6VGyc/s1600/fat-obese-man-guy-dancing-proud-living-like-boss-troll-face-stomach.gif"
b[n++]="gMgfZjJd7qc/UqANwb86EHI/AAAAAAAAFac/XaEmegMcbrk/s1600/feed-a-troll-feedatroll-save-trolls-foundation-starving.gif"
b[n++]="ssgsYVHcQdY/UqANwfLSl8I/AAAAAAAAFaY/-duucTQ91hU/s1600/flipbook-trollface-troll-stickman-stick-man-animated.gif"
b[n++]="z18bs5LNleQ/UqANxbRfHdI/AAAAAAAAFag/kQe-WVv-7Ww/s1600/fuck-you-fuck-off-F-U-goof-trollface-troll-face.gif"
b[n++]="CIdlX3nw-Is/UqANyaHsGGI/AAAAAAAAFaw/UIMSmSpTdiU/s1600/futurama-fry-leela-bender-characters-troll-face-trollface.gif"
b[n++]="ODEIEjx6mXc/UqANybVoQNI/AAAAAAAAFa8/KQNTtGGKObE/s1600/get-out-wave-hand-point-way-leave-troll-face-trollface.gif"
b[n++]="uIekqVVNxXw/UqANyalHIzI/AAAAAAAAFa0/6Y93EeZMmPM/s1600/god-created-man-troll-face-trollface-meme.gif"
b[n++]="g_MvVIZirNU/UqANz6F7UKI/AAAAAAAAFbM/8JIvF_JQJlg/s1600/google-plus-wasted-space-post-troll-faces-trollface.gif"
b[n++]="agLLQXkif68/UqANz_8qavI/AAAAAAAAFbU/G7xoDVTModI/s1600/googly-eyes-troll-face-pedo-predotroll-pedobear.gif"
b[n++]="qc26bXtoaUw/UqANzxfwh1I/AAAAAAAAFbE/so0reG6K76w/s1600/googly-eyes-troll-face-trollface-eyed-googlies.gif"
b[n++]="nkrrgpe2AQU/UqAN0j4rzcI/AAAAAAAAFbg/uMGusYPNCvw/s1600/great-big-fuck-you-douche-bag-cock-sucker-goof-jerk-ex-boyfriend-girlfriend.gif"
b[n++]="uFqOeE7qzk4/UqAN1D_7fbI/AAAAAAAAFbk/lKOfPcOVFI8/s1600/haters-gonna-hate-dancing-troll-face-trollface.gif"
b[n++]="qTBhouQa2ME/UqAN1pQlQ3I/AAAAAAAAFbs/6v3Vzrqn3Gs/s1600/heres-johnny-nicholson-the-shinning-troll-face-trollface.gif"
b[n++]="i3my5IO1iKY/UqAN2ZjZ1GI/AAAAAAAAFb0/rR_WaLNG5Ec/s1600/hung-man-hanging-noose-troll-face-flicks-body-trollface.gif"
b[n++]="ZVRiMc5Ervk/UqAN3AB-YtI/AAAAAAAAFcA/O2L9--m8CH0/s1600/i-be-trolling.gif"
b[n++]="V136nitea28/UqAN4e8QNyI/AAAAAAAAFcI/Il-paDR0JmY/s1600/i-be-trolling2.gif"
b[n++]="NeSF1N8DKV4/UqAN5LG-OfI/AAAAAAAAFdQ/XUfAeaTRPrY/s1600/i-be-trolling3.gif"
b[n++]="zJkuvj8hmZA/UqAN4Qp3juI/AAAAAAAAFcM/tCiWFqpSyn4/s1600/id-hit-that-troll-face-trying-to-hump-fuck-you.gif"
b[n++]="aTY7L3fatls/UqAN5Pg6EYI/AAAAAAAAFcU/yy1BLaO_YwE/s1600/incredible-hulk-comic-book-cartoon-troll-face-trollface.gif"
b[n++]="R_b1yCEc9_o/UqAN5IyedNI/AAAAAAAAFcc/2Dko4sr76gQ/s1600/infinite-trolling-forever-always-stroll-troll-face-trollface.gif"
b[n++]="0rUS1iG4qCE/UqAN5tXJl9I/AAAAAAAAFck/nWJfR5QGItQ/s1600/infinite-trolling-forever-always-troll-face-trollface.gif"
b[n++]="qgk0yaG_0uo/UqAN6pFBcwI/AAAAAAAAFdI/hj4AzKnN1TE/s1600/internet-memes-troll-face-remix-troll-face-remixed.gif"
b[n++]="DTQJgcbshDk/UqAN7EJmVrI/AAAAAAAAFdE/yvLrLcS8Tkg/s1600/jesus-christ-hitching-ride-with-cross-troll-train.gif"
b[n++]="4C8VbNxXWRE/UqAN7Z0kChI/AAAAAAAAFdA/y5bRKYGLVFw/s1600/jesus-christ-troll-face-trollface-oh-god-women-horny.gif"
b[n++]="1uJvPFCAW2c/UqAN7sMTC4I/AAAAAAAAFc8/p9V5egkHNks/s1600/jesus_christ_movie_theater_now_playing_city_town_nazareth.gif"
b[n++]="63LmW9L8Hpo/UqAN8CsyuLI/AAAAAAAAFdM/QzwPevfbGvA/s1600/jim-carey-dancing-mental-institution-troll-face-trollface.gif"
b[n++]="_lPASNmFiAA/UqAN9P-9saI/AAAAAAAAFdo/yuF_jBh562E/s1600/jonah-hill-fangirling-trollface-troll-face-meme.gif"
b[n++]="pp315DOC9lA/UqAN9G-4amI/AAAAAAAAFdg/jjajTioazRk/s1600/jump-on-head-broklyn-bounce-troll-face-trollface.gif"
b[n++]="zulqQpvusaU/UqAN9FN8HXI/AAAAAAAAFds/Pj7kR3PsSys/s1600/kill-cute-baby-of-the-week-troll-face-trollface.gif"
b[n++]="bGATM5Ub3uU/UqAN-H8tgXI/AAAAAAAAFd0/67wh4St8-iI/s1600/ladies-night-out-male-stripper-trollface-troll-face-jerking-off.gif"
b[n++]="15XGQ_G2it8/UqAN-eHbNAI/AAAAAAAAFeA/rIeH7cIUSMc/s1600/letter-to-santa-claus-u-gusta-troll-face-trollface-memes.gif"
b[n++]="JDZUdcSvg2s/UqAN_ejYdEI/AAAAAAAAFeM/IXEvTGY5sLY/s1600/lol-laugh-out-loud-scroll-troll-face-downward-spiral.gif"
b[n++]="RVQTu17eCqY/UqAN_iw2dII/AAAAAAAAFeU/hI-Vd9qNllc/s1600/lol-laugh-out-loud-scroll-troll-face-upward-spiral.gif"
b[n++]="TGZwzdf77yI/UqAN_wPilLI/AAAAAAAAFeQ/CZRUrPtBEjo/s1600/lol-laughing-out-loud-troll-face-loltroll-trololol-derp.gif"
b[n++]="GCsQX7a99OI/UqAOANGie3I/AAAAAAAAFec/QDx6VvuFtOs/s1600/lol-laughing-out-loud-troll-face-trollface-meme.gif"
b[n++]="PghjwMNPfm8/UqAOAWYJwSI/AAAAAAAAFeo/4k1QCSQVJHI/s1600/lol-laughing-out-loud-troll-face-trollface-rainbow.gif"
b[n++]="RrIb-dHNmP0/UqAOBAvh9_I/AAAAAAAAFew/g_HW1rwJHsQ/s1600/lol-laughing-out-loud-troll-face-trolol.gif"
b[n++]="rJwYtrhIDu8/UqAOBHw3WsI/AAAAAAAAFe0/lAGFE8pqB8w/s1600/long-scrolling-infinite-troll-faces-trollface.gif"
b[n++]="V7ab5Tixq_A/UqAOB46FxEI/AAAAAAAAFe4/zTrbIv0zVAc/s1600/meet-the-scrolltroll-scrolling-trolls-endless-faces-trollface.gif"
b[n++]="BLMbB3h7Iec/UqAOC6GItRI/AAAAAAAAFfI/LpN1FxQaHIQ/s1600/meme-fuck-you-troll-face-giving-middle-finger-trolllface.gif"
b[n++]="imcuh03qR-I/UqAODpl4a6I/AAAAAAAAFfU/XtfhdATdVxY/s1600/meme-how-many-fucks-given-middle-finger-trolllface.gif"
b[n++]="xC_9WKaxJB0/UqAODS4YrqI/AAAAAAAAFfQ/ee1N8UVsd6A/s1600/michael-jackson-moon-walk-pedobear-trollbear-pedo-bear-troll-bear.gif"
b[n++]="IxDGgC_H28o/UqAODzEOvwI/AAAAAAAAFfY/oKb0ycW2FvM/s1600/mickey-mouse-disney-troll-face-trollface.gif"
b[n++]="GldHhj69Ubo/UqAOEnEggeI/AAAAAAAAFfk/kH4_mHkcebM/s1600/mr-creepy-troll-face-animated-trollface-meme.gif"
b[n++]="fkQ58S7XSX0/UqAOFsU-7pI/AAAAAAAAFfw/O3PEqKa3Z6k/s1600/mr-mrs-male-female-morphing-faces-troll.gif"
b[n++]="56icshasqms/UqAOFlOnt7I/AAAAAAAAFf8/reG7LYeGwf0/s1600/muhaha-evil-troll-face-animated.gif"
b[n++]="JSVOnx3vKPI/UqAOGeHAOcI/AAAAAAAAFf4/xBDL1svcMjM/s1600/no-troll-face-shaking-head-animated.gif"
b[n++]="PCsBqK80GLw/UqAOGp0cE3I/AAAAAAAAFgE/ymnw6Iw-Y6g/s1600/obey-listen-to-follow-me-troll-face-meme-trollface.gif"
b[n++]="SkABIO9hY6g/UqAOHHPZ3UI/AAAAAAAAFgQ/bbUeJKMlNaw/s1600/phenakistoscope-POV-persistence-of-vision-optical-illusion-troll-face-gusta-meme.gif"
b[n++]="ALkz6GvPbiE/UqAOH2ELXYI/AAAAAAAAFgY/17cVAs7h4a8/s1600/pikachu-trollface-surfing-trolling-victims-deal-with-it-troll-face.gif"
b[n++]="bdzLvHIQ8l4/UqAOIYuJZjI/AAAAAAAAFgc/obXgh2pmQ6k/s1600/puss-in-boots-wtf-cat-troll-face-trollface-pussy.gif"
b[n++]="p80acHIPGxE/UqAOI1k5HeI/AAAAAAAAFgk/7AhWe09gdfc/s1600/rage-face-troll-meme-fuck-you-fuuuuu-animated.gif"
b[n++]="xM7mMhoeW68/UqAOI515QGI/AAAAAAAAFgs/tYaFhHYQjOI/s1600/rage-troll-face-meme-comic-painting-saying-fuck-off-you.gif"
b[n++]="sO2uIsPtUeA/UqAOJYcK-7I/AAAAAAAAFg0/qxzje5s4FvM/s1600/retard-alert-troll-face-mr-garrison-south-park-cartoon.gif"
b[n++]="G3h0NWeaOUI/UqAOJ6Y0jGI/AAAAAAAAFhE/voQzQHrJswA/s1600/scroll-troll-poster-animated.gif"
b[n++]="3TihvtCL4dg/UqAOK0EgqII/AAAAAAAAFhU/SKtPtz_Xwsw/s1600/scrolling-infinite-loop-trolls-puking-puke-troll-face-spew-throw-up-sick-vomit.gif"
b[n++]="cgJRZIrHcqc/UqAOKyGLM7I/AAAAAAAAFhI/KBQmdbrS4Cc/s1600/scrolling-infinite-troll-faces-trollface.gif"
b[n++]="znH9y3DaAZY/UqAOK1bIBGI/AAAAAAAAFhM/FUdVYE7Jiqo/s1600/scrolltroll-scrolling-trolls-endless-faces-trollface.gif"
b[n++]="TG_owXcQlSk/UqAOMAcvtRI/AAAAAAAAFhg/1Skg0R6RdvU/s1600/sexy-woman-female-troll-rage-face-hot-babe-bra-naked.gif"
b[n++]="yqvqmQnSvoY/UqAOMlMNmhI/AAAAAAAAFhw/bt0w0BnEYFw/s1600/slenderman-being-trolled-by-trollfaces-troll-faces-pervert.gif"
b[n++]="2irt2ocO5FE/UqAOMrq7HeI/AAAAAAAAFho/uTXz4M8JXAE/s1600/springtime-troll-trollface-trolls.gif"
b[n++]="2i2G-KnUqUo/UqAONDYRufI/AAAAAAAAFh4/3Hjj6Kh8rjc/s1600/stream-of-trolls-puking-puke-troll-face-spew-throw-up-sick-vomit.gif"
b[n++]="ZdY6IKdpG6k/UqAONj6zZEI/AAAAAAAAFh8/ynvH1NbmpHM/s1600/surfing-troll-trollface-water-speed-boat_Micael_Reynaud22.gif"
b[n++]="gEByccHEnjY/UqAONimZnUI/AAAAAAAAFiM/Nvh-sNjoTi4/s1600/swag_troll_face_fur_coat_trollface_mask_haters_gonna_hate.gif"
b[n++]="xpgQw-cPNQE/UqAONyroqTI/AAAAAAAAFiE/gaHwvEOe_hE/s1600/this-post-is-gay-gaytroll-troll-homosexual-trololol.gif"
b[n++]="cpDb0KifCtI/UqAOOojyqmI/AAAAAAAAFiU/Exwivr35GSM/s1600/troll-batman-movie-Joker-Clapping-trollface.gif"
b[n++]="7P0TQXe6Baw/UqAOPDXZQ1I/AAAAAAAAFik/dRStwjGXz48/s1600/troll-behind-the-mask-wolf-sheep-clothing-trollface-face.gif"
b[n++]="ihD0oBFqKT4/UqAOPk8QWyI/AAAAAAAAFig/UEDp_QeibV4/s1600/troll-creepy-freaky-weird-face-trollface-meme-animated.gif"
b[n++]="PiVUu-W3WTs/UqAOQJQriaI/AAAAAAAAFis/C3Vt3tvWEb0/s1600/troll-face-animated-reaction-num-yup-hey-hi.gif"
b[n++]="LHoJlfbcHeM/UqAOQQXvSRI/AAAAAAAAFi0/E27FskZPJWg/s1600/troll-face-batman-robin-running-gotham-city-trollface.gif"
b[n++]="qX4qNbpXmPU/UqAORFIM9SI/AAAAAAAAFjA/dwBHQbFFWRQ/s1600/troll-face-bling-gold-animated-trollface.gif"
b[n++]="oVWZWrl489U/UqAOREXkZyI/AAAAAAAAFjI/yrDnNRaN9Gg/s1600/troll-face-bob-dobbs-chsurch-of-subgenius-trollface.gif"
b[n++]="esuewLevkRQ/UqAORzLOwaI/AAAAAAAAFjM/UmCPvPwT1YM/s1600/troll-face-changes-into-human-creature-mutation-meme.gif"
b[n++]="jxbaEWuakWQ/UqAOSJniLdI/AAAAAAAAFjQ/Tb2yEmKoYvw/s1600/troll-face-clapping-proud-of-your-stupid-post.gif"
b[n++]="G8J8_KeUtzo/UqAOTIhVGuI/AAAAAAAAFjk/lSN0YK_GrKM/s1600/troll-face-clowning-spinning-around-clown-trollface.gif"
b[n++]="S4CEffiIDr0/UqAOTEu1emI/AAAAAAAAFjg/vJLeSTWSQAQ/s1600/troll-face-cookie-monster-waiting-sesame-street.gif"
b[n++]="-OYAw_Hq460/UqAOUDDTjJI/AAAAAAAAFkE/9uwiV-tsqGg/s1600/troll-face-dancing-pumpkin-head-bob-dobbs-trollface%2B%25282%2529.gif"
b[n++]="f5uXmp82W18/UqAOVF8A6RI/AAAAAAAAFkY/rZLu5TN1H3Q/s1600/troll-face-fail-Bob-Dylan-Subterranean-Homesick-Blues.gif"
b[n++]="xiYsTHPMNz4/UqAOVAl0yMI/AAAAAAAAFkM/50EH4dLVx7c/s1600/troll-face-giving-blow-job-fake-animated.gif"
b[n++]="zte7x_GbmRI/UqAOWB7GnlI/AAAAAAAAFkk/VWQcK1YRF1w/s1600/troll-face-glitch-art-glitchart-trollface.gif"
b[n++]="bsR4rbQHjgI/UqAOWU6_wcI/AAAAAAAAFks/SN_BgbbKEcY/s1600/troll-face-glitch-art-glitchart-trollface2.gif"
b[n++]="_ahJEPKwzeM/UqAOW6RYzJI/AAAAAAAAFlE/bKd0RdoB__o/s1600/troll-face-glitch-art-wtc-911-terrorist-attack-usa.gif"
b[n++]="GfWfhnwFd08/UqAOW-Vn84I/AAAAAAAAFlA/Xnn7Fgb6PDQ/s1600/troll-face-heres-johnny-the-shinning-shining-trollface.gif"
b[n++]="pli1lISv8Z4/UqAOX6e2ZOI/AAAAAAAAFk8/UG-cjRytrnQ/s1600/troll-face-holding-gun-shoot-kill-you-trolling.gif"
b[n++]="rPjYrude3Fo/UqAOYFS2bHI/AAAAAAAAFlI/qR61kTY7KOM/s1600/troll-face-how-not-to-cross-the-street-trollface.gif"
b[n++]="JDNLNL2n7RM/UqAOYTur0eI/AAAAAAAAFlY/7uPHycd4GOI/s1600/troll-face-itch-bum-dancing-ant-pants-dance-trollface.gif"
b[n++]="zCbMM6xE4XU/UqAOZUB4c9I/AAAAAAAAFlk/kmAI95jz_qc/s1600/troll-face-look-at-me-i-dont-care-trollface.gif"
b[n++]="s1fIm_cDhyQ/UqAOZRVcmFI/AAAAAAAAFlg/6gpqA_f79i4/s1600/troll-face-meh-blah-boring-didnt-read-trollface-down.gif"
b[n++]="KJrCOt8cH1o/UqAOar6Jm1I/AAAAAAAAFlo/k3fNknq38T8/s1600/troll-face-meh-blah-boring-didnt-read-trollface.gif"
b[n++]="1BUFureDFfI/UqAObNSgOeI/AAAAAAAAFmE/M7jHmSrxC68/s1600/troll-face-music-dance-party-dancing-trollface%2B%25282%2529.gif"
b[n++]="cu7VHjbXmn8/UqAObZugGMI/AAAAAAAAFl4/YUSQvmAMInM/s1600/troll-face-music-dance-party-dancing-trollface.gif"
b[n++]="SSTu3Hd_Hro/UqAObXWRWdI/AAAAAAAAFl8/Lt9GhzhGr8s/s1600/troll-face-put-up-your-dukes-them-there-fighting-words-trollface%2B%25282%2529.gif"
b[n++]="X07MgxRBG8g/UqAOcnnQH2I/AAAAAAAAFmU/ZW0NB30Spis/s1600/troll-face-queen-we-will-rock-you-trollface.gif"
b[n++]="z03EINY29Zw/UqAOdNafm9I/AAAAAAAAFmc/eSEs0NxpgWA/s1600/troll-face-run-away-leave-sick-trollface%2B%25282%2529.gif"
b[n++]="n8dHfmjWYMA/UqAOdzcuzXI/AAAAAAAAFms/q1sJwwJrNpM/s1600/troll-face-saying-blah-boring-didnt-read-trollface.gif"
b[n++]="YBp81r6tcDQ/UqAOexdLR3I/AAAAAAAAFnA/woGX8gX04eY/s1600/troll-face-terrorism-wtc-911-terrorist-attack-usa-united-states.gif"
b[n++]="Fyar-1PfHpM/UqAOe1L4BZI/AAAAAAAAFm0/Pgcrs7QBQxM/s1600/troll-face-trollface-canada-canadian-canuck.gif"
b[n++]="XuRc7cibCGQ/UqAOfbDq0RI/AAAAAAAAFnE/oralxsAVeBQ/s1600/troll-face-trollface-pug-dog-puglet-pugly.gif"
b[n++]="lzP35wlO_rE/UqAOf7-HEtI/AAAAAAAAFnM/faQz_Do-oOk/s1600/troll-face-trolls-fap-fappable-fapping-trollface%2B%25282%2529.gif"
b[n++]="HORYPDrHNSA/UqAOgEDUppI/AAAAAAAAFnY/2Rf8Xw1yhcI/s1600/troll-face-trolls-fap-fappable-fapping-trollface.gif"
b[n++]="Sc9g1qECvVw/UqAOgl1EriI/AAAAAAAAFnk/pjs3kjejEoY/s1600/troll-face-trolls-music-dance-party-dancing-trollface.gif"
b[n++]="Wuq9TmtpuUM/UqAOgviYFwI/AAAAAAAAFng/5oGTBeBzgU4/s1600/troll-face-twerking-dancing-twerk-dance-trollface.gif"
b[n++]="vCyHJ6pN2-M/UqAOhZ2lH_I/AAAAAAAAFno/h8U71jGx2pI/s1600/troll-face-you-are-insane-crazy-trollface.gif"
b[n++]="RsjJ5kzGfiA/UqAOiL-PZ3I/AAAAAAAAFoE/G5xbk4G0XG8/s1600/troll-jesus-christ-slips-bannana-peel-walking-on-water-trollface.gif"
b[n++]="rvvICXwpXto/UqAOiIHYQeI/AAAAAAAAFn8/XctyML7zNL4/s1600/troll-powered-car-bike-unicycle-transportation-trollface.gif"
b[n++]="V6zM_HdFL4E/UqAOiP098AI/AAAAAAAAFn4/Fla5kpDn3w4/s1600/troll-santa-claus-why-u-no-bring-me-presents-christmas.gif"
b[n++]="2CuKBOQCscw/UqAOjDzdndI/AAAAAAAAFoM/5OtPJM312ng/s1600/trollface-bart-homer-simpson-tv-character-troll-face.gif"
b[n++]="jA5jihUF8kI/UqAOjv3WdrI/AAAAAAAAFoU/vAaf3F2tf-s/s1600/trollface-bobble-head-back-forth-bobbing-face.gif"
b[n++]="Qo6BvgKLmi4/UqAOjn2EB5I/AAAAAAAAFoc/afcMvcESuVw/s1600/trollface-douche-bag-dancing-goof-jerk-disco-face.gif"
b[n++]="HJ2L5yhqMSE/UqAOkvYvCkI/AAAAAAAAFok/an1ksBjGSek/s1600/trollface-funny-dance-silly-walk-troll-face.gif"
b[n++]="ECbt_HxFcS0/UqAOlV13UQI/AAAAAAAAFow/BGxeWNwUDkY/s1600/trollface-masterbait-master-bait-bate-masturbate-masterbate-troll-face.gif"
b[n++]="913JBOuHOaI/UqAOl2MaU8I/AAAAAAAAFo4/fj3VH2_crLU/s1600/trollface-sexy-woman-walking-red-head-ginger-troll-face%2B%25281%2529.gif"
b[n++]="F1U6gsboCdQ/UqAOmhTziDI/AAAAAAAAFpA/h5keJVbb0Fg/s1600/trollface-troll-face-meme-flashing-OPTICAL-illusion.gif"
b[n++]="2RuV58HsiLo/UqAOm8VBAwI/AAAAAAAAFpU/NAUYXldQVxk/s1600/trollface-troll-face-meme-flashing-strobe-OPTICAL-illusion.gif"
b[n++]="60ZlpkzbXN0/UqAOm1nt7lI/AAAAAAAAFpI/N0CmFpdDeJo/s1600/trolling-in-the-deep-trollface-trollies-trollied-dumb-stupid.gif"
b[n++]="KWBMm6Koo6U/UqAOoCO5R6I/AAAAAAAAFpg/mc20hYE_6AA/s1600/trolls-like-fun-too-trollface-troll-face-bouncing-jumping.gif"
b[n++]="NIrLCadMzNc/UqAOozhNv4I/AAAAAAAAFpw/6DB-q1u_pCw/s1600/trollway-highway-trolls-faces.gif"
b[n++]="WBCX7YkrWt8/UqAOoxWaXAI/AAAAAAAAFpk/Wiq1UZqI4Aw/s1600/truth-santa-claus-is-fake-just-your-parents-troll-christmas.gif"
b[n++]="MBKC9bL58Do/UqAOpPb0O3I/AAAAAAAAFp4/4njNYxnKuhQ/s1600/tweeker-troll-face-trollface-meth-addiction-recovery.gif"
b[n++]="iuu9RigYa60/UqAOp9927uI/AAAAAAAAFqA/lyGARpF7Oiw/s1600/u-mad-bro-Art-Thou-Angered-trollface-troll-facegif.gif"
b[n++]="qVBVp4UUsKk/UqAOp3Rf_eI/AAAAAAAAFqE/Uk1_8rNpbkI/s1600/u-trippin-balls-yet-bro-troll-face-trollface.gif"
b[n++]="lrvuq3rECGE/UqAOqfL_M0I/AAAAAAAAFqU/eG_yB14aYmI/s1600/u-you-me-gusta-trollface-troll-face-meme-animated.gif"
b[n++]="DUjzyTZeEI4/UqAOq7jeiLI/AAAAAAAAFqQ/yF_DKnTm4q4/s1600/vagina-vulva-troll-pussy-face-twat-snatch-squirter.gif"
b[n++]="-MRQzwCLF88/UqAOrP1N4dI/AAAAAAAAFqg/rywIvTnHrXQ/s1600/weird-trollface-troll-face-googly-eyes-eyed-googlies.gif"
b[n++]="2Rj_1PqHzI4/UqAOrUBgB3I/AAAAAAAAFqk/9Bsxjk3-wBo/s1600/whack-a-troll-boss-employee-whak-trolls-face-punch-kapow-pow.gif"
b[n++]="m3o3zA1iaiY/UqAOsKkPyMI/AAAAAAAAFqs/JT1mf8qeo7s/s1600/whak-a-kitty-whack-a-mole-game-kittens-cute.gif"
b[n++]="VqEQAHe6lmI/UqAOsdiTYAI/AAAAAAAAFq0/sgdi6WVfIow/s1600/whak-a-troll-whack-punch-out-trollface-face-knock.gif"
b[n++]="CmgPiOLJBMg/UqAOtL2J0XI/AAAAAAAAFq8/BnY57jOOAk4/s1600/whak.com_funny_advertisement_chuck_norris_punching.gif"
b[n++]="qtjgqa-3M8Q/UqAOtNSsf5I/AAAAAAAAFrE/sNi4bsX0oBA/s1600/whak.com_funny_advertisement_face_punch_fight_club.gif"
b[n++]="SWiZjR0JE1w/UqAOt2H5_KI/AAAAAAAAFrQ/2LUatxwY-Ho/s1600/who-cares-dancing-troll-face-office-work-place-goofing-off.gif"
b[n++]="RpS-qX1Vwcw/UqAOunwCHHI/AAAAAAAAFrc/RHgjvOH2nzU/s1600/whos-on-top-trolls-troll-faces-meme-trollface.gif"
b[n++]="UGo2aeGG7po/UqAOuyTV8jI/AAAAAAAAFrY/Bg549jaHJAA/s1600/wtf-man-with-troll-face-mask-kinky-wig-freak.gif"
b[n++]="OI6PJFsmCwc/UqAOvJkMOtI/AAAAAAAAFrk/gk2anxsLRco/s1600/you-angered-a-pissed-off-troll-face-trollface.gif"
b[n++]="9qos00unWGQ/UqAOvjSWxSI/AAAAAAAAFrw/oMkjRWDyfcA/s1600/you-have-been-officially-trolled-troll-faces-trollface.gif"
b[n++]="81fZg0zmzOc/UqAOwll6Q_I/AAAAAAAAFr8/GVV_wDOOAT0/s1600/you-have-been-trolled-1280x720-HD-scroll-troll-poster-animated.gif"
b[n++]="AG3EYvzAFL4/UqAOwGbmABI/AAAAAAAAFr4/-Lcj5n0y5cc/s1600/you-turn-me-on-troll-face-lightbulb-electricity-trollface.gif"
b[n++]="2-XhPYR4WbY/UqAOw1dDIPI/AAAAAAAAFsA/GGlq_WksOCQ/s1600/zoom-in-your-face-big-huge-trollface-troll.gif"
b[n++]="Dqelkj6vxIs/UqAQo6VKTCI/AAAAAAAAFsY/xyxD_NrxJrk/s1600/baby_slap_troll_punches_babies_too_cute_trollface_meme.gif"
b[n++]="6_wdcOKBnRw/UqAQpE4jF7I/AAAAAAAAFsc/9f8qR_RkBIY/s1600/cat-plays-ipad-dancing-trolls-trollface-meme-lolcat-funny.gif"
b[n++]="2t446s-Bilc/UqAQpCOIlYI/AAAAAAAAFsk/dKx4THWecNw/s1600/cockroach-troll-pest-control-controll-trollface-bugs-insects.gif"
b[n++]="-mcotoShE_k/UqAQp9QA6-I/AAAAAAAAFs4/8xNKpiv_-_k/s1600/complaining_troll_face_meme_trollface_lip_sync_animated.gif"
b[n++]="uTM43bd7IP8/UqAQp4OPtsI/AAAAAAAAFs0/x02hRWNyhkI/s1600/creepy_goth_emo_troll_black_eye_liner_lol_face.gif"
b[n++]="b2zZKSEDrRg/UqAQqIOrMII/AAAAAAAAFsw/PQ1tN-YEETk/s1600/dance-pump-up-jam-two-trolls-black-negro-troll-white-trollface.gif"
b[n++]="qWLCgDsLR2c/UqAQrhloSQI/AAAAAAAAFtI/8TZqLcUgMsY/s1600/finger-circle-game-troll-style-meme-rage-face-rageface-comic.gif"
b[n++]="utfHiuAwzxs/UqAQriRZdBI/AAAAAAAAFtU/Oo9kyFlKTTw/s1600/human_anatomy_ovaries_woman_egg_menstrual_cycle_uterus_troll.gif"
b[n++]="JrvVoyN-GCA/UqAQrpVPTMI/AAAAAAAAFtQ/fjCfsyHu9TM/s1600/i_will_pray_for_you_holy_bible_praying_hands_troll_face_meme.gif"
b[n++]="fqCSD8iJm60/UqAQs1dm3XI/AAAAAAAAFto/0KaoUDy7tG8/s1600/la-cucaracha-the-cockroaches-a-cock-roach-roaches-pests-bugs.gif"
b[n++]="DufQzgcDDFg/UqAQsgmUKmI/AAAAAAAAFtc/2Z6tqjGqcz8/s1600/lol_cat_kitten_kitty_cute_playing_with_ipad_tablet_PC_troll_on_screen.gif"
b[n++]="Imx7IVFT3HE/UqAQtPK34KI/AAAAAAAAFuQ/fU-tbTNrY0I/s1600/mosquitoes-bite-infection-disease-mosquito-troll-face-meme.gif"
b[n++]="8thKU_CIY6U/UqAQtjM3GFI/AAAAAAAAFts/vIy-rwNvxOw/s1600/pedobear-pedo-bear-is-in-heat-hot-panting-sexy-drooling.gif"
b[n++]="unqLiKkwvEY/UqAQur3ICGI/AAAAAAAAFuA/uCNnqtBKVbY/s1600/santa_claus_troll_trollface_cockroaches_la_cucarachas.gif"
b[n++]="CFwiUQfk50k/UqAQuzaqiLI/AAAAAAAAFt8/9xbkq_WZh5s/s1600/smack-my-bitch-up-troll-slaps-cute-baby-knocked-out-cold.gif"
b[n++]="4_aDkiYmMOo/UqAQvUzT8rI/AAAAAAAAFuI/Pk3PrHKmB1g/s1600/tongue-troll-face-optical-illusion-paradox-infinity-loop.gif"
b[n++]="2k-CCxP3OFw/UqAQwEpvPyI/AAAAAAAAFuY/P21lX7bkf64/s1600/troll-face-optical-illusion-Droste-effect-picture-in-pic-infinity.gif"
b[n++]="XksUMA9ikI8/UqAQwRMwmaI/AAAAAAAAFuc/8K5-Feo_bD0/s1600/tux_boxing_windows_PENGUIN_troll_face_meme_linux_OS_server.gif"
b[n++]="ERQvV9gODaQ/UqAQwrHUZLI/AAAAAAAAFug/JEWTU3oQ8U8/s1600/windows-bluescreen-error-code-crash-linux-penguin-troll-meme.gif"
b[n++]="BEJsJfD9oiI/UqdK1qtNl-I/AAAAAAAAFz4/X5Lq4C0-xuo/s1600/urinal-mens-washroom-pee-urine-urination-piss-troll-meme-penis.gif"

b.forEach(function (val) {
    console.log("http://lh5.googleusercontent.com/-" + val);
})
```

これで全ての画像のURLがコンソール上に表示されるため，以下のコマンドをシェルで実行し全ての画像をダウンロードした．
```bash
$ node main.js 2> /dev/null | xargs wget
```

そのあと，**全てのトロール画像**を**目で確認した**が，フラグが書かれた画像はなかった :innocent:

---

気を取り直して，ページAの中身を確認することにした．

まずページAで読み込んでいる[`hook.js`](./hook.js)を確認すると，
何かしらの難読化がされた関数`catch_me`があった．
しかし，この関数は使われておらず，この難読化を解読することが解決に繋がると推測した．

Google Chromeのデベロッパーツールを用いて，ブレークポイントをつけたりしながら，
`catch_me`関数が実行されるように試みたが上手くいかなかったので，
`catch_me`関数の中の難読化された部分を単純にコンソールに表示することにした．

コンソールに表示するスクリプト([`console.js`](./console.js))を実行すると，かなり酷い文字列が得られた．

```bash
$ node console.js
alert(Xiomara{i_4gr33_Y0U_4r3_a_Flash!}))
```

Java Scriptの命令として実行も出来なければ，フラグの形式も無茶苦茶なものだった．
とりあえず，`alert`の中の文字列をフラグとしてサブミットしてみたが，もちろん正解にはならなかった． :rage:

ここで若干の**エスパー力**を発揮して，色々とフラグを確かめてみると正解となるフラグが得られた．

## Flag

`xiomara{i_4gr33_Y0U_4r3_a_Flash!})`

#### その後は恐らく修正されたと思われる :shit:
