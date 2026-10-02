#!/usr/bin/env bash
# Gera os PDFs estáticos do deck (um quadro por slide, após ~8 s de animação).
# Uso: tools/pdf.sh   → neutrinos-espaco-tempo-curvo.pdf (PT) e neutrinos-curved-spacetime.pdf (EN)
set -e
cd "$(dirname "$0")/.."
TMP=$(mktemp -d)
shot() { # arquivo slide
  timeout 60 google-chrome --headless=new --disable-gpu --hide-scrollbars --mute-audio \
    --autoplay-policy=no-user-gesture-required --window-size=1920,1080 \
    --virtual-time-budget=8000 --screenshot="$TMP/${1%.html}-$(printf %02d "$2").png" \
    "file://$PWD/$1#$2" >/dev/null 2>&1
}
export -f shot; export TMP
for f in index.html en.html; do
  n=$(grep -c '<section class="slide' "$f")
  seq 1 "$n" | xargs -P 6 -I{} bash -c "shot $f {}"
done
for p in "index neutrinos-espaco-tempo-curvo" "en neutrinos-curved-spacetime"; do
  set -- $p
  for i in "$TMP/$1"-*.png; do convert "$i" -quality 82 "${i%.png}.jpg"; done
  img2pdf "$TMP/$1"-*.jpg -o "$2.pdf" 2>/dev/null || convert "$TMP/$1"-*.jpg "$2.pdf"
  echo "$2.pdf: $(du -h "$2.pdf" | cut -f1)"
done
rm -rf "$TMP"
