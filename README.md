# Neutrinos em espaço-tempo curvo

Seminário na **II Escola Brasileira de Neutrinos** — sexta, 02 de outubro de 2026.
Rafael C. R. de Lima · Departamento de Física · UDESC/CCT · Joinville.

**No ar:** <https://rafaelcrdelima.github.io/Seminario2026/>

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
| ? | atalhos |

O endereço guarda o slide atual (`#3` abre o terceiro). O palco é fixo em
1920×1080 e escala para caber na tela, então o layout é o mesmo no notebook e
no projetor. Para PDF, imprima do navegador: um slide por página.

## Desenho

Mesma identidade da [página pessoal](https://rafael-lima.pages.dev):
Instrument Serif nos títulos, Literata no texto corrido, Inter Tight nos
rótulos. Os três sabores têm cor fixa em todo o seminário:
ν<sub>e</sub> violeta `#9E8CFF`, ν<sub>μ</sub> turquesa `#56E1D0`,
ν<sub>τ</sub> âmbar `#FFB86B`.

As fontes vêm do Google Fonts — sem rede, o navegador cai nas serifas do sistema.

## A capa

O fundo é um canvas: uma grade mergulhada num poço gravitacional, com pacotes
de neutrino desviados pelo poço e trocando de cor (sabor) ao longo do caminho.
A fase avança mais devagar onde o potencial é fundo — o fator de lapso —,
então as cores "atrasam" perto do centro. É ilustração, não integração
de geodésica; os dashboards dos slides seguintes é que farão a conta de verdade.

Com `prefers-reduced-motion` a animação para e a capa mostra um quadro fixo.

## Publicação

`push` na `main` → a Action publica `index.html` e `assets/` no GitHub Pages.
