#!/usr/bin/env python3
"""Generate the French + pictogram WILDFIRE teaching sheet (A4).

Writes an HTML file next to this script; print it to PDF from a browser at A4,
100% scale. The committed WILDFIRE_FR_teaching_sheet.pdf was produced this way.
"""
from pathlib import Path

NAMES_FR = {1: "Lune", 2: "Feuille", 3: "Vague", 4: "Flamme", 5: "Œil",
            6: "Masque", 7: "Clé", 8: "Étoile", 9: "Couronne"}

COLORS = {1: "#2E2C5F", 2: "#3E7A3E", 3: "#1577B5", 4: "#D83A22",
          5: "#169488", 6: "#A6328C", 7: "#B98A2A", 8: "#E0A91F", 9: "#5E3A9E"}

GLYPHS = {
    1: '<path fill-rule="evenodd" d="M50 50 m-36 0 a36 36 0 1 0 72 0 a36 36 0 1 0 -72 0 Z M58 50 m-28 0 a28 28 0 1 0 56 0 a28 28 0 1 0 -56 0 Z" fill="{c}"/>',
    2: '<path d="M50 12 C70 30 70 56 50 80 C30 56 30 30 50 12 Z" fill="{c}"/><rect x="48" y="76" width="4" height="12" rx="2" fill="{c}"/>',
    3: '<path d="M14 56 Q32 32 50 56 T86 56" fill="none" stroke="{c}" stroke-width="11" stroke-linecap="round"/>',
    4: '<path fill-rule="evenodd" d="M54 6 C48 30 30 36 30 60 C30 78 42 94 54 94 C69 94 77 78 71 60 C67 48 56 50 59 35 C61 26 58 16 54 6 Z M53 52 C51 61 45 65 45 73 C45 81 49 85 54 85 C60 85 63 79 61 72 C59 64 55 63 53 52 Z" fill="{c}"/>',
    5: '<path d="M12 50 Q50 18 88 50 Q50 82 12 50 Z" fill="none" stroke="{c}" stroke-width="9"/><circle cx="50" cy="50" r="12" fill="{c}"/>',
    6: '<path fill-rule="evenodd" d="M14 40 C24 30 40 30 50 37 C60 30 76 30 86 40 C88 53 79 63 65 64 C57 65 52 59 50 53 C48 59 43 65 35 64 C21 63 12 53 14 40 Z M33 47 m-9 0 a9 6 0 1 0 18 0 a9 6 0 1 0 -18 0 Z M67 47 m-9 0 a9 6 0 1 0 18 0 a9 6 0 1 0 -18 0 Z" fill="{c}"/>',
    7: '<circle cx="50" cy="30" r="16" fill="none" stroke="{c}" stroke-width="10"/><rect x="45" y="44" width="10" height="42" fill="{c}"/><rect x="55" y="66" width="15" height="9" fill="{c}"/>',
    8: '<path d="M50 14 L61 39 L88 42 L67 60 L74 87 L50 72 L26 87 L33 60 L12 42 L39 39 Z" fill="{c}"/>',
    9: '<path d="M18 74 L18 38 L35 53 L50 30 L65 53 L82 38 L82 74 Z" fill="{c}"/>',
}


def glyph(sign, size=40):
    body = GLYPHS[sign].format(c=COLORS[sign])
    return (f'<svg viewBox="0 0 100 100" width="{size}" height="{size}" '
            f'class="gl">{body}</svg>')


def card(sign, size=31, cls="", pip=True):
    """A card face: frame, pip, glyph."""
    p = f'<span class="pip" style="color:{COLORS[sign]}">{sign}</span>' if pip else ''
    return (f'<span class="card {cls}">{p}{glyph(sign, size)}</span>')


def legend():
    out = []
    for s in range(1, 10):
        out.append(
            f'<div class="lg"><div>{glyph(s, 20)}</div>'
            f'<div class="lgn" style="color:{COLORS[s]}">{s} · {NAMES_FR[s]}</div></div>')
    return "".join(out)


ARROW = ('<svg class="arw" viewBox="0 0 40 24" width="34" height="20">'
         '<path d="M2 12 H30 M23 5 L31 12 L23 19" fill="none" stroke="#5a5348" '
         'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>')

FLIP = ('<svg class="arw" viewBox="0 0 44 26" width="40" height="24">'
        '<path d="M6 17 A14 12 0 1 1 20 21" fill="none" stroke="#D83A22" '
        'stroke-width="3" stroke-linecap="round"/>'
        '<path d="M22 14 L20 22 L12 20" fill="none" stroke="#D83A22" '
        'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
        '</svg>')

HTML = f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>WILDFIRE — règles</title>
<style>
@page {{ size: A4; margin: 9mm 11mm; }}
* {{ box-sizing: border-box; }}
body {{ font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  color:#222; background:#FCFAF4; margin:0; font-size:9.4pt; line-height:1.26; }}
.page {{ page-break-after: always; }}
.page:last-child {{ page-break-after: auto; }}
h1 {{ font-size:22pt; margin:0 0 0.8mm; letter-spacing:.06em; color:#D83A22; }}
h2 {{ font-size:10pt; margin:2.8mm 0 1.2mm; letter-spacing:.12em;
  text-transform:uppercase; color:#5a5348; border-bottom:1px solid #D8D2C4;
  padding-bottom:0.8mm; }}
.sub {{ font-size:9.8pt; color:#5a5348; margin:0 0 1mm; }}
.tag {{ font-size:8.4pt; color:#8a8272; margin:0 0 1.5mm; }}
p {{ margin:0 0 1.4mm; }}
.card {{ display:inline-flex; align-items:center; justify-content:center;
  position:relative; width:12mm; height:16mm; background:#FCFAF4;
  border:1px solid #D8D2C4; border-radius:2mm; vertical-align:middle;
  margin:0 1mm; }}
.card.sm {{ width:10mm; height:13.5mm; }}
.card.tgt {{ border:2px solid #D83A22; }}
.pip {{ position:absolute; top:0.6mm; left:1.2mm; font-size:7.5pt; font-weight:700; }}
.row {{ display:flex; align-items:center; flex-wrap:wrap; gap:1mm; margin:1mm 0 2mm; }}
.step {{ display:flex; gap:2.5mm; margin:0 0 2mm; align-items:flex-start; }}
.num {{ flex:0 0 6mm; height:6mm; border-radius:50%; background:#D83A22;
  color:#fff; font-weight:700; font-size:9pt; display:flex;
  align-items:center; justify-content:center; margin-top:.6mm; }}
.stxt {{ flex:1; }}
.stxt b {{ color:#D83A22; }}
.lgrid {{ display:grid; grid-template-columns:repeat(9,1fr); gap:1mm;
  text-align:center; margin-top:1mm; }}
.lgn {{ font-size:6.8pt; font-weight:700; margin-top:.5mm; }}
.note {{ background:#F3EFE4; border-left:3px solid #B98A2A; padding:1.4mm 2.4mm;
  font-size:8.4pt; margin:1.4mm 0 0; }}
.cols {{ display:grid; grid-template-columns:1fr 1fr; gap:6mm; }}
.foot {{ margin-top:2mm; font-size:8pt; color:#8a8272; font-style:italic;
  text-align:center; }}
.lbl {{ font-size:8pt; color:#8a8272; text-align:center; width:100%;
  margin-top:.5mm; }}
.grp {{ display:flex; flex-direction:column; align-items:center; }}
table {{ border-collapse:collapse; font-size:8.8pt; width:100%; }}
td, th {{ border:1px solid #D8D2C4; padding:1.2mm 2mm; text-align:center; }}
th {{ background:#F3EFE4; font-size:8.5pt; letter-spacing:.04em; }}
</style></head><body>

<div class="page">
<h1>WILDFIRE</h1>
<p class="sub"><b>6 joueurs · 10 minutes ·</b> Videz votre main avant les autres.</p>
<p class="tag">Les mots écrits sur les cartes ne servent à rien. Seuls comptent
le <b>dessin</b> et le <b>chiffre</b>.</p>

<h2>Le paquet</h2>
<div class="cols">
<div>
<p>36 cartes. <b>Chaque carte a deux faces</b>, chacune avec un signe différent.
Chaque paire de signes existe sur une seule carte.</p>
<div class="row">
  <div class="grp">{card(4)}<div class="lbl">recto</div></div>
  {FLIP}
  <div class="grp">{card(8)}<div class="lbl">verso</div></div>
  <div style="margin-left:4mm">= une seule carte</div>
</div>
</div>
<div>
<p><b>Mise en place :</b> mélangez en retournant des paquets au hasard.</p>
<table>
<tr><th>Chaque joueur</th><th>Au centre</th><th>La réserve</th></tr>
<tr><td><b>5 cartes</b> en main</td><td><b>2 cartes</b> = les deux feux</td>
<td><b>4 cartes</b> visibles</td></tr>
</table>
<p style="margin-top:1.5mm">Les deux feux montrent chacun un signe : ce sont les
<b>deux cibles</b>. On joue dans le sens des aiguilles d'une montre.</p>
</div>
</div>

<h2>Votre tour — poser, puis retourner</h2>
<p style="margin-bottom:1.5mm"><b>Une seule carte par tour.</b></p>

<div class="step"><div class="num">1</div><div class="stxt">
<b>Posez</b> une carte de votre main sur <b>l'un des deux feux</b>. La face que
vous montrez doit être <b>le même signe que ce feu</b>. Les deux faces de vos
cartes sont utilisables — tournez-les dans la main autant que vous voulez.
<div class="row">
  <div class="grp">{card(4, cls="tgt")}<div class="lbl">le feu</div></div>
  {ARROW}
  <div class="grp">{card(4)}<div class="lbl">votre carte,<br>face Flamme</div></div>
</div>
</div></div>

<div class="step"><div class="num">2</div><div class="stxt">
<b>Retournez-la immédiatement</b>, sur place. Son autre signe apparaît : c'est
la <b>nouvelle cible</b> pour le joueur suivant.
<div class="row">
  <div class="grp">{card(4)}<div class="lbl">posée</div></div>
  {FLIP}
  <div class="grp">{card(8, cls="tgt")}<div class="lbl">nouvelle cible</div></div>
</div>
<span style="font-size:8.4pt;color:#5a5348">Décalez les cartes en ligne, sans les empiler : l'histoire de la partie doit rester visible.</span>
</div></div>

<div class="step"><div class="num">3</div><div class="stxt">
<b>Vous ne pouvez pas — ou ne voulez pas ?</b> Prenez les <b>2 cartes du dessus
de la réserve</b> dans votre main. Les cibles ne changent pas.
<div class="note" style="margin-top:1.5mm">Réserve vide : ôtez la carte la plus
récente du feu le plus haut, ramassez le reste de cette ligne, retournez le tas
et posez-le à côté — voilà la nouvelle réserve. Remettez la carte récente en
place ; les cibles ne changent pas.</div>
</div></div>

<h2>Le miroir</h2>
<div class="cols">
<div>
<p>Si, à la fin de votre tour, <b>les deux feux montrent le même signe</b>, vous
avez fait un <b>miroir</b> : le joueur à votre gauche <b>passe son tour</b>.</p>
<p>Il n'est pas sans défense : en passant, il <b>retourne la carte du dessus</b>
d'un des deux feux, ce qui casse le miroir et choisit une nouvelle cible.</p>
<p style="font-size:8.4pt;color:#5a5348">Une seule carte du paquet peut faire ça à
un instant donné : celle qui porte les deux signes affichés. Regardez les deux
feux et demandez-vous si vous l'avez en main.</p>
</div>
<div>
<div class="row" style="margin-top:0">
  <div class="grp">{card(6, cls="tgt")}<div class="lbl">feu 1</div></div>
  <div class="grp">{card(6, cls="tgt")}<div class="lbl">feu 2</div></div>
  <div style="margin-left:3mm">→ miroir : le voisin de gauche passe</div>
</div>
<div class="note">Un miroir ne peut jamais sauter deux joueurs de suite.
Prendre des cartes dans la réserve ne fait jamais de miroir.</div>
</div>
</div>

<h2>Finir</h2>
<p>Quand il ne vous reste <b>qu'une seule carte</b>, annoncez
« <b>WILDFIRE&nbsp;!</b> » à la fin de ce tour. Oublié, et repéré avant votre
tour suivant : prenez 2 cartes de la réserve.</p>
<p>Posez votre dernière carte (poser <i>et</i> retourner, comme toujours) et vous
<b>gagnez</b>. Les autres peuvent continuer pour la deuxième place.</p>

<h2>Les neuf signes</h2>
<div class="lgrid">{legend()}</div>

<p class="foot">Prototype — vos remarques comptent plus que la partie.</p>
</div>

<div class="page">
<h1 style="color:#5E3A9E">FAVOURS</h1>
<p class="sub"><b>6 joueurs · 10 minutes ·</b> Offrez ; l'important est d'arriver seul.</p>
<p class="tag">À jouer seulement si WILDFIRE a plu et qu'il reste du temps.</p>

<h2>L'idée en une phrase</h2>
<p><b>Chaque carte de ce jeu nomme deux personnes assises à cette table — et
chaque paire de personnes se trouve sur une seule carte.</b></p>

<h2>Mise en place (6 joueurs)</h2>
<p>Chacun prend un signe, dans l'ordre, en tournant autour de la table :</p>
<div class="row">
{"".join(f'<div class="grp">{card(s, 26, cls="sm")}<div class="lbl">joueur {s}</div></div>' for s in range(1, 7))}
</div>
<p>On ne garde que les cartes ne portant que ces six signes (15 cartes), puis on
<b>retire trois cartes</b> : <b>1–6</b>, <b>2–5</b>, <b>3–4</b>. Il reste 12
cartes, <b>2 par joueur</b> — donc 2 manches. Jouez deux donnes de suite et
additionnez.</p>
<p>Il faut aussi un petit tas de jetons au centre (pièces, bonbons, n'importe quoi).</p>

<h2>Chaque manche, tous en même temps</h2>
<div class="step"><div class="num">1</div><div class="stxt">
Choisissez <b>une carte</b> de votre main, sans la montrer.</div></div>
<div class="step"><div class="num">2</div><div class="stxt">
À trois, <b>donnez-la</b> : posez-la face visible devant <b>l'une des deux
personnes inscrites dessus</b>, en montrant <b>le signe de cette personne</b>.
On ne se donne jamais rien à soi-même.</div></div>
<div class="step"><div class="num">3</div><div class="stxt">
<b>Une seule</b> carte reçue → elle est <b>acceptée</b> : le receveur la garde
devant lui, et <b>le donneur prend un jeton</b>.<br>
<b>Deux cartes ou plus</b> → le receveur est débordé : <b>tout est refusé</b>.
Les cartes vont dans une rangée commune au milieu, hors jeu.</div></div>

<h2>Score</h2>
<p>Cartes devant vous <b>+</b> jetons en main. Le plus haut gagne. Égalité :
celui qui a reçu le plus de cartes.</p>
<div class="note">Sans jetons : une carte refusée revient à son donneur, posée
<b>de travers</b> devant lui, et vaut <b>−1</b>.</div>

<h2>Les neuf signes</h2>
<div class="lgrid">{legend()}</div>
</div>

</body></html>
"""

OUT = Path(__file__).with_name("WILDFIRE_FR_teaching_sheet.html")
OUT.write_text(HTML, encoding="utf-8")
print(f"wrote {OUT} - open it and print to PDF at A4, 100% scale")
