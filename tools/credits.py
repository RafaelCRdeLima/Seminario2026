"""Regenera o slide de créditos a partir de assets/img/credits.json.

    python3 tools/credits.py
"""
import html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
LABEL = {
    'pauli': 'Wolfgang Pauli', 'pauli-letter': 'Carta de Pauli, 1930', 'fermi': 'Enrico Fermi',
    'cowan-reines': 'Cowan e Reines', 'davis': 'Raymond Davis Jr.', 'homestake-tank': 'Tanque de Homestake',
    'pontecorvo': 'Bruno Pontecorvo', 'pmt': 'Fotomultiplicadora de 50 cm', 'kajita': 'Takaaki Kajita',
    'mcdonald': 'Arthur B. McDonald', 'snoplus': 'SNO+', 'standard-model': 'Modelo Padrão',
    'sun': 'O Sol (SDO)', 'einstein': 'Albert Einstein', 'eclipse-1919': 'Eclipse de 1919',
    'schwarzschild': 'Karl Schwarzschild', 'm87': 'M87*', 'sgra': 'Sgr A*', 'ligo-gw150914': 'GW150914',
    'psr1913': 'PSR B1913+16', 'crab': 'Nebulosa do Caranguejo', 'sn1987a': 'SN 1987A', 'wr124': 'WR 124 (JWST)',
    'grb-mechanism': 'Mecanismo de GRB', 'grb-illustration': 'Ilustração de GRB', 'icecube-lab': 'IceCube Lab',
    'icecube-schematic': 'Esquema do IceCube', 'neutron-star': 'Estrela de nêutrons (ilustração)',
    'juno': 'JUNO', 'hyperk': 'Hyper-Kamiokande', 'protodune': 'ProtoDUNE',
}
meta = json.loads((ROOT / 'assets/img/credits.json').read_text())
used = (ROOT / 'index.html').read_text()
rows = []
for key, m in meta.items():
    if pathlib.Path(m['file']).name not in used:
        continue
    artist = re.sub(r'\s+', ' ', m['artist']).strip() or 'autor desconhecido'
    if len(artist) > 90:
        artist = artist[:88].rsplit(' ', 1)[0] + '…'
    lic = m['license'].replace('Public domain', 'domínio público')
    rows.append(f'<p class="ref" style="break-inside: avoid; margin: 0 0 6px"><a href="{m["page"]}"><b>{html.escape(LABEL.get(key, key))}</b></a> — {html.escape(artist)} · {html.escape(lic)}</p>')
block = '<!--CREDITS-->\n    ' + '\n    '.join(rows) + '\n    <!--/CREDITS-->'
out = re.sub(r'<!--CREDITS-->.*?<!--/CREDITS-->', lambda _: block, used, flags=re.S)
(ROOT / 'index.html').write_text(out)
print(len(rows), 'créditos')
