"""Rigenera index.html da src/index.template.html e dai loghi in assets/."""
from pathlib import Path
R = Path(__file__).resolve().parent.parent
t = (R / "src/index.template.html").read_text()
kite = (R / "assets/kitusy-kite.svg").read_text().replace("<title>Kitusy</title>", "").replace("<svg ", '<svg aria-hidden="true" ', 1)
logo = (R / "assets/kitusy-logo.svg").read_text().replace('<rect width="600" height="720" fill="#0B2A4A"/>\n', "").replace('width="600" height="720" ', "", 1).replace("<title>Kitusy</title>", "<title>Logo Kitusy</title>").replace("<svg ", '<svg role="img" ', 1)
frag = t.replace("{{KITE}}", kite).replace("{{LOGO}}", logo)
head, body = frag.split("</style>", 1)
full = ('<!doctype html>\n<html lang="it">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<link rel="icon" type="image/svg+xml" href="assets/kitusy-kite.svg">\n' + head + "</style>\n</head>\n<body>" + body + "</body>\n</html>\n")
full = full.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "").replace(":root{\n", "*{box-sizing:border-box}\nbody{margin:0}\n:root{\n", 1)
(R / "index.html").write_text(full)
