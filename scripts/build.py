#!/usr/bin/env python3
"""Build the complete static collection with Python's standard library."""
from pathlib import Path
from html import escape as e
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs'
OUT.mkdir(exist_ok=True)
load = lambda name: json.loads((ROOT / 'content' / name).read_text())
readings, sections, exercises = (load(n) for n in ('readings.json', 'sections.json', 'exercises.json'))
references = load('schedule-references.json')
references.append({'text': 'Wellman, M. P., Tuyls, K., and Greenwald, A. (2025). Empirical Game-Theoretic Analysis: A Survey. Journal of Artificial Intelligence Research 82, pp. 1017–1076.', 'links': [{'url':'https://arxiv.org/abs/2403.04018'}]})
by_id = {r['id']: r for r in readings}
by_ex = {x['id']: x for x in exercises}
assigned = [rid for s in sections for g in s['groups'] for rid in g['readings']]
assert len(by_id) == len(readings) == len(references) == 43
assert sorted(r['source'] for r in readings) == list(range(43))
assert sorted(assigned) == sorted(by_id), 'Each reading must appear once.'
assert sorted(x for s in sections for x in s['exercises']) == sorted(by_ex)
assert all(1 <= r['importance'] <= 5 and 1 <= r['length'] <= 5 for r in readings)

importance = {5:'Essential',4:'Recommended',3:'Useful depth',2:'Optional',1:'Specialist extension'}
lengths = {1:'Under 15 min',2:'15–45 min',3:'1–2 hours',4:'Half a day',5:'A day or more'}
access_notes = {
  0:'The publisher response could not be read automatically. The citation and framing were checked against the supplied materials and the locally available article.',
  8:'The publisher presents an automated-access challenge. Bibliographic details and the abstract were checked through the publisher’s indexed page and the supplied talk.',
  9:'The publisher presents an automated-access challenge. Bibliographic details and the abstract were checked through the publisher’s indexed page and the supplied talk.',
  20:'The publisher response could not be read automatically. The original schedule link is retained; use this as a historical technical reference.',
  22:'The publisher response could not be read automatically. The original schedule link is retained; the reading guidance follows its role in the supplied normative-agency materials.',
  24:'The publisher blocked automated retrieval. The original DOI is retained; this is a background reference for selected topics.',
  31:'The publisher blocked automated retrieval. The original schedule DOI is retained; the annotation is a conceptual guide, not a new full-text review.',
  32:'The publisher blocked automated retrieval. The original schedule DOI is retained; the annotation is a conceptual guide, not a new full-text review.',
  33:'The publisher blocked automated retrieval. The original schedule DOI is retained; the annotation is a conceptual guide, not a new full-text review.',
  34:'The publisher blocked automated retrieval. The original schedule DOI is retained; the annotation is a conceptual guide, not a new full-text review.',
  39:'The DOI destination blocked automated retrieval. An open-access full-text alternative is provided.',
  40:'The DOI destination blocked automated retrieval. An author-preprint alternative is provided.'
}

def dots(value):
    return '<span aria-hidden="true" class="dots">' + '●'*value + '<span class="empty">' + '○'*(5-value) + '</span></span>'

def card(r):
    ref = references[r['source']]
    url = ref['links'][0]['url']
    alt = f'<a href="{e(r["alternate_url"])}">Open-access alternative ↗</a>' if r.get('alternate_url') else ''
    origin = 'Schedule reference' if r['source'] < 42 else 'Added from lecture and worksheet'
    extra = f'<p class="access-note">{e(access_notes[r["source"]])}</p>' if r['source'] in access_notes else ''
    haystack = ' '.join(str(r.get(k,'')) for k in ('title','authors','year','read','note','question'))
    return f'''<article class="reading" id="{r['id']}" data-importance="{r['importance']}" data-length="{r['length']}" data-search="{e(haystack, quote=True)}">
      <div class="reading-heading"><h4><a href="{e(url)}">{e(r['title'])}<span class="external" aria-hidden="true"> ↗</span></a></h4><a class="permalink" href="#{r['id']}" aria-label="Link to {e(r['title'])}">#</a></div>
      <p class="byline">{e(r['authors'])} <span aria-hidden="true">·</span> {e(r['year'])}</p>
      <div class="scores"><span class="importance" aria-label="Importance {r['importance']} of 5: {importance[r['importance']]}">{dots(r['importance'])} {importance[r['importance']]}</span><span class="length" aria-label="Length {r['length']} of 5: {lengths[r['length']]}">{dots(r['length'])} {lengths[r['length']]}</span></div>
      <p class="read-target"><strong>Read:</strong> {e(r['read'])}</p><p>{e(r['note'])}</p>
      <p class="reading-question"><strong>Ask:</strong> {e(r['question'])}</p>
      <details class="citation"><summary>Citation &amp; source</summary><p>{e(ref['text'])}</p><p class="source-links"><a href="{e(url)}">Original reference ↗</a> {alt}</p><p class="source-origin">{origin} · Access reviewed 8 November 2026.</p>{extra}</details>
    </article>'''

def exercise(x):
    return f'''<article class="exercise" id="exercise-{x['id']}"><p class="eyebrow">Exercise · {e(x['time'])}</p><h4>{e(x['title'])}</h4>{x['prompt']}<details class="solution"><summary>Show solution / discussion</summary><div>{x['solution']}</div></details><p class="provenance">{e(x['provenance'])}</p></article>'''

def section(s):
    q = f'<p class="section-question">{e(s["question"])}</p>' if s.get('question') else ''
    connection = f'<p class="connection">{e(s["connection"])}<br><a href="{e(s["material"])}">{e(s["material_label"])} ↗</a></p>' if s.get('connection') else ''
    groups = ''.join(f'<div class="reading-group"><h3>{e(g["title"])}</h3>{"".join(card(by_id[r]) for r in g["readings"])}</div>' for g in s['groups'])
    exs = ''.join(exercise(by_ex[x]) for x in s['exercises'])
    n = sum(len(g['readings']) for g in s['groups'])
    return f'''<details class="topic" id="{s['id']}" {'open' if s['id']=='start-here' else ''}><summary><span class="section-number">{s['number']}</span><h2>{e(s['title'])}</h2><span class="section-count">{n} readings</span><span class="chevron" aria-hidden="true">+</span></summary><div class="topic-body">{q}<p class="section-intro">{e(s['intro'])}</p>{connection}{groups}<div class="exercises">{exs}</div></div></details>'''

def layout(title, body, page='readings', sidebar=''):
    current = lambda p: ' aria-current="page"' if p == page else ''
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light dark"><title>{e(title)} · Iliad Intensive</title><meta name="description" content="A guided multi-agent systems reading collection: 43 annotated references, six topic collections, and eight exercises with solutions."><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/style.css"><script src="assets/app.js" defer></script></head>
<body><a class="skip-link" href="#main">Skip to content</a><header class="topbar"><a class="wordmark" href="index.html"><span class="brand-mark" aria-hidden="true">I</span> ILIAD <span>INTENSIVE</span></a><nav aria-label="Main navigation"><a href="index.html"{current('readings')}>Reading collection</a><a href="schedule.html"{current('schedule')}>Schedule</a><a href="materials.html"{current('materials')}>Materials</a></nav></header><div class="page-shell {'' if sidebar else 'without-sidebar'}">{sidebar}<main id="main">{body}<footer><span>Iliad Intensive · Multi-agent Systems · October 2026</span><a href="materials.html#editorial-notes">Sources &amp; editorial notes</a><a href="#main">Back to top ↑</a></footer></main></div></body></html>'''

toc = ''.join(f'<li><a href="#{s["id"]}"><span>{s["number"]}</span>{e(s["short"])}</a></li>' for s in sections)
sidebar = f'''<aside class="sidebar"><details class="contents" open><summary>In this collection</summary><nav aria-label="Collection contents"><ol>{toc}<li><a href="#closing"><span>↗</span>Closing comparison</a></li></ol></nav></details><div class="sidebar-tools js-only"><button id="toggle-sections" type="button">Expand all collections</button><button id="toggle-solutions" type="button">Show all 8 solutions</button><button id="print" type="button">Print collection</button></div><details class="legend"><summary>Reading scores</summary><p>Importance is relative to this day.</p>{''.join(f'<div class="legend-row">{dots(i)}<span>{importance[i]}</span></div>' for i in range(5,0,-1))}<p>Length estimates cover the suggested reading target, including study time.</p>{''.join(f'<div class="legend-row length">{dots(i)}<span>{lengths[i]}</span></div>' for i in range(1,6))}</details><p class="sidebar-note">Choose a path.<br>You are not expected to read everything.</p></aside>'''
intro = '''<div class="intro"><p class="eyebrow">Iliad Intensive / October 2026</p><h1>Multi-agent systems<span>Reading collection</span></h1><p class="dek">What does each perspective establish?</p><p>Readings on commitments, learning dynamics, AI control, empirical games, and the explanation of agency. Follow the six collections in order, or choose the question you want to investigate.</p><p><strong>Start with Shoham’s research agendas.</strong> Within each collection, readings are in suggested order. Importance and length are scored separately; an essential reading can be a selected section rather than a whole book. The priorities, study-time estimates, and annotations are editorial guidance for this collection.</p><div class="collection-meta"><span><strong>43</strong> readings</span><span><strong>6</strong> topic collections</span><span><strong>8</strong> exercises</span></div>
<details class="reading-route"><summary>A first route through the collection</summary><p>Read the framing first, then choose one or two collections. For a broad orientation, skim these anchors in order and return for the technical details:</p><ol><li><a href="#shoham">Shoham et al.</a> — identify the research question.</li><li><a href="#institutions">Critch et al.</a> — understand conditional commitments.</li><li><a href="#marl-book">Albrecht et al.</a> — establish the learning setup; then <a href="#pair-approximation">Chu</a> and <a href="#fast-slow">Geng</a> for the guest talk.</li><li><a href="#ai-control">The control collection</a> — pair the original paper with untrusted monitoring.</li><li><a href="#egta-survey">Wellman et al.</a> — distinguish payoff error from missing policies.</li><li><a href="#separation-essay">Rosas on separation</a> — compare an optimal-policy description with an implemented mechanism.</li><li><a href="#openai-report">The incident reports</a>, then <a href="#altruism-essay">Rosas on altruism</a> — compare explanations against the evidence.</li></ol></details></div>
<form class="filters js-only" role="search" onsubmit="return false"><div class="search-field"><label for="search">Find a reading</label><input id="search" type="search" placeholder="Title, author, or idea…" autocomplete="off"></div><div><label for="priority">Importance</label><select id="priority"><option value="0">All readings</option><option value="5">Essential · 5</option><option value="4">Recommended · 4–5</option></select></div><div><label for="length">Reading time</label><select id="length"><option value="5">Any length</option><option value="2">Up to 45 minutes</option><option value="3">Up to 2 hours</option></select></div><button type="reset" class="reset">Reset</button><p id="result-count" role="status" aria-live="polite">43 readings · all collections</p></form><p id="no-results" hidden>No readings match these filters. Try a broader term or reset the filters.</p>'''
closing = '''<section class="closing" id="closing"><p class="eyebrow">Closing discussion</p><h2>Put the claims side by side</h2><p>Take one result from each collection. State the object it studies, the claim it supports, and the extra evidence needed to carry it into another setting.</p><div class="table-scroll"><table><caption>What each perspective can establish</caption><thead><tr><th>Perspective</th><th>Typical claim</th><th>Check before extending it</th></tr></thead><tbody><tr><th>Commitment</th><td>A conditional program sustains an outcome.</td><td>Source access, proof or simulation assumptions, and timing.</td></tr><tr><th>Learning dynamics</th><td>An approximation predicts how a population changes.</td><td>Closure assumptions, mixing, and relevant timescales.</td></tr><tr><th>AI control</th><td>A protocol resists a specified set of attacks.</td><td>Threat-model coverage, collusion, and deployment opportunities.</td></tr><tr><th>Empirical games</th><td>A profile has low regret in a measured strategy set.</td><td>Payoff uncertainty and omitted deviations.</td></tr><tr><th>Normative agency</th><td>An optimal policy admits a useful mathematical representation.</td><td>The theorem’s assumptions and evidence about implementation.</td></tr><tr><th>Descriptive explanation</th><td>A mechanism predicts behavior under specified conditions.</td><td>Alternative explanations and discriminating interventions.</td></tr></tbody></table></div><p>For the course’s original closing comparison, see <a href="materials/04-multi-agent-systems.pdf#page=142">“What does each perspective establish?” · PDF page 142</a>. These rows summarize the questions; they are not interchangeable guarantees.</p></section>'''
(OUT / 'index.html').write_text(layout('Multi-agent systems reading collection', intro + ''.join(section(s) for s in sections) + closing, sidebar=sidebar))

schedule_rows = [
 ('10:00–11:00','Part I · Open-source game theory','open-source-game-theory'),
 ('11:00–11:15','Opening game · Chicken and credible commitment','open-source-game-theory'),
 ('11:15–11:30','Break',None),
 ('11:30–12:30','Part II · James Sykes on stochastic dynamics of multi-agent RL','stochastic-dynamics'),
 ('12:30–13:30','Lunch',None),
 ('13:30–14:30','Part III · Morgan Sinclaire on multi-agent AI control','ai-control'),
 ('14:30–15:30','Part IV · Empirical game-theoretic analysis','empirical-game-theory'),
 ('15:30–16:00','Exercises · Empirical game-theoretic analysis','empirical-game-theory'),
 ('16:00–16:15','Break',None),
 ('16:15–16:45','Part V · Descriptive explanations of the Hugging Face incident and emergent altruism','descriptive-explanations'),
 ('16:45–17:15','Exercises and discussion in small groups','descriptive-explanations'),
 ('17:15–17:30','Closing · What does each perspective establish?','closing'),
 ('17:30–17:45','Feedback and quiz',None)
]
rows = ''
for time, title, link in schedule_rows:
    link_html = f'<a href="index.html#{link}">Readings →</a>' if link else '—'
    row_class = 'interval' if title in ('Break', 'Lunch') else ''
    rows += f'<tr class="{row_class}"><th scope="row">{e(time)}</th><td>{e(title)}</td><td>{link_html}</td></tr>'
schedule_html = f'''<div class="intro"><p class="eyebrow">Iliad Intensive / October 2026</p><h1>The day’s schedule</h1><p class="dek">Multi-agent Systems</p><p>Led by Aden Power. Schedule written by Sandy Tanwisuth. Guest talks by James Sykes and Morgan Sinclaire.</p><p>The timetable follows the supplied schedule. The reading collection gives normative agency its own section, preserving a topic listed in the bibliography and covered in the main slide deck.</p></div><div class="table-scroll"><table class="schedule"><caption>Plan for the day · times as supplied, displayed in 24-hour format</caption><thead><tr><th>Time</th><th>Session</th><th>Reading collection</th></tr></thead><tbody>{rows}</tbody></table></div><section class="prose"><h2>Preparation</h2><p>The schedule assumes familiarity with proofs, linear algebra, calculus, elementary real analysis, and probability. Game-theoretic concepts are introduced as needed.</p><p>For reading preparation, begin with <a href="index.html#shoham">Shoham et al.</a> and choose the anchor for the session you want to explore. The collection is more than a day’s reading.</p><h2>Small-group work</h2><p>The schedule highlights robust equilibrium certification (worksheet Exercise 1.1) and observational equivalence (Exercise 3.1). Allow about 20 minutes to work and 10 minutes to compare conclusions. The online collection includes shorter companion versions with collapsible solutions.</p><p><a href="materials/exercises-and-solutions.pdf">Open the original exercises and solutions (PDF) ↗</a></p><h2>The additional agency collection</h2><p>The timetable’s Part IV is empirical game theory, while the bibliography’s “Part IV” is normative agency. <a href="index.html#normative-agency">Collection V</a> retains the latter as a separate reading path without assigning it an invented time slot.</p><p><a href="materials/october-schedule.docx">Download the original schedule (DOCX)</a></p></section>'''
(OUT / 'schedule.html').write_text(layout('Schedule', schedule_html, page='schedule'))

materials = [
 ('01-open-source-game-theory.pdf','Open-source game theory','17 pages · PDF','Collection I'),
 ('02-stochastic-dynamics.pdf','Stochastic Dynamics of Multi-agent Reinforcement Learning','James Sykes · 66 pages · PDF','Collection II'),
 ('03-ai-control.pdf','Multi-agent AI Control','Morgan Sinclaire · 75 pages · PDF','Collection III'),
 ('04-multi-agent-systems.pdf','Multi-agent Systems','166 pages · PDF','Collections IV–VI and closing'),
 ('exercises-and-solutions.pdf','Exercises and solutions','24 pages · PDF','Original full worksheet'),
 ('october-schedule.docx','October schedule','DOCX','Original timetable and 42 references')
]
materials_html = '''<div class="intro"><p class="eyebrow">Iliad Intensive / October 2026</p><h1>Course materials</h1><p class="dek">The source packet, alongside the reading guide.</p><p>These are the six original files from the supplied October archive, with shorter download filenames. The annotated collection links to the publications themselves; third-party readings have not been copied into this repository.</p></div><div class="material-list">'''
materials_html += ''.join(f'<article><div><h2><a href="materials/{filename}">{e(title)} ↗</a></h2><p>{e(metadata)}</p></div><span>{e(connection)}</span></article>' for filename,title,metadata,connection in materials)
materials_html += '''</div><section class="prose" id="editorial-notes"><h2>Sources and editorial choices</h2><p>The schedule’s bibliography supplies 42 references. All appear once in the reading collection. Wellman, Tuyls, and Greenwald’s <a href="https://arxiv.org/abs/2403.04018">Empirical Game-Theoretic Analysis: A Survey</a> is the sole added reference, drawn from the supplied slides and worksheet.</p><p>The six topic collections separate empirical game theory from normative agency. Lanctot et al. is placed with empirical games because of the PSRO connection; it remains a reading from the schedule’s stochastic-dynamics bibliography. Collection numbers refer to this guide, not a relabeling of the source timetable.</p><p>Reading priorities, estimated study times, questions, and annotations were prepared for this guide. They do not claim to be the lecturers’ own rankings. Time scores refer to the suggested target, not necessarily the complete paper or book. Essays, primary reports, empirical studies, and formal results are described according to their different roles.</p><p>The short exercises are companion material. Adaptations of the supplied worksheet and newly written discussion prompts are labeled individually. The original full worksheet remains available above.</p><h2>Reference checks</h2><p>Links and available abstracts or full texts were reviewed on 8 November 2026. Some publisher sites block automated access or return unreadable responses. Original citation links are retained, with access notes in each affected reading’s “Citation &amp; source” disclosure; open alternatives are supplied where checked. An access failure is not evidence that a citation is invalid.</p><p>Bibliographic citations preserve the schedule’s publication information; displayed entries note consequential version differences, including the 2021 update to the provability-logic paper and the later edit to King’s essay. Publisher pages may change after this review.</p><h2>About the format</h2><p>The organization takes inspiration from <a href="https://charlesr-w.github.io/crw-iliad-intensive-oct-2026/notebooks/ami_reading_collection.html">Charles Renshaw-Whitman’s Ambitious Mechinterp and Activation Geometry reading collection</a>: a guided sequence, independent importance and length scores, and exercises with hidden solutions. This site’s code, annotations, and organization were prepared separately for the multi-agent materials.</p><p><a href="reading-collection.md">Download the complete reading guide as Markdown</a> · <a href="readings.json">Download the reading catalog as JSON</a></p></section>'''
(OUT / 'materials.html').write_text(layout('Materials and sources', materials_html, page='materials'))

# A readable, editable companion that preserves the full catalog and citations.
md = ['# Multi-agent systems reading collection','Iliad Intensive · October 2026','43 readings across six topic collections. Importance: 5 essential, 4 recommended, 3 useful depth, 2 optional, 1 specialist extension. Study times are editorial estimates for the suggested target, not full books.','The original schedule contains 42 references. Wellman et al. is added from the lecture and worksheet. See materials.html for provenance and access notes.']
for s in sections:
    md += [f'## {s["number"]}. {s["title"]}',s['intro']]
    for g in s['groups']:
        md += [f'### {g["title"]}']
        for rid in g['readings']:
            r = by_id[rid]; ref = references[r['source']]
            md += [f'#### [{r["title"]}]({ref["links"][0]["url"]})', f'{r["authors"]} · {r["year"]} | Importance {r["importance"]}/5 | Length {r["length"]}/5: {lengths[r["length"]]}', f'**Read:** {r["read"]}',r['note'],f'**Ask:** {r["question"]}',ref['text']]
    for xid in s['exercises']:
        x = by_ex[xid]
        md += [f'### Exercise: {x["title"]}',x['prompt'],'<details><summary>Solution / discussion</summary>\n\n'+x['solution']+'\n\n</details>',x['provenance']]
(OUT / 'reading-collection.md').write_text('\n\n'.join(md)+'\n')
catalog=[]
for r in readings:
    catalog.append({**r,'citation':references[r['source']]['text'],'url':references[r['source']]['links'][0]['url'],'access_note':access_notes.get(r['source'],'Primary page, abstract, or full text available at review. Verification is not a claim of exhaustive full-text review.')})
(OUT / 'readings.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
(OUT / '.nojekyll').touch()
shutil.copytree(ROOT / 'assets',OUT / 'assets',dirs_exist_ok=True)
print(f'Built {OUT}: 43 readings, 6 topic collections, 8 exercises, 3 HTML pages.')
