#!/usr/bin/env python3
import json, re, sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]
errors=[]
skill=(R/"ai-skill/SKILL.md").read_text()
manifest=json.loads((R/"ai-skill/manifest.json").read_text())
profile=json.loads((R/"ai-skill/references/authority-profile.json").read_text())
bundle=json.loads((R/"ai-skill/generated/research-bundle-index.json").read_text())
corpus=json.loads((R/"data/manifest.json").read_text())
m=re.search(r"^version:\s*([^\s]+)",skill,re.M)
if (m.group(1) if m else None)!=manifest.get("skill_version"): errors.append("skill/manifest version mismatch")
if manifest.get("skill_version")!="0.3.1": errors.append("skill must implement 0.3.1 contract")
if profile.get("current_state",{}).get("objects")!=len(corpus.get("objects",[])): errors.append("authority profile object count stale")
if any(r.get(k) is not None for r in corpus.get("objects",[]) for k in ("transcription","transliteration","translation")): errors.append("current acquisition corpus contains unchecked reading")
if not bundle.get("contract",{}).get("preserve_rights"): errors.append("rights firewall missing")
for p in ("LICENSE","LICENSE-CODE","LICENSE-CONTENT.md","LICENSING.md","NOTICE","research/pre-expert-maximum.json"):
    if not (R/p).exists(): errors.append("missing "+p)
if errors:
    print("\n".join(errors)); sys.exit(1)
print(f"Egyptian AI contract PASS: {len(corpus['objects'])} objects; pre-annotation rights firewall active")
