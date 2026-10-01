# Neutrinos em espaço-tempo curvo

Seminário na **II Escola Brasileira de Neutrinos** — sexta, 02 de outubro de 2026.
Rafael C. R. de Lima · Departamento de Física · UDESC/CCT · Joinville.

**No ar:** <https://rafael-lima.pages.dev/talks/2026-ebn/> — publicado pela [página pessoal](https://github.com/RafaelCRdeLima/homepage), na seção Talks.

## Idiomas

`index.html` (português) e `en.html` (inglês) são o mesmo deck, com o mesmo CSS e JS; o `dash.js`
lê o `<html lang>` e escolhe rótulos e separador decimal pela função `T(pt, en)`. A escolha segue a
chave `rcrl-lang` da página pessoal (mesmo domínio): quem escolheu EN no site abre direto em inglês;
sem preferência, vale o idioma do navegador. O canto superior direito tem PT / EN.

**Ao editar um slide, mexa nos dois arquivos.**

## Apresentar

Um único `index.html`, sem build. Abra direto no navegador ou sirva a pasta:

```bash
python3 -m http.server 8000
```

| tecla | ação |
|---|---|
| → / espaço | próximo slide |
| ← | anterior |
| Home / End | primeiro / último |
| F | tela cheia |
| N | notas do apresentador |
| O | visão geral (clique num slide para ir até ele) |
| Esc | solta um controle e devolve as setas à navegação |
| ? | atalhos |

O endereço guarda o slide atual (`#3` abre o terceiro). O palco é fixo em
1920×1080 e escala para caber na tela, então o layout é o mesmo no notebook e
no projetor. Para PDF, imprima do navegador: um slide por página.

## Estrutura

47 slides em **três partes**, cada uma com capa própria, mais duas laminas de
premissa na abertura.

| parte | cor | conteúdo |
|---|---|---|
| abertura | violeta | roteiro e duas premissas: as duas bases (sabor e massa) e a ressonância MSW com o peso do ordenamento |
| I · Espaço-tempo curvo | âmbar | Einstein, Sobral 1919, Schwarzschild, o que a curvatura faz com um neutrino (redshift e desvio, com números), geodésicas, compacidade, objetos compactos, pulsares e LIGO, a fase covariante e seu dashboard |
| II · A supernova, e os neutrinos no poço | turquesa | SN 1987A, anatomia da supernova (fases e tempos, estagnação e revivescimento do choque), colapsares e o motor NDAF, emissão dentro do poço, lente gravitacional, fronteira, DUNE e observatórios, onde moram as ressonâncias H e L, e a frente cruzando a H |
| III · GHOST (resultados) | rosa | adiabaticidade e L_osc, o critério, a largura numérica, o custo em P_H, o viés no DUNE, o mapa em (t, E) e as bandas por progenitor |

**Redesenhado em 30/09/2026 para a II Escola Brasileira de Neutrinos.** A escola
já tem seminários sobre a história do neutrino e sobre oscilação, então a antiga
Parte I, que gastava 19 slides nisso, foi reduzida a duas laminas de premissa.
O espaço foi para relatividade, astrofísica e os resultados, que passaram de 10
para 13 slides. A figura `fig_landau_zener.svg` estava nos assets desde o início
e nunca tinha ido a um slide; agora ela sustenta a lamina que define L_osc, sem
a qual o critério de 3 L_osc aparece como número sem origem.

```text
index.html           os slides (texto e marcação)
assets/deck.css      o estilo inteiro
assets/deck.js       navegação, utilitários de gráfico, fundo animado da capa
assets/dash.js       gráficos de dados e dashboards
assets/ghost-choque.js  perfis de M15-7b para o painel do choque (copiado de GHOST/slides/choque-dados.js)
assets/img/ghost/    figuras do paper do GHOST (de GHOST/slides/figuras)
assets/img/          fotos e figuras + credits.json (autor, licença, página de origem)
tools/credits.py     regenera o slide de créditos a partir de credits.json
```

## Dashboards

Todos calculam no navegador, sem rede.

| slide | o que faz |
|---|---|
| 8 | órbita de Mercúrio animada: rosácea da RG r = p/(1 + e cos kφ) com a precessão exagerada 3×10⁵×, lei das áreas, elipse de Newton tracejada; contadores com o avanço real (0,1035″ por órbita, 43″ por século) |
| 9–10 | o espaço cai — modelo do rio (Hamilton & Lisle 2008): Schwarzschild em Gullstrand–Painlevé, espaço plano escoando a v = √(r_s/r) c; cascas cúbicas de referenciais em queda livre injetadas na borda e carregadas pelo rio. Slide 9: estrela de nêutrons 1,4 M☉, 12 km; slide 10: buraco negro de 6 M☉. Sem botões; arrastar gira; perfil da velocidade do rio e do ritmo de um relógio parado |
| 14 | duas bases: eixos de sabor e de massa girados por θ, relógios de fase de ν₁ e ν₂, medições simuladas em massa (constantes) e em sabor (oscilam) |
| 15 | P(ν_α→ν_β) a dois sabores contra L; faixa mín–máx por pixel quando a oscilação fica rápida |
| 16 | Super-K: sobrevivência de ν_μ contra cos θ_z, assimetria cima/baixo comparada com −0,296 ± 0,048 |
| 26 | geodésicas nulas de Schwarzschild, u″ + u = (3/2) r_s u², RK4 |
| 27 | compacidade r_s/R da Terra ao horizonte; redshift, relógio, desvio exato da luz rasante; perfil de Flamm |
| 36 | fase Φ = (Δm²/2E∞)∫dr/√(1−b²B/r²) (Fornengo et al. 1997) ao longo da órbita, contra a reta plana |
| 37 | lente pontual: franja por autoestado de massa ∝ m_k²Δb²/4E — sensível à massa absoluta e ao ordenamento |
| 48 | painel do GHOST: perfil de M15-7b, ressonância H, P_H(t) e a frente de perto; a largura da frente é o controle |
| 40 | DUNE: P(ν_μ→ν_e) e P(ν̄) a 1285 km com matéria (Cervera et al. 2000), δ_CP e ordenamento |

Gráficos de dados (não interativos): espectro beta, espectro solar (fluxos B16-GS98, formas
simplificadas), déficit solar (razões em relação ao BP04), plano de fluxos do SNO 2002 e o espectro de
massas com conteúdo de sabor (NuFIT 6.0).

## Imagens

Todas vêm do Wikimedia Commons, em domínio público ou Creative Commons. `assets/img/credits.json`
guarda autor, licença e página de cada uma; o penúltimo slide é gerado dele:

```bash
python3 tools/credits.py
```

## Desenho

Mesma identidade da [página pessoal](https://rafael-lima.pages.dev):
Instrument Serif nos títulos, Literata no texto corrido, Inter Tight nos
rótulos. Os três sabores têm cor fixa em todo o seminário:
ν<sub>e</sub> violeta `#9E8CFF`, ν<sub>μ</sub> turquesa `#56E1D0`,
ν<sub>τ</sub> âmbar `#FFB86B`.

As fontes vêm do Google Fonts — sem rede, o navegador cai nas serifas do sistema. Todo o resto
(imagens, gráficos, dashboards) funciona offline.

## A capa

O fundo é um canvas: uma grade mergulhada num poço gravitacional, com pacotes
de neutrino desviados pelo poço e trocando de cor (sabor) ao longo do caminho.
A fase avança mais devagar onde o potencial é fundo — o fator de lapso —,
então as cores "atrasam" perto do centro. É ilustração, não integração
de geodésica; os dashboards dos slides seguintes é que farão a conta de verdade.

Com `prefers-reduced-motion` a animação para e a capa mostra um quadro fixo.

## Publicação

Este repositório é a fonte. A cópia que vai ao ar fica em `homepage/site/talks/2026-ebn/`; depois de
editar aqui, sincronize e publique a página pessoal:

```bash
rsync -a --delete --exclude .git --exclude .gitignore --exclude .github --exclude tools \
  --exclude privado --exclude README.md ./ ~/Codes/homepage/site/talks/2026-ebn/
```
