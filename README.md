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

55 slides em quatro partes, cada uma com capa própria:

| parte | cor | conteúdo |
|---|---|---|
| I · Neutrinos | violeta | Pauli, Fermi, Cowan–Reines, três sabores, problema solar, Super-K, SNO, MSW, Nobel 2015, Modelo Padrão |
| II · Espaço-tempo curvo | âmbar | Einstein, Sobral 1919, Schwarzschild, objetos compactos, pulsares e LIGO, colapsares |
| III · Neutrinos em espaço-tempo curvo | turquesa | SN 1987A, emissão no poço, fase covariante, lentes, fronteira, DUNE, observatórios |
| IV · GHOST (resultados) | rosa | a frente de choque na ressonância MSW: critério, largura numérica, custo em P_H, viés no DUNE, a banda (t, E) |

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
| 14 | P(ν_α→ν_β) a dois sabores contra L; faixa mín–máx por pixel quando a oscilação fica rápida |
| 15 | Super-K: sobrevivência de ν_μ contra cos θ_z, assimetria cima/baixo comparada com −0,296 ± 0,048 |
| 25 | geodésicas nulas de Schwarzschild, u″ + u = (3/2) r_s u², RK4 |
| 26 | compacidade r_s/R da Terra ao horizonte; redshift, relógio, desvio exato da luz rasante; perfil de Flamm |
| 35 | fase Φ = (Δm²/2E∞)∫dr/√(1−b²B/r²) (Fornengo et al. 1997) ao longo da órbita, contra a reta plana |
| 36 | lente pontual: franja por autoestado de massa ∝ m_k²Δb²/4E — sensível à massa absoluta e ao ordenamento |
| 47 | painel do GHOST: perfil de M15-7b, ressonância H, P_H(t) e a frente de perto; a largura da frente é o controle |
| 39 | DUNE: P(ν_μ→ν_e) e P(ν̄) a 1285 km com matéria (Cervera et al. 2000), δ_CP e ordenamento |

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
rsync -a --delete --exclude .git --exclude .github --exclude tools --exclude README.md \
  ./ ~/Codes/homepage/site/talks/2026-ebn/
```
