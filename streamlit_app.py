import streamlit as st

st.set_page_config(page_title="Molecular Mechanisms", page_icon="🧬", layout="wide")

# ---------------------------------------------------------------------------
# Shared CSS variables/classes used by every animation fragment below.
# Change colors/typography once here and every diagram updates.
# ---------------------------------------------------------------------------
COMMON_STYLE = '''
<style>
  :root {
    --t: #2b2f36;
    --text-secondary: #6b7280;
    --text-accent: #2563eb;
    --surface-1: #f4f6f8;
    --surface-2: #e9edf1;
    --border-strong: #94a3b8;
    --border-accent: #2563eb;
  }
  body { font-family: -apple-system, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 6px 4px; color: var(--t); }
  .sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; }
  .ts { font-size: 11px; fill: var(--t); font-family: inherit; }
  .th { font-size: 13px; font-weight: 600; fill: var(--t); font-family: inherit; }
  .c-purple { fill: #C4B5FD; stroke: #6D28D9; stroke-width: 1; }
  .c-gray   { fill: #CBD5E1; stroke: #64748B; stroke-width: 1; }
  .c-teal   { fill: #99F6E4; stroke: #0F6E56; stroke-width: 1; }
  .c-coral  { fill: #FCA5A5; stroke: #B91C1C; stroke-width: 1; }
  .c-amber  { fill: #FDE68A; stroke: #B45309; stroke-width: 1; }
  .c-green  { fill: #86EFAC; stroke: #15803D; stroke-width: 1; }
  .c-red    { fill: #FCA5A5; stroke: #DC2626; stroke-width: 1; }
  button {
    padding: 6px 14px; border-radius: 8px; border: 1px solid #cbd5e1;
    background: #ffffff; cursor: pointer; font-size: 13px; color: var(--t);
  }
  button:hover { background: #f1f5f9; }
  button.active { border-color: var(--border-accent); color: var(--text-accent); font-weight: 600; }
</style>
'''

# ---------------------------------------------------------------------------
# GPCR_GENERAL  (source: gpcr_general.html)
# ---------------------------------------------------------------------------
GPCR_GENERAL = '''
<h2 class="sr-only">Interactive diagram of a GPCR signaling cascade: ligand binding activates a G-protein, which activates adenylyl cyclase, raising cAMP and activating PKA to phosphorylate a target protein.</h2>
<style>
  .stg { opacity: 0.15; transition: opacity .6s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.4s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.55} }
  .drift { animation: drift 2.2s ease-in-out infinite; }
  @keyframes drift { 0%,100%{transform:translateY(0)} 50%{transform:translateY(6px)} }
  @media (prefers-reduced-motion: reduce) { .pulse, .drift { animation: none; } }
  #ligandGroup { transition: transform .8s cubic-bezier(.3,0,.2,1); }
  #ligandGroup.docked { transform: translateY(88px); }
  #pocket { transition: opacity .5s ease, stroke .5s ease; opacity: 0; }
  #pocket.on { opacity: 1; }
  #receptorBody { transition: fill .5s ease, stroke .5s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:14px; }
  #stepLabel { font-size:13px; color:var(--text-secondary); min-width:96px; }
</style>
<svg width="100%" viewBox="0 0 680 480" role="img">
<title>GPCR to PKA signaling cascade</title>
<desc>A ligand binds a G-protein-coupled receptor, triggering GDP to GTP exchange on the G-alpha subunit, which activates adenylyl cyclase to produce cAMP, which activates protein kinase A to phosphorylate a target protein.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<rect x="40" y="150" width="600" height="60" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="214" y="145">Plasma membrane</text>

<rect id="receptorBody" x="120" y="140" width="60" height="80" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<circle id="pocket" cx="150" cy="158" r="14" fill="none" stroke="#EF9F27" stroke-width="2" stroke-dasharray="3 3"/>
<text class="ts" x="150" y="234" text-anchor="middle">GPCR</text>

<g id="ligandGroup">
  <circle id="ligand" cx="150" cy="70" r="10" fill="#EF9F27"/>
  <text id="ligandLabel" class="ts" x="150" y="50" text-anchor="middle">Ligand</text>
</g>
<line id="ligarrow" x1="150" y1="82" x2="150" y2="140" stroke="#EF9F27" stroke-width="1.5" stroke-dasharray="2 3" marker-end="url(#arrow)"/>

<rect x="470" y="140" width="70" height="80" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="505" y="234" text-anchor="middle">Adenylyl cyclase</text>

<g id="gprot">
<circle id="galpha" cx="220" cy="255" r="24" fill-opacity="1" class="c-purple"/>
<text class="th" x="220" y="255" text-anchor="middle" dominant-baseline="central">Ga</text>
<circle cx="270" cy="260" r="18" class="c-gray"/>
<text class="ts" x="270" y="260" text-anchor="middle" dominant-baseline="central">Gb</text>
<circle cx="255" cy="290" r="16" class="c-gray"/>
<text class="ts" x="255" y="290" text-anchor="middle" dominant-baseline="central">Gg</text>
<text id="gdpgtp" class="ts" x="220" y="288" text-anchor="middle">GDP</text>
</g>

<g id="s2" class="stg">
<circle class="drift" cx="500" cy="270" r="5" fill="#378ADD"/>
<circle class="drift" cx="520" cy="290" r="5" fill="#378ADD" style="animation-delay:.3s"/>
<circle class="drift" cx="480" cy="300" r="5" fill="#378ADD" style="animation-delay:.6s"/>
<circle class="drift" cx="510" cy="320" r="5" fill="#378ADD" style="animation-delay:.9s"/>
<text class="ts" x="560" y="295">cAMP rising</text>
</g>

<g id="s3" class="stg">
<rect x="395" y="350" width="140" height="40" rx="8" class="c-teal" stroke-width="0.5"/>
<text class="th" x="465" y="365" text-anchor="middle" dominant-baseline="central">PKA</text>
<text class="ts" x="465" y="382" text-anchor="middle" dominant-baseline="central">catalytic subunit released</text>
</g>

<g id="s4" class="stg">
<rect x="405" y="420" width="120" height="36" rx="8" class="c-coral" stroke-width="0.5"/>
<text class="th" x="465" y="434" text-anchor="middle" dominant-baseline="central">Target</text>
<text class="ts" x="465" y="450" text-anchor="middle" dominant-baseline="central">phosphorylated (P)</text>
</g>
<line id="pkaarrow" x1="465" y1="391" x2="465" y2="418" stroke="var(--t)" stroke-width="1" marker-end="url(#arrow)" class="stg"/>

<line id="gtoAC0" x1="165" y1="222" x2="199" y2="243" stroke="var(--t)" stroke-width="1" marker-end="url(#arrow)"/>
<line id="atoAC" x1="236" y1="234" x2="466" y2="205" stroke="var(--t)" stroke-width="1" class="stg" marker-end="url(#arrow)"/>
<line id="ACtocamp" x1="505" y1="220" x2="505" y2="255" stroke="var(--t)" stroke-width="1" class="stg" marker-end="url(#arrow)"/>
<line id="camptopka" x1="500" y1="330" x2="475" y2="348" stroke="var(--t)" stroke-width="1" class="stg" marker-end="url(#arrow)"/>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — resting",
  "Step 1 of 4 — ligand docks",
  "Step 2 of 4 — G-alpha active, AC on",
  "Step 3 of 4 — cAMP activates PKA",
  "Step 4 of 4 — target phosphorylated"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('ligandGroup').classList.toggle('docked', step >= 1);
  document.getElementById('ligandLabel').textContent = step >= 1 ? 'Ligand (docked)' : 'Ligand';
  document.getElementById('ligarrow').setAttribute('opacity', step >= 1 ? '0' : '1');
  document.getElementById('pocket').classList.toggle('on', step >= 1);
  document.getElementById('receptorBody').setAttribute('stroke', step >= 1 ? '#EF9F27' : 'var(--t)');
  document.getElementById('receptorBody').setAttribute('stroke-width', step >= 1 ? '2' : '1');
  document.getElementById('galpha').classList.toggle('pulse', step === 1);
  document.getElementById('gdpgtp').textContent = step >= 1 ? 'GTP' : 'GDP';
  document.getElementById('atoAC').classList.toggle('on', step >= 2);
  document.getElementById('ACtocamp').classList.toggle('on', step >= 2);
  document.getElementById('s2').classList.toggle('on', step >= 2);
  document.getElementById('camptopka').classList.toggle('on', step >= 3);
  document.getElementById('s3').classList.toggle('on', step >= 3);
  document.getElementById('pkaarrow').classList.toggle('on', step >= 4);
  document.getElementById('s4').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''

# ---------------------------------------------------------------------------
# GPCR_TECHNICAL  (source: gpcr_technical.html)
# ---------------------------------------------------------------------------
GPCR_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of GPCR signaling showing Gs, Gi, and Gq branches, the intrinsic GTPase off-switch, and the PKA R2C2 holoenzyme.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .drift { animation: drift 2s ease-in-out infinite; }
  @keyframes drift { 0%,100%{transform:translateY(0)} 50%{transform:translateY(5px)} }
  @media (prefers-reduced-motion: reduce) { .pulse, .drift { animation: none; } }
  #ligandGroup { transition: transform .7s cubic-bezier(.3,0,.2,1); }
  #ligandGroup.docked { transform: translateY(72px); }
  #Cunit1, #Cunit2 { transition: transform .8s ease; }
  .split #Cunit1 { transform: translate(-40px, 36px); }
  .split #Cunit2 { transform: translate(40px, 36px); }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnGs" onclick="setPath('Gs')">Gs pathway</button>
  <button id="btnGi" onclick="setPath('Gi')">Gi pathway</button>
  <button id="btnGq" onclick="setPath('Gq')">Gq pathway</button>
</div>

<svg width="100%" viewBox="0 0 680 470" role="img">
<title>GPCR Gs/Gi/Gq branching with GTPase off-switch</title>
<desc>A receptor couples to Gs, Gi, or Gq depending on selection. Gs stimulates and Gi inhibits adenylyl cyclase, changing cAMP; Gq activates phospholipase C to produce IP3 and DAG. Intrinsic GTPase activity on G-alpha hydrolyzes GTP back to GDP, returning the switch to its resting state.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<rect x="30" y="120" width="620" height="55" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="184" y="115">Plasma membrane</text>

<rect id="receptorBody" x="100" y="110" width="56" height="76" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<circle id="pocket" cx="128" cy="128" r="12" fill="none" stroke="#EF9F27" stroke-width="2" stroke-dasharray="3 3" opacity="0"/>
<text class="ts" x="128" y="200" text-anchor="middle">GPCR</text>
<g id="ligandGroup">
  <circle id="ligand" cx="128" cy="60" r="9" fill="#EF9F27"/>
  <text id="ligandLabel" class="ts" x="128" y="42" text-anchor="middle">Ligand</text>
</g>
<line id="ligarrow" x1="128" y1="72" x2="128" y2="110" stroke="#EF9F27" stroke-width="1.5" stroke-dasharray="2 3" marker-end="url(#arrow)"/>

<g id="galpha">
<circle id="galphaC" cx="200" cy="225" r="22" class="c-purple"/>
<text class="th" x="200" y="225" text-anchor="middle" dominant-baseline="central">Ga</text>
<text id="nucleotide" class="ts" x="200" y="255" text-anchor="middle">GDP</text>
</g>
<circle cx="245" cy="230" r="16" class="c-gray"/>
<text class="ts" x="245" y="230" text-anchor="middle" dominant-baseline="central">Gb</text>
<circle cx="230" cy="256" r="14" class="c-gray"/>
<text class="ts" x="230" y="256" text-anchor="middle" dominant-baseline="central">Gg</text>

<g id="gsPath">
<rect x="360" y="110" width="66" height="76" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="393" y="200" text-anchor="middle">Adenylyl cyclase</text>
<line id="toAC_s" x1="214" y1="208" x2="358" y2="180" stroke="#639922" stroke-width="1.2" class="stg" marker-end="url(#arrow)"/>
<g id="campUp" class="stg">
<circle class="drift" cx="410" cy="215" r="4" fill="#378ADD"/>
<circle class="drift" cx="425" cy="230" r="4" fill="#378ADD" style="animation-delay:.3s"/>
<circle class="drift" cx="400" cy="235" r="4" fill="#378ADD" style="animation-delay:.6s"/>
<text class="ts" x="393" y="260" text-anchor="middle">cAMP ↑</text>
</g>
</g>

<g id="giPath" class="stg">
<line id="toAC_i" x1="214" y1="208" x2="358" y2="180" stroke="#E24B4A" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#arrow)"/>
<text class="ts" x="393" y="260" text-anchor="middle">cAMP ↓ (inhibited)</text>
</g>

<g id="gqPath" class="stg">
<rect x="500" y="110" width="66" height="76" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="533" y="200" text-anchor="middle">Phospholipase C</text>
<path d="M214 208 Q400 240 498 178" fill="none" stroke="#0F6E56" stroke-width="1.2" marker-end="url(#arrow)"/>
<text class="ts" x="533" y="220" text-anchor="middle">IP3 + DAG</text>
<circle class="drift" cx="515" cy="235" r="4" fill="#1D9E75"/>
<circle class="drift" cx="550" cy="235" r="4" fill="#1D9E75" style="animation-delay:.4s"/>
</g>

<g id="pkaBlock" class="stg">
<g id="pkaGroup" transform="translate(393,320)">
  <rect x="-62" y="-24" width="60" height="24" rx="6" class="c-teal" stroke-width="0.5"/>
  <text class="ts" x="-32" y="-12" text-anchor="middle" dominant-baseline="central">R</text>
  <rect x="2" y="-24" width="60" height="24" rx="6" class="c-teal" stroke-width="0.5"/>
  <text class="ts" x="32" y="-12" text-anchor="middle" dominant-baseline="central">R</text>
  <g id="Cunit1">
    <rect x="-62" y="2" width="60" height="24" rx="6" class="c-coral" stroke-width="0.5"/>
    <text class="ts" x="-32" y="14" text-anchor="middle" dominant-baseline="central">C</text>
  </g>
  <g id="Cunit2">
    <rect x="2" y="2" width="60" height="24" rx="6" class="c-coral" stroke-width="0.5"/>
    <text class="ts" x="32" y="14" text-anchor="middle" dominant-baseline="central">C</text>
  </g>
</g>
<text class="ts" x="322" y="310" text-anchor="end">PKA holoenzyme (R2C2)</text>
<line id="camptopka" x1="405" y1="265" x2="400" y2="296" stroke="var(--t)" stroke-width="1" opacity="0" marker-end="url(#arrow)"/>
</g>

<g id="targetBlock" class="stg">
<rect x="363" y="400" width="60" height="34" rx="8" class="c-amber" stroke-width="0.5"/>
<text class="ts" x="393" y="417" text-anchor="middle" dominant-baseline="central">Target-P</text>
<line id="pkaarrow" x1="393" y1="356" x2="393" y2="398" stroke="var(--t)" stroke-width="1" opacity="0" marker-end="url(#arrow)"/>
</g>

<text id="gtpaseNote" class="ts" x="200" y="290" text-anchor="middle" opacity="0">intrinsic GTPase resets Ga</text>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="hydrolyze()">Trigger GTPase (off-switch)</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 — resting</span>
</div>

<script>
let step = 0;
let path = 'Gs';
const labelsGs = ["Step 0 of 4 — resting","Step 1 of 4 — ligand docks, Ga-GTP forms","Step 2 of 4 — AC activated, cAMP rises","Step 3 of 4 — PKA holoenzyme splits","Step 4 of 4 — target phosphorylated"];
const labelsGi = ["Step 0 of 2 — resting","Step 1 of 2 — ligand docks, Ga-GTP forms","Step 2 of 2 — AC inhibited, cAMP falls"];
const labelsGq = ["Step 0 of 2 — resting","Step 1 of 2 — ligand docks, Ga-GTP forms","Step 2 of 2 — PLC activated, IP3 + DAG produced"];
function maxStep() { return path==='Gs' ? 4 : 2; }
function setPath(p) {
  path = p; step = 0;
  document.querySelectorAll('.rowbtns button').forEach(b=>b.classList.remove('active'));
  document.getElementById('btn'+p).classList.add('active');
  document.getElementById('galphaC').setAttribute('class', p==='Gs' ? 'c-purple' : p==='Gi' ? 'c-red' : 'c-green');
  render();
}
function render() {
  const labels = path==='Gs' ? labelsGs : path==='Gi' ? labelsGi : labelsGq;
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('ligandGroup').classList.toggle('docked', step >= 1);
  document.getElementById('ligandLabel').textContent = step >= 1 ? 'Ligand (docked)' : 'Ligand';
  document.getElementById('ligarrow').setAttribute('opacity', step >= 1 ? '0' : '1');
  document.getElementById('pocket').setAttribute('opacity', step >= 1 ? '1' : '0');
  document.getElementById('receptorBody').setAttribute('stroke', step >= 1 ? '#EF9F27' : 'var(--t)');
  document.getElementById('receptorBody').setAttribute('stroke-width', step >= 1 ? '2' : '1');
  document.getElementById('nucleotide').textContent = step >= 1 ? 'GTP' : 'GDP';
  document.getElementById('galphaC').classList.toggle('pulse', step === 1);
  ['toAC_s','campUp','pkaBlock','targetBlock'].forEach(id => document.getElementById(id).style.display = path==='Gs' ? '' : 'none');
  document.getElementById('giPath').style.display = path==='Gi' ? '' : 'none';
  document.getElementById('gqPath').style.display = path==='Gq' ? '' : 'none';
  // effector is engaged at step 2 (matches the step labels); step 1 = ligand docks + GTP exchange only
  document.getElementById('toAC_s').classList.toggle('on', path==='Gs' && step>=2);
  document.getElementById('giPath').classList.toggle('on', path==='Gi' && step>=2);
  document.getElementById('gqPath').classList.toggle('on', path==='Gq' && step>=2);
  document.getElementById('campUp').classList.toggle('on', path==='Gs' && step>=2);
  document.getElementById('pkaBlock').classList.toggle('on', path==='Gs' && step>=3);
  document.getElementById('pkaGroup').classList.toggle('split', path==='Gs' && step>=3);
  document.getElementById('camptopka').setAttribute('opacity', path==='Gs' && step>=3 ? '1':'0');
  document.getElementById('targetBlock').classList.toggle('on', path==='Gs' && step>=4);
  document.getElementById('pkaarrow').setAttribute('opacity', path==='Gs' && step>=4 ? '1':'0');
  document.getElementById('gtpaseNote').setAttribute('opacity','0');
}
function stepFwd() { if (step < maxStep()) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function hydrolyze() {
  document.getElementById('nucleotide').textContent = 'GDP';
  document.getElementById('gtpaseNote').setAttribute('opacity','1');
  document.getElementById('galphaC').classList.remove('pulse');
  step = 0;
  setTimeout(()=>{ render(); document.getElementById('gtpaseNote').setAttribute('opacity','0'); }, 900);
}
function reset() { step = 0; render(); }
setPath('Gs');
</script>
'''

# ---------------------------------------------------------------------------
# DNA_REPLICATION_GENERAL  (source: dna_replication_general.html)
# ---------------------------------------------------------------------------
DNA_REPLICATION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of DNA replication showing the double helix unwinding at a replication fork and two new strands being synthesized.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #helicase { transition: transform 1s ease; }
  #newTop, #newBot { transition: stroke-dasharray .6s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 380" role="img">
<title>DNA replication fork, general view</title>
<desc>The double helix is unwound by helicase at a replication fork, exposing two template strands. New complementary strands are synthesized by DNA polymerase along each exposed template, producing two identical double helices from one.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<g id="closedHelix">
<line x1="40" y1="150" x2="220" y2="150" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<line x1="40" y1="170" x2="220" y2="170" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
<line x1="60" y1="150" x2="60" y2="170" stroke="var(--t)" stroke-width="1" opacity="0.4"/>
<line x1="90" y1="150" x2="90" y2="170" stroke="var(--t)" stroke-width="1" opacity="0.4"/>
<line x1="120" y1="150" x2="120" y2="170" stroke="var(--t)" stroke-width="1" opacity="0.4"/>
<line x1="150" y1="150" x2="150" y2="170" stroke="var(--t)" stroke-width="1" opacity="0.4"/>
<line x1="180" y1="150" x2="180" y2="170" stroke="var(--t)" stroke-width="1" opacity="0.4"/>
</g>
<text class="ts" x="130" y="130" text-anchor="middle">Parental double helix</text>

<g id="helicase" class="stg">
<circle cx="235" cy="160" r="22" class="c-amber"/>
<text class="ts" x="235" y="160" text-anchor="middle" dominant-baseline="central">Helicase</text>
</g>

<g id="forkGroup" class="stg">
<path id="topStrand" d="M250 158 Q300 130 480 100" stroke="#378ADD" stroke-width="3" fill="none" stroke-linecap="round"/>
<path id="botStrand" d="M250 162 Q300 190 480 220" stroke="#D85A30" stroke-width="3" fill="none" stroke-linecap="round"/>

<g id="polTop" class="stg">
<circle cx="330" cy="112" r="16" class="c-teal"/>
<text class="ts" x="330" y="112" text-anchor="middle" dominant-baseline="central">Pol</text>
<path id="newTop" d="M260 158 Q300 138 460 108" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-dasharray="6 4" stroke-linecap="round"/>
</g>
<g id="polBot" class="stg">
<circle cx="330" cy="205" r="16" class="c-teal"/>
<text class="ts" x="330" y="205" text-anchor="middle" dominant-baseline="central">Pol</text>
<path id="newBot" d="M260 162 Q300 178 440 210" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-dasharray="18 7" stroke-linecap="round"/>
<text class="ts" x="400" y="255" text-anchor="middle">Okazaki fragments (lagging strand)</text>
</g>

<text class="ts" x="470" y="90" text-anchor="middle">Leading strand</text>
</g>

<text class="ts" x="130" y="310" text-anchor="middle" id="labelParent">Original DNA</text>
<text class="ts stg" x="470" y="310" text-anchor="middle" id="labelDaughters">Two identical daughter helices</text>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 — intact helix</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 3 — intact double helix",
  "Step 1 of 3 — helicase unwinds the strands",
  "Step 2 of 3 — polymerase synthesizes new strands",
  "Step 3 of 3 — two daughter helices formed"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('helicase').classList.toggle('on', step >= 1);
  document.getElementById('helicase').classList.toggle('pulse', step === 1);
  document.getElementById('forkGroup').classList.toggle('on', step >= 1);
  document.getElementById('polTop').classList.toggle('on', step >= 2);
  document.getElementById('polBot').classList.toggle('on', step >= 2);
  document.getElementById('labelDaughters').classList.toggle('on', step >= 3);
  document.getElementById('newTop').style.strokeDasharray = step >= 3 ? 'none' : '6 4';
  document.getElementById('newBot').style.strokeDasharray = step >= 3 ? 'none' : '18 7';
}
function stepFwd() { if (step < 3) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''

# ---------------------------------------------------------------------------
# DNA_REPLICATION_TECHNICAL  (source: dna_replication_technical.html)
# ---------------------------------------------------------------------------
DNA_REPLICATION_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of the replisome: topoisomerase, helicase, SSB proteins, primase, DNA polymerase III with sliding clamp, RNase H, and ligase.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #helicase { transition: transform 1s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 700 420" role="img">
<title>Replisome-level DNA replication</title>
<desc>Topoisomerase relieves supercoiling ahead of the fork, helicase unwinds the helix, single-strand binding proteins coat exposed strands, primase lays RNA primers, DNA polymerase III with a sliding clamp extends the leading strand continuously and the lagging strand as Okazaki fragments, and primers are later removed and the fragments sealed by ligase.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<line x1="20" y1="140" x2="120" y2="140" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<line x1="20" y1="160" x2="120" y2="160" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
<line x1="40" y1="140" x2="40" y2="160" stroke="var(--t)" stroke-width="1" opacity="0.4"/>
<line x1="70" y1="140" x2="70" y2="160" stroke="var(--t)" stroke-width="1" opacity="0.4"/>
<line x1="100" y1="140" x2="100" y2="160" stroke="var(--t)" stroke-width="1" opacity="0.4"/>
<text class="ts" x="70" y="120" text-anchor="middle">Ahead of fork</text>

<g id="topo" class="stg">
<circle cx="135" cy="150" r="16" class="c-purple"/>
<text class="ts" x="135" y="150" text-anchor="middle" dominant-baseline="central">Topo</text>
</g>

<g id="helicase" class="stg">
<circle cx="180" cy="150" r="18" class="c-amber"/>
<text class="ts" x="180" y="150" text-anchor="middle" dominant-baseline="central" style="font-size:8px">Helicase</text>
</g>

<g id="forkGroup" class="stg">
<path d="M198 148 Q260 115 480 90" stroke="#378ADD" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M198 152 Q260 185 480 220" stroke="#D85A30" stroke-width="3" fill="none" stroke-linecap="round"/>

<g id="ssb" class="stg">
<circle cx="230" cy="132" r="5" fill="#8B5CF6"/>
<circle cx="250" cy="122" r="5" fill="#8B5CF6"/>
<circle cx="230" cy="170" r="5" fill="#8B5CF6"/>
<circle cx="255" cy="180" r="5" fill="#8B5CF6"/>
<text class="ts" x="240" y="200" text-anchor="middle">SSB proteins</text>
</g>

<g id="primerLead" class="stg">
<path d="M422.4 104.1 L426.4 103.6 L430.4 103.1 L434.4 102.5 L438.5 102.0 L442.5 101.5 L446.7 101.0 L450.8 100.5 L455.0 100.0" stroke="#EF9F27" stroke-width="6" fill="none" stroke-linecap="round"/>
<text class="ts" x="436" y="81" text-anchor="middle">RNA primer</text>
</g>

<g id="polLead" class="stg">
<path id="newLead" d="M274.5 129.7 L281.8 128.0 L289.3 126.3 L297.1 124.7 L305.1 123.0 L313.5 121.4 L322.1 119.7 L330.9 118.1 L340.0 116.5 L349.4 114.9 L359.0 113.3 L368.9 111.7 L379.1 110.2 L389.5 108.6 L400.2 107.1 L411.2 105.6 L422.4 104.1" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<circle cx="269.6" cy="130.9" r="7" class="c-teal"/>
<circle cx="269.6" cy="130.9" r="13" fill="none" stroke="#0F6E56" stroke-width="1.5" stroke-dasharray="2 2"/>
<text class="ts" x="285" y="100" text-anchor="middle">Pol III + clamp</text>
<text class="ts" x="488" y="94" text-anchor="start">Leading (continuous)</text>
</g>

<g id="primerLag" class="stg">
<path d="M274.7 172.0 L278.0 172.9 L281.4 173.8 L284.9 174.6" stroke="#EF9F27" stroke-width="6" fill="none" stroke-linecap="round"/>
<path d="M324.6 184.1 L328.7 185.0 L332.9 185.9 L337.1 186.8" stroke="#EF9F27" stroke-width="6" fill="none" stroke-linecap="round"/>
<path d="M384.8 196.4 L389.7 197.4 L394.6 198.3 L399.6 199.2" stroke="#EF9F27" stroke-width="6" fill="none" stroke-linecap="round"/>
</g>
<g id="polLag" class="stg">
<circle cx="317.0" cy="182.4" r="6" class="c-teal"/>
<circle cx="375.8" cy="194.7" r="6" class="c-teal"/>
</g>
<g id="fragments" class="stg">
<path d="M284.9 174.6 L289.0 175.7 L293.2 176.8 L297.5 177.8 L301.8 178.9 L306.3 179.9 L310.8 181.0 L315.4 182.0 L320.0 183.1" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M337.1 186.8 L342.1 187.9 L347.2 189.0 L352.4 190.0 L357.6 191.1 L362.9 192.2 L368.3 193.3 L373.8 194.3 L379.4 195.4" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<text class="ts" x="488" y="224" text-anchor="start">Lagging (Okazaki fragments)</text>
</g>
<g id="gapFill" style="opacity:0;transition:opacity .5s ease">
<path d="M274.7 172.0 L278.0 172.9 L281.4 173.8 L284.9 174.6" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M320.0 183.1 L324.6 184.1 L328.7 185.0 L332.9 185.9 L337.1 186.8" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M379.4 195.4 L384.8 196.4 L389.7 197.4 L394.6 198.3 L399.6 199.2" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M422.4 104.1 L426.4 103.6 L430.4 103.1 L434.4 102.5 L438.5 102.0 L442.5 101.5 L446.7 101.0 L450.8 100.5 L455.0 100.0" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round"/>
</g>

<g id="ligase" class="stg">
<circle cx="322.2" cy="183.6" r="7" class="c-coral"/>
<text class="ts" x="322" y="214" text-anchor="middle">Ligase seals nicks</text>
</g>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 — intact helix</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 5 — intact helix ahead of the fork",
  "Step 1 of 5 — topoisomerase relieves supercoiling",
  "Step 2 of 5 — helicase unwinds, SSB proteins coat strands",
  "Step 3 of 5 — primase lays RNA primers",
  "Step 4 of 5 — Pol III extends leading (continuous) and lagging (fragments) strands",
  "Step 5 of 5 — primers removed, ligase seals the nicks"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('topo').classList.toggle('on', step >= 1);
  document.getElementById('topo').classList.toggle('pulse', step === 1);
  document.getElementById('helicase').classList.toggle('on', step >= 2);
  document.getElementById('forkGroup').classList.toggle('on', step >= 2);
  document.getElementById('ssb').classList.toggle('on', step >= 2);
  document.getElementById('primerLead').classList.toggle('on', step >= 3);
  document.getElementById('primerLag').classList.toggle('on', step >= 3);
  document.getElementById('primerLead').style.opacity = step >= 5 ? '0' : '';
  document.getElementById('primerLag').style.opacity = step >= 5 ? '0' : '';
  document.getElementById('gapFill').style.opacity = step >= 5 ? '1' : '0';
  document.getElementById('polLead').classList.toggle('on', step >= 4);
  document.getElementById('polLag').classList.toggle('on', step === 4);
  document.getElementById('fragments').classList.toggle('on', step >= 4);
  document.getElementById('ligase').classList.toggle('on', step >= 5);
  document.getElementById('ligase').classList.toggle('pulse', step === 5);
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''

# ---------------------------------------------------------------------------
# MITOSIS_GENERAL  (source: mitosis_general.html)
# ---------------------------------------------------------------------------
MITOSIS_GENERAL = '''
<h2 class="sr-only">Corrected interactive diagram of mitosis where individual sister chromatids separate to opposite poles at anaphase, so each daughter cell receives one copy of each chromosome.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #chrA_c1, #chrA_c2, #chrB_c1, #chrB_c2 { transition: transform 1s cubic-bezier(.3,0,.2,1); }
  #linkA, #linkB, #labelA, #labelB { transition: opacity 0.5s ease, transform 1s cubic-bezier(.3,0,.2,1); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 400" role="img">
<title>Mitosis with correct sister chromatid segregation</title>
<desc>Two chromosomes, blue and red, each duplicated into two identical sister chromatids. At anaphase, each chromosome's own two sister chromatids separate from each other and move to opposite poles, so each resulting daughter cell receives one blue chromatid and one red chromatid — genetically identical to each other and to the parent cell.</desc>

<ellipse id="cellOutline" cx="340" cy="190" rx="220" ry="140" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<text class="ts" x="340" y="40" text-anchor="middle" id="stageLabel">Interphase</text>

<ellipse id="nucleus" cx="340" cy="175" rx="90" ry="55" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>

<g id="chromatin">
<path d="M280 160 Q300 130 320 160 Q340 190 360 160" stroke="#378ADD" stroke-width="2" fill="none" opacity="0.5"/>
<path d="M340 190 Q360 220 380 190" stroke="#D85A30" stroke-width="2" fill="none" opacity="0.5"/>
</g>

<g id="condensed" class="stg">
<!-- Chromosome A (blue) -->
<line id="chrA_c1" x1="305" y1="145" x2="305" y2="195" stroke="#378ADD" stroke-width="7" stroke-linecap="round"/>
<line id="chrA_c2" x1="325" y1="145" x2="325" y2="195" stroke="#378ADD" stroke-width="7" stroke-linecap="round"/>
<line id="linkA" x1="305" y1="170" x2="325" y2="170" stroke="#378ADD" stroke-width="3"/>
<text class="ts" x="315" y="130" text-anchor="middle" id="labelA">Chromosome A</text>

<!-- Chromosome B (red) -->
<line id="chrB_c1" x1="355" y1="145" x2="355" y2="195" stroke="#D85A30" stroke-width="7" stroke-linecap="round"/>
<line id="chrB_c2" x1="375" y1="145" x2="375" y2="195" stroke="#D85A30" stroke-width="7" stroke-linecap="round"/>
<line id="linkB" x1="355" y1="170" x2="375" y2="170" stroke="#D85A30" stroke-width="3"/>
<text class="ts" x="365" y="215" text-anchor="middle" id="labelB">Chromosome B</text>
</g>

<g id="spindle" class="stg">
<circle cx="140" cy="180" r="6" class="c-amber"/>
<circle cx="540" cy="180" r="6" class="c-amber"/>
<text class="ts" x="140" y="160" text-anchor="middle">Pole</text>
<text class="ts" x="540" y="160" text-anchor="middle">Pole</text>
</g>

<g id="newNuclei" class="stg">
<ellipse cx="220" cy="190" rx="60" ry="48" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<ellipse cx="460" cy="190" rx="60" ry="48" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
</g>

<g id="daughterCells" style="opacity:0;transition:opacity .5s ease">
<ellipse cx="225" cy="190" rx="112" ry="125" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<ellipse cx="455" cy="190" rx="112" ry="125" fill="none" stroke="var(--t)" stroke-width="1.5"/>
</g>

<g id="furrow" class="stg">
<line x1="340" y1="50" x2="340" y2="330" stroke="var(--border-strong)" stroke-width="2" stroke-dasharray="5 4"/>
</g>

<g id="daughterLabels" class="stg">
<text class="th" x="220" y="360" text-anchor="middle">Daughter cell 1</text>
<text class="ts" x="220" y="378" text-anchor="middle">1 blue + 1 red — identical to cell 2</text>
<text class="th" x="460" y="360" text-anchor="middle">Daughter cell 2</text>
<text class="ts" x="460" y="378" text-anchor="middle">1 blue + 1 red — identical to cell 1</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 6</span>
</div>

<script>
let step = 0;
const labels = [
  "Interphase — chromatin uncondensed",
  "Prophase — each chromosome condenses; A and B are each ALREADY duplicated (2 identical sister chromatids, same color)",
  "Prometaphase — nuclear envelope breaks down, spindle fibers search for attachment",
  "Metaphase — both chromosomes align at the equator, sister chromatids still joined",
  "Anaphase — sister chromatids separate: ONE blue chromatid and ONE red chromatid go to EACH pole",
  "Telophase — nuclear envelopes reform around each set (1 blue + 1 red apiece)",
  "Cytokinesis — two daughter cells, each with one blue and one red chromosome — genetically identical"
];
function render() {
  document.getElementById('stageLabel').textContent = labels[step];
  document.getElementById('stepLabel').textContent = 'Step ' + step + ' of 6';
  document.getElementById('chromatin').style.opacity = step === 0 ? '1' : '0';
  document.getElementById('nucleus').style.opacity = step <= 1 ? '1' : '0';
  document.getElementById('condensed').classList.toggle('on', step >= 1);
  document.getElementById('spindle').classList.toggle('on', step >= 2 && step <= 4);

  let ax1=0, ay1=0, ax2=0, ay2=0, bx1=0, by1=0, bx2=0, by2=0;
  if (step === 1) {
    ax1=ax2=-20; ay1=ay2=-5; bx1=bx2=20; by1=by2=5;
  } else if (step === 2) {
    ax1=ax2=-12; ay1=ay2=-8; bx1=bx2=10; by1=by2=6;
  } else if (step === 3) {
    ax1=ax2=0; ay1=ay2=0; bx1=bx2=0; by1=by2=0;
  } else if (step === 4) {
    ax1=-140; ay1=0; ax2=170; ay2=0;
    bx1=-170; by1=0; bx2=140; by2=0;
  } else if (step >= 5) {
    ax1=-110; ay1=20; ax2=110; ay2=20;
    bx1=-110; by1=20; bx2=110; by2=20;
  }
  document.getElementById('chrA_c1').style.transform = `translate(${ax1}px, ${ay1}px)`;
  document.getElementById('chrA_c2').style.transform = `translate(${ax2}px, ${ay2}px)`;
  document.getElementById('chrB_c1').style.transform = `translate(${bx1}px, ${by1}px)`;
  document.getElementById('chrB_c2').style.transform = `translate(${bx2}px, ${by2}px)`;
  // centromere bars and labels travel with their (still-joined) chromosome until anaphase
  document.getElementById('linkA').style.transform = step < 4 ? `translate(${ax1}px, ${ay1}px)` : '';
  document.getElementById('linkB').style.transform = step < 4 ? `translate(${bx1}px, ${by1}px)` : '';
  document.getElementById('labelA').style.transform = step < 4 ? `translate(${ax1}px, ${ay1}px)` : '';
  document.getElementById('labelB').style.transform = step < 4 ? `translate(${bx1}px, ${by1}px)` : '';
  document.getElementById('labelA').style.opacity = step >= 4 ? '0' : '1';
  document.getElementById('labelB').style.opacity = step >= 4 ? '0' : '1';
  document.getElementById('linkA').style.opacity = step >= 4 ? '0' : (step >= 1 ? '1' : '0');
  document.getElementById('linkB').style.opacity = step >= 4 ? '0' : (step >= 1 ? '1' : '0');

  document.getElementById('newNuclei').classList.toggle('on', step >= 5);
  document.getElementById('condensed').style.opacity = step >= 5 ? '0.35' : (step>=1 ? '1':'0.12');
  document.getElementById('furrow').classList.toggle('on', step >= 6);
  document.getElementById('daughterLabels').classList.toggle('on', step >= 6);
  document.getElementById('cellOutline').style.opacity = step >= 6 ? '0' : '1';
  document.getElementById('daughterCells').style.opacity = step >= 6 ? '1' : '0';
}
function stepFwd() { if (step < 6) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''

# ---------------------------------------------------------------------------
# TRANSCRIPTION_GENERAL  (source: transcription_general.html)
# ---------------------------------------------------------------------------
TRANSCRIPTION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of transcription: RNA polymerase binds a promoter, unwinds DNA, and synthesizes a complementary mRNA strand before terminating.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #rnapGroup { transition: transform 1.2s ease; }
  .unbound #rnapGroup { transform: translateX(-65px); }
  .elongating #rnapGroup { transform: translateX(180px); }
  .terminated #rnapGroup { transform: translateX(340px); opacity: 0; }
  #mrnaTail { transition: stroke-dashoffset 1.2s ease; }
  #bubble { transition: opacity .5s ease, transform 1.2s ease; }
  .elongating #bubble { transform: translateX(180px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Transcription, general view</title>
<desc>RNA polymerase binds a promoter on DNA, locally unwinds the double helix, and synthesizes a single-stranded mRNA copy of the template strand as it moves along the gene, then releases both the mRNA and the DNA at a terminator.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<line x1="30" y1="150" x2="630" y2="150" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<line x1="30" y1="170" x2="630" y2="170" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
<g id="rungs">
<line x1="70" y1="150" x2="70" y2="170" stroke="var(--t)" stroke-width="1" opacity="0.3"/>
<line x1="140" y1="150" x2="140" y2="170" stroke="var(--t)" stroke-width="1" opacity="0.3"/>
<line x1="210" y1="150" x2="210" y2="170" stroke="var(--t)" stroke-width="1" opacity="0.3"/>
<line x1="280" y1="150" x2="280" y2="170" stroke="var(--t)" stroke-width="1" opacity="0.3"/>
<line x1="350" y1="150" x2="350" y2="170" stroke="var(--t)" stroke-width="1" opacity="0.3"/>
<line x1="420" y1="150" x2="420" y2="170" stroke="var(--t)" stroke-width="1" opacity="0.3"/>
<line x1="490" y1="150" x2="490" y2="170" stroke="var(--t)" stroke-width="1" opacity="0.3"/>
<line x1="560" y1="150" x2="560" y2="170" stroke="var(--t)" stroke-width="1" opacity="0.3"/>
</g>

<rect id="promoterBox" x="90" y="140" width="50" height="40" fill="none" stroke="#EF9F27" stroke-width="1.5" stroke-dasharray="3 3"/>
<text class="ts" x="115" y="198" text-anchor="middle">Promoter</text>

<g id="bubble" class="stg">
<path id="bubbleTop" d="M70 150 Q115 128 160 150" stroke="#378ADD" stroke-width="3" fill="none" stroke-linecap="round"/>
<path id="bubbleBot" d="M70 170 Q115 192 160 170" stroke="#D85A30" stroke-width="3" fill="none" stroke-linecap="round"/>
</g>

<g id="rnapGroup">
<circle cx="115" cy="160" r="24" class="c-purple"/>
<text class="th" x="115" y="160" text-anchor="middle" dominant-baseline="central">RNAP</text>
</g>

<g id="mrna" class="stg">
<path id="mrnaTail" d="M86 112 Q98 134 116 136 C175 100 240 100 294 136" pathLength="100" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-dasharray="100 100" stroke-dashoffset="100"/>
<text class="ts" x="205" y="92" text-anchor="middle">mRNA (growing 5'→3')</text>
</g>

<g id="released" class="stg">
<text class="th" x="470" y="70" text-anchor="middle">mRNA released</text>
<path d="M330 100 Q400 90 460 90" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round"/>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — intact DNA, promoter unbound",
  "Step 1 of 4 — RNA polymerase binds the promoter",
  "Step 2 of 4 — DNA unwinds, mRNA synthesis begins",
  "Step 3 of 4 — polymerase elongates the mRNA along the gene",
  "Step 4 of 4 — termination: mRNA released, DNA reanneals"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('promoterBox').setAttribute('stroke-width', step === 1 ? '2.5' : '1.5');
  document.getElementById('bubble').classList.toggle('on', step >= 2);
  document.getElementById('bubble').style.opacity = step >= 4 ? '0' : '';   // DNA reanneals at termination
  document.getElementById('mrna').classList.toggle('on', step >= 2);
  document.getElementById('mrna').style.opacity = step >= 4 ? '0' : '';     // transcript leaves (shown as "released")
  document.getElementById('mrnaTail').style.strokeDashoffset = step >= 3 ? '0' : step === 2 ? '82.5' : '100';
  document.getElementById('released').classList.toggle('on', step >= 4);
  const svg = document.querySelector('svg');
  svg.classList.toggle('unbound', step === 0);
  svg.classList.toggle('elongating', step === 3);
  svg.classList.toggle('terminated', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''

# ---------------------------------------------------------------------------
# TRANSLATION_GENERAL  (source: translation_general.html)
# ---------------------------------------------------------------------------
TRANSLATION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of translation: a ribosome reads mRNA codons, tRNA delivers matching amino acids, and a polypeptide chain grows until a stop codon triggers release.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #ribosomeGroup { transition: transform 1s ease; }
  #chain, #trnaP, #trnaA { transition: transform 1s ease, opacity .6s ease; }
  #largeSub { transition: opacity .5s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Translation, general view</title>
<desc>A ribosome assembles on mRNA at the start codon, transfer RNAs deliver matching amino acids into the ribosome, peptide bonds link them into a growing polypeptide chain, and a stop codon triggers release of the finished chain.</desc>

<line x1="30" y1="220" x2="650" y2="220" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<g id="codonTicks">
<line x1="150" y1="212" x2="150" y2="228" stroke="var(--t)" stroke-width="1" opacity="0.3"/>
<line x1="200" y1="212" x2="200" y2="228" stroke="var(--t)" stroke-width="1" opacity="0.3"/>
<line x1="250" y1="212" x2="250" y2="228" stroke="var(--t)" stroke-width="1" opacity="0.3"/>
<line x1="300" y1="212" x2="300" y2="228" stroke="var(--t)" stroke-width="1" opacity="0.3"/>
<line x1="350" y1="212" x2="350" y2="228" stroke="var(--t)" stroke-width="1" opacity="0.3"/>
</g>
<text class="ts" x="150" y="245" text-anchor="middle" id="startLabel">AUG (start)</text>
<text class="ts" x="350" y="245" text-anchor="middle" id="stopLabel">UAA (stop)</text>

<g id="ribosomeGroup">
<ellipse id="largeSub" cx="150" cy="180" rx="55" ry="26" class="c-purple" opacity="0"/>
<ellipse id="smallSub" cx="150" cy="212" rx="50" ry="18" class="c-gray"/>
<rect id="siteE" x="90" y="200" width="20" height="16" rx="3" fill="none" stroke="var(--t)" stroke-width="0.5" opacity="0"/>
<rect id="siteP" x="140" y="200" width="20" height="16" rx="3" fill="none" stroke="var(--t)" stroke-width="0.5"/>
<rect id="siteA" x="190" y="200" width="20" height="16" rx="3" fill="none" stroke="var(--t)" stroke-width="0.5" opacity="0"/>
<text class="ts" x="150" y="186" text-anchor="middle">Ribosome</text>
<text class="ts" x="100" y="198" text-anchor="middle" font-size="9" id="lblE" opacity="0">E</text>
<text class="ts" x="150" y="198" text-anchor="middle" font-size="9" id="lblP" opacity="0">P</text>
<text class="ts" x="200" y="198" text-anchor="middle" font-size="9" id="lblA" opacity="0">A</text>
</g>

<g id="trnaP" class="stg">
<circle cx="150" cy="150" r="9" class="c-teal"/>
<text class="ts" x="150" y="135" text-anchor="middle">tRNA</text>
</g>
<g id="trnaA" class="stg">
<circle cx="200" cy="150" r="9" class="c-amber"/>
</g>

<g id="chain" class="stg">
<circle cx="150" cy="105" r="7" class="c-coral"/>
<circle id="aa2" cx="168" cy="95" r="7" class="c-coral" opacity="0"/>
<circle id="aa3" cx="186" cy="90" r="7" class="c-coral" opacity="0"/>
<text class="ts" x="168" y="75" text-anchor="middle" id="chainLbl">Polypeptide chain</text>
</g>

<g id="releaseFactor" class="stg">
<rect x="330" y="195" width="40" height="26" rx="6" class="c-red" stroke-width="0.5"/>
<text class="ts" x="350" y="208" text-anchor="middle" dominant-baseline="central">RF</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 5</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 5 — mRNA alone, start codon marked",
  "Step 1 of 5 — small subunit binds, initiator tRNA pairs with start codon",
  "Step 2 of 5 — large subunit joins, forming the complete ribosome",
  "Step 3 of 5 — tRNA delivers next amino acid into the A site, peptide bond forms",
  "Step 4 of 5 — translocation: the ribosome shifts one codon; the empty tRNA moves to the E site and leaves, freeing the A site for the next tRNA",
  "Step 5 of 5 — many cycles later the stop codon reaches the A site; a release factor binds and the finished polypeptide is released"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('largeSub').setAttribute('opacity', step >= 2 ? '1' : '0');
  document.getElementById('trnaP').classList.toggle('on', step >= 1);
  document.getElementById('siteP').setAttribute('opacity', step >= 1 ? '1' : '0');
  document.getElementById('trnaA').classList.toggle('on', step >= 3 && step < 5);
  document.getElementById('siteA').setAttribute('opacity', step >= 2 ? '1' : '0');
  document.getElementById('siteE').setAttribute('opacity', step >= 4 ? '1' : '0');
  document.getElementById('chain').classList.toggle('on', step >= 3);
  document.getElementById('aa2').setAttribute('opacity', step >= 3 ? '1' : '0');
  document.getElementById('aa3').setAttribute('opacity', step >= 5 ? '1' : '0');
  document.getElementById('releaseFactor').classList.toggle('on', step >= 5);
  document.getElementById('releaseFactor').classList.toggle('pulse', step === 5);
  ['lblE','lblP','lblA'].forEach(id => document.getElementById(id).setAttribute('opacity', step >= 2 ? '1' : '0'));
  // ribosome moves along the mRNA one codon (50 px) per translocation; at step 5 its A site sits on the stop codon (x=350)
  document.getElementById('ribosomeGroup').style.transform = step >= 5 ? 'translateX(150px)' : (step >= 4 ? 'translateX(50px)' : 'translateX(0)');
  // tRNAs stay on their codons: the first tRNA ends up in the E site and leaves; the A-site tRNA becomes the P-site tRNA
  document.getElementById('trnaP').style.opacity = step === 4 ? '0.45' : (step >= 5 ? '0' : '');
  document.getElementById('trnaA').style.transform = step >= 5 ? 'translateX(100px)' : 'none';
  // peptide bond (step 3) moves the chain onto the A-site tRNA; at step 5 it is released and drifts away
  const chain = document.getElementById('chain');
  chain.style.transform = step >= 5 ? 'translate(330px, -20px)' : (step >= 3 ? 'translateX(50px)' : 'none');   // released, drifts free
  document.getElementById('chainLbl').textContent = step >= 5 ? 'Released polypeptide' : 'Polypeptide chain';
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# MEIOSIS_GENERAL  (source: meiosis.html)
# ---------------------------------------------------------------------------
MEIOSIS_GENERAL = '''
<h2 class="sr-only">Corrected interactive diagram of meiosis where homologs (maternal vs paternal copies) separate at anaphase I, and only later do sister chromatids separate at meiosis II, producing four haploid cells.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #matA_c1, #matA_c2, #patA_c1, #patA_c2, #matB_c1, #matB_c2, #patB_c1, #patB_c2 { transition: transform 1s cubic-bezier(.3,0,.2,1); }
  #linkMatA, #linkPatA, #linkMatB, #linkPatB { transition: opacity 0.5s ease, transform 1s cubic-bezier(.3,0,.2,1); }
  #tipMatA2, #tipPatA1 { transition: opacity .5s ease, transform 1s cubic-bezier(.3,0,.2,1); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 420" role="img">
<title>Meiosis with correct homolog then chromatid separation</title>
<desc>Two homologous chromosome pairs: chromosome A (maternal solid blue, paternal light blue) and chromosome B (maternal solid red, paternal light red). At anaphase I, the maternal and paternal homologs of each chromosome separate from each other to opposite poles, while their own sister chromatids stay joined. Only in meiosis II do sister chromatids finally separate, producing four haploid cells, each with a different combination of maternal and paternal chromosomes.</desc>

<ellipse id="cellOutline" cx="340" cy="170" rx="220" ry="130" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<text class="ts" x="340" y="28" text-anchor="middle" id="stageLabel">Diploid cell, homologs unpaired</text>

<line id="matA_c1" x1="290" y1="145" x2="290" y2="185" stroke="#378ADD" stroke-width="6" stroke-linecap="round"/>
<line id="matA_c2" x1="305" y1="145" x2="305" y2="185" stroke="#378ADD" stroke-width="6" stroke-linecap="round"/>
<line id="linkMatA" x1="290" y1="165" x2="305" y2="165" stroke="#378ADD" stroke-width="2.5"/>

<line id="patA_c1" x1="325" y1="145" x2="325" y2="185" stroke="#85B7EB" stroke-width="6" stroke-linecap="round"/>
<line id="patA_c2" x1="340" y1="145" x2="340" y2="185" stroke="#85B7EB" stroke-width="6" stroke-linecap="round"/>
<line id="linkPatA" x1="325" y1="165" x2="340" y2="165" stroke="#85B7EB" stroke-width="2.5"/>
<line id="tipMatA2" x1="305" y1="145" x2="305" y2="157" stroke="#85B7EB" stroke-width="6" stroke-linecap="round" style="opacity:0"/>
<line id="tipPatA1" x1="325" y1="145" x2="325" y2="157" stroke="#378ADD" stroke-width="6" stroke-linecap="round" style="opacity:0"/>

<line id="matB_c1" x1="360" y1="145" x2="360" y2="185" stroke="#D85A30" stroke-width="6" stroke-linecap="round"/>
<line id="matB_c2" x1="375" y1="145" x2="375" y2="185" stroke="#D85A30" stroke-width="6" stroke-linecap="round"/>
<line id="linkMatB" x1="360" y1="165" x2="375" y2="165" stroke="#D85A30" stroke-width="2.5"/>

<line id="patB_c1" x1="395" y1="145" x2="395" y2="185" stroke="#F0997B" stroke-width="6" stroke-linecap="round"/>
<line id="patB_c2" x1="410" y1="145" x2="410" y2="185" stroke="#F0997B" stroke-width="6" stroke-linecap="round"/>
<line id="linkPatB" x1="395" y1="165" x2="410" y2="165" stroke="#F0997B" stroke-width="2.5"/>

<g id="chiasma" class="stg">
<circle cx="315" cy="165" r="4" fill="#EF9F27"/>
<text class="ts" x="315" y="205" text-anchor="middle">Crossing over (chiasma)</text>
</g>

<g id="spindle" class="stg">
<circle cx="140" cy="170" r="6" class="c-amber"/>
<circle cx="540" cy="170" r="6" class="c-amber"/>
</g>

<g id="twoCells" class="stg">
<ellipse cx="220" cy="170" rx="80" ry="60" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<ellipse cx="460" cy="170" rx="80" ry="60" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<text class="ts" x="220" y="250" text-anchor="middle">Maternal A + maternal B</text>
<text class="ts" x="460" y="250" text-anchor="middle">Paternal A + paternal B</text>
</g>

<g id="fourCells" class="stg">
<ellipse cx="130" cy="330" rx="55" ry="42" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<ellipse cx="270" cy="330" rx="55" ry="42" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<ellipse cx="410" cy="330" rx="55" ry="42" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<ellipse cx="550" cy="330" rx="55" ry="42" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<text class="th" x="340" y="390" text-anchor="middle">Four haploid cells — each a different maternal/paternal combination</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 6</span>
</div>

<script>
let step = 0;
const labels = [
  "Diploid cell — each chromosome (A and B) already duplicated; maternal and paternal homologs shown as dark vs light shade",
  "Prophase I — homologous chromosomes pair up (synapsis) and cross over",
  "Metaphase I — homolog pairs (tetrads) align at the equator",
  "Anaphase I — the MATERNAL and PATERNAL homologs separate from EACH OTHER (not sister chromatids — those stay joined)",
  "Telophase I — two haploid cells form: one gets maternal A + maternal B, the other gets paternal A + paternal B",
  "Meiosis II — NOW sister chromatids separate within each cell, like mitosis",
  "Result — four haploid cells, each with a different maternal/paternal combination"
];
function render() {
  document.getElementById('stageLabel').textContent = labels[step];
  document.getElementById('stepLabel').textContent = 'Step ' + step + ' of 6';
  document.getElementById('chiasma').classList.toggle('on', step === 1);
  document.getElementById('spindle').classList.toggle('on', step >= 2 && step <= 3);

  let m = {};
  const ids = ['matA_c1','matA_c2','patA_c1','patA_c2','matB_c1','matB_c2','patB_c1','patB_c2'];
  ids.forEach(id => m[id] = [0,0]);

  if (step === 1) {
    // synapsis: each maternal homolog pairs tightly with its paternal partner
    m.matA_c1=[5,0]; m.matA_c2=[5,0]; m.patA_c1=[-5,0]; m.patA_c2=[-5,0];
    m.matB_c1=[5,0]; m.matB_c2=[5,0]; m.patB_c1=[-5,0]; m.patB_c2=[-5,0];
  } else if (step === 2) {
    // metaphase I: base positions (tetrads aligned at the equator, not yet separating)
  } else if (step === 3) {
    // anaphase I: maternal and paternal homologs migrate toward opposite poles, sisters remain paired
    // (each joined pair kept as a visible group, clear of the pole markers at x=140 / 540)
    m.matA_c1=[-115,0]; m.matA_c2=[-115,0]; m.patA_c1=[130,0]; m.patA_c2=[130,0];
    m.matB_c1=[-150,0]; m.matB_c2=[-150,0]; m.patB_c1=[95,0]; m.patB_c2=[95,0];
  } else if (step === 4) {
    // Telophase I: homologs separated into two cells (cx 220 / 460), sisters still joined
    m.matA_c1=[-100,0]; m.matA_c2=[-100,0]; m.patA_c1=[105,0]; m.patA_c2=[105,0];
    m.matB_c1=[-125,0]; m.matB_c2=[-125,0]; m.patB_c1=[80,0]; m.patB_c2=[80,0];
  } else if (step === 5) {
    // Meiosis II: sister chromatids begin separating, still inside the same two cells
    m.matA_c1=[-125,0]; m.matA_c2=[-40,0]; m.patA_c1=[80,0]; m.patA_c2=[165,0];
    m.matB_c1=[-185,0]; m.matB_c2=[-100,0]; m.patB_c1=[20,0]; m.patB_c2=[105,0];
  } else if (step >= 6) {
    // Cytokinesis II complete: four separate haploid cells (cx 130/270/410/550)
    m.matA_c1=[-170,165]; m.matA_c2=[-45,165]; m.patA_c1=[75,165]; m.patA_c2=[200,165];
    m.matB_c1=[-220,165]; m.matB_c2=[-95,165]; m.patB_c1=[25,165]; m.patB_c2=[150,165];
  }
  ids.forEach(id => {
    document.getElementById(id).style.transform = `translate(${m[id][0]}px, ${m[id][1]}px)`;
  });
  // centromere links and recombinant tips travel with their chromatids
  const tr = id => `translate(${m[id][0]}px, ${m[id][1]}px)`;
  [['linkMatA','matA_c1'],['linkPatA','patA_c1'],['linkMatB','matB_c1'],['linkPatB','patB_c1'],
   ['tipMatA2','matA_c2'],['tipPatA1','patA_c1']].forEach(([el, ch]) => document.getElementById(el).style.transform = tr(ch));
  document.getElementById('tipMatA2').style.opacity = step >= 1 ? '1' : '0';
  document.getElementById('tipPatA1').style.opacity = step >= 1 ? '1' : '0';
  const linksVisible = step < 5;
  document.getElementById('linkMatA').style.opacity = linksVisible ? '1' : '0';
  document.getElementById('linkPatA').style.opacity = linksVisible ? '1' : '0';
  document.getElementById('linkMatB').style.opacity = linksVisible ? '1' : '0';
  document.getElementById('linkPatB').style.opacity = linksVisible ? '1' : '0';

  document.getElementById('twoCells').classList.toggle('on', step === 4 || step === 5);
  document.getElementById('fourCells').classList.toggle('on', step >= 6);
  document.getElementById('cellOutline').style.opacity = step >= 4 ? '0' : '1';
}
function stepFwd() { if (step < 6) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# APOPTOSIS_GENERAL  (source: apoptosis.html)
# ---------------------------------------------------------------------------
APOPTOSIS_GENERAL = '''
<h2 class="sr-only">Interactive diagram of apoptosis with two pathways: the extrinsic pathway triggered by a death ligand, and the intrinsic mitochondrial pathway triggered by internal cellular stress, both converging on the same executioner caspase-3.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .drift { animation: drift 1.6s ease-in-out infinite; }
  @keyframes drift { 0%{transform:translate(0,0)} 100%{transform:translate(40px,-32px)} }
  #cellBody { transition: d 0.8s ease, opacity .6s ease; }
  #bodies { transition: transform 1s ease, opacity .8s ease; transform-box: fill-box; transform-origin: center; }
  .engulfed #bodies { transform: translateX(89px) scale(0.3); opacity: 0; }
  #phagocyte { transition: transform 0.8s ease; }
  .approaching #phagocyte { transform: translateX(-40px); }
  #mitoOutline { transition: stroke-dasharray 0.6s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnExtrinsic" onclick="setMode('extrinsic')">Extrinsic pathway</button>
  <button id="btnIntrinsic" onclick="setMode('intrinsic')">Intrinsic pathway</button>
</div>

<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Apoptosis — extrinsic and intrinsic pathways</title>
<desc>The extrinsic pathway begins when a death ligand binds a surface receptor, activating initiator caspase-8. The intrinsic (mitochondrial) pathway begins with internal cellular stress or DNA damage, which tips the Bcl-2 family balance, permeabilizes the mitochondrial outer membrane, and releases cytochrome c to form the apoptosome, activating initiator caspase-9. Both pathways converge on the same executioner caspase-3, which dismantles the cell into apoptotic bodies that a phagocyte clears.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<ellipse id="cellBody" cx="200" cy="170" rx="90" ry="80" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<circle cx="200" cy="170" r="28" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="3 3"/>
<text class="ts" x="200" y="270" text-anchor="middle" id="nucleusLabel">Nucleus intact</text>

<!-- Extrinsic-only elements -->
<g id="ligand" class="stg">
<circle cx="200" cy="60" r="8" fill="#E24B4A"/>
<text class="ts" x="200" y="42" text-anchor="middle">Death ligand</text>
<line x1="200" y1="70" x2="200" y2="90" stroke="#E24B4A" stroke-width="1.5" marker-end="url(#arrow)"/>
</g>

<g id="caspase8" class="stg">
<circle cx="200" cy="105" r="14" class="c-amber"/>
<text class="ts" x="200" y="105" text-anchor="middle" dominant-baseline="central">C8</text>
</g>

<!-- Intrinsic-only elements -->
<g id="stressSignal" class="stg">
<circle cx="90" cy="60" r="10" fill="#B91C1C"/>
<text class="ts" x="90" y="42" text-anchor="middle">DNA damage / stress (p53)</text>
</g>

<g id="bh3" class="stg">
<circle cx="165" cy="112" r="8" class="c-amber pulse"/>
<text class="ts" x="150" y="103" text-anchor="end">BH3-only proteins</text>
</g>

<ellipse id="mitoOutline" cx="152" cy="142" rx="30" ry="20" fill="none" stroke="var(--t)" stroke-width="1.5" class="stg"/>
<text class="ts" x="130" y="112" text-anchor="middle" id="mitoLabel" class="stg"></text>

<g id="baxbak" class="stg">
<circle cx="140" cy="138" r="5" fill="#E24B4A"/>
<circle cx="164" cy="146" r="5" fill="#E24B4A"/>
<text class="ts" x="110" y="146" text-anchor="end">Bax/Bak — MOMP</text>
</g>

<g id="cytc" class="stg">
<circle class="drift" cx="150" cy="140" r="4" fill="#EF9F27"/>
<circle class="drift" cx="158" cy="148" r="4" fill="#EF9F27" style="animation-delay:.3s"/>
</g>

<g id="apoptosome" class="stg">
<circle cx="200" cy="100" r="16" class="c-purple"/>
<text class="ts" x="200" y="80" text-anchor="middle" font-size="8">Apoptosome</text>
</g>

<g id="caspase9" class="stg">
<circle cx="200" cy="105" r="14" class="c-teal"/>
<text class="ts" x="200" y="105" text-anchor="middle" dominant-baseline="central">C9</text>
</g>

<!-- Shared convergence point -->
<g id="caspase3" class="stg">
<circle cx="260" cy="140" r="14" class="c-red"/>
<text class="ts" x="260" y="140" text-anchor="middle" dominant-baseline="central">C3</text>
<text class="ts" x="279" y="140" text-anchor="start" dominant-baseline="central" id="executionerLabel">Executioner</text>
</g>

<g id="damage" class="stg">
<path d="M170 165 L185 175 M185 165 L170 175" stroke="#E24B4A" stroke-width="2" stroke-linecap="round"/>
<path d="M215 165 L230 175 M230 165 L215 175" stroke="#E24B4A" stroke-width="2" stroke-linecap="round"/>
<text class="ts" x="200" y="200" text-anchor="middle">DNA fragmentation</text>
</g>

<g id="bodies" class="stg">
<circle cx="440" cy="140" r="20" fill="none" stroke="var(--t)" stroke-width="1"/>
<circle cx="480" cy="180" r="16" fill="none" stroke="var(--t)" stroke-width="1"/>
<circle cx="430" cy="195" r="14" fill="none" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="450" y="230" text-anchor="middle">Apoptotic bodies</text>
</g>

<g id="phagocyte" class="stg">
<ellipse cx="580" cy="170" rx="45" ry="35" class="c-teal"/>
<text class="ts" x="580" y="170" text-anchor="middle" dominant-baseline="central" id="phagocyteLabel">Phagocyte</text>
</g>

<g id="engulfNote" class="stg">
<text class="th" x="500" y="270" text-anchor="middle">Bodies engulfed and digested — no inflammation</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 6</span>
</div>

<script>
let step = 0;
let mode = 'extrinsic';
const extrinsicLabels = [
  "Step 0 of 6 — healthy cell, no death signal",
  "Step 1 of 6 — death ligand binds receptor, initiator caspase-8 activates",
  "Step 2 of 6 — caspase-8 activates executioner caspase-3",
  "Step 3 of 6 — caspase-3 fragments DNA, breaks down the cytoskeleton, cell blebs into apoptotic bodies",
  "Step 4 of 6 — a phagocyte approaches the apoptotic bodies",
  "Step 5 of 6 — phagocytosis: the phagocyte engulfs and digests the bodies",
  "Step 6 of 6 — cleared without triggering inflammation"
];
const intrinsicLabels = [
  "Step 0 of 6 — cellular stress or DNA damage detected, often sensed by p53",
  "Step 1 of 6 — pro-apoptotic BH3-only proteins activate, tipping the Bcl-2 family balance",
  "Step 2 of 6 — Bax/Bak oligomerize on the mitochondrial membrane — MOMP — and cytochrome c is released",
  "Step 3 of 6 — cytochrome c + Apaf-1 + caspase-9 assemble into the apoptosome, activating caspase-9, which activates the SAME executioner caspase-3 as the extrinsic pathway",
  "Step 4 of 6 — caspase-3 fragments DNA, breaks down the cytoskeleton, cell blebs into apoptotic bodies",
  "Step 5 of 6 — a phagocyte approaches the apoptotic bodies",
  "Step 6 of 6 — phagocytosis clears them without triggering inflammation"
];
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnExtrinsic').classList.toggle('active', m === 'extrinsic');
  document.getElementById('btnIntrinsic').classList.toggle('active', m === 'intrinsic');
  render();
}
function render() {
  const labels = mode === 'extrinsic' ? extrinsicLabels : intrinsicLabels;
  document.getElementById('stepLabel').textContent = labels[step];
  const svg = document.querySelector('svg');
  ['ligand','caspase8'].forEach(id => document.getElementById(id).style.display = mode === 'extrinsic' ? '' : 'none');
  ['stressSignal','bh3','mitoOutline','baxbak','cytc','apoptosome','caspase9'].forEach(id => document.getElementById(id).style.display = mode === 'intrinsic' ? '' : 'none');

  document.getElementById('ligand').classList.toggle('on', mode === 'extrinsic' && step >= 1);
  document.getElementById('caspase8').classList.toggle('on', mode === 'extrinsic' && step >= 1);
  document.getElementById('caspase8').classList.toggle('pulse', mode === 'extrinsic' && step === 1);

  document.getElementById('stressSignal').classList.toggle('on', mode === 'intrinsic');
  document.getElementById('bh3').classList.toggle('on', mode === 'intrinsic' && step >= 1);
  document.getElementById('mitoOutline').classList.toggle('on', mode === 'intrinsic');
  document.getElementById('mitoOutline').setAttribute('stroke-dasharray', mode === 'intrinsic' && step >= 2 ? '4 3' : '0');
  document.getElementById('baxbak').classList.toggle('on', mode === 'intrinsic' && step >= 2);
  document.getElementById('cytc').classList.toggle('on', mode === 'intrinsic' && step >= 2);
  document.getElementById('apoptosome').classList.toggle('on', mode === 'intrinsic' && step >= 3);
  document.getElementById('caspase9').classList.toggle('on', mode === 'intrinsic' && step >= 3);

  const c3threshold = mode === 'extrinsic' ? 2 : 3;
  document.getElementById('caspase3').classList.toggle('on', step >= c3threshold);
  document.getElementById('caspase3').classList.toggle('pulse', step === c3threshold);
  document.getElementById('executionerLabel').textContent = (mode === 'intrinsic' && step === c3threshold) ? 'Same executioner!' : 'Executioner';

  const dmgThreshold = mode === 'extrinsic' ? 3 : 4;
  const bodiesThreshold = dmgThreshold;
  const phagoThreshold = mode === 'extrinsic' ? 4 : 5;
  const engulfThreshold = mode === 'extrinsic' ? 5 : 6;
  const clearedThreshold = 6;

  document.getElementById('damage').classList.toggle('on', step >= dmgThreshold);
  document.getElementById('cellBody').style.opacity = step >= dmgThreshold ? '0.15' : '1';
  document.getElementById('nucleusLabel').textContent = step >= dmgThreshold ? 'Nucleus fragmented' : 'Nucleus intact';
  document.getElementById('bodies').classList.toggle('on', step >= bodiesThreshold && step < engulfThreshold);
  document.getElementById('phagocyte').classList.toggle('on', step >= phagoThreshold);
  svg.classList.toggle('approaching', step >= phagoThreshold);
  svg.classList.toggle('engulfed', step >= engulfThreshold);
  document.getElementById('phagocyte').classList.toggle('pulse', step === engulfThreshold && step < clearedThreshold);
  document.getElementById('phagocyteLabel').textContent = step >= clearedThreshold ? 'Phagocyte (fed)' : step >= engulfThreshold ? 'Engulfing…' : 'Phagocyte';
  document.getElementById('engulfNote').classList.toggle('on', step >= clearedThreshold);
}
function stepFwd() { if (step < 6) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('extrinsic');
</script>
'''


# ---------------------------------------------------------------------------
# ENDO_EXOCYTOSIS_GENERAL  (source: endo_exocytosis.html)
# ---------------------------------------------------------------------------
ENDO_EXOCYTOSIS_GENERAL = '''
<h2 class="sr-only">Interactive diagram of endocytosis and exocytosis: a switchable view of vesicle formation from the membrane, or vesicle docking and fusion to release cargo.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #vesicle, #vcargo, #coat circle { transition: cy .9s ease, cx .9s ease, r .5s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnEndo" onclick="setMode('endo')">Endocytosis</button>
  <button id="btnExo" onclick="setMode('exo')">Exocytosis</button>
</div>

<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Endocytosis and exocytosis</title>
<desc>Endocytosis: the membrane invaginates around extracellular cargo, coated by clathrin, then pinches off into an intracellular vesicle. Exocytosis: an intracellular vesicle moves to the membrane, docks via SNARE proteins, and fuses to release its cargo outside the cell.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<line x1="30" y1="150" x2="650" y2="150" stroke="var(--border-strong)" stroke-width="2"/>
<text class="ts" x="340" y="135" text-anchor="middle">Plasma membrane</text>
<text class="ts" x="340" y="270" text-anchor="middle">Inside the cell</text>
<text class="ts" x="340" y="40" text-anchor="middle">Outside the cell</text>

<g id="cargoOutside" class="stg">
<circle cx="200" cy="80" r="10" fill="#EF9F27"/>
<text class="ts" x="200" y="62" text-anchor="middle">Cargo</text>
</g>

<path id="membraneDip" d="M150 150 L250 150" stroke="var(--t)" stroke-width="2" fill="none"/>
<g id="coat" class="stg">
<circle id="coat0" cx="178" cy="160" r="4" class="c-purple"/>
<circle id="coat1" cx="184" cy="172" r="4" class="c-purple"/>
<circle id="coat2" cx="200" cy="178" r="4" class="c-purple"/>
<circle id="coat3" cx="216" cy="172" r="4" class="c-purple"/>
<circle id="coat4" cx="222" cy="160" r="4" class="c-purple"/>
<text class="ts" x="236" y="196" text-anchor="start">Clathrin coat (cytoplasmic side)</text>
</g>

<g id="vesicleGroup">
<circle id="vesicle" cx="200" cy="150" r="0" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<circle id="vcargo" cx="200" cy="150" r="0" fill="#EF9F27"/>
</g>

<g id="snare" class="stg">
<rect x="186" y="146" width="28" height="8" rx="3" class="c-teal"/>
<text class="ts" x="200" y="127" text-anchor="middle">SNARE docking</text>
</g>

<g id="released" class="stg">
<circle cx="200" cy="90" r="9" fill="#EF9F27"/>
<text class="ts" x="200" y="72" text-anchor="middle">Cargo released</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0</span>
</div>

<script>
let step = 0;
let mode = 'endo';
const labelsEndo = [
  "Step 0 of 3 — cargo outside, membrane flat",
  "Step 1 of 3 — clathrin coats the membrane, it begins to invaginate",
  "Step 2 of 3 — vesicle pinches off, enclosing the cargo",
  "Step 3 of 3 — vesicle moves into the cytoplasm and uncoats"
];
const labelsExo = [
  "Step 0 of 3 — vesicle with cargo inside the cytoplasm",
  "Step 1 of 3 — vesicle moves to the membrane and docks via SNARE proteins",
  "Step 2 of 3 — vesicle membrane fuses with the plasma membrane",
  "Step 3 of 3 — cargo released outside the cell"
];
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnEndo').classList.toggle('active', m === 'endo');
  document.getElementById('btnExo').classList.toggle('active', m === 'exo');
  render();
}
function render() {
  const labels = mode === 'endo' ? labelsEndo : labelsExo;
  document.getElementById('stepLabel').textContent = labels[step];
  // each mode shows only its own parts (ghosts of the other mode overprinted each other)
  ['cargoOutside','coat'].forEach(id => document.getElementById(id).style.display = mode === 'endo' ? '' : 'none');
  ['snare','released'].forEach(id => document.getElementById(id).style.display = mode === 'exo' ? '' : 'none');
  document.getElementById('cargoOutside').classList.toggle('on', mode === 'endo' && step === 0);
  document.getElementById('coat').classList.toggle('on', mode === 'endo' && step >= 1 && step <= 2);
  document.getElementById('snare').classList.toggle('on', mode === 'exo' && step === 1);
  document.getElementById('released').classList.toggle('on', mode === 'exo' && step === 3);

  // membrane shape: flat / coated pit dipping into the cytoplasm / fusion pore (omega) opening outward
  const FLAT = 'M150 150 L250 150';
  const PIT  = 'M150 150 L178 150 A22 22 0 0 0 222 150 L250 150';
  const PORE = 'M150 150 L190 150 C190 156 178 158 178 170 A22 22 0 0 0 222 170 C222 158 210 156 210 150 L250 150';
  let d = FLAT, r = 0, cy = 150, cr = 0, ccy = 150, coatC = 150;
  if (mode === 'endo') {
    if (step === 1)      { d = PIT; cr = 8; ccy = 160; coatC = 150; }          // cargo sits in the coated pit
    else if (step === 2) { r = 18; cy = 178; cr = 8; ccy = 178; coatC = 178; } // pinched-off coated vesicle just under the membrane
    else if (step === 3) { r = 18; cy = 230; cr = 8; ccy = 230; coatC = 178; } // moves inward; coat is shed where it pinched off and fades
  } else {
    if (step === 0)      { r = 18; cy = 230; cr = 8; ccy = 230; }
    else if (step === 1) { r = 18; cy = 172; cr = 8; ccy = 172; }              // docked just under the membrane via SNAREs
    else if (step === 2) { d = PORE; cr = 8; ccy = 168; }                       // vesicle membrane merges, pore opens outward
  }
  document.getElementById('membraneDip').setAttribute('d', d);
  const set = (el, k, v) => { el.setAttribute(k, v); el.style[k] = v + 'px'; };
  const v = document.getElementById('vesicle'), vc = document.getElementById('vcargo');
  set(v, 'r', r); set(v, 'cy', cy); set(vc, 'r', cr); set(vc, 'cy', ccy);
  const R = coatC === 150 ? 26 : 22;                                            // coat hugs the pit / the vesicle from the cytoplasm side
  [20, 55, 90, 125, 160].forEach((deg, i) => {
    const el = document.getElementById('coat' + i), t = deg * Math.PI / 180;
    set(el, 'cx', +(200 + R * Math.cos(t)).toFixed(1)); set(el, 'cy', +(coatC + R * Math.sin(t)).toFixed(1));
  });
}
function stepFwd() { if (step < 3) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('endo');
</script>
'''


# ---------------------------------------------------------------------------
# ENZYME_KINETICS_GENERAL  (source: enzyme_kinetics.html)
# ---------------------------------------------------------------------------
ENZYME_KINETICS_GENERAL = '''
<h2 class="sr-only">Interactive diagram of enzyme regulation modes: normal catalysis, competitive inhibition at the active site, allosteric inhibition at a distinct site, and allosteric activation.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #substrateGroup { transition: transform 1s ease, opacity .5s ease; }
  .bound #substrateGroup { transform: translate(157px, 0px); }   /* substrate centre 113,150 -> active site 270,150 */
  #product { transition: transform 1s ease, opacity .5s ease; }
  .inSite #product { transform: translate(-160px, 2px); }        /* product formed in the active site, then released */
  #excessSubstrate rect { transition: transform 1s ease; }
  #activeSite { transition: r 0.6s ease, stroke 0.6s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnNormal" onclick="setMode('normal')">Normal</button>
  <button id="btnComp" onclick="setMode('competitive')">Competitive inhibitor</button>
  <button id="btnAlloI" onclick="setMode('alloInhibit')">Allosteric inhibitor</button>
  <button id="btnAlloA" onclick="setMode('alloActivate')">Allosteric activator</button>
</div>

<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Enzyme regulation modes</title>
<desc>Normal catalysis: substrate binds the active site by induced fit and is converted to product. Competitive inhibition: a lookalike molecule binds the same active site, directly blocking substrate. Allosteric inhibition: an inhibitor binds a separate site, distorting the active site so substrate cannot fit, regardless of substrate concentration. Allosteric activation: an activator binds a separate site and improves the active site's fit for substrate, enhancing catalysis.</desc>

<path id="enzymeBody" d="M180 150 Q210 90 280 110 Q340 100 360 150 Q340 200 280 190 Q210 210 180 150 Z" class="c-teal" stroke-width="0.5"/>
<circle id="activeSite" cx="270" cy="150" r="16" fill="none" stroke="#EF9F27" stroke-width="2" stroke-dasharray="3 3"/>
<text class="ts" x="270" y="230" text-anchor="middle">Enzyme</text>

<g id="substrateGroup">
<rect x="100" y="140" width="26" height="20" rx="4" fill="#EF9F27"/>
<text class="ts" x="113" y="122" text-anchor="middle" id="substrateLabel">Substrate</text>
</g>

<g id="competitiveInhibitor" class="stg">
<rect x="258" y="141" width="24" height="18" rx="4" fill="#B91C1C"/>
<text class="ts" x="270" y="94" text-anchor="middle">Lookalike inhibitor</text>
<text class="ts" x="330" y="260" text-anchor="middle">Blocks the same site — beaten by more substrate</text>
</g>

<g id="excessSubstrate" style="opacity:0;transition:opacity .5s ease">
<rect x="96" y="176" width="26" height="20" rx="4" fill="#EF9F27"/>
<rect x="130" y="196" width="26" height="20" rx="4" fill="#EF9F27"/>
<rect x="66" y="196" width="26" height="20" rx="4" fill="#EF9F27"/>
<text class="ts" x="112" y="236" text-anchor="middle">More substrate added</text>
</g>

<g id="product" class="stg">
<circle cx="420" cy="140" r="8" fill="#1D9E75"/>
<circle cx="440" cy="155" r="8" fill="#1D9E75"/>
<text class="ts" x="430" y="185" text-anchor="middle">Product</text>
</g>

<g id="allostericSite" class="stg">
<circle cx="200" cy="180" r="10" fill="none" stroke="#7F77DD" stroke-width="1.5" stroke-dasharray="2 2"/>
<text class="ts" x="200" y="205" text-anchor="middle">Allosteric site</text>
</g>
<g id="inhibitor" class="stg">
<circle cx="200" cy="180" r="9" fill="#E24B4A"/>
<text class="ts" x="270" y="260" text-anchor="middle">Different site — NOT beaten by more substrate</text>
</g>
<g id="activator" class="stg">
<circle cx="200" cy="180" r="9" fill="#1D9E75"/>
<text class="ts" x="270" y="260" text-anchor="middle" id="activatorNote">Active site opens wider — easier binding</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 3</span>
</div>

<script>
let step = 0;
let mode = 'normal';
const labelsNormal = [
  "Step 0 of 3 — substrate approaches the active site",
  "Step 1 of 3 — induced fit: substrate binds, enzyme-substrate complex forms",
  "Step 2 of 3 — reaction catalyzed, product formed",
  "Step 3 of 3 — product released, enzyme resets for another cycle"
];
const labelsComp = [
  "Step 0 of 2 — a lookalike molecule approaches the same active site",
  "Step 1 of 2 — it binds the active site directly, blocking substrate",
  "Step 2 of 2 — reversible: raising substrate concentration can outcompete it (this is why competitive inhibition raises the apparent Km but not Vmax)"
];
const labelsAlloI = [
  "Step 0 of 2 — an inhibitor approaches a site distinct from the active site",
  "Step 1 of 2 — it binds the allosteric site",
  "Step 2 of 2 — the active site is distorted — substrate can't bind no matter how much is added (this lowers Vmax, unlike competitive inhibition)"
];
const labelsAlloA = [
  "Step 0 of 2 — an activator approaches the allosteric site",
  "Step 1 of 2 — it binds, and the active site's shape improves",
  "Step 2 of 2 — substrate now binds more readily — catalysis is enhanced, the opposite effect of an allosteric inhibitor"
];
function maxStep() { return mode === 'normal' ? 3 : 2; }
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnNormal').classList.toggle('active', m === 'normal');
  document.getElementById('btnComp').classList.toggle('active', m === 'competitive');
  document.getElementById('btnAlloI').classList.toggle('active', m === 'alloInhibit');
  document.getElementById('btnAlloA').classList.toggle('active', m === 'alloActivate');
  render();
}
function render() {
  const labels = mode === 'normal' ? labelsNormal : mode === 'competitive' ? labelsComp : mode === 'alloInhibit' ? labelsAlloI : labelsAlloA;
  document.getElementById('stepLabel').textContent = labels[step];
  const svg = document.querySelector('svg');

  // each mode shows only its own parts (other modes' ghost notes overprinted each other)
  const show = (id, yes) => document.getElementById(id).style.display = yes ? '' : 'none';
  show('competitiveInhibitor', mode === 'competitive');
  show('allostericSite', mode === 'alloInhibit' || mode === 'alloActivate');
  show('inhibitor', mode === 'alloInhibit');
  show('activator', mode === 'alloActivate');
  show('product', mode === 'normal');
  document.getElementById('competitiveInhibitor').classList.toggle('on', mode === 'competitive' && step >= 1);
  document.getElementById('allostericSite').classList.toggle('on', (mode === 'alloInhibit' || mode === 'alloActivate') && step >= 0);
  document.getElementById('inhibitor').classList.toggle('on', mode === 'alloInhibit' && step >= 1);
  document.getElementById('activator').classList.toggle('on', mode === 'alloActivate' && step >= 1);
  // reset shared state so nothing leaks from the previous mode
  svg.classList.remove('bound', 'inSite');
  document.getElementById('substrateLabel').textContent = 'Substrate';
  document.getElementById('excessSubstrate').style.opacity = '0';

  if (mode === 'normal') {
    svg.classList.toggle('bound', step >= 1);
    svg.classList.toggle('inSite', step === 2);
    document.getElementById('substrateLabel').textContent = step === 1 ? 'Bound substrate' : 'Substrate';
    document.getElementById('substrateGroup').style.opacity = step >= 2 ? '0' : '1';   // converted into product
    document.getElementById('activeSite').setAttribute('stroke', '#EF9F27');
    document.getElementById('activeSite').setAttribute('r', '16');
    document.getElementById('product').classList.toggle('on', step >= 2);
  } else if (mode === 'competitive') {
    document.getElementById('substrateGroup').style.opacity = step === 1 ? '0.15' : '1';
    document.getElementById('excessSubstrate').style.opacity = step >= 2 ? '1' : '0';   // step 2: substrate concentration raised
    document.getElementById('activeSite').setAttribute('stroke', '#EF9F27');
    document.getElementById('activeSite').setAttribute('r', '16');
    document.getElementById('product').classList.toggle('on', false);
  } else if (mode === 'alloInhibit') {
    // step 1: inhibitor binds; step 2: the active site distorts and substrate can't fit
    document.getElementById('substrateGroup').style.opacity = step >= 2 ? '0.15' : '1';
    document.getElementById('activeSite').setAttribute('stroke', step >= 2 ? '#E24B4A' : '#EF9F27');
    document.getElementById('activeSite').setAttribute('r', step >= 2 ? '10' : '16');
    document.getElementById('product').classList.toggle('on', false);
  } else if (mode === 'alloActivate') {
    document.getElementById('substrateGroup').style.opacity = '1';
    svg.classList.toggle('bound', step >= 2);                                   // step 2: substrate binds the improved site
    if (step >= 2) document.getElementById('substrateLabel').textContent = 'Bound substrate';
    document.getElementById('activeSite').setAttribute('stroke', step >= 1 ? '#1D9E75' : '#EF9F27');
    document.getElementById('activeSite').setAttribute('r', step >= 1 ? '22' : '16');
    document.getElementById('product').classList.toggle('on', false);
  }
}
function stepFwd() { if (step < maxStep()) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('normal');
</script>
'''


# ---------------------------------------------------------------------------
# MEMBRANE_TRANSPORT_GENERAL  (source: membrane_transport.html)
# ---------------------------------------------------------------------------
MEMBRANE_TRANSPORT_GENERAL = '''
<h2 class="sr-only">Interactive diagram of membrane transport modes, each shown as an actual step-through: simple diffusion, facilitated diffusion through a channel, active transport by an ATP-powered pump, and a ligand-gated channel that only opens when a ligand binds.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  #channelProt, #pump, #ligandChannel { opacity: 0; }
  #channelProt.on, #pump.on, #ligandChannel.on { opacity: 1; }
  #pumpFunnel { transition: transform .8s cubic-bezier(.3,0,.2,1); transform-origin: 340px 150px; }
  .flip #pumpFunnel { transform: scaleY(-1); }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #molecule { transition: transform 1s ease, opacity .4s ease; }
  #ligandGroup { transition: transform .8s ease, opacity .4s ease; }
  .docked #ligandGroup { transform: translate(90px, 25px); }   /* ligand 230,80 -> receptor site on the outer face 320,105 */
  #gateTop, #gateBottom { transition: transform 0.8s ease; }
  .gateopen #gateTop { transform: translateY(-16px); }          /* opens a 32px passage — wider than the molecule */
  .gateopen #gateBottom { transform: translateY(16px); }
  #atp { transition: r .4s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnSimple" onclick="setMode('simple')">Simple diffusion</button>
  <button id="btnFacil" onclick="setMode('facil')">Facilitated diffusion</button>
  <button id="btnActive" onclick="setMode('active')">Active transport</button>
  <button id="btnLigand" onclick="setMode('ligand')">Ligand-gated channel</button>
</div>

<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Modes of membrane transport, stepped</title>
<desc>Each transport mode is shown as a sequence: a molecule approaches the membrane, crosses it by a different mechanism depending on the mode, and arrives on the other side. Simple diffusion passes directly through the lipid bilayer. Facilitated diffusion passes through an always-open channel protein. Active transport is pumped through against its gradient, consuming ATP. A ligand-gated channel stays closed until a ligand binds a receptor site, opening the pore only while the ligand remains bound.</desc>

<rect x="280" y="40" width="120" height="220" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="340" y="30" text-anchor="middle">Membrane</text>
<text class="ts" x="140" y="30" text-anchor="middle" id="outsideLabel">Outside — high concentration</text>
<text class="ts" x="540" y="30" text-anchor="middle" id="insideLabel">Inside — low concentration</text>

<g id="channelProt" class="stg">
<rect x="320" y="60" width="40" height="180" rx="16" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="340" y="255" text-anchor="middle">Channel protein (always open)</text>
</g>

<g id="pump" class="stg">
<path d="M340,60 C300,60 300,120 322,150 C300,180 300,240 340,240 C380,240 380,180 358,150 C380,120 380,60 340,60 Z" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1.5"/>
<path id="pumpFunnel" d="M320,85 L360,85 L340,148 Z" fill="#FDE68A" stroke="#B45309" stroke-width="1" opacity="0.85"/>
<text class="ts" x="340" y="255" text-anchor="middle">Pump</text>
<circle id="atp" cx="420" cy="150" r="12" class="c-amber" opacity="0"/>
<text class="ts" x="420" y="150" text-anchor="middle" dominant-baseline="central" id="atpLabel" opacity="0">ATP</text>
</g>

<g id="ligandChannel" class="stg">
<rect x="320" y="60" width="40" height="180" rx="16" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<circle id="receptorSite" cx="320" cy="105" r="10" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="3 3"/>
<rect id="gateTop" x="330" y="140" width="20" height="10" fill="var(--t)" opacity="0.5"/>
<rect id="gateBottom" x="330" y="150" width="20" height="10" fill="var(--t)" opacity="0.5"/>
<text class="ts" x="340" y="255" text-anchor="middle">Ligand-gated channel</text>
<g id="ligandGroup">
<circle id="ligand" cx="230" cy="80" r="9" fill="#EF9F27"/>
<text id="ligandLabel" class="ts" x="218" y="84" text-anchor="end">Ligand</text>
</g>
</g>

<circle id="molecule" cx="120" cy="150" r="10" fill="#1D9E75"/>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 3</span>
</div>

<script>
let step = 0;
let mode = 'simple';
const configs = {
  simple: {
    labels: [
      "Step 0 of 3 — small nonpolar molecule approaches the bilayer",
      "Step 1 of 3 — dissolves directly into the lipid bilayer, no protein needed",
      "Step 2 of 3 — passes through the hydrophobic core",
      "Step 3 of 3 — exits into the cytoplasm, moving down its gradient"
    ]
  },
  facil: {
    labels: [
      "Step 0 of 3 — molecule approaches the channel protein",
      "Step 1 of 3 — enters the channel's pore",
      "Step 2 of 3 — passes through the channel, still no energy required",
      "Step 3 of 3 — exits into the cytoplasm, still down its gradient"
    ]
  },
  active: {
    labels: [
      "Step 0 of 4 — molecule binds the pump on the low-concentration side",
      "Step 1 of 4 — ATP binds the pump",
      "Step 2 of 4 — ATP hydrolyzed, pump changes shape, molecule moves across",
      "Step 3 of 4 — ADP + Pi released, pump resets",
      "Step 4 of 4 — molecule released on the other side, against its gradient"
    ]
  },
  ligand: {
    labels: [
      "Step 0 of 4 — channel closed by default, no ligand bound",
      "Step 1 of 4 — ligand binds the receptor site on the channel's outer face",
      "Step 2 of 4 — binding triggers a conformational change — the gate opens",
      "Step 3 of 4 — while the ligand stays bound, the molecule passes through",
      "Step 4 of 4 — ligand unbinds, the channel closes again — transport stops"
    ]
  }
};
function maxStep() { return mode === 'active' || mode === 'ligand' ? 4 : 3; }
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnSimple').classList.toggle('active', m === 'simple');
  document.getElementById('btnFacil').classList.toggle('active', m === 'facil');
  document.getElementById('btnActive').classList.toggle('active', m === 'active');
  document.getElementById('btnLigand').classList.toggle('active', m === 'ligand');
  document.getElementById('channelProt').classList.toggle('on', m === 'facil');
  document.getElementById('pump').classList.toggle('on', m === 'active');
  document.getElementById('ligandChannel').classList.toggle('on', m === 'ligand');
  document.getElementById('outsideLabel').textContent = m === 'active' ? 'Outside — low concentration' : 'Outside — high concentration';
  document.getElementById('insideLabel').textContent = m === 'active' ? 'Inside — high concentration' : 'Inside — low concentration';
  render();
}
function render() {
  const cfg = configs[mode];
  document.getElementById('stepLabel').textContent = cfg.labels[step];
  const svg = document.querySelector('svg');
  let x = 120;
  if (mode === 'active') {
    x = step === 0 ? 308 : step === 1 ? 320 : step === 2 ? 340 : step === 3 ? 360 : 560;   // step 0: bound at the pump's open face
    document.getElementById('atp').setAttribute('opacity', step === 1 || step === 3 ? '1' : '0');
    document.getElementById('atpLabel').setAttribute('opacity', step === 1 || step === 3 ? '1' : '0');
    document.getElementById('atp').setAttribute('cx', step === 3 ? '400' : '420');
    document.getElementById('atpLabel').setAttribute('x', step === 3 ? '400' : '420');
    document.getElementById('atpLabel').textContent = step === 3 ? 'ADP + Pi' : 'ATP';
    document.getElementById('atp').setAttribute('r', step === 3 ? '26' : '12');   // fit the longer "ADP + Pi" text
    document.getElementById('pump').classList.toggle('flip', step >= 2);
  } else if (mode === 'ligand') {
    svg.classList.toggle('docked', step >= 1 && step < 4);   // step 4: ligand unbinds and leaves the site
    svg.classList.toggle('gateopen', step >= 2 && step < 4);
    document.getElementById('receptorSite').setAttribute('stroke', step >= 1 && step < 4 ? '#EF9F27' : 'var(--border-strong)');
    document.getElementById('receptorSite').setAttribute('stroke-width', step >= 1 && step < 4 ? '2.5' : '1');
    document.getElementById('ligandGroup').style.opacity = '1';
    document.getElementById('ligandLabel').textContent = step >= 1 && step < 4 ? 'Ligand (bound)' : 'Ligand';
    x = step === 3 ? 340 : step >= 4 ? 560 : 120;
  } else {
    x = step === 0 ? 120 : step === 1 ? 300 : step === 2 ? 340 : 560;
  }
  document.getElementById('molecule').style.transform = `translateX(${x - 120}px)`;
}
function stepFwd() { if (step < maxStep()) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('simple');
</script>
'''


# ---------------------------------------------------------------------------
# HUMORAL_IMMUNE_GENERAL  (source: humoral.html)
# ---------------------------------------------------------------------------
HUMORAL_IMMUNE_GENERAL = '''
<h2 class="sr-only">Interactive diagram of the humoral immune response: a B cell binds antigen, presents it to a helper T cell, then proliferates into antibody-secreting plasma cells and memory B cells.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .drift { animation: drift 2s ease-in-out infinite; }
  @keyframes drift { 0%,100%{transform:translateY(0)} 50%{transform:translateY(6px)} }
  #antigen { transition: transform 0.8s ease; }
  .docked #antigen { transform: translateY(30px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 360" role="img">
<title>Humoral immune response</title>
<desc>A B cell's receptor binds a matching antigen, internalizes and presents it on MHC-II, a helper T cell recognizes the complex and delivers cytokine signals, and the B cell proliferates into antibody-secreting plasma cells and memory B cells.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<circle cx="180" cy="180" r="60" class="c-teal"/>
<text class="th" x="180" y="180" text-anchor="middle" dominant-baseline="central">B cell</text>
<path id="bcr" d="M180 120 L165 100 M180 120 L195 100" stroke="#0F6E56" stroke-width="2" stroke-linecap="round"/>

<g id="antigen" class="stg">
<circle class="drift" cx="180" cy="70" r="9" fill="#EF9F27"/>
<text class="ts" x="180" y="52" text-anchor="middle">Antigen</text>
</g>

<g id="mhcPresent" class="stg">
<rect x="165" y="150" width="30" height="12" rx="3" fill="#EF9F27"/>
<text class="ts" x="180" y="140" text-anchor="middle">MHC-II presenting</text>
</g>

<g id="helperT" class="stg">
<circle cx="340" cy="150" r="45" class="c-purple"/>
<text class="th" x="340" y="150" text-anchor="middle" dominant-baseline="central">Helper T</text>
<line id="cytokine" x1="285" y1="160" x2="245" y2="170" stroke="#7F77DD" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow)"/>
<text class="ts" x="340" y="205" text-anchor="middle">Cytokine signal</text>
</g>

<g id="plasmaCells" class="stg">
<circle cx="480" cy="120" r="30" class="c-coral"/>
<text class="ts" x="480" y="120" text-anchor="middle" dominant-baseline="central">Plasma cell</text>
<circle cx="480" cy="230" r="30" class="c-coral"/>
<text class="ts" x="480" y="230" text-anchor="middle" dominant-baseline="central">Plasma cell</text>
</g>

<g id="memoryCells" class="stg">
<circle cx="580" cy="175" r="24" class="c-gray"/>
<text class="ts" x="580" y="175" text-anchor="middle" dominant-baseline="central">Memory B</text>
</g>

<g id="antibodies" class="stg">
<path class="drift" d="M540 100 l-6 -6 M540 100 l6 -6 M540 100 l0 8" stroke="#B91C1C" stroke-width="1.5" fill="none"/>
<path class="drift" d="M560 260 l-6 -6 M560 260 l6 -6 M560 260 l0 8" stroke="#B91C1C" stroke-width="1.5" fill="none" style="animation-delay:.4s"/>
<path class="drift" d="M600 90 l-6 -6 M600 90 l6 -6 M600 90 l0 8" stroke="#B91C1C" stroke-width="1.5" fill="none" style="animation-delay:.7s"/>
<text class="ts" x="580" y="290" text-anchor="middle">Antibodies neutralize antigen</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — B cell receptor unbound, antigen free",
  "Step 1 of 4 — antigen binds BCR, internalized and presented on MHC-II",
  "Step 2 of 4 — helper T cell recognizes the complex, delivers cytokine signal",
  "Step 3 of 4 — B cell proliferates into plasma cells and memory B cells",
  "Step 4 of 4 — plasma cells secrete antibodies that neutralize the antigen"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.querySelector('svg').classList.toggle('docked', step >= 1);
  document.getElementById('antigen').classList.toggle('on', step <= 1);
  document.getElementById('mhcPresent').classList.toggle('on', step >= 1 && step <= 2);
  document.getElementById('helperT').classList.toggle('on', step >= 2);
  document.getElementById('plasmaCells').classList.toggle('on', step >= 3);
  document.getElementById('memoryCells').classList.toggle('on', step >= 3);
  document.getElementById('antibodies').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# TCELL_ACTIVATION_GENERAL  (source: tcell.html)
# ---------------------------------------------------------------------------
TCELL_ACTIVATION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of T cell activation: an antigen-presenting cell displays a processed antigen on MHC-II, a naive T cell's receptor binds it, and a costimulatory signal is required before full activation.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #tcellGroup { transition: transform 1s ease; }
  .docked #tcellGroup { transform: translateX(-40px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>T cell activation, general view</title>
<desc>An antigen-presenting cell engulfs and processes a pathogen, displaying a fragment on MHC-II. A naive T cell's receptor binds the MHC-antigen complex as signal one, and a costimulatory CD28-B7 interaction provides signal two, together fully activating the T cell.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<path d="M120 160 Q80 100 150 70 Q220 40 260 100 Q290 150 240 200 Q180 240 120 160 Z" class="c-amber" stroke-width="0.5"/>
<text class="th" x="180" y="150" text-anchor="middle">APC</text>

<g id="pathogen" class="stg">
<circle cx="180" cy="60" r="9" fill="#E24B4A"/>
<text class="ts" x="180" y="42" text-anchor="middle">Pathogen</text>
</g>

<g id="mhcII" class="stg">
<rect x="230" y="150" width="26" height="12" rx="3" fill="#EF9F27"/>
<text class="ts" x="243" y="135" text-anchor="middle">MHC-II + antigen</text>
</g>

<g id="tcellGroup">
<circle cx="440" cy="160" r="55" class="c-purple"/>
<text class="th" x="440" y="160" text-anchor="middle" dominant-baseline="central">Naive T cell</text>
</g>

<g id="signal1" class="stg">
<line x1="380" y1="160" x2="258" y2="158" stroke="#7F77DD" stroke-width="1.5" marker-end="url(#arrow)"/>
<text class="ts" x="320" y="145" text-anchor="middle">Signal 1 — TCR / MHC</text>
</g>

<g id="signal2" class="stg">
<line x1="400" y1="200" x2="270" y2="195" stroke="#639922" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow)"/>
<text class="ts" x="335" y="215" text-anchor="middle">Signal 2 — CD28 / B7 (costimulation)</text>
</g>

<g id="activated" class="stg">
<circle cx="440" cy="160" r="60" fill="none" stroke="#639922" stroke-width="2" stroke-dasharray="4 3"/>
<text class="ts" x="440" y="225" text-anchor="middle">Activated</text>
<circle cx="560" cy="110" r="28" class="c-purple"/>
<text class="ts" x="560" y="110" text-anchor="middle" dominant-baseline="central">Helper T</text>
<circle cx="560" cy="210" r="28" class="c-purple"/>
<text class="ts" x="560" y="210" text-anchor="middle" dominant-baseline="central">Helper T</text>
<text class="th" x="560" y="255" text-anchor="middle">Proliferates into helper T cells</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — APC engulfs the pathogen",
  "Step 1 of 4 — pathogen processed, fragment presented on MHC-II",
  "Step 2 of 4 — signal 1: naive T cell's receptor binds the MHC-antigen complex",
  "Step 3 of 4 — signal 2: costimulatory CD28-B7 interaction confirms the signal is genuine",
  "Step 4 of 4 — T cell fully activated, proliferates into helper T cells"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('pathogen').classList.toggle('on', step === 0);
  document.getElementById('mhcII').classList.toggle('on', step >= 1);
  document.querySelector('svg').classList.toggle('docked', step >= 2);
  document.getElementById('signal1').classList.toggle('on', step >= 2);
  document.getElementById('signal2').classList.toggle('on', step >= 3);
  document.getElementById('activated').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# FERTILIZATION_GENERAL  (source: fertilization.html)
# ---------------------------------------------------------------------------
FERTILIZATION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of fertilization: sperm penetrates the egg's outer layers, membranes fuse, cortical granules block additional sperm, and pronuclei fuse into a zygote.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #spermGroup { transition: transform 1s ease, opacity .6s ease; }
  #zonaLayer { transition: stroke 0.6s ease, stroke-width 0.6s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Fertilization, general view</title>
<desc>A sperm cell approaches the egg, undergoes the acrosomal reaction to penetrate the zona pellucida, fuses its membrane with the egg, triggers cortical granule release that hardens the zona pellucida to block additional sperm, and the two pronuclei fuse into a zygote.</desc>

<circle cx="380" cy="150" r="90" class="c-amber"/>
<circle id="zonaLayer" cx="380" cy="150" r="90" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<text class="th" x="380" y="112" text-anchor="middle" dominant-baseline="central">Egg</text>
<text class="ts" x="380" y="255" text-anchor="middle">Zona pellucida</text>

<g id="spermGroup">
<path d="M140 150 L190 150" stroke="var(--t)" stroke-width="2" stroke-linecap="round"/>
<circle cx="200" cy="150" r="10" fill="#378ADD"/>
<text class="ts" x="196" y="132" text-anchor="end">Sperm</text>
<g id="acrosome" class="stg">
<circle cx="210" cy="150" r="5" fill="#EF9F27"/>
<text class="ts" x="205" y="185" text-anchor="end">Acrosomal enzymes penetrate zona</text>
</g>
</g>

<g id="corticalReaction" class="stg">
<circle cx="330" cy="100" r="4" fill="#B91C1C"/>
<circle cx="330" cy="215" r="4" fill="#B91C1C"/>
<circle cx="410" cy="90" r="4" fill="#B91C1C"/>
<text class="ts" x="380" y="60" text-anchor="middle">Cortical granules released — zona hardens</text>
</g>

<g id="pronuclei" class="stg">
<circle cx="370" cy="150" r="14" fill="none" stroke="#378ADD" stroke-width="1.5"/>
<circle cx="395" cy="150" r="14" fill="none" stroke="#D85A30" stroke-width="1.5"/>
<text class="ts" x="380" y="200" text-anchor="middle" id="pronucleiLabel">Two pronuclei approach</text>
</g>

<g id="zygote" class="stg">
<circle cx="382" cy="150" r="16" class="c-green"/>
<text class="ts" x="382" y="150" text-anchor="middle" dominant-baseline="central">Zygote</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — sperm approaches the egg",
  "Step 1 of 4 — acrosomal reaction: enzymes digest a path through the zona pellucida",
  "Step 2 of 4 — sperm and egg plasma membranes fuse",
  "Step 3 of 4 — cortical reaction: granules release, zona hardens to block other sperm",
  "Step 4 of 4 — pronuclei fuse, forming a diploid zygote"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('acrosome').classList.toggle('on', step === 1);
  document.getElementById('spermGroup').style.transform = step === 0 ? 'translateX(0px)' : step === 1 ? 'translateX(80px)' : 'translateX(160px)';
  document.getElementById('spermGroup').style.opacity = step >= 2 ? '0' : '1';
  document.getElementById('corticalReaction').classList.toggle('on', step === 3);
  document.getElementById('zonaLayer').setAttribute('stroke-width', step >= 3 ? '4' : '1.5');
  document.getElementById('pronuclei').classList.toggle('on', step >= 2 && step < 4);
  document.getElementById('zygote').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# CLEAVAGE_BLASTOCYST_GENERAL  (new)
# ---------------------------------------------------------------------------
CLEAVAGE_BLASTOCYST_GENERAL = '''
<h2 class="sr-only">Interactive diagram of cleavage and blastocyst formation: the zygote divides into 2, 4, 8 and then 16 ever-smaller cells inside the zona pellucida, compacts into a morula, and hollows out into a blastocyst with an inner cell mass, a trophoblast layer and a fluid-filled blastocoel.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .reveal { opacity: 0; transition: opacity .5s ease; }
  .reveal.on { opacity: 1; }
  .cell { transition: cx .9s cubic-bezier(.3,0,.2,1), cy .9s cubic-bezier(.3,0,.2,1), r .9s cubic-bezier(.3,0,.2,1), fill .6s ease, stroke .6s ease; }
  #blastocoel, #troLayer, #morulaSurface { transition: opacity .6s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Cleavage and blastocyst formation</title>
<desc>After fertilization the zygote divides repeatedly without growing: 2 cells, then 4, then 8, each half the size of the one before, all inside the same zona pellucida. Around day 3 to 4 the 16-cell embryo compacts into a tight ball called the morula, in which outer and inner cells begin to differ. By day 5 fluid collects in a central cavity, the blastocoel, turning the morula into a blastocyst: the outer cells form the trophoblast, which will become the placenta, and an inner cell mass clustered at one side will form the embryo itself.</desc>

<text class="ts" x="340" y="26" text-anchor="middle" id="stageLabel">Zygote</text>

<circle id="blastocoel" cx="340" cy="150" r="66" fill="#378ADD" fill-opacity="0.12" style="opacity:0"/>
<circle id="troLayer" cx="340" cy="150" r="74" fill="none" stroke="#0F6E56" stroke-width="9" stroke-opacity="0.35" style="opacity:0"/>
<circle id="morulaSurface" cx="340" cy="150" r="80" fill="none" stroke="var(--t)" stroke-width="1" stroke-dasharray="3 3" style="opacity:0"/>
<circle id="cell0" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell1" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell2" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell3" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell4" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell5" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell6" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell7" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell8" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell9" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell10" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell11" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell12" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell13" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell14" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="cell15" class="cell c-amber" cx="340" cy="150" r="0"/>
<circle id="zona" cx="340" cy="150" r="88" fill="none" stroke="#B45309" stroke-width="2.5" stroke-opacity="0.6"/>
<text class="ts" x="340" y="256" text-anchor="middle">Zona pellucida — the embryo does not grow yet</text>

<text class="th" x="60" y="120" id="dayLabel">Day 0–1</text>
<text class="ts" x="60" y="140" id="countLabel">1 cell</text>
<text class="ts" x="60" y="158" id="sizeLabel">full-size cell</text>

<g id="morulaNote" class="reveal">
<text class="ts" x="452" y="118" text-anchor="start">Cells pack tightly (compaction)</text>
<text class="ts" x="452" y="150" text-anchor="start"><tspan fill="#0F6E56" font-weight="600">Outer cells</tspan> → trophoblast</text>
<text class="ts" x="452" y="168" text-anchor="start"><tspan fill="#6D28D9" font-weight="600">Inner cells</tspan> → inner cell mass</text>
</g>

<g id="blastoLabels" class="reveal">
<line x1="370" y1="98" x2="448" y2="78" stroke="var(--t)" stroke-width="0.75"/>
<text class="ts" x="452" y="74" text-anchor="start">Inner cell mass → the embryo</text>
<line x1="410" y1="168" x2="448" y2="190" stroke="var(--t)" stroke-width="0.75"/>
<text class="ts" x="452" y="196" text-anchor="start">Trophoblast → placenta</text>
<text class="ts" x="340" y="174" text-anchor="middle">Blastocoel</text>
<text class="ts" x="340" y="188" text-anchor="middle">(fluid-filled cavity)</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 5</span>
</div>

<script>
let step = 0;
const LAYOUT = [[[0,0,74],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[-40,0,40],[40,0,40],[-40,0,0],[40,0,0],[-40,0,0],[40,0,0],[-40,0,0],[40,0,0],[-40,0,0],[40,0,0],[-40,0,0],[40,0,0],[-40,0,0],[40,0,0],[-40,0,0],[40,0,0]],[[-29,-29,30],[29,-29,30],[-29,29,30],[29,29,30],[-29,-29,0],[29,-29,0],[-29,29,0],[29,29,0],[-29,-29,0],[29,-29,0],[-29,29,0],[29,29,0],[-29,-29,0],[29,-29,0],[-29,29,0],[29,29,0]],[[-41.7,-19.4,22],[27.7,-36.7,22],[-41.0,20.9,22],[29.6,35.2,22],[0,0,22],[-11.1,-44.6,22],[-8.8,45.2,22],[46.0,-0.8,22],[-41.7,-19.4,0],[27.7,-36.7,0],[-41.0,20.9,0],[29.6,35.2,0],[0,0,0],[-11.1,-44.6,0],[-8.8,45.2,0],[46.0,-0.8,0]],[[-52.7,-21.8,22],[21.8,-52.7,22],[-52.7,21.8,22],[52.7,21.8,22],[-21.8,-52.7,22],[52.7,-21.8,22],[-21.8,52.7,22],[21.8,52.7,22],[-26.3,-12.3,14],[17.5,-23.2,14],[-25.8,13.2,14],[18.6,22.2,14],[0,0,14],[-7.0,-28.1,14],[-5.5,28.5,14],[29.0,-0.5,14]],[[-68.4,-28.3,11],[28.3,-68.4,11],[-68.4,28.3,11],[68.4,28.3,11],[-28.3,-68.4,11],[68.4,-28.3,11],[-28.3,68.4,11],[28.3,68.4,11],[-22,-52,11],[0,-55,11],[22,-52,11],[-24,-32,11],[0,-34,11],[24,-32,11],[-12,-14,11],[12,-14,11]]];
const stages = ['Zygote', '2-cell stage', '4-cell stage', '8-cell stage', 'Morula (compacted)', 'Blastocyst'];
const days   = ['Day 0–1', 'Day 1–2', 'Day 2', 'Day 3', 'Day 3–4', 'Day 5'];
const counts = ['1 cell', '2 cells', '4 cells', '8 cells', '16+ cells', '~60–100 cells'];
const sizes  = ['full-size cell', 'each ½ the size', 'each ¼ the size', 'each ⅛ the size', 'smaller still', 'two cell types'];
const labels = [
  "Step 0 of 5 — the zygote: one large cell inside the zona pellucida",
  "Step 1 of 5 — first cleavage: the zygote divides into 2 cells (blastomeres) — the embryo does not get bigger",
  "Step 2 of 5 — second cleavage: 4 cells, each smaller again; total size is still the same",
  "Step 3 of 5 — third cleavage: 8 cells — each division just splits the same volume into more, smaller cells",
  "Step 4 of 5 — compaction: the 16+ cells pack tightly into a morula; outer and inner cells start to take different fates",
  "Step 5 of 5 — blastocyst: fluid fills a central cavity (blastocoel); outer cells form the trophoblast (future placenta), the inner cell mass will form the embryo"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('stageLabel').textContent = stages[step];
  document.getElementById('dayLabel').textContent = days[step];
  document.getElementById('countLabel').textContent = counts[step];
  document.getElementById('sizeLabel').textContent = sizes[step];
  LAYOUT[step].forEach(([dx, dy, r], i) => {
    const c = document.getElementById('cell' + i);
    const cx = 340 + dx, cy = 150 + dy;
    c.setAttribute('cx', cx); c.setAttribute('cy', cy); c.setAttribute('r', r);
    c.style.cx = cx + 'px'; c.style.cy = cy + 'px'; c.style.r = r + 'px';
    // from compaction on, outer cells (0-7) and inner cells (8-15) take different fates
    c.setAttribute('class', 'cell ' + (step >= 4 ? (i < 8 ? 'c-teal' : 'c-purple') : 'c-amber'));
  });
  document.getElementById('morulaSurface').style.opacity = step === 4 ? '1' : '0';
  document.getElementById('morulaNote').classList.toggle('on', step === 4);
  document.getElementById('blastocoel').style.opacity = step >= 5 ? '1' : '0';
  document.getElementById('troLayer').style.opacity = step >= 5 ? '1' : '0';
  document.getElementById('blastoLabels').classList.toggle('on', step >= 5);
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# CLEAVAGE_BLASTOCYST_TECHNICAL  (new)
# ---------------------------------------------------------------------------
CLEAVAGE_BLASTOCYST_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of preimplantation development: compaction by E-cadherin and apical polarity, outer versus inner cells, Hippo and YAP signalling switching on Cdx2 or Oct4, cavitation driven by Na/K pumps and tight junctions, and the split of the inner cell mass into epiblast and primitive endoderm.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .reveal { opacity: 0; transition: opacity .5s ease; }
  .reveal.on { opacity: 1; }
  .tcell, .tnuc { transition: cx .9s cubic-bezier(.3,0,.2,1), cy .9s cubic-bezier(.3,0,.2,1), r .9s cubic-bezier(.3,0,.2,1), fill .6s ease, stroke .6s ease; }
  .tnuc { stroke-width: 1; }
  .cap { transition: opacity .5s ease; }
  #ballBg, #blastocoelT { transition: opacity .6s ease, r .9s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Cleavage and blastocyst formation, technical view</title>
<desc>At the 8-cell stage the blastomeres compact: E-cadherin adherens junctions flatten them against each other and each cell forms an apical domain of Par3, Par6 and aPKC on its outer face. At the 8 to 16 cell divisions, daughters that keep the apical domain stay outside and become polar, while daughters without it are pushed inside and are apolar. In outer cells the Hippo pathway is off, so YAP enters the nucleus, binds TEAD4 and switches on Cdx2, making trophectoderm. In inner cells Hippo is on, LATS kinases keep YAP out of the nucleus, and Oct4 and Nanog remain on, making the inner cell mass. Tight junctions then seal the trophectoderm and Na/K ATPases on its inner face pump sodium inward; water follows through aquaporins and inflates the blastocoel. In the blastocyst the inner cell mass separates into Nanog-positive epiblast, the future embryo, and a Gata6-positive primitive endoderm layer facing the cavity, driven by FGF4 and ERK signalling.</desc>
<defs>
<marker id="arrowT" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></marker>
<clipPath id="ballClip"><circle id="ballClipC" cx="290" cy="165" r="200"/></clipPath>
</defs>

<text class="ts" x="290" y="22" text-anchor="middle" id="stageLabelT">8-cell embryo</text>
<text class="th" x="20" y="60" id="dayLabelT">Day 3</text>

<circle id="blastocoelT" cx="290" cy="165" r="64" fill="#378ADD" fill-opacity="0.12" style="opacity:0"/>
<circle id="ballBg" cx="290" cy="165" r="66" fill="#FDE68A" style="opacity:0"/>
<circle id="teLayer" cx="290" cy="165" r="77" fill="none" stroke="#0F6E56" stroke-width="12" stroke-opacity="0.3" style="opacity:0;transition:opacity .6s ease"/>
<g clip-path="url(#ballClip)">
<circle id="tc0" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc1" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc2" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc3" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc4" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc5" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc6" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc7" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc8" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc9" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc10" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc11" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc12" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc13" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc14" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tc15" class="tcell c-amber" cx="290" cy="165" r="0"/>
<circle id="tn0" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn1" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn2" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn3" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn4" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn5" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn6" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn7" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn8" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn9" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn10" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn11" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn12" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn13" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn14" class="tnuc" cx="290" cy="165" r="0"/>
<circle id="tn15" class="tnuc" cx="290" cy="165" r="0"/>
</g>
<path id="cap0" class="cap" d="M0 0" fill="none" stroke="#EA580C" stroke-width="4" stroke-linecap="round"/>
<path id="cap1" class="cap" d="M0 0" fill="none" stroke="#EA580C" stroke-width="4" stroke-linecap="round"/>
<path id="cap2" class="cap" d="M0 0" fill="none" stroke="#EA580C" stroke-width="4" stroke-linecap="round"/>
<path id="cap3" class="cap" d="M0 0" fill="none" stroke="#EA580C" stroke-width="4" stroke-linecap="round"/>
<path id="cap4" class="cap" d="M0 0" fill="none" stroke="#EA580C" stroke-width="4" stroke-linecap="round"/>
<path id="cap5" class="cap" d="M0 0" fill="none" stroke="#EA580C" stroke-width="4" stroke-linecap="round"/>
<path id="cap6" class="cap" d="M0 0" fill="none" stroke="#EA580C" stroke-width="4" stroke-linecap="round"/>
<path id="cap7" class="cap" d="M0 0" fill="none" stroke="#EA580C" stroke-width="4" stroke-linecap="round"/>
<g id="ecad" class="reveal">
<line x1="297.1" y1="172.1" x2="333.8" y2="208.8" stroke="#6D28D9" stroke-width="2.5" stroke-dasharray="3 3"/>
<line x1="290.0" y1="175.0" x2="290.0" y2="227.0" stroke="#6D28D9" stroke-width="2.5" stroke-dasharray="3 3"/>
<line x1="282.9" y1="172.1" x2="246.2" y2="208.8" stroke="#6D28D9" stroke-width="2.5" stroke-dasharray="3 3"/>
<line x1="280.0" y1="165.0" x2="228.0" y2="165.0" stroke="#6D28D9" stroke-width="2.5" stroke-dasharray="3 3"/>
<line x1="282.9" y1="157.9" x2="246.2" y2="121.2" stroke="#6D28D9" stroke-width="2.5" stroke-dasharray="3 3"/>
<line x1="290.0" y1="155.0" x2="290.0" y2="103.0" stroke="#6D28D9" stroke-width="2.5" stroke-dasharray="3 3"/>
<line x1="297.1" y1="157.9" x2="333.8" y2="121.2" stroke="#6D28D9" stroke-width="2.5" stroke-dasharray="3 3"/>
<line x1="300.0" y1="165.0" x2="352.0" y2="165.0" stroke="#6D28D9" stroke-width="2.5" stroke-dasharray="3 3"/>
</g>
<g id="tightJ" class="reveal">
<circle cx="348.0" cy="223.0" r="2.6" fill="#1F2937"/>
<circle cx="290.0" cy="247.0" r="2.6" fill="#1F2937"/>
<circle cx="232.0" cy="223.0" r="2.6" fill="#1F2937"/>
<circle cx="208.0" cy="165.0" r="2.6" fill="#1F2937"/>
<circle cx="232.0" cy="107.0" r="2.6" fill="#1F2937"/>
<circle cx="290.0" cy="83.0" r="2.6" fill="#1F2937"/>
<circle cx="348.0" cy="107.0" r="2.6" fill="#1F2937"/>
<circle cx="372.0" cy="165.0" r="2.6" fill="#1F2937"/>
</g>
<g id="pumps" class="reveal">
<rect x="227.8" y="136.9" width="8" height="8" rx="1.5" fill="#F59E0B" stroke="#B45309" stroke-width="0.8"/><line x1="236.4" y1="142.8" x2="249.3" y2="148.2" stroke="#B45309" stroke-width="1.2" marker-end="url(#arrowT)"/>
<rect x="227.8" y="185.1" width="8" height="8" rx="1.5" fill="#F59E0B" stroke="#B45309" stroke-width="0.8"/><line x1="236.4" y1="187.2" x2="249.3" y2="181.8" stroke="#B45309" stroke-width="1.2" marker-end="url(#arrowT)"/>
<rect x="344.2" y="185.1" width="8" height="8" rx="1.5" fill="#F59E0B" stroke="#B45309" stroke-width="0.8"/><line x1="343.6" y1="187.2" x2="330.7" y2="181.8" stroke="#B45309" stroke-width="1.2" marker-end="url(#arrowT)"/>
<rect x="344.2" y="136.9" width="8" height="8" rx="1.5" fill="#F59E0B" stroke="#B45309" stroke-width="0.8"/><line x1="343.6" y1="142.8" x2="330.7" y2="148.2" stroke="#B45309" stroke-width="1.2" marker-end="url(#arrowT)"/>
<rect x="261.9" y="219.2" width="8" height="8" rx="1.5" fill="#F59E0B" stroke="#B45309" stroke-width="0.8"/><line x1="267.8" y1="218.6" x2="273.2" y2="205.7" stroke="#B45309" stroke-width="1.2" marker-end="url(#arrowT)"/>
<rect x="310.1" y="219.2" width="8" height="8" rx="1.5" fill="#F59E0B" stroke="#B45309" stroke-width="0.8"/><line x1="312.2" y1="218.6" x2="306.8" y2="205.7" stroke="#B45309" stroke-width="1.2" marker-end="url(#arrowT)"/>
</g>
<circle cx="290" cy="165" r="100" fill="none" stroke="#B45309" stroke-width="2.5" stroke-opacity="0.55"/>
<text class="ts" x="290" y="282" text-anchor="middle">Zona pellucida</text>

<g id="note0" class="reveal">
<text class="ts" x="420" y="120">Blastomeres round and loosely attached</text>
<text class="ts" x="420" y="138">— every cell still touches the outside</text>
</g>
<g id="note1" class="reveal">
<text class="ts" x="420" y="110"><tspan fill="#6D28D9" font-weight="600">E-cadherin</tspan> junctions pull cells flat</text>
<text class="ts" x="420" y="128">against each other (compaction)</text>
<text class="ts" x="420" y="156"><tspan fill="#EA580C" font-weight="600">Apical domain</tspan> (Par3 / Par6 / aPKC)</text>
<text class="ts" x="420" y="174">forms on each cell's outer face</text>
</g>
<g id="note2" class="reveal">
<text class="ts" x="420" y="104">8 → 16 cells</text>
<text class="ts" x="420" y="126">Keeps the <tspan fill="#EA580C" font-weight="600">apical domain</tspan></text>
<text class="ts" x="420" y="144">→ stays outside (polar)</text>
<text class="ts" x="420" y="170">No apical domain</text>
<text class="ts" x="420" y="188">→ pushed inside (apolar)</text>
</g>
<g id="note3" class="reveal">
<text class="ts" x="420" y="92"><tspan fill="#0F6E56" font-weight="600">Outer (polar) cells</tspan></text>
<text class="ts" x="420" y="110">Hippo OFF → YAP enters nucleus</text>
<text class="ts" x="420" y="128">+ TEAD4 → <tspan font-weight="600">Cdx2</tspan> → trophectoderm</text>
<text class="ts" x="420" y="160"><tspan fill="#6D28D9" font-weight="600">Inner (apolar) cells</tspan></text>
<text class="ts" x="420" y="178">Hippo ON → LATS keeps YAP out</text>
<text class="ts" x="420" y="196">of nucleus → <tspan font-weight="600">Oct4 / Nanog</tspan> → ICM</text>
</g>
<g id="note4" class="reveal">
<text class="ts" x="420" y="100"><tspan fill="#1F2937" font-weight="600">●</tspan> Tight junctions seal the</text>
<text class="ts" x="420" y="118">trophectoderm into a barrier</text>
<text class="ts" x="420" y="148"><tspan fill="#B45309" font-weight="600">■</tspan> Na⁺/K⁺-ATPase on the inner</text>
<text class="ts" x="420" y="166">face pumps Na⁺ inward →</text>
<text class="ts" x="420" y="184">water follows (aquaporins)</text>
<text class="ts" x="420" y="202">→ blastocoel inflates</text>
</g>
<g id="note5" class="reveal">
<text class="ts" x="420" y="92"><tspan fill="#6D28D9" font-weight="600">Epiblast</tspan> (Nanog) → the embryo</text>
<text class="ts" x="420" y="112"><tspan fill="#B45309" font-weight="600">Primitive endoderm</tspan> (Gata6)</text>
<text class="ts" x="420" y="130">→ yolk sac; lines the cavity</text>
<text class="ts" x="420" y="148">(sorted by FGF4 → ERK)</text>
<text class="ts" x="420" y="178"><tspan fill="#0F6E56" font-weight="600">Trophectoderm</tspan> → placenta</text>
<text class="ts" x="420" y="208">Next: hatches from the zona</text>
<text class="ts" x="420" y="226">and implants (day 6–7)</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 5</span>
</div>

<script>
let step = 0;
const CX = 290, CY = 165;
const LAYOUT = [[[-40.7,-16.8,21],[16.8,-40.7,21],[-40.7,16.8,21],[40.7,16.8,21],[-16.8,-40.7,21],[40.7,-16.8,21],[-16.8,40.7,21],[16.8,40.7,21],[-40.7,-16.8,0],[16.8,-40.7,0],[-40.7,16.8,0],[40.7,16.8,0],[-16.8,-40.7,0],[40.7,-16.8,0],[-16.8,40.7,0],[16.8,40.7,0]],[[-33.3,-13.8,31],[13.8,-33.3,31],[-33.3,13.8,31],[33.3,13.8,31],[-13.8,-33.3,31],[33.3,-13.8,31],[-13.8,33.3,31],[13.8,33.3,31],[-33.3,-13.8,0],[13.8,-33.3,0],[-33.3,13.8,0],[33.3,13.8,0],[-13.8,-33.3,0],[33.3,-13.8,0],[-13.8,33.3,0],[13.8,33.3,0]],[[-49.9,-20.7,21],[20.7,-49.9,21],[-49.9,20.7,21],[49.9,20.7,21],[-20.7,-49.9,21],[49.9,-20.7,21],[-20.7,49.9,21],[20.7,49.9,21],[-22.2,-9.2,13],[9.2,-22.2,13],[-22.2,9.2,13],[22.2,9.2,13],[-9.2,-22.2,13],[22.2,-9.2,13],[-9.2,22.2,13],[9.2,22.2,13]],[[-49.9,-20.7,21],[20.7,-49.9,21],[-49.9,20.7,21],[49.9,20.7,21],[-20.7,-49.9,21],[49.9,-20.7,21],[-20.7,49.9,21],[20.7,49.9,21],[-22.2,-9.2,13],[9.2,-22.2,13],[-22.2,9.2,13],[22.2,9.2,13],[-9.2,-22.2,13],[22.2,-9.2,13],[-9.2,22.2,13],[9.2,22.2,13]],[[-71.1,-29.5,13],[29.5,-71.1,13],[-71.1,29.5,13],[71.1,29.5,13],[-29.5,-71.1,13],[71.1,-29.5,13],[-29.5,71.1,13],[29.5,71.1,13],[-22,-53,11],[0,-56,11],[22,-53,11],[-24,-33,11],[0,-35,11],[24,-33,11],[-12,-15,11],[12,-15,11]],[[-71.1,-29.5,13],[29.5,-71.1,13],[-71.1,29.5,13],[71.1,29.5,13],[-29.5,-71.1,13],[71.1,-29.5,13],[-29.5,71.1,13],[29.5,71.1,13],[-22,-53,11],[0,-56,11],[22,-53,11],[-24,-33,11],[0,-35,11],[24,-33,11],[-12,-15,11],[12,-15,11]]];
const CAPS = [["M0 0","M0 0","M0 0","M0 0","M0 0","M0 0","M0 0","M0 0"],["M224.3 158.7 A66 66 0 0 1 239.1 123.0","M296.3 99.3 A66 66 0 0 1 332.0 114.1","M239.1 207.0 A66 66 0 0 1 224.3 171.3","M355.7 171.3 A66 66 0 0 1 340.9 207.0","M248.0 114.1 A66 66 0 0 1 283.7 99.3","M340.9 123.0 A66 66 0 0 1 355.7 158.7","M283.7 230.7 A66 66 0 0 1 248.0 215.9","M332.0 215.9 A66 66 0 0 1 296.3 230.7"],["M215.3 157.8 A75 75 0 0 1 232.1 117.3","M297.2 90.3 A75 75 0 0 1 337.7 107.1","M232.1 212.7 A75 75 0 0 1 215.3 172.2","M364.7 172.2 A75 75 0 0 1 347.9 212.7","M242.3 107.1 A75 75 0 0 1 282.8 90.3","M347.9 117.3 A75 75 0 0 1 364.7 157.8","M282.8 239.7 A75 75 0 0 1 242.3 222.9","M337.7 222.9 A75 75 0 0 1 297.2 239.7"],["M215.3 157.8 A75 75 0 0 1 232.1 117.3","M297.2 90.3 A75 75 0 0 1 337.7 107.1","M232.1 212.7 A75 75 0 0 1 215.3 172.2","M364.7 172.2 A75 75 0 0 1 347.9 212.7","M242.3 107.1 A75 75 0 0 1 282.8 90.3","M347.9 117.3 A75 75 0 0 1 364.7 157.8","M282.8 239.7 A75 75 0 0 1 242.3 222.9","M337.7 222.9 A75 75 0 0 1 297.2 239.7"],["M0 0","M0 0","M0 0","M0 0","M0 0","M0 0","M0 0","M0 0"],["M0 0","M0 0","M0 0","M0 0","M0 0","M0 0","M0 0","M0 0"]];
const BALL = [0, 66, 75, 75, 0, 0];
const PRE = [11, 13, 14, 15];   // ICM cells on the side facing the cavity
const stages = ['8-cell embryo', 'Compaction', '16-cell: outer vs inner cells', 'Cell-fate decision', 'Cavitation', 'Blastocyst'];
const days   = ['Day 3', 'Day 3', 'Day 3–4', 'Day 3–4', 'Day 4', 'Day 5–6'];
const labels = [
  "Step 0 of 5 — 8-cell embryo (day 3): blastomeres are round and loosely attached; every cell still touches the outside",
  "Step 1 of 5 — compaction: E-cadherin adherens junctions flatten the cells against each other, and each cell polarizes — an apical domain (Par3/Par6/aPKC) forms on its outer face",
  "Step 2 of 5 — 8 → 16 cells: in asymmetric divisions the daughter that keeps the apical domain stays outside (polar), while the daughter without it is pushed inside (apolar)",
  "Step 3 of 5 — Hippo signalling decides fate: outer cells have Hippo OFF, so YAP enters the nucleus with TEAD4 and switches on Cdx2 (trophectoderm); inner cells have Hippo ON, so YAP stays out and Oct4/Nanog stay on (inner cell mass)",
  "Step 4 of 5 — cavitation: tight junctions seal the trophectoderm; Na⁺/K⁺-ATPases on its inner face pump Na⁺ inward and water follows by osmosis through aquaporins, inflating the blastocoel",
  "Step 5 of 5 — blastocyst: the inner cell mass splits into epiblast (Nanog, future embryo) and a primitive endoderm layer (Gata6) facing the cavity, sorted by FGF4 → ERK signalling; next the blastocyst hatches and implants"
];
const set = (el, k, v) => { el.setAttribute(k, v); el.style[k] = v + 'px'; };
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('stageLabelT').textContent = stages[step];
  document.getElementById('dayLabelT').textContent = days[step];
  const ball = BALL[step];
  document.getElementById('ballClipC').setAttribute('r', ball || 200);
  document.getElementById('ballBg').style.opacity = ball ? '1' : '0';
  document.getElementById('ballBg').setAttribute('r', ball || 66);
  document.getElementById('blastocoelT').style.opacity = step >= 4 ? '1' : '0';
  document.getElementById('teLayer').style.opacity = step >= 4 ? '1' : '0';   // trophectoderm is one continuous epithelium
  LAYOUT[step].forEach(([dx, dy, r], i) => {
    const c = document.getElementById('tc' + i), n = document.getElementById('tn' + i);
    const x = CX + dx, y = CY + dy;
    set(c, 'cx', x); set(c, 'cy', y); set(c, 'r', r);
    let cls = 'c-amber';
    if (step >= 3) cls = i < 8 ? 'c-teal' : (step >= 5 && PRE.includes(i) ? 'c-amber' : 'c-purple');
    c.setAttribute('class', 'tcell ' + cls);
    // nuclei appear when the fate decision is shown: outer = Cdx2 on, inner = Oct4 on (epiblast) / Gata6 (primitive endoderm)
    const nr = step >= 3 && r > 0 ? (i < 8 ? 5 : 4) : 0;
    set(n, 'cx', x); set(n, 'cy', y); set(n, 'r', nr);
    n.setAttribute('fill', i < 8 ? '#0F6E56' : (step >= 5 && PRE.includes(i) ? '#B45309' : '#6D28D9'));
    n.setAttribute('stroke', '#ffffff');
  });
  CAPS[step].forEach((d, i) => {
    const cap = document.getElementById('cap' + i);
    cap.setAttribute('d', d); cap.style.opacity = d === 'M0 0' ? '0' : '1';
  });
  document.getElementById('ecad').classList.toggle('on', step === 1);
  document.getElementById('tightJ').classList.toggle('on', step >= 4);
  document.getElementById('pumps').classList.toggle('on', step === 4);
  for (let k = 0; k <= 5; k++) document.getElementById('note' + k).classList.toggle('on', k === step);
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# IMPLANTATION_GENERAL  (new)
# ---------------------------------------------------------------------------
IMPLANTATION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of implantation: the blastocyst hatches from the zona pellucida, attaches to the uterine lining with its inner cell mass facing the wall, its trophoblast splits into cytotrophoblast and an invading syncytiotrophoblast, it sinks fully into the endometrium, and the syncytiotrophoblast releases hCG.</h2>
<style>
  .reveal { opacity: 0; transition: opacity .5s ease; }
  .reveal.on { opacity: 1; }
  #blasto { transition: transform 1.1s cubic-bezier(.3,0,.2,1); transform-box: view-box; transform-origin: 0 0; }
  #zonaWhole, #zonaBroken { transition: opacity .5s ease; }
  .hcg { animation: hcgUp 2.4s ease-in infinite; }
  @keyframes hcgUp { 0% { transform: translateY(0); opacity: 0; } 20% { opacity: 1; } 100% { transform: translateY(-34px); opacity: 0; } }
  @media (prefers-reduced-motion: reduce) { .hcg { animation: none; } }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Implantation</title>
<desc>Around day 5 the blastocyst, still inside its zona pellucida, floats in the uterine cavity. It hatches out of the zona and attaches to the endometrium with its inner cell mass, the embryonic pole, facing the uterine wall. At the contact site the trophoblast splits into an inner layer of dividing cytotrophoblast cells and an outer syncytiotrophoblast, a fused mass with many nuclei that digests its way into the endometrium. By around day 10 the embryo has sunk completely into the uterine lining, which closes over it. The syncytiotrophoblast releases the hormone hCG, which keeps the corpus luteum producing progesterone so the uterine lining is maintained, and maternal blood begins to fill spaces called lacunae, the first step toward the placenta. hCG is the hormone that pregnancy tests detect.</desc>
<defs>
<marker id="arrowI" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<text class="ts" x="40" y="40">Uterine cavity</text>
<text class="th" x="40" y="62" id="dayLabelI">Day 5</text>

<!-- endometrium (uterine lining) with glands and maternal vessels -->
<rect x="30" y="210" width="620" height="110" fill="#FBCFE8" fill-opacity="0.55"/>
<line x1="30" y1="210" x2="650" y2="210" stroke="#BE185D" stroke-width="2"/>
<path d="M60 211 Q60 262 74 262 Q88 262 88 211" fill="none" stroke="#BE185D" stroke-width="1.2" stroke-opacity="0.6"/>
<path d="M110 211 Q110 270 124 270 Q138 270 138 211" fill="none" stroke="#BE185D" stroke-width="1.2" stroke-opacity="0.6"/>
<path d="M560 211 Q560 266 574 266 Q588 266 588 211" fill="none" stroke="#BE185D" stroke-width="1.2" stroke-opacity="0.6"/>
<path d="M610 211 Q610 258 624 258 Q638 258 638 211" fill="none" stroke="#BE185D" stroke-width="1.2" stroke-opacity="0.6"/>
<path id="vesselL" d="M170 320 C158 296 182 284 170 262 C160 244 182 236 176 222" fill="none" stroke="#B91C1C" stroke-width="3" stroke-opacity="0.75"/>
<path id="vesselR" d="M520 320 C532 296 508 284 520 262 C530 244 508 236 514 222" fill="none" stroke="#B91C1C" stroke-width="3" stroke-opacity="0.75"/>
<text class="ts" x="40" y="312">Endometrium (uterine lining)</text>

<!-- zona pellucida: whole (step 0), then the empty broken shell left behind after hatching -->
<circle id="zonaWhole" cx="200" cy="112" r="49" fill="none" stroke="#B45309" stroke-width="2.5" stroke-opacity="0.65"/>
<path id="zonaBroken" d="M236 145 A49 49 0 1 1 245 132" fill="none" stroke="#B45309" stroke-width="2.5" stroke-opacity="0.65" style="opacity:0"/>

<!-- syncytiotrophoblast: small invading front (step 3), then a large shell around the embedded embryo (step 4-5) -->
<path id="synct3" class="reveal" d="M324 200 Q360 246 396 200 Q360 222 324 200 Z" fill="#9D174D" fill-opacity="0.55"/>
<path id="synct4" class="reveal" d="M314 252 Q312 316 360 316 Q408 316 406 252 Q394 300 360 300 Q326 300 314 252 Z" fill="#9D174D" fill-opacity="0.55"/>
<g id="lacunae" class="reveal">
<ellipse cx="334" cy="300" rx="7" ry="4" fill="#B91C1C"/>
<ellipse cx="360" cy="308" rx="8" ry="4" fill="#B91C1C"/>
<ellipse cx="386" cy="300" rx="7" ry="4" fill="#B91C1C"/>
</g>

<!-- blastocyst, drawn around (0,0) so it can move and turn -->
<g id="blasto">
<circle r="34" fill="#378ADD" fill-opacity="0.12"/>
<circle r="38" fill="none" stroke="#0F6E56" stroke-width="7" stroke-opacity="0.55"/>
<circle cx="0" cy="-28" r="8" class="c-purple"/>
<circle cx="-13" cy="-23" r="7" class="c-purple"/>
<circle cx="13" cy="-23" r="7" class="c-purple"/>
<circle cx="-6" cy="-15" r="6" class="c-purple"/>
<circle cx="6" cy="-15" r="6" class="c-purple"/>
</g>

<!-- endometrium closes over the embedded embryo (step 4-5) -->
<path id="sealed" class="reveal" d="M316 210 Q360 204 404 210" fill="none" stroke="#BE185D" stroke-width="3" stroke-linecap="round"/>

<g id="hcgGroup" class="reveal">
<circle class="hcg" cx="330" cy="292" r="3.5" fill="#F59E0B"/>
<circle class="hcg" cx="350" cy="300" r="3.5" fill="#F59E0B" style="animation-delay:.6s"/>
<circle class="hcg" cx="372" cy="300" r="3.5" fill="#F59E0B" style="animation-delay:1.2s"/>
<circle class="hcg" cx="392" cy="292" r="3.5" fill="#F59E0B" style="animation-delay:1.8s"/>
<line x1="410" y1="290" x2="510" y2="268" stroke="#B45309" stroke-width="1.2" marker-end="url(#arrowI)"/>
<text class="ts" x="536" y="292" text-anchor="start" font-weight="600" fill="#B45309">hCG → maternal blood</text>
</g>

<!-- structure labels, one set per step -->
<g id="lab0" class="reveal">
<text class="ts" x="200" y="52" text-anchor="middle">Zona pellucida</text>
<text class="ts" x="140" y="90" text-anchor="end">Inner cell mass</text>
<text class="ts" x="140" y="138" text-anchor="end">Trophoblast</text>
</g>
<g id="lab1" class="reveal">
<text class="ts" x="140" y="84" text-anchor="end">Empty zona</text>
<text class="ts" x="140" y="98" text-anchor="end">left behind</text>
</g>
<g id="lab2" class="reveal">
<text class="ts" x="300" y="150" text-anchor="end">Inner cell mass</text>
<text class="ts" x="300" y="164" text-anchor="end">faces the wall</text>
</g>
<g id="lab3" class="reveal">
<line x1="322" y1="176" x2="288" y2="160" stroke="var(--t)" stroke-width="0.75"/>
<text class="ts" x="284" y="156" text-anchor="end">Cytotrophoblast</text>
<line x1="336" y1="214" x2="288" y2="232" stroke="var(--t)" stroke-width="0.75"/>
<text class="ts" x="284" y="240" text-anchor="end">Syncytiotrophoblast</text>
</g>
<g id="lab4" class="reveal">
<line x1="323" y1="246" x2="304" y2="234" stroke="var(--t)" stroke-width="0.75"/>
<text class="ts" x="300" y="236" text-anchor="end">Cytotrophoblast</text>
<line x1="318" y1="280" x2="304" y2="266" stroke="var(--t)" stroke-width="0.75"/>
<text class="ts" x="300" y="268" text-anchor="end">Syncytiotrophoblast</text>
</g>
<g id="lab5" class="reveal">
<line x1="326" y1="302" x2="304" y2="296" stroke="var(--t)" stroke-width="0.75"/>
<text class="ts" x="300" y="298" text-anchor="end">Maternal blood (lacunae)</text>
</g>

<!-- explanation panel -->
<g id="note0" class="reveal">
<text class="ts" x="430" y="70">Day 5: the blastocyst floats in</text>
<text class="ts" x="430" y="86">the uterus, still inside its zona</text>
</g>
<g id="note1" class="reveal">
<text class="ts" x="430" y="70"><tspan font-weight="600">Hatching:</tspan> the blastocyst breaks</text>
<text class="ts" x="430" y="86">out of the zona — it cannot attach</text>
<text class="ts" x="430" y="102">to the uterus while still inside</text>
</g>
<g id="note2" class="reveal">
<text class="ts" x="430" y="70"><tspan font-weight="600">Attachment:</tspan> it sticks to the</text>
<text class="ts" x="430" y="86">uterine lining with the inner cell</text>
<text class="ts" x="430" y="102">mass side (embryonic pole) first</text>
</g>
<g id="note3" class="reveal">
<text class="ts" x="430" y="70">The trophoblast splits in two:</text>
<text class="ts" x="430" y="90"><tspan fill="#0F6E56" font-weight="600">Cytotrophoblast</tspan> — inner layer</text>
<text class="ts" x="430" y="106">of dividing cells</text>
<text class="ts" x="430" y="126"><tspan fill="#9D174D" font-weight="600">Syncytiotrophoblast</tspan> — fused cells,</text>
<text class="ts" x="430" y="142">many nuclei, invades the lining</text>
</g>
<g id="note4" class="reveal">
<text class="ts" x="430" y="70"><tspan font-weight="600">Invasion:</tspan> the syncytiotrophoblast</text>
<text class="ts" x="430" y="86">digests its way in; the embryo sinks</text>
<text class="ts" x="430" y="102">completely into the lining, which</text>
<text class="ts" x="430" y="118">then closes over it</text>
</g>
<g id="note5" class="reveal">
<text class="ts" x="430" y="70"><tspan fill="#B45309" font-weight="600">hCG</tspan> keeps the corpus luteum</text>
<text class="ts" x="430" y="86">making progesterone → the lining</text>
<text class="ts" x="430" y="102">is kept (no period)</text>
<text class="ts" x="430" y="122">hCG is what pregnancy tests detect</text>
<text class="ts" x="430" y="142">Maternal blood fills lacunae — the</text>
<text class="ts" x="430" y="158">first step toward the placenta</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 5</span>
</div>

<script>
let step = 0;
// blastocyst position and turn per step: [x, y, rotation°] — ICM starts at the top, turns to face the wall
const POS = [[200, 112, 0], [256, 140, 60], [360, 170, 180], [360, 170, 180], [360, 254, 180], [360, 254, 180]];
const days = ['Day 5', 'Day 5–6', 'Day 6–7', 'Day 7–8', 'Day 8–10', 'Day 10–12'];
const labels = [
  "Step 0 of 5 — day 5: the blastocyst, still inside its zona pellucida, floats in the uterine cavity",
  "Step 1 of 5 — hatching: the blastocyst breaks out of the zona pellucida, leaving the empty shell behind",
  "Step 2 of 5 — attachment: the blastocyst sticks to the uterine lining (endometrium) with its inner cell mass side facing the wall",
  "Step 3 of 5 — the trophoblast splits into cytotrophoblast (inner, dividing cells) and syncytiotrophoblast (outer, fused, many nuclei), which begins to invade",
  "Step 4 of 5 — invasion: the syncytiotrophoblast digests its way in and the embryo sinks completely into the endometrium, which closes over it",
  "Step 5 of 5 — the syncytiotrophoblast releases hCG, keeping progesterone high so the lining is maintained; maternal blood fills lacunae — the start of the placenta"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('dayLabelI').textContent = days[step];
  const [x, y, rot] = POS[step];
  document.getElementById('blasto').style.transform = `translate(${x}px, ${y}px) rotate(${rot}deg)`;
  document.getElementById('zonaWhole').style.opacity = step === 0 ? '1' : '0';
  document.getElementById('zonaBroken').style.opacity = step === 1 ? '1' : step === 2 ? '0.35' : '0';
  document.getElementById('synct3').classList.toggle('on', step === 3);
  document.getElementById('synct4').classList.toggle('on', step >= 4);
  document.getElementById('sealed').classList.toggle('on', step >= 4);
  document.getElementById('lacunae').classList.toggle('on', step >= 5);
  document.getElementById('hcgGroup').classList.toggle('on', step >= 5);
  for (let k = 0; k <= 5; k++) {
    document.getElementById('note' + k).classList.toggle('on', k === step);
    document.getElementById('lab' + k).classList.toggle('on', k === step);
  }
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# IMPLANTATION_TECHNICAL  (new)
# ---------------------------------------------------------------------------
IMPLANTATION_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of implantation: the progesterone-primed window of implantation, L-selectin apposition, integrin and osteopontin adhesion, syncytiotrophoblast invasion with syncytin and matrix metalloproteinases, decidualization with uterine NK cells, and hCG rescuing the corpus luteum.</h2>
<style>
  .reveal { opacity: 0; transition: opacity .5s ease; }
  .reveal.on { opacity: 1; }
  #blastoT { transition: transform 1.1s cubic-bezier(.3,0,.2,1); transform-box: view-box; transform-origin: 0 0; }
  .hcgT { animation: hcgUpT 2.4s ease-in infinite; }
  @keyframes hcgUpT { 0% { transform: translateY(0); opacity: 0; } 20% { opacity: 1; } 100% { transform: translateY(-34px); opacity: 0; } }
  @media (prefers-reduced-motion: reduce) { .hcgT { animation: none; } }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Implantation, technical view</title>
<desc>Implantation is only possible during a short window of implantation, about 6 to 10 days after ovulation, when progesterone from the corpus luteum has made the endometrium receptive: the epithelium grows pinopodes and secretes LIF. After hatching, the blastocyst makes loose contact as L-selectin on the trophoblast binds sugar ligands on the uterine epithelium, then firm adhesion forms as alpha-v beta-3 integrins on both surfaces are bridged by osteopontin. Trophoblast cells fuse, using syncytin, into an invasive syncytiotrophoblast that secretes matrix metalloproteinases to digest the extracellular matrix and push into the stroma. Around the embryo, progesterone turns stromal cells into swollen, glycogen-rich decidual cells, and uterine natural killer cells gather; together they nourish the embryo and keep invasion controlled. The syncytiotrophoblast then secretes hCG, which binds the LH/hCG receptor on the corpus luteum and keeps it producing progesterone, maintaining the decidua, while eroded maternal vessels fill lacunae with blood, beginning the uteroplacental circulation.</desc>
<defs>
<marker id="arrowIT" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<text class="ts" x="40" y="40">Uterine cavity</text>
<text class="th" x="40" y="62" id="dayLabelIT">Day 6</text>

<rect x="30" y="210" width="620" height="110" fill="#FBCFE8" fill-opacity="0.55"/>
<line x1="30" y1="210" x2="650" y2="210" stroke="#BE185D" stroke-width="2"/>
<path d="M60 211 Q60 262 74 262 Q88 262 88 211" fill="none" stroke="#BE185D" stroke-width="1.2" stroke-opacity="0.6"/>
<path d="M110 211 Q110 270 124 270 Q138 270 138 211" fill="none" stroke="#BE185D" stroke-width="1.2" stroke-opacity="0.6"/>
<path d="M560 211 Q560 266 574 266 Q588 266 588 211" fill="none" stroke="#BE185D" stroke-width="1.2" stroke-opacity="0.6"/>
<path d="M610 211 Q610 258 624 258 Q638 258 638 211" fill="none" stroke="#BE185D" stroke-width="1.2" stroke-opacity="0.6"/>
<path d="M170 320 C158 296 182 284 170 262 C160 244 182 236 176 222" fill="none" stroke="#B91C1C" stroke-width="3" stroke-opacity="0.75"/>
<path d="M520 320 C532 296 508 284 520 262 C530 244 508 236 514 222" fill="none" stroke="#B91C1C" stroke-width="3" stroke-opacity="0.75"/>
<text class="ts" x="40" y="312">Endometrium</text>

<g id="pinopodes" class="reveal">
<path d="M270 210 Q276 199 282 210" fill="#FBCFE8" stroke="#BE185D" stroke-width="1.2"/>
<path d="M292 210 Q298 199 304 210" fill="#FBCFE8" stroke="#BE185D" stroke-width="1.2"/>
<path d="M314 210 Q320 199 326 210" fill="#FBCFE8" stroke="#BE185D" stroke-width="1.2"/>
<path d="M336 210 Q342 199 348 210" fill="#FBCFE8" stroke="#BE185D" stroke-width="1.2"/>
<path d="M358 210 Q364 199 370 210" fill="#FBCFE8" stroke="#BE185D" stroke-width="1.2"/>
<path d="M380 210 Q386 199 392 210" fill="#FBCFE8" stroke="#BE185D" stroke-width="1.2"/>
<path d="M402 210 Q408 199 414 210" fill="#FBCFE8" stroke="#BE185D" stroke-width="1.2"/>
<path d="M424 210 Q430 199 436 210" fill="#FBCFE8" stroke="#BE185D" stroke-width="1.2"/>
</g>
<circle id="zonaWT" cx="200" cy="112" r="49" fill="none" stroke="#B45309" stroke-width="2.5" stroke-opacity="0.65"/>
<path id="zonaBT" d="M236 145 A49 49 0 1 1 245 132" fill="none" stroke="#B45309" stroke-width="2.5" stroke-opacity="0.65" style="opacity:0;transition:opacity .5s ease"/>

<path id="synctA" class="reveal" d="M322 214 Q360 266 398 214 Q360 240 322 214 Z" fill="#9D174D" fill-opacity="0.55"/>
<path id="synctB" class="reveal" d="M314 252 Q312 316 360 316 Q408 316 406 252 Q394 300 360 300 Q326 300 314 252 Z" fill="#9D174D" fill-opacity="0.55"/>
<g id="mmp" class="reveal">
<circle cx="330" cy="246" r="4" fill="#EA580C"/><circle cx="360" cy="262" r="4" fill="#EA580C"/><circle cx="390" cy="246" r="4" fill="#EA580C"/>
<path d="M318 252 l-8 6 M402 252 l8 6 M360 270 l0 9" stroke="#EA580C" stroke-width="1.5" stroke-dasharray="2 2"/>
</g>
<g id="decidua" class="reveal">
<circle cx="429.5" cy="244.5" r="9" fill="#FEF3C7" stroke="#D97706" stroke-width="1"/>
<circle cx="429.5" cy="271.5" r="9" fill="#FEF3C7" stroke="#D97706" stroke-width="1"/>
<circle cx="410.9" cy="294.8" r="9" fill="#FEF3C7" stroke="#D97706" stroke-width="1"/>
<circle cx="378.6" cy="308.2" r="9" fill="#FEF3C7" stroke="#D97706" stroke-width="1"/>
<circle cx="341.4" cy="308.2" r="9" fill="#FEF3C7" stroke="#D97706" stroke-width="1"/>
<circle cx="309.1" cy="294.8" r="9" fill="#FEF3C7" stroke="#D97706" stroke-width="1"/>
<circle cx="290.5" cy="271.5" r="9" fill="#FEF3C7" stroke="#D97706" stroke-width="1"/>
<circle cx="290.5" cy="244.5" r="9" fill="#FEF3C7" stroke="#D97706" stroke-width="1"/>
<circle cx="300" cy="300" r="4" class="c-purple"/><circle cx="420" cy="303" r="4" class="c-purple"/><circle cx="440" cy="244" r="4" class="c-purple"/>
</g>
<g id="lacunaeT" class="reveal">
<ellipse cx="334" cy="300" rx="7" ry="4" fill="#B91C1C"/><ellipse cx="360" cy="308" rx="8" ry="4" fill="#B91C1C"/><ellipse cx="386" cy="300" rx="7" ry="4" fill="#B91C1C"/>
</g>

<g id="blastoT">
<circle r="34" fill="#378ADD" fill-opacity="0.12"/>
<circle r="38" fill="none" stroke="#0F6E56" stroke-width="7" stroke-opacity="0.55"/>
<circle cx="0" cy="-28" r="8" class="c-purple"/><circle cx="-13" cy="-23" r="7" class="c-purple"/><circle cx="13" cy="-23" r="7" class="c-purple"/>
<circle cx="-6" cy="-15" r="6" class="c-purple"/><circle cx="6" cy="-15" r="6" class="c-purple"/>
</g>
<g id="selectin" class="reveal">
<line x1="334" y1="201" x2="334" y2="205" stroke="#0F6E56" stroke-width="1.5"/><path d="M331 208 L334 205 L337 208" fill="none" stroke="#0F6E56" stroke-width="1.5"/><circle cx="334" cy="209.5" r="2.4" fill="#F59E0B"/>
<line x1="347" y1="201" x2="347" y2="205" stroke="#0F6E56" stroke-width="1.5"/><path d="M344 208 L347 205 L350 208" fill="none" stroke="#0F6E56" stroke-width="1.5"/><circle cx="347" cy="209.5" r="2.4" fill="#F59E0B"/>
<line x1="360" y1="201" x2="360" y2="205" stroke="#0F6E56" stroke-width="1.5"/><path d="M357 208 L360 205 L363 208" fill="none" stroke="#0F6E56" stroke-width="1.5"/><circle cx="360" cy="209.5" r="2.4" fill="#F59E0B"/>
<line x1="373" y1="201" x2="373" y2="205" stroke="#0F6E56" stroke-width="1.5"/><path d="M370 208 L373 205 L376 208" fill="none" stroke="#0F6E56" stroke-width="1.5"/><circle cx="373" cy="209.5" r="2.4" fill="#F59E0B"/>
<line x1="386" y1="201" x2="386" y2="205" stroke="#0F6E56" stroke-width="1.5"/><path d="M383 208 L386 205 L389 208" fill="none" stroke="#0F6E56" stroke-width="1.5"/><circle cx="386" cy="209.5" r="2.4" fill="#F59E0B"/>
</g>
<g id="integrins" class="reveal">
<rect x="335" y="203" width="2.5" height="10" fill="#0F6E56"/><rect x="338.5" y="203" width="2.5" height="10" fill="#BE185D"/><circle cx="338" cy="208" r="2" fill="#7C3AED"/>
<rect x="349" y="203" width="2.5" height="10" fill="#0F6E56"/><rect x="352.5" y="203" width="2.5" height="10" fill="#BE185D"/><circle cx="352" cy="208" r="2" fill="#7C3AED"/>
<rect x="365" y="203" width="2.5" height="10" fill="#0F6E56"/><rect x="368.5" y="203" width="2.5" height="10" fill="#BE185D"/><circle cx="368" cy="208" r="2" fill="#7C3AED"/>
<rect x="379" y="203" width="2.5" height="10" fill="#0F6E56"/><rect x="382.5" y="203" width="2.5" height="10" fill="#BE185D"/><circle cx="382" cy="208" r="2" fill="#7C3AED"/>
</g>
<path id="sealedT" class="reveal" d="M316 210 Q360 204 404 210" fill="none" stroke="#BE185D" stroke-width="3" stroke-linecap="round"/>

<g id="hcgT" class="reveal">
<circle class="hcgT" cx="330" cy="292" r="3.5" fill="#F59E0B"/><circle class="hcgT" cx="350" cy="300" r="3.5" fill="#F59E0B" style="animation-delay:.6s"/>
<circle class="hcgT" cx="372" cy="300" r="3.5" fill="#F59E0B" style="animation-delay:1.2s"/><circle class="hcgT" cx="392" cy="292" r="3.5" fill="#F59E0B" style="animation-delay:1.8s"/>
<line x1="410" y1="290" x2="510" y2="268" stroke="#B45309" stroke-width="1.2" marker-end="url(#arrowIT)"/>
<text class="ts" x="536" y="292" font-weight="600" fill="#B45309">hCG → blood</text>
<rect x="40" y="84" width="200" height="92" rx="10" fill="#FFFBEB" stroke="#D97706" stroke-width="1"/>
<circle cx="76" cy="130" r="20" fill="#FDE68A" stroke="#B45309" stroke-width="1.2"/>
<path d="M60 116 l-4 -4 M92 116 l4 -4 M60 144 l-4 4 M92 144 l4 4" stroke="#B45309" stroke-width="2"/>
<text class="ts" x="104" y="104" font-weight="600">Corpus luteum (ovary)</text>
<text class="ts" x="104" y="122">hCG binds LH/hCG</text>
<text class="ts" x="104" y="138">receptor → keeps making</text>
<text class="ts" x="104" y="154">progesterone</text>
<text class="ts" x="104" y="170">→ decidua maintained</text>
</g>

<g id="labIT0" class="reveal">
<text class="ts" x="270" y="196" text-anchor="end">Pinopodes</text>
<text class="ts" x="200" y="52" text-anchor="middle">Zona pellucida</text>
</g>
<g id="labIT1" class="reveal">
<text class="ts" x="324" y="194" text-anchor="end">L-selectin ↔ sugar ligands</text>
</g>
<g id="labIT2" class="reveal">
<text class="ts" x="316" y="200" text-anchor="end">αvβ3 integrins + osteopontin</text>
</g>
<g id="labIT3" class="reveal">
<line x1="322" y1="180" x2="296" y2="168" stroke="var(--t)" stroke-width="0.75"/>
<text class="ts" x="292" y="166" text-anchor="end">Cytotrophoblast</text>
<line x1="332" y1="226" x2="296" y2="236" stroke="var(--t)" stroke-width="0.75"/>
<text class="ts" x="292" y="240" text-anchor="end">Syncytiotrophoblast</text>
<text class="ts" x="410" y="262" font-weight="600" fill="#EA580C">MMPs</text>
</g>
<g id="labIT4" class="reveal">
<line x1="281" y1="271" x2="266" y2="266" stroke="var(--t)" stroke-width="0.75"/>
<text class="ts" x="262" y="268" text-anchor="end">Decidual cells</text>
<line x1="297" y1="303" x2="288" y2="310" stroke="var(--t)" stroke-width="0.75"/>
<text class="ts" x="284" y="316" text-anchor="end">uNK cells</text>
</g>
<g id="labIT5" class="reveal">
<line x1="327" y1="303" x2="300" y2="313" stroke="var(--t)" stroke-width="0.75"/>
<text class="ts" x="296" y="317" text-anchor="end">Blood-filled lacunae</text>
</g>

<g id="noteIT0" class="reveal">
<text class="ts" x="430" y="56"><tspan font-weight="600">Window of implantation</tspan></text>
<text class="ts" x="430" y="72">~6–10 days after ovulation only</text>
<text class="ts" x="430" y="92">Progesterone (corpus luteum)</text>
<text class="ts" x="430" y="108">makes the lining receptive:</text>
<text class="ts" x="430" y="124">pinopodes + LIF secretion</text>
</g>
<g id="noteIT1" class="reveal">
<text class="ts" x="430" y="56"><tspan font-weight="600">Hatching + apposition</tspan></text>
<text class="ts" x="430" y="72">Proteases free it from the zona;</text>
<text class="ts" x="430" y="88"><tspan fill="#0F6E56" font-weight="600">L-selectin</tspan> on trophoblast binds</text>
<text class="ts" x="430" y="104"><tspan fill="#B45309" font-weight="600">sugar ligands</tspan> on the epithelium</text>
<text class="ts" x="430" y="120">— loose, reversible contact</text>
</g>
<g id="noteIT2" class="reveal">
<text class="ts" x="430" y="56"><tspan font-weight="600">Adhesion</tspan></text>
<text class="ts" x="430" y="72"><tspan fill="#0F6E56" font-weight="600">αvβ3</tspan> integrins on trophoblast</text>
<text class="ts" x="430" y="88">and <tspan fill="#BE185D" font-weight="600">αvβ3</tspan> on the epithelium,</text>
<text class="ts" x="430" y="104">bridged by <tspan fill="#7C3AED" font-weight="600">osteopontin</tspan></text>
<text class="ts" x="430" y="120">— firm attachment</text>
</g>
<g id="noteIT3" class="reveal">
<text class="ts" x="430" y="56"><tspan font-weight="600">Invasion</tspan></text>
<text class="ts" x="430" y="72">Trophoblast cells fuse (syncytin,</text>
<text class="ts" x="430" y="88">a retroviral gene) into the</text>
<text class="ts" x="430" y="104"><tspan fill="#9D174D" font-weight="600">syncytiotrophoblast</tspan>, which</text>
<text class="ts" x="430" y="120">secretes <tspan fill="#EA580C" font-weight="600">MMPs</tspan> to digest the matrix</text>
</g>
<g id="noteIT4" class="reveal">
<text class="ts" x="430" y="56"><tspan font-weight="600">Decidualization</tspan></text>
<text class="ts" x="430" y="72">Progesterone turns stromal cells</text>
<text class="ts" x="430" y="88">into swollen, glycogen-rich</text>
<text class="ts" x="430" y="104"><tspan fill="#B45309" font-weight="600">decidual cells</tspan>; <tspan fill="#6D28D9" font-weight="600">uNK cells</tspan> gather</text>
<text class="ts" x="430" y="120">— nourish the embryo and</text>
<text class="ts" x="430" y="136">keep invasion under control</text>
</g>
<g id="noteIT5" class="reveal">
<text class="ts" x="430" y="56"><tspan font-weight="600">Maternal recognition</tspan></text>
<text class="ts" x="430" y="72"><tspan fill="#B45309" font-weight="600">hCG</tspan> rescues the corpus luteum,</text>
<text class="ts" x="430" y="88">so progesterone stays high</text>
<text class="ts" x="430" y="104">Eroded maternal vessels fill</text>
<text class="ts" x="430" y="120">lacunae — the uteroplacental</text>
<text class="ts" x="430" y="136">circulation begins</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 5</span>
</div>

<script>
let step = 0;
// [x, y, rotation°]: in the zona -> just above the epithelium (loose) -> touching (firm) -> half sunk -> fully embedded
const POS = [[200, 112, 0], [360, 160, 180], [360, 169, 180], [360, 192, 180], [360, 254, 180], [360, 254, 180]];
const days = ['Day 6', 'Day 6–7', 'Day 7', 'Day 7–8', 'Day 8–10', 'Day 10–12'];
const labels = [
  "Step 0 of 5 — window of implantation: progesterone from the corpus luteum makes the endometrium receptive (pinopodes, LIF) for only a few days",
  "Step 1 of 5 — hatching and apposition: proteases free the blastocyst from the zona; L-selectin on the trophoblast binds sugar ligands on the epithelium — a loose, reversible contact",
  "Step 2 of 5 — adhesion: αvβ3 integrins on trophoblast and epithelium are bridged by osteopontin, firmly attaching the embryonic pole",
  "Step 3 of 5 — invasion: trophoblast cells fuse via syncytin into the syncytiotrophoblast, which secretes matrix metalloproteinases (MMPs) and digests its way into the stroma",
  "Step 4 of 5 — decidualization: progesterone turns the surrounding stromal cells into glycogen-rich decidual cells, and uterine NK cells gather — nourishing the embryo and limiting invasion",
  "Step 5 of 5 — hCG from the syncytiotrophoblast binds the LH/hCG receptor on the corpus luteum, keeping progesterone high; lacunae fill with maternal blood as the uteroplacental circulation begins"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('dayLabelIT').textContent = days[step];
  const [x, y, rot] = POS[step];
  document.getElementById('blastoT').style.transform = `translate(${x}px, ${y}px) rotate(${rot}deg)`;
  document.getElementById('zonaWT').style.opacity = step === 0 ? '1' : '0';
  document.getElementById('zonaBT').style.opacity = step === 1 ? '0.4' : '0';
  const on = (id, v) => document.getElementById(id).classList.toggle('on', v);
  on('pinopodes', step <= 2);
  on('selectin', step === 1);
  on('integrins', step === 2);
  on('synctA', step === 3);
  on('mmp', step === 3);
  on('synctB', step >= 4);
  on('sealedT', step >= 4);
  on('decidua', step >= 4);
  on('lacunaeT', step >= 5);
  on('hcgT', step >= 5);
  for (let k = 0; k <= 5; k++) { on('noteIT' + k, k === step); on('labIT' + k, k === step); }
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# NEURULATION_GENERAL  (new)
# ---------------------------------------------------------------------------
NEURULATION_GENERAL = '''
<h2 class="sr-only">Interactive cross-section of neurulation: the notochord induces the ectoderm above it to form the neural plate, the plate edges rise as neural folds around a neural groove, the folds fuse into the neural tube beneath the surface ectoderm, and neural crest cells from the fold tips migrate away.</h2>
<style>
  .reveal { opacity: 0; transition: opacity .5s ease; }
  .reveal.on { opacity: 1; }
  .sheet { fill: none; stroke-linecap: round; transition: d 1s cubic-bezier(.3,0,.2,1), stroke .6s ease, stroke-width .6s ease; }
  .crest { transition: cx 1s cubic-bezier(.3,0,.2,1), cy 1s cubic-bezier(.3,0,.2,1), r .6s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 330" role="img">
<title>Neurulation, cross-section</title>
<desc>Seen in cross-section, the embryo after gastrulation is a flat sheet of three layers: ectoderm on top, mesoderm in the middle with the rod-shaped notochord along the midline, and endoderm below. Signals from the notochord make the ectoderm above it thicken into the neural plate. The edges of the plate rise as neural folds, leaving a neural groove in the middle, and curl toward each other; cells at the tips of the folds become neural crest cells. The folds fuse into a hollow neural tube that sinks beneath the surface ectoderm, which seals over the top. The neural tube becomes the brain and spinal cord, the neural crest cells migrate away to form peripheral nerves, pigment cells and parts of the face, and the mesoderm beside the tube forms somites. If the tube fails to close, anencephaly or spina bifida results; folic acid lowers the risk.</desc>
<defs>
<marker id="arrowN" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<text class="th" x="30" y="30" id="dayLabelN">Day 17–18</text>
<text class="ts" x="30" y="48" id="stageLabelN">Three-layered embryo</text>

<!-- mesoderm on each side, notochord at the midline, endoderm below -->
<rect x="64" y="140" width="176" height="46" rx="14" fill="#C4B5FD" fill-opacity="0.55" stroke="#6D28D9" stroke-width="1"/>
<rect x="360" y="140" width="176" height="46" rx="14" fill="#C4B5FD" fill-opacity="0.55" stroke="#6D28D9" stroke-width="1"/>
<circle cx="300" cy="190" r="12" fill="#FDBA74" stroke="#C2410C" stroke-width="1.2"/>
<line x1="60" y1="222" x2="540" y2="222" stroke="#D85A30" stroke-width="8" stroke-linecap="round" stroke-opacity="0.85"/>

<!-- ectoderm: two surface halves (future skin) and the central neural plate, reshaped step by step -->
<path id="surfL" class="sheet" d="M60 120 C150 120 200 120 230 120" stroke="#378ADD" stroke-width="10"/>
<path id="surfR" class="sheet" d="M370 120 C400 120 450 120 540 120" stroke="#378ADD" stroke-width="10"/>
<path id="plate" class="sheet" d="M230 120 C260 120 270 120 300 120 C330 120 340 120 370 120" stroke="#378ADD" stroke-width="10"/>

<circle id="crestL" class="crest" cx="230" cy="120" r="0" fill="#16A34A" stroke="#14532D" stroke-width="1"/>
<circle id="crestR" class="crest" cx="370" cy="120" r="0" fill="#16A34A" stroke="#14532D" stroke-width="1"/>

<g id="signals" class="reveal">
<line x1="284" y1="178" x2="276" y2="134" stroke="#C2410C" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrowN)"/>
<line x1="300" y1="176" x2="300" y2="134" stroke="#C2410C" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrowN)"/>
<line x1="316" y1="178" x2="324" y2="134" stroke="#C2410C" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrowN)"/>
</g>
<g id="migrate" class="reveal">
<path d="M262 104 Q236 126 226 160" fill="none" stroke="#16A34A" stroke-width="1.5" marker-end="url(#arrowN)"/>
<path d="M338 104 Q364 126 374 160" fill="none" stroke="#16A34A" stroke-width="1.5" marker-end="url(#arrowN)"/>
</g>

<!-- layer labels (always) -->
<text class="ts" x="550" y="124">Ectoderm</text>
<text class="ts" x="550" y="167">Mesoderm</text>
<text class="ts" x="550" y="226">Endoderm</text>
<text class="ts" x="300" y="212" text-anchor="middle">Notochord</text>

<!-- step-specific structure labels -->
<g id="labN1" class="reveal"><text class="ts" x="300" y="104" text-anchor="middle" font-weight="600" fill="#4338CA">Neural plate</text></g>
<g id="labN2" class="reveal">
<text class="ts" x="300" y="96" text-anchor="middle">Neural groove</text>
<text class="ts" x="214" y="94" text-anchor="middle">Neural fold</text>
<text class="ts" x="386" y="94" text-anchor="middle">Neural fold</text>
</g>
<g id="labN3" class="reveal"><text class="ts" x="300" y="50" text-anchor="middle" font-weight="600" fill="#15803D">Neural crest cells</text></g>
<g id="labN4" class="reveal">
<text class="ts" x="300" y="128" text-anchor="middle" font-weight="600" fill="#4338CA">Neural</text>
<text class="ts" x="300" y="142" text-anchor="middle" font-weight="600" fill="#4338CA">tube</text>
<text class="ts" x="300" y="64" text-anchor="middle" fill="#15803D">Neural crest</text>
<text class="ts" x="60" y="96" text-anchor="start">Surface ectoderm (skin)</text>
</g>
<g id="labN5" class="reveal">
<text class="ts" x="300" y="128" text-anchor="middle" font-weight="600" fill="#4338CA">Neural</text>
<text class="ts" x="300" y="142" text-anchor="middle" font-weight="600" fill="#4338CA">tube</text>
<text class="ts" x="392" y="132" text-anchor="start" font-weight="600" fill="#4338CA">← brain &amp; spinal cord</text>
<text class="ts" x="152" y="167" text-anchor="middle">Somites</text>
<text class="ts" x="448" y="167" text-anchor="middle">Somites</text>
<text class="ts" x="300" y="64" text-anchor="middle" fill="#15803D">Neural crest migrates out</text>
</g>

<!-- explanation under the diagram -->
<g id="noteN0" class="reveal">
<text class="ts" x="30" y="262">After gastrulation the embryo is a flat sheet of three layers.</text>
<text class="ts" x="30" y="278">The notochord, a rod of mesoderm, runs along the midline.</text>
</g>
<g id="noteN1" class="reveal">
<text class="ts" x="30" y="262"><tspan font-weight="600">Induction:</tspan> signals from the notochord make the ectoderm above it</text>
<text class="ts" x="30" y="278">thicken into the <tspan fill="#4338CA" font-weight="600">neural plate</tspan> — the future nervous system.</text>
</g>
<g id="noteN2" class="reveal">
<text class="ts" x="30" y="262">The edges of the plate rise as <tspan font-weight="600">neural folds</tspan>,</text>
<text class="ts" x="30" y="278">leaving a <tspan font-weight="600">neural groove</tspan> down the middle.</text>
</g>
<g id="noteN3" class="reveal">
<text class="ts" x="30" y="262">The folds curl toward each other. Cells at their tips become</text>
<text class="ts" x="30" y="278"><tspan fill="#15803D" font-weight="600">neural crest cells</tspan>.</text>
</g>
<g id="noteN4" class="reveal">
<text class="ts" x="30" y="262">The folds fuse into the hollow <tspan fill="#4338CA" font-weight="600">neural tube</tspan>, which sinks below the</text>
<text class="ts" x="30" y="278">surface ectoderm; the surface (future skin) seals over the top.</text>
</g>
<g id="noteN5" class="reveal">
<text class="ts" x="30" y="262">The tube becomes the brain and spinal cord; <tspan fill="#15803D" font-weight="600">neural crest</tspan> cells form nerves, pigment</text>
<text class="ts" x="30" y="278">cells and facial bones. Closure ends by ~day 28 — if it fails: anencephaly (head end)</text>
<text class="ts" x="30" y="294">or spina bifida (lower spine). <tspan font-weight="600">Folic acid</tspan> before and in early pregnancy lowers the risk.</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 5</span>
</div>

<script>
let step = 0;
// ectoderm shapes per step (same path structure in every step so the sheet can morph smoothly)
const SURF_L = [
  "M60 120 C150 120 200 120 230 120", "M60 120 C150 120 200 120 230 120",
  "M60 120 C150 120 200 112 226 104", "M60 120 C170 120 240 100 276 70",
  "M60 120 C170 120 240 80 300 80",   "M60 120 C170 120 240 80 300 80"
];
const SURF_R = [
  "M370 120 C400 120 450 120 540 120", "M370 120 C400 120 450 120 540 120",
  "M374 104 C400 112 450 120 540 120", "M324 70 C360 100 430 120 540 120",
  "M300 80 C360 80 430 120 540 120",   "M300 80 C360 80 430 120 540 120"
];
const PLATE = [
  "M230 120 C260 120 270 120 300 120 C330 120 340 120 370 120",
  "M230 120 C260 120 270 120 300 120 C330 120 340 120 370 120",
  "M226 104 C240 112 268 164 300 164 C332 164 360 112 374 104",
  "M276 70 C236 84 256 168 300 168 C344 168 364 84 324 70",
  "M300 100 C262 100 262 160 300 160 C338 160 338 100 300 100",
  "M300 100 C262 100 262 160 300 160 C338 160 338 100 300 100"
];
// neural crest cells: [xL, yL, xR, yR, r]
const CREST = [[230,120,370,120,0],[230,120,370,120,0],[226,104,374,104,6],[276,70,324,70,6],[285,92,315,92,6],[240,132,360,132,6]];
const days   = ['Day 17–18', 'Day 18', 'Day 19–20', 'Day 20–21', 'Day 21–22', 'Day 22–28'];
const stages = ['Three-layered embryo', 'Neural plate', 'Neural folds and groove', 'Folds curl together', 'Neural tube', 'Tube and neural crest'];
const labels = [
  "Step 0 of 5 — after gastrulation: ectoderm on top, mesoderm with the notochord in the middle, endoderm below",
  "Step 1 of 5 — induction: the notochord signals the ectoderm above it, which thickens into the neural plate",
  "Step 2 of 5 — the plate's edges rise as neural folds, leaving a neural groove in the middle",
  "Step 3 of 5 — the folds curl toward each other; cells at their tips become neural crest cells",
  "Step 4 of 5 — the folds fuse into the neural tube, which sinks under the surface ectoderm as it seals over",
  "Step 5 of 5 — the tube becomes the brain and spinal cord, neural crest cells migrate away, and somites form beside the tube"
];
function setD(id, d) { const el = document.getElementById(id); el.setAttribute('d', d); el.style.d = `path("${d}")`; }
function setC(id, x, y, r) { const el = document.getElementById(id);
  el.setAttribute('cx', x); el.setAttribute('cy', y); el.setAttribute('r', r);
  el.style.cx = x + 'px'; el.style.cy = y + 'px'; el.style.r = r + 'px'; }
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('dayLabelN').textContent = days[step];
  document.getElementById('stageLabelN').textContent = stages[step];
  setD('surfL', SURF_L[step]); setD('surfR', SURF_R[step]); setD('plate', PLATE[step]);
  const plate = document.getElementById('plate');
  plate.setAttribute('stroke', step >= 1 ? '#4338CA' : '#378ADD');        // neural ectoderm once induced
  plate.setAttribute('stroke-width', step >= 1 ? '14' : '10');            // thickened plate
  const [xl, yl, xr, yr, r] = CREST[step];
  setC('crestL', xl, yl, r); setC('crestR', xr, yr, r);
  const on = (id, v) => document.getElementById(id).classList.toggle('on', v);
  on('signals', step === 1);
  on('migrate', step === 5);
  for (let k = 0; k <= 5; k++) { on('noteN' + k, k === step); if (k >= 1) on('labN' + k, k === step); }
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# NEURULATION_TECHNICAL  (new)
# ---------------------------------------------------------------------------
NEURULATION_TECHNICAL = '''
<h2 class="sr-only">Technical cross-section of neurulation: BMP antagonists induce the neural plate, convergent extension narrows it, hinge points bend it by apical constriction, a switch from E-cadherin to N-cadherin separates the fused tube from the surface ectoderm, neural crest cells undergo an epithelial-to-mesenchymal transition, and opposing Shh and BMP gradients pattern the tube from ventral to dorsal.</h2>
<style>
  .reveal { opacity: 0; transition: opacity .5s ease; }
  .reveal.on { opacity: 1; }
  .sheetT { fill: none; stroke-linecap: round; transition: d 1s cubic-bezier(.3,0,.2,1), stroke .6s ease, stroke-width .6s ease; }
  .crestT { transition: cx 1s cubic-bezier(.3,0,.2,1), cy 1s cubic-bezier(.3,0,.2,1), r .6s ease, stroke-width .4s ease; }
  #layerLabelsT { transition: opacity .5s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Neurulation, technical view</title>
<desc>BMP signalling in the ectoderm promotes epidermis; the organizer and notochord secrete the BMP antagonists Noggin, Chordin and Follistatin, and where BMP is blocked the ectoderm becomes neural plate by default. Plate cells elongate and intercalate by convergent extension, driven by planar cell polarity, so the plate narrows and lengthens. At the medial hinge point above the notochord and at paired dorsolateral hinge points, apical actomyosin constriction makes the cells wedge-shaped and the folds rise. When the folds meet, the neural plate has switched from E-cadherin to N-cadherin, letting the tube separate from the E-cadherin surface ectoderm. Neural crest cells at the border, specified by intermediate BMP plus Wnt, express Snail and Slug, FoxD3 and Sox10, lose their junctions in an epithelial-to-mesenchymal transition and migrate. Finally Sonic hedgehog from the notochord induces the floor plate, which also secretes Sonic hedgehog and patterns ventral motor neurons, while BMP and Wnt from the roof plate and surface ectoderm pattern dorsal sensory interneurons.</desc>
<defs>
<marker id="arrowNT" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></marker>
<linearGradient id="dvGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#38BDF8" stop-opacity="0.85"/><stop offset="0.5" stop-color="#ffffff" stop-opacity="0.2"/><stop offset="1" stop-color="#EA580C" stop-opacity="0.75"/></linearGradient>
</defs>

<text class="th" x="30" y="30" id="dayLabelNT">Day 17–18</text>
<text class="ts" x="30" y="48" id="stageLabelNT">Neural induction</text>

<rect x="64" y="140" width="176" height="46" rx="14" fill="#C4B5FD" fill-opacity="0.55" stroke="#6D28D9" stroke-width="1"/>
<rect x="360" y="140" width="176" height="46" rx="14" fill="#C4B5FD" fill-opacity="0.55" stroke="#6D28D9" stroke-width="1"/>
<circle cx="300" cy="190" r="12" fill="#FDBA74" stroke="#C2410C" stroke-width="1.2"/>
<line x1="60" y1="222" x2="540" y2="222" stroke="#D85A30" stroke-width="8" stroke-linecap="round" stroke-opacity="0.85"/>
<text class="ts" x="300" y="212" text-anchor="middle">Notochord</text>

<ellipse id="dvFill" class="reveal" cx="300" cy="130" rx="26" ry="26" fill="url(#dvGrad)"/>
<path id="surfLT" class="sheetT" d="M60 120 C150 120 200 120 230 120" stroke="#378ADD" stroke-width="10"/>
<path id="surfRT" class="sheetT" d="M370 120 C400 120 450 120 540 120" stroke="#378ADD" stroke-width="10"/>
<path id="plateT" class="sheetT" d="M230 120 C260 120 270 120 300 120 C330 120 340 120 370 120" stroke="#4338CA" stroke-width="14"/>
<path id="roofP" class="reveal" d="M284 103 Q300 95 316 103" fill="none" stroke="#38BDF8" stroke-width="7" stroke-linecap="round"/>
<path id="floorP" class="reveal" d="M286 157 Q300 164 314 157" fill="none" stroke="#EA580C" stroke-width="6" stroke-linecap="round"/>

<circle id="crestLT" class="crestT" cx="230" cy="120" r="0" fill="#16A34A" stroke="#14532D" stroke-width="1"/>
<circle id="crestRT" class="crestT" cx="370" cy="120" r="0" fill="#16A34A" stroke="#14532D" stroke-width="1"/>

<!-- step 0: BMP on the lateral ectoderm vs antagonists from the notochord -->
<g id="bmpT" class="reveal">
<line x1="110" y1="80" x2="110" y2="108" stroke="#1D4ED8" stroke-width="1.6" marker-end="url(#arrowNT)"/>
<line x1="170" y1="80" x2="170" y2="108" stroke="#1D4ED8" stroke-width="1.6" marker-end="url(#arrowNT)"/>
<line x1="430" y1="80" x2="430" y2="108" stroke="#1D4ED8" stroke-width="1.6" marker-end="url(#arrowNT)"/>
<line x1="490" y1="80" x2="490" y2="108" stroke="#1D4ED8" stroke-width="1.6" marker-end="url(#arrowNT)"/>
<text class="ts" x="140" y="72" text-anchor="middle" font-weight="600" fill="#1D4ED8">BMP → epidermis</text>
<text class="ts" x="460" y="72" text-anchor="middle" font-weight="600" fill="#1D4ED8">BMP → epidermis</text>
<line x1="284" y1="178" x2="276" y2="134" stroke="#C2410C" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrowNT)"/>
<line x1="300" y1="176" x2="300" y2="134" stroke="#C2410C" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrowNT)"/>
<line x1="316" y1="178" x2="324" y2="134" stroke="#C2410C" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrowNT)"/>
<text class="ts" x="300" y="96" text-anchor="middle" font-weight="600" fill="#4338CA">Neural plate (BMP blocked)</text>
</g>
<!-- step 1: convergent extension -->
<g id="ceT" class="reveal">
<line x1="222" y1="100" x2="252" y2="100" stroke="#4338CA" stroke-width="1.6" marker-end="url(#arrowNT)"/>
<line x1="378" y1="100" x2="348" y2="100" stroke="#4338CA" stroke-width="1.6" marker-end="url(#arrowNT)"/>
<text class="ts" x="300" y="88" text-anchor="middle" font-weight="600" fill="#4338CA">Narrows and lengthens</text>
</g>
<!-- step 2: hinge points -->
<g id="hingeT" class="reveal">
<path d="M294 156 L306 156 L300 167 Z" fill="#F59E0B" stroke="#B45309" stroke-width="1"/>
<path d="M240 119 L251 119 L245.5 130 Z" fill="#F59E0B" stroke="#B45309" stroke-width="1"/>
<path d="M349 119 L360 119 L354.5 130 Z" fill="#F59E0B" stroke="#B45309" stroke-width="1"/>
<text class="ts" x="300" y="148" text-anchor="middle" font-weight="600" fill="#B45309">MHP</text>
<text class="ts" x="236" y="136" text-anchor="end" font-weight="600" fill="#B45309">DLHP</text>
<text class="ts" x="364" y="136" text-anchor="start" font-weight="600" fill="#B45309">DLHP</text>
</g>
<!-- step 3: cadherin switch -->
<g id="cadT" class="reveal">
<text class="ts" x="120" y="104" text-anchor="middle" font-weight="600" fill="#1D4ED8">E-cadherin</text>
<text class="ts" x="480" y="104" text-anchor="middle" font-weight="600" fill="#1D4ED8">E-cadherin</text>
<text class="ts" x="300" y="128" text-anchor="middle" font-weight="600" fill="#4338CA">N-cadherin</text>
</g>
<!-- step 4: neural crest EMT -->
<g id="emtT" class="reveal">
<text class="ts" x="300" y="56" text-anchor="middle" font-weight="600" fill="#15803D">Neural crest EMT: Snail/Slug, FoxD3, Sox10</text>
<text class="ts" x="300" y="70" text-anchor="middle" fill="#15803D">junctions lost → migratory</text>
<text class="ts" x="300" y="128" text-anchor="middle" font-weight="600" fill="#4338CA">Neural</text>
<text class="ts" x="300" y="142" text-anchor="middle" font-weight="600" fill="#4338CA">tube</text>
</g>
<!-- step 5: dorsal-ventral patterning -->
<g id="dvT" class="reveal">
<line x1="300" y1="177" x2="300" y2="168" stroke="#EA580C" stroke-width="1.6" marker-end="url(#arrowNT)"/>
<rect x="556" y="76" width="10" height="92" rx="3" fill="url(#dvGrad)"/>
<text class="ts" x="572" y="84" font-weight="600" fill="#0284C7">Roof plate</text>
<text class="ts" x="572" y="98" fill="#0284C7">BMP, Wnt</text>
<text class="ts" x="572" y="112">→ dorsal sensory</text>
<text class="ts" x="572" y="124">interneurons</text>
<text class="ts" x="572" y="146" font-weight="600" fill="#EA580C">Floor plate</text>
<text class="ts" x="572" y="160" fill="#EA580C">Shh</text>
<text class="ts" x="572" y="174">→ ventral motor</text>
<text class="ts" x="572" y="186">neurons</text>
</g>
<g id="layerLabelsT">
<text class="ts" x="550" y="124">Ectoderm</text>
<text class="ts" x="550" y="167">Mesoderm</text>
<text class="ts" x="550" y="226">Endoderm</text>
</g>

<g id="noteNT0" class="reveal">
<text class="ts" x="30" y="262"><tspan font-weight="600">Neural induction:</tspan> BMP signalling in the ectoderm makes epidermis. The organizer and notochord</text>
<text class="ts" x="30" y="278">secrete BMP antagonists (<tspan font-weight="600">Noggin, Chordin, Follistatin</tspan>); where BMP is blocked,</text>
<text class="ts" x="30" y="294">ectoderm becomes neural plate by default.</text>
</g>
<g id="noteNT1" class="reveal">
<text class="ts" x="30" y="262">Plate cells grow tall (apicobasal elongation) and intercalate by <tspan font-weight="600">convergent extension</tspan></text>
<text class="ts" x="30" y="278">(planar cell polarity pathway), so the plate narrows and lengthens along the head–tail axis.</text>
</g>
<g id="noteNT2" class="reveal">
<text class="ts" x="30" y="262"><tspan font-weight="600">Bending:</tspan> cells at the medial hinge point (MHP, anchored over the notochord) and the dorsolateral</text>
<text class="ts" x="30" y="278">hinge points (DLHP) become wedge-shaped by <tspan font-weight="600">apical actomyosin constriction</tspan>, lifting the folds.</text>
</g>
<g id="noteNT3" class="reveal">
<text class="ts" x="30" y="262"><tspan font-weight="600">Fusion:</tspan> the folds meet at the dorsal midline. The plate has switched from <tspan fill="#1D4ED8" font-weight="600">E-cadherin</tspan></text>
<text class="ts" x="30" y="278">to <tspan fill="#4338CA" font-weight="600">N-cadherin</tspan>, so the tube can separate from the E-cadherin surface ectoderm.</text>
</g>
<g id="noteNT4" class="reveal">
<text class="ts" x="30" y="262"><tspan fill="#15803D" font-weight="600">Neural crest EMT:</tspan> border cells (intermediate BMP + Wnt) switch on Snail/Slug, FoxD3 and Sox10,</text>
<text class="ts" x="30" y="278">lose N-cadherin and tight junctions, and become migratory mesenchyme.</text>
</g>
<g id="noteNT5" class="reveal">
<text class="ts" x="30" y="262"><tspan font-weight="600">Dorsal–ventral patterning:</tspan> <tspan fill="#EA580C" font-weight="600">Shh</tspan> from the notochord induces the floor plate, which makes more</text>
<text class="ts" x="30" y="278">Shh → ventral motor neurons. <tspan fill="#1D4ED8" font-weight="600">BMP/Wnt</tspan> from the roof plate and ectoderm → dorsal sensory</text>
<text class="ts" x="30" y="294">interneurons. The opposing gradients give each position along the tube its identity.</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 5</span>
</div>

<script>
let step = 0;
const SURF_L = [
  "M60 120 C150 120 200 120 230 120", "M60 120 C150 120 200 120 250 120",
  "M60 120 C150 120 200 112 226 104", "M60 120 C170 120 240 100 276 70",
  "M60 120 C170 120 240 80 300 80",   "M60 120 C170 120 240 80 300 80"
];
const SURF_R = [
  "M370 120 C400 120 450 120 540 120", "M350 120 C400 120 450 120 540 120",
  "M374 104 C400 112 450 120 540 120", "M324 70 C360 100 430 120 540 120",
  "M300 80 C360 80 430 120 540 120",   "M300 80 C360 80 430 120 540 120"
];
const PLATE = [
  "M230 120 C260 120 270 120 300 120 C330 120 340 120 370 120",
  "M250 120 C270 120 280 120 300 120 C320 120 330 120 350 120",
  "M226 104 C240 112 268 164 300 164 C332 164 360 112 374 104",
  "M276 70 C236 84 256 168 300 168 C344 168 364 84 324 70",
  "M300 100 C262 100 262 160 300 160 C338 160 338 100 300 100",
  "M300 100 C262 100 262 160 300 160 C338 160 338 100 300 100"
];
const CREST = [[230,120,370,120,0],[250,120,350,120,0],[226,104,374,104,6],[276,70,324,70,6],[285,92,315,92,6],[240,132,360,132,6]];
const days   = ['Day 17–18', 'Day 18–19', 'Day 19–20', 'Day 20–21', 'Day 21–22', 'Day 22–28'];
const stages = ['Neural induction', 'Convergent extension', 'Hinge points bend the plate', 'Fusion and cadherin switch', 'Neural crest EMT', 'Dorsal–ventral patterning'];
const labels = [
  "Step 0 of 5 — neural induction: BMP makes epidermis; BMP antagonists from the organizer and notochord let the ectoderm above become neural plate",
  "Step 1 of 5 — convergent extension: plate cells elongate and intercalate (planar cell polarity), narrowing and lengthening the plate",
  "Step 2 of 5 — hinge points: apical actomyosin constriction makes wedge-shaped cells at the medial and dorsolateral hinge points, lifting the folds",
  "Step 3 of 5 — fusion: the folds meet; the plate's switch from E-cadherin to N-cadherin lets the tube separate from the surface ectoderm",
  "Step 4 of 5 — neural crest EMT: Snail/Slug, FoxD3 and Sox10 make border cells lose their junctions and become migratory",
  "Step 5 of 5 — dorsal–ventral patterning: Shh from notochord and floor plate (ventral, motor neurons) opposes BMP/Wnt from the roof plate (dorsal, sensory interneurons)"
];
function setD(id, d) { const el = document.getElementById(id); el.setAttribute('d', d); el.style.d = `path("${d}")`; }
function setC(id, x, y, r) { const el = document.getElementById(id);
  el.setAttribute('cx', x); el.setAttribute('cy', y); el.setAttribute('r', r);
  el.style.cx = x + 'px'; el.style.cy = y + 'px'; el.style.r = r + 'px'; }
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('dayLabelNT').textContent = days[step];
  document.getElementById('stageLabelNT').textContent = stages[step];
  setD('surfLT', SURF_L[step]); setD('surfRT', SURF_R[step]); setD('plateT', PLATE[step]);
  document.getElementById('plateT').setAttribute('stroke-width', step === 1 ? '17' : '14');   // taller cells during convergent extension
  const [xl, yl, xr, yr, r] = CREST[step];
  setC('crestLT', xl, yl, r); setC('crestRT', xr, yr, r);
  ['crestLT', 'crestRT'].forEach(id => {                        // spiky outline = mesenchymal after EMT
    const c = document.getElementById(id);
    c.setAttribute('stroke-width', step >= 4 ? '3' : '1');
    c.setAttribute('stroke-dasharray', step >= 4 ? '2 2' : 'none');
  });
  const on = (id, v) => document.getElementById(id).classList.toggle('on', v);
  on('bmpT', step === 0); on('ceT', step === 1); on('hingeT', step === 2);
  on('cadT', step === 3); on('emtT', step === 4); on('dvT', step === 5);
  on('dvFill', step === 5); on('roofP', step === 5); on('floorP', step === 5);
  document.getElementById('layerLabelsT').style.opacity = step === 5 ? '0' : '1';   // column reused for the D–V legend
  for (let k = 0; k <= 5; k++) on('noteNT' + k, k === step);
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# GASTRULATION_GENERAL  (source: gastrulation.html)
# ---------------------------------------------------------------------------
GASTRULATION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of gastrulation: a hollow blastula invaginates at the blastopore, forming an archenteron and establishing three germ layers — ectoderm, mesoderm, and endoderm.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  #innerFold { transition: d 1s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Gastrulation, general view</title>
<desc>A hollow ball of cells, the blastula, begins invaginating at the blastopore. Cells migrate inward to form the archenteron, a primitive gut, establishing the three germ layers: outer ectoderm, middle mesoderm, and inner endoderm.</desc>

<circle cx="340" cy="160" r="110" fill="none" stroke="#378ADD" stroke-width="3"/>
<text class="ts" x="340" y="40" text-anchor="middle" id="stageLabel">Blastula — hollow ball of cells</text>

<g id="blastopore" class="stg">
<circle cx="340" cy="270" r="8" fill="#D85A30"/>
<text class="ts" x="340" y="295" text-anchor="middle">Blastopore</text>
</g>

<path id="innerFold" d="M340 270 C340 270 340 270 340 270 C340 270 340 270 340 270" fill="none" stroke="#D85A30" stroke-width="3" stroke-linecap="round" class="stg"/>

<g id="archenteron" class="stg">
<path d="M324 266 C324 212 326 152 340 152 C354 152 356 212 356 266 Z" fill="#D85A30" fill-opacity="0.12" stroke="none"/>
<text class="ts" x="340" y="130" text-anchor="middle" dominant-baseline="central">Archenteron (gut)</text>
</g>

<g id="mesoderm" class="stg">
<path d="M297.5 233.6 A85 85 0 1 1 382.5 233.6" fill="none" stroke="#7F77DD" stroke-width="2" stroke-dasharray="5 4"/>
</g>

<g id="layers" class="stg">
<circle cx="460" cy="90" r="5" fill="#378ADD"/>
<text class="ts" x="475" y="90" dominant-baseline="central">Ectoderm (outer)</text>
<circle cx="460" cy="160" r="5" fill="#7F77DD"/>
<text class="ts" x="475" y="160" dominant-baseline="central">Mesoderm (middle)</text>
<circle cx="460" cy="230" r="5" fill="#D85A30"/>
<text class="ts" x="475" y="230" dominant-baseline="central">Endoderm (inner)</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 3</span>
</div>

<script>
let step = 0;
const labels = [
  "Blastula — hollow ball of cells surrounding a fluid-filled cavity",
  "Invagination begins at the blastopore",
  "Cells migrate inward, forming the archenteron (primitive gut)",
  "Three germ layers established: ectoderm, mesoderm, endoderm"
];
// the wall folds inward at the blastopore: flat -> shallow dent -> deep tube (archenteron wall = endoderm)
const folds = [
  "M340 270 C340 270 340 270 340 270 C340 270 340 270 340 270",
  "M316 268 C322 250 330 238 340 238 C350 238 358 250 364 268",
  "M318 268 C318 210 322 144 340 144 C358 144 362 210 362 268",
  "M318 268 C318 210 322 144 340 144 C358 144 362 210 362 268"
];
function render() {
  document.getElementById('stageLabel').textContent = labels[step];
  document.getElementById('stepLabel').textContent = 'Step ' + step + ' of 3';
  document.getElementById('blastopore').classList.toggle('on', step >= 1);
  document.getElementById('innerFold').classList.toggle('on', step >= 1);
  const fold = document.getElementById('innerFold');
  fold.setAttribute('d', folds[step]); fold.style.d = `path("${folds[step]}")`;   // animates where CSS d is supported
  document.getElementById('archenteron').classList.toggle('on', step >= 2);
  document.getElementById('mesoderm').classList.toggle('on', step >= 3);
  document.getElementById('layers').classList.toggle('on', step >= 3);
}
function stepFwd() { if (step < 3) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# ACTION_POTENTIAL_GENERAL  (source: action_potential.html)
# ---------------------------------------------------------------------------
ACTION_POTENTIAL_GENERAL = '''
<h2 class="sr-only">Interactive diagram comparing three types of action potential: the fast neuronal spike, the cardiac ventricular action potential with its plateau phase, and the spontaneously drifting pacemaker potential of the SA node.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #traceLine { transition: d 0.8s ease; }
  #channel0, #channel1, #channel2 { transition: transform 0.6s ease; }
  #channel0Rect, #channel1Rect, #channel2Rect { transition: fill 0.4s ease, stroke-width 0.4s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnNeuronal" onclick="setMode('neuronal')">Neuronal</button>
  <button id="btnCardiac" onclick="setMode('cardiac')">Cardiac (ventricular)</button>
  <button id="btnPacemaker" onclick="setMode('pacemaker')">Pacemaker (SA node)</button>
</div>

<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Three types of action potential</title>
<desc>Neuronal action potentials are fast, brief spikes lasting one to two milliseconds, driven by voltage-gated sodium then potassium channels. Cardiac ventricular action potentials have a long plateau phase lasting two to three hundred milliseconds, where calcium influx balances potassium efflux, preventing the heart muscle from being tetanized. Pacemaker cells in the SA node have no stable resting potential; a funny current causes spontaneous slow depolarization to threshold, where calcium channels, not sodium channels, drive the upstroke, producing the heart's own spontaneous rhythm.</desc>

<line x1="30" y1="50" x2="650" y2="50" stroke="var(--t)" stroke-width="2" stroke-linecap="round"/>
<text class="ts" x="60" y="34" id="cellLabel">Neuron axon membrane</text>

<g id="channel0" transform="translate(140,50)">
<rect id="channel0Rect" x="-7" y="-7" width="14" height="14" rx="3" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" id="channel0Name" x="0" y="24" text-anchor="middle"></text>
</g>
<g id="channel1" transform="translate(175,50)">
<rect id="channel1Rect" x="-7" y="-7" width="14" height="14" rx="3" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" id="channel1Name" x="0" y="24" text-anchor="middle"></text>
</g>
<g id="channel2" transform="translate(450,50)">
<rect id="channel2Rect" x="-7" y="-7" width="14" height="14" rx="3" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" id="channel2Name" x="0" y="24" text-anchor="middle"></text>
</g>

<path id="traceLine" d="M30 200 L650 200" stroke="#378ADD" stroke-width="2.5" fill="none"/>
<text class="ts" x="60" y="240" id="voltageLabel">Resting potential: −70 mV</text>

<g id="channelNote" class="stg">
<text class="ts" x="340" y="262" text-anchor="middle" id="channelLabel"></text>
<text class="ts" x="340" y="280" text-anchor="middle" id="channelLabel2"></text>
</g>

<g id="specialNote" class="stg">
<text class="th" x="340" y="304" text-anchor="middle" id="specialLabel"></text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
let mode = 'neuronal';

const neuronal = {
  cellLabel: 'Neuron axon membrane',
  maxStep: 4,
  labels: [
    "Step 0 of 4 — resting potential, Na/K pump maintains -70 mV",
    "Step 1 of 4 — threshold reached, Na+ channels open, rapid depolarization",
    "Step 2 of 4 — peak (~+30 mV), Na+ channels inactivate, K+ channels open",
    "Step 3 of 4 — repolarization as K+ exits, brief undershoot",
    "Step 4 of 4 — wave propagates to the next segment — total duration ~1-2 ms"
  ],
  traces: [
    "M30 200 L650 200",
    "M30 200 L120 200 L140 90 L160 200 L650 200",
    "M30 200 L120 200 L140 90 L160 200 L650 200",
    "M30 200 L120 200 L140 90 L160 215 L180 200 L650 200",
    "M340 200 L360 90 L380 215 L400 200 L650 200 M30 200 L340 200"
  ],
  voltage: ["Resting: −70 mV", "Depolarizing toward +30 mV", "Peak reached", "Repolarizing", "Wave moving on"],
  channel: "Na+ channels open first and drive the fast upstroke; K+ channels open after to repolarize the membrane",
  special: "",
  channels: [
    { x: 140, color: "#378ADD", name: "Na+" },
    { x: 175, color: "#2DAA6D", name: "K+" }
  ],
  channelOpen: [[], [0], [1], [1], []]
};

const cardiac = {
  cellLabel: 'Ventricular cardiomyocyte membrane',
  maxStep: 3,
  labels: [
    "Step 0 of 3 — resting potential, around -90 mV",
    "Step 1 of 3 — rapid depolarization — fast Na+ channels open, sharp upstroke",
    "Step 2 of 3 — PLATEAU phase (~200-300 ms) — Ca2+ influx balances K+ efflux, holding the cell depolarized",
    "Step 3 of 3 — repolarization as Ca2+ channels close and K+ dominates — refractory period just ended"
  ],
  traces: [
    "M30 200 L650 200",
    "M30 200 L100 200 L120 90 L140 120 L650 120",
    "M30 200 L100 200 L120 90 L140 120 L450 120 L650 120",
    "M30 200 L100 200 L120 90 L140 120 L450 120 L480 200 L650 200"
  ],
  voltage: ["Resting: −90 mV", "Rapid upstroke", "Plateau — sustained depolarization", "Repolarized, refractory period ends"],
  channel: "Na+ channels drive the fast upstroke; | Ca2+ channels then hold the plateau against K+ efflux; K+ alone repolarizes",
  special: "This plateau is why heart muscle can't be tetanized like skeletal muscle",
  channels: [
    { x: 110, color: "#378ADD", name: "Na+" },
    { x: 140, color: "#7F77DD", name: "Ca2+" },
    { x: 450, color: "#2DAA6D", name: "K+" }
  ],
  channelOpen: [[], [0], [1, 2], [2]]
};

const pacemaker = {
  cellLabel: 'SA node pacemaker cell membrane',
  maxStep: 3,
  labels: [
    "Step 0 of 3 — no stable resting potential, sits around -60 mV",
    "Step 1 of 3 — the 'funny current' (HCN channels) causes slow, spontaneous depolarization",
    "Step 2 of 3 — threshold reached — Ca2+ channels drive the upstroke (pacemaker cells lack fast Na+ channels)",
    "Step 3 of 3 — K+ channels repolarize, then the cycle repeats spontaneously — no external stimulus needed"
  ],
  traces: [
    "M30 190 L650 190",
    "M30 190 Q200 190 330 160",
    "M30 190 Q200 190 330 160 L350 100",
    "M30 190 Q200 190 330 160 L350 100 L385 190 Q520 190 640 160"
  ],
  voltage: ["~ −60 mV, drifting", "Slow spontaneous depolarization", "Ca2+-driven upstroke", "Repolarized — cycle repeats"],
  channel: "HCN 'funny current' channels drive the slow spontaneous drift; | Ca2+ channels trigger the upstroke; K+ repolarizes — no fast Na+ channels here",
  special: "This spontaneous, self-repeating cycle is the origin of your heartbeat's rhythm",
  channels: [
    { x: 200, color: "#EF9F27", name: "HCN" },
    { x: 340, color: "#7F77DD", name: "Ca2+" },
    { x: 380, color: "#2DAA6D", name: "K+" }
  ],
  channelOpen: [[], [0], [1], [2]]
};

function getCfg() { return mode === 'neuronal' ? neuronal : mode === 'cardiac' ? cardiac : pacemaker; }

function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnNeuronal').classList.toggle('active', m === 'neuronal');
  document.getElementById('btnCardiac').classList.toggle('active', m === 'cardiac');
  document.getElementById('btnPacemaker').classList.toggle('active', m === 'pacemaker');
  document.getElementById('cellLabel').textContent = getCfg().cellLabel;
  const note = getCfg().channel.split(' | ');
  document.getElementById('channelLabel').textContent = note[0];
  document.getElementById('channelLabel2').textContent = note[1] || '';
  const chCfg = getCfg().channels;
  for (let i = 0; i < 3; i++) {
    const g = document.getElementById('channel' + i);
    if (chCfg[i]) {
      g.style.display = '';
      g.setAttribute('transform', `translate(${chCfg[i].x},50)`);
      document.getElementById('channel' + i + 'Name').textContent = chCfg[i].name;
    } else {
      g.style.display = 'none';
    }
  }
  render();
}

function render() {
  const cfg = getCfg();
  document.getElementById('stepLabel').textContent = cfg.labels[step];
  document.getElementById('traceLine').setAttribute('d', cfg.traces[step]);
  document.getElementById('voltageLabel').textContent = cfg.voltage[step];
  document.getElementById('channelNote').classList.toggle('on', step >= 1);
  document.getElementById('specialLabel').textContent = (step === cfg.maxStep && cfg.special) ? cfg.special : '';
  document.getElementById('specialNote').classList.toggle('on', step === cfg.maxStep && !!cfg.special);
  const openSet = new Set((cfg.channelOpen && cfg.channelOpen[step]) || []);
  cfg.channels.forEach((ch, i) => {
    const rect = document.getElementById('channel' + i + 'Rect');
    const isOpen = openSet.has(i);
    rect.setAttribute('fill', isOpen ? ch.color : 'var(--surface-2)');
    rect.setAttribute('stroke-width', isOpen ? '2' : '1');
  });
}
function stepFwd() { if (step < getCfg().maxStep) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('neuronal');
</script>
'''


# ---------------------------------------------------------------------------
# MUSCLE_CONTRACTION_GENERAL  (source: muscle_contraction.html)
# ---------------------------------------------------------------------------
MUSCLE_CONTRACTION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of the sliding filament model of muscle contraction: calcium release, cross-bridge formation, the power stroke, and sarcomere shortening.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #actinLeft, #actinRight { transition: transform 1s ease; }
  .contracted #actinLeft { transform: translateX(40px); }
  .contracted #actinRight { transform: translateX(-40px); }
  .tropo { transition: transform 0.6s ease, opacity 0.6s ease; }
  .exposed .tropo { transform: translateY(6px); opacity: 0.3; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 260" role="img">
<title>Sliding filament model of muscle contraction</title>
<desc>Calcium released from the sarcoplasmic reticulum binds troponin, moving tropomyosin to expose myosin-binding sites on actin. Myosin heads form cross-bridges, pull the actin filaments inward during the power stroke, and the sarcomere shortens as the Z-lines are drawn closer together.</desc>

<line x1="60" y1="130" x2="620" y2="130" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="2 2"/>

<rect x="250" y="115" width="180" height="30" fill="#7F77DD"/>
<text class="ts" x="340" y="105" text-anchor="middle">Myosin (thick filament)</text>

<g id="actinLeft">
<line x1="80" y1="60" x2="80" y2="200" stroke="var(--t)" stroke-width="3"/>
<text class="ts" x="80" y="50" text-anchor="middle">Z-line</text>
<rect x="80" y="120" width="200" height="8" fill="#378ADD"/>
<rect id="tropomyosin" class="tropo" x="80" y="120" width="200" height="8" fill="#EF9F27" opacity="0.7"/>
</g>
<g id="actinRight">
<line x1="600" y1="60" x2="600" y2="200" stroke="var(--t)" stroke-width="3"/>
<text class="ts" x="600" y="50" text-anchor="middle">Z-line</text>
<rect x="400" y="120" width="200" height="8" fill="#D85A30"/>
<rect class="tropo" x="400" y="120" width="200" height="8" fill="#EF9F27" opacity="0.7"/>
</g>
<text class="ts" x="340" y="215" text-anchor="middle">Actin (thin filaments)</text>

<g id="calcium" class="stg">
<circle class="pulse" cx="200" cy="90" r="6" fill="#639922"/>
<circle class="pulse" cx="440" cy="90" r="6" fill="#639922"/>
<text class="ts" x="340" y="75" text-anchor="middle">Ca2+ released, binds troponin</text>
</g>

<g id="crossbridge" class="stg">
<path d="M268 145 L258 128 M298 145 L288 128 M382 145 L392 128 M412 145 L422 128" stroke="#3C3489" stroke-width="3" stroke-linecap="round" fill="none"/>
<text class="ts" x="340" y="160" text-anchor="middle">Cross-bridges (myosin heads)</text>
</g>

<g id="atpRelease" class="stg">
<circle cx="340" cy="182" r="9" class="c-amber pulse"/>
<text class="ts" x="340" y="182" text-anchor="middle" dominant-baseline="central" font-size="8">ATP</text>
<text class="ts" x="340" y="245" text-anchor="middle">ATP binds — cross-bridge releases</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — relaxed: tropomyosin blocks the myosin-binding sites on actin",
  "Step 1 of 4 — Ca2+ released, binds troponin, tropomyosin shifts to expose binding sites",
  "Step 2 of 4 — myosin heads form cross-bridges and pull actin inward (power stroke)",
  "Step 3 of 4 — sarcomere shortens, Z-lines drawn closer together",
  "Step 4 of 4 — ATP binds the myosin head, the cross-bridge releases — without ATP the head stays locked (this is why rigor mortis happens)"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('calcium').classList.toggle('on', step >= 1);
  document.querySelector('svg').classList.toggle('exposed', step >= 1);
  document.getElementById('crossbridge').classList.toggle('on', step >= 2 && step < 4);
  document.querySelector('svg').classList.toggle('contracted', step >= 3);
  document.getElementById('atpRelease').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# CARDIAC_CONDUCTION_GENERAL  (source: cardiac_conduction.html)
# ---------------------------------------------------------------------------
CARDIAC_CONDUCTION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of the cardiac conduction system: the SA node fires, atria depolarize, the AV node delays the signal, then it races through the Bundle of His and Purkinje fibers to trigger ventricular contraction.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text, .stg:not(.on) .lead { visibility: hidden; }
  .lead { stroke: var(--t); stroke-width: 0.75; }
  .pulse { animation: pulse 1.1s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #atriaFill, #ventFill { transition: fill 0.5s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Cardiac conduction system</title>
<desc>The SA node fires spontaneously, depolarizing the atria to trigger atrial contraction. The signal reaches the AV node, delays briefly, then travels through the Bundle of His and Purkinje fibers, depolarizing the ventricles and triggering ventricular contraction.</desc>

<path id="atriaFill" d="M200 60 Q140 60 140 120 Q140 170 200 170 Q260 170 260 120 Q260 60 200 60 Z" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="200" y="115" text-anchor="middle">Atria</text>

<path id="ventFill" d="M200 180 L120 300 L280 300 Z" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="200" y="296" text-anchor="middle">Ventricles</text>

<g id="saNode">
<circle cx="230" cy="80" r="10" class="c-amber"/>
<line class="lead" x1="241" y1="80" x2="300" y2="80"/>
<text class="ts" x="306" y="84">SA node (pacemaker)</text>
</g>

<g id="avNode" class="stg">
<circle cx="200" cy="175" r="9" class="c-purple"/>
<line class="lead" x1="210" y1="175" x2="300" y2="175"/>
<text class="ts" x="306" y="179">AV node (delay)</text>
</g>

<g id="hisPurkinje" class="stg">
<line x1="200" y1="185" x2="200" y2="230" stroke="#0F6E56" stroke-width="2"/>
<line x1="200" y1="230" x2="150" y2="290" stroke="#0F6E56" stroke-width="1.5"/>
<line x1="200" y1="230" x2="250" y2="290" stroke="#0F6E56" stroke-width="1.5"/>
<line class="lead" x1="202" y1="210" x2="300" y2="210"/>
<text class="ts" x="306" y="214">Bundle of His</text>
<line class="lead" x1="246" y1="285" x2="300" y2="285"/>
<text class="ts" x="306" y="289">Purkinje fibers</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — SA node (pacemaker) fires spontaneously",
  "Step 1 of 4 — signal spreads across the atria, triggering atrial contraction",
  "Step 2 of 4 — signal reaches the AV node, briefly delayed",
  "Step 3 of 4 — signal races through the Bundle of His and Purkinje fibers",
  "Step 4 of 4 — ventricles depolarize and contract, ejecting blood"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('saNode').classList.toggle('pulse', step === 0);
  document.getElementById('atriaFill').setAttribute('fill', step >= 1 && step <= 1 ? '#EF9F27' : 'var(--surface-2)');
  document.getElementById('avNode').classList.toggle('on', step >= 2);
  document.getElementById('avNode').classList.toggle('pulse', step === 2);
  document.getElementById('hisPurkinje').classList.toggle('on', step >= 3);
  document.getElementById('ventFill').setAttribute('fill', step >= 4 ? '#E24B4A' : 'var(--surface-2)');
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# GAS_EXCHANGE_GENERAL  (source: gas_exchange.html)
# ---------------------------------------------------------------------------
GAS_EXCHANGE_GENERAL = '''
<h2 class="sr-only">Interactive diagram of gas exchange in the alveoli: oxygen diffuses into the blood and binds hemoglobin while carbon dioxide diffuses out to be exhaled.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .gasdot { transition: transform 1.3s ease-in-out, opacity 1.3s ease-in-out; }
  .gasarrow { transition: opacity .5s ease; opacity: 0; }
  .gasarrow.on { opacity: 1; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Gas exchange in the alveoli</title>
<desc>Oxygen-rich air in the alveolus diffuses down its concentration gradient into the adjacent capillary, where it binds hemoglobin in red blood cells, while carbon dioxide diffuses the opposite direction from blood into the alveolus to be exhaled.</desc>
<defs>
<marker id="gxArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<circle cx="220" cy="150" r="110" fill="var(--surface-1)" stroke="var(--t)" stroke-width="1.5"/>
<text class="th" x="220" y="90" text-anchor="middle">Alveolus</text>
<text class="ts" x="220" y="108" text-anchor="middle">High O2, low CO2</text>

<rect x="380" y="110" width="260" height="80" rx="30" fill="none" stroke="#B91C1C" stroke-width="3"/>
<text class="ts" x="510" y="100" text-anchor="middle">Capillary</text>
<text class="ts" x="390" y="215" id="outLabel">→ Deoxygenated blood in</text>

<path id="o2Arrow" class="gasarrow" d="M300 128 L400 128" stroke="#378ADD" stroke-width="2" fill="none" marker-end="url(#gxArrow)"/>
<text class="ts" x="350" y="118" text-anchor="middle">O2</text>

<path id="co2Arrow" class="gasarrow" d="M400 182 L300 182" stroke="#639922" stroke-width="2" fill="none" marker-end="url(#gxArrow)"/>
<text class="ts" x="350" y="200" text-anchor="middle">CO2</text>

<g id="o2" class="stg">
<circle id="o2a" class="gasdot" cx="285" cy="135" r="7" fill="#378ADD"/>
<circle id="o2b" class="gasdot" cx="300" cy="165" r="7" fill="#378ADD"/>
</g>

<g id="co2" class="stg">
<circle id="co2a" class="gasdot" cx="405" cy="140" r="7" fill="#639922"/>
<circle id="co2b" class="gasdot" cx="420" cy="165" r="7" fill="#639922"/>
</g>

<g id="hemoglobin" class="stg">
<circle cx="480" cy="150" r="16" fill="#B91C1C"/>
<text class="ts" x="480" y="150" text-anchor="middle" dominant-baseline="central" style="fill:#fff">Hb</text>
<text class="ts" x="480" y="175" text-anchor="middle">O2 binds hemoglobin</text>
</g>

<g id="oxygenated" class="stg">
<text class="th" x="640" y="238" text-anchor="end">Oxygenated blood out →</text>
</g>

<g id="exhaled" class="stg">
<text class="ts" x="220" y="60" text-anchor="middle">CO2 exhaled ↑</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 3</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 3 — deoxygenated blood arrives, fresh air fills the alveolus",
  "Step 1 of 3 — O2 diffuses down its gradient from alveolus into blood",
  "Step 2 of 3 — CO2 diffuses the opposite direction, from blood into alveolus",
  "Step 3 of 3 — O2 binds hemoglobin, oxygenated blood leaves via the pulmonary vein"
];
function setDot(id, dx, dy, visible) {
  const el = document.getElementById(id);
  el.style.transform = 'translate(' + dx + 'px,' + dy + 'px)';
  el.style.opacity = visible ? '1' : '0';
}
function render() {
  document.getElementById('stepLabel').textContent = labels[step];

  // O2: starts in the alveolus, crosses into the capillary at step 1,
  // then slides into hemoglobin and disappears (bound) at step 3.
  document.getElementById('o2').classList.toggle('on', step >= 1);
  document.getElementById('o2Arrow').classList.toggle('on', step === 1);
  if (step < 1) { setDot('o2a', 0, 0, false); setDot('o2b', 0, 0, false); }
  else if (step < 3) { setDot('o2a', 130, 0, true); setDot('o2b', 130, 0, true); }
  else { setDot('o2a', 187, 9, false); setDot('o2b', 188, -9, false); }

  // CO2: starts in the capillary, crosses into the alveolus at step 2,
  // then drifts further up and fades — exhaled — at step 3.
  document.getElementById('co2').classList.toggle('on', step >= 2);
  document.getElementById('co2Arrow').classList.toggle('on', step === 2);
  if (step < 2) { setDot('co2a', 0, 0, false); setDot('co2b', 0, 0, false); }
  else if (step < 3) { setDot('co2a', -150, 5, true); setDot('co2b', -145, 5, true); }
  else { setDot('co2a', -150, -50, false); setDot('co2b', -145, -55, false); }

  document.getElementById('hemoglobin').classList.toggle('on', step >= 3);
  document.getElementById('oxygenated').classList.toggle('on', step >= 3);
  document.getElementById('exhaled').classList.toggle('on', step >= 3);
}
function stepFwd() { if (step < 3) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# GAS_EXCHANGE_TECHNICAL
# ---------------------------------------------------------------------------
GAS_EXCHANGE_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of gas exchange and gas transport: partial-pressure gradients, diffusion across the respiratory membrane, the oxygen-hemoglobin dissociation curve with the Bohr shift, and carbon dioxide carriage as bicarbonate via carbonic anhydrase and the chloride shift, shown for loading in the lungs and unloading in the tissues.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .hide { display: none; }
  .gdot { transition: cx 1.1s ease, cy 1.1s ease, opacity .6s ease; }
  #hbPt { transition: cx 1s ease, cy 1s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnLungs" onclick="setMode('lungs')">Lungs (loading)</button>
  <button id="btnTissues" onclick="setMode('tissues')">Tissues (unloading)</button>
</div>

<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Gas exchange and transport, technical view</title>
<desc>In the lungs, venous blood (PO2 about 40, PCO2 about 46 mmHg) meets alveolar air (PO2 about 100, PCO2 about 40); O2 diffuses in and saturates hemoglobin to about 98 percent within about a third of the capillary transit time, while CO2, far more soluble, diffuses out after being regenerated from bicarbonate by carbonic anhydrase. In the tissues, CO2, H+ and heat shift the dissociation curve right (Bohr effect) so O2 unloads, and CO2 is converted to bicarbonate, which leaves the red cell in exchange for chloride.</desc>
<defs><marker id="gtArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>

<!-- exchange compartment: alveolus (lungs) or tissue (tissues) -->
<rect x="30" y="34" width="360" height="70" rx="12" fill="var(--surface-1)" stroke="var(--t)" stroke-width="1"/>
<text class="th" x="44" y="58" id="compName"></text>
<text class="ts" x="44" y="80" id="compP"></text>
<line x1="30" y1="114" x2="390" y2="114" stroke="var(--t)" stroke-width="1" stroke-dasharray="4 3"/>
<text class="ts" x="388" y="128" text-anchor="end" id="memLabel" style="font-size:10px"></text>

<!-- capillary with a red blood cell -->
<rect x="30" y="134" width="360" height="92" rx="24" fill="#FCEBEB" stroke="#B91C1C" stroke-width="2"/>
<text class="ts" x="44" y="152" style="font-size:10px">blood flow →</text>
<ellipse cx="210" cy="182" rx="48" ry="26" class="c-coral"/>
<text class="ts" x="210" y="198" text-anchor="middle">RBC · Hb</text>
<text class="ts" x="30" y="244" id="inLabel"></text>
<text class="ts" x="390" y="244" text-anchor="end" id="outLabel"></text>

<!-- chloride shift across the RBC membrane -->
<g id="shift" class="stg">
<path id="hco3Arrow" d="M258 176 L298 176" stroke="#0F6E56" stroke-width="2" fill="none" marker-end="url(#gtArrow)"/>
<path id="clArrow" d="M298 192 L258 192" stroke="#64748B" stroke-width="2" fill="none" marker-end="url(#gtArrow)"/>
<text class="ts" x="304" y="180" id="hco3Text"></text>
<text class="ts" x="304" y="196" id="clText"></text>
</g>

<!-- gas molecules -->
<circle class="gdot o2" r="6" fill="#378ADD"/>
<circle class="gdot o2" r="6" fill="#378ADD"/>
<circle class="gdot o2" r="6" fill="#378ADD"/>
<circle class="gdot co2" r="6" fill="#639922"/>
<circle class="gdot co2" r="6" fill="#639922"/>
<circle class="gdot co2" r="6" fill="#639922"/>
<text class="ts" x="320" y="58"><tspan fill="#378ADD">●</tspan> O2   <tspan fill="#639922">●</tspan> CO2</text>

<!-- carbonic anhydrase reaction -->
<g id="reaction" class="stg"><text class="ts" x="30" y="272" id="rxText"></text></g>

<!-- equilibration within the transit time (lungs) -->
<g id="transit" class="stg">
<line x1="30" y1="296" x2="390" y2="296" stroke="#C9C7C0" stroke-width="6" stroke-linecap="round"/>
<line x1="30" y1="296" x2="150" y2="296" stroke="#378ADD" stroke-width="6" stroke-linecap="round"/>
<text class="ts" x="30" y="316">0 s</text>
<text class="ts" x="150" y="316" text-anchor="middle">~0.25 s: equilibrated</text>
<text class="ts" x="390" y="316" text-anchor="end">0.75 s: leaves capillary</text>
</g>

<!-- O2-Hb dissociation curve -->
<text class="th" x="540" y="34" text-anchor="middle">O2–Hb dissociation curve</text>
<line x1="430" y1="220" x2="650" y2="220" stroke="var(--t)" stroke-width="1"/>
<line x1="430" y1="60" x2="430" y2="220" stroke="var(--t)" stroke-width="1"/>
<line x1="430" y1="60" x2="650" y2="60" stroke="var(--t)" stroke-width="0.5" stroke-dasharray="2 3"/>
<text class="ts" x="430" y="236" text-anchor="middle">0</text>
<text class="ts" x="518" y="236" text-anchor="middle">40</text>
<text class="ts" x="650" y="236" text-anchor="middle">100</text>
<text class="ts" x="540" y="252" text-anchor="middle">PO2 (mmHg)</text>
<text class="ts" x="424" y="224" text-anchor="end">0</text>
<text class="ts" x="424" y="144" text-anchor="end">50</text>
<text class="ts" x="424" y="64" text-anchor="end">100</text>
<text class="ts" x="424" y="48" text-anchor="end" style="font-size:10px">SO2 %</text>
<path id="curveN" fill="none" stroke="#888780" stroke-width="2"/>
<g id="bohr" class="stg"><path id="curveR" fill="none" stroke="#B91C1C" stroke-width="2" stroke-dasharray="5 3"/>
<text class="ts" x="560" y="176" style="fill:#B91C1C">right shift (Bohr)</text></g>
<circle id="hbPt" r="6" fill="#B91C1C" stroke="#fff" stroke-width="1.5"/>
<text class="th" x="650" y="276" text-anchor="end" id="satLabel"></text>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
let mode = 'lungs';
const N = 2.7;
function sat(p, p50) { return Math.pow(p, N) / (Math.pow(p, N) + Math.pow(p50, N)); }
function X(p) { return 430 + p * 2.2; }
function Y(s) { return 220 - s * 160; }
function curvePath(p50) {
  let d = '';
  for (let p = 0; p <= 100; p += 2) d += (p ? ' L' : 'M') + X(p).toFixed(1) + ' ' + Y(sat(p, p50)).toFixed(1);
  return d;
}
document.getElementById('curveN').setAttribute('d', curvePath(27));
document.getElementById('curveR').setAttribute('d', curvePath(33));

// molecule positions: top = in the alveolus / tissue, rbc = bound in the red cell, plasma = dissolved in blood
const POS = {
  o2Top: [[110, 96], [150, 92], [190, 96]],
  o2Rbc: [[190, 174], [210, 170], [230, 174]],
  co2Top: [[270, 96], [310, 92], [350, 96]],
  co2Blood: [[90, 190], [120, 204], [320, 210]]
};
const M = {
  lungs: {
    name: 'Alveolus', p: 'PO2 ~100 · PCO2 ~40 mmHg', mem: 'respiratory membrane ~0.5 µm',
    inL: 'in: PO2 40 · PCO2 46', outL: 'out: PO2 100 · PCO2 40',
    labels: [
      "Step 0 of 4 — venous blood enters the pulmonary capillary (PO2 ~40, PCO2 ~46 mmHg) and meets alveolar air (PO2 ~100, PCO2 ~40)",
      "Step 1 of 4 — O2 diffuses down a ~60 mmHg gradient across the ~0.5 µm membrane (Fick: rate ∝ area × ΔP ÷ thickness) and binds Hb",
      "Step 2 of 4 — blood equilibrates with alveolar air within ~0.25 s of a ~0.75 s transit, leaving a reserve for exercise; Hb saturation reaches ~98%",
      "Step 3 of 4 — CO2 diffuses out on a gradient of only ~6 mmHg, but it is ~20× more soluble than O2, so it keeps pace",
      "Step 4 of 4 — in the red cell HCO3− re-enters (Cl− leaves) and carbonic anhydrase regenerates CO2 to be exhaled; O2 binding to Hb releases CO2 and H+ (Haldane effect)"
    ],
    po2: [40, 70, 100, 100, 100], shifted: [false, false, false, false, false],
    o2AtTop: [true, false, false, false, false],
    co2AtTop: [false, false, false, true, true],
    rx: 'RBC: HCO3− + H+ → H2CO3 → CO2 + H2O  (carbonic anhydrase)', rxOn: s => s === 4,
    shiftOn: s => s === 4, hco3: 'HCO3− in', cl: 'Cl− out', transitOn: s => s === 2
  },
  tissues: {
    name: 'Active tissue', p: 'PO2 ~40 or lower · PCO2 ~46+ mmHg', mem: 'capillary wall',
    inL: 'in: PO2 100 · PCO2 40', outL: 'out: PO2 40 · PCO2 46',
    labels: [
      "Step 0 of 4 — arterial blood reaches the systemic capillary (PO2 ~100, PCO2 ~40 mmHg); working tissue has PO2 ~40 or lower and PCO2 ~46 or higher",
      "Step 1 of 4 — CO2, H+ and heat from metabolism shift the O2–Hb curve to the right (Bohr effect): hemoglobin's O2 affinity falls",
      "Step 2 of 4 — O2 unloads down its gradient into the tissue; on the steep part of the curve a small fall in PO2 releases a lot of O2",
      "Step 3 of 4 — CO2 diffuses into the blood; in the red cell carbonic anhydrase converts CO2 + H2O → H2CO3 → H+ + HCO3−",
      "Step 4 of 4 — HCO3− leaves the red cell in exchange for Cl− (chloride shift) and travels in plasma (~70% of CO2); deoxy-Hb buffers H+ and carries more CO2 (Haldane effect)"
    ],
    po2: [100, 100, 40, 40, 40], shifted: [false, true, true, true, true],
    o2AtTop: [false, false, true, true, true],
    co2AtTop: [true, true, true, false, false],
    rx: 'RBC: CO2 + H2O → H2CO3 → H+ + HCO3−  (carbonic anhydrase)', rxOn: s => s >= 3,
    shiftOn: s => s === 4, hco3: 'HCO3− out', cl: 'Cl− in', transitOn: s => false
  }
};
function cfg() { return M[mode]; }
function place(el, xy) {
  el.setAttribute('cx', xy[0]); el.setAttribute('cy', xy[1]);
  el.style.cx = xy[0] + 'px'; el.style.cy = xy[1] + 'px';
}
function setMode(m) {
  mode = m; step = 0;
  const c = cfg();
  document.getElementById('btnLungs').classList.toggle('active', m === 'lungs');
  document.getElementById('btnTissues').classList.toggle('active', m === 'tissues');
  document.getElementById('compName').textContent = c.name;
  document.getElementById('compP').textContent = c.p;
  document.getElementById('memLabel').textContent = c.mem;
  document.getElementById('inLabel').textContent = c.inL;
  document.getElementById('outLabel').textContent = c.outL;
  document.getElementById('rxText').textContent = c.rx;
  document.getElementById('transit').classList.toggle('hide', m !== 'lungs');   // equilibration timing is a lung concept
  document.getElementById('bohr').classList.toggle('hide', m !== 'tissues');    // the right shift is shown where it happens
  document.getElementById('hco3Text').textContent = c.hco3;
  document.getElementById('clText').textContent = c.cl;
  // arrows point the way each ion moves in this mode
  document.getElementById('hco3Arrow').setAttribute('d', m === 'tissues' ? 'M258 176 L298 176' : 'M298 176 L258 176');
  document.getElementById('clArrow').setAttribute('d', m === 'tissues' ? 'M298 192 L258 192' : 'M258 192 L298 192');
  render();
}
function render() {
  const c = cfg();
  document.getElementById('stepLabel').textContent = c.labels[step];
  document.querySelectorAll('.o2').forEach((d, i) => place(d, c.o2AtTop[step] ? POS.o2Top[i] : POS.o2Rbc[i]));
  document.querySelectorAll('.co2').forEach((d, i) => place(d, c.co2AtTop[step] ? POS.co2Top[i] : POS.co2Blood[i]));
  document.getElementById('reaction').classList.toggle('on', c.rxOn(step));
  document.getElementById('shift').classList.toggle('on', c.shiftOn(step));
  document.getElementById('transit').classList.toggle('on', c.transitOn(step));
  const sh = c.shifted[step];
  document.getElementById('bohr').classList.toggle('on', sh);
  const p = c.po2[step], s = sat(p, sh ? 33 : 27);
  place(document.getElementById('hbPt'), [X(p), Y(s)]);
  document.getElementById('satLabel').textContent = 'PO2 ' + p + ' mmHg → SO2 ≈ ' + Math.round(s * 100) + '%';
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('lungs');
</script>
'''


# ---------------------------------------------------------------------------
# SYNAPTIC_TRANSMISSION_GENERAL  (source: synaptic.html)
# ---------------------------------------------------------------------------
SYNAPTIC_TRANSMISSION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of synaptic transmission: an action potential triggers calcium influx, vesicle fusion, neurotransmitter release, and receptor binding on the postsynaptic neuron.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }   /* faint previews keep their shape, not their overlapping captions */
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #neurotransmitter circle { transition: transform 1s ease; }
  .crossing #neurotransmitter circle { transform: translateX(150px); }
  .bound #neurotransmitter circle { transform: translateX(300px); }
  #vesicle { transition: transform 0.8s ease, opacity 0.5s ease; }
  .released #vesicle { transform: translateX(22px); opacity: 0; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Synaptic transmission, general view</title>
<desc>An action potential arrives at the axon terminal, opening voltage-gated calcium channels. Calcium influx triggers a synaptic vesicle to fuse with the presynaptic membrane, releasing neurotransmitter into the synaptic cleft, which diffuses across and binds receptors on the postsynaptic membrane.</desc>

<rect x="40" y="80" width="140" height="140" rx="16" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="110" y="70" text-anchor="middle">Axon terminal</text>

<rect x="500" y="80" width="140" height="140" rx="16" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="570" y="70" text-anchor="middle">Postsynaptic neuron</text>
<text class="ts" x="340" y="255" text-anchor="middle">Synaptic cleft</text>

<g id="apArrow" class="stg">
<text class="ts" x="60" y="100" text-anchor="middle">AP →</text>
</g>

<g id="caChannel" class="stg">
<rect x="170" y="140" width="14" height="30" fill="#639922"/>
<text class="ts" x="177" y="185" text-anchor="middle">Ca2+ in</text>
</g>

<g id="vesicle">
<circle cx="140" cy="150" r="22" fill="none" stroke="#7F77DD" stroke-width="2"/>
<circle cx="132" cy="145" r="3" fill="#7F77DD"/>
<circle cx="148" cy="150" r="3" fill="#7F77DD"/>
<circle cx="138" cy="158" r="3" fill="#7F77DD"/>
</g>

<g id="neurotransmitter" class="stg">
<circle cx="190" cy="150" r="5" fill="#7F77DD"/>
<circle cx="190" cy="165" r="5" fill="#7F77DD"/>
<circle cx="190" cy="135" r="5" fill="#7F77DD"/>
</g>

<g id="receptor" class="stg">
<rect x="495" y="135" width="16" height="30" rx="4" fill="var(--surface-1)" stroke="#EF9F27" stroke-width="2"/>
<text class="ts" x="503" y="120" text-anchor="middle">Receptor</text>
</g>

<g id="response" class="stg">
<circle cx="503" cy="150" r="20" fill="none" stroke="#639922" stroke-width="2" stroke-dasharray="3 3"/>
<text class="ts" x="570" y="240" text-anchor="middle">Postsynaptic response</text>
<text class="ts" x="570" y="256" text-anchor="middle">(ion channel opens)</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — action potential arrives at the axon terminal",
  "Step 1 of 4 — voltage-gated Ca2+ channels open, calcium flows in",
  "Step 2 of 4 — vesicle fuses with the membrane, neurotransmitter released",
  "Step 3 of 4 — neurotransmitter diffuses across the synaptic cleft",
  "Step 4 of 4 — neurotransmitter binds receptors, postsynaptic response triggered"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('apArrow').classList.toggle('on', step === 0);
  document.getElementById('caChannel').classList.toggle('on', step >= 1);
  document.querySelector('svg').classList.toggle('released', step >= 2);
  document.getElementById('neurotransmitter').classList.toggle('on', step >= 2);
  document.querySelector('svg').classList.toggle('crossing', step === 3);   // halfway across the cleft
  document.querySelector('svg').classList.toggle('bound', step >= 4);      // arrived at the receptor
  document.getElementById('receptor').classList.toggle('on', step >= 3);
  document.getElementById('response').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# ELECTRON_TRANSPORT_CHAIN_GENERAL  (source: etc.html)
# ---------------------------------------------------------------------------
ELECTRON_TRANSPORT_CHAIN_GENERAL = '''
<h2 class="sr-only">Interactive diagram of the electron transport chain and ATP synthase: electrons pass through membrane complexes pumping protons, building a gradient that powers ATP synthase.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.1s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #rotor { transform-box: fill-box; transform-origin: center; }
  .spin { animation: spin 1.2s linear infinite; }
  #eDot { transition: cx 1.4s ease-in-out, cy 1s ease, opacity .5s ease; }
  .flowdown { animation: flowdown 1.4s linear infinite; }
  @keyframes flowdown { 0%{transform:translateY(0);opacity:0} 15%{opacity:1} 85%{opacity:1} 100%{transform:translateY(90px);opacity:0} }
  @keyframes spin { from{transform:rotate(0)} to{transform:rotate(360deg)} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 280" role="img">
<title>Electron transport chain and ATP synthase</title>
<desc>Electrons from NADH pass through membrane protein complexes, which pump protons into the intermembrane space, building an electrochemical gradient. Oxygen accepts electrons at the final complex, forming water. Protons flow back through ATP synthase, spinning it to catalyze ATP formation from ADP and phosphate.</desc>

<defs><marker id="etcArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text class="ts" x="40" y="40" id="imsLabel">Intermembrane space</text>
<rect x="30" y="120" width="620" height="50" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="450" y="149" text-anchor="middle" style="font-size:10px">Inner mitochondrial membrane</text>
<text class="ts" x="40" y="268" id="matrixLabel">Matrix</text>

<!-- electron route through the chain -->
<g id="route" class="stg"><path d="M150 145 L218 145" stroke="#EF9F27" stroke-width="2" stroke-dasharray="4 3" fill="none" marker-end="url(#etcArrow)"/>
<path d="M250 145 L318 145" stroke="#EF9F27" stroke-width="2" stroke-dasharray="4 3" fill="none" marker-end="url(#etcArrow)"/></g>

<rect x="120" y="110" width="30" height="70" rx="8" class="c-purple"/>
<text class="ts" x="135" y="196" text-anchor="middle">I</text>
<rect x="220" y="110" width="30" height="70" rx="8" class="c-teal"/>
<text class="ts" x="235" y="196" text-anchor="middle">III</text>
<rect x="320" y="110" width="30" height="70" rx="8" class="c-coral"/>
<text class="ts" x="335" y="196" text-anchor="middle">IV</text>

<g id="electron" class="stg">
<text class="ts" x="90" y="222" text-anchor="middle">NADH → NAD+</text>
<path d="M98 206 L124 178" stroke="#EF9F27" stroke-width="1.5" fill="none" marker-end="url(#etcArrow)"/>
<text class="ts" x="90" y="238" text-anchor="middle">e- from NADH</text>
</g>
<circle id="eDot" cx="135" cy="145" r="6" fill="#EF9F27"/>

<!-- protons pumped up by I, III and IV, accumulating in the intermembrane space -->
<g id="protons" class="stg">
<path d="M135 106 L135 76" stroke="#B91C1C" stroke-width="2" fill="none" marker-end="url(#etcArrow)"/>
<path d="M235 106 L235 76" stroke="#B91C1C" stroke-width="2" fill="none" marker-end="url(#etcArrow)"/>
<path d="M335 106 L335 76" stroke="#B91C1C" stroke-width="2" fill="none" marker-end="url(#etcArrow)"/>
<text class="ts" x="235" y="62" text-anchor="middle">H+ pumped into intermembrane space</text>
</g>
<g id="gradient" class="stg">
<circle cx="160" cy="88" r="4" fill="#B91C1C"/><circle cx="200" cy="96" r="4" fill="#B91C1C"/>
<circle cx="270" cy="86" r="4" fill="#B91C1C"/><circle cx="300" cy="100" r="4" fill="#B91C1C"/>
<circle cx="380" cy="90" r="4" fill="#B91C1C"/><circle cx="420" cy="102" r="4" fill="#B91C1C"/>
<circle cx="460" cy="86" r="4" fill="#B91C1C"/><circle cx="500" cy="98" r="4" fill="#B91C1C"/>
<text class="ts" x="400" y="70" text-anchor="middle">high H+ (gradient)</text>
</g>

<g id="oxygen" class="stg">
<circle cx="380" cy="214" r="10" fill="#378ADD"/>
<path d="M342 182 L370 206" stroke="#EF9F27" stroke-width="1.5" fill="none" marker-end="url(#etcArrow)"/>
<text class="ts" x="380" y="242" text-anchor="middle">O2 + e- → H2O</text>
</g>

<!-- ATP synthase: Fo channel in the membrane, F1 head (rotor) in the matrix -->
<g id="atpSynthase">
<rect x="545" y="112" width="30" height="66" rx="8" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<line x1="560" y1="178" x2="560" y2="192" stroke="var(--t)" stroke-width="3"/>
<g id="rotor">
<circle cx="560" cy="214" r="22" class="c-amber"/>
<path d="M560 196 L560 232 M544 205 L576 223 M544 223 L576 205" stroke="#B45309" stroke-width="2"/>
</g>
<text class="ts" x="582" y="108">ATP synthase</text>
</g>
<g id="flow" class="stg">
<path d="M560 64 L560 104" stroke="#B91C1C" stroke-width="2" fill="none" marker-end="url(#etcArrow)"/>
<circle class="flowdown" cx="560" cy="96" r="4" fill="#B91C1C"/>
<circle class="flowdown" cx="560" cy="96" r="4" fill="#B91C1C" style="animation-delay:.47s"/>
<circle class="flowdown" cx="560" cy="96" r="4" fill="#B91C1C" style="animation-delay:.94s"/>
<text class="ts" x="552" y="60" text-anchor="end">H+ flows back</text>
</g>

<g id="atpOut" class="stg">
<text class="th" x="560" y="262" text-anchor="middle">ADP + Pi → ATP</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — electrons enter Complex I from NADH",
  "Step 1 of 4 — electrons pass through I → III → IV, pumping H+ across the membrane",
  "Step 2 of 4 — oxygen accepts electrons at Complex IV, forming water",
  "Step 3 of 4 — protons flow back down their gradient through ATP synthase",
  "Step 4 of 4 — ATP synthase spins, catalyzing ADP + Pi → ATP"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('electron').classList.toggle('on', step === 0);
  document.getElementById('route').classList.toggle('on', step >= 1);
  // the electron travels I -> III -> IV, then is handed to O2
  const e = document.getElementById('eDot');
  const ex = step === 0 ? 135 : step === 1 ? 335 : 380, ey = step >= 2 ? 214 : 145;
  e.setAttribute('cx', ex); e.setAttribute('cy', ey); e.style.cx = ex + 'px'; e.style.cy = ey + 'px';
  e.style.opacity = step >= 2 ? 0 : 1;
  document.getElementById('protons').classList.toggle('on', step >= 1 && step <= 2);
  document.getElementById('gradient').classList.toggle('on', step >= 1);
  document.getElementById('flow').classList.toggle('on', step >= 3);
  document.getElementById('oxygen').classList.toggle('on', step >= 2);
  document.getElementById('rotor').classList.toggle('spin', step >= 3);
  document.getElementById('atpOut').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# ELECTRON_TRANSPORT_CHAIN_TECHNICAL
# ---------------------------------------------------------------------------
ELECTRON_TRANSPORT_CHAIN_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of oxidative phosphorylation: electrons from NADH (Complex I) or FADH2 (Complex II) pass via ubiquinone, Complex III and cytochrome c to Complex IV, pumping 10 or 6 protons; the proton-motive force turns the Fo c-ring and the F1 binding-change mechanism makes ATP, giving P/O ratios of about 2.5 and 1.5.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .hide { display: none; }
  .dim { opacity: .3; transition: opacity .5s ease; }
  .turning .csub { animation: csub 1.2s linear infinite; }
  @keyframes csub { 0%,100%{opacity:.35} 12%{opacity:1} 25%{opacity:.35} }
  #gamma { transform-origin: 520px 248px; }
  .turning #gamma { animation: gspin 1.2s linear infinite; }
  @keyframes gspin { from{transform:rotate(0)} to{transform:rotate(360deg)} }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnNadh" onclick="setMode('nadh')">NADH (Complex I)</button>
  <button id="btnFad" onclick="setMode('fadh')">FADH2 (Complex II)</button>
</div>

<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Oxidative phosphorylation, technical view</title>
<desc>Complex I oxidizes NADH and pumps 4 protons; Complex II oxidizes succinate via FADH2 and pumps none. Ubiquinol carries electrons to Complex III, which pumps 4 protons via the Q cycle and reduces cytochrome c; Complex IV reduces oxygen to water and pumps 2 protons. The resulting proton-motive force of about 200 mV drives protons through the Fo c-ring, rotating the gamma shaft inside F1, whose three beta subunits cycle through loose, tight and open states to make ATP.</desc>
<defs><marker id="oxArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>

<text class="ts" x="40" y="24">Intermembrane space</text>
<text class="th" x="640" y="24" text-anchor="end" id="hCount"></text>
<rect x="30" y="110" width="620" height="60" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="40" y="326">Matrix</text>

<!-- complexes -->
<g id="cI"><rect x="70" y="100" width="40" height="80" rx="8" class="c-purple"/><rect x="72" y="176" width="22" height="30" rx="6" class="c-purple"/>
<text class="ts" x="90" y="122" text-anchor="middle">I</text></g>
<g id="cII"><rect x="140" y="132" width="30" height="58" rx="8" class="c-gray"/><text class="ts" x="155" y="166" text-anchor="middle">II</text></g>
<circle cx="190" cy="150" r="10" class="c-amber"/><text class="ts" x="190" y="154" text-anchor="middle" style="font-size:10px">Q</text>
<rect x="210" y="100" width="40" height="80" rx="8" class="c-teal"/><text class="ts" x="230" y="196" text-anchor="middle">III</text>
<circle cx="275" cy="102" r="9" class="c-red"/><text class="ts" x="275" y="106" text-anchor="middle" style="font-size:10px">c</text>
<rect x="300" y="100" width="40" height="80" rx="8" class="c-coral"/><text class="ts" x="342" y="196">IV</text>

<!-- electron donors -->
<g id="donNadh"><text class="ts" x="83" y="238" text-anchor="middle">NADH → NAD+</text></g>
<g id="donFad"><text class="ts" x="160" y="238" text-anchor="middle">succinate → fumarate</text><text class="ts" x="160" y="252" text-anchor="middle" style="font-size:10px">(FADH2 in Complex II)</text></g>

<!-- electron path, drawn in three legs -->
<g id="e1" class="stg"><path id="e1p" d="M83 224 L83 150 L178 150" stroke="#EF9F27" stroke-width="2.5" fill="none" marker-end="url(#oxArrow)"/></g>
<g id="e2" class="stg"><path d="M200 150 L230 150 L230 116 L264 104" stroke="#EF9F27" stroke-width="2.5" fill="none" marker-end="url(#oxArrow)"/></g>
<g id="e3" class="stg"><path d="M284 104 L320 116 L320 208" stroke="#EF9F27" stroke-width="2.5" fill="none" marker-end="url(#oxArrow)"/></g>

<!-- proton pumping -->
<g id="pI" class="stg"><path d="M98 96 L98 56" stroke="#B91C1C" stroke-width="2" fill="none" marker-end="url(#oxArrow)"/><text class="ts" x="104" y="64">4 H+</text></g>
<g id="pII" class="stg"><text class="ts" x="155" y="124" text-anchor="middle" style="fill:#888780">0 H+</text></g>
<g id="pIII" class="stg"><path d="M238 96 L238 56" stroke="#B91C1C" stroke-width="2" fill="none" marker-end="url(#oxArrow)"/><text class="ts" x="244" y="64">4 H+</text></g>
<g id="pIV" class="stg"><path d="M328 96 L328 56" stroke="#B91C1C" stroke-width="2" fill="none" marker-end="url(#oxArrow)"/><text class="ts" x="334" y="64">2 H+</text></g>

<g id="oxy" class="stg"><circle cx="322" cy="222" r="8" fill="#378ADD"/><text class="ts" x="322" y="250" text-anchor="middle">½O2 + 2H+ → H2O</text></g>

<!-- proton-motive force + ATP synthase -->
<g id="pmf" class="stg">
<path d="M520 52 L520 112" stroke="#B91C1C" stroke-width="2.5" fill="none" marker-end="url(#oxArrow)"/>
<text class="ts" x="512" y="48" text-anchor="end">Δp ≈ 200 mV</text>
<text class="ts" x="528" y="48">(mostly Δψ, plus ΔpH)</text>
</g>
<text class="ts" x="600" y="104" text-anchor="middle" style="font-size:10px">Fo c-ring</text>
<g id="cring">
<rect class="csub" x="484" y="126" width="7" height="28" rx="2" fill="#1D9E75" style="animation-delay:0s"/>
<rect class="csub" x="493" y="126" width="7" height="28" rx="2" fill="#1D9E75" style="animation-delay:.15s"/>
<rect class="csub" x="502" y="126" width="7" height="28" rx="2" fill="#1D9E75" style="animation-delay:.3s"/>
<rect class="csub" x="511" y="126" width="7" height="28" rx="2" fill="#1D9E75" style="animation-delay:.45s"/>
<rect class="csub" x="520" y="126" width="7" height="28" rx="2" fill="#1D9E75" style="animation-delay:.6s"/>
<rect class="csub" x="529" y="126" width="7" height="28" rx="2" fill="#1D9E75" style="animation-delay:.75s"/>
<rect class="csub" x="538" y="126" width="7" height="28" rx="2" fill="#1D9E75" style="animation-delay:.9s"/>
<rect class="csub" x="547" y="126" width="7" height="28" rx="2" fill="#1D9E75" style="animation-delay:1.05s"/>
</g>
<line x1="519" y1="154" x2="519" y2="236" stroke="var(--t)" stroke-width="3"/>
<text class="ts" x="512" y="194" text-anchor="end" style="font-size:10px">γ shaft</text>
<!-- F1 head: alternating alpha (grey) and beta (amber) subunits -->
<circle cx="550" cy="248" r="13" class="c-amber"/><text class="ts" id="b0" x="550" y="252" text-anchor="middle" style="font-size:10px"></text>
<circle cx="535" cy="274" r="13" class="c-gray"/>
<circle cx="505" cy="274" r="13" class="c-amber"/><text class="ts" id="b1" x="505" y="278" text-anchor="middle" style="font-size:10px"></text>
<circle cx="490" cy="248" r="13" class="c-gray"/>
<circle cx="505" cy="222" r="13" class="c-amber"/><text class="ts" id="b2" x="505" y="226" text-anchor="middle" style="font-size:10px"></text>
<circle cx="535" cy="222" r="13" class="c-gray"/>
<g id="gamma"><circle cx="520" cy="248" r="5" fill="var(--t)"/><line x1="520" y1="248" x2="520" y2="234" stroke="var(--t)" stroke-width="3"/></g>
<text class="ts" x="650" y="304" text-anchor="end" style="font-size:10px">F1 (α3β3)</text>
<text class="ts" x="650" y="318" text-anchor="end" style="font-size:10px">β: L loose · T tight · O open</text>

<g id="yield" class="stg">
<text class="th" x="466" y="282" text-anchor="end" id="poText"></text>
<text class="ts" x="466" y="300" text-anchor="end">~2.7 H+ per ATP</text>
<text class="ts" x="466" y="316" text-anchor="end">+1 H+ (ADP/Pi import)</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
let mode = 'nadh';
let bTimer = null, bPhase = 0;
const M = {
  nadh: {
    labels: [
      "Step 0 of 4 — Complex I oxidizes NADH: 2 e− pass via FMN and Fe–S clusters to ubiquinone (Q → QH2) while 4 H+ are pumped",
      "Step 1 of 4 — QH2 delivers electrons to Complex III; the Q cycle releases 4 H+ into the intermembrane space and reduces cytochrome c",
      "Step 2 of 4 — cytochrome c carries electrons to Complex IV, which reduces ½O2 to H2O and pumps 2 more H+ — 10 H+ per NADH in total",
      "Step 3 of 4 — the proton-motive force (Δp ≈ 200 mV, mostly membrane potential Δψ plus ΔpH) drives H+ back through the Fo c-ring, turning it and the γ shaft",
      "Step 4 of 4 — binding change in F1: the rotating γ shaft drives each β subunit through Loose → Tight (ATP forms) → Open (ATP released); 3 ATP per turn → P/O ≈ 2.5"
    ],
    counts: ["4 H+ pumped per NADH", "8 H+ pumped per NADH", "10 H+ pumped per NADH", "10 H+ pumped per NADH", "10 H+ pumped per NADH"],
    po: "P/O ≈ 10 ÷ 4 ≈ 2.5 ATP"
  },
  fadh: {
    labels: [
      "Step 0 of 4 — Complex II (succinate dehydrogenase, also a TCA-cycle enzyme) oxidizes succinate; FADH2 passes electrons to Q — Complex II pumps no protons",
      "Step 1 of 4 — QH2 delivers electrons to Complex III; the Q cycle releases 4 H+ into the intermembrane space and reduces cytochrome c",
      "Step 2 of 4 — cytochrome c carries electrons to Complex IV, which reduces ½O2 to H2O and pumps 2 more H+ — only 6 H+ per FADH2, because Complex I is bypassed",
      "Step 3 of 4 — the proton-motive force (Δp ≈ 200 mV, mostly membrane potential Δψ plus ΔpH) drives H+ back through the Fo c-ring, turning it and the γ shaft",
      "Step 4 of 4 — binding change in F1 as above; with 6 H+ instead of 10, each FADH2 yields fewer ATP → P/O ≈ 1.5"
    ],
    counts: ["0 H+ pumped per FADH2", "4 H+ pumped per FADH2", "6 H+ pumped per FADH2", "6 H+ pumped per FADH2", "6 H+ pumped per FADH2"],
    po: "P/O ≈ 6 ÷ 4 ≈ 1.5 ATP"
  }
};
const STATES = ['L', 'T', 'O'];
function showBeta() { for (let i = 0; i < 3; i++) document.getElementById('b' + i).textContent = STATES[(i + bPhase) % 3]; }
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnNadh').classList.toggle('active', m === 'nadh');
  document.getElementById('btnFad').classList.toggle('active', m === 'fadh');
  document.getElementById('cI').classList.toggle('dim', m === 'fadh');
  document.getElementById('cII').classList.toggle('dim', m === 'nadh');
  document.getElementById('donNadh').classList.toggle('hide', m !== 'nadh');
  document.getElementById('donFad').classList.toggle('hide', m !== 'fadh');
  document.getElementById('pI').classList.toggle('hide', m !== 'nadh');
  document.getElementById('pII').classList.toggle('hide', m !== 'fadh');
  document.getElementById('e1p').setAttribute('d', m === 'nadh' ? 'M83 224 L83 150 L178 150' : 'M160 224 L160 150 L178 150');
  document.getElementById('poText').textContent = M[m].po;
  render();
}
function render() {
  const c = M[mode];
  document.getElementById('stepLabel').textContent = c.labels[step];
  document.getElementById('hCount').textContent = c.counts[step];
  document.getElementById('e1').classList.toggle('on', step >= 0);
  document.getElementById('e2').classList.toggle('on', step >= 1);
  document.getElementById('e3').classList.toggle('on', step >= 2);
  document.getElementById('pI').classList.toggle('on', step >= 0);
  document.getElementById('pII').classList.toggle('on', step >= 0);
  document.getElementById('pIII').classList.toggle('on', step >= 1);
  document.getElementById('pIV').classList.toggle('on', step >= 2);
  document.getElementById('oxy').classList.toggle('on', step >= 2);
  document.getElementById('pmf').classList.toggle('on', step >= 3);
  document.querySelector('svg').classList.toggle('turning', step >= 3);
  document.getElementById('yield').classList.toggle('on', step >= 4);
  // beta-subunit states cycle only while ATP is being made
  if (bTimer) { clearInterval(bTimer); bTimer = null; }
  bPhase = 0; showBeta();
  if (step >= 4) bTimer = setInterval(() => { bPhase = (bPhase + 1) % 3; showBeta(); }, 900);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('nadh');
</script>
'''


# ---------------------------------------------------------------------------
# BLOOD_CLOTTING_GENERAL  (source: clotting.html)
# ---------------------------------------------------------------------------
BLOOD_CLOTTING_GENERAL = '''
<h2 class="sr-only">Interactive diagram of hemostasis: platelets plug an injured vessel, then the coagulation cascade converts fibrinogen into a fibrin mesh that stabilizes the clot.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 304" role="img">
<title>Hemostasis, general view</title>
<desc>Vessel injury exposes collagen, platelets adhere and aggregate to form a temporary plug, the coagulation cascade converges on thrombin, thrombin converts fibrinogen into fibrin strands, and the fibrin mesh stabilizes the clot.</desc>

<!-- vessel drawn as a tube; the top wall is broken at the injury, exposing collagen -->
<rect x="40" y="120" width="600" height="100" fill="#FCEBEB"/>
<text class="ts" x="60" y="200">Blood (lumen)</text>
<line x1="40" y1="220" x2="640" y2="220" stroke="#B91C1C" stroke-width="12"/>
<line x1="40" y1="120" x2="300" y2="120" stroke="#B91C1C" stroke-width="12"/>
<line x1="380" y1="120" x2="640" y2="120" stroke="#B91C1C" stroke-width="12"/>
<g id="injuryGap">
<path d="M302 104 Q312 92 322 104 T342 104 T362 104 T378 104" fill="none" stroke="#8B5A2B" stroke-width="2.5"/>
<path d="M304 114 Q314 102 324 114 T344 114 T364 114 T378 114" fill="none" stroke="#8B5A2B" stroke-width="2.5"/>
</g>
<text class="ts" x="340" y="76" text-anchor="middle">Vessel injury — collagen exposed</text>

<g id="platelets" class="stg">
<circle cx="316" cy="118" r="10" fill="#EF9F27"/>
<circle cx="340" cy="110" r="10" fill="#EF9F27"/>
<circle cx="364" cy="118" r="10" fill="#EF9F27"/>
<circle cx="328" cy="134" r="10" fill="#EF9F27"/>
<circle cx="352" cy="134" r="10" fill="#EF9F27"/>
<text class="ts" x="396" y="152">Platelet plug</text>
</g>

<g id="cascade" class="stg">
<circle cx="300" cy="160" r="5" fill="#7F77DD"/>
<circle cx="384" cy="166" r="5" fill="#7F77DD"/>
<circle cx="296" cy="140" r="5" fill="#7F77DD"/>
<text class="ts" x="340" y="248" text-anchor="middle">Coagulation cascade → thrombin</text>
</g>

<g id="fibrin" class="stg">
<path d="M302 100 L378 146 M306 146 L376 100 M300 124 L382 124 M318 96 L322 148 M358 96 L362 148" stroke="#7F77DD" stroke-width="2" fill="none"/>
<text class="ts" x="340" y="270" text-anchor="middle">Fibrinogen → fibrin mesh</text>
</g>

<g id="stableClot" class="stg">
<ellipse cx="340" cy="122" rx="54" ry="36" fill="none" stroke="#639922" stroke-width="2" stroke-dasharray="4 3"/>
<text class="th" x="340" y="294" text-anchor="middle">Stable clot</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — vessel injury exposes collagen",
  "Step 1 of 4 — platelets adhere and aggregate, forming a temporary plug",
  "Step 2 of 4 — coagulation cascade activates, converging on thrombin",
  "Step 3 of 4 — thrombin converts fibrinogen into fibrin strands",
  "Step 4 of 4 — fibrin mesh reinforces the platelet plug into a stable clot"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('injuryGap').classList.toggle('pulse', step === 0);
  document.getElementById('platelets').classList.toggle('on', step >= 1);
  document.getElementById('cascade').classList.toggle('on', step === 2);
  document.getElementById('fibrin').classList.toggle('on', step >= 3);
  document.getElementById('stableClot').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# BLOOD_GLUCOSE_HOMEOSTASIS_GENERAL  (source: glucose.html)
# ---------------------------------------------------------------------------
BLOOD_GLUCOSE_HOMEOSTASIS_GENERAL = '''
<h2 class="sr-only">Interactive diagram of blood glucose homeostasis: switchable view of the insulin pathway lowering high glucose and the glucagon pathway raising low glucose.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  #hDot { transition: cx 1.2s ease, cy 1.2s ease; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnHigh" onclick="setMode('high')">High blood glucose</button>
  <button id="btnLow" onclick="setMode('low')">Low blood glucose</button>
</div>

<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Blood glucose homeostasis</title>
<desc>When blood glucose is high, pancreatic beta cells release insulin, prompting cells to take up glucose via GLUT4 transporters, lowering blood glucose. When blood glucose is low, pancreatic alpha cells release glucagon, prompting the liver to break down glycogen and release glucose, raising blood glucose. Both loops return glucose toward the setpoint.</desc>

<defs><marker id="gluArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<rect x="30" y="130" width="620" height="40" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="42" y="125">Bloodstream</text>
<text class="ts" x="340" y="155" text-anchor="middle" id="glucoseLabel">Blood glucose: normal</text>

<g id="pancreas">
<ellipse cx="150" cy="80" rx="55" ry="35" class="c-amber"/>
<text class="ts" x="150" y="80" text-anchor="middle" dominant-baseline="central">Pancreas</text>
<text class="ts" x="150" y="32" text-anchor="middle" id="pancreasLabel"></text>
</g>

<g id="hormone" class="stg">
<circle id="hDot" cx="220" cy="110" r="8" fill="#7F77DD"/>
<text class="ts" x="230" y="104" id="hormoneLabel">Insulin</text>
</g>

<g id="targetOrgan" class="stg">
<rect x="480" y="60" width="100" height="60" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="530" y="95" text-anchor="middle" id="organLabel">Body cells</text>
</g>

<g id="effect" class="stg">
<path id="gluArrow1" d="M530 166 L530 124" stroke="#EF9F27" stroke-width="2.5" fill="none" marker-end="url(#gluArrow)"/>
<text class="ts" x="530" y="190" text-anchor="middle" id="effectLabel">GLUT4 uptake ↑</text>
</g>

<g id="resultArrow" class="stg">
<text class="th" x="340" y="226" text-anchor="middle" id="resultLabel">Blood glucose falls back to setpoint</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0</span>
</div>

<script>
let step = 0;
let mode = 'high';
const configHigh = {
  pancreasLabel: 'Beta cells sense high glucose',
  hormoneLabel: 'Insulin released',
  organLabel: 'Muscle / fat cells',
  effectLabel: 'GLUT4 moves to surface, glucose uptake ↑',
  resultLabel: 'Blood glucose falls back to setpoint',
  glucoseSteps: ['Blood glucose: high', 'Blood glucose: high, insulin rising', 'Blood glucose: falling', 'Blood glucose: back to setpoint'],
  captions: [
    'after a meal, blood glucose rises and pancreatic β cells sense it',
    'β cells release insulin into the blood',
    'insulin reaches muscle and fat cells: GLUT4 moves to the cell surface and glucose enters (the liver also stores glucose as glycogen)',
    'glucose falls back to its setpoint, and insulin release switches off (negative feedback)'
  ]
};
const configLow = {
  pancreasLabel: 'Alpha cells sense low glucose',
  hormoneLabel: 'Glucagon released',
  organLabel: 'Liver',
  effectLabel: 'Glycogen broken down, glucose released',
  resultLabel: 'Blood glucose rises back to setpoint',
  glucoseSteps: ['Blood glucose: low', 'Blood glucose: low, glucagon rising', 'Blood glucose: rising', 'Blood glucose: back to setpoint'],
  captions: [
    'between meals or during exercise, blood glucose falls and pancreatic α cells sense it',
    'α cells release glucagon into the blood',
    'glucagon reaches the liver, which breaks down glycogen (glycogenolysis), makes new glucose (gluconeogenesis) and releases it',
    'glucose rises back to its setpoint, and glucagon release switches off (negative feedback)'
  ]
};
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnHigh').classList.toggle('active', m === 'high');
  document.getElementById('btnLow').classList.toggle('active', m === 'low');
  const cfg = m === 'high' ? configHigh : configLow;
  document.getElementById('pancreasLabel').textContent = cfg.pancreasLabel;
  document.getElementById('hormoneLabel').textContent = cfg.hormoneLabel;
  document.getElementById('organLabel').textContent = cfg.organLabel;
  document.getElementById('effectLabel').textContent = cfg.effectLabel;
  document.getElementById('resultLabel').textContent = cfg.resultLabel;
  // glucose moves from blood into muscle/fat (high) or out of the liver into blood (low)
  document.getElementById('gluArrow1').setAttribute('d', m === 'high' ? 'M530 160 L530 124' : 'M530 122 L530 158');
  render();
}
function render() {
  const cfg = mode === 'high' ? configHigh : configLow;
  document.getElementById('glucoseLabel').textContent = cfg.glucoseSteps[step];
  document.getElementById('stepLabel').textContent = 'Step ' + step + ' of 3 — ' + cfg.captions[step];
  document.getElementById('hormone').classList.toggle('on', step >= 1);
  document.getElementById('hormone').classList.toggle('pulse', step === 1);
  // hormone travels in the blood to its target
  const h = document.getElementById('hDot'), hx = step >= 2 ? 470 : 220, hy = step >= 2 ? 120 : 110;
  h.setAttribute('cx', hx); h.setAttribute('cy', hy); h.style.cx = hx + 'px'; h.style.cy = hy + 'px';
  document.getElementById('targetOrgan').classList.toggle('on', step >= 2);
  document.getElementById('effect').classList.toggle('on', step >= 2);
  document.getElementById('resultArrow').classList.toggle('on', step >= 3);
}
function stepFwd() { if (step < 3) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('high');
</script>
'''


# ---------------------------------------------------------------------------
# BLOOD_GLUCOSE_HOMEOSTASIS_TECHNICAL
# ---------------------------------------------------------------------------
BLOOD_GLUCOSE_HOMEOSTASIS_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of glucose homeostasis: in high glucose, beta-cell glucose metabolism closes K-ATP channels, depolarization opens Ca2+ channels and insulin is secreted, then the insulin receptor, IRS-1, PI3K and Akt move GLUT4 to the membrane; in low glucose, alpha cells secrete glucagon, which acts through a Gs receptor, cAMP and PKA in hepatocytes to drive glycogenolysis and gluconeogenesis and glucose export.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .hide { display: none; }
  .mv { transition: cx 1.1s ease, cy 1.1s ease; }
  #glycogen { transition: transform .9s ease; transform-box: fill-box; transform-origin: center; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnHigh" onclick="setMode('high')">High blood glucose</button>
  <button id="btnLow" onclick="setMode('low')">Low blood glucose</button>
</div>

<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Glucose homeostasis, technical view</title>
<desc>High glucose: glucose enters the beta cell through GLUT2, glucokinase and metabolism raise ATP, ATP closes K-ATP channels, the cell depolarizes, L-type Ca2+ channels open and insulin granules are released; insulin binds its receptor tyrosine kinase on muscle and fat, signalling through IRS-1, PI3K and Akt to move GLUT4 to the membrane. Low glucose: the insulin brake on alpha cells lifts, alpha cells fire and release glucagon; glucagon acts on a Gs-coupled receptor in hepatocytes, raising cAMP and PKA, which drives glycogen breakdown and gluconeogenesis; glucose-6-phosphatase frees glucose, which leaves through GLUT2.</desc>
<defs><marker id="gtA" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>

<!-- frames -->
<rect x="30" y="40" width="270" height="260" rx="20" fill="var(--surface-1)" stroke="var(--t)" stroke-width="1"/>
<text class="th" x="44" y="64" id="leftName"></text>
<rect x="310" y="30" width="60" height="280" fill="#FCEBEB"/>
<text class="ts" x="340" y="24" text-anchor="middle">blood</text>
<rect x="380" y="40" width="270" height="260" rx="20" fill="var(--surface-1)" stroke="var(--t)" stroke-width="1"/>
<text class="th" x="394" y="64" id="rightName"></text>

<!-- shared: voltage-gated Ca2+ channel and Ca2+ entry -->
<rect x="150" y="294" width="26" height="12" rx="3" fill="#D85A30"/>
<text class="ts" x="163" y="324" text-anchor="middle">voltage-gated Ca2+ channel</text>
<g id="caIn" class="stg"><circle cx="158" cy="274" r="4" fill="#B91C1C"/><circle cx="172" cy="264" r="4" fill="#B91C1C"/><circle cx="160" cy="254" r="4" fill="#B91C1C"/>
<text class="ts" x="184" y="268">Ca2+ in</text></g>
<text class="ts" x="248" y="216" text-anchor="middle" id="granLabel"></text>

<!-- ===== HIGH glucose ===== -->
<g id="gHigh">
<rect x="24" y="82" width="12" height="24" rx="3" class="c-teal"/>
<text class="ts" x="44" y="88">GLUT2</text>
<g id="h0" class="stg">
<circle cx="56" cy="104" r="5" fill="#EF9F27"/>
<text class="ts" x="66" y="108">glucose → glucokinase →</text>
<text class="ts" x="44" y="126">glycolysis/TCA → ATP/ADP ↑</text>
</g>
<rect x="24" y="152" width="12" height="26" rx="3" fill="#EF9F27" stroke="#B45309" stroke-width="1"/>
<text class="ts" x="44" y="162">K_ATP (Kir6.2/SUR1)</text>
<text class="ts" x="44" y="178" id="katpState"></text>
<g id="h1" class="stg">
<path d="M20 156 L40 176 M40 156 L20 176" stroke="#B91C1C" stroke-width="2.5"/>
<text class="ts" x="44" y="206" style="fill:#D85A30">+ + + membrane depolarizes</text>
</g>
<!-- muscle / fat cell -->
<rect x="376" y="96" width="10" height="30" rx="3" class="c-purple"/>
<text class="ts" x="396" y="94">insulin receptor (tyrosine kinase)</text>
<g id="h3" class="stg"><text class="ts" x="396" y="124">autophosphorylation →</text><text class="ts" x="396" y="140">IRS-1 → PI3K → Akt</text></g>
<circle id="glut4a" class="mv" cx="530" cy="200" r="9" fill="#1D9E75"/>
<circle id="glut4b" class="mv" cx="566" cy="232" r="9" fill="#1D9E75"/>
<text class="ts" x="548" y="262" text-anchor="middle" id="glut4Label">GLUT4 vesicles</text>
<g id="h4" class="stg">
<path d="M346 196 L398 200" stroke="#EF9F27" stroke-width="2" fill="none" marker-end="url(#gtA)"/>
<path d="M346 240 L398 236" stroke="#EF9F27" stroke-width="2" fill="none" marker-end="url(#gtA)"/>
<text class="ts" x="410" y="220">glucose in</text>
<text class="ts" x="396" y="286">glycogen synthesis ↑ · lipogenesis ↑</text>
</g>
</g>

<!-- ===== LOW glucose ===== -->
<g id="gLow">
<g id="l0" class="stg">
<text class="ts" x="44" y="96">low glucose → β cells cut insulin,</text>
<text class="ts" x="44" y="112">removing their brake on α cells</text>
<text class="ts" x="44" y="132">adrenaline, amino acids also stimulate</text>
</g>
<g id="l1" class="stg"><text class="ts" x="44" y="180" style="fill:#D85A30">α cell fires action potentials</text></g>
<!-- hepatocyte -->
<rect x="376" y="96" width="10" height="30" rx="3" class="c-coral"/>
<text class="ts" x="396" y="94">glucagon receptor (Gs-coupled)</text>
<g id="l2" class="stg"><text class="ts" x="396" y="124">Gs → adenylyl cyclase →</text><text class="ts" x="396" y="140">cAMP → PKA</text></g>
<g id="glycogen">
<circle cx="560" cy="180" r="7" class="c-gray"/><circle cx="574" cy="172" r="7" class="c-gray"/><circle cx="574" cy="190" r="7" class="c-gray"/>
<circle cx="546" cy="172" r="7" class="c-gray"/><circle cx="546" cy="190" r="7" class="c-gray"/><circle cx="560" cy="164" r="7" class="c-gray"/><circle cx="560" cy="196" r="7" class="c-gray"/>
</g>
<text class="ts" x="560" y="222" text-anchor="middle">glycogen</text>
<g id="l3" class="stg">
<text class="ts" x="396" y="164">phosphorylase ↑ · synthase ↓</text>
<text class="ts" x="396" y="242">gluconeogenesis ↑</text>
<text class="ts" x="396" y="256" style="font-size:10px">(PEPCK, FBPase-1, G6Pase)</text>
</g>
<rect x="376" y="270" width="10" height="22" rx="3" class="c-teal"/>
<g id="l4" class="stg">
<path d="M420 282 L350 282" stroke="#EF9F27" stroke-width="2.5" fill="none" marker-end="url(#gtA)"/>
<text class="ts" x="428" y="286">G6Pase → glucose → GLUT2 out</text>
</g>
</g>

<!-- hormone molecules (insulin or glucagon) -->
<circle class="hd mv" r="6"/>
<circle class="hd mv" r="6"/>
<circle class="hd mv" r="6"/>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
let mode = 'high';
const GRAN = [[236, 160], [256, 180], [236, 196]];
const BLOOD = [[340, 130], [340, 170], [340, 210]];
const BOUND = [[366, 111], [340, 170], [340, 210]];
const M = {
  high: {
    left: 'Pancreatic β cell', right: 'Muscle / fat cell', gran: 'insulin granules', color: '#7F77DD',
    labels: [
      "Step 0 of 4 — glucose enters the β cell through GLUT2 (mainly GLUT1 in humans) and is phosphorylated by glucokinase, the glucose sensor; its metabolism raises the ATP/ADP ratio",
      "Step 1 of 4 — the rise in ATP closes K_ATP channels (Kir6.2/SUR1), which sulfonylureas also close, so K+ stops leaking out and the membrane depolarizes",
      "Step 2 of 4 — depolarization opens voltage-gated (L-type) Ca2+ channels; the Ca2+ influx triggers exocytosis of insulin granules into the blood",
      "Step 3 of 4 — insulin binds its receptor tyrosine kinase on muscle and fat; autophosphorylation recruits IRS-1, which activates PI3K and then Akt",
      "Step 4 of 4 — Akt moves GLUT4 vesicles to the membrane so glucose enters; insulin also switches on glycogen synthase and lipogenesis and suppresses hepatic glucose output"
    ],
    hormone: ['gran', 'gran', 'blood', 'bound', 'bound'],
    caOn: s => s >= 2
  },
  low: {
    left: 'Pancreatic α cell', right: 'Hepatocyte (liver)', gran: 'glucagon granules', color: '#D85A30',
    labels: [
      "Step 0 of 4 — blood glucose falls (fasting, exercise): β cells cut insulin release, lifting insulin's paracrine brake on α cells; adrenaline and amino acids also stimulate them",
      "Step 1 of 4 — α cells fire action potentials; Ca2+ entry through voltage-gated channels triggers exocytosis of glucagon granules into the blood",
      "Step 2 of 4 — glucagon binds its Gs-coupled receptor on hepatocytes → adenylyl cyclase → cAMP → PKA",
      "Step 3 of 4 — PKA activates glycogen phosphorylase (via phosphorylase kinase) and inactivates glycogen synthase, so glycogen is broken down; it also boosts gluconeogenesis (PEPCK, FBPase-1, G6Pase)",
      "Step 4 of 4 — glucose-6-phosphatase frees glucose, which leaves through GLUT2 into the blood; muscle lacks G6Pase, so only liver (and kidney) can export glucose"
    ],
    hormone: ['gran', 'blood', 'bound', 'bound', 'bound'],
    caOn: s => s >= 1
  }
};
function place(el, xy) { el.setAttribute('cx', xy[0]); el.setAttribute('cy', xy[1]); el.style.cx = xy[0] + 'px'; el.style.cy = xy[1] + 'px'; }
function setMode(m) {
  mode = m; step = 0;
  const c = M[m];
  document.getElementById('btnHigh').classList.toggle('active', m === 'high');
  document.getElementById('btnLow').classList.toggle('active', m === 'low');
  document.getElementById('gHigh').classList.toggle('hide', m !== 'high');
  document.getElementById('gLow').classList.toggle('hide', m !== 'low');
  document.getElementById('leftName').textContent = c.left;
  document.getElementById('rightName').textContent = c.right;
  document.getElementById('granLabel').textContent = c.gran;
  document.querySelectorAll('.hd').forEach(d => d.setAttribute('fill', c.color));
  render();
}
function render() {
  const c = M[mode];
  document.getElementById('stepLabel').textContent = c.labels[step];
  const where = c.hormone[step];
  document.querySelectorAll('.hd').forEach((d, i) => place(d, (where === 'gran' ? GRAN : where === 'blood' ? BLOOD : BOUND)[i]));
  document.getElementById('caIn').classList.toggle('on', c.caOn(step));
  if (mode === 'high') {
    document.getElementById('h0').classList.toggle('on', step >= 0);
    document.getElementById('h1').classList.toggle('on', step >= 1);
    document.getElementById('katpState').textContent = step >= 1 ? 'closed by ATP' : 'open: K+ leaks out';
    document.getElementById('h3').classList.toggle('on', step >= 3);
    document.getElementById('h4').classList.toggle('on', step >= 4);
    const up = step >= 4;
    place(document.getElementById('glut4a'), up ? [392, 196] : [530, 200]);
    place(document.getElementById('glut4b'), up ? [392, 238] : [566, 232]);
    document.getElementById('glut4Label').textContent = up ? '' : 'GLUT4 vesicles';
  } else {
    document.getElementById('l0').classList.toggle('on', step >= 0);
    document.getElementById('l1').classList.toggle('on', step >= 1);
    document.getElementById('l2').classList.toggle('on', step >= 2);
    document.getElementById('l3').classList.toggle('on', step >= 3);
    document.getElementById('l4').classList.toggle('on', step >= 4);
    document.getElementById('glycogen').style.transform = step >= 3 ? 'scale(0.55)' : 'none';
  }
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('high');
</script>
'''


# ---------------------------------------------------------------------------
# MITOSIS_TECHNICAL  (source: mitosis_technical.html)
# ---------------------------------------------------------------------------
MITOSIS_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of mitosis: cohesin holds sister chromatids together, the spindle assembly checkpoint blocks anaphase until every kinetochore is bi-oriented, separase cleaves cohesin to trigger separation, and an actomyosin ring drives cytokinesis.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #chromLeft, #chromRight { transition: transform 1s ease; }
  .separated #chromLeft { transform: translateX(-70px); }
  .separated #chromRight { transform: translateX(70px); }
  #kinL, #kinR { transition: transform 1s ease; }
  .separated #kinL { transform: translateX(-70px); }
  .separated #kinR { transform: translateX(70px); }
  #furrow { transition: transform 1s ease; transform-box: fill-box; transform-origin: center; }
  .constricted #furrow { transform: scaleY(0.3); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Mitosis, technical view</title>
<desc>Cohesin rings hold sister chromatids together. Kinetochores attach to spindle microtubules from both poles; the spindle assembly checkpoint blocks progression until every chromosome is bi-oriented and under tension. Once satisfied, the anaphase-promoting complex triggers separase to cleave cohesin, sister chromatids separate, and an actomyosin contractile ring pinches the cell in two during cytokinesis.</desc>

<ellipse cx="340" cy="170" rx="220" ry="130" fill="none" stroke="var(--t)" stroke-width="1.5"/>

<g id="chromLeft">
<line x1="332" y1="138" x2="332" y2="182" stroke="#378ADD" stroke-width="6" stroke-linecap="round"/>
<circle id="cohesinL" cx="335" cy="160" r="3" fill="#EF9F27"/>
</g>
<g id="chromRight">
<line x1="348" y1="138" x2="348" y2="182" stroke="#378ADD" stroke-width="6" stroke-linecap="round"/>
<circle id="cohesinR" cx="345" cy="160" r="3" fill="#EF9F27"/>
</g>
<line id="cohesinLink" x1="335" y1="160" x2="345" y2="160" stroke="#EF9F27" stroke-width="2"/>
<text class="ts" x="340" y="240" text-anchor="middle">Sister chromatids (identical)</text>

<g id="kinetochores" class="stg">
<circle id="kinL" cx="325" cy="160" r="4" class="c-purple"/>
<circle id="kinR" cx="355" cy="160" r="4" class="c-purple"/>
<text class="ts" x="340" y="128" text-anchor="middle">Kinetochores</text>
</g>

<g id="spindleSearching" class="stg">
<line x1="140" y1="170" x2="321" y2="160" stroke="var(--t)" stroke-width="0.75" stroke-dasharray="3 3" opacity="0.5"/>
<line x1="540" y1="170" x2="359" y2="160" stroke="var(--t)" stroke-width="0.75" stroke-dasharray="3 3" opacity="0.5"/>
<text class="ts" x="340" y="90" text-anchor="middle" id="sacLabel">SAC active — anaphase blocked</text>
</g>

<g id="spindleAttached" class="stg">
<line x1="140" y1="170" x2="321" y2="160" stroke="var(--t)" stroke-width="1"/>
<line x1="540" y1="170" x2="359" y2="160" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="340" y="90" text-anchor="middle" id="attachedLabel">Bi-oriented, under tension — SAC satisfied</text>
</g>

<g id="separaseNote" class="stg">
<text class="th" x="340" y="200" text-anchor="middle">Separase cleaves cohesin</text>
</g>

<g id="furrowGroup" class="stg">
<rect id="furrow" x="330" y="60" width="20" height="220" fill="var(--border-strong)" opacity="0.5"/>
<text class="ts" x="340" y="310" text-anchor="middle">Actomyosin ring constricts</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 5</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 5 — cohesin holds sister chromatids together",
  "Step 1 of 5 — kinetochores assemble at each centromere",
  "Step 2 of 5 — spindle fibers probe for attachment; SAC blocks anaphase until bi-oriented",
  "Step 3 of 5 — bi-orientation achieved, tension detected, SAC satisfied — APC/C activates",
  "Step 4 of 5 — separase cleaves cohesin, sister chromatids pulled apart",
  "Step 5 of 5 — actomyosin contractile ring constricts, completing cytokinesis"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('kinetochores').classList.toggle('on', step >= 1);
  document.getElementById('spindleSearching').classList.toggle('on', step === 2);
  document.getElementById('spindleAttached').classList.toggle('on', step >= 3 && step < 4);
  document.getElementById('sacLabel').style.opacity = step === 2 ? '1' : '0';
  document.getElementById('attachedLabel').style.opacity = step === 3 ? '1' : '0';
  document.getElementById('separaseNote').classList.toggle('on', step === 4);
  document.getElementById('cohesinLink').style.opacity = step >= 4 ? '0' : '1';
  document.querySelector('svg').classList.toggle('separated', step >= 4);
  document.getElementById('furrowGroup').classList.toggle('on', step >= 5);
  document.querySelector('svg').classList.toggle('constricted', step >= 5);
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# TRANSCRIPTION_TECHNICAL  (source: transcription_technical.html)
# ---------------------------------------------------------------------------
TRANSCRIPTION_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of transcription initiation: TFIID binds the TATA box, general transcription factors assemble the pre-initiation complex, TFIIH unwinds the DNA, and the 5' end of the mRNA is capped co-transcriptionally.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #rnapGroup { transition: transform 1.2s ease; }
  .elongating #rnapGroup { transform: translateX(160px); }
  #mrnaTail { transition: stroke-dashoffset 1.2s ease; }
  #bubble { transition: opacity .5s ease, transform 1.2s ease; }
  .elongating #bubble { transform: translateX(160px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Transcription initiation, technical view</title>
<desc>TFIID recognizes and binds the TATA box, other general transcription factors assemble into the pre-initiation complex, TFIIH's helicase activity opens the DNA to form the transcription bubble, RNA polymerase II begins synthesizing mRNA, and the 5' end is capped with a modified guanine nucleotide co-transcriptionally.</desc>

<line x1="30" y1="180" x2="630" y2="180" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<line x1="30" y1="200" x2="630" y2="200" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>

<rect id="tataBox" x="90" y="170" width="40" height="40" fill="none" stroke="#EF9F27" stroke-width="1.5" stroke-dasharray="3 3"/>
<text class="ts" x="86" y="172" text-anchor="end">TATA box</text>

<g id="tfiid" class="stg">
<circle cx="110" cy="150" r="14" class="c-purple"/>
<text class="ts" x="110" y="150" text-anchor="middle" dominant-baseline="central">TFIID</text>
</g>

<g id="pic" class="stg">
<circle cx="85" cy="130" r="10" class="c-teal"/>
<text class="ts" x="85" y="115" text-anchor="middle">TFIIB</text>
<circle cx="140" cy="125" r="10" class="c-teal"/>
<text class="ts" x="140" y="110" text-anchor="middle">TFIIF</text>
<circle cx="165" cy="145" r="10" class="c-amber"/>
<text class="ts" x="175" y="130" text-anchor="middle">TFIIH</text>
<text class="ts" x="115" y="95" text-anchor="middle">Pre-initiation complex</text>
</g>

<g id="bubble" class="stg">
<path d="M110 180 Q150 160 190 180" stroke="#378ADD" stroke-width="3" fill="none"/>
<path d="M110 200 Q150 220 190 200" stroke="#D85A30" stroke-width="3" fill="none"/>
<text class="ts" x="150" y="262" text-anchor="middle">TFIIH unwinds DNA — transcription bubble</text>
</g>

<g id="rnapGroup" class="stg">
<circle cx="150" cy="190" r="18" class="c-purple"/>
<text class="ts" x="150" y="190" text-anchor="middle" dominant-baseline="central">Pol II</text>
</g>

<g id="mrna" class="stg">
<path id="mrnaTail" d="M118 240 Q130 214 152 212 C210 236 260 236 308 212" pathLength="100" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-dasharray="100 100" stroke-dashoffset="77.7"/>
<circle id="capG" cx="118" cy="240" r="6" fill="#B91C1C" opacity="0"/>
<text class="ts" x="106" y="244" text-anchor="end" id="capLabel" opacity="0">5' cap</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — TFIID (via TBP) recognizes and binds the TATA box",
  "Step 1 of 4 — TFIIB, TFIIF, TFIIH and RNA Pol II assemble into the pre-initiation complex",
  "Step 2 of 4 — TFIIH's helicase activity unwinds the DNA, forming the transcription bubble",
  "Step 3 of 4 — Pol II begins elongating; the 5' end is capped co-transcriptionally",
  "Step 4 of 4 — elongation continues down the gene, capped mRNA growing"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('tfiid').classList.toggle('on', step >= 0);
  document.getElementById('tfiid').classList.toggle('pulse', step === 0);
  document.getElementById('pic').classList.toggle('on', step >= 1);
  document.getElementById('rnapGroup').classList.toggle('on', step >= 1);
  document.getElementById('mrnaTail').style.strokeDashoffset = step >= 4 ? '0' : '77.7';
  document.getElementById('bubble').classList.toggle('on', step >= 2);
  document.getElementById('mrna').classList.toggle('on', step >= 3);
  document.getElementById('capG').setAttribute('opacity', step >= 3 ? '1' : '0');
  document.getElementById('capLabel').setAttribute('opacity', step >= 3 ? '1' : '0');
  document.querySelector('svg').classList.toggle('elongating', step === 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# TRANSLATION_TECHNICAL  (source: translation_technical.html)
# ---------------------------------------------------------------------------
TRANSLATION_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of translation elongation: EF-Tu delivers aminoacyl-tRNA with wobble base pairing at the third codon position, peptide bond formation, EF-G-driven translocation, and SRP-mediated targeting to the ER for secreted proteins.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .trna, .aa { transition: cx .9s ease, cy .9s ease, opacity .5s ease; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #ribosomeGroup { transition: transform 1s ease; }
  .translocated #ribosomeGroup { transform: translateX(30px); }   /* one codon = one site width (30 px) */
  #efTu { transition: transform .9s ease, opacity .5s ease; }
  .tuGone #efTu { transform: translate(70px, -40px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Translation elongation, technical view</title>
<defs><marker id="arrowTT" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<desc>EF-Tu bound to GTP delivers aminoacyl-tRNA to the ribosome's A site, where codon-anticodon pairing is checked, including wobble pairing at the third codon position. After GTP hydrolysis and accommodation, the ribozyme peptidyl transferase forms a peptide bond, and EF-G bound to GTP drives translocation, ratcheting the ribosome one codon forward. If a signal sequence emerges, the signal recognition particle targets the whole complex to the ER membrane.</desc>

<line x1="30" y1="240" x2="650" y2="240" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>

<g id="ribosomeGroup">
<ellipse cx="200" cy="230" rx="55" ry="20" class="c-gray"/>
<ellipse cx="200" cy="200" rx="55" ry="26" class="c-purple"/>
<rect x="155" y="222" width="18" height="16" rx="3" fill="none" stroke="var(--t)" stroke-width="0.5"/>
<rect x="185" y="222" width="18" height="16" rx="3" fill="none" stroke="var(--t)" stroke-width="0.5"/>
<rect x="215" y="222" width="18" height="16" rx="3" fill="none" stroke="var(--t)" stroke-width="0.5"/>
<text class="ts" x="164" y="234" text-anchor="middle" font-size="8">E</text>
<text class="ts" x="194" y="234" text-anchor="middle" font-size="8">P</text>
<text class="ts" x="224" y="234" text-anchor="middle" font-size="8">A</text>
<text class="ts" x="140" y="196" text-anchor="end">Ribosome</text>

<g id="srp" class="stg">
<path d="M180 130 L200 110 L220 130" stroke="#B91C1C" stroke-width="2" fill="none"/>
<text class="ts" x="200" y="95" text-anchor="middle">SRP recognizes signal sequence</text>
</g>
</g>

<circle id="tP" class="trna c-teal" cx="194" cy="212" r="7"/>
<circle id="tA" class="trna c-amber" cx="246" cy="170" r="7"/>
<circle id="aaA" class="aa c-coral" cx="246" cy="156" r="5"/>
<circle id="c1" class="aa c-coral" cx="194" cy="198" r="5"/>
<circle id="c2" class="aa c-coral" cx="186" cy="188" r="5"/>
<circle id="c3" class="aa c-coral" cx="180" cy="177" r="5"/>
<text class="ts" x="160" y="280" text-anchor="middle" id="tPlbl">peptidyl-tRNA</text>

<g id="efTu" class="stg">
<circle cx="264" cy="150" r="15" class="c-amber"/>
<text class="ts" x="264" y="150" text-anchor="middle" dominant-baseline="central" font-size="9">EF-Tu</text>
<text class="ts" x="264" y="128" text-anchor="middle" id="wobbleLabel">Checking codon-anticodon (wobble at position 3)</text>
<text class="ts" x="300" y="150" text-anchor="start" id="gdpLabel" opacity="0">GTP → GDP, leaves</text>
</g>

<g id="peptideBond" class="stg">
<circle cx="214" cy="194" r="9" fill="none" stroke="#EA580C" stroke-width="2" class="pulse"/>
<text class="ts" x="192" y="150" text-anchor="middle">Peptidyl transferase (rRNA ribozyme)</text>
</g>

<g id="efG" class="stg">
<circle cx="256" cy="206" r="12" class="c-teal"/>
<text class="ts" x="256" y="206" text-anchor="middle" dominant-baseline="central" font-size="9">EF-G</text>
<text class="ts" x="256" y="262" text-anchor="middle">Drives translocation (ratchet)</text>
</g>

<g id="erMembrane" class="stg">
<rect x="450" y="60" width="20" height="280" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="460" y="50" text-anchor="middle">ER membrane</text>
<circle cx="460" cy="200" r="10" fill="none" stroke="#B91C1C" stroke-width="1.5"/>
<text class="ts" x="460" y="225" text-anchor="middle">Translocon</text>
<path d="M290 150 Q380 130 444 192" fill="none" stroke="#B91C1C" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arrowTT)"/>
<text class="ts" x="380" y="122" text-anchor="middle" fill="#B91C1C">SRP brings the ribosome to the ER</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — EF-Tu-GTP delivers aminoacyl-tRNA to the A site; wobble pairing checked at codon position 3",
  "Step 1 of 4 — GTP hydrolyzed, EF-Tu released, tRNA fully accommodates",
  "Step 2 of 4 — peptidyl transferase (a ribozyme) forms the peptide bond",
  "Step 3 of 4 — EF-G-GTP drives translocation, ratcheting the ribosome one codon forward",
  "Step 4 of 4 — if a signal sequence emerges, SRP targets the complex to the ER translocon"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('efTu').classList.toggle('on', step === 0);
  document.getElementById('peptideBond').classList.toggle('on', step >= 1 && step <= 2);
  document.getElementById('efG').classList.toggle('on', step === 3);
  document.querySelector('svg').classList.toggle('translocated', step >= 3);
  document.getElementById('srp').classList.toggle('on', step >= 4);
  const svg = document.querySelector('svg');
  svg.classList.toggle('tuGone', step >= 1);                                  // EF-Tu-GDP leaves after GTP hydrolysis
  document.getElementById('efTu').style.opacity = step === 1 ? '0.5' : '';
  document.getElementById('gdpLabel').setAttribute('opacity', step === 1 ? '1' : '0');
  const set = (id, x, y) => { const e = document.getElementById(id); e.setAttribute('cx', x); e.setAttribute('cy', y); e.style.cx = x + 'px'; e.style.cy = y + 'px'; };
  // aminoacyl-tRNA: held by EF-Tu (step 0), accommodated in the A site (step 1 on)
  if (step === 0) { set('tA', 246, 170); set('aaA', 246, 156); } else { set('tA', 224, 212); set('aaA', 224, 198); }
  // peptide bond (step 2): the chain is transferred from the P-site tRNA onto the A-site amino acid
  const chainOnA = step >= 2;
  set('c1', chainOnA ? 216 : 194, chainOnA ? 186 : 198);
  set('c2', chainOnA ? 210 : 186, chainOnA ? 175 : 188);
  set('c3', chainOnA ? 206 : 180, chainOnA ? 163 : 177);
  // after translocation the old P-site tRNA is in the E site (now empty) and exits
  document.getElementById('tP').style.opacity = step === 3 ? '0.45' : (step >= 4 ? '0' : '1');
  document.getElementById('tPlbl').textContent = step === 3 ? 'empty tRNA in E site → exits' : (step >= 4 ? '' : 'peptidyl-tRNA');
  document.getElementById('erMembrane').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# NEPHRON_FILTRATION_GENERAL  (source: nephron.html)
# ---------------------------------------------------------------------------
NEPHRON_FILTRATION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of nephron function: blood is filtered at the glomerulus, useful solutes are reabsorbed along the tubule, waste is secreted, and the remainder becomes urine.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .drift { animation: drift 1.6s ease-in-out infinite; }
  @keyframes drift { 0%{transform:translateX(0)} 100%{transform:translateX(60px)} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Nephron function, general view</title>
<desc>Blood enters the glomerulus where fluid and small solutes are filtered into Bowman's capsule, retaining blood cells and large proteins. The filtrate flows through the tubule, where useful substances like glucose, amino acids, and water are reabsorbed back into the blood, and waste products are secreted into the filtrate, which becomes urine.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<circle id="glom" cx="120" cy="150" r="45" fill="none" stroke="#B91C1C" stroke-width="2"/>
<text class="ts" x="120" y="154" text-anchor="middle">Glomerulus</text>
<g id="bloodIn" class="stg">
<path d="M30 70 L80 112" stroke="#B91C1C" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="30" y="62">Blood in (afferent arteriole)</text>
</g>
<circle cx="120" cy="150" r="60" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="3 3"/>
<text class="ts" x="120" y="222" text-anchor="middle">Bowman's capsule</text>

<path d="M180 150 Q300 100 400 150 Q500 200 600 150" stroke="var(--t)" stroke-width="3" fill="none"/>
<text class="ts" x="400" y="235" text-anchor="middle">Tubule</text>

<g id="filtrate" class="stg">
<circle class="drift" cx="185" cy="150" r="5" fill="#378ADD"/>
<circle class="drift" cx="185" cy="145" r="5" fill="#EF9F27" style="animation-delay:.3s"/>
<text class="ts" x="190" y="180">Filtrate — water, ions, glucose</text>
</g>

<g id="reabsorption" class="stg">
<line x1="296" y1="118" x2="296" y2="72" stroke="#639922" stroke-width="1.5" marker-end="url(#arrow)"/>
<text class="ts" x="296" y="62" text-anchor="middle">Glucose, water, ions reabsorbed → blood</text>
</g>

<g id="secretion" class="stg">
<line x1="480" y1="240" x2="480" y2="184" stroke="#B91C1C" stroke-width="1.5" marker-end="url(#arrow)"/>
<text class="ts" x="480" y="258" text-anchor="middle">Waste, H+, K+ secreted → filtrate</text>
</g>

<g id="urine" class="stg">
<circle cx="600" cy="150" r="16" fill="#D4A017"/>
<text class="ts" x="600" y="185" text-anchor="middle">Urine</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — blood enters the glomerulus",
  "Step 1 of 4 — glomerular filtration: fluid and small solutes filtered into Bowman's capsule",
  "Step 2 of 4 — reabsorption: glucose, amino acids, water, and ions returned to the blood",
  "Step 3 of 4 — secretion: waste products and excess ions added into the filtrate",
  "Step 4 of 4 — remaining filtrate concentrated into urine"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('bloodIn').classList.toggle('on', step === 0);
  document.getElementById('glom').classList.toggle('pulse', step === 0);
  document.getElementById('filtrate').classList.toggle('on', step >= 1);
  document.getElementById('reabsorption').classList.toggle('on', step >= 2);
  document.getElementById('secretion').classList.toggle('on', step >= 3);
  document.getElementById('urine').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# NEPHRON_FILTRATION_TECHNICAL
# ---------------------------------------------------------------------------
NEPHRON_FILTRATION_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of nephron function: Starling forces set the glomerular filtration rate, then the proximal tubule, loop of Henle, distal tubule and collecting duct each handle solutes and water with specific transporters over the corticomedullary osmotic gradient; ADH decides whether the final urine is dilute or concentrated.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .hide { display: none; }
  .seg { transition: stroke .4s ease, stroke-width .4s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnHyd" onclick="setMode('hyd')">Hydrated (low ADH)</button>
  <button id="btnDeh" onclick="setMode('deh')">Dehydrated (high ADH)</button>
</div>

<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Nephron function, technical view</title>
<desc>Glomerular capillary pressure minus plasma oncotic pressure and Bowman's capsule pressure gives a net filtration pressure of about 10 mmHg and a GFR of about 125 mL/min. The proximal tubule reabsorbs about two-thirds of sodium and water iso-osmotically and all filtered glucose through SGLT2 and SGLT1. The descending limb loses water through aquaporin-1 into the hypertonic medulla, and the water-impermeable thick ascending limb pumps out NaCl through NKCC2, building the gradient and diluting the fluid. The distal tubule reabsorbs NaCl through NCC and calcium under PTH. In the collecting duct, aldosterone drives ENaC and ROMK, and ADH inserts aquaporin-2 so water leaves and urine is concentrated; without ADH, dilute urine is excreted.</desc>
<defs>
<marker id="nfArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
<linearGradient id="medGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FDE7C8" stop-opacity=".25"/><stop offset="1" stop-color="#F59E0B" stop-opacity=".45"/></linearGradient>
</defs>

<!-- cortex and medulla with the osmotic gradient -->
<rect x="30" y="30" width="620" height="90" fill="var(--surface-1)"/>
<rect x="30" y="120" width="620" height="200" fill="url(#medGrad)"/>
<text class="ts" x="644" y="46" text-anchor="end">Cortex · 300</text>
<text class="ts" x="644" y="136" text-anchor="end">Medulla · 300</text>
<text class="ts" x="644" y="200" text-anchor="end">600</text>
<text class="ts" x="644" y="260" text-anchor="end">900</text>
<text class="ts" x="644" y="314" text-anchor="end">1200 mOsm/kg</text>

<!-- nephron -->
<circle cx="70" cy="74" r="30" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="3 3"/>
<circle id="glom" cx="70" cy="74" r="20" fill="none" stroke="#B91C1C" stroke-width="2.5"/>
<path id="sPCT" class="seg" d="M100 74 Q115 54 130 74 T160 74 T190 74 L210 84" fill="none" stroke="#888780" stroke-width="3"/>
<path id="sLoop" class="seg" d="M210 84 L215 296 Q235 326 255 296" fill="none" stroke="#888780" stroke-width="3"/>
<path id="sTAL" class="seg" d="M255 296 L260 112" fill="none" stroke="#888780" stroke-width="5"/>
<path id="sDCT" class="seg" d="M260 112 Q290 92 320 102 T380 100 L420 92" fill="none" stroke="#888780" stroke-width="3"/>
<path id="sCD" class="seg" d="M420 92 L560 72 L560 320" fill="none" stroke="#888780" stroke-width="4"/>

<!-- step 0: Starling forces -->
<g id="t0" class="stg">
<text class="ts" x="110" y="24">P_GC 55 − π_GC 30 − P_BS 15 = net +10 mmHg → GFR ≈ 125 mL/min (180 L/day)</text>
</g>
<!-- step 1: proximal tubule -->
<g id="t1" class="stg">
<path d="M150 64 L150 40" stroke="#639922" stroke-width="2" fill="none" marker-end="url(#nfArrow)"/>
<text class="ts" x="158" y="44">SGLT2/1: all glucose · ~65% Na+ &amp; water · HCO3−</text>
<text class="ts" x="204" y="116" text-anchor="end">fluid stays ~300 (iso-osmotic)</text>
</g>
<!-- step 2: loop of Henle -->
<g id="t2" class="stg">
<path d="M212 190 L182 190" stroke="#378ADD" stroke-width="2" fill="none" marker-end="url(#nfArrow)"/>
<text class="ts" x="178" y="186" text-anchor="end">descending:</text>
<text class="ts" x="178" y="200" text-anchor="end">water out (AQP1)</text>
<path d="M258 220 L290 220" stroke="#D85A30" stroke-width="2" fill="none" marker-end="url(#nfArrow)"/>
<text class="ts" x="296" y="216">thick ascending: NKCC2 pumps NaCl out,</text>
<text class="ts" x="296" y="230">impermeable to water → builds the gradient</text>
<text class="ts" x="236" y="336" text-anchor="middle" style="font-size:10px">tip ≈ 1200</text>
<text class="ts" x="268" y="130">fluid ≈ 100 (dilute)</text>
</g>
<!-- step 3: distal tubule -->
<g id="t3" class="stg">
<text class="ts" x="290" y="62">DCT: NCC (thiazide target) · Ca2+ reabsorbed (PTH)</text>
</g>
<!-- step 4: collecting duct, depends on ADH -->
<g id="t4" class="stg">
<text class="ts" x="548" y="150" text-anchor="end">ENaC: Na+ in · ROMK: K+ out (aldosterone)</text>
<text class="ts" x="548" y="166" text-anchor="end" id="adhText"></text>
<g id="water">
<path d="M556 200 L524 200" stroke="#378ADD" stroke-width="2" fill="none" marker-end="url(#nfArrow)"/>
<path d="M556 240 L524 240" stroke="#378ADD" stroke-width="2" fill="none" marker-end="url(#nfArrow)"/>
<path d="M556 280 L524 280" stroke="#378ADD" stroke-width="2" fill="none" marker-end="url(#nfArrow)"/>
<text class="ts" x="520" y="244" text-anchor="end">water out</text>
</g>
<text class="th" x="548" y="316" text-anchor="end" id="urineText"></text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
let mode = 'deh';
const common = [
  "Step 0 of 4 — glomerulus: glomerular capillary pressure (~55 mmHg) minus plasma oncotic pressure (~30) and Bowman's capsule pressure (~15) leaves ~10 mmHg net filtration → GFR ≈ 125 mL/min",
  "Step 1 of 4 — proximal tubule: SGLT2 (and SGLT1) reabsorb all filtered glucose, plus ~65% of Na+ and water, amino acids and HCO3−; fluid leaves still iso-osmotic (~300 mOsm)",
  "Step 2 of 4 — loop of Henle: the descending limb loses water through AQP1 into the hypertonic medulla; the water-tight thick ascending limb pumps NaCl out via NKCC2 — the countercurrent multiplier that builds the gradient and dilutes the fluid",
  "Step 3 of 4 — distal convoluted tubule: NCC (the thiazide target) reabsorbs ~5% of NaCl; Ca2+ is reabsorbed under PTH; fluid stays dilute"
];
const M = {
  hyd: {
    last: "Step 4 of 4 — collecting duct, low ADH: aldosterone still tunes Na+/K+ via ENaC and ROMK, but without AQP2 the duct is water-tight — large volumes of dilute urine (~50–100 mOsm)",
    adh: "low ADH: no AQP2 inserted — duct stays water-tight",
    urine: "Urine ≈ 50–100 mOsm · large volume",
    water: false
  },
  deh: {
    last: "Step 4 of 4 — collecting duct, high ADH: V2 receptor → cAMP inserts AQP2; water leaves into the hypertonic medulla — small volume of concentrated urine (up to ~1200 mOsm)",
    adh: "high ADH: AQP2 inserted (V2 → cAMP)",
    urine: "Urine up to ~1200 mOsm · small volume",
    water: true
  }
};
const SEGS = ['glom', 'sPCT', 'sLoop', 'sDCT', 'sCD'];
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnHyd').classList.toggle('active', m === 'hyd');
  document.getElementById('btnDeh').classList.toggle('active', m === 'deh');
  document.getElementById('adhText').textContent = M[m].adh;
  document.getElementById('urineText').textContent = M[m].urine;
  document.getElementById('water').classList.toggle('hide', !M[m].water);
  render();
}
function render() {
  document.getElementById('stepLabel').textContent = step < 4 ? common[step] : M[mode].last;
  for (let i = 0; i <= 4; i++) document.getElementById('t' + i).classList.toggle('on', step === i);
  // highlight the segment being described
  SEGS.forEach((id, i) => {
    const el = document.getElementById(id);
    if (id === 'glom') { el.style.strokeWidth = step === 0 ? 4 : 2.5; return; }
    el.style.stroke = step === i ? '#378ADD' : '#888780';
  });
  const tal = document.getElementById('sTAL');
  tal.style.stroke = step === 2 ? '#D85A30' : '#888780';
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('deh');
</script>
'''


# ---------------------------------------------------------------------------
# REFLEX_ARC_GENERAL  (source: reflex_arc.html)
# ---------------------------------------------------------------------------
REFLEX_ARC_GENERAL = '''
<h2 class="sr-only">Interactive diagram of the patellar reflex arc: a tap stretches the muscle spindle, a sensory neuron carries the signal to the spinal cord, it synapses directly onto a motor neuron, and the quadriceps contracts while the hamstring relaxes.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text, text.stg:not(.on) { visibility: hidden; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Patellar reflex arc, general view</title>
<desc>A tap stretches the muscle spindle in the quadriceps, triggering a sensory neuron that carries the signal to the spinal cord. It synapses directly onto a motor neuron, monosynaptic and bypassing the brain, which signals the quadriceps to contract. An inhibitory interneuron simultaneously relaxes the antagonist hamstring muscle, a process called reciprocal inhibition.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<rect x="30" y="120" width="70" height="100" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="65" y="112" text-anchor="middle">Quadriceps</text>
<circle id="tap" cx="65" cy="170" r="8" fill="#EF9F27"/>

<ellipse cx="580" cy="170" rx="70" ry="90" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<text class="ts" x="580" y="70" text-anchor="middle">Spinal cord</text>

<g id="sensoryPath" class="stg">
<path d="M100 170 Q300 90 520 140" stroke="#378ADD" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="300" y="80" text-anchor="middle">Sensory (afferent) neuron</text>
</g>

<g id="synapse" class="stg">
<circle cx="540" cy="150" r="6" fill="#7F77DD"/>
<text class="ts" x="580" y="282" text-anchor="middle">Monosynaptic — no brain involved</text>
</g>

<g id="motorPath" class="stg">
<path d="M520 190 Q300 260 100 200" stroke="#D85A30" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="330" y="252" text-anchor="middle">Motor (efferent) neuron</text>
</g>

<g id="contraction" class="stg">
<text class="th" x="65" y="245" text-anchor="middle">Contracts</text>
</g>

<rect id="hamstring" x="150" y="248" width="70" height="44" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1" class="stg"/>
<text class="ts stg" x="185" y="243" text-anchor="middle" id="hamLabel1">Hamstring</text>
<g id="inhibition" class="stg">
<path d="M540 156 L556 196" stroke="#888780" stroke-width="1.5" fill="none"/>
<circle cx="558" cy="202" r="6" class="c-gray"/>
<text class="ts" x="570" y="206">interneuron</text>
<path d="M552 210 Q420 300 224 274" stroke="#888780" stroke-width="2" stroke-dasharray="5 4" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="185" y="308" text-anchor="middle">Inhibitory interneuron relaxes it (reciprocal inhibition)</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — tap stretches the muscle spindle in the quadriceps",
  "Step 1 of 4 — sensory neuron carries the signal to the spinal cord",
  "Step 2 of 4 — synapses directly onto a motor neuron — monosynaptic, no brain involved",
  "Step 3 of 4 — motor neuron signals the quadriceps to contract",
  "Step 4 of 4 — reciprocal inhibition: an interneuron relaxes the hamstring simultaneously"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('tap').classList.toggle('pulse', step === 0);
  document.getElementById('sensoryPath').classList.toggle('on', step >= 1);
  document.getElementById('synapse').classList.toggle('on', step >= 2);
  document.getElementById('motorPath').classList.toggle('on', step >= 3);
  document.getElementById('contraction').classList.toggle('on', step >= 3);
  document.getElementById('hamstring').classList.toggle('on', step >= 4);
  document.getElementById('hamLabel1').classList.toggle('on', step >= 4);
  document.getElementById('inhibition').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# BARORECEPTOR_REFLEX_GENERAL  (source: baroreceptor.html)
# ---------------------------------------------------------------------------
BARORECEPTOR_REFLEX_GENERAL = '''
<h2 class="sr-only">Interactive diagram of the baroreceptor reflex: rising blood pressure stretches baroreceptors, the medulla increases parasympathetic and decreases sympathetic output, and heart rate and vessel tone fall, returning blood pressure to its setpoint.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text, text.stg:not(.on) { visibility: hidden; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Baroreceptor reflex, general view</title>
<desc>Rising blood pressure stretches baroreceptors in the carotid sinus and aortic arch. Increased signaling reaches the medulla's cardiovascular center, which raises parasympathetic and lowers sympathetic output to the heart and vessels, reducing heart rate and contractility and dilating vessels, bringing blood pressure back down toward its setpoint.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<text class="th" x="120" y="80" text-anchor="middle" id="bpLabel">Blood pressure: normal</text>
<ellipse cx="120" cy="140" rx="50" ry="30" fill="none" stroke="#B91C1C" stroke-width="2"/>
<text class="ts" x="120" y="140" text-anchor="middle" dominant-baseline="central">Carotid sinus</text>
<circle id="baro" cx="120" cy="110" r="6" fill="#EF9F27"/>

<g id="signal1" class="stg">
<path d="M170 140 Q280 90 380 130" stroke="#378ADD" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="280" y="80" text-anchor="middle">Afferent signal ↑</text>
</g>

<ellipse cx="440" cy="130" rx="60" ry="40" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="440" y="130" text-anchor="middle" dominant-baseline="central">Medulla</text>

<g id="outputChange" class="stg">
<text class="ts" x="500" y="190" text-anchor="middle" id="outputLabel">Parasympathetic ↑, sympathetic ↓</text>
</g>

<g id="signal2" class="stg">
<path d="M400 170 Q280 220 170 200" stroke="#D85A30" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="280" y="240" text-anchor="middle">Efferent signal to heart & vessels</text>
</g>

<ellipse cx="120" cy="220" rx="45" ry="30" class="c-coral stg" id="heart"/>
<text class="ts stg" x="120" y="220" text-anchor="middle" dominant-baseline="central" id="heartLabel">Heart rate ↓</text>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 3</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 3 — blood pressure rises, baroreceptors stretch",
  "Step 1 of 3 — afferent signal to the medulla's cardiovascular center increases",
  "Step 2 of 3 — medulla raises parasympathetic, lowers sympathetic output",
  "Step 3 of 3 — heart rate and vessel tone fall, blood pressure returns to setpoint"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('bpLabel').textContent = step === 0 ? 'Blood pressure: rising' : step >= 3 ? 'Blood pressure: back to setpoint' : 'Blood pressure: elevated';
  document.getElementById('baro').classList.toggle('pulse', step === 0);
  document.getElementById('signal1').classList.toggle('on', step >= 1);
  document.getElementById('outputChange').classList.toggle('on', step >= 2);
  document.getElementById('signal2').classList.toggle('on', step >= 2);
  document.getElementById('heart').classList.toggle('on', step >= 3);
  document.getElementById('heartLabel').classList.toggle('on', step >= 3);
}
function stepFwd() { if (step < 3) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# BARORECEPTOR_REFLEX_TECHNICAL
# ---------------------------------------------------------------------------
BARORECEPTOR_REFLEX_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of the baroreceptor reflex: carotid sinus and aortic arch baroreceptors signal through cranial nerves IX and X to the nucleus tractus solitarius, which drives the nucleus ambiguus (vagal output) and, through the CVLM, inhibits the RVLM (sympathetic output); shown for a rise and for a fall in blood pressure.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.1s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.45} }
  .nuc { transition: opacity .5s ease; }
  .nuc.lo { opacity: .35; }
  .nuc circle { transition: stroke-width .4s ease; }
  .nuc.hi circle { stroke-width: 4; }
  .outPath { transition: stroke-width .5s ease, opacity .5s ease; }
  #vessel { transition: transform .8s ease; transform-box: fill-box; transform-origin: center; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnRise" onclick="setMode('rise')">BP rises</button>
  <button id="btnFall" onclick="setMode('fall')">BP falls (standing up)</button>
</div>

<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Baroreceptor reflex, technical view</title>
<desc>Baroreceptors in the carotid sinus (cranial nerve IX) and aortic arch (cranial nerve X) fire faster when stretched. They excite the nucleus tractus solitarius (NTS) in the medulla, which excites the nucleus ambiguus (vagal output to the heart) and the caudal ventrolateral medulla (CVLM); the CVLM inhibits the rostral ventrolateral medulla (RVLM), the source of sympathetic drive to the heart, vessels and kidney. A rise in pressure therefore slows the heart and dilates vessels; a fall in pressure does the opposite.</desc>
<defs><marker id="brArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>

<text class="th" x="30" y="22" id="bpLabel">Arterial pressure: ↑ high</text>

<!-- sensors -->
<g id="sensors">
<ellipse cx="90" cy="80" rx="46" ry="22" fill="none" stroke="#B91C1C" stroke-width="2"/>
<text class="ts" x="90" y="84" text-anchor="middle">Carotid sinus</text>
<path d="M48 196 Q90 140 132 196" fill="none" stroke="#B91C1C" stroke-width="5" stroke-linecap="round"/>
<text class="ts" x="90" y="214" text-anchor="middle">Aortic arch</text>
</g>

<!-- afferent nerves -->
<g id="afferent" class="stg">
<path d="M136 80 L278 80" stroke="#378ADD" stroke-width="2" fill="none" marker-end="url(#brArrow)"/>
<text class="ts" x="206" y="72" text-anchor="middle">CN IX</text>
<path d="M126 176 Q220 160 284 98" stroke="#378ADD" stroke-width="2" fill="none" marker-end="url(#brArrow)"/>
<text class="ts" x="214" y="180" text-anchor="middle">CN X</text>
</g>

<!-- medulla -->
<rect x="250" y="30" width="222" height="186" rx="14" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.75"/>
<text class="ts" x="262" y="208">Medulla</text>

<path d="M320 80 L396 80" stroke="var(--t)" stroke-width="1.5" fill="none" marker-end="url(#brArrow)"/>
<path d="M300 100 L300 146" stroke="var(--t)" stroke-width="1.5" fill="none" marker-end="url(#brArrow)"/>
<path d="M320 170 L398 170 M400 161 L400 179" stroke="var(--t)" stroke-width="1.5" fill="none"/>
<text class="ts" x="359" y="162" text-anchor="middle" style="font-size:10px">inhibits</text>

<g id="nNTS" class="nuc"><circle cx="300" cy="80" r="20" class="c-purple"/><text class="ts" x="300" y="84" text-anchor="middle">NTS</text></g>
<g id="nNA" class="nuc"><circle cx="420" cy="80" r="20" class="c-teal"/><text class="ts" x="420" y="84" text-anchor="middle">NA</text></g>
<g id="nCVLM" class="nuc"><circle cx="300" cy="170" r="20" class="c-gray"/><text class="ts" x="300" y="174" text-anchor="middle">CVLM</text></g>
<g id="nRVLM" class="nuc"><circle cx="420" cy="170" r="20" class="c-coral"/><text class="ts" x="420" y="174" text-anchor="middle">RVLM</text></g>
<text class="th" x="272" y="70" text-anchor="end" id="aNTS"></text>
<text class="th" x="420" y="52" text-anchor="middle" id="aNA"></text>
<text class="th" x="272" y="160" text-anchor="end" id="aCVLM"></text>
<text class="th" x="448" y="152" text-anchor="middle" id="aRVLM"></text>

<!-- outputs -->
<path id="vagal" class="outPath" d="M440 80 Q500 80 560 100" stroke="#0F6E56" stroke-width="2" fill="none" marker-end="url(#brArrow)"/>
<text class="ts" x="500" y="72" text-anchor="middle">vagus (parasymp.)</text>
<g id="symp" class="outPath">
<path d="M440 172 Q500 168 566 122" stroke="#D85A30" stroke-width="2" fill="none" marker-end="url(#brArrow)"/>
<path d="M440 176 Q500 196 544 220" stroke="#D85A30" stroke-width="2" fill="none" marker-end="url(#brArrow)"/>
<path d="M440 180 Q480 268 568 296" stroke="#D85A30" stroke-width="2" fill="none" marker-end="url(#brArrow)"/>
</g>
<text class="ts" x="470" y="322">sympathetic</text>

<!-- effectors -->
<circle cx="592" cy="104" r="26" class="c-red"/>
<text class="ts" x="592" y="108" text-anchor="middle">Heart</text>
<g id="eHeart" class="stg"><text class="th" x="592" y="148" text-anchor="middle" id="tHeart"></text><text class="th" x="592" y="164" text-anchor="middle" id="tHeart2"></text></g>

<text class="ts" x="598" y="190" text-anchor="middle">Arterioles &amp; veins</text>
<g id="vessel">
<line x1="548" y1="210" x2="650" y2="210" stroke="#B91C1C" stroke-width="3"/>
<line x1="548" y1="234" x2="650" y2="234" stroke="#B91C1C" stroke-width="3"/>
</g>
<g id="eVessel" class="stg"><text class="th" x="598" y="256" text-anchor="middle" id="tVessel"></text></g>

<ellipse cx="600" cy="300" rx="28" ry="16" class="c-amber"/>
<text class="ts" x="600" y="304" text-anchor="middle">Kidney</text>
<g id="eKidney" class="stg"><text class="th" x="600" y="332" text-anchor="middle" id="tKidney"></text></g>

<!-- afferent firing-rate strip -->
<text class="ts" x="30" y="252">Baroreceptor firing</text>
<rect x="30" y="260" width="180" height="30" rx="4" fill="none" stroke="var(--t)" stroke-width="0.75"/>
<g id="ticks"></g>
<text class="ts" x="30" y="306" id="rateLabel"></text>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
let mode = 'rise';
const M = {
  rise: {
    labels: [
      "Step 0 of 4 — blood pressure rises: the carotid sinus and aortic arch walls stretch, and mechanosensitive channels (PIEZO1/2) depolarize the baroreceptor endings",
      "Step 1 of 4 — firing rate increases on CN IX (glossopharyngeal, carotid) and CN X (vagus, aortic) into the nucleus tractus solitarius (NTS)",
      "Step 2 of 4 — the NTS excites the nucleus ambiguus (vagal output ↑) and the CVLM, which inhibits the RVLM (sympathetic output ↓)",
      "Step 3 of 4 — effectors: vagal ACh on M2 receptors slows the SA node; less sympathetic drive lowers contractility, dilates arterioles and veins, and reduces renin release",
      "Step 4 of 4 — cardiac output and peripheral resistance fall, blood pressure returns toward setpoint, and firing settles back to baseline"
    ],
    bp: ["↑ high", "↑ high", "↑ high", "↑ high", "→ back to setpoint"],
    rate: [18, 18, 18, 18, 8],
    nts: "↑", na: "↑", cvlm: "↑", rvlm: "↓",
    heart: ["HR ↓", "contractility ↓"], vessel: "dilate", kidney: "renin ↓", vScale: 1.35
  },
  fall: {
    labels: [
      "Step 0 of 4 — standing up: blood pools in the legs, venous return and blood pressure drop, and the baroreceptors are stretched less",
      "Step 1 of 4 — firing on CN IX and CN X falls — less excitatory input reaches the NTS",
      "Step 2 of 4 — NTS drive weakens: the nucleus ambiguus quietens (vagal output ↓) and the CVLM no longer restrains the RVLM (sympathetic output ↑)",
      "Step 3 of 4 — effectors: heart rate and contractility rise (β1), arterioles and veins constrict (α1), and the kidney releases renin (β1) → angiotensin II",
      "Step 4 of 4 — cardiac output and resistance rise, blood pressure is restored within seconds, and firing returns to baseline"
    ],
    bp: ["↓ low", "↓ low", "↓ low", "↓ low", "→ restored"],
    rate: [3, 3, 3, 3, 8],
    nts: "↓", na: "↓", cvlm: "↓", rvlm: "↑",
    heart: ["HR ↑", "contractility ↑"], vessel: "constrict", kidney: "renin ↑", vScale: 0.6
  }
};
function cfg() { return M[mode]; }
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnRise').classList.toggle('active', m === 'rise');
  document.getElementById('btnFall').classList.toggle('active', m === 'fall');
  render();
}
function drawTicks(n) {
  const g = document.getElementById('ticks');
  g.innerHTML = '';
  for (let i = 0; i < n; i++) {
    const x = 38 + (i + 0.5) * (164 / n);
    const l = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    l.setAttribute('x1', x); l.setAttribute('x2', x); l.setAttribute('y1', 265); l.setAttribute('y2', 285);
    l.setAttribute('stroke', '#378ADD'); l.setAttribute('stroke-width', '2');
    g.appendChild(l);
  }
  document.getElementById('rateLabel').textContent = n > 8 ? 'firing ↑ (more stretch)' : n < 8 ? 'firing ↓ (less stretch)' : 'baseline firing';
}
function setNuc(id, arrowId, dir, active) {
  const el = document.getElementById(id);
  el.classList.toggle('lo', active && dir === '↓');
  el.classList.toggle('hi', active && dir === '↑');
  document.getElementById(arrowId).textContent = active ? dir : '';
}
function render() {
  const c = cfg();
  document.getElementById('stepLabel').textContent = c.labels[step];
  document.getElementById('bpLabel').textContent = 'Arterial pressure: ' + c.bp[step];
  document.getElementById('sensors').classList.toggle('pulse', step === 0);
  drawTicks(c.rate[step]);
  document.getElementById('afferent').classList.toggle('on', step >= 1);
  const inBrain = step >= 1 && step <= 3;
  setNuc('nNTS', 'aNTS', c.nts, inBrain);
  setNuc('nNA', 'aNA', c.na, step >= 2 && step <= 3);
  setNuc('nCVLM', 'aCVLM', c.cvlm, step >= 2 && step <= 3);
  setNuc('nRVLM', 'aRVLM', c.rvlm, step >= 2 && step <= 3);
  // output pathways: the active limb thickens, the withdrawn limb fades
  const out = step >= 2 && step <= 3;
  const v = document.getElementById('vagal'), s = document.getElementById('symp');
  v.style.strokeWidth = out && c.na === '↑' ? 4 : 2;
  v.style.opacity = out && c.na === '↓' ? 0.3 : 1;
  s.style.opacity = out && c.rvlm === '↓' ? 0.3 : 1;
  s.querySelectorAll('path').forEach(p => p.style.strokeWidth = out && c.rvlm === '↑' ? 4 : 2);
  const eff = step >= 3;
  document.getElementById('tHeart').textContent = c.heart[0];
  document.getElementById('tHeart2').textContent = c.heart[1];
  document.getElementById('tVessel').textContent = c.vessel;
  document.getElementById('tKidney').textContent = c.kidney;
  ['eHeart', 'eVessel', 'eKidney'].forEach(id => document.getElementById(id).classList.toggle('on', eff && step === 3));
  document.getElementById('vessel').style.transform = step === 3 ? `scaleY(${c.vScale})` : 'none';
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('rise');
</script>
'''


# ---------------------------------------------------------------------------
# CARDIAC_MUSCLE_CONTRACTION_GENERAL  (source: cardiac_muscle.html)
# ---------------------------------------------------------------------------
CARDIAC_MUSCLE_CONTRACTION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of cardiac muscle excitation-contraction coupling: a small calcium trigger influx opens ryanodine receptors for calcium-induced calcium release, and the signal spreads to neighboring cells through gap junctions at intercalated discs.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text, text.stg:not(.on) { visibility: hidden; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .drift-up { animation: driftup 1.4s ease-in-out infinite; }
  @keyframes driftup { 0%{transform:translateY(0)} 100%{transform:translateY(-30px)} }
  #cellRight { transition: opacity 0.6s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Cardiac muscle excitation-contraction coupling</title>
<desc>An action potential opens a small number of L-type calcium channels in the T-tubule, and this trigger calcium binds ryanodine receptors on the sarcoplasmic reticulum, releasing a much larger flood of calcium — calcium-induced calcium release — that drives contraction. The electrical signal then spreads to the neighboring cardiomyocyte through gap junctions clustered at the intercalated disc, so the tissue contracts as a single functional unit.</desc>

<rect x="60" y="60" width="220" height="180" rx="12" fill="var(--surface-1)" stroke="var(--t)" stroke-width="1.5"/>
<text class="ts" x="170" y="50" text-anchor="middle">Cardiomyocyte 1</text>

<rect id="cellRight" x="320" y="60" width="220" height="180" rx="12" fill="var(--surface-1)" stroke="var(--t)" stroke-width="1.5" class="stg"/>
<text class="ts stg" x="430" y="50" text-anchor="middle" id="cell2Label">Cardiomyocyte 2</text>

<rect x="280" y="60" width="40" height="180" fill="#7F77DD" opacity="0.3"/>
<text class="ts" x="300" y="255" text-anchor="middle" id="idLabel">Intercalated disc</text>

<g id="lTypeChannel" class="stg">
<rect x="70" y="210" width="14" height="22" fill="#EF9F27"/>
<text class="ts" x="90" y="225">L-type Ca2+ channel (trigger)</text>
</g>

<ellipse cx="170" cy="130" rx="60" ry="32" fill="none" stroke="#B91C1C" stroke-width="1.5" stroke-dasharray="3 3"/>
<text class="ts" x="170" y="90" text-anchor="middle">Sarcoplasmic reticulum</text>

<g id="ryr" class="stg">
<circle cx="130" cy="154" r="6" class="c-red"/>
<text class="ts" x="130" y="178" text-anchor="middle">Ryanodine receptor</text>
</g>

<g id="cicr" class="stg">
<circle class="drift-up" cx="150" cy="140" r="4" fill="#B91C1C"/>
<circle class="drift-up" cx="165" cy="135" r="4" fill="#B91C1C" style="animation-delay:.2s"/>
<circle class="drift-up" cx="180" cy="142" r="4" fill="#B91C1C" style="animation-delay:.4s"/>
<circle class="drift-up" cx="195" cy="148" r="4" fill="#B91C1C" style="animation-delay:.6s"/>
<text class="ts" x="170" y="198" text-anchor="middle">Calcium-induced calcium release</text>
</g>

<g id="gapJunction" class="stg">
<circle cx="300" cy="120" r="5" fill="#1D9E75"/>
<circle cx="300" cy="150" r="5" fill="#1D9E75"/>
<circle cx="300" cy="180" r="5" fill="#1D9E75"/>
<text class="ts" x="300" y="50" text-anchor="middle" id="gjLabel">Gap junctions</text>
</g>

<g id="cell2Activity" class="stg">
<circle class="drift-up" cx="420" cy="150" r="4" fill="#B91C1C"/>
<circle class="drift-up" cx="435" cy="145" r="4" fill="#B91C1C" style="animation-delay:.2s"/>
<text class="ts" x="430" y="196" text-anchor="middle">Same coupling repeats —</text>
<text class="ts" x="430" y="211" text-anchor="middle">syncytial contraction</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — resting cardiomyocyte, no signal",
  "Step 1 of 4 — action potential opens L-type Ca2+ channels — a small trigger influx",
  "Step 2 of 4 — trigger Ca2+ opens ryanodine receptors — calcium-induced calcium release floods the cell",
  "Step 3 of 4 — the electrical signal crosses gap junctions at the intercalated disc",
  "Step 4 of 4 — the neighboring cell depolarizes and contracts the same way — the heart acts as one syncytium"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('lTypeChannel').classList.toggle('on', step >= 1);
  document.getElementById('lTypeChannel').classList.toggle('pulse', step === 1);
  document.getElementById('ryr').classList.toggle('on', step >= 2);
  document.getElementById('cicr').classList.toggle('on', step >= 2);
  document.getElementById('gapJunction').classList.toggle('on', step >= 3);
  document.getElementById('cell2Label').classList.toggle('on', step >= 3);
  document.getElementById('cellRight').style.opacity = step >= 3 ? '1' : '0.4';
  document.getElementById('cell2Activity').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# CARDIAC_MUSCLE_CONTRACTION_TECHNICAL
# ---------------------------------------------------------------------------
CARDIAC_MUSCLE_CONTRACTION_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of cardiac excitation-contraction coupling: trigger Ca2+ through L-type channels opens RyR2 across the dyad (calcium-induced calcium release), Ca2+ binds troponin C, relaxation by SERCA2a (regulated by phospholamban) and the Na+/Ca2+ exchanger, and beta-adrenergic enhancement through PKA.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .cyt { transition: opacity .6s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Cardiac excitation-contraction coupling, technical view</title>
<desc>An action potential opens L-type Ca2+ channels in the T-tubule; the small trigger influx crosses the dyad and opens RyR2 on the junctional sarcoplasmic reticulum, releasing a much larger amount of Ca2+ (calcium-induced calcium release). Ca2+ binds troponin C and the cell contracts, with force graded by the amount released. SERCA2a, braked by phospholamban, pumps most Ca2+ back into the SR and the Na+/Ca2+ exchanger removes the rest from the cell. Beta-1 adrenergic stimulation activates PKA, which phosphorylates the L-type channel and phospholamban, giving a larger and faster Ca2+ transient.</desc>
<defs><marker id="ctArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>

<!-- sarcolemma with a T-tubule dipping into the cell -->
<text class="ts" x="40" y="40">Extracellular</text>
<path d="M30 60 L140 60 L140 140 L180 140 L180 60 L650 60" fill="none" stroke="var(--t)" stroke-width="2"/>
<text class="ts" x="188" y="100">T-tubule</text>

<!-- L-type Ca2+ channel on the T-tubule floor -->
<rect x="152" y="134" width="16" height="12" rx="2" fill="#EF9F27" stroke="#B45309" stroke-width="1"/>
<text class="ts" x="134" y="118" text-anchor="end">L-type Ca2+</text>
<text class="ts" x="134" y="131" text-anchor="end">channel</text>
<text class="ts" x="186" y="155" style="font-size:9px">dyad ~15 nm</text>

<!-- junctional SR with RyR2 facing the L-type channel -->
<rect x="100" y="160" width="240" height="46" rx="18" fill="none" stroke="#B91C1C" stroke-width="1.5" stroke-dasharray="3 3"/>
<text class="ts" x="230" y="188" text-anchor="middle">SR (Ca2+ store)</text>
<circle id="ryr" cx="160" cy="164" r="7" class="c-red"/>
<text class="ts" x="112" y="196">RyR2</text>

<!-- SERCA2a + phospholamban on the SR -->
<circle cx="320" cy="206" r="8" class="c-green"/>
<text class="ts" x="332" y="226">SERCA2a</text>
<circle cx="304" cy="214" r="5" class="c-gray"/>
<text class="ts" x="296" y="232" text-anchor="end">PLB</text>
<g id="serca" class="stg"><path d="M322 252 L322 220" stroke="#15803D" stroke-width="2" fill="none" marker-end="url(#ctArrow)"/>
<text class="ts" x="332" y="250">Ca2+ back into SR</text></g>

<!-- NCX on the sarcolemma -->
<rect x="322" y="52" width="16" height="16" rx="3" class="c-teal"/>
<text class="ts" x="330" y="86" text-anchor="middle">NCX</text>
<g id="ncx" class="stg">
<path d="M346 72 L346 30" stroke="#B91C1C" stroke-width="2" fill="none" marker-end="url(#ctArrow)"/>
<text class="ts" x="352" y="36">1 Ca2+ out</text>
<path d="M314 26 L314 70" stroke="#0F6E56" stroke-width="2" fill="none" marker-end="url(#ctArrow)"/>
<text class="ts" x="308" y="36" text-anchor="end">3 Na+ in</text>
</g>

<!-- trigger Ca2+ in the dyad -->
<g id="trigger" class="stg">
<circle cx="156" cy="151" r="3" fill="#B91C1C"/><circle cx="166" cy="154" r="3" fill="#B91C1C"/>
</g>
<g id="release" class="stg"><path d="M160 172 L170 214" stroke="#B91C1C" stroke-width="2" fill="none" marker-end="url(#ctArrow)"/></g>

<!-- cytosolic Ca2+ -->
<circle class="cyt" cx="130" cy="226" r="4" fill="#B91C1C"/>
<circle class="cyt" cx="152" cy="238" r="4" fill="#B91C1C"/>
<circle class="cyt" cx="176" cy="226" r="4" fill="#B91C1C"/>
<circle class="cyt" cx="198" cy="240" r="4" fill="#B91C1C"/>
<circle class="cyt" cx="220" cy="228" r="4" fill="#B91C1C"/>
<circle class="cyt" cx="242" cy="242" r="4" fill="#B91C1C"/>
<circle class="cyt" cx="262" cy="226" r="4" fill="#B91C1C"/>
<circle class="cyt" cx="140" cy="254" r="4" fill="#B91C1C"/>
<circle class="cyt" cx="230" cy="256" r="4" fill="#B91C1C"/>
<text class="ts" x="40" y="244" id="cytLabel">cytosolic Ca2+</text>

<!-- Ca2+ transient plot -->
<text class="ts" x="400" y="84">[Ca2+]i transient</text>
<line x1="400" y1="190" x2="640" y2="190" stroke="var(--t)" stroke-width="1"/>
<line x1="400" y1="92" x2="400" y2="190" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="640" y="204" text-anchor="end">time</text>
<path id="baseTrace" d="" fill="none" stroke="#888780" stroke-width="1.5" stroke-dasharray="4 3"/>
<path id="caTrace" d="M400 180 L640 180" fill="none" stroke="#B91C1C" stroke-width="2.5" stroke-linejoin="round"/>
<g id="baseKey" class="stg"><text class="ts" x="636" y="104" text-anchor="end">dashed = baseline beat</text></g>

<!-- myofilaments -->
<line x1="390" y1="262" x2="640" y2="262" stroke="#378ADD" stroke-width="5" stroke-linecap="round"/>
<rect x="440" y="270" width="160" height="14" rx="3" fill="#7F77DD"/>
<circle class="tnc" cx="425" cy="262" r="6" class="c-purple"/>
<circle class="tnc" cx="515" cy="262" r="6" class="c-purple"/>
<circle class="tnc" cx="605" cy="262" r="6" class="c-purple"/>
<text class="ts" x="640" y="248" text-anchor="end">Troponin C on actin · myosin</text>
<g id="contract" class="stg"><text class="th" x="515" y="304" text-anchor="middle">Ca2+ on troponin C → cross-bridges cycle</text></g>

<!-- beta-adrenergic: PKA phosphorylations -->
<g id="beta" class="stg">
<circle cx="90" cy="60" r="8" class="c-coral"/>
<text class="ts" x="40" y="80">β1 → cAMP → PKA</text>
<circle cx="174" cy="132" r="6" class="c-coral"/><text x="174" y="135" text-anchor="middle" style="font-size:8px;font-weight:600;fill:#7F1D1D">P</text>
<circle cx="296" cy="208" r="6" class="c-coral"/><text x="296" y="211" text-anchor="middle" style="font-size:8px;font-weight:600;fill:#7F1D1D">P</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 5</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 5 — the action potential spreads down the T-tubule and opens L-type Ca2+ channels (Cav1.2) — a small trigger influx into the dyad",
  "Step 1 of 5 — trigger Ca2+ binds RyR2 on the junctional SR across the ~15 nm dyad and opens it: calcium-induced calcium release amplifies the signal ~10× (no mechanical DHPR–RyR link, unlike skeletal muscle)",
  "Step 2 of 5 — cytosolic Ca2+ rises ~10-fold and binds troponin C — cross-bridges cycle and the cell contracts; force is graded by how much Ca2+ is released",
  "Step 3 of 5 — relaxation: SERCA2a pumps most of the Ca2+ (~70%) back into the SR; phospholamban (PLB) acts as its brake",
  "Step 4 of 5 — relaxation: the Na+/Ca2+ exchanger (NCX) removes the rest (3 Na+ in for 1 Ca2+ out), so Ca2+ entry and exit balance beat to beat",
  "Step 5 of 5 — sympathetic β1 stimulation: cAMP → PKA phosphorylates the L-type channel (more trigger Ca2+) and phospholamban (SERCA unbraked) — a larger, faster Ca2+ transient: stronger and quicker beats"
];
const T0 = "M400 180 L440 180 L450 176";
const traces = [
  T0,
  T0 + " L462 112",
  T0 + " L462 112 L472 104",
  T0 + " L462 112 L472 104 Q500 110 530 150",
  T0 + " L462 112 L472 104 Q500 110 530 150 Q560 176 600 180 L640 180",
  "M400 180 L440 180 L448 172 L458 92 L464 86 Q484 96 504 150 Q522 176 548 180 L640 180"
];
const BASE = traces[4];
const cytCount = [0, 4, 9, 4, 0, 9];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('trigger').classList.toggle('on', step <= 2 || step === 5);
  document.getElementById('ryr').classList.toggle('pulse', step === 1);
  document.getElementById('release').classList.toggle('on', step === 1 || step === 2 || step === 5);
  document.querySelectorAll('.cyt').forEach((d, i) => { d.style.opacity = i < cytCount[step] ? 1 : 0; });
  document.getElementById('contract').classList.toggle('on', step === 2 || step === 5);
  document.querySelectorAll('.tnc').forEach(c => c.setAttribute('class', (step === 2 || step === 5) ? 'tnc c-red' : 'tnc c-purple'));
  document.getElementById('serca').classList.toggle('on', step === 3 || step === 5);
  document.getElementById('ncx').classList.toggle('on', step === 4 || step === 5);
  document.getElementById('beta').classList.toggle('on', step === 5);
  document.getElementById('caTrace').setAttribute('d', traces[step]);
  document.getElementById('baseTrace').setAttribute('d', step === 5 ? BASE : '');
  document.getElementById('baseKey').classList.toggle('on', step === 5);
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# MUSCLE_CONTRACTION_TECHNICAL  (source: muscle_technical.html)
# ---------------------------------------------------------------------------
MUSCLE_CONTRACTION_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of skeletal muscle excitation-contraction coupling and the full cross-bridge cycle: DHPR directly opens RyR, and myosin cycles through weak binding, power stroke, rigor, and ATP-driven detachment.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #myosinHead { transition: transform 1s ease; }
  #myosinHead { transform-origin: 340px 144px; }
  .stroke #myosinHead { transform: rotate(-25deg); }
  .detached #myosinHead { transform: rotate(-25deg) translateY(-16px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Skeletal muscle EC coupling and cross-bridge cycle, technical view</title>
<desc>An action potential travels down the T-tubule, where the voltage sensor DHPR directly mechanically opens the ryanodine receptor on the adjacent sarcoplasmic reticulum, without needing a calcium trigger. Calcium floods out, binds troponin C, and tropomyosin shifts. Myosin then cycles through weak binding, a phosphate-release power stroke, a rigor state after ADP release, and ATP-driven detachment that resets the head for another cycle.</desc>

<rect x="30" y="60" width="30" height="220" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="45" y="50" text-anchor="middle">T-tubule</text>
<circle id="dhpr" cx="60" cy="150" r="8" class="c-amber"/>
<text class="ts" x="60" y="175" text-anchor="middle">DHPR</text>

<ellipse cx="140" cy="150" rx="60" ry="90" fill="none" stroke="#B91C1C" stroke-width="1.5" stroke-dasharray="3 3"/>
<text class="ts" x="140" y="55" text-anchor="middle">Sarcoplasmic reticulum</text>
<circle id="ryr" cx="90" cy="150" r="7" class="c-red"/>
<text class="ts" x="90" y="175" text-anchor="middle" id="ryrLabel">RyR</text>

<g id="calcium" class="stg">
<circle cx="214" cy="128" r="4" fill="#B91C1C"/>
<circle cx="228" cy="142" r="4" fill="#B91C1C"/>
<circle cx="216" cy="158" r="4" fill="#B91C1C"/>
<text class="ts" x="246" y="104" text-anchor="middle">Ca2+ floods out</text>
</g>

<g id="troponin" class="stg">
<circle cx="260" cy="160" r="8" class="c-purple"/>
<text class="ts" x="260" y="185" text-anchor="middle">Troponin C binds Ca2+</text>
</g>

<line x1="220" y1="200" x2="480" y2="200" stroke="#378ADD" stroke-width="6" stroke-linecap="round"/>
<text class="ts" x="480" y="220" text-anchor="middle">Actin</text>
<rect x="300" y="120" width="140" height="24" fill="#7F77DD"/>
<text class="ts" x="370" y="112" text-anchor="middle">Myosin</text>

<g id="myosinHead" class="stg">
<line x1="340" y1="144" x2="340" y2="196" stroke="#7F77DD" stroke-width="4"/>
<circle cx="340" cy="196" r="6" fill="#7F77DD"/>
</g>

<g id="stateLabel" class="stg">
<text class="th" x="480" y="260" text-anchor="middle" id="crossBridgeState">Weak binding</text>
</g>

<g id="atpNote" class="stg">
<text class="ts" x="480" y="280" text-anchor="middle">ATP binds — cross-bridge detaches, myosin re-cocks</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 5</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 5 — action potential travels down the T-tubule, DHPR senses voltage",
  "Step 1 of 5 — DHPR directly (mechanically) opens RyR — no calcium trigger needed, unlike cardiac muscle",
  "Step 2 of 5 — Ca2+ floods out, binds troponin C, tropomyosin shifts to expose binding sites",
  "Step 3 of 5 — myosin weakly binds actin, then phosphate release drives the power stroke",
  "Step 4 of 5 — ADP released — rigor state, myosin locked tightly to actin",
  "Step 5 of 5 — ATP binds the myosin head, the cross-bridge detaches and re-cocks for another cycle"
];
const states = ["", "", "", "Weak binding → power stroke", "Rigor (ADP released)", "ATP-bound, detached"];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('dhpr').classList.toggle('pulse', step === 0);
  document.getElementById('ryr').classList.toggle('on', step >= 1);
  document.getElementById('ryr').classList.toggle('pulse', step === 1);
  document.getElementById('calcium').classList.toggle('on', step >= 2);
  document.getElementById('troponin').classList.toggle('on', step >= 2);
  document.getElementById('myosinHead').classList.toggle('on', step >= 3);
  document.querySelector('svg').classList.toggle('stroke', step === 3);
  document.querySelector('svg').classList.toggle('detached', step === 5);
  document.getElementById('stateLabel').classList.toggle('on', step >= 3);
  document.getElementById('crossBridgeState').textContent = states[step] || '';
  document.getElementById('atpNote').classList.toggle('on', step >= 5);
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# LABOR_POSITIVE_FEEDBACK_GENERAL  (source: labor_feedback.html)
# ---------------------------------------------------------------------------
LABOR_POSITIVE_FEEDBACK_GENERAL = '''
<h2 class="sr-only">Interactive diagram of the Ferguson reflex: labor as a positive feedback loop where cervical stretch triggers oxytocin release, which causes contractions that increase cervical stretch, escalating until birth.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.1s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #loopArrow { transition: stroke-width 0.5s ease, opacity 0.5s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Labor as a positive feedback loop — the Ferguson reflex</title>
<desc>Pressure from the fetal head stretches the cervix, signaling the hypothalamus to trigger oxytocin release from the posterior pituitary. Oxytocin causes uterine contractions, which push the fetus further against the cervix, increasing the stretch signal and triggering even more oxytocin. Unlike most physiological control loops, this one amplifies rather than corrects, intensifying until birth occurs and the loop is broken.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<circle cx="340" cy="170" r="130" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>

<g id="cervix">
<ellipse cx="340" cy="280" rx="50" ry="24" fill="none" stroke="#B91C1C" stroke-width="2"/>
<text class="ts" x="340" y="315" text-anchor="middle">Cervix stretch receptors</text>
</g>

<g id="loop1" class="stg">
<path d="M370 260 Q460 220 480 150" stroke="#378ADD" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="500" y="206">Signal to hypothalamus</text>
</g>

<ellipse cx="500" cy="120" rx="55" ry="35" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="500" y="116" text-anchor="middle">Hypothalamus /</text>
<text class="ts" x="500" y="132" text-anchor="middle">pituitary</text>

<g id="oxytocin" class="stg">
<circle id="oxyDot" cx="460" cy="86" r="7" class="c-purple pulse"/>
<text class="ts" x="452" y="74" text-anchor="end">Oxytocin released</text>
</g>

<g id="loop2" class="stg">
<path d="M456 144 Q400 130 372 144" stroke="#7F77DD" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
</g>

<g id="uterus" class="stg">
<ellipse cx="340" cy="190" rx="70" ry="50" fill="none" stroke="#D85A30" stroke-width="2" id="uterusOutline"/>
<text class="ts" x="340" y="190" text-anchor="middle" dominant-baseline="central" id="uterusLabel">Uterine contraction</text>
</g>

<g id="loop3" class="stg">
<path id="loopArrow" d="M280 240 Q260 260 300 275" stroke="#B91C1C" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="230" y="255" text-anchor="middle">More stretch →</text>
</g>

<g id="birth" class="stg">
<text class="th" x="340" y="40" text-anchor="middle">Birth occurs — loop breaks</text>
</g>

<text class="ts" x="340" y="330" text-anchor="middle" id="cycleLabel"></text>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — fetal head presses against the cervix, some baseline stretch",
  "Step 1 of 4 — stretch receptors signal the hypothalamus, triggering oxytocin release",
  "Step 2 of 4 — oxytocin causes uterine contractions",
  "Step 3 of 4 — contractions push the fetus further against the cervix — MORE stretch, MORE oxytocin (this is positive feedback: it amplifies rather than corrects)",
  "Step 4 of 4 — the cycle intensifies over successive contractions until birth occurs, finally breaking the loop"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('loop1').classList.toggle('on', step >= 1);
  document.getElementById('oxytocin').classList.toggle('on', step >= 1);
  document.getElementById('loop2').classList.toggle('on', step >= 2);
  document.getElementById('uterus').classList.toggle('on', step >= 2);
  document.getElementById('loop3').classList.toggle('on', step >= 3);
  document.getElementById('uterusOutline').setAttribute('stroke-width', step === 3 ? '4' : '2');
  document.getElementById('birth').classList.toggle('on', step >= 4);
  document.getElementById('cycleLabel').textContent = step === 3 ? 'Loop repeats, escalating each time' : '';
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# LABOR_TECHNICAL  (source: labor_technical.html)
# ---------------------------------------------------------------------------
LABOR_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of labor initiation: progesterone withdrawal and rising CRH shift the uterus out of quiescence, prostaglandins ripen the cervix and upregulate oxytocin receptors, then the sensitized Ferguson reflex positive feedback loop drives labor to completion.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.1s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #progBar { transition: width 1s ease; }
  #receptorDots circle { transition: opacity 0.6s ease; }
  .hide { display: none; }
  .fil { transition: transform 1s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<div class="rowbtns">
  <button id="btnOnset" onclick="setMode('onset')">Labor onset</button>
  <button id="btnCell" onclick="setMode('cell')">Myometrial cell</button>
</div>

<svg width="100%" viewBox="0 0 680 334" role="img">
<title>Labor initiation and the primed Ferguson reflex, technical view</title>
<desc>Late in pregnancy progesterone maintains uterine quiescence. Progesterone withdrawal alongside rising placental CRH and cortisol shifts the balance toward contraction readiness. Prostaglandins ripen the cervix and upregulate oxytocin receptors on the myometrium, sensitizing the tissue. Only then does the Ferguson reflex positive feedback loop — cervical stretch triggering oxytocin, which causes contractions that increase stretch — drive labor to completion.</desc>

<g id="onsetView">
<text class="ts" x="60" y="40">Progesterone (uterine quiescence)</text>
<rect x="60" y="50" width="200" height="16" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<rect id="progBar" x="60" y="50" width="200" height="16" fill="#7F77DD"/>

<g id="crh" class="stg">
<text class="ts" x="400" y="40">CRH / cortisol / estrogen rising</text>
<circle class="pulse" cx="400" cy="60" r="7" fill="#EF9F27"/>
</g>

<ellipse cx="340" cy="180" rx="120" ry="90" fill="none" stroke="#D85A30" stroke-width="2" id="uterusOutline"/>
<text class="ts" x="340" y="90" text-anchor="middle">Myometrium</text>

<g id="prostaglandin" class="stg">
<circle cx="292" cy="274" r="5" fill="#B91C1C"/>
<circle cx="388" cy="274" r="5" fill="#B91C1C"/>
<text class="ts" x="286" y="300" text-anchor="end">Prostaglandins ripen cervix</text>
</g>

<g id="receptorDots" class="stg">
<circle cx="300" cy="196" r="4" class="c-teal"/>
<circle cx="320" cy="206" r="4" class="c-teal"/>
<circle cx="340" cy="198" r="4" class="c-teal"/>
<circle cx="360" cy="206" r="4" class="c-teal"/>
<circle cx="380" cy="196" r="4" class="c-teal"/>
<text class="ts" x="340" y="230" text-anchor="middle">Oxytocin receptors upregulated</text>
</g>

<ellipse cx="340" cy="270" rx="40" ry="18" fill="none" stroke="#B91C1C" stroke-width="2"/>
<text class="ts" x="340" y="300" text-anchor="middle">Cervix</text>

<g id="loop" class="stg">
<path d="M370 260 Q450 200 400 130" stroke="#378ADD" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
<text class="th" x="472" y="190">Ferguson reflex loop</text>
<text class="th" x="472" y="208">— now sensitized</text>
</g>

<g id="birth" class="stg">
<text class="th" x="640" y="324" text-anchor="end">Labor completes — loop breaks at birth</text>
</g>

<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>
</g>

<!-- ===== Myometrial cell view: oxytocin -> Gq -> Ca2+ -> MLCK -> contraction ===== -->
<g id="cellView" class="hide">
<rect x="40" y="50" width="480" height="250" rx="40" fill="var(--surface-1)" stroke="var(--t)" stroke-width="1"/>
<text class="th" x="40" y="324">Myometrial smooth muscle cell</text>
<rect x="532" y="80" width="118" height="180" rx="30" fill="none" stroke="var(--t)" stroke-width="1" stroke-dasharray="4 3"/>
<text class="ts" x="591" y="104" text-anchor="middle">neighbouring cell</text>

<rect x="152" y="38" width="16" height="26" rx="4" class="c-purple"/>
<text class="ts" x="176" y="66">oxytocin receptor (Gq)</text>
<g id="c0" class="stg"><circle class="pulse" cx="160" cy="24" r="7" fill="#7F77DD"/><text class="ts" x="174" y="26">oxytocin</text></g>

<ellipse cx="160" cy="172" rx="70" ry="30" fill="none" stroke="#B91C1C" stroke-width="1.5" stroke-dasharray="3 3"/>
<text class="ts" x="130" y="176" text-anchor="middle">SR</text>
<rect x="34" y="236" width="12" height="26" rx="3" fill="#D85A30"/>
<text class="ts" x="56" y="280">L-type Ca2+ channel</text>
<g id="c1" class="stg">
<path d="M160 74 L160 138" stroke="#7F77DD" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="168" y="102">Gq → PLCβ → IP3 + DAG</text>
<circle cx="214" cy="140" r="4" fill="#B91C1C"/><circle cx="236" cy="152" r="4" fill="#B91C1C"/><circle cx="228" cy="128" r="4" fill="#B91C1C"/>
<circle cx="62" cy="244" r="4" fill="#B91C1C"/><circle cx="76" cy="256" r="4" fill="#B91C1C"/>
<text class="ts" x="246" y="140">Ca2+</text>
</g>

<line x1="270" y1="214" x2="362" y2="214" class="fil" id="aL1" stroke="#378ADD" stroke-width="4"/>
<line x1="270" y1="252" x2="362" y2="252" class="fil" id="aL2" stroke="#378ADD" stroke-width="4"/>
<line x1="418" y1="214" x2="510" y2="214" class="fil" id="aR1" stroke="#378ADD" stroke-width="4"/>
<line x1="418" y1="252" x2="510" y2="252" class="fil" id="aR2" stroke="#378ADD" stroke-width="4"/>
<rect x="330" y="226" width="120" height="14" rx="3" fill="#7F77DD"/>
<text class="ts" x="390" y="278" text-anchor="middle">actin · myosin (no troponin)</text>
<g id="c2" class="stg">
<text class="ts" x="270" y="176">Ca2+–calmodulin → MLCK</text>
<path d="M330 182 L346 220" stroke="#EF9F27" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
<circle cx="352" cy="226" r="7" class="c-coral"/><text x="352" y="229" text-anchor="middle" style="font-size:8px;font-weight:600;fill:#7F1D1D">P</text>
<text class="ts" x="366" y="192">myosin light chain</text>
<text class="ts" x="366" y="206">phosphorylated</text>
</g>

<rect x="512" y="150" width="28" height="9" rx="2" fill="#1D9E75"/>
<rect x="512" y="172" width="28" height="9" rx="2" fill="#1D9E75"/>
<text class="ts" x="591" y="280" text-anchor="middle" style="font-size:10px">connexin-43 gap junctions</text>
<g id="c3" class="stg">
<path d="M500 166 L572 166" stroke="#D85A30" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="591" y="196" text-anchor="middle">excitation</text>
<text class="ts" x="591" y="210" text-anchor="middle">spreads</text>
</g>

<g id="c4" class="stg">
<text class="ts" x="176" y="46" style="fill:#B91C1C">✕ atosiban (OTR antagonist)</text>
<text class="ts" x="54" y="230" style="fill:#B91C1C">✕ nifedipine</text>
<text class="ts" x="650" y="36" text-anchor="end">induce: oxytocin, prostaglandins</text>
<text class="ts" x="650" y="52" text-anchor="end">delay: atosiban, nifedipine</text>
</g>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
let mode = 'onset';
const labelsCell = [
  "Step 0 of 4 — oxytocin binds its Gq-coupled receptor (OTR), which rises sharply near term; PGF2α acts through a similar Gq receptor",
  "Step 1 of 4 — Gq activates PLCβ → IP3 (+ DAG); IP3 releases Ca2+ from the SR, and depolarization lets more Ca2+ in through L-type channels",
  "Step 2 of 4 — Ca2+ binds calmodulin; Ca2+–calmodulin activates myosin light-chain kinase (MLCK), which phosphorylates the myosin regulatory light chain (smooth muscle has no troponin)",
  "Step 3 of 4 — phosphorylated myosin cycles on actin and the cell shortens; connexin-43 gap junctions, greatly increased at term, spread excitation so the uterus contracts as one",
  "Step 4 of 4 — drug targets: oxytocin and prostaglandin analogues (misoprostol, dinoprostone) induce labor; atosiban (OTR antagonist) and nifedipine (L-type blocker) are tocolytics that delay preterm labor"
];
const labels = [
  "Step 0 of 4 — late pregnancy: high progesterone keeps the uterus quiescent",
  "Step 1 of 4 — progesterone withdrawal, rising CRH/cortisol/estrogen shift the balance toward contraction readiness",
  "Step 2 of 4 — prostaglandins ripen the cervix and upregulate oxytocin receptors on the myometrium",
  "Step 3 of 4 — the sensitized tissue now responds strongly — the Ferguson reflex positive feedback loop takes over",
  "Step 4 of 4 — contractions intensify, cervix fully dilates, labor completes and the loop breaks at birth"
];
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnOnset').classList.toggle('active', m === 'onset');
  document.getElementById('btnCell').classList.toggle('active', m === 'cell');
  document.getElementById('onsetView').classList.toggle('hide', m !== 'onset');
  document.getElementById('cellView').classList.toggle('hide', m !== 'cell');
  render();
}
function renderCell() {
  document.getElementById('stepLabel').textContent = labelsCell[step];
  for (let i = 0; i <= 4; i++) document.getElementById('c' + i).classList.toggle('on', i === 4 ? step === 4 : step >= i);
  const pull = step >= 3 ? 18 : 0;   // filaments slide toward the myosin as the cell contracts
  ['aL1', 'aL2'].forEach(id => document.getElementById(id).style.transform = `translateX(${pull}px)`);
  ['aR1', 'aR2'].forEach(id => document.getElementById(id).style.transform = `translateX(${-pull}px)`);
}
function render() {
  if (mode === 'cell') { renderCell(); return; }
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('progBar').setAttribute('width', step === 0 ? '200' : step === 1 ? '80' : '20');
  document.getElementById('crh').classList.toggle('on', step >= 1);
  document.getElementById('prostaglandin').classList.toggle('on', step >= 2);
  document.getElementById('receptorDots').classList.toggle('on', step >= 2);
  document.getElementById('loop').classList.toggle('on', step >= 3);
  document.getElementById('uterusOutline').setAttribute('stroke-width', step >= 3 ? '4' : '2');
  document.getElementById('birth').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('onset');
</script>
'''


# ---------------------------------------------------------------------------
# FERTILIZATION_TECHNICAL  (source: fertilization_technical.html)
# ---------------------------------------------------------------------------
FERTILIZATION_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of fertilization: the egg arrested at meiosis II, the fast electrical block via depolarization, the calcium wave triggering the slow cortical block, egg activation completing meiosis, and pronuclear fusion.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #calciumWave { transition: r 1.2s ease, opacity 0.6s ease; }
  #calciumWave.stg { opacity: 0; }
  #calciumWave.stg.on { opacity: 1; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Fertilization, technical view</title>
<desc>The egg is arrested at metaphase II of meiosis. Sperm-egg recognition and membrane fusion trigger a fast electrical block via membrane depolarization, then a calcium wave sweeps across the egg by calcium-induced calcium release, triggering the slow cortical granule block that hardens the zona pellucida. The same calcium wave activates the egg, allowing it to complete meiosis II and extrude a second polar body, after which the male and female pronuclei form and fuse into a diploid zygote.</desc>

<defs><clipPath id="eggClip"><circle cx="380" cy="160" r="100"/></clipPath></defs>
<circle cx="380" cy="160" r="100" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<g id="meiosisArrest">
<path d="M370 130 L390 130 M380 120 L380 140" stroke="#7F77DD" stroke-width="2"/>
<text class="ts" x="380" y="105" text-anchor="middle" id="arrestLabel">Egg arrested at metaphase II</text>
</g>

<g id="spermGroup" class="stg">
<circle cx="266" cy="160" r="10" fill="#378ADD"/>
<path d="M216 160 L256 160" stroke="var(--t)" stroke-width="2" stroke-linecap="round"/>
<text class="ts" x="258" y="138" text-anchor="end">Sperm — ZP3 binding, acrosome reaction</text>
</g>

<g id="fastBlock" class="stg">
<circle cx="380" cy="160" r="105" fill="none" stroke="#EF9F27" stroke-width="3"/>
<text class="ts" x="380" y="276" text-anchor="middle">Fast block — membrane depolarizes (Na+ influx)</text>
</g>

<circle id="calciumWave" cx="280" cy="160" r="0" fill="#B91C1C" fill-opacity="0.12" stroke="#B91C1C" stroke-width="2" class="stg" clip-path="url(#eggClip)"/>
<g id="calciumLabel" class="stg">
<text class="ts" x="380" y="240" text-anchor="middle">Ca2+ wave — calcium-induced calcium release</text>
</g>

<g id="cortical" class="stg">
<circle cx="380" cy="160" r="100" fill="none" stroke="#B91C1C" stroke-width="4"/>
<text class="ts" x="380" y="298" text-anchor="middle">Slow block — cortical granules harden the zona</text>
</g>

<g id="polarBody" class="stg">
<circle cx="440" cy="90" r="8" fill="#7F77DD"/>
<text class="ts" x="440" y="72" text-anchor="middle">2nd polar body extruded</text>
</g>

<g id="pronuclei" class="stg">
<circle cx="360" cy="160" r="14" fill="none" stroke="#378ADD" stroke-width="1.5"/>
<circle cx="390" cy="160" r="14" fill="none" stroke="#D85A30" stroke-width="1.5"/>
</g>
<g id="zygote" class="stg">
<circle cx="375" cy="160" r="16" class="c-green"/>
<text class="ts" x="375" y="160" text-anchor="middle" dominant-baseline="central">Zygote</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — egg arrested at metaphase II; sperm undergoes species-specific ZP3 binding and the acrosome reaction",
  "Step 1 of 4 — membrane fusion triggers the fast block: immediate depolarization prevents polyspermy within seconds",
  "Step 2 of 4 — a Ca2+ wave sweeps across the egg by calcium-induced calcium release, triggering the slow cortical block that permanently hardens the zona",
  "Step 3 of 4 — the same Ca2+ wave activates the egg — meiosis II resumes, a second polar body is extruded",
  "Step 4 of 4 — male and female pronuclei form and fuse into a diploid zygote"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('spermGroup').classList.toggle('on', step === 0);
  document.getElementById('fastBlock').classList.toggle('on', step >= 1 && step < 2);
  const wave = document.getElementById('calciumWave');
  wave.setAttribute('r', step === 2 ? '200' : '0'); wave.style.r = step === 2 ? '200px' : '0px';   // sweeps from entry point across the whole egg
  wave.classList.toggle('on', step === 2);   // the opacity attribute was overridden by .stg, so the wave never showed
  document.getElementById('calciumLabel').classList.toggle('on', step >= 2 && step < 3);
  document.getElementById('cortical').classList.toggle('on', step >= 2);   // slow block is triggered by the step-2 Ca2+ wave
  document.getElementById('polarBody').classList.toggle('on', step >= 3 && step < 4);
  document.getElementById('meiosisArrest').style.opacity = step >= 3 ? '0' : '1';
  document.getElementById('pronuclei').classList.toggle('on', step === 3);
  document.getElementById('zygote').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# GASTRULATION_TECHNICAL  (source: gastrulation_technical.html)
# ---------------------------------------------------------------------------
GASTRULATION_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of gastrulation: the Spemann organizer secretes BMP antagonists to pattern the dorsal-ventral axis, cells move by involution and convergent extension, and a Nodal signaling gradient specifies the three germ layers.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Gastrulation, technical view</title>
<desc>The Spemann organizer at the dorsal blastopore lip secretes BMP antagonists, creating a gradient that patterns the dorsal-ventral axis of the ectoderm. Cells move by involution, rolling inward around the blastopore lip, and by convergent extension, intercalating to narrow and elongate the embryo. A separate Nodal signaling gradient specifies the three germ layers: the highest Nodal levels produce endoderm, lower levels produce mesoderm, and the absence of Nodal leaves ectoderm.</desc>

<circle cx="340" cy="160" r="120" fill="none" stroke="var(--t)" stroke-width="1.5"/>

<g id="organizer">
<circle cx="340" cy="280" r="14" class="c-amber"/>
<text class="ts" x="340" y="305" text-anchor="middle">Spemann organizer</text>
</g>

<g id="bmpGradient" class="stg">
<defs><linearGradient id="bmpFade" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#7F77DD" stop-opacity="0.85"/><stop offset="1" stop-color="#7F77DD" stop-opacity="0.05"/></linearGradient></defs>
<polygon points="326,266 354,266 342,86 338,86" fill="url(#bmpFade)"/>
<text class="ts" x="362" y="296" text-anchor="start">← BMP antagonists (Noggin, Chordin)</text>
</g>

<g id="dvPattern" class="stg">
<text class="ts" x="350" y="208" text-anchor="start">Low BMP → neural</text>
<text class="ts" x="340" y="70" text-anchor="middle">High BMP → epidermis (far side)</text>
</g>

<g id="involution" class="stg">
<path d="M300 270 Q318 240 300 212" stroke="#B91C1C" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="294" y="206" text-anchor="end">Involution</text>
</g>

<g id="convExt" class="stg">
<path d="M260 160 L420 160" stroke="#1D9E75" stroke-width="1.5" marker-end="url(#arrow)" marker-start="url(#arrow)"/>
<text class="ts" x="340" y="145" text-anchor="middle">Convergent extension</text>
</g>

<g id="nodalGradient" class="stg">
<circle cx="340" cy="180" r="30" fill="#E24B4A" opacity="0.5"/>
<circle cx="340" cy="180" r="55" fill="#E24B4A" opacity="0.25"/>
<text class="ts" x="340" y="185" text-anchor="middle">Highest Nodal — endoderm</text>
<text class="ts" x="340" y="248" text-anchor="middle">Lower Nodal — mesoderm</text>
</g>

<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — the Spemann organizer sits at the dorsal blastopore lip",
  "Step 1 of 4 — it secretes BMP antagonists (Noggin, Chordin), forming a gradient",
  "Step 2 of 4 — the gradient patterns the dorsal-ventral axis: low BMP specifies neural tissue, high BMP specifies epidermis",
  "Step 3 of 4 — cells move by involution (rolling inward) and convergent extension (narrowing and elongating the embryo)",
  "Step 4 of 4 — a separate Nodal gradient specifies the germ layers: highest Nodal → endoderm, lower → mesoderm, none → ectoderm"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('bmpGradient').classList.toggle('on', step >= 1 && step < 4);
  document.getElementById('dvPattern').classList.toggle('on', step >= 2 && step < 4);
  document.getElementById('involution').classList.toggle('on', step === 3);
  document.getElementById('convExt').classList.toggle('on', step === 3);
  document.getElementById('nodalGradient').classList.toggle('on', step >= 4);
  document.getElementById('bmpGradient').style.opacity = step >= 4 ? '0.12' : (step >= 1 ? '1' : '0.12');
  document.getElementById('dvPattern').style.opacity = step >= 4 ? '0.12' : (step >= 2 ? '1' : '0.12');
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# CYTOTOXIC_T_CELL_GENERAL  (source: cytotoxic_t_cell.html)
# ---------------------------------------------------------------------------
CYTOTOXIC_T_CELL_GENERAL = '''
<h2 class="sr-only">Interactive diagram of cytotoxic T cell killing: a CD8 T cell recognizes viral peptide on MHC-I, releases perforin to form pores, and granzymes trigger apoptosis in the infected target cell.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #tcellGroup { transition: transform 1s ease; }
  .docked #tcellGroup { transform: translateX(-40px); }
  #targetCell { transition: opacity 0.8s ease, stroke 0.6s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Cytotoxic T cell killing</title>
<desc>An infected cell presents a viral peptide on MHC class one. A CD8 cytotoxic T cell's receptor recognizes this complex, releases perforin to punch pores in the target cell's membrane, and granzymes enter through the pores to trigger apoptosis, destroying the infected cell before the virus can spread.</desc>

<circle cx="180" cy="150" r="70" fill="none" id="targetCell" stroke="var(--t)" stroke-width="1.5"/>
<text class="ts" x="180" y="235" text-anchor="middle">Infected cell</text>
<rect x="165" y="90" width="30" height="12" rx="3" fill="#EF9F27"/>
<text class="ts" x="180" y="75" text-anchor="middle">Viral peptide on MHC-I</text>

<g id="tcellGroup">
<circle cx="440" cy="150" r="55" class="c-red"/>
<text class="th" x="440" y="150" text-anchor="middle" dominant-baseline="central">CD8 T cell</text>
</g>

<g id="recognition" class="stg">
<line x1="385" y1="150" x2="255" y2="120" stroke="#7F77DD" stroke-width="1.5" marker-end="url(#arrow)"/>
<text class="ts" x="320" y="105" text-anchor="middle">TCR recognizes peptide-MHC-I</text>
</g>

<g id="perforin" class="stg">
<circle cx="230" cy="120" r="3" fill="#B91C1C"/>
<circle cx="230" cy="150" r="3" fill="#B91C1C"/>
<circle cx="230" cy="180" r="3" fill="#B91C1C"/>
<text class="ts" x="230" y="200" text-anchor="middle">Perforin punches pores</text>
</g>

<g id="granzyme" class="stg">
<circle cx="180" cy="150" r="5" class="c-amber"/>
<text class="ts" x="180" y="170" text-anchor="middle">Granzymes enter</text>
</g>

<g id="apoptosis" class="stg">
<path d="M155 130 L170 145 M170 130 L155 145" stroke="#E24B4A" stroke-width="2" stroke-linecap="round"/>
<path d="M190 155 L205 170 M205 155 L190 170" stroke="#E24B4A" stroke-width="2" stroke-linecap="round"/>
<text class="th" x="180" y="260" text-anchor="middle">Apoptosis — infected cell destroyed</text>
</g>

<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — infected cell presents viral peptide on MHC-I",
  "Step 1 of 4 — CD8 T cell's receptor recognizes the peptide-MHC-I complex",
  "Step 2 of 4 — the T cell releases perforin, punching pores in the target's membrane",
  "Step 3 of 4 — granzymes enter through the pores",
  "Step 4 of 4 — granzymes trigger apoptosis — the infected cell is destroyed before the virus can spread"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('recognition').classList.toggle('on', step >= 1);
  document.querySelector('svg').classList.toggle('docked', step >= 1);
  document.getElementById('perforin').classList.toggle('on', step >= 2);
  document.getElementById('granzyme').classList.toggle('on', step >= 3);
  document.getElementById('apoptosis').classList.toggle('on', step >= 4);
  document.getElementById('targetCell').style.opacity = step >= 4 ? '0.3' : '1';
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# COMPLEMENT_SYSTEM_GENERAL  (source: complement.html)
# ---------------------------------------------------------------------------
COMPLEMENT_SYSTEM_GENERAL = '''
<h2 class="sr-only">Interactive diagram of the complement system: a cascade of proteins opsonizes a pathogen and assembles a membrane attack complex that punches a lethal pore in its membrane.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #pathogenCell { transition: opacity 0.8s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Complement system, general view</title>
<desc>Complement proteins activate in a cascade on a pathogen's surface. Early components opsonize the pathogen, tagging it for phagocytosis. The cascade continues through later components, which assemble into a membrane attack complex that inserts into the pathogen's membrane, forming a pore that causes it to lyse.</desc>

<circle id="pathogenCell" cx="200" cy="150" r="70" class="c-coral"/>
<text class="th" x="200" y="150" text-anchor="middle" dominant-baseline="central">Pathogen</text>

<g id="cascade1" class="stg">
<circle cx="150.5" cy="100.5" r="8" class="c-purple"/>
<text class="ts" x="140" y="90" text-anchor="end">C1, C4, C2 activate</text>
</g>

<g id="opsonize" class="stg">
<circle cx="150" cy="200" r="7" class="c-amber"/>
<circle cx="250" cy="200" r="7" class="c-amber"/>
<text class="ts" x="200" y="225" text-anchor="middle">C3b opsonizes — tags for phagocytosis</text>
</g>

<g id="cascadeLate" class="stg">
<circle cx="292" cy="128" r="5" fill="#B91C1C"/>
<circle cx="302" cy="146" r="5" fill="#B91C1C"/>
<circle cx="300" cy="166" r="5" fill="#B91C1C"/>
<circle cx="288" cy="180" r="5" fill="#B91C1C"/>
<text class="ts" x="312" y="190" text-anchor="start">C5-C9 assemble at the membrane</text>
</g>

<g id="mac" class="stg">
<rect x="261" y="134" width="6" height="32" rx="2" fill="#B91C1C"/>
<rect x="275" y="134" width="6" height="32" rx="2" fill="#B91C1C"/>
<text class="ts" x="280" y="105" text-anchor="middle">Membrane attack complex</text>
</g>

<g id="lysis" class="stg">
<path d="M260 150 L340 150" stroke="#B91C1C" stroke-width="1.5" marker-end="url(#arrow)"/>
<text class="th" x="200" y="270" text-anchor="middle">Pore forms — pathogen lyses</text>
</g>

<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — pathogen present, complement not yet activated",
  "Step 1 of 4 — early complement proteins (C1, C4, C2) activate on the surface",
  "Step 2 of 4 — C3b opsonizes the pathogen, tagging it for phagocytosis",
  "Step 3 of 4 — the cascade continues, C5 through C9 begin assembling",
  "Step 4 of 4 — the membrane attack complex inserts into the membrane, forming a pore that lyses the pathogen"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('cascade1').classList.toggle('on', step >= 1);
  document.getElementById('opsonize').classList.toggle('on', step >= 2);
  document.getElementById('cascadeLate').classList.toggle('on', step === 3);
  document.getElementById('mac').classList.toggle('on', step >= 4);
  document.getElementById('lysis').classList.toggle('on', step >= 4);
  document.getElementById('pathogenCell').style.opacity = step >= 4 ? '0.25' : '1';
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# COMPLEMENT_SYSTEM_TECHNICAL  (source: complement_technical.html)
# ---------------------------------------------------------------------------
COMPLEMENT_SYSTEM_TECHNICAL = '''
<h2 class="sr-only">Interactive diagram of the three complement pathways — classical, lectin, and alternative — converging on a shared C3 and C5 convertase cascade that assembles the membrane attack complex.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #pathogenCell { transition: opacity 0.8s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnClassical" onclick="setMode('classical')">Classical pathway</button>
  <button id="btnLectin" onclick="setMode('lectin')">Lectin pathway</button>
  <button id="btnAlternative" onclick="setMode('alternative')">Alternative pathway</button>
</div>

<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Complement system, technical view</title>
<desc>The three complement pathways each generate a C3 convertase through different initiating molecules: the classical pathway via antibody-bound C1q, the lectin pathway via mannose-binding lectin and MASP-2, and the alternative pathway via spontaneous C3 hydrolysis stabilized by properdin. All three converge on cleaving C3 into C3b, an opsonin that tags the pathogen, and C3a, an anaphylatoxin. The C3 convertase combines with C3b to form a C5 convertase, which cleaves C5 into C5b, initiating assembly of the C5b-C9 membrane attack complex that lyses the pathogen, and C5a, a potent anaphylatoxin.</desc>

<circle id="pathogenCell" cx="250" cy="160" r="65" class="c-coral"/>
<text class="th" x="250" y="160" text-anchor="middle" dominant-baseline="central">Pathogen</text>

<g id="initiation" class="stg">
<circle cx="193.7" cy="127.5" r="8" class="c-purple"/>
<text class="ts" x="182" y="118" text-anchor="end" id="initLabel"></text>
</g>

<g id="convertase3" class="stg">
<circle cx="186" cy="171.3" r="9" class="c-teal"/>
<text class="ts" x="173" y="175" text-anchor="end" id="convertase3Label"></text>
</g>

<g id="c3split" class="stg">
<circle cx="205" cy="215" r="7" class="c-amber"/>
<text class="ts" x="205" y="238" text-anchor="middle">C3b opsonizes</text>
<circle cx="70" cy="240" r="6" class="c-red"/>
<text class="ts" x="70" y="262" text-anchor="middle">C3a (anaphylatoxin)</text>
</g>

<g id="convertase5" class="stg">
<circle cx="299.8" cy="118.2" r="9" class="c-teal"/>
<text class="ts" x="312" y="108" text-anchor="start" id="convertase5Label"></text>
</g>

<g id="mac" class="stg">
<rect x="306" y="144" width="6" height="32" rx="2" fill="#B91C1C"/>
<rect x="320" y="144" width="6" height="32" rx="2" fill="#B91C1C"/>
<text class="ts" x="334" y="192" text-anchor="start">C5b-9 (MAC) pore</text>
</g>

<g id="c5split" class="stg">
<circle cx="420" cy="250" r="6" class="c-red"/>
<text class="ts" x="420" y="270" text-anchor="middle">C5a (anaphylatoxin)</text>
</g>

<g id="lysis" class="stg">
<path d="M300 160 L390 160" stroke="#B91C1C" stroke-width="1.5" marker-end="url(#arrow)"/>
<text class="th" x="250" y="295" text-anchor="middle">Pore forms — pathogen lyses</text>
</g>

<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
let mode = 'classical';

const MODES = {
  classical: {
    initTag: "IgG/IgM + C1q",
    c3Tag: "C4b2a (C3 convertase)",
    c5Tag: "C4b2a3b (C5 convertase)",
    labels: [
      "Step 0 of 4 — pathogen present; classical pathway not yet triggered",
      "Step 1 of 4 — IgG or IgM antibody binds the pathogen; C1q recognizes the bound Fc region, activating C1r and C1s",
      "Step 2 of 4 — C1s cleaves C4 and C2; C4b2a assembles on the surface as the classical C3 convertase",
      "Step 3 of 4 — C3 convertase cleaves C3 — C3b opsonizes the pathogen, C3a diffuses away as an anaphylatoxin",
      "Step 4 of 4 — C4b2a3b (C5 convertase) cleaves C5 — C5b seeds C5b-C9 (MAC) assembly, forming a lethal pore; C5a is released as a potent anaphylatoxin"
    ]
  },
  lectin: {
    initTag: "MBL + MASP-2",
    c3Tag: "C4b2a (C3 convertase)",
    c5Tag: "C4b2a3b (C5 convertase)",
    labels: [
      "Step 0 of 4 — pathogen present; lectin pathway not yet triggered",
      "Step 1 of 4 — mannose-binding lectin (MBL) binds repeating sugars on the pathogen surface, activating MASP-2 — no antibody needed",
      "Step 2 of 4 — MASP-2 cleaves C4 and C2, just like C1s does; C4b2a assembles as the C3 convertase — identical from here on",
      "Step 3 of 4 — C3 convertase cleaves C3 — C3b opsonizes the pathogen, C3a diffuses away as an anaphylatoxin",
      "Step 4 of 4 — C4b2a3b (C5 convertase) cleaves C5 — C5b seeds C5b-C9 (MAC) assembly, forming a lethal pore; C5a is released as a potent anaphylatoxin"
    ]
  },
  alternative: {
    initTag: "Factor B, D + properdin",
    c3Tag: "C3bBb (C3 convertase)",
    c5Tag: "C3bBb3b (C5 convertase)",
    labels: [
      "Step 0 of 4 — pathogen present; the alternative pathway idles continuously at low level, independent of antibodies",
      "Step 1 of 4 — spontaneous C3(H2O) hydrolysis plus Factor B and D generate trace C3b; on a pathogen surface, properdin stabilizes it against inactivation",
      "Step 2 of 4 — C3bBb assembles as the alternative C3 convertase, rapidly amplifying C3b deposition in a positive feedback loop",
      "Step 3 of 4 — C3 convertase cleaves more C3 — C3b opsonizes the pathogen, C3a diffuses away as an anaphylatoxin",
      "Step 4 of 4 — C3bBb3b (C5 convertase) cleaves C5 — C5b seeds C5b-C9 (MAC) assembly, forming a lethal pore; C5a is released as a potent anaphylatoxin"
    ]
  }
};

function render() {
  const m = MODES[mode];
  document.getElementById('stepLabel').textContent = m.labels[step];
  document.getElementById('initLabel').textContent = m.initTag;
  document.getElementById('convertase3Label').textContent = m.c3Tag;
  document.getElementById('convertase5Label').textContent = m.c5Tag;
  document.getElementById('initiation').classList.toggle('on', step >= 1);
  document.getElementById('convertase3').classList.toggle('on', step >= 2);
  document.getElementById('c3split').classList.toggle('on', step >= 3);
  document.getElementById('convertase5').classList.toggle('on', step >= 4);
  document.getElementById('mac').classList.toggle('on', step >= 4);
  document.getElementById('c5split').classList.toggle('on', step >= 4);
  document.getElementById('lysis').classList.toggle('on', step >= 4);
  document.getElementById('pathogenCell').style.opacity = step >= 4 ? '0.25' : '1';
  document.getElementById('btnClassical').classList.toggle('active', mode === 'classical');
  document.getElementById('btnLectin').classList.toggle('active', mode === 'lectin');
  document.getElementById('btnAlternative').classList.toggle('active', mode === 'alternative');
}
function setMode(newMode) { mode = newMode; step = 0; render(); }
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# INNATE_IMMUNE_RECOGNITION_GENERAL  (source: innate_immunity.html)
# ---------------------------------------------------------------------------
INNATE_IMMUNE_RECOGNITION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of innate immune pattern recognition: a Toll-like receptor on a macrophage detects a pathogen-associated molecular pattern, triggering NF-kB signaling and inflammatory cytokine release.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  #pampDot, #nfkbG { transition: transform 1s ease; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .drift { animation: drift 1.8s ease-in-out infinite; }
  @keyframes drift { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Innate immune pattern recognition</title>
<desc>A pathogen-associated molecular pattern such as bacterial LPS is recognized by a Toll-like receptor on a macrophage. Binding triggers an intracellular signaling cascade that activates the transcription factor NF-kB, which moves into the nucleus and drives the release of inflammatory cytokines, recruiting more immune cells and triggering inflammation.</desc>

<ellipse cx="250" cy="170" rx="130" ry="90" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<text class="ts" x="250" y="70" text-anchor="middle">Macrophage</text>
<ellipse cx="275" cy="200" rx="38" ry="26" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="3 3"/>
<text class="ts" x="275" y="242" text-anchor="middle">Nucleus</text>

<!-- TLR sits in the plasma membrane -->
<circle id="tlr" cx="123" cy="150" r="10" class="c-amber"/>
<text class="ts" x="104" y="180" text-anchor="end">TLR</text>

<g id="pamp" class="stg">
<circle id="pampDot" cx="60" cy="146" r="8" fill="#B91C1C"/>
<text class="ts" x="60" y="122" text-anchor="middle">PAMP (e.g. LPS)</text>
</g>

<g id="signaling" class="stg">
<line x1="135" y1="156" x2="200" y2="178" stroke="#7F77DD" stroke-width="1.5" marker-end="url(#arrow)"/>
<text class="ts" x="150" y="130">Signaling cascade</text>
</g>

<!-- NF-kB is freed in the cytoplasm, then moves into the nucleus -->
<g id="nfkb" class="stg">
<g id="nfkbG" transform="translate(212,186)">
<circle cx="0" cy="0" r="8" class="c-purple pulse"/>
<text class="ts" x="0" y="-13" text-anchor="middle" style="font-size:10px">NF-κB</text>
</g>
</g>

<g id="cytokines" class="stg">
<path d="M312 192 L372 168" stroke="#E24B4A" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
<circle class="drift" cx="406" cy="140" r="6" fill="#E24B4A"/>
<circle class="drift" cx="428" cy="160" r="6" fill="#E24B4A" style="animation-delay:.3s"/>
<circle class="drift" cx="400" cy="178" r="6" fill="#E24B4A" style="animation-delay:.6s"/>
<text class="ts" x="530" y="112" text-anchor="middle">Cytokines released (TNF-α, IL-1, IL-6)</text>
</g>

<g id="inflammation" class="stg">
<text class="th" x="530" y="214" text-anchor="middle">Recruits immune cells,</text>
<text class="th" x="530" y="232" text-anchor="middle">triggers inflammation</text>
</g>

<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — a pathogen-associated molecular pattern (PAMP) is present",
  "Step 1 of 4 — a Toll-like receptor on the macrophage binds the PAMP",
  "Step 2 of 4 — an intracellular signaling cascade activates",
  "Step 3 of 4 — NF-kB moves into the nucleus, driving gene expression",
  "Step 4 of 4 — inflammatory cytokines are released, recruiting more immune cells and triggering inflammation"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('pamp').classList.toggle('on', true);
  // the PAMP stays visible and docks on the TLR at step 1
  document.getElementById('pampDot').style.transform = step >= 1 ? 'translateX(45px)' : 'none';
  document.getElementById('tlr').classList.toggle('pulse', step === 1);
  document.getElementById('signaling').classList.toggle('on', step >= 2);
  document.getElementById('nfkb').classList.toggle('on', step >= 2);
  document.getElementById('nfkbG').style.transform = step >= 3 ? 'translate(275px,200px)' : 'translate(212px,186px)';
  document.getElementById('cytokines').classList.toggle('on', step >= 4);
  document.getElementById('inflammation').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# INNATE_IMMUNE_RECOGNITION_TECHNICAL
# ---------------------------------------------------------------------------
INNATE_IMMUNE_RECOGNITION_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of innate immune signalling as a two-signal model: TLR4 recognizes LPS and signals through MyD88, IRAKs, TRAF6, TAK1 and IKK to free NF-kB and induce cytokines including inactive pro-IL-1 beta; a second danger signal activates the NLRP3 inflammasome, whose caspase-1 matures IL-1 beta and IL-18 and cleaves gasdermin D to cause pyroptosis.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .hide { display: none; }
  .mvg { transition: transform 1s ease, opacity .6s ease; }
  .pulse { animation: pulse 1.1s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.45} }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnTlr" onclick="setMode('tlr')">TLR4 → NF-κB (signal 1)</button>
  <button id="btnInf" onclick="setMode('inf')">NLRP3 inflammasome (signal 2)</button>
</div>

<svg width="100%" viewBox="0 0 680 330" role="img">
<title>Innate immune signalling, technical view</title>
<desc>Signal 1: LPS is transferred by LBP and CD14 to the TLR4-MD-2 complex; TLR4 recruits MyD88, IRAK4 and IRAK1 and TRAF6, which activates TAK1 and then IKK; IKK phosphorylates IkB, which is ubiquitinated and degraded, freeing NF-kB to enter the nucleus and induce TNF-alpha, IL-6 and inactive pro-IL-1 beta. Signal 2: a danger cue such as potassium efflux through P2X7, urate crystals or toxins activates NLRP3, which assembles with ASC and pro-caspase-1; active caspase-1 cleaves pro-IL-1 beta, pro-IL-18 and gasdermin D, whose pores release IL-1 beta and can kill the cell by pyroptosis.</desc>
<defs><marker id="inA" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>

<text class="ts" x="650" y="30" text-anchor="end">outside the cell</text>
<line x1="20" y1="80" x2="660" y2="80" stroke="var(--t)" stroke-width="3"/>
<text class="ts" x="650" y="104" text-anchor="end">macrophage cytoplasm</text>
<ellipse cx="560" cy="262" rx="84" ry="40" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="3 3"/>
<text class="ts" x="560" y="318" text-anchor="middle">Nucleus</text>

<!-- ================ signal 1: TLR4 ================ -->
<g id="gT">
<rect x="112" y="62" width="10" height="18" rx="3" class="c-amber"/>
<text class="ts" x="117" y="40" text-anchor="middle">LBP → CD14</text>
<path d="M126 58 L210 46" stroke="#B91C1C" stroke-width="1.2" stroke-dasharray="3 3" fill="none" marker-end="url(#inA)"/>
<rect x="212" y="64" width="12" height="40" rx="4" class="c-purple"/>
<rect x="230" y="64" width="12" height="40" rx="4" class="c-purple"/>
<circle cx="218" cy="56" r="7" class="c-amber"/><circle cx="236" cy="56" r="7" class="c-amber"/>
<circle cx="227" cy="42" r="6" fill="#B91C1C"/>
<text class="ts" x="227" y="26" text-anchor="middle">LPS</text>
<text class="ts" x="252" y="60">TLR4–MD-2 dimer</text>

<g id="t1" class="stg">
<circle cx="236" cy="132" r="15" class="c-teal"/><text class="ts" x="236" y="135" text-anchor="middle" style="font-size:8px">MyD88</text>
<path d="M236 106 L236 115" stroke="var(--t)" stroke-width="1.2"/>
<path d="M236 148 L236 160" stroke="var(--t)" stroke-width="1.2" fill="none" marker-end="url(#inA)"/>
<circle cx="236" cy="176" r="15" class="c-gray"/><text class="ts" x="236" y="179" text-anchor="middle" style="font-size:8px">IRAK4/1</text>
<path d="M236 192 L236 204" stroke="var(--t)" stroke-width="1.2" fill="none" marker-end="url(#inA)"/>
<circle cx="236" cy="220" r="15" class="c-amber"/><text class="ts" x="236" y="223" text-anchor="middle" style="font-size:8px">TRAF6</text>
<text class="ts" x="210" y="252" text-anchor="end" style="font-size:10px">K63-ubiquitin</text>
</g>
<g id="t2" class="stg">
<path d="M252 220 L312 220" stroke="var(--t)" stroke-width="1.2" fill="none" marker-end="url(#inA)"/>
<circle cx="330" cy="220" r="15" class="c-coral"/><text class="ts" x="330" y="223" text-anchor="middle" style="font-size:8px">TAK1</text>
<path d="M346 220 L402 220" stroke="var(--t)" stroke-width="1.2" fill="none" marker-end="url(#inA)"/>
<circle cx="420" cy="220" r="15" class="c-purple"/><text class="ts" x="420" y="223" text-anchor="middle" style="font-size:8px">IKK</text>
<path d="M420 204 L420 166" stroke="var(--t)" stroke-width="1.2" fill="none" marker-end="url(#inA)"/>
<rect x="490" y="122" width="30" height="40" rx="6" class="c-gray"/>
<text class="ts" x="505" y="178" text-anchor="middle" style="font-size:10px">proteasome</text>
<text class="ts" x="330" y="252" text-anchor="middle" style="font-size:10px">also → MAPKs → AP-1</text>
</g>
<!-- IkB : NF-kB complex -->
<g id="ikb" class="mvg">
<circle cx="408" cy="150" r="12" class="c-gray"/><text class="ts" x="408" y="153" text-anchor="middle" style="font-size:8px">IκBα</text>
<g id="ikbP" class="stg"><circle cx="398" cy="138" r="6" class="c-coral"/><text x="398" y="141" text-anchor="middle" style="font-size:7px;font-weight:600;fill:#7F1D1D">P</text></g>
</g>
<g id="nfkb" class="mvg">
<circle cx="432" cy="150" r="12" class="c-purple"/><text class="ts" x="432" y="153" text-anchor="middle" style="font-size:8px">NF-κB</text>
</g>
<g id="t4" class="stg">
<text class="ts" x="522" y="258">→ TNF-α · IL-6 · IL-12</text>
<text class="ts" x="522" y="274">→ pro-IL-1β (inactive)</text>
<text class="ts" x="30" y="300">endosomal TLR4 also → TRIF → IRF3 → type I IFN</text>
</g>
</g>

<!-- ================ signal 2: NLRP3 inflammasome ================ -->
<g id="gI">
<rect x="398" y="62" width="14" height="36" rx="4" class="c-teal"/>
<text class="ts" x="418" y="118">P2X7</text>
<g id="i1" class="stg">
<circle cx="405" cy="44" r="6" fill="#EF9F27"/><text class="ts" x="394" y="40" text-anchor="end">ATP</text>
<path d="M422 112 L422 50" stroke="#378ADD" stroke-width="2" fill="none" marker-end="url(#inA)"/>
<text class="ts" x="430" y="56">K+ out</text>
<rect x="500" y="36" width="12" height="12" transform="rotate(45 506 42)" fill="#888780"/>
<text class="ts" x="522" y="46">urate crystals, toxins</text>
</g>
<!-- pro-cytokines made during priming -->
<g id="pro" class="mvg">
<circle class="cyt" cx="110" cy="190" r="6" fill="#888780"/><circle class="cyt" cx="128" cy="202" r="6" fill="#888780"/>
<circle class="cyt" cx="112" cy="214" r="6" fill="#888780"/><circle class="cyt" cx="132" cy="180" r="6" fill="#888780"/>
</g>
<text class="ts" x="122" y="240" text-anchor="middle" id="proLabel">pro-IL-1β, pro-IL-18</text>
<!-- NLRP3 -->
<circle id="nlrp3One" cx="300" cy="170" r="14" class="c-gray"/>
<g id="i2" class="stg">
<circle cx="300" cy="148" r="8" class="c-purple"/><circle cx="319" cy="159" r="8" class="c-purple"/><circle cx="319" cy="181" r="8" class="c-purple"/>
<circle cx="300" cy="192" r="8" class="c-purple"/><circle cx="281" cy="181" r="8" class="c-purple"/><circle cx="281" cy="159" r="8" class="c-purple"/>
<circle cx="300" cy="170" r="9" class="c-amber"/>
</g>
<text class="ts" x="300" y="218" text-anchor="middle" id="nlrpLabel">NLRP3 (inactive)</text>
<g id="i3" class="stg">
<path d="M282 196 L150 200" stroke="#D85A30" stroke-width="1.5" fill="none" marker-end="url(#inA)"/>
<text class="ts" x="336" y="166">caspase-1 cleaves</text>
<text class="ts" x="336" y="182">pro-IL-1β, pro-IL-18, gasdermin D</text>
</g>
<g id="i4" class="stg">
<rect x="104" y="72" width="14" height="16" fill="var(--surface-1)" stroke="#B91C1C" stroke-width="1.5"/>
<rect x="138" y="72" width="14" height="16" fill="var(--surface-1)" stroke="#B91C1C" stroke-width="1.5"/>
<text class="ts" x="160" y="64">gasdermin D pores</text>
<text class="th" x="30" y="300">IL-1β, IL-18 released · pyroptosis (fever, inflammation)</text>
</g>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
let mode = 'tlr';
const L = {
  tlr: [
    "Step 0 of 4 — LPS is passed by LBP to CD14 and then to the TLR4–MD-2 complex; two TLR4–MD-2 units dimerize",
    "Step 1 of 4 — the TLR4 TIR domains recruit MyD88 (via TIRAP), which recruits IRAK4 and IRAK1 and then TRAF6, which builds K63-ubiquitin chains",
    "Step 2 of 4 — TRAF6 activates TAK1, which activates IKK (IKKα/β + NEMO); IKK phosphorylates IκBα, which is ubiquitinated and destroyed by the proteasome",
    "Step 3 of 4 — freed NF-κB (p65/p50) enters the nucleus; TAK1 also activates MAPKs → AP-1",
    "Step 4 of 4 — transcription of TNF-α, IL-6, IL-12, chemokines and pro-IL-1β (still inactive); TLR4 taken into endosomes also signals via TRIF → IRF3 → type I interferons"
  ],
  inf: [
    "Step 0 of 4 — signal 1 (priming): TLR → NF-κB has already made pro-IL-1β, pro-IL-18 and NLRP3, but pro-IL-1β is inactive and NLRP3 is idle",
    "Step 1 of 4 — signal 2: a danger cue activates NLRP3 — K+ efflux (e.g. extracellular ATP through P2X7), urate or cholesterol crystals, pore-forming toxins",
    "Step 2 of 4 — NLRP3 oligomerizes and recruits the adaptor ASC, which polymerizes and recruits pro-caspase-1 — the inflammasome",
    "Step 3 of 4 — autoactivated caspase-1 cleaves pro-IL-1β and pro-IL-18 into mature cytokines and cleaves gasdermin D",
    "Step 4 of 4 — gasdermin D N-terminal fragments insert into the membrane as pores: IL-1β and IL-18 are released and the cell may die by pyroptosis"
  ]
};
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnTlr').classList.toggle('active', m === 'tlr');
  document.getElementById('btnInf').classList.toggle('active', m === 'inf');
  document.getElementById('gT').classList.toggle('hide', m !== 'tlr');
  document.getElementById('gI').classList.toggle('hide', m !== 'inf');
  render();
}
function render() {
  document.getElementById('stepLabel').textContent = L[mode][step];
  if (mode === 'tlr') {
    document.getElementById('t1').classList.toggle('on', step >= 1);
    document.getElementById('t2').classList.toggle('on', step >= 2);
    document.getElementById('ikbP').classList.toggle('on', step >= 2);
    const ikb = document.getElementById('ikb');
    ikb.style.transform = step >= 2 ? 'translate(97px,-8px)' : 'none';   // into the proteasome
    ikb.style.opacity = step >= 3 ? 0 : 1;
    document.getElementById('nfkb').style.transform = step >= 3 ? 'translate(68px,112px)' : 'none';
    document.getElementById('t4').classList.toggle('on', step >= 4);
  } else {
    document.getElementById('i1').classList.toggle('on', step >= 1);
    const active = step >= 2;
    document.getElementById('i2').classList.toggle('on', active);
    document.getElementById('nlrp3One').style.opacity = active ? 0 : 1;
    document.getElementById('nlrp3One').classList.toggle('pulse', step === 1);
    document.getElementById('nlrpLabel').textContent = active ? 'NLRP3–ASC–caspase-1 inflammasome' : 'NLRP3 (inactive)';
    document.getElementById('i3').classList.toggle('on', step >= 3);
    document.querySelectorAll('#pro .cyt').forEach(c => c.setAttribute('fill', step >= 3 ? '#E24B4A' : '#888780'));
    document.getElementById('proLabel').textContent = step >= 3 ? 'mature IL-1β, IL-18' : 'pro-IL-1β, pro-IL-18';
    document.getElementById('i4').classList.toggle('on', step >= 4);
    document.getElementById('pro').style.transform = step >= 4 ? 'translateY(-150px)' : 'none';   // out through the pores
  }
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('tlr');
</script>
'''


# ---------------------------------------------------------------------------
# NK_CELL_MISSING_SELF_GENERAL  (source: nk_cell.html)
# ---------------------------------------------------------------------------
NK_CELL_MISSING_SELF_GENERAL = '''
<h2 class="sr-only">Interactive diagram of NK cell missing-self recognition: a switchable comparison between a healthy cell presenting MHC-I, which inhibits killing, and an infected cell that has downregulated MHC-I, which triggers killing.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .hide { display: none; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnHealthy" onclick="setMode('healthy')">Healthy cell</button>
  <button id="btnInfected" onclick="setMode('infected')">Infected cell (MHC-I lost)</button>
</div>

<svg width="100%" viewBox="0 0 680 280" role="img">
<title>NK cell missing-self recognition</title>
<desc>An NK cell checks target cells for MHC class one. A healthy cell displaying MHC-I sends an inhibitory signal that stops the NK cell from killing. An infected or cancerous cell that has downregulated MHC-I to evade T cells loses that inhibitory signal, so activating receptors detecting stress ligands go unopposed, and the NK cell kills it — recognizing the absence of a normal self marker rather than the presence of a foreign one.</desc>

<circle cx="480" cy="140" r="55" class="c-purple"/>
<text class="th" x="480" y="140" text-anchor="middle" dominant-baseline="central">NK cell</text>

<circle id="targetCell" cx="180" cy="140" r="70" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<text class="ts" x="180" y="225" text-anchor="middle" id="targetLabel">Healthy cell</text>

<g id="mhcMarker" class="stg">
<rect id="mhcRect" x="165" y="64" width="30" height="12" rx="3" fill="#EF9F27"/>
<rect id="mhcGap" x="165" y="64" width="30" height="12" rx="3" fill="none" stroke="#888780" stroke-width="1.2" stroke-dasharray="3 2"/>
<text class="ts" x="180" y="52" text-anchor="middle" id="mhcLabel">MHC-I present</text>
</g>

<g id="inhibitorySignal" class="stg">
<line x1="250" y1="130" x2="425" y2="130" stroke="#639922" stroke-width="2" marker-end="url(#arrow)"/>
<text class="ts" x="340" y="115" text-anchor="middle">Inhibitory signal</text>
</g>

<g id="activatingSignal" class="stg">
<line x1="250" y1="150" x2="425" y2="150" stroke="#E24B4A" stroke-width="2" marker-end="url(#arrow)"/>
<text class="ts" x="340" y="170" text-anchor="middle">Activating signal (stress ligands)</text>
</g>

<g id="kill" class="stg">
<circle cx="300" cy="140" r="4" fill="#7F77DD"/><circle cx="318" cy="134" r="4" fill="#7F77DD"/><circle cx="336" cy="142" r="4" fill="#7F77DD"/>
<text class="ts" x="318" y="200" text-anchor="middle">perforin + granzymes</text>
</g>
<g id="outcome" class="stg">
<text class="th" x="480" y="220" text-anchor="middle" id="outcomeLabel">No killing</text>
</g>

<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 2</span>
</div>

<script>
let step = 0;
let mode = 'healthy';
const configHealthy = {
  targetLabel: 'Healthy cell',
  mhcLabel: 'MHC-I present',
  outcomeLabel: 'Inhibitory signal dominates — no killing',
  labels: [
    "Step 0 of 2 — NK cell surveys a healthy cell",
    "Step 1 of 2 — MHC-I present sends an inhibitory signal",
    "Step 2 of 2 — inhibitory signal dominates, the NK cell does not kill"
  ]
};
const configInfected = {
  targetLabel: 'Infected cell',
  mhcLabel: 'MHC-I downregulated (missing)',
  outcomeLabel: 'No inhibition — activating signal wins — NK cell kills',
  labels: [
    "Step 0 of 2 — NK cell surveys an infected cell that has downregulated MHC-I to evade T cells",
    "Step 1 of 2 — no MHC-I means no inhibitory signal; stress ligands provide an activating signal",
    "Step 2 of 2 — with nothing to oppose it, the activating signal wins — the NK cell kills the cell"
  ]
};
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnHealthy').classList.toggle('active', m === 'healthy');
  document.getElementById('btnInfected').classList.toggle('active', m === 'infected');
  const cfg = m === 'healthy' ? configHealthy : configInfected;
  document.getElementById('targetLabel').textContent = cfg.targetLabel;
  document.getElementById('mhcLabel').textContent = cfg.mhcLabel;
  document.getElementById('outcomeLabel').textContent = cfg.outcomeLabel;
  // an infected cell has lost MHC-I: show the empty spot, not a marker
  document.getElementById('mhcRect').classList.toggle('hide', m !== 'healthy');
  document.getElementById('mhcGap').classList.toggle('hide', m === 'healthy');
  render();
}
function render() {
  const cfg = mode === 'healthy' ? configHealthy : configInfected;
  document.getElementById('stepLabel').textContent = cfg.labels[step];
  document.getElementById('mhcMarker').classList.toggle('on', step >= 1);
  document.getElementById('inhibitorySignal').classList.toggle('on', mode === 'healthy' && step >= 1);
  document.getElementById('activatingSignal').classList.toggle('on', step >= 1);
  document.getElementById('outcome').classList.toggle('on', step >= 2);
  document.getElementById('kill').classList.toggle('hide', mode !== 'infected');
  document.getElementById('kill').classList.toggle('on', mode === 'infected' && step >= 2);
  document.getElementById('targetCell').style.opacity = (mode === 'infected' && step >= 2) ? '0.25' : '1';
}
function stepFwd() { if (step < 2) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('healthy');
</script>
'''


# ---------------------------------------------------------------------------
# NK_CELL_MISSING_SELF_TECHNICAL
# ---------------------------------------------------------------------------
NK_CELL_MISSING_SELF_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of NK cell recognition: inhibitory receptors (KIR, CD94/NKG2A) reading HLA class I signal through ITIMs and SHP-1/2, activating receptors such as NKG2D reading stress ligands signal through DAP10/DAP12, the balance decides killing by perforin and granzyme B; antibody-dependent cellular cytotoxicity through CD16 is shown as a second mode.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .hide { display: none; }
  .mvg { transition: transform .9s ease, opacity .6s ease; }
  .rc { transition: x .9s ease, width .9s ease; }
  #ptr { transition: transform .9s ease; }
  #target { transition: opacity .8s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnBal" onclick="setMode('balance')">Missing self (balance)</button>
  <button id="btnAdcc" onclick="setMode('adcc')">ADCC (CD16)</button>
</div>

<svg width="100%" viewBox="0 0 680 330" role="img">
<title>NK cell recognition, technical view</title>
<desc>Inhibitory receptors KIR and CD94/NKG2A bind self HLA class I and signal through ITIM motifs that recruit the phosphatases SHP-1 and SHP-2. The activating receptor NKG2D binds stress ligands such as MICA, MICB and ULBPs and signals through DAP10 and DAP12. A healthy cell inhibits the NK cell; a stressed cell that keeps HLA-I is balanced; a cell that has lost HLA-I and expresses stress ligands is killed by perforin and granzyme B. In antibody-dependent cellular cytotoxicity, CD16 binds the Fc region of IgG coating a target and triggers killing.</desc>

<circle id="target" cx="150" cy="150" r="85" fill="var(--surface-1)" stroke="var(--t)" stroke-width="1.5"/>
<text class="ts" x="150" y="256" text-anchor="middle" id="targetLabel"></text>
<circle cx="520" cy="150" r="85" fill="var(--surface-1)" stroke="#7F77DD" stroke-width="2"/>
<text class="th" x="520" y="92" text-anchor="middle">NK cell</text>

<!-- ============ balance mode ============ -->
<g id="vBal">
<!-- inhibitory pair -->
<g id="hla" class="mvg"><rect id="hlaR" class="rc" x="235" y="104" width="62" height="12" rx="4" fill="#EF9F27"/></g>
<rect id="hlaGap" x="235" y="104" width="62" height="12" rx="4" fill="none" stroke="#888780" stroke-width="1.2" stroke-dasharray="3 2"/>
<text class="ts" x="250" y="96" id="hlaLabel">HLA-I</text>
<g id="kir" class="mvg"><rect id="kirR" class="rc" x="373" y="104" width="62" height="12" rx="4" fill="#7F77DD"/></g>
<text class="ts" x="430" y="96" text-anchor="end">KIR / NKG2A</text>
<!-- activating pair -->
<g id="lig" class="mvg"><rect id="ligR" class="rc" x="235" y="184" width="62" height="12" rx="4" fill="#E24B4A"/></g>
<text class="ts" x="236" y="214" id="ligLabel">MICA/B, ULBP</text>
<g id="nkg" class="mvg"><rect id="nkgR" class="rc" x="373" y="184" width="62" height="12" rx="4" fill="#D85A30"/></g>
<text class="ts" x="430" y="214" text-anchor="end">NKG2D</text>

<g id="itim" class="stg"><text class="ts" x="452" y="128" style="fill:#3C3489">ITIM → SHP-1/2</text><text class="ts" x="452" y="142" style="fill:#3C3489;font-size:10px">dephosphorylates</text></g>
<g id="itam" class="stg"><text class="ts" x="452" y="178" style="fill:#B4400A">DAP10/12 (ITAM)</text><text class="ts" x="452" y="192" style="fill:#B4400A;font-size:10px">→ Syk/ZAP-70, PI3K</text></g>

<!-- balance meter -->
<line x1="240" y1="298" x2="440" y2="298" stroke="var(--t)" stroke-width="2"/>
<line x1="340" y1="290" x2="340" y2="306" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="236" y="302" text-anchor="end">inhibition</text>
<text class="ts" x="444" y="302">activation</text>
<path id="ptr" d="M340 290 L333 278 L347 278 Z" fill="#B91C1C"/>
</g>

<!-- ============ ADCC mode ============ -->
<g id="vAdcc" class="hide">
<g id="abs">
<path d="M236 112 L250 120 L236 128 M250 120 L292 120" stroke="#378ADD" stroke-width="3" fill="none"/>
<path d="M236 142 L250 150 L236 158 M250 150 L292 150" stroke="#378ADD" stroke-width="3" fill="none"/>
<path d="M236 172 L250 180 L236 188 M250 180 L292 180" stroke="#378ADD" stroke-width="3" fill="none"/>
</g>
<text class="ts" x="262" y="102" text-anchor="middle">IgG</text>
<g id="cd16" class="mvg">
<rect class="rc cd" x="400" y="115" width="35" height="10" rx="3" fill="#C9C4F5" stroke="#7F77DD" stroke-width="1"/>
<rect class="rc cd" x="400" y="145" width="35" height="10" rx="3" fill="#C9C4F5" stroke="#7F77DD" stroke-width="1"/>
<rect class="rc cd" x="400" y="175" width="35" height="10" rx="3" fill="#C9C4F5" stroke="#7F77DD" stroke-width="1"/>
</g>
<text class="ts" x="430" y="212" text-anchor="end">CD16 (FcγRIIIa)</text>
<g id="aItam" class="stg"><text class="ts" x="452" y="146" style="fill:#B4400A">CD3ζ / FcRγ ITAM</text><text class="ts" x="452" y="160" style="fill:#B4400A;font-size:10px">→ Syk/ZAP-70</text></g>
<g id="drugs" class="stg"><text class="th" x="340" y="304" text-anchor="middle">e.g. rituximab (anti-CD20), trastuzumab (anti-HER2)</text></g>
</g>

<!-- killing (both modes) -->
<g id="kill" class="stg">
<circle cx="312" cy="164" r="4" fill="#7F77DD"/><circle cx="328" cy="170" r="4" fill="#7F77DD"/><circle cx="344" cy="162" r="4" fill="#7F77DD"/><circle cx="360" cy="168" r="4" fill="#7F77DD"/>
<text class="ts" x="150" y="154" text-anchor="middle">apoptosis</text>
<text class="ts" x="336" y="240" text-anchor="middle">perforin + granzyme B · IFN-γ</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
let mode = 'balance';
const BAL = {
  labels: [
    "Step 0 of 4 — the NK cell contacts a target: inhibitory receptors (KIR, CD94/NKG2A) probe for self HLA class I, activating receptors (NKG2D) probe for stress ligands",
    "Step 1 of 4 — healthy cell: HLA-I engages KIR/NKG2A → ITIMs recruit SHP-1/SHP-2; with no stress ligands the balance tips to inhibition — no killing",
    "Step 2 of 4 — stressed cell that still shows HLA-I: NKG2D binds MICA/B or ULBP → DAP10/DAP12 → Syk/ZAP-70 and PI3K, but SHP-1/2 dephosphorylate these signals — the outcome depends on the balance",
    "Step 3 of 4 — infected or tumour cell that has lost HLA-I to escape CD8 T cells: no ITIM brake, stress ligands present → activation wins",
    "Step 4 of 4 — killing: granules polarize to the synapse; perforin pores let granzyme B in → caspases → apoptosis (Fas–FasL as a backup); IFN-γ is also released"
  ],
  target: ['Target cell', 'Healthy cell', 'Stressed cell (HLA-I kept)', 'Infected / tumour cell (HLA-I lost)', 'Infected / tumour cell (HLA-I lost)'],
  hla: [true, true, true, false, false],
  lig: [false, false, true, true, true],
  ptr: [0, -70, -25, 70, 85]
};
const ADCC = [
  "Step 0 of 4 — a virus-infected or tumour cell is coated with IgG antibodies bound to its surface antigens",
  "Step 1 of 4 — CD16 (FcγRIIIa) on the NK cell binds the antibodies' Fc regions — the antibody bridges the target and the NK cell",
  "Step 2 of 4 — CD16 signals through ITAM-bearing CD3ζ/FcRγ chains → Syk/ZAP-70: a strong activating signal, even if the target still shows HLA-I",
  "Step 3 of 4 — degranulation: perforin + granzyme B → target apoptosis; IFN-γ is released",
  "Step 4 of 4 — antibody-dependent cellular cytotoxicity (ADCC) is one way therapeutic antibodies such as rituximab and trastuzumab kill target cells"
];
function setR(el, x, w) { el.setAttribute('x', x); el.setAttribute('width', w); el.style.x = x + 'px'; el.style.width = w + 'px'; }
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnBal').classList.toggle('active', m === 'balance');
  document.getElementById('btnAdcc').classList.toggle('active', m === 'adcc');
  document.getElementById('vBal').classList.toggle('hide', m !== 'balance');
  document.getElementById('vAdcc').classList.toggle('hide', m !== 'adcc');
  render();
}
function render() {
  let killing;
  if (mode === 'balance') {
    const c = BAL;
    document.getElementById('stepLabel').textContent = c.labels[step];
    document.getElementById('targetLabel').textContent = c.target[step];
    const hla = c.hla[step], lig = c.lig[step], engaged = step >= 1;
    const hlaEl = document.getElementById('hla');
    hlaEl.style.opacity = hla ? 1 : 0;
    document.getElementById('hlaGap').style.opacity = hla ? 0 : 1;
    document.getElementById('hlaLabel').textContent = hla ? 'HLA-I' : 'HLA-I lost';
    // engaged receptor pairs slide together and meet in the gap
    const pair = (tId, nId, on) => {
      setR(document.getElementById(tId), 235, on ? 100 : 62);
      setR(document.getElementById(nId), on ? 335 : 373, on ? 100 : 62);
    };
    pair('hlaR', 'kirR', engaged && hla);
    const ligEl = document.getElementById('lig');
    ligEl.style.opacity = lig ? 1 : 0;
    document.getElementById('ligLabel').style.opacity = lig ? 1 : 0;
    pair('ligR', 'nkgR', engaged && lig);
    document.getElementById('itim').classList.toggle('on', engaged && hla);
    document.getElementById('itam').classList.toggle('on', engaged && lig);
    document.getElementById('ptr').style.transform = `translateX(${c.ptr[step]}px)`;
    killing = step >= 4;
  } else {
    document.getElementById('stepLabel').textContent = ADCC[step];
    document.getElementById('targetLabel').textContent = 'Antibody-coated target';
    document.querySelectorAll('#cd16 .cd').forEach(r => setR(r, step >= 1 ? 292 : 400, step >= 1 ? 143 : 35));
    document.getElementById('aItam').classList.toggle('on', step >= 2);
    document.getElementById('drugs').classList.toggle('on', step >= 4);
    killing = step >= 3;
  }
  document.getElementById('kill').classList.toggle('on', killing);
  document.getElementById('target').style.opacity = killing ? 0.35 : 1;
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('balance');
</script>
'''


# ---------------------------------------------------------------------------
# GERMINAL_CENTER_TECHNICAL  (source: germinal_center.html)
# ---------------------------------------------------------------------------
GERMINAL_CENTER_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of the germinal center reaction: somatic hypermutation, affinity testing against follicular dendritic cells, Tfh-mediated selection, and cytokine-driven class switching.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Germinal center reaction, technical view</title>
<desc>An activated B cell proliferates in the germinal center dark zone. AID enzyme introduces mutations into the antibody variable region genes, somatic hypermutation. Mutated B cells migrate to the light zone and test their affinity for antigen displayed on follicular dendritic cells. T follicular helper cells select only the highest-affinity clones to survive, driving affinity maturation, while low-affinity clones undergo apoptosis. Selected cells undergo cytokine-driven class switching and differentiate into high-affinity plasma cells and memory B cells.</desc>

<ellipse cx="200" cy="160" rx="160" ry="120" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<line x1="200" y1="40" x2="200" y2="280" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<text class="ts" x="110" y="55" text-anchor="middle">Dark zone</text>
<text class="ts" x="290" y="55" text-anchor="middle">Light zone</text>

<circle cx="110" cy="150" r="14" class="c-teal"/>
<text class="ts" x="110" y="185" text-anchor="middle">B cell proliferates</text>

<g id="mutation" class="stg">
<circle cx="110" cy="150" r="18" fill="none" stroke="#EF9F27" stroke-width="2" stroke-dasharray="2 2" class="pulse"/>
<text class="ts" x="110" y="120" text-anchor="middle">AID mutates BCR gene</text>
</g>

<g id="fdc" class="stg">
<circle cx="290" cy="150" r="12" class="c-amber"/>
<text class="ts" x="290" y="185" text-anchor="middle">Follicular dendritic cell</text>
<text class="ts" x="290" y="120" text-anchor="middle">Antigen displayed — affinity tested</text>
</g>

<g id="selection" class="stg">
<circle cx="330" cy="110" r="10" class="c-purple"/>
<text class="ts" x="330" y="95" text-anchor="middle">Tfh selects high-affinity clones</text>
<path d="M250 190 L270 210 M270 190 L250 210" stroke="#E24B4A" stroke-width="2" stroke-linecap="round"/>
<text class="ts" x="260" y="230" text-anchor="middle">Low-affinity — apoptosis</text>
</g>

<g id="classSwitch" class="stg">
<text class="th" x="290" y="255" text-anchor="middle">Class switching (cytokine-driven)</text>
</g>

<g id="output" class="stg">
<circle cx="450" cy="130" r="20" class="c-coral"/>
<text class="ts" x="450" y="130" text-anchor="middle" dominant-baseline="central">Plasma cell</text>
<circle cx="450" cy="190" r="16" class="c-gray"/>
<text class="ts" x="450" y="190" text-anchor="middle" dominant-baseline="central">Memory B</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — activated B cell proliferates in the dark zone",
  "Step 1 of 4 — AID enzyme introduces mutations into the antibody gene (somatic hypermutation)",
  "Step 2 of 4 — mutated B cells migrate to the light zone, testing affinity against antigen on follicular dendritic cells",
  "Step 3 of 4 — Tfh cells select only the highest-affinity clones to survive; low-affinity clones undergo apoptosis (affinity maturation)",
  "Step 4 of 4 — selected cells undergo class switching and differentiate into high-affinity plasma cells and memory B cells"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('mutation').classList.toggle('on', step >= 1);
  document.getElementById('fdc').classList.toggle('on', step >= 2);
  document.getElementById('selection').classList.toggle('on', step === 3);
  document.getElementById('classSwitch').classList.toggle('on', step >= 4);
  document.getElementById('output').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# TCR_SIGNALING_TECHNICAL  (source: tcr_signaling.html)
# ---------------------------------------------------------------------------
TCR_SIGNALING_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of TCR signaling: Lck phosphorylates CD3 ITAMs, ZAP-70 builds the LAT signalosome, PLC-gamma generates second messengers, and calcineurin activates NFAT to drive IL-2 transcription.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>TCR signaling cascade, technical view</title>
<desc>The TCR-CD3 complex engages peptide-MHC. Lck phosphorylates ITAMs on CD3, recruiting ZAP-70, which phosphorylates LAT to form a signalosome and activates PLC-gamma. PLC-gamma generates DAG and IP3: DAG activates the Ras-MAPK pathway while IP3 triggers calcium release, activating calcineurin. Calcineurin dephosphorylates NFAT, which translocates to the nucleus and drives IL-2 gene transcription, causing T cell proliferation.</desc>

<line x1="30" y1="140" x2="650" y2="140" stroke="var(--border-strong)" stroke-width="2"/>
<text class="ts" x="60" y="125">Membrane</text>

<circle cx="90" cy="140" r="12" class="c-purple"/>
<text class="ts" x="90" y="165" text-anchor="middle">TCR-CD3</text>

<g id="lck" class="stg">
<circle cx="140" cy="120" r="8" class="c-amber pulse"/>
<text class="ts" x="140" y="105" text-anchor="middle">Lck phosphorylates ITAMs</text>
</g>

<g id="zap70" class="stg">
<circle cx="190" cy="140" r="9" class="c-teal"/>
<text class="ts" x="190" y="165" text-anchor="middle">ZAP-70</text>
</g>

<g id="lat" class="stg">
<circle cx="250" cy="160" r="10" class="c-coral"/>
<text class="ts" x="250" y="185" text-anchor="middle">LAT signalosome</text>
</g>

<g id="plcg" class="stg">
<circle cx="310" cy="140" r="9" class="c-red"/>
<text class="ts" x="310" y="120" text-anchor="middle">PLC-gamma</text>
</g>

<g id="dag" class="stg">
<circle cx="380" cy="100" r="7" fill="#639922"/>
<text class="ts" x="380" y="82" text-anchor="middle">DAG → Ras-MAPK</text>
</g>
<g id="ip3" class="stg">
<circle cx="380" cy="180" r="7" fill="#378ADD"/>
<text class="ts" x="380" y="200" text-anchor="middle">IP3 → Ca2+ release</text>
</g>

<g id="calcineurin" class="stg">
<circle cx="450" cy="180" r="9" class="c-purple"/>
<text class="ts" x="450" y="205" text-anchor="middle">Calcineurin</text>
</g>

<g id="nfat" class="stg">
<circle cx="520" cy="160" r="10" class="c-amber pulse"/>
<text class="ts" x="520" y="185" text-anchor="middle">NFAT → nucleus</text>
</g>

<g id="il2" class="stg">
<text class="th" x="600" y="160" text-anchor="middle">IL-2 gene transcribed — proliferation</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 5</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 5 — TCR-CD3 complex engages peptide-MHC",
  "Step 1 of 5 — Lck phosphorylates ITAMs on CD3, recruiting ZAP-70",
  "Step 2 of 5 — ZAP-70 phosphorylates LAT, forming a signalosome that activates PLC-gamma",
  "Step 3 of 5 — PLC-gamma generates DAG (activating Ras-MAPK) and IP3 (triggering Ca2+ release)",
  "Step 4 of 5 — calcium activates calcineurin, which dephosphorylates NFAT",
  "Step 5 of 5 — NFAT enters the nucleus and drives IL-2 gene transcription — the T cell proliferates"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('lck').classList.toggle('on', step >= 1);
  document.getElementById('zap70').classList.toggle('on', step >= 1);
  document.getElementById('lat').classList.toggle('on', step >= 2);
  document.getElementById('plcg').classList.toggle('on', step >= 2);
  document.getElementById('dag').classList.toggle('on', step >= 3);
  document.getElementById('ip3').classList.toggle('on', step >= 3);
  document.getElementById('calcineurin').classList.toggle('on', step >= 4);
  document.getElementById('nfat').classList.toggle('on', step >= 5);
  document.getElementById('il2').classList.toggle('on', step >= 5);
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# IMMUNOLOGICAL_MEMORY_GENERAL  (source: immunological_memory.html)
# ---------------------------------------------------------------------------
IMMUNOLOGICAL_MEMORY_GENERAL = '''
<h2 class="sr-only">Interactive diagram of immunological memory: a switchable comparison between the slow, modest primary immune response and the fast, strong secondary response driven by pre-existing memory cells.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #responseBar { transition: height 1s ease, y 1s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnPrimary" onclick="setMode('primary')">Primary exposure</button>
  <button id="btnSecondary" onclick="setMode('secondary')">Secondary exposure</button>
</div>

<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Immunological memory — primary vs secondary response</title>
<desc>On first exposure to an antigen, naive lymphocytes must find, activate, and proliferate, so the antibody response is slow to rise, taking one to two weeks, and moderate in magnitude, dominated initially by IgM. On second exposure, pre-existing memory cells respond within days, producing a faster, much larger, higher-affinity IgG-dominated response.</desc>

<line x1="60" y1="240" x2="620" y2="240" stroke="var(--t)" stroke-width="1"/>
<line x1="60" y1="240" x2="60" y2="40" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="340" y="270" text-anchor="middle">Time since exposure</text>
<text class="ts" x="30" y="140" text-anchor="middle" transform="rotate(-90 30 140)">Antibody level</text>

<rect id="responseBar" x="300" y="220" width="80" height="20" fill="#7F77DD"/>
<text class="ts" x="340" y="255" text-anchor="middle" id="lagLabel">Lag: 1-2 weeks</text>
<text class="ts" x="500" y="60" text-anchor="middle" id="peakLabel"></text>

<g id="cellSource" class="stg">
<circle cx="150" cy="140" r="10" class="c-gray"/>
<text class="ts" x="150" y="120" text-anchor="middle" id="sourceLabel">Naive lymphocytes</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0</span>
</div>

<script>
let step = 0;
let mode = 'primary';
const configPrimary = {
  source: 'Naive lymphocytes — must be found and activated',
  lag: 'Lag: 1-2 weeks',
  barY: [220, 190, 150],
  barH: [20, 50, 90],
  peakNote: 'Moderate peak, mostly IgM then IgG',
  labels: [
    'Step 0 of 2 — antigen encountered for the first time',
    'Step 1 of 2 — naive B and T cells must be found and activated — slow',
    'Step 2 of 2 — response peaks late (1-2 weeks) and moderate, IgM-dominant early on'
  ]
};
const configSecondary = {
  source: 'Memory cells — already primed and waiting',
  lag: 'Lag: 1-2 days',
  barY: [220, 130, 60],
  barH: [20, 110, 180],
  peakNote: 'Much higher peak, high-affinity IgG',
  labels: [
    'Step 0 of 2 — same antigen encountered again',
    'Step 1 of 2 — pre-existing memory cells respond almost immediately',
    'Step 2 of 2 — response peaks fast (1-2 days) and much higher, dominated by high-affinity IgG'
  ]
};
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnPrimary').classList.toggle('active', m === 'primary');
  document.getElementById('btnSecondary').classList.toggle('active', m === 'secondary');
  const cfg = m === 'primary' ? configPrimary : configSecondary;
  document.getElementById('sourceLabel').textContent = cfg.source;
  document.getElementById('lagLabel').textContent = cfg.lag;
  render();
}
function render() {
  const cfg = mode === 'primary' ? configPrimary : configSecondary;
  document.getElementById('stepLabel').textContent = cfg.labels[step];
  document.getElementById('cellSource').classList.toggle('on', step >= 1);
  document.getElementById('responseBar').setAttribute('y', cfg.barY[step]);
  document.getElementById('responseBar').setAttribute('height', cfg.barH[step]);
  document.getElementById('peakLabel').textContent = step >= 2 ? cfg.peakNote : '';
}
function stepFwd() { if (step < 2) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('primary');
</script>
'''


# ---------------------------------------------------------------------------
# TYPE1_HYPERSENSITIVITY_GENERAL  (source: type1_hypersensitivity.html)
# ---------------------------------------------------------------------------
TYPE1_HYPERSENSITIVITY_GENERAL = '''
<h2 class="sr-only">Interactive diagram of type one hypersensitivity: IgE sensitizes mast cells on first exposure, and a second exposure cross-links that IgE, triggering degranulation and histamine release.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .drift { animation: drift 1.6s ease-in-out infinite; }
  @keyframes drift { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Type I hypersensitivity, general view</title>
<desc>On first exposure to an allergen, plasma cells produce IgE, which binds Fc receptors on mast cells, sensitizing them without triggering a reaction. On a second exposure, the allergen cross-links the bound IgE molecules, triggering the mast cell to degranulate, releasing histamine and other mediators that cause vasodilation, increased permeability, and smooth muscle contraction — the symptoms of an allergic reaction.</desc>

<ellipse cx="340" cy="170" rx="90" ry="70" class="c-coral"/>
<text class="th" x="340" y="170" text-anchor="middle" dominant-baseline="central">Mast cell</text>

<g id="ige" class="stg">
<path d="M263 133 L277 119 M277 133 L263 119" stroke="#7F77DD" stroke-width="2"/>
<path d="M403 133 L417 119 M417 133 L403 119" stroke="#7F77DD" stroke-width="2"/>
<text class="ts" x="340" y="58" text-anchor="middle">IgE bound to Fc receptors — sensitized</text>
</g>

<g id="allergen" class="stg">
<circle cx="270" cy="112" r="8" fill="#EF9F27"/>
<circle cx="410" cy="112" r="8" fill="#EF9F27"/>
<text class="ts" x="340" y="40" text-anchor="middle">Allergen cross-links IgE</text>
</g>

<g id="degranulation" class="stg">
<circle class="drift" cx="300" cy="180" r="6" fill="#B91C1C"/>
<circle class="drift" cx="340" cy="200" r="6" fill="#B91C1C" style="animation-delay:.3s"/>
<circle class="drift" cx="380" cy="180" r="6" fill="#B91C1C" style="animation-delay:.6s"/>
<text class="ts" x="340" y="230" text-anchor="middle">Degranulation — histamine released</text>
</g>

<g id="symptoms" class="stg">
<text class="th" x="340" y="270" text-anchor="middle">Vasodilation, swelling, bronchoconstriction</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 3</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 3 — first exposure: IgE binds Fc receptors on mast cells, sensitizing them (no reaction yet)",
  "Step 1 of 3 — second exposure: allergen cross-links the bound IgE molecules",
  "Step 2 of 3 — cross-linking triggers the mast cell to degranulate, releasing histamine",
  "Step 3 of 3 — histamine causes vasodilation, swelling, and smooth muscle contraction — allergy symptoms"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('ige').classList.toggle('on', step >= 0);
  document.getElementById('allergen').classList.toggle('on', step >= 1);
  document.getElementById('degranulation').classList.toggle('on', step >= 2);
  document.getElementById('symptoms').classList.toggle('on', step >= 3);
}
function stepFwd() { if (step < 3) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# IMMUNE_CHECKPOINT_GENERAL  (source: immune_checkpoint.html)
# ---------------------------------------------------------------------------
IMMUNE_CHECKPOINT_GENERAL = '''
<h2 class="sr-only">Interactive diagram of the PD-1/PD-L1 immune checkpoint: a tumor cell exploits PD-L1 to exhaust an attacking T cell, and a checkpoint inhibitor drug blocks this interaction to restore the T cell's killing ability.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #tcellGroup { transition: transform 1s ease; }
  .docked #tcellGroup { transform: translateX(-30px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>PD-1 / PD-L1 immune checkpoint, general view</title>
<desc>An activated T cell expresses PD-1 as a normal negative feedback brake. A tumor cell exploits this by expressing PD-L1, and their binding delivers an inhibitory signal that exhausts the T cell, letting the tumor evade attack. A checkpoint inhibitor drug, an anti-PD-1 or anti-PD-L1 antibody, blocks this interaction, restoring the T cell's ability to kill the tumor cell — the basis of modern cancer immunotherapy.</desc>

<circle cx="180" cy="150" r="70" fill="none" stroke="var(--t)" stroke-width="1.5" id="tumorCell"/>
<text class="ts" x="180" y="235" text-anchor="middle">Tumor cell</text>

<g id="pdl1" class="stg">
<rect x="165" y="95" width="30" height="12" rx="3" fill="#E24B4A"/>
<text class="ts" x="180" y="80" text-anchor="middle">PD-L1</text>
</g>

<g id="tcellGroup">
<circle cx="440" cy="150" r="55" class="c-purple"/>
<text class="th" x="440" y="150" text-anchor="middle" dominant-baseline="central">T cell</text>
</g>

<g id="pd1" class="stg">
<rect x="385" y="120" width="26" height="12" rx="3" fill="#7F77DD"/>
<text class="ts" x="398" y="105" text-anchor="middle">PD-1</text>
</g>

<g id="binding" class="stg">
<line x1="255" y1="115" x2="385" y2="126" stroke="#E24B4A" stroke-width="2"/>
<text class="ts" x="320" y="105" text-anchor="middle">Inhibitory signal — T cell exhausted</text>
</g>

<g id="drug" class="stg">
<rect x="290" y="140" width="60" height="20" rx="6" class="c-teal"/>
<text class="ts" x="320" y="150" text-anchor="middle" dominant-baseline="central">Anti-PD-1</text>
<text class="ts" x="320" y="175" text-anchor="middle">Checkpoint inhibitor blocks binding</text>
</g>

<g id="restored" class="stg">
<text class="th" x="320" y="250" text-anchor="middle">T cell restored — kills the tumor cell</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — activated T cell expresses PD-1, a normal negative feedback brake",
  "Step 1 of 4 — tumor cell expresses PD-L1, exploiting this checkpoint",
  "Step 2 of 4 — PD-1/PD-L1 binding delivers an inhibitory signal — the T cell becomes exhausted, tumor evades attack",
  "Step 3 of 4 — a checkpoint inhibitor drug (anti-PD-1 antibody) blocks the interaction",
  "Step 4 of 4 — T cell function restored — it can now kill the tumor cell (basis of cancer immunotherapy)"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('pdl1').classList.toggle('on', step >= 1);
  document.getElementById('pd1').classList.toggle('on', step >= 0);
  document.querySelector('svg').classList.toggle('docked', step >= 1 && step < 3);
  document.getElementById('binding').classList.toggle('on', step >= 2 && step < 3);
  document.getElementById('drug').classList.toggle('on', step >= 3);
  document.getElementById('restored').classList.toggle('on', step >= 4);
  document.getElementById('tumorCell').style.opacity = step >= 4 ? '0.3' : '1';
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# DNA_MISMATCH_REPAIR_GENERAL  (source: mismatch_repair.html)
# ---------------------------------------------------------------------------
DNA_MISMATCH_REPAIR_GENERAL = '''
<h2 class="sr-only">Interactive diagram of DNA mismatch repair: a replication error is detected, the faulty segment excised, and the correct sequence resynthesized and sealed.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }   /* faint previews keep their shape but not their (overlapping) captions */
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #gap { transition: opacity 0.6s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 260" role="img">
<title>DNA mismatch repair, general view</title>
<desc>DNA polymerase makes a replication error, creating a mismatched base pair. Mismatch repair proteins detect the distortion, excise the incorrect segment on the new strand, DNA polymerase resynthesizes the correct sequence using the template, and ligase seals the remaining nick.</desc>

<line x1="30" y1="120" x2="650" y2="120" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<line x1="30" y1="140" x2="650" y2="140" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
<text class="ts" x="30" y="110">Template strand (parental — correct)</text>
<text class="ts" x="30" y="160" id="newStrandLabel">New strand (carries the error)</text>
<line id="fixedPair" x1="340" y1="122" x2="340" y2="138" stroke="#1D9E75" stroke-width="3" stroke-linecap="round" style="opacity:0;transition:opacity .5s ease"/>

<circle id="mismatch" cx="340" cy="130" r="8" fill="#E24B4A"/>
<text class="ts" x="340" y="105" text-anchor="middle" id="mismatchLabel">Mismatched base</text>

<g id="mutS" class="stg">
<circle cx="340" cy="130" r="20" fill="none" stroke="#7F77DD" stroke-width="2" stroke-dasharray="3 3" class="pulse"/>
<text class="ts" x="340" y="165" text-anchor="middle">Repair complex detects distortion</text>
</g>

<g id="excision" class="stg">
<rect id="gap" x="300" y="135" width="80" height="10" fill="var(--surface-1)"/>
<text class="ts" x="340" y="190" text-anchor="middle">Faulty segment excised</text>
</g>

<g id="resynthesis" class="stg">
<rect x="300" y="135" width="80" height="10" fill="#1D9E75" stroke-dasharray="4 3"/>
<text class="ts" x="340" y="190" text-anchor="middle">Polymerase resynthesizes correct sequence</text>
</g>

<g id="ligate" class="stg">
<circle cx="380" cy="140" r="6" fill="#EF9F27"/>
<text class="ts" x="380" y="215" text-anchor="middle">Ligase seals the nick — error corrected</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — DNA polymerase makes a replication error, a mismatched base pair",
  "Step 1 of 4 — mismatch repair proteins detect the distortion in the helix",
  "Step 2 of 4 — the faulty segment on the new strand is excised",
  "Step 3 of 4 — DNA polymerase resynthesizes the correct sequence using the template strand",
  "Step 4 of 4 — ligase seals the remaining nick — the error is corrected"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('mismatchLabel').style.opacity = step === 0 ? '1' : '0';
  document.getElementById('mutS').classList.toggle('on', step === 1);
  document.getElementById('mismatch').style.opacity = step >= 2 ? '0' : '1';
  document.getElementById('excision').classList.toggle('on', step === 2);
  document.getElementById('resynthesis').classList.toggle('on', step >= 3);
  document.getElementById('fixedPair').style.opacity = step >= 3 ? '1' : '0';   // the correct base now pairs with the template
  document.getElementById('newStrandLabel').textContent = step >= 3 ? 'New strand (now corrected)' : 'New strand (carries the error)';
  document.getElementById('ligate').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# DNA_MISMATCH_REPAIR_TECHNICAL  (new)
# ---------------------------------------------------------------------------
DNA_MISMATCH_REPAIR_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of human DNA mismatch repair: MutS-alpha clamps a mismatch, MutL-alpha and PCNA nick only the new strand, EXO1 excises it, Pol delta and ligase I restore it, and loss of mismatch repair causes microsatellite instability in Lynch syndrome.</h2>
<style>
  .reveal { opacity: 0; transition: opacity .5s ease; }
  .reveal.on { opacity: 1; }
  #mutSa { transition: transform .9s ease, opacity .5s ease; }
  .slide #mutSa { transform: translateX(-26px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>DNA mismatch repair, technical view</title>
<desc>After replication a G-T mismatch sits in the newly made strand, which still carries a nick where PCNA is loaded. MutS-alpha, made of MSH2 and MSH6, clamps onto the mismatch and, on binding ATP, becomes a sliding clamp. It recruits MutL-alpha, made of MLH1 and PMS2; PCNA activates the PMS2 endonuclease so that only the new strand is nicked. In E. coli the same job is done by MutH, which nicks the new strand at GATC sites that are not yet methylated. EXO1 then removes the new strand from the nick past the mismatch while RPA protects the single-stranded template. DNA polymerase delta with PCNA fills the gap using the template, and DNA ligase I seals the strand. Inherited loss of MLH1, MSH2, MSH6 or PMS2 causes Lynch syndrome: slippage errors in short repeats are not corrected, producing microsatellite instability and a high risk of colorectal and endometrial cancer; such tumours carry many neoantigens and respond well to PD-1 checkpoint inhibitors.</desc>

<text class="ts" x="30" y="92">Template (parental)</text>
<text class="ts" x="30" y="138" id="newLblT">New strand</text>
<line x1="30" y1="100" x2="650" y2="100" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<line x1="30" y1="120" x2="196" y2="120" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
<line id="newExcised" x1="204" y1="120" x2="430" y2="120" stroke="#D85A30" stroke-width="3" stroke-linecap="round" style="transition:opacity .6s ease"/>
<line x1="430" y1="120" x2="650" y2="120" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
<line id="newFill" x1="196" y1="120" x2="430" y2="120" stroke="#1D9E75" stroke-width="3" stroke-linecap="round" style="opacity:0;transition:opacity .6s ease"/>

<circle id="mmDot" cx="400" cy="110" r="6" fill="#E24B4A" style="transition:opacity .5s ease"/>
<line id="okPair" x1="400" y1="102" x2="400" y2="118" stroke="#1D9E75" stroke-width="3" stroke-linecap="round" style="opacity:0;transition:opacity .5s ease"/>

<g id="mmLbl" class="reveal"><text class="ts" x="400" y="72" text-anchor="middle" font-weight="600" fill="#B91C1C">G·T mismatch</text></g>
<g id="nickLbl" class="reveal">
<text class="ts" x="200" y="150" text-anchor="middle">nick in new strand</text>
</g>
<g id="pcna" class="reveal">
<ellipse cx="214" cy="110" rx="7" ry="22" fill="none" stroke="#0F6E56" stroke-width="3"/>
<text class="ts" x="214" y="80" text-anchor="middle" font-weight="600" fill="#0F6E56">PCNA</text>
</g>

<g id="mutSg" class="reveal">
<g id="mutSa">
<rect x="378" y="84" width="44" height="52" rx="12" fill="#C4B5FD" fill-opacity="0.75" stroke="#6D28D9" stroke-width="1.5"/>
</g>
<text class="ts" x="400" y="152" text-anchor="middle" font-weight="600" fill="#6D28D9" id="mutSLbl">MutSα (MSH2–MSH6)</text>
<text class="ts" x="400" y="72" text-anchor="middle" fill="#6D28D9" id="atpLbl">+ ATP → sliding clamp</text>
</g>
<g id="mutLg" class="reveal">
<rect x="310" y="86" width="40" height="48" rx="12" fill="#FDE68A" fill-opacity="0.85" stroke="#B45309" stroke-width="1.5"/>
<text class="ts" x="300" y="152" text-anchor="end" font-weight="600" fill="#B45309">MutLα (MLH1–PMS2)</text>
<line x1="294" y1="113" x2="294" y2="127" stroke="#ffffff" stroke-width="4"/>
<text class="ts" x="294" y="168" text-anchor="middle" fill="#B45309">✂ PMS2 nicks the new strand only</text>
</g>
<g id="exo1" class="reveal">
<path d="M441 120 A10 10 0 1 1 437.1 112.1 L431 120 L437.1 127.9 A10 10 0 0 1 441 120" fill="#FDBA74" stroke="#C2410C" stroke-width="1.2" transform="translate(-2 0)"/>
<text class="ts" x="440" y="150" text-anchor="middle" font-weight="600" fill="#C2410C">EXO1</text>
<text class="ts" x="320" y="150" text-anchor="middle" fill="#15803D" font-weight="600">RPA coats the template</text>
<path d="M240 136 L400 136" stroke="#C2410C" stroke-width="1.2" stroke-dasharray="3 3" marker-end="url(#arrowMT)"/>
<ellipse cx="220" cy="106" rx="5" ry="3.2" fill="#16A34A"/>
<ellipse cx="236" cy="106" rx="5" ry="3.2" fill="#16A34A"/>
<ellipse cx="252" cy="106" rx="5" ry="3.2" fill="#16A34A"/>
<ellipse cx="268" cy="106" rx="5" ry="3.2" fill="#16A34A"/>
<ellipse cx="284" cy="106" rx="5" ry="3.2" fill="#16A34A"/>
<ellipse cx="300" cy="106" rx="5" ry="3.2" fill="#16A34A"/>
<ellipse cx="316" cy="106" rx="5" ry="3.2" fill="#16A34A"/>
<ellipse cx="332" cy="106" rx="5" ry="3.2" fill="#16A34A"/>
<ellipse cx="348" cy="106" rx="5" ry="3.2" fill="#16A34A"/>
<ellipse cx="364" cy="106" rx="5" ry="3.2" fill="#16A34A"/>
<ellipse cx="380" cy="106" rx="5" ry="3.2" fill="#16A34A"/>
<ellipse cx="396" cy="106" rx="5" ry="3.2" fill="#16A34A"/>
<ellipse cx="412" cy="106" rx="5" ry="3.2" fill="#16A34A"/>
</g>
<g id="polD" class="reveal">
<circle cx="420" cy="120" r="9" class="c-teal"/>
<ellipse cx="420" cy="110" rx="6" ry="20" fill="none" stroke="#0F6E56" stroke-width="2"/>
<path d="M432 113 l6 7 l-6 7 l-6 -7 z" fill="#EF9F27" stroke="#B45309" stroke-width="1"/>
<text class="ts" x="420" y="150" text-anchor="middle" font-weight="600" fill="#0F6E56">Pol δ + PCNA fill · ligase I seals</text>
<text class="ts" x="400" y="72" text-anchor="middle" font-weight="600" fill="#15803D">C·G — corrected</text>
</g>

<defs><marker id="arrowMT" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>

<!-- step 5: what happens without mismatch repair -->
<g id="msiT" class="reveal">
<line x1="40" y1="200" x2="290" y2="200" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<line x1="40" y1="220" x2="160" y2="220" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
<path d="M160 220 Q172 252 184 220" fill="none" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
<line x1="184" y1="220" x2="290" y2="220" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
<text class="ts" x="165" y="190" text-anchor="middle" font-family="monospace" letter-spacing="2">CACACACACACA</text>
<text class="ts" x="196" y="250" font-weight="600" fill="#B91C1C">extra "CA" repeat</text>
<text class="ts" x="196" y="264">(slippage loop) not repaired</text>
<text class="ts" x="360" y="194" font-weight="600">Lynch syndrome</text>
<text class="ts" x="360" y="210">Inherited loss of MLH1, MSH2, MSH6 or PMS2</text>
<text class="ts" x="360" y="226">→ repeat-slippage errors pile up</text>
<text class="ts" x="360" y="242">→ <tspan font-weight="600">microsatellite instability (MSI)</tspan></text>
<text class="ts" x="360" y="258">→ colorectal &amp; endometrial cancer</text>
<text class="ts" x="360" y="278">MSI-high tumours carry many neoantigens</text>
<text class="ts" x="360" y="294">→ respond well to <tspan font-weight="600">PD-1 checkpoint inhibitors</tspan></text>
</g>

<g id="noteMT0" class="reveal">
<text class="ts" x="30" y="200">After replication a G·T mismatch sits in the new strand. The new strand is recognisable:</text>
<text class="ts" x="30" y="216">it still has a <tspan font-weight="600">nick</tspan> (an Okazaki-fragment end), and <tspan fill="#0F6E56" font-weight="600">PCNA</tspan> stays loaded there.</text>
</g>
<g id="noteMT1" class="reveal">
<text class="ts" x="30" y="200"><tspan fill="#6D28D9" font-weight="600">MutSα (MSH2–MSH6)</tspan> clamps onto the mismatch; binding ATP turns it into a</text>
<text class="ts" x="30" y="216">sliding clamp that can move along the DNA.</text>
</g>
<g id="noteMT2" class="reveal">
<text class="ts" x="30" y="200">MutSα recruits <tspan fill="#B45309" font-weight="600">MutLα (MLH1–PMS2)</tspan>. PCNA, oriented by the existing nick, activates PMS2's</text>
<text class="ts" x="30" y="216">endonuclease so <tspan font-weight="600">only the new strand</tspan> is cut.</text>
<text class="ts" x="30" y="236" fill="var(--text-secondary)">In E. coli, MutH does this: it nicks the new strand at GATC sites that are not yet methylated (Dam).</text>
</g>
<g id="noteMT3" class="reveal">
<text class="ts" x="30" y="200"><tspan fill="#C2410C" font-weight="600">EXO1</tspan> removes the new strand from the nick, past the mismatch;</text>
<text class="ts" x="30" y="216"><tspan fill="#15803D" font-weight="600">RPA</tspan> protects the exposed single-stranded template.</text>
</g>
<g id="noteMT4" class="reveal">
<text class="ts" x="30" y="200"><tspan fill="#0F6E56" font-weight="600">Pol δ</tspan> (with PCNA) refills the gap from the template — now C pairs with G — and</text>
<text class="ts" x="30" y="216"><tspan fill="#B45309" font-weight="600">DNA ligase I</tspan> seals it. Mismatch repair makes replication ~100–1000× more accurate.</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 5</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 5 — a G·T mismatch in the new strand; a nick and loaded PCNA mark which strand is new",
  "Step 1 of 5 — MutSα (MSH2–MSH6) clamps the mismatch and, with ATP, becomes a sliding clamp",
  "Step 2 of 5 — MutLα (MLH1–PMS2) joins; PCNA activates PMS2 to nick only the new strand (E. coli: MutH at unmethylated GATC)",
  "Step 3 of 5 — EXO1 excises the new strand past the mismatch while RPA protects the template",
  "Step 4 of 5 — Pol δ with PCNA resynthesises the gap (C now pairs with G) and DNA ligase I seals it",
  "Step 5 of 5 — without mismatch repair (Lynch syndrome), repeat-slippage errors persist: microsatellite instability and cancer risk"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  const on = (id, v) => document.getElementById(id).classList.toggle('on', v);
  on('mmLbl', step === 0); on('nickLbl', step === 0);
  on('pcna', step <= 2);
  on('mutSg', step === 1 || step === 2);
  document.querySelector('svg').classList.toggle('slide', step === 2);   // the clamp slides along the DNA
  document.getElementById('atpLbl').style.opacity = step === 1 ? '1' : '0';
  on('mutLg', step === 2);
  on('exo1', step === 3);
  on('polD', step === 4);
  on('msiT', step === 5);
  document.getElementById('newExcised').style.opacity = step >= 3 ? '0' : '1';
  document.getElementById('mmDot').style.opacity = step >= 3 ? '0' : '1';
  document.getElementById('newFill').style.opacity = step >= 4 ? '1' : '0';
  document.getElementById('okPair').style.opacity = step >= 4 ? '1' : '0';
  document.getElementById('newLblT').textContent = step >= 4 ? 'New strand (corrected)' : 'New strand';
  for (let k = 0; k <= 4; k++) on('noteMT' + k, k === step);
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''



# ---------------------------------------------------------------------------
# CRISPR_CAS9_GENERAL  (source: crispr_cas9.html)
# ---------------------------------------------------------------------------
CRISPR_CAS9_GENERAL = '''
<h2 class="sr-only">Interactive diagram of CRISPR-Cas9 gene editing: a guide RNA directs Cas9 to a target DNA sequence, Cas9 cuts both strands, and the cell repairs the break either by NHEJ or by homology-directed repair with a donor template.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }   /* faint previews keep their shape, not their overlapping captions */
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #cas9Group { transition: transform 1s ease; }
  #gRNA, #topL { transition: d .8s ease; }
  #dnaL, #dnaR { transition: transform .6s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>CRISPR-Cas9 gene editing, general view</title>
<desc>A guide RNA loaded into Cas9 protein scans DNA for a matching sequence next to a PAM site, base-pairs with the target strand to confirm the match, and Cas9 cuts both DNA strands. The cell then repairs the break either through error-prone non-homologous end joining, which disrupts the gene, or through homology-directed repair using a donor template, which precisely edits the sequence.</desc>

<!-- DNA drawn in two halves so the ends can part at the double-strand break (x = 370, 3 bp upstream of the PAM) -->
<g id="dnaL">
<path id="topL" d="M30 150 L290 150 Q330 150 370 150" fill="none" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<line x1="30" y1="170" x2="370" y2="170" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
</g>
<g id="dnaR">
<line x1="370" y1="150" x2="650" y2="150" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<line x1="370" y1="170" x2="650" y2="170" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
<rect x="375" y="145" width="30" height="10" fill="#EF9F27"/>
<text class="ts" x="410" y="140">PAM</text>
</g>

<g id="basePairing" class="stg">
<line x1="295" y1="163" x2="295" y2="169" stroke="#639922" stroke-width="1.5"/>
<line x1="307" y1="163" x2="307" y2="169" stroke="#639922" stroke-width="1.5"/>
<line x1="319" y1="163" x2="319" y2="169" stroke="#639922" stroke-width="1.5"/>
<line x1="331" y1="163" x2="331" y2="169" stroke="#639922" stroke-width="1.5"/>
<line x1="343" y1="163" x2="343" y2="169" stroke="#639922" stroke-width="1.5"/>
<line x1="355" y1="163" x2="355" y2="169" stroke="#639922" stroke-width="1.5"/>
<line x1="365" y1="163" x2="365" y2="169" stroke="#639922" stroke-width="1.5"/>
<text class="ts" x="220" y="200" text-anchor="middle">gRNA base-pairs — match confirmed</text>
</g>

<g id="cas9Group">
<ellipse cx="340" cy="95" rx="62" ry="28" class="c-purple"/>
<text class="th" x="340" y="88" text-anchor="middle" dominant-baseline="central">Cas9</text>
<path id="gRNA" d="M285 115 L370 115 L388 100" fill="none" stroke="#639922" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
</g>

<g id="grna" class="stg">
<text class="ts" x="150" y="52" text-anchor="middle">Guide RNA finds matching sequence</text>
</g>

<g id="cut" class="stg">
<path d="M372 140 L364 152 L376 158 L368 180" fill="none" stroke="#E24B4A" stroke-width="2.5" stroke-linejoin="round"/>
<text class="ts" x="370" y="203" text-anchor="middle">Double-strand break</text>
</g>

<g id="nhej" class="stg">
<text class="ts" x="180" y="226" text-anchor="middle">NHEJ — error-prone, disrupts gene</text>
<line x1="70" y1="242" x2="290" y2="242" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<line x1="70" y1="254" x2="290" y2="254" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
<rect x="174" y="238" width="12" height="20" rx="2" fill="#E24B4A"/>
<text class="ts" x="180" y="278" text-anchor="middle">ends rejoined with a small indel</text>
</g>

<g id="hdr" class="stg">
<text class="ts" x="500" y="222" text-anchor="middle">HDR — donor template, precise edit</text>
<line x1="440" y1="234" x2="480" y2="234" stroke="#888780" stroke-width="2" stroke-linecap="round"/>
<rect x="480" y="230" width="40" height="8" rx="2" fill="#1D9E75"/>
<line x1="520" y1="234" x2="560" y2="234" stroke="#888780" stroke-width="2" stroke-linecap="round"/>
<line x1="390" y1="248" x2="610" y2="248" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<line x1="390" y1="260" x2="610" y2="260" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
<rect x="480" y="244" width="40" height="20" rx="2" fill="#1D9E75"/>
<text class="ts" x="500" y="282" text-anchor="middle">new sequence copied in from the donor</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — guide RNA loaded into Cas9 scans DNA for a matching sequence near a PAM site",
  "Step 1 of 4 — Cas9-gRNA complex docks near the PAM sequence",
  "Step 2 of 4 — the guide RNA base-pairs with the target DNA strand, confirming the match",
  "Step 3 of 4 — Cas9 cuts both DNA strands at the target site",
  "Step 4 of 4 — the cell repairs the break: NHEJ disrupts the gene, or HDR with a donor template precisely edits it"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  const paired = step === 2 || step === 3;          // gRNA leaves Cas9's groove and pairs with the target strand
  const cas = document.getElementById('cas9Group');
  cas.style.transform = step === 0 ? 'translateX(-190px)' : step >= 4 ? 'translateX(230px)' : 'none';
  const g = paired ? "M285 162 L370 162 L388 100" : "M285 115 L370 115 L388 100";
  const t = paired ? "M30 150 L290 150 Q330 114 370 150" : "M30 150 L290 150 Q330 150 370 150";
  const gEl = document.getElementById('gRNA'), tEl = document.getElementById('topL');
  gEl.setAttribute('d', g); gEl.style.d = 'path("' + g + '")';
  tEl.setAttribute('d', t); tEl.style.d = 'path("' + t + '")';
  document.getElementById('dnaL').style.transform = step >= 3 ? 'translateX(-8px)' : 'none';
  document.getElementById('dnaR').style.transform = step >= 3 ? 'translateX(8px)' : 'none';
  document.getElementById('grna').classList.toggle('on', step === 0);
  document.getElementById('basePairing').classList.toggle('on', step >= 2 && step < 3);
  document.getElementById('cut').classList.toggle('on', step >= 3);
  document.getElementById('nhej').classList.toggle('on', step >= 4);
  document.getElementById('hdr').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# LAC_OPERON_GENERAL  (source: lac_operon.html)
# ---------------------------------------------------------------------------
LAC_OPERON_GENERAL = '''
<h2 class="sr-only">Interactive diagram of the lac operon: a switchable comparison between lactose absent, where a repressor blocks transcription, and lactose present, where the repressor is removed and the genes are transcribed.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #repressor { transition: transform 0.8s ease, opacity 0.5s ease, fill .5s ease; transform-box: fill-box; transform-origin: center; }
  .induced #repressor { transform: translateY(-4px) scale(1.15, 0.8); }          /* inducer bound: shape change loosens its grip */
  .removed #repressor { transform: translateY(-40px) scale(1.15, 0.8); opacity: 0; }
  #lactoseMol { transition: transform 0.8s ease, opacity 0.5s ease; }
  .induced #lactoseMol { transform: translateY(42px); }                          /* lactose lands on the repressor */
  .removed #lactoseMol { transform: translateY(2px); opacity: 0; }               /* ...and leaves with it */
  #mrnaLac { transition: stroke-dashoffset 1s ease, opacity .5s ease; }
  #blockMark { transition: opacity .4s ease; }
  .tryBind #rnaPol { transform: translateX(22px); }                               /* polymerase pushes up to the repressor */
  #rnaPol { transition: transform 1s ease, opacity 0.5s ease; }
  .transcribing #rnaPol { transform: translateX(200px); }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnAbsent" onclick="setMode('absent')">Lactose absent</button>
  <button id="btnPresent" onclick="setMode('present')">Lactose present</button>
</div>

<svg width="100%" viewBox="0 0 680 260" role="img">
<title>The lac operon</title>
<desc>When lactose is absent, a repressor protein binds the operator, physically blocking RNA polymerase from transcribing the lac genes, so no lactose-digesting enzymes are made. When lactose is present, it binds the repressor, changing its shape so it falls off the operator, freeing RNA polymerase to transcribe the genes and produce the enzymes needed to digest lactose.</desc>

<line x1="30" y1="150" x2="650" y2="150" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<rect x="150" y="140" width="50" height="20" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="175" y="130" text-anchor="middle">Promoter</text>
<rect x="210" y="140" width="50" height="20" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="235" y="130" text-anchor="middle">Operator</text>
<rect x="270" y="140" width="300" height="20" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="420" y="185" text-anchor="middle">lac genes (lacZ, lacY, lacA)</text>

<circle id="repressor" cx="235" cy="150" r="14" class="c-red"/>
<text class="ts" x="235" y="105" text-anchor="middle" id="repressorLabel">Repressor bound</text>

<g id="lactoseMol" class="stg">
<circle cx="235" cy="90" r="7" fill="#EF9F27"/>
<text class="ts" x="235" y="33" text-anchor="middle">Lactose binds repressor</text>
</g>

<path id="mrnaLac" d="M215 116 L375 116" stroke="#1D9E75" stroke-width="3" stroke-linecap="round" pathLength="100" stroke-dasharray="100 100" stroke-dashoffset="100" style="opacity:0"/>
<circle id="rnaPol" cx="175" cy="150" r="12" class="c-teal"/>
<g id="blockMark" style="opacity:0">
<path d="M212 134 l10 10 M222 134 l-10 10" stroke="#B91C1C" stroke-width="2.5" stroke-linecap="round"/>
<text class="ts" x="160" y="186" text-anchor="middle" font-weight="600" fill="#B91C1C">RNA polymerase blocked</text>
</g>

<g id="mrnaOut" class="stg">
<text class="th" x="420" y="220" text-anchor="middle">Genes transcribed — enzymes made</text>
<text class="ts" x="300" y="108" text-anchor="middle" fill="#15803D">mRNA</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0</span>
</div>

<script>
let step = 0;
let mode = 'absent';
const configAbsent = {
  repressorLabel: 'Repressor bound to operator',
  labels: [
    'Step 0 of 1 — no lactose present, repressor sits on the operator',
    'Step 1 of 1 — RNA polymerase is blocked — genes stay OFF, no enzymes made'
  ]
};
const configPresent = {
  repressorLabel: '',
  labels: [
    'Step 0 of 2 — lactose is present',
    'Step 1 of 2 — lactose (as its isomer allolactose) binds the repressor, changing its shape so it loosens its grip on the operator',
    'Step 2 of 2 — RNA polymerase transcribes the genes — enzymes made to digest lactose'
  ]
};
function maxStep() { return mode === 'absent' ? 1 : 2; }
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnAbsent').classList.toggle('active', m === 'absent');
  document.getElementById('btnPresent').classList.toggle('active', m === 'present');
  render();
}
function render() {
  const cfg = mode === 'absent' ? configAbsent : configPresent;
  document.getElementById('stepLabel').textContent = cfg.labels[step];
  document.getElementById('lactoseMol').classList.toggle('on', mode === 'present' && step >= 1);
  document.getElementById('lactoseMol').style.display = mode === 'present' ? '' : 'none';
  const svg = document.querySelector('svg');
  svg.classList.toggle('induced', mode === 'present' && step === 1);
  svg.classList.toggle('removed', mode === 'present' && step >= 2);
  svg.classList.toggle('transcribing', mode === 'present' && step >= 2);
  svg.classList.toggle('tryBind', mode === 'absent' && step >= 1);
  document.getElementById('blockMark').style.opacity = mode === 'absent' && step >= 1 ? '1' : '0';
  document.getElementById('repressorLabel').textContent =
    mode === 'absent' ? cfg.repressorLabel : (step === 0 ? 'Repressor bound to operator' : step === 1 ? 'Repressor changes shape' : '');
  const m = document.getElementById('mrnaLac');
  const tx = mode === 'present' && step >= 2;
  m.style.opacity = tx ? '1' : '0'; m.style.strokeDashoffset = tx ? '0' : '100';   // mRNA grows behind the polymerase
  document.getElementById('mrnaOut').classList.toggle('on', mode === 'present' && step >= 2);
}
function stepFwd() { if (step < maxStep()) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('absent');
</script>
'''


# ---------------------------------------------------------------------------
# RNA_INTERFERENCE_GENERAL  (source: rna_interference.html)
# ---------------------------------------------------------------------------
RNA_INTERFERENCE_GENERAL = '''
<h2 class="sr-only">Interactive diagram of RNA interference: Dicer cleaves double-stranded RNA into siRNA, the guide strand loads into RISC, and RISC cleaves the complementary target mRNA, silencing the gene.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #riscGroup { transition: transform 1s ease; }
  .docked #riscGroup { transform: translateX(270px); }   /* RISC centre 140 -> 410: guide strand lies on the target */
  #targetMrna, #targetMrnaR { transition: opacity 0.6s ease, transform .8s ease; }
  .cut #targetMrna { transform: translateX(-10px); opacity: .35; }
  .cut #targetMrnaR { transform: translateX(10px); opacity: .35; }
  #dsTop, #dsBot { transition: stroke-dasharray .6s ease; }
  #passenger { transition: transform 1s ease, opacity .8s ease; }
  .loaded #passenger { transform: translate(-50px, 40px); opacity: .7; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 280" role="img">
<title>RNA interference, general view</title>
<desc>Double-stranded RNA is cleaved by the enzyme Dicer into short interfering RNA fragments. One strand is loaded into the RNA-induced silencing complex, RISC, as a guide. The RISC-siRNA complex scans mRNA molecules in the cell, and when the guide strand base-pairs with a complementary target mRNA, RISC cleaves it, degrading the message and silencing that gene.</desc>

<path id="dsTop" d="M100 100 L180 100" stroke="#378ADD" stroke-width="4" stroke-linecap="butt"/>
<path id="dsBot" d="M100 115 L180 115" stroke="#D85A30" stroke-width="4" stroke-linecap="butt"/>
<text class="ts" x="140" y="85" text-anchor="middle" id="dsLabel">Double-stranded RNA</text>
<g id="passengerG" style="opacity:0;transition:opacity .4s ease">
<path id="passenger" d="M120 168 L160 168" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<text class="ts" x="60" y="226" id="passengerLbl">passenger strand discarded</text>
</g>

<g id="dicer" class="stg">
<circle cx="198" cy="107" r="14" class="c-amber pulse"/>
<text class="ts" x="140" y="140" text-anchor="middle">Dicer cleaves into siRNA</text>
</g>

<g id="riscGroup">
<ellipse cx="140" cy="180" rx="30" ry="22" class="c-purple stg" id="risc"/>
<text class="ts" x="140" y="180" text-anchor="middle" dominant-baseline="central" id="riscLabel"></text>
<path id="guideStrand" d="M120 175 L160 175" stroke="#D85A30" stroke-width="3" stroke-linecap="round" opacity="0"/>
</g>

<line x1="300" y1="180" x2="410" y2="180" id="targetMrna" stroke="#1D9E75" stroke-width="3" stroke-linecap="round"/>
<line x1="410" y1="180" x2="600" y2="180" id="targetMrnaR" stroke="#1D9E75" stroke-width="3" stroke-linecap="round"/>
<text class="ts" x="560" y="200" text-anchor="middle">Target mRNA</text>

<g id="basePairing" class="stg">
<text class="ts" x="410" y="150" text-anchor="middle">Guide strand base-pairs with target</text>
</g>

<g id="cleavage" class="stg">
<path d="M410 166 L410 194" stroke="#E24B4A" stroke-width="2.5" stroke-linecap="round"/>
<text class="th" x="450" y="230" text-anchor="middle">mRNA cleaved — gene silenced</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — double-stranded RNA present in the cell",
  "Step 1 of 4 — Dicer cleaves it into short interfering RNA (siRNA) fragments",
  "Step 2 of 4 — one strand loads into RISC as a guide",
  "Step 3 of 4 — the RISC-siRNA complex finds and base-pairs with a complementary target mRNA",
  "Step 4 of 4 — RISC cleaves the target mRNA — the gene is silenced, no protein made"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('dicer').classList.toggle('on', step >= 1);
  document.getElementById('risc').classList.toggle('on', step >= 2);
  document.getElementById('guideStrand').setAttribute('opacity', step >= 2 ? '1' : '0');
  document.querySelector('svg').classList.toggle('docked', step >= 3);
  document.getElementById('basePairing').classList.toggle('on', step === 3);
  document.getElementById('cleavage').classList.toggle('on', step >= 4);
  const svg = document.querySelector('svg');
  svg.classList.toggle('cut', step >= 4);                                     // mRNA cut in two at the guide's centre, then degraded
  // Dicer chops the long dsRNA into short ~21-nt siRNA duplexes
  document.getElementById('dsTop').style.strokeDasharray = step >= 1 ? '24 4' : 'none';
  document.getElementById('dsBot').style.strokeDasharray = step >= 1 ? '24 4' : 'none';
  document.getElementById('dsLabel').textContent = step >= 1 ? 'siRNA pieces (~21 nt each)' : 'Double-stranded RNA';
  // only the guide strand stays in RISC; the passenger strand is thrown out
  document.getElementById('passengerG').style.opacity = step === 2 ? '1' : '0';
  svg.classList.toggle('loaded', step >= 2);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# SYNAPSE_TYPES_TECHNICAL  (source: synapse_types.html)
# ---------------------------------------------------------------------------
SYNAPSE_TYPES_TECHNICAL = '''
<h2 class="sr-only">Technical diagram comparing chemical and electrical synapses: chemical synapses use neurotransmitter release and clearance with a delay, while electrical synapses connect cells directly through gap junctions with almost no delay but no modifiability.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .hide { display: none; }
  #postCell { transition: transform .8s ease; }
  .nt, .ion { transition: transform .9s ease, opacity .6s ease; }
  .rcp { transition: fill .4s ease; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnChemical" onclick="setMode('chemical')">Chemical synapse</button>
  <button id="btnElectrical" onclick="setMode('electrical')">Electrical synapse</button>
</div>

<svg width="100%" viewBox="0 0 680 280" role="img">
<title>Chemical vs electrical synapses</title>
<desc>A chemical synapse releases neurotransmitter across a gap, which binds receptors and is then cleared by reuptake or enzymatic degradation, taking one to five milliseconds but allowing the connection strength to be modified. An electrical synapse connects two cells directly through gap junction channels called connexons, letting ions flow straight through with almost no delay, but the connection strength cannot be adjusted.</desc>

<rect x="80" y="80" width="180" height="120" rx="12" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="170" y="70" text-anchor="middle">Presynaptic cell</text>
<g id="apNote" class="stg"><text class="ts" x="130" y="145" text-anchor="middle">AP →</text></g>

<!-- postsynaptic cell slides close for the electrical synapse: 20 nm cleft vs 3.5 nm gap junction -->
<g id="postCell">
<rect x="350" y="80" width="180" height="120" rx="12" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="440" y="70" text-anchor="middle">Postsynaptic cell</text>
<g id="postResp" class="stg"><text class="ts" x="450" y="145" text-anchor="middle">depolarizes ✦</text></g>
</g>

<g id="chemGap">
<text class="ts" x="305" y="70" text-anchor="middle">Synaptic cleft (20 nm)</text>
<circle cx="236" cy="118" r="12" fill="none" stroke="#7F77DD" stroke-width="2"/>
<circle cx="236" cy="162" r="12" fill="none" stroke="#7F77DD" stroke-width="2"/>
<circle class="nt" cx="250" cy="115" r="5" fill="#7F77DD"/>
<circle class="nt" cx="250" cy="140" r="5" fill="#7F77DD"/>
<circle class="nt" cx="250" cy="165" r="5" fill="#7F77DD"/>
<rect class="rcp" x="350" y="107" width="8" height="16" rx="2" fill="none" stroke="#EF9F27" stroke-width="2"/>
<rect class="rcp" x="350" y="132" width="8" height="16" rx="2" fill="none" stroke="#EF9F27" stroke-width="2"/>
<rect class="rcp" x="350" y="157" width="8" height="16" rx="2" fill="none" stroke="#EF9F27" stroke-width="2"/>
<text class="ts" x="365" y="100">Receptor</text>
<g id="clearNote" class="stg"><text class="ts" x="305" y="222" text-anchor="middle">Cleared by reuptake / degradation</text></g>
</g>

<g id="elecGap">
<rect x="250" y="108" width="32" height="12" rx="3" fill="#1D9E75"/>
<rect x="250" y="134" width="32" height="12" rx="3" fill="#1D9E75"/>
<rect x="250" y="160" width="32" height="12" rx="3" fill="#1D9E75"/>
<circle class="ion" cx="232" cy="114" r="4" fill="#E1F5EE" stroke="#0F6E56"/>
<circle class="ion" cx="232" cy="140" r="4" fill="#E1F5EE" stroke="#0F6E56"/>
<circle class="ion" cx="232" cy="166" r="4" fill="#E1F5EE" stroke="#0F6E56"/>
<text class="ts" x="266" y="222" text-anchor="middle">Gap junction (3.5 nm) — Connexons span both membranes</text>
</g>

<g id="delayNote" class="stg">
<text class="th" x="340" y="258" text-anchor="middle" id="delayLabel"></text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 3</span>
</div>

<script>
let step = 0;
let mode = 'chemical';
const chemical = {
  labels: [
    "Step 0 of 3 — presynaptic action potential triggers neurotransmitter release",
    "Step 1 of 3 — neurotransmitter diffuses across the cleft and binds receptors",
    "Step 2 of 3 — postsynaptic response triggered (delay: ~1-5 ms)",
    "Step 3 of 3 — neurotransmitter cleared by reuptake or enzymatic degradation — synapse resets, and its strength CAN be modified (basis of plasticity)"
  ]
};
const electrical = {
  labels: [
    "Step 0 of 3 — presynaptic cell depolarizes",
    "Step 1 of 3 — ions flow directly through connexon channels — no neurotransmitter involved",
    "Step 2 of 3 — postsynaptic cell depolarizes almost instantly (delay: ~0.1 ms)",
    "Step 3 of 3 — connection is fast and often bidirectional, but its strength generally CANNOT be modified"
  ]
};
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnChemical').classList.toggle('active', m === 'chemical');
  document.getElementById('btnElectrical').classList.toggle('active', m === 'electrical');
  document.getElementById('chemGap').classList.toggle('hide', m !== 'chemical');
  document.getElementById('elecGap').classList.toggle('hide', m !== 'electrical');
  document.getElementById('postCell').style.transform = m === 'electrical' ? 'translateX(-78px)' : 'none';
  render();
}
function render() {
  const cfg = mode === 'chemical' ? chemical : electrical;
  document.getElementById('stepLabel').textContent = cfg.labels[step];
  document.getElementById('apNote').classList.toggle('on', step === 0);
  document.getElementById('postResp').classList.toggle('on', step >= 2);
  // chemical: released (0) -> bound to receptors (1, 2) -> taken back up / degraded (3)
  const ntX = [0, 92, 92, 0][step];
  document.querySelectorAll('#chemGap .nt').forEach(c => { c.style.transform = `translateX(${ntX}px)`; c.style.opacity = step === 3 ? 0.3 : 1; });
  document.querySelectorAll('#chemGap .rcp').forEach(r => r.setAttribute('fill', step === 1 || step === 2 ? '#EF9F27' : 'none'));
  document.getElementById('clearNote').classList.toggle('on', step === 3);
  // electrical: ions pass straight through the connexons; at step 3 one flows back (bidirectional)
  const ionX = [[0, 0, 0], [34, 34, 34], [68, 68, 68], [68, 0, 68]][step];
  document.querySelectorAll('#elecGap .ion').forEach((c, i) => c.style.transform = `translateX(${ionX[i]}px)`);
  document.getElementById('delayNote').classList.toggle('on', step === 3);
  document.getElementById('delayLabel').textContent = step === 3 ? cfg.labels[3].split('— ')[1] : '';
}
function stepFwd() { if (step < 3) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('chemical');
</script>
'''


# ---------------------------------------------------------------------------
# SYNAPTIC_PLASTICITY_LTP_GENERAL  (source: ltp.html)
# ---------------------------------------------------------------------------
SYNAPTIC_PLASTICITY_LTP_GENERAL = '''
<h2 class="sr-only">Interactive diagram of long-term potentiation: the NMDA receptor acts as a coincidence detector, requiring both glutamate binding and postsynaptic depolarization to open, and its resulting calcium influx drives insertion of new AMPA receptors, strengthening the synapse.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #mgBlock { transition: transform 0.8s ease, opacity 0.5s ease; }
  .expelled #mgBlock { transform: translateY(-30px); opacity: 0; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Long-term potentiation, general view</title>
<desc>The NMDA receptor requires two simultaneous conditions to open: glutamate must be bound, and the postsynaptic membrane must already be depolarized enough to expel a blocking magnesium ion, making it a coincidence detector. When both conditions are met, calcium flows in and triggers a signaling cascade that inserts new AMPA receptors into the postsynaptic membrane, strengthening the synapse so future signals produce a larger response — the cellular basis of learning and memory.</desc>

<rect x="30" y="60" width="620" height="20" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="60" y="50">Presynaptic terminal</text>

<text class="ts" x="210" y="98" text-anchor="middle" id="glutamateLabel">Glutamate released</text>
<path d="M210 104 L210 128" stroke="#7F77DD" stroke-width="1.5" fill="none" marker-end="url(#ltpArrow)"/>
<defs><marker id="ltpArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#7F77DD" stroke-width="1.5"/></marker></defs>

<rect x="80" y="140" width="570" height="120" rx="8" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="640" y="250" text-anchor="end">Postsynaptic membrane</text>

<circle cx="220" cy="160" r="14" class="c-purple"/>
<text class="ts" x="220" y="185" text-anchor="middle">NMDA receptor</text>
<circle id="mgBlock" cx="220" cy="150" r="5" fill="#EF9F27"/>
<circle class="stg" id="glutamate1" cx="200" cy="148" r="6" fill="#7F77DD"/>
<circle class="stg" id="glutamate2" cx="240" cy="148" r="6" fill="#7F77DD"/>
<text class="ts" x="250" y="168" id="mgLabel">Mg2+ block</text>

<g id="depol" class="stg">
<text class="ts" x="100" y="250" fill="#D85A30">+ + +  membrane depolarized</text>
</g>

<g id="calcium" class="stg">
<circle cx="212" cy="200" r="4" fill="#B91C1C"/>
<circle cx="228" cy="200" r="4" fill="#B91C1C"/>
<circle cx="220" cy="208" r="4" fill="#B91C1C"/>
<text class="ts" x="220" y="228" text-anchor="middle">Ca2+ influx</text>
</g>

<g id="camkii" class="stg">
<circle cx="320" cy="200" r="10" class="c-amber pulse"/>
<text class="ts" x="320" y="225" text-anchor="middle">CaMKII activated</text>
</g>

<g id="ampaOld" class="c-teal">
<circle cx="450" cy="170" r="10"/>
<text class="ts" x="450" y="195" text-anchor="middle">AMPA receptor</text>
</g>

<g id="ampaNew" class="stg">
<circle cx="500" cy="170" r="10" class="c-teal"/>
<circle cx="550" cy="170" r="10" class="c-teal"/>
<text class="th" x="500" y="128" text-anchor="middle">New AMPA receptors inserted</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — glutamate binds NMDA receptors, but a Mg2+ ion blocks the channel at resting potential",
  "Step 1 of 4 — strong or repeated stimulation depolarizes the membrane enough to expel the Mg2+ block",
  "Step 2 of 4 — with BOTH glutamate bound AND depolarization present, the NMDA receptor opens — Ca2+ flows in (coincidence detection)",
  "Step 3 of 4 — Ca2+ activates CaMKII, triggering a signaling cascade",
  "Step 4 of 4 — new AMPA receptors are inserted into the membrane — the synapse is strengthened (long-term potentiation)"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('glutamate1').classList.toggle('on', step >= 0);
  document.getElementById('glutamate2').classList.toggle('on', step >= 0);
  document.querySelector('svg').classList.toggle('expelled', step >= 1);   // step 1 caption: depolarization expels the Mg2+ block
  document.getElementById('depol').classList.toggle('on', step >= 1);
  document.getElementById('mgLabel').style.opacity = step >= 1 ? '0' : '1';
  document.getElementById('calcium').classList.toggle('on', step >= 2);
  document.getElementById('camkii').classList.toggle('on', step >= 3);
  document.getElementById('ampaNew').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# SYNAPTIC_PLASTICITY_LTP_TECHNICAL
# ---------------------------------------------------------------------------
SYNAPTIC_PLASTICITY_LTP_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of bidirectional synaptic plasticity: strong stimulation gives a large Ca2+ rise that activates CaMKII and strengthens the synapse (early and late LTP), while weak stimulation gives a small Ca2+ rise that activates phosphatases and removes AMPA receptors (LTD).</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .hide { display: none; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #spine, #caFill { transition: x .9s ease, y .9s ease, width .9s ease, height .9s ease; }
  #mg, .ampaMove, .ca { transition: transform .9s ease, opacity .6s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnLtp" onclick="setMode('ltp')">LTP (strengthening)</button>
  <button id="btnLtd" onclick="setMode('ltd')">LTD (weakening)</button>
</div>

<svg width="100%" viewBox="0 0 680 300" role="img">
<title>LTP versus LTD, technical view</title>
<desc>Strong high-frequency stimulation opens NMDA receptors fully and gives a large Ca2+ rise. Ca2+/calmodulin activates CaMKII, which autophosphorylates and stays active, phosphorylates AMPA receptors and drives insertion of more of them (early LTP); repeated stimulation recruits PKA and CREB, new protein synthesis and spine enlargement (late LTP). Weak low-frequency stimulation gives only a small Ca2+ rise, which activates calcineurin and PP1; AMPA receptors are dephosphorylated and removed by endocytosis (LTD).</desc>

<rect x="30" y="40" width="620" height="22" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="40" y="32">Presynaptic terminal</text>

<!-- dendritic spine (postsynaptic); grows in late LTP -->
<rect id="spine" x="80" y="110" width="460" height="150" rx="30" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="530" y="250" text-anchor="end">Dendritic spine</text>

<!-- glutamate in the cleft -->
<circle cx="160" cy="80" r="5" fill="#7F77DD"/>
<circle cx="308" cy="80" r="5" fill="#7F77DD"/>
<circle cx="348" cy="80" r="5" fill="#7F77DD"/>
<text class="ts" x="380" y="84">glutamate</text>

<!-- NMDA receptor with Mg2+ plug -->
<rect x="151" y="97" width="18" height="26" rx="4" class="c-purple"/>
<text class="ts" x="160" y="138" text-anchor="middle">NMDA</text>
<circle id="mg" cx="160" cy="102" r="5" fill="#EF9F27" stroke="#B45309" stroke-width="1"/>
<text class="ts" x="146" y="106" text-anchor="end" id="mgLabel">Mg2+</text>

<!-- AMPA receptors: two present at baseline, two more can be inserted (LTP); one can be removed (LTD) -->
<g id="ampa1"><rect x="300" y="97" width="16" height="26" rx="4" class="c-teal"/>
<g id="p1" class="stg"><circle cx="318" cy="98" r="6" class="c-coral"/><text x="318" y="101" text-anchor="middle" style="font-size:8px;font-weight:600;fill:#7F1D1D">P</text></g></g>
<g id="ampa2" class="ampaMove"><rect x="340" y="97" width="16" height="26" rx="4" class="c-teal"/>
<g id="p2" class="stg"><circle cx="358" cy="98" r="6" class="c-coral"/><text x="358" y="101" text-anchor="middle" style="font-size:8px;font-weight:600;fill:#7F1D1D">P</text></g></g>
<g id="ampaNew3" class="ampaMove" style="opacity:0;transform:translateY(80px)"><rect x="380" y="97" width="16" height="26" rx="4" class="c-teal"/></g>
<g id="ampaNew4" class="ampaMove" style="opacity:0;transform:translateY(80px)"><rect x="420" y="97" width="16" height="26" rx="4" class="c-teal"/></g>
<text class="ts" x="368" y="148" text-anchor="middle" id="ampaLabel">AMPA receptors</text>
<g id="endo" class="stg"><circle cx="348" cy="190" r="20" fill="none" stroke="#64748B" stroke-width="1.5" stroke-dasharray="3 3"/>
<text class="ts" x="376" y="214">endocytosed</text></g>

<!-- depolarization -->
<g id="depol" class="stg"><text class="ts" x="460" y="175" text-anchor="middle" id="depolLabel"></text></g>

<!-- Ca2+ entering through NMDA -->
<circle class="ca" cx="152" cy="160" r="4" fill="#B91C1C"/>
<circle class="ca" cx="168" cy="160" r="4" fill="#B91C1C"/>
<circle class="ca" cx="160" cy="172" r="4" fill="#B91C1C"/>
<circle class="ca" cx="148" cy="184" r="4" fill="#B91C1C"/>
<circle class="ca" cx="172" cy="184" r="4" fill="#B91C1C"/>
<circle class="ca" cx="160" cy="196" r="4" fill="#B91C1C"/>
<g id="caText" class="stg"><text class="ts" x="136" y="180" text-anchor="end">Ca2+</text></g>

<!-- LTP enzyme: CaMKII, autophosphorylated -->
<g id="camkii" class="stg">
<circle cx="250" cy="200" r="15" class="c-amber"/>
<text class="ts" x="250" y="230" text-anchor="middle">CaMKII</text>
<g id="camkiiP" class="stg"><circle cx="263" cy="188" r="6" class="c-coral"/><text x="263" y="191" text-anchor="middle" style="font-size:8px;font-weight:600;fill:#7F1D1D">P</text>
<text class="ts" x="274" y="204">autophosphorylated — stays active</text></g>
</g>

<!-- LTD enzymes: calcineurin -> PP1 -->
<g id="phos" class="stg">
<circle cx="250" cy="200" r="15" class="c-gray"/>
<text class="ts" x="250" y="230" text-anchor="middle">Calcineurin → PP1</text>
</g>

<!-- late LTP -->
<g id="late" class="stg"><text class="ts" x="100" y="278">cAMP → PKA → CREB → new gene expression &amp; protein synthesis · spine enlarges</text></g>

<!-- Ca2+ level gauge: high Ca2+ favours kinases (LTP), low Ca2+ favours phosphatases (LTD) -->
<text class="ts" x="589" y="112" text-anchor="middle">Ca2+</text>
<rect x="582" y="120" width="14" height="130" rx="3" fill="none" stroke="var(--t)" stroke-width="1"/>
<rect id="caFill" x="582" y="250" width="14" height="0" rx="3" fill="#B91C1C" opacity="0.75"/>
<line x1="576" y1="172" x2="602" y2="172" stroke="var(--t)" stroke-width="1" stroke-dasharray="3 2"/>
<text class="ts" x="604" y="150">kinases</text>
<text class="ts" x="604" y="214">phospha-</text>
<text class="ts" x="604" y="227">tases</text>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
let mode = 'ltp';
const ltp = {
  maxStep: 4,
  labels: [
    "Step 0 of 4 — strong, high-frequency stimulation: glutamate binds AMPA and NMDA receptors and AMPA current strongly depolarizes the spine",
    "Step 1 of 4 — depolarization expels Mg2+ from the NMDA channel — a large, fast Ca2+ rise floods the spine (well above the kinase threshold)",
    "Step 2 of 4 — Ca2+/calmodulin activates CaMKII, which autophosphorylates (Thr286) and stays active after Ca2+ falls — a molecular memory switch",
    "Step 3 of 4 — early LTP (minutes to ~1 h): CaMKII phosphorylates AMPA receptors (GluA1 Ser831, more conductance) and drives insertion of extra AMPA receptors",
    "Step 4 of 4 — late LTP (hours and longer): repeated stimulation recruits cAMP/PKA → CREB → new gene expression and protein synthesis; the spine enlarges and the change is stabilized"
  ],
  depol: "+ + +  strong depolarization",
  caLevel: [0, 0.9, 0.65, 0.65, 0.65],   // Ca2+ eases back but stays in the kinase range
  caCount: [0, 6, 6, 6, 6]
};
const ltd = {
  maxStep: 3,
  labels: [
    "Step 0 of 3 — weak, low-frequency stimulation (~1 Hz): glutamate binds, but the spine is only modestly depolarized",
    "Step 1 of 3 — the Mg2+ block is only partly relieved — NMDA receptors let in a small, slow Ca2+ rise (below the kinase threshold)",
    "Step 2 of 3 — low Ca2+ preferentially activates phosphatases: calcineurin (PP2B) activates PP1",
    "Step 3 of 3 — PP1 dephosphorylates AMPA receptors (GluA1 Ser845) and they are removed by clathrin-mediated endocytosis — the synapse weakens (LTD)"
  ],
  depol: "+  weak depolarization",
  caLevel: [0, 0.3, 0.3, 0.25],
  caCount: [0, 2, 2, 2]
};
function cfg() { return mode === 'ltp' ? ltp : ltd; }
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnLtp').classList.toggle('active', m === 'ltp');
  document.getElementById('btnLtd').classList.toggle('active', m === 'ltd');
  document.getElementById('camkii').classList.toggle('hide', m !== 'ltp');
  document.getElementById('late').classList.toggle('hide', m !== 'ltp');
  document.getElementById('phos').classList.toggle('hide', m !== 'ltd');
  document.getElementById('endo').classList.toggle('hide', m !== 'ltd');
  document.getElementById('depolLabel').textContent = cfg().depol;
  render();
}
function setRect(el, x, y, w, h) {
  el.setAttribute('x', x); el.setAttribute('y', y); el.setAttribute('width', w); el.setAttribute('height', h);
  el.style.x = x + 'px'; el.style.y = y + 'px'; el.style.width = w + 'px'; el.style.height = h + 'px';
}
function render() {
  const c = cfg(), L = mode === 'ltp';
  document.getElementById('stepLabel').textContent = c.labels[step];
  document.getElementById('depol').classList.toggle('on', true);
  // Mg2+ plug: fully expelled by strong depolarization, only partly relieved by weak
  const mg = document.getElementById('mg');
  if (step === 0) { mg.style.transform = 'none'; mg.style.opacity = 1; }
  else if (L) { mg.style.transform = 'translateY(-28px)'; mg.style.opacity = 0; }
  else { mg.style.transform = 'translateY(-10px)'; mg.style.opacity = 0.6; }
  document.getElementById('mgLabel').style.opacity = step === 0 || !L ? 1 : 0;
  // Ca2+ entry and gauge
  document.querySelectorAll('.ca').forEach((d, i) => { d.style.opacity = i < c.caCount[step] ? 1 : 0; });
  document.getElementById('caText').classList.toggle('on', step >= 1);
  const h = Math.round(130 * c.caLevel[step]);
  setRect(document.getElementById('caFill'), 582, 250 - h, 14, h);
  // enzymes
  document.getElementById('camkii').classList.toggle('on', L && step >= 2);
  document.getElementById('camkiiP').classList.toggle('on', L && step >= 2);
  document.getElementById('phos').classList.toggle('on', !L && step >= 2);
  // AMPA receptors: baseline phosphorylation shown at rest; LTP adds P + inserts two more; LTD strips P and removes one
  const phos = L ? step >= 3 : step < 3;
  document.getElementById('p1').classList.toggle('on', L ? step >= 3 : step < 3);
  document.getElementById('p2').classList.toggle('on', phos);
  const ins = L && step >= 3;
  ['ampaNew3', 'ampaNew4'].forEach(id => { const g = document.getElementById(id); g.style.opacity = ins ? 1 : 0; g.style.transform = ins ? 'none' : 'translateY(80px)'; });
  const removed = !L && step >= 3;
  const a2 = document.getElementById('ampa2');
  a2.style.transform = removed ? 'translateY(78px)' : 'none';
  a2.style.opacity = removed ? 0.55 : 1;
  document.getElementById('endo').classList.toggle('on', removed);
  // late LTP: spine enlarges
  document.getElementById('late').classList.toggle('on', L && step >= 4);
  const big = L && step >= 4;
  setRect(document.getElementById('spine'), big ? 64 : 80, 110, big ? 496 : 460, big ? 155 : 150);
}
function stepFwd() { if (step < cfg().maxStep) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('ltp');
</script>
'''


# ---------------------------------------------------------------------------
# DOPAMINE_REWARD_PATHWAY_GENERAL  (source: dopamine_reward.html)
# ---------------------------------------------------------------------------
DOPAMINE_REWARD_PATHWAY_GENERAL = '''
<h2 class="sr-only">Interactive diagram of the dopamine reward pathway: a rewarding stimulus activates VTA dopamine neurons, which release dopamine into the nucleus accumbens, reinforcing the behavior, before reuptake ends the signal.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .drift { animation: drift 1.6s ease-in-out infinite; }
  @keyframes drift { 0%{transform:translateX(0)} 100%{transform:translateX(95px)}   /* far enough to reach the nucleus accumbens */ }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 280" role="img">
<title>Dopamine reward pathway, general view</title>
<desc>A rewarding stimulus activates dopamine neurons in the ventral tegmental area, which project to and release dopamine in the nucleus accumbens, producing reinforcement that strengthens the behavior that led to the reward. Dopamine transporters then clear the dopamine from the synapse, ending the signal. Certain drugs of abuse hijack this pathway by blocking those transporters or triggering extra release, producing a much larger and more sustained surge than natural rewards.</desc>

<circle cx="130" cy="150" r="16" fill="#EF9F27" id="stimulus"/>
<text class="ts" x="130" y="120" text-anchor="middle">Rewarding stimulus</text>

<defs><marker id="daArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<g id="activate" class="stg">
<path d="M150 150 L200 150" stroke="#EF9F27" stroke-width="2" fill="none" marker-end="url(#daArrow)"/>
<path d="M296 150 L412 150" stroke="#7F77DD" stroke-width="2" fill="none" marker-end="url(#daArrow)"/>
<text class="ts" x="354" y="188" text-anchor="middle">VTA → NAc projection</text>
</g>
<ellipse id="vtaGlow" cx="250" cy="150" rx="52" ry="42" fill="none" stroke="#EF9F27" stroke-width="2" class="stg"/>
<ellipse cx="250" cy="150" rx="45" ry="35" class="c-purple"/>
<text class="ts" x="250" y="150" text-anchor="middle" dominant-baseline="central">VTA</text>

<g id="dopamineRelease" class="stg">
<circle class="drift" cx="320" cy="140" r="5" fill="#7F77DD"/>
<circle class="drift" cx="320" cy="160" r="5" fill="#7F77DD" style="animation-delay:.3s"/>
<circle class="drift" cx="320" cy="150" r="5" fill="#7F77DD" style="animation-delay:.6s"/>
</g>

<ellipse cx="480" cy="150" rx="64" ry="38" class="c-teal"/>
<text class="ts" x="480" y="150" text-anchor="middle" dominant-baseline="central">Nucleus accumbens</text>

<g id="reinforcement" class="stg">
<text class="th" x="480" y="215" text-anchor="middle">Reward signal — behavior reinforced</text>
</g>

<g id="reuptake" class="stg">
<circle cx="434" cy="121" r="6" fill="#B91C1C"/>
<text class="ts" x="440" y="100" text-anchor="middle">DAT clears dopamine — signal ends</text>
</g>

<g id="hijack" class="stg">
<text class="th" x="400" y="240" text-anchor="middle">Some drugs block DAT or trigger extra release —</text>
<text class="th" x="400" y="258" text-anchor="middle">a much larger, longer surge</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — a rewarding stimulus (food, social contact, etc.) occurs",
  "Step 1 of 4 — dopamine neurons in the ventral tegmental area (VTA) activate",
  "Step 2 of 4 — dopamine is released into the nucleus accumbens",
  "Step 3 of 4 — dopamine signaling produces reinforcement — the behavior that led here gets strengthened",
  "Step 4 of 4 — dopamine transporters (DAT) clear it from the synapse, ending the signal — some drugs of abuse block this step or trigger extra release, producing a much larger surge"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('stimulus').classList.toggle('pulse', step === 0);
  document.getElementById('activate').classList.toggle('on', step >= 1);
  const glow = document.getElementById('vtaGlow');
  glow.classList.toggle('on', step >= 1);
  glow.classList.toggle('pulse', step === 1);   // VTA dopamine neurons firing
  document.getElementById('dopamineRelease').classList.toggle('on', step >= 2 && step < 4);
  document.getElementById('reinforcement').classList.toggle('on', step >= 2 && step < 4);
  document.getElementById('reuptake').classList.toggle('on', step >= 4);
  document.getElementById('hijack').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# MEDICATION_MECHANISM_GENERAL  (source: medication_mechanism.html)
# ---------------------------------------------------------------------------
MEDICATION_MECHANISM_GENERAL = '''
<h2 class="sr-only">Interactive diagram comparing two psychiatric medication mechanisms of action: SSRIs blocking serotonin reuptake, and benzodiazepines acting as positive allosteric modulators of the GABA-A receptor.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .hide { display: none; }
  #drugShape { transition: x .6s ease, y .6s ease; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .drift { animation: drift 1.6s ease-in-out infinite; }
  @keyframes drift { 0%,100%{transform:translateY(0)} 50%{transform:translateY(6px)} }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnSSRI" onclick="setMode('ssri')">SSRI</button>
  <button id="btnBenzo" onclick="setMode('benzo')">Benzodiazepine</button>
</div>

<svg width="100%" viewBox="0 0 680 280" role="img">
<title>Mechanism of action: SSRI vs benzodiazepine</title>
<desc>SSRIs block the serotonin transporter, leaving more serotonin in the synapse to stimulate receptors for longer. Benzodiazepines bind a separate allosteric site on the GABA-A receptor, distinct from where GABA itself binds, increasing how often the receptor's chloride channel opens in response to GABA, enhancing inhibitory signaling.</desc>

<line x1="30" y1="140" x2="650" y2="140" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="3 3"/>
<rect x="60" y="80" width="140" height="120" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="130" y="70" text-anchor="middle">Presynaptic terminal</text>
<rect x="480" y="80" width="140" height="120" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="550" y="70" text-anchor="middle">Postsynaptic membrane</text>

<circle id="transporter" cx="200" cy="150" r="10" class="c-teal"/>
<text class="ts" x="200" y="175" text-anchor="middle" id="transporterLabel">SERT transporter</text>

<defs><marker id="medArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<g id="reuptake" class="stg"><path d="M290 166 L216 160" stroke="#1D9E75" stroke-width="1.5" fill="none" marker-end="url(#medArrow)"/>
<text class="ts" x="300" y="190">reuptake</text></g>
<text class="ts" x="330" y="124" text-anchor="middle" id="ntLabel">serotonin</text>
<g id="extraNT" class="stg">
<circle class="drift" cx="315" cy="168" r="5" fill="#7F77DD"/><circle class="drift" cx="345" cy="128" r="5" fill="#7F77DD" style="animation-delay:.4s"/>
<circle class="drift" cx="380" cy="160" r="5" fill="#7F77DD" style="animation-delay:.2s"/><circle class="drift" cx="410" cy="144" r="5" fill="#7F77DD" style="animation-delay:.5s"/>
<circle class="drift" cx="440" cy="166" r="5" fill="#7F77DD" style="animation-delay:.7s"/>
</g>
<g id="neurotransmitter" class="stg">
<circle class="drift" cx="300" cy="140" r="5" fill="#7F77DD"/>
<circle class="drift" cx="330" cy="150" r="5" fill="#7F77DD" style="animation-delay:.3s"/>
<circle class="drift" cx="360" cy="140" r="5" fill="#7F77DD" style="animation-delay:.6s"/>
</g>

<circle id="receptor" cx="480" cy="150" r="14" class="c-purple"/>
<text class="ts" x="480" y="222" text-anchor="middle" id="receptorLabel">Receptor</text>
<g id="chloride" class="stg"><circle cx="502" cy="182" r="4" fill="#378ADD"/><circle cx="516" cy="194" r="4" fill="#378ADD"/><circle cx="530" cy="180" r="4" fill="#378ADD"/>
<text class="ts" x="540" y="194">Cl− in</text></g>

<g id="drug" class="stg">
<rect x="185" y="130" width="30" height="14" rx="4" class="c-coral" id="drugShape"/>
<text class="ts" x="200" y="115" text-anchor="middle" id="drugLabel">SSRI blocks transporter</text>
</g>

<g id="effect" class="stg">
<text class="th" x="340" y="256" text-anchor="middle" id="effectLabel"></text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 3</span>
</div>

<script>
let step = 0;
let mode = 'ssri';
const ssri = {
  transporterLabel: 'SERT transporter',
  receptorLabel: 'Serotonin receptor',
  drugLabel: 'SSRI blocks the transporter',
  nt: 'serotonin', effect: 'more serotonin signalling, for longer', drugXY: [185, 130], labelX: 200, anchor: 'middle',
  labels: [
    'Step 0 of 3 — normally, serotonin is released, binds its receptor, then SERT clears it away',
    'Step 1 of 3 — an SSRI binds and blocks the SERT transporter',
    'Step 2 of 3 — serotonin can no longer be cleared efficiently, so it stays in the synapse longer',
    'Step 3 of 3 — receptors are stimulated for longer — over weeks this drives downstream adaptations linked to mood effects'
  ]
};
const benzo = {
  transporterLabel: '',
  receptorLabel: 'GABA-A receptor',
  drugLabel: 'Benzodiazepine binds a separate allosteric site',
  nt: 'GABA', effect: 'more Cl− influx → stronger inhibition', drugXY: [484, 122], labelX: 476, anchor: 'end',
  labels: [
    'Step 0 of 3 — normally, GABA binds its receptor, opening a chloride channel — an inhibitory signal',
    'Step 1 of 3 — a benzodiazepine binds a DIFFERENT site on the same receptor, not where GABA binds',
    "Step 2 of 3 — this is positive allosteric modulation — it doesn't activate the receptor alone, but makes it respond more strongly to GABA",
    'Step 3 of 3 — the chloride channel opens more often when GABA is present — enhanced inhibitory signaling (calming, anti-anxiety effect)'
  ]
};
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnSSRI').classList.toggle('active', m === 'ssri');
  document.getElementById('btnBenzo').classList.toggle('active', m === 'benzo');
  const cfg = m === 'ssri' ? ssri : benzo;
  document.getElementById('transporterLabel').textContent = cfg.transporterLabel;
  document.getElementById('receptorLabel').textContent = cfg.receptorLabel;
  document.getElementById('drugLabel').textContent = cfg.drugLabel;
  document.getElementById('transporter').style.opacity = m === 'ssri' ? '1' : '0.12';
  document.getElementById('ntLabel').textContent = cfg.nt;
  // SSRI binds SERT on the presynaptic side; a benzodiazepine binds its own site on the GABA-A receptor
  const d = document.getElementById('drugShape');
  d.setAttribute('x', cfg.drugXY[0]); d.setAttribute('y', cfg.drugXY[1]); d.style.x = cfg.drugXY[0] + 'px'; d.style.y = cfg.drugXY[1] + 'px';
  document.getElementById('drugLabel').setAttribute('x', cfg.labelX);
  document.getElementById('drugLabel').setAttribute('text-anchor', cfg.anchor);
  document.getElementById('drugLabel').setAttribute('y', m === 'benzo' ? 100 : 115);
  document.getElementById('reuptake').classList.toggle('hide', m !== 'ssri');
  document.getElementById('extraNT').classList.toggle('hide', m !== 'ssri');
  document.getElementById('chloride').classList.toggle('hide', m !== 'benzo');
  render();
}
function render() {
  const cfg = mode === 'ssri' ? ssri : benzo;
  document.getElementById('stepLabel').textContent = cfg.labels[step];
  document.getElementById('neurotransmitter').classList.toggle('on', step >= 0);
  document.getElementById('drug').classList.toggle('on', step >= 1);
  document.getElementById('receptor').setAttribute('r', (mode === 'benzo' && step >= 2) ? '18' : '14');
  document.getElementById('effect').classList.toggle('on', step >= 3);
  document.getElementById('effectLabel').textContent = step >= 3 ? cfg.effect : '';
  document.getElementById('reuptake').classList.toggle('on', step === 0);
  document.getElementById('extraNT').classList.toggle('on', step >= 2);
  document.getElementById('chloride').classList.toggle('on', step >= 3);
}
function stepFwd() { if (step < 3) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('ssri');
</script>
'''


# ---------------------------------------------------------------------------
# MEDICATION_MECHANISM_TECHNICAL
# ---------------------------------------------------------------------------
MEDICATION_MECHANISM_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of two drug mechanisms: SSRIs block SERT, but somatodendritic 5-HT1A autoreceptors initially brake raphe firing until they desensitize over weeks; benzodiazepines bind the alpha/gamma-2 interface of the GABA-A receptor and increase opening frequency, unlike barbiturates, which prolong openings, and flumazenil blocks the benzodiazepine site.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .hide { display: none; }
  #auto { transition: opacity .6s ease; }
  #lvl { transition: width .8s ease; }
  .nt { transition: opacity .5s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnSSRI" onclick="setMode('ssri')">SSRI</button>
  <button id="btnBenzo" onclick="setMode('benzo')">Benzodiazepine</button>
</div>

<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Drug mechanisms, technical view: SSRI and benzodiazepine</title>
<desc>SSRI: blocking SERT raises extracellular serotonin, but serotonin around the raphe cell body activates 5-HT1A autoreceptors, which slow firing; over two to six weeks the autoreceptors desensitize, firing recovers and serotonin release stays high. Benzodiazepine: the GABA-A receptor is a pentamer of two alpha, two beta and one gamma-2 subunit; GABA binds at the beta/alpha interfaces and benzodiazepines at the alpha/gamma-2 interface, increasing how often the chloride channel opens, whereas barbiturates prolong each opening; flumazenil competitively blocks the benzodiazepine site.</desc>

<!-- ================= SSRI ================= -->
<g id="vSSRI">
<circle cx="110" cy="140" r="62" fill="var(--surface-1)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="110" y="66" text-anchor="middle">Raphe 5-HT neuron</text>
<text class="ts" x="110" y="222" text-anchor="middle">(cell body)</text>
<rect id="auto" x="150" y="82" width="14" height="22" rx="4" class="c-purple"/>
<text class="ts" x="172" y="84">5-HT1A autoreceptor</text>
<text class="ts" x="172" y="100" id="autoState"></text>
<g id="somaNT" class="stg"><circle cx="180" cy="114" r="4" fill="#7F77DD"/><circle cx="190" cy="124" r="4" fill="#7F77DD"/><circle cx="178" cy="128" r="4" fill="#7F77DD"/></g>

<line x1="172" y1="140" x2="380" y2="140" stroke="var(--t)" stroke-width="2"/>
<g id="ticks"></g>
<text class="ts" x="276" y="172" text-anchor="middle" id="fireText"></text>

<rect x="380" y="90" width="100" height="100" rx="12" fill="var(--surface-1)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="430" y="82" text-anchor="middle">axon terminal</text>
<circle cx="480" cy="160" r="10" class="c-teal"/>
<text class="ts" x="480" y="208" text-anchor="middle">SERT</text>
<g id="ssriDrug" class="stg"><rect x="469" y="144" width="22" height="12" rx="3" class="c-coral"/><text class="ts" x="520" y="132" text-anchor="middle">SSRI</text></g>

<rect x="560" y="80" width="90" height="120" rx="12" fill="var(--surface-1)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="605" y="72" text-anchor="middle">postsynaptic</text>
<circle cx="560" cy="120" r="8" class="c-purple"/>
<circle cx="560" cy="164" r="8" class="c-purple"/>
<g id="cleftNT">
<circle class="nt" cx="500" cy="110" r="4" fill="#7F77DD"/><circle class="nt" cx="520" cy="150" r="4" fill="#7F77DD"/>
<circle class="nt" cx="536" cy="120" r="4" fill="#7F77DD"/><circle class="nt" cx="510" cy="176" r="4" fill="#7F77DD"/>
<circle class="nt" cx="540" cy="168" r="4" fill="#7F77DD"/><circle class="nt" cx="498" cy="134" r="4" fill="#7F77DD"/>
<circle class="nt" cx="528" cy="100" r="4" fill="#7F77DD"/><circle class="nt" cx="544" cy="140" r="4" fill="#7F77DD"/>
</g>

<text class="ts" x="380" y="250">synaptic serotonin</text>
<rect x="380" y="258" width="270" height="14" rx="3" fill="none" stroke="var(--t)" stroke-width="0.75"/>
<rect id="lvl" x="380" y="258" width="90" height="14" rx="3" fill="#7F77DD"/>
<text class="th" x="40" y="300" id="ssriNote"></text>
</g>

<!-- ================= Benzodiazepine ================= -->
<g id="vBenzo" class="hide">
<text class="ts" x="180" y="40" text-anchor="middle">GABA-A receptor (top view)</text>
<g id="ring"></g>
<circle cx="180" cy="175" r="13" fill="var(--surface-1)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="180" y="179" text-anchor="middle" style="font-size:9px">Cl−</text>
<g id="gabaSites"></g>
<text class="ts" x="252" y="96">GABA (β/α)</text>
<text class="ts" x="198" y="282">GABA (β/α)</text>
<g id="bzSite"><rect x="88" y="190" width="18" height="14" rx="3" fill="none" stroke="#D85A30" stroke-width="1.5" stroke-dasharray="2 2"/></g>
<text class="ts" x="40" y="230">BZ site (α/γ2)</text>
<g id="bzDrug" class="stg"><rect x="88" y="190" width="18" height="14" rx="3" class="c-coral"/></g>
<g id="fluma" class="stg"><rect x="86" y="188" width="22" height="18" rx="3" fill="#888780"/><text x="97" y="201" text-anchor="middle" style="font-size:11px;font-weight:700;fill:#fff">✕</text>
<text class="ts" x="40" y="248" style="fill:#B91C1C">flumazenil blocks</text></g>

<text class="ts" x="340" y="64" id="tr0Label">GABA alone</text>
<path id="tr0" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<g id="tr1g" class="stg"><text class="ts" x="340" y="144">+ benzodiazepine: more frequent openings</text>
<path id="tr1" fill="none" stroke="#D85A30" stroke-width="1.5"/></g>
<g id="tr2g" class="stg"><text class="ts" x="340" y="224">+ barbiturate: longer openings</text>
<path id="tr2" fill="none" stroke="#7F77DD" stroke-width="1.5"/></g>
<text class="ts" x="650" y="300" text-anchor="end" style="font-size:10px">single-channel recording · downward = channel open</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
let mode = 'ssri';
const NS = 'http://www.w3.org/2000/svg';
const SSRI = {
  labels: [
    "Step 0 of 4 — baseline: raphe neurons fire steadily; serotonin released at the terminal is cleared by SERT, and somatodendritic 5-HT1A autoreceptors act as a brake on firing",
    "Step 1 of 4 — day 1: the SSRI blocks SERT at the terminals and around the cell body — extracellular serotonin rises",
    "Step 2 of 4 — the extra serotonin around the cell body activates 5-HT1A autoreceptors (Gi → GIRK K+ channels): the neuron fires less, so release falls and the net gain is small",
    "Step 3 of 4 — over 2–6 weeks, continuous stimulation desensitizes and downregulates the 5-HT1A autoreceptors — the brake fades",
    "Step 4 of 4 — firing recovers while SERT stays blocked → sustained higher serotonin release, followed by postsynaptic adaptations (e.g. BDNF) — explaining the delayed benefit and early side effects"
  ],
  ticks: [8, 8, 3, 7, 9],
  fire: ['firing: normal', 'firing: normal', 'firing ↓ (autoreceptor brake)', 'firing recovering', 'firing restored'],
  level: [0.3, 0.6, 0.45, 0.7, 0.85],
  auto: ['', '', 'activated → firing ↓', 'desensitizing', 'desensitized'],
  note: ['', '', 'acute: little net gain', 'weeks…', 'therapeutic effect: weeks, not days']
};
const BENZO = {
  labels: [
    "Step 0 of 4 — the GABA-A receptor is a pentamer (typically 2α, 2β, 1γ2) around a Cl− pore; GABA binds at the two β/α interfaces and opens the channel briefly",
    "Step 1 of 4 — a benzodiazepine binds a separate site at the α/γ2 interface: a positive allosteric modulator that does nothing without GABA",
    "Step 2 of 4 — with the benzodiazepine bound, GABA opens the channel more often → more Cl− influx and hyperpolarization (α1-containing receptors: sedation; α2/α3: anxiolysis)",
    "Step 3 of 4 — barbiturates (a different site) prolong each opening and at high doses open the channel without GABA — no ceiling, so overdose, especially with alcohol, is far more dangerous",
    "Step 4 of 4 — flumazenil is a competitive antagonist at the benzodiazepine site: it reverses benzodiazepine sedation or overdose (but can precipitate withdrawal seizures)"
  ]
};
// GABA-A ring: beta, alpha, beta, alpha, gamma2
(function buildRing() {
  const names = ['β2', 'α1', 'β2', 'α1', 'γ2'], ang = [-90, -18, 54, 126, 198];
  const cls = { 'β2': 'c-teal', 'α1': 'c-purple', 'γ2': 'c-amber' };
  const g = document.getElementById('ring');
  names.forEach((n, i) => {
    const a = ang[i] * Math.PI / 180, x = 180 + 54 * Math.cos(a), y = 175 + 54 * Math.sin(a);
    const c = document.createElementNS(NS, 'circle');
    c.setAttribute('cx', x); c.setAttribute('cy', y); c.setAttribute('r', 26); c.setAttribute('class', cls[n]);
    const t = document.createElementNS(NS, 'text');
    t.setAttribute('x', x); t.setAttribute('y', y + 4); t.setAttribute('text-anchor', 'middle'); t.setAttribute('class', 'ts'); t.textContent = n;
    g.appendChild(c); g.appendChild(t);
  });
  const gs = document.getElementById('gabaSites');
  [-54, 90].forEach(d => {
    const a = d * Math.PI / 180, x = 180 + 86 * Math.cos(a), y = 175 + 86 * Math.sin(a);
    const r = document.createElementNS(NS, 'rect');
    r.setAttribute('x', x - 6); r.setAttribute('y', y - 6); r.setAttribute('width', 12); r.setAttribute('height', 12);
    r.setAttribute('fill', '#7F77DD'); r.setAttribute('transform', `rotate(45 ${x} ${y})`);
    gs.appendChild(r);
  });
})();
function trace(y, opens) {
  let d = `M340 ${y}`, x0 = 340;
  opens.forEach(([s, l]) => { const a = 340 + s, b = a + l; d += ` L${a} ${y} L${a} ${y + 20} L${b} ${y + 20} L${b} ${y}`; });
  return d + ' L650 ' + y;
}
document.getElementById('tr0').setAttribute('d', trace(76, [[30, 8], [120, 8], [220, 8]]));
document.getElementById('tr1').setAttribute('d', trace(156, [[15, 8], [55, 8], [95, 8], [140, 8], [185, 8], [228, 8], [270, 8]]));
document.getElementById('tr2').setAttribute('d', trace(236, [[30, 34], [130, 40], [225, 46]]));
function drawTicks(n) {
  const g = document.getElementById('ticks'); g.innerHTML = '';
  for (let i = 0; i < n; i++) {
    const x = 190 + (i + 0.5) * (180 / n), l = document.createElementNS(NS, 'line');
    l.setAttribute('x1', x); l.setAttribute('x2', x); l.setAttribute('y1', 130); l.setAttribute('y2', 150);
    l.setAttribute('stroke', '#378ADD'); l.setAttribute('stroke-width', 2); g.appendChild(l);
  }
}
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnSSRI').classList.toggle('active', m === 'ssri');
  document.getElementById('btnBenzo').classList.toggle('active', m === 'benzo');
  document.getElementById('vSSRI').classList.toggle('hide', m !== 'ssri');
  document.getElementById('vBenzo').classList.toggle('hide', m !== 'benzo');
  render();
}
function render() {
  if (mode === 'ssri') {
    const c = SSRI;
    document.getElementById('stepLabel').textContent = c.labels[step];
    drawTicks(c.ticks[step]);
    document.getElementById('fireText').textContent = c.fire[step];
    document.getElementById('ssriDrug').classList.toggle('on', step >= 1);
    document.getElementById('somaNT').classList.toggle('on', step >= 1);
    document.getElementById('autoState').textContent = c.auto[step];
    document.getElementById('auto').style.opacity = step >= 4 ? 0.3 : step === 3 ? 0.6 : 1;
    const lv = c.level[step];
    document.getElementById('lvl').setAttribute('width', Math.round(270 * lv));
    document.querySelectorAll('#cleftNT .nt').forEach((d, i) => d.style.opacity = i < Math.round(8 * lv) ? 1 : 0);
    document.getElementById('ssriNote').textContent = c.note[step];
  } else {
    document.getElementById('stepLabel').textContent = BENZO.labels[step];
    document.getElementById('bzDrug').classList.toggle('on', step >= 1 && step <= 3);
    document.getElementById('tr1g').classList.toggle('on', step >= 2 && step <= 3);
    document.getElementById('tr2g').classList.toggle('on', step === 3);
    document.getElementById('fluma').classList.toggle('on', step === 4);
  }
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
setMode('ssri');
</script>
'''


# ---------------------------------------------------------------------------
# SLEEP_WAKE_REGULATION_GENERAL  (source: sleep_wake.html)
# ---------------------------------------------------------------------------
SLEEP_WAKE_REGULATION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of sleep-wake regulation: adenosine builds sleep pressure during wakefulness, the circadian clock gates timing, sleep-promoting neurons trigger sleep onset, and the brain cycles through NREM and REM stages with distinct wave patterns.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .stg:not(.on) text { visibility: hidden; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #adenosineBar { transition: width 1s ease; }
  #waveTrace { transition: d 0.8s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Sleep-wake regulation, general view</title>
<desc>During wakefulness, adenosine gradually accumulates and builds sleep pressure. The suprachiasmatic nucleus, the brain's circadian clock, tracks light and gates when sleep is appropriate. When sleep pressure is high and the circadian signal permits, sleep-promoting neurons inhibit arousal centers and sleep begins. Sleep cycles through NREM stages, with slow high-amplitude delta waves, and REM sleep, with fast low-amplitude waves resembling wakefulness plus muscle atonia and dreaming, roughly every ninety minutes.</desc>

<text class="ts" x="60" y="40">Sleep pressure (adenosine)</text>
<rect x="60" y="50" width="250" height="16" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<rect id="adenosineBar" x="60" y="50" width="20" height="16" fill="#B91C1C"/>
<text class="ts" x="60" y="84" id="adenoNote"></text>

<g id="scn" class="stg">
<circle cx="450" cy="60" r="12" class="c-amber"/>
<text class="ts" x="450" y="42" text-anchor="middle">SCN — circadian clock (light-gated)</text>
</g>

<g id="vlpo" class="stg">
<circle cx="250" cy="120" r="10" class="c-purple pulse"/>
<text class="ts" x="250" y="105" text-anchor="middle">Sleep-promoting neurons inhibit arousal</text>
</g>

<line x1="30" y1="200" x2="650" y2="200" stroke="var(--t)" stroke-width="1"/>
<path id="waveTrace" d="M30 200 L650 200" stroke="#378ADD" stroke-width="2" fill="none"/>
<text class="ts" x="60" y="230" id="waveLabel">Awake — fast, low-amplitude waves</text>

<g id="cycleNote" class="stg">
<text class="th" x="340" y="270" text-anchor="middle" id="cycleLabel"></text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="stepBack()">Back</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 of 4</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 of 4 — awake: adenosine gradually accumulates, building sleep pressure",
  "Step 1 of 4 — the suprachiasmatic nucleus tracks light input, gating when sleep is appropriate",
  "Step 2 of 4 — with high sleep pressure and circadian permission, sleep-promoting neurons inhibit arousal centers — sleep begins",
  "Step 3 of 4 — NREM sleep: slow, high-amplitude delta waves — deep, restorative sleep",
  "Step 4 of 4 — REM sleep: fast, low-amplitude waves resembling wakefulness, muscle atonia, dreaming — NREM/REM cycles repeat roughly every 90 minutes"
];
const waveTraces = [   // each trace spans the full width (previously they stopped part-way and ran flat)
  "M30 200 L45 195 L60 204 L75 194 L90 203 L105 195 L120 206 L135 196 L150 205 L165 196 L180 206 L195 197 L210 205 L225 194 L240 204 L255 195 L270 204 L285 194 L300 203 L315 195 L330 206 L345 196 L360 205 L375 196 L390 206 L405 197 L420 205 L435 194 L450 204 L465 195 L480 204 L495 194 L510 203 L525 195 L540 206 L555 196 L570 205 L585 196 L600 206 L615 197 L630 205 L645 194 L650 200",
  "M30 200 L45 195 L60 204 L75 194 L90 203 L105 195 L120 206 L135 196 L150 205 L165 196 L180 206 L195 197 L210 205 L225 194 L240 204 L255 195 L270 204 L285 194 L300 203 L315 195 L330 206 L345 196 L360 205 L375 196 L390 206 L405 197 L420 205 L435 194 L450 204 L465 195 L480 204 L495 194 L510 203 L525 195 L540 206 L555 196 L570 205 L585 196 L600 206 L615 197 L630 205 L645 194 L650 200",
  "M30 200 L56 196 L82 206 L108 197 L134 205 L160 196 L186 204 L212 194 L238 203 L264 195 L290 204 L316 196 L342 206 L368 197 L394 205 L420 196 L446 204 L472 194 L498 203 L524 195 L550 204 L576 196 L602 206 L628 197 L650 200",
  "M30 200 Q49.375 160 68.75 200 Q88.125 240 107.5 200 Q126.875 160 146.25 200 Q165.625 240 185 200 Q204.375 160 223.75 200 Q243.125 240 262.5 200 Q281.875 160 301.25 200 Q320.625 240 340 200 Q359.375 160 378.75 200 Q398.125 240 417.5 200 Q436.875 160 456.25 200 Q475.625 240 495 200 Q514.375 160 533.75 200 Q553.125 240 572.5 200 Q591.875 160 611.25 200 Q630.625 240 650 200",
  "M30 200 L43 194 L56 209 L69 196 L82 208 L95 195 L108 207 L121 197 L134 206 L147 191 L160 204 L173 192 L186 205 L199 193 L212 203 L225 194 L238 209 L251 196 L264 208 L277 195 L290 207 L303 197 L316 206 L329 191 L342 204 L355 192 L368 205 L381 193 L394 203 L407 194 L420 209 L433 196 L446 208 L459 195 L472 207 L485 197 L498 206 L511 191 L524 204 L537 192 L550 205 L563 193 L576 203 L589 194 L602 209 L615 196 L628 208 L641 195 L650 200"
];
const waveLabels = [
  "Awake — fast, low-amplitude waves",
  "Awake — fast, low-amplitude waves",
  "Drowsy — waves begin slowing",
  "NREM — slow, high-amplitude delta waves",
  "REM — fast, low-amplitude waves + muscle atonia + dreaming"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  // adenosine builds while awake and is cleared during sleep
  const bar = [40, 140, 230, 150, 80][step];
  document.getElementById('adenosineBar').setAttribute('width', bar);
  document.getElementById('adenosineBar').style.width = bar + 'px';
  document.getElementById('adenoNote').textContent = step <= 1 ? '↑ builds while awake' : step === 2 ? 'high — sleep pressure peaks' : '↓ cleared during sleep';
  document.getElementById('scn').classList.toggle('on', step >= 1);
  document.getElementById('vlpo').classList.toggle('on', step >= 2);
  document.getElementById('waveTrace').setAttribute('d', waveTraces[step]);
  document.getElementById('waveLabel').textContent = waveLabels[step];
  document.getElementById('cycleNote').classList.toggle('on', step === 4);
  document.getElementById('cycleLabel').textContent = step === 4 ? "Cycles repeat ~every 90 minutes through the night" : "";
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# Registry: add a new mechanism by (1) defining a new FRAGMENT_NAME = '''...'''
# string constant above with your SVG/JS animation, and (2) adding one entry
# below. No existing entries need to change.
# "height" controls the iframe height in pixels (svg viewBox height + ~140
# for buttons/labels/description text tends to look right).
# ---------------------------------------------------------------------------
REGISTRY = {
    "Cell signaling (GPCR → cAMP → PKA)": {
        "General": {
            "fragment": GPCR_GENERAL,
            "height": 620,
            "blurb": (
                "Ligand binds a GPCR, which activates a G-protein, which "
                "activates adenylyl cyclase to raise cAMP, which activates "
                "PKA to phosphorylate a target protein."
            ),
        },
        "Technical": {
            "fragment": GPCR_TECHNICAL,
            "height": 640,
            "blurb": (
                "Adds the Gs / Gi / Gq branch selector, the intrinsic "
                "GTPase off-switch, and the PKA R2C2 holoenzyme splitting "
                "into free catalytic subunits."
            ),
        },
    },
    "DNA replication": {
        "General": {
            "fragment": DNA_REPLICATION_GENERAL,
            "height": 520,
            "blurb": (
                "Helicase opens the double helix at a replication fork; "
                "polymerase builds new strands — one continuous (leading), "
                "one in fragments (lagging)."
            ),
        },
        "Technical": {
            "fragment": DNA_REPLICATION_TECHNICAL,
            "height": 560,
            "blurb": (
                "Adds topoisomerase, SSB proteins, primase/RNA primers, "
                "the Pol III sliding clamp, and ligase sealing the "
                "Okazaki fragments."
            ),
        },
    },
    "Cell division (mitosis)": {
        "General": {
            "fragment": MITOSIS_GENERAL,
            "height": 580,
            "blurb": (
                "Seven stages, with sister chromatids correctly separating "
                "individually at anaphase — each daughter cell ends up "
                "with one copy of each chromosome, genetically identical."
            ),
        },
        "Technical": {
            "fragment": MITOSIS_TECHNICAL,
            "height": 460,
            "blurb": (
                "Cohesin holds sister chromatids together until separase "
                "cleaves it; the spindle assembly checkpoint blocks "
                "anaphase until every kinetochore is bi-oriented; an "
                "actomyosin ring drives cytokinesis."
            ),
        },
    },
    "Transcription": {
        "General": {
            "fragment": TRANSCRIPTION_GENERAL,
            "height": 480,
            "blurb": (
                "RNA polymerase binds a promoter, unwinds the DNA locally, "
                "and synthesizes a complementary mRNA strand as it moves "
                "along the gene, then releases it at a terminator."
            ),
        },
        "Technical": {
            "fragment": TRANSCRIPTION_TECHNICAL,
            "height": 460,
            "blurb": (
                "TFIID binds the TATA box, general transcription factors "
                "assemble the pre-initiation complex, TFIIH unwinds the "
                "DNA, and the mRNA's 5' end is capped co-transcriptionally."
            ),
        },
    },
    "Translation": {
        "General": {
            "fragment": TRANSLATION_GENERAL,
            "height": 460,
            "blurb": (
                "A ribosome assembles on mRNA at the start codon, tRNA "
                "delivers matching amino acids, peptide bonds link them "
                "into a growing chain, and a stop codon triggers release."
            ),
        },
        "Technical": {
            "fragment": TRANSLATION_TECHNICAL,
            "height": 460,
            "blurb": (
                "EF-Tu delivers tRNA with wobble pairing checked at codon "
                "position 3, EF-G drives translocation, and — for "
                "secreted proteins — SRP targets the ribosome to the ER."
            ),
        },
    },
    "DNA mismatch repair": {
        "General": {
            "fragment": DNA_MISMATCH_REPAIR_GENERAL,
            "height": 440,
            "blurb": (
                "A replication error is detected, the faulty segment on "
                "the new strand excised, correctly resynthesized from "
                "the template, and sealed — proofreading after the fact."
            ),
        },
        "Technical": {
            "fragment": DNA_MISMATCH_REPAIR_TECHNICAL,
            "height": 460,
            "blurb": (
                "MutSα (MSH2–MSH6) clamps the mismatch, MutLα (MLH1–PMS2) and "
                "PCNA nick only the new strand, EXO1 excises it and Pol δ + "
                "ligase I restore it. Loss of these genes causes Lynch syndrome "
                "and microsatellite instability."
            ),
        },
    },
    "CRISPR-Cas9 gene editing": {
        "General": {
            "fragment": CRISPR_CAS9_GENERAL,
            "height": 460,
            "blurb": (
                "Guide RNA directs Cas9 to a matching DNA sequence next "
                "to a PAM site; Cas9 cuts both strands, and the cell "
                "repairs it via error-prone NHEJ or precise HDR editing."
            ),
        },
    },
    "Lac operon": {
        "General": {
            "fragment": LAC_OPERON_GENERAL,
            "height": 440,
            "blurb": (
                "The classic gene-regulation example: a repressor blocks "
                "the lac genes until lactose binds it and releases the "
                "operator, letting RNA polymerase transcribe them."
            ),
        },
    },
    "RNA interference": {
        "General": {
            "fragment": RNA_INTERFERENCE_GENERAL,
            "height": 460,
            "blurb": (
                "Dicer cleaves double-stranded RNA into siRNA; the guide "
                "strand loads into RISC and directs it to cleave a "
                "complementary target mRNA, silencing that gene."
            ),
        },
    },
    "Meiosis": {
        "General": {
            "fragment": MEIOSIS_GENERAL,
            "height": 560,
            "blurb": (
                "Correctly shows homologs (maternal vs paternal) "
                "separating at anaphase I — not sister chromatids, which "
                "stay joined until meiosis II — producing four haploid "
                "cells, each a different parental combination."
            ),
        },
    },
    "Apoptosis": {
        "General": {
            "fragment": APOPTOSIS_GENERAL,
            "height": 460,
            "blurb": (
                "Two different triggers, one ending: switch between the "
                "extrinsic pathway (death ligand → caspase-8) and the "
                "intrinsic pathway (internal stress → mitochondria → "
                "caspase-9) — both converge on the same executioner "
                "caspase-3."
            ),
        },
    },
    "Endocytosis / exocytosis": {
        "General": {
            "fragment": ENDO_EXOCYTOSIS_GENERAL,
            "height": 460,
            "blurb": (
                "Switch between the two directions: endocytosis pinches a "
                "clathrin-coated vesicle in from the membrane; exocytosis "
                "docks and fuses a vesicle to release cargo outward."
            ),
        },
    },
    "Enzyme kinetics & allosteric regulation": {
        "General": {
            "fragment": ENZYME_KINETICS_GENERAL,
            "height": 480,
            "blurb": (
                "Switch between normal catalysis, competitive inhibition "
                "(same site, beatable by more substrate), allosteric "
                "inhibition (different site, not beatable), and allosteric "
                "activation — regulation isn't only inhibition."
            ),
        },
    },
    "Membrane transport": {
        "General": {
            "fragment": MEMBRANE_TRANSPORT_GENERAL,
            "height": 460,
            "blurb": (
                "Step through a molecule crossing the membrane under each "
                "mode: straight through the bilayer (simple), through an "
                "always-open channel (facilitated), pumped uphill with ATP "
                "(active), or through a channel that only opens once a "
                "ligand binds its receptor site (ligand-gated)."
            ),
        },
    },
    "Humoral immune response": {
        "General": {
            "fragment": HUMORAL_IMMUNE_GENERAL,
            "height": 500,
            "blurb": (
                "A B cell binds antigen, presents it to a helper T cell for "
                "a cytokine signal, then proliferates into antibody-"
                "secreting plasma cells and long-lived memory B cells."
            ),
        },
        "Technical": {
            "fragment": GERMINAL_CENTER_TECHNICAL,
            "height": 460,
            "blurb": (
                "The germinal center reaction: AID mutates the antibody "
                "gene (somatic hypermutation), Tfh cells select only the "
                "highest-affinity clones (affinity maturation), and "
                "surviving cells undergo class switching."
            ),
        },
    },
    "T cell activation": {
        "General": {
            "fragment": TCELL_ACTIVATION_GENERAL,
            "height": 460,
            "blurb": (
                "An antigen-presenting cell displays antigen on MHC-II; "
                "full T cell activation needs both TCR/MHC binding "
                "(signal 1) and CD28/B7 costimulation (signal 2)."
            ),
        },
        "Technical": {
            "fragment": TCR_SIGNALING_TECHNICAL,
            "height": 460,
            "blurb": (
                "The actual signaling cascade: Lck phosphorylates CD3, "
                "ZAP-70 builds the LAT signalosome, second messengers "
                "activate calcineurin, and NFAT drives IL-2 transcription."
            ),
        },
    },
    "Cytotoxic T cell killing": {
        "General": {
            "fragment": CYTOTOXIC_T_CELL_GENERAL,
            "height": 460,
            "blurb": (
                "A CD8 T cell recognizes viral peptide on MHC-I, releases "
                "perforin to punch pores in the target's membrane, and "
                "granzymes entering through them trigger apoptosis."
            ),
        },
    },
    "Complement system": {
        "General": {
            "fragment": COMPLEMENT_SYSTEM_GENERAL,
            "height": 460,
            "blurb": (
                "A cascade of proteins opsonizes a pathogen for "
                "phagocytosis, then assembles a membrane attack complex "
                "that punches a lethal pore in its membrane."
            ),
        },
        "Technical": {
            "fragment": COMPLEMENT_SYSTEM_TECHNICAL,
            "height": 480,
            "blurb": (
                "Adds the classical, lectin, and alternative pathway "
                "selector, showing how each generates its own C3 "
                "convertase before converging on a shared C5 convertase "
                "and membrane attack complex, with C3a/C5a anaphylatoxins."
            ),
        },
    },
    "Innate immune recognition": {
        "General": {
            "fragment": INNATE_IMMUNE_RECOGNITION_GENERAL,
            "height": 460,
            "blurb": (
                "A Toll-like receptor on a macrophage detects a "
                "pathogen-associated pattern, triggering NF-kB signaling "
                "and inflammatory cytokine release."
            ),
        },
        "Technical": {
            "fragment": INNATE_IMMUNE_RECOGNITION_TECHNICAL,
            "height": 560,
            "blurb": (
                "The two-signal model: TLR4-MyD88-IRAK-TRAF6-TAK1-IKK frees "
                "NF-kB to make pro-IL-1 beta, then the NLRP3-ASC-caspase-1 "
                "inflammasome matures IL-1 beta and IL-18 and drives "
                "gasdermin D pyroptosis."
            ),
        },
    },
    "NK cell missing-self recognition": {
        "General": {
            "fragment": NK_CELL_MISSING_SELF_GENERAL,
            "height": 440,
            "blurb": (
                "Switch between a healthy cell (MHC-I present — "
                "inhibits killing) and an infected cell (MHC-I lost — "
                "killing proceeds), the opposite detection strategy from "
                "cytotoxic T cells."
            ),
        },
        "Technical": {
            "fragment": NK_CELL_MISSING_SELF_TECHNICAL,
            "height": 560,
            "blurb": (
                "The receptor balance: KIR/NKG2A (ITIM, SHP-1/2) versus NKG2D "
                "(DAP10/12) for healthy, stressed and HLA-I-lost targets, "
                "killing by perforin and granzyme B, and ADCC through CD16."
            ),
        },
    },
    "Immunological memory": {
        "General": {
            "fragment": IMMUNOLOGICAL_MEMORY_GENERAL,
            "height": 440,
            "blurb": (
                "Compare primary exposure (naive cells, slow, moderate) "
                "against secondary exposure (memory cells, fast, much "
                "stronger) — why vaccines and boosters work."
            ),
        },
    },
    "Type I hypersensitivity": {
        "General": {
            "fragment": TYPE1_HYPERSENSITIVITY_GENERAL,
            "height": 440,
            "blurb": (
                "The allergy mechanism: first exposure sensitizes mast "
                "cells with IgE; a second exposure cross-links that IgE, "
                "triggering degranulation and histamine release."
            ),
        },
    },
    "Immune checkpoint (PD-1/PD-L1)": {
        "General": {
            "fragment": IMMUNE_CHECKPOINT_GENERAL,
            "height": 440,
            "blurb": (
                "How tumors evade T cells by exploiting a normal immune "
                "brake, and how checkpoint inhibitor drugs block it — "
                "the basis of modern cancer immunotherapy."
            ),
        },
    },
    "Fertilization": {
        "General": {
            "fragment": FERTILIZATION_GENERAL,
            "height": 440,
            "blurb": (
                "Sperm penetrates the zona pellucida, membranes fuse, "
                "cortical granules harden the zona to block polyspermy, "
                "and the pronuclei fuse into a diploid zygote."
            ),
        },
        "Technical": {
            "fragment": FERTILIZATION_TECHNICAL,
            "height": 460,
            "blurb": (
                "The egg is arrested at meiosis II until fertilization: a "
                "fast electrical block, then a calcium wave (calcium-"
                "induced calcium release) triggers the slow cortical "
                "block AND resumes meiosis, extruding a second polar body."
            ),
        },
    },
    "Cleavage & blastocyst formation": {
        "General": {
            "fragment": CLEAVAGE_BLASTOCYST_GENERAL,
            "height": 460,
            "blurb": (
                "The zygote divides into 2, 4, 8 and 16 ever-smaller cells "
                "without growing, compacts into a morula, then hollows into "
                "a blastocyst: trophoblast (future placenta) around a "
                "fluid-filled cavity, with an inner cell mass (future embryo)."
            ),
        },
        "Technical": {
            "fragment": CLEAVAGE_BLASTOCYST_TECHNICAL,
            "height": 480,
            "blurb": (
                "Compaction (E-cadherin) and apical polarity (Par/aPKC) create "
                "outer polar and inner apolar cells; Hippo-YAP-TEAD4 switches on "
                "Cdx2 outside (trophectoderm) while Oct4/Nanog stay on inside; "
                "Na+/K+ pumps and tight junctions inflate the blastocoel; the ICM "
                "splits into epiblast and primitive endoderm (FGF4-ERK)."
            ),
        },
    },
    "Implantation": {
        "General": {
            "fragment": IMPLANTATION_GENERAL,
            "height": 480,
            "blurb": (
                "The blastocyst hatches from the zona, attaches to the uterine "
                "lining with its inner cell mass facing the wall, and its "
                "trophoblast splits into cytotrophoblast and an invading "
                "syncytiotrophoblast that buries the embryo and releases hCG."
            ),
        },
        "Technical": {
            "fragment": IMPLANTATION_TECHNICAL,
            "height": 480,
            "blurb": (
                "A progesterone-primed window of implantation (pinopodes, LIF); "
                "L-selectin apposition then αvβ3 integrin/osteopontin adhesion; "
                "syncytin-driven syncytiotrophoblast invades with MMPs; "
                "decidualization and uNK cells; hCG rescues the corpus luteum."
            ),
        },
    },
    "Gastrulation": {
        "General": {
            "fragment": GASTRULATION_GENERAL,
            "height": 460,
            "blurb": (
                "The hollow blastula invaginates at the blastopore, "
                "forming the archenteron and establishing the three germ "
                "layers: ectoderm, mesoderm, and endoderm."
            ),
        },
        "Technical": {
            "fragment": GASTRULATION_TECHNICAL,
            "height": 480,
            "blurb": (
                "The Spemann organizer secretes BMP antagonists that "
                "pattern the dorsal-ventral axis; cells move by "
                "involution and convergent extension while a separate "
                "Nodal gradient specifies the three germ layers."
            ),
        },
    },
    "Neurulation": {
        "General": {
            "fragment": NEURULATION_GENERAL,
            "height": 480,
            "blurb": (
                "The notochord induces the neural plate; its edges rise as "
                "neural folds and fuse into the neural tube (future brain and "
                "spinal cord) while neural crest cells migrate away. Failed "
                "closure causes spina bifida or anencephaly."
            ),
        },
        "Technical": {
            "fragment": NEURULATION_TECHNICAL,
            "height": 490,
            "blurb": (
                "BMP antagonists (Noggin, Chordin) induce the neural plate; "
                "convergent extension narrows it; hinge points bend it by apical "
                "constriction; an E- to N-cadherin switch frees the tube; neural "
                "crest undergoes EMT; Shh vs BMP/Wnt gradients pattern the tube."
            ),
        },
    },
    "Action potential": {
        "General": {
            "fragment": ACTION_POTENTIAL_GENERAL,
            "height": 480,
            "blurb": (
                "Compare three cell types: the fast neuronal spike, the "
                "cardiac ventricular plateau (Ca2+ balances K+, prevents "
                "tetany), and the spontaneously drifting SA node pacemaker "
                "potential (Ca2+-driven, no fast Na+ channels at all)."
            ),
        },
    },
    "Muscle contraction (skeletal)": {
        "General": {
            "fragment": MUSCLE_CONTRACTION_GENERAL,
            "height": 420,
            "blurb": (
                "The sliding filament model: Ca2+ exposes myosin-binding "
                "sites on actin, cross-bridges form and pull the "
                "filaments inward, and ATP is needed to release the "
                "cross-bridge and reset the cycle."
            ),
        },
        "Technical": {
            "fragment": MUSCLE_CONTRACTION_TECHNICAL,
            "height": 460,
            "blurb": (
                "DHPR directly (mechanically) opens RyR — no calcium "
                "trigger, unlike cardiac muscle — and myosin cycles "
                "through weak binding, power stroke, rigor, and "
                "ATP-driven detachment."
            ),
        },
    },
    "Muscle contraction (cardiac)": {
        "General": {
            "fragment": CARDIAC_MUSCLE_CONTRACTION_GENERAL,
            "height": 440,
            "blurb": (
                "Excitation-contraction coupling in heart muscle: a small "
                "trigger Ca2+ influx opens ryanodine receptors for "
                "calcium-induced calcium release, and gap junctions at "
                "intercalated discs spread the signal cell to cell."
            ),
        },
        "Technical": {
            "fragment": CARDIAC_MUSCLE_CONTRACTION_TECHNICAL,
            "height": 500,
            "blurb": (
                "The dyad and the full Ca2+ cycle: L-type trigger Ca2+ opens "
                "RyR2 (CICR), Ca2+ binds troponin C, SERCA2a/phospholamban and "
                "NCX clear it, and beta-1/PKA signalling makes beats stronger "
                "and faster."
            ),
        },
    },
    "Cardiac conduction system": {
        "General": {
            "fragment": CARDIAC_CONDUCTION_GENERAL,
            "height": 460,
            "blurb": (
                "The SA node fires, depolarizing the atria; the signal "
                "delays at the AV node, then races through the Bundle of "
                "His and Purkinje fibers to trigger ventricular contraction."
            ),
        },
    },
    "Gas exchange (alveoli)": {
        "General": {
            "fragment": GAS_EXCHANGE_GENERAL,
            "height": 440,
            "blurb": (
                "O2 diffuses from alveolus into blood and binds "
                "hemoglobin, while CO2 diffuses the opposite direction "
                "to be exhaled — both driven by concentration gradients."
            ),
        },
        "Technical": {
            "fragment": GAS_EXCHANGE_TECHNICAL,
            "height": 540,
            "blurb": (
                "Partial pressures and Fick diffusion, the O2-Hb "
                "dissociation curve with the Bohr shift, and CO2 carried as "
                "bicarbonate (carbonic anhydrase, chloride shift, Haldane "
                "effect) in the lungs and in the tissues."
            ),
        },
    },
    "Synaptic transmission": {
        "General": {
            "fragment": SYNAPTIC_TRANSMISSION_GENERAL,
            "height": 440,
            "blurb": (
                "An action potential opens Ca2+ channels at the axon "
                "terminal, triggering vesicle fusion and neurotransmitter "
                "release, which crosses the cleft and binds receptors."
            ),
        },
        "Technical": {
            "fragment": SYNAPSE_TYPES_TECHNICAL,
            "height": 440,
            "blurb": (
                "Chemical synapses aren't the only kind: compare them "
                "against electrical synapses, which connect cells "
                "directly through gap junctions — near-instant but not "
                "modifiable, the opposite trade-off from chemical ones."
            ),
        },
    },
    "Synaptic plasticity (LTP)": {
        "General": {
            "fragment": SYNAPTIC_PLASTICITY_LTP_GENERAL,
            "height": 460,
            "blurb": (
                "The cellular basis of learning and memory: the NMDA "
                "receptor acts as a coincidence detector, needing both "
                "glutamate AND depolarization to open, triggering AMPA "
                "receptor insertion that strengthens the synapse."
            ),
        },
        "Technical": {
            "fragment": SYNAPTIC_PLASTICITY_LTP_TECHNICAL,
            "height": 500,
            "blurb": (
                "LTP vs LTD: a large Ca2+ rise activates CaMKII "
                "(autophosphorylation, AMPA phosphorylation and insertion, "
                "then PKA-CREB for late LTP), while a small Ca2+ rise "
                "activates calcineurin/PP1, which removes AMPA receptors."
            ),
        },
    },
    "Dopamine reward pathway": {
        "General": {
            "fragment": DOPAMINE_REWARD_PATHWAY_GENERAL,
            "height": 440,
            "blurb": (
                "A reward activates VTA dopamine neurons, releasing "
                "dopamine into the nucleus accumbens to reinforce the "
                "behavior; some drugs of abuse hijack this by blocking "
                "reuptake or triggering extra release."
            ),
        },
    },
    "Medication mechanism of action": {
        "General": {
            "fragment": MEDICATION_MECHANISM_GENERAL,
            "height": 440,
            "blurb": (
                "Compare two receptor pharmacology mechanisms: SSRIs "
                "block serotonin reuptake, while benzodiazepines act as "
                "positive allosteric modulators of the GABA-A receptor."
            ),
        },
        "Technical": {
            "fragment": MEDICATION_MECHANISM_TECHNICAL,
            "height": 560,
            "blurb": (
                "Why SSRIs take weeks (5-HT1A autoreceptor brake and its "
                "desensitization) and why benzodiazepines are safer than "
                "barbiturates (alpha/gamma-2 site, more frequent vs longer "
                "openings, flumazenil reversal)."
            ),
        },
    },
    "Sleep-wake regulation": {
        "General": {
            "fragment": SLEEP_WAKE_REGULATION_GENERAL,
            "height": 460,
            "blurb": (
                "Adenosine builds sleep pressure while awake, the "
                "circadian clock (SCN) gates timing, and sleep cycles "
                "through NREM (slow delta waves) and REM (fast waves, "
                "muscle atonia, dreaming) roughly every 90 minutes."
            ),
        },
    },
    "Electron transport chain & ATP synthase": {
        "General": {
            "fragment": ELECTRON_TRANSPORT_CHAIN_GENERAL,
            "height": 440,
            "blurb": (
                "Electrons pass through membrane complexes pumping "
                "protons to build a gradient; protons flowing back "
                "through ATP synthase spin it, generating ATP."
            ),
        },
        "Technical": {
            "fragment": ELECTRON_TRANSPORT_CHAIN_TECHNICAL,
            "height": 540,
            "blurb": (
                "NADH vs FADH2: proton stoichiometry of Complexes I-IV "
                "(10 vs 6 H+), the proton-motive force, Fo c-ring rotation and "
                "the F1 binding-change mechanism, giving P/O ratios of about "
                "2.5 and 1.5."
            ),
        },
    },
    "Blood clotting (hemostasis)": {
        "General": {
            "fragment": BLOOD_CLOTTING_GENERAL,
            "height": 460,
            "blurb": (
                "Platelets form a fast temporary plug at the injury; the "
                "slower coagulation cascade converges on thrombin, which "
                "converts fibrinogen into a fibrin mesh that stabilizes it."
            ),
        },
    },
    "Blood glucose homeostasis": {
        "General": {
            "fragment": BLOOD_GLUCOSE_HOMEOSTASIS_GENERAL,
            "height": 480,
            "blurb": (
                "Switch between the insulin loop (high glucose → uptake) "
                "and the glucagon loop (low glucose → liver releases "
                "glucose) — a classic negative feedback pair."
            ),
        },
        "Technical": {
            "fragment": BLOOD_GLUCOSE_HOMEOSTASIS_TECHNICAL,
            "height": 560,
            "blurb": (
                "Beta-cell stimulus-secretion coupling (GLUT2, glucokinase, "
                "K-ATP, Ca2+), insulin signalling via IRS-1/PI3K/Akt to GLUT4, "
                "and glucagon's Gs-cAMP-PKA control of hepatic glycogenolysis "
                "and gluconeogenesis."
            ),
        },
    },
    "Nephron filtration": {
        "General": {
            "fragment": NEPHRON_FILTRATION_GENERAL,
            "height": 460,
            "blurb": (
                "Blood is filtered at the glomerulus, useful solutes are "
                "reabsorbed along the tubule back into blood, waste is "
                "secreted into the filtrate, and the rest becomes urine."
            ),
        },
        "Technical": {
            "fragment": NEPHRON_FILTRATION_TECHNICAL,
            "height": 560,
            "blurb": (
                "Starling forces and GFR, then segment by segment: SGLT2 in "
                "the proximal tubule, AQP1 and NKCC2 in the loop (countercurrent "
                "multiplier), NCC in the DCT, and ENaC/ROMK/AQP2 in the "
                "collecting duct, with and without ADH."
            ),
        },
    },
    "Reflex arc (patellar reflex)": {
        "General": {
            "fragment": REFLEX_ARC_GENERAL,
            "height": 460,
            "blurb": (
                "A tap stretches the muscle spindle; a sensory neuron "
                "synapses directly onto a motor neuron in the spinal "
                "cord — no brain involved — contracting the quadriceps "
                "while an interneuron relaxes the hamstring."
            ),
        },
    },
    "Baroreceptor reflex": {
        "General": {
            "fragment": BARORECEPTOR_REFLEX_GENERAL,
            "height": 440,
            "blurb": (
                "Rising blood pressure stretches baroreceptors, the "
                "medulla shifts autonomic output, and heart rate and "
                "vessel tone fall to bring pressure back to setpoint."
            ),
        },
        "Technical": {
            "fragment": BARORECEPTOR_REFLEX_TECHNICAL,
            "height": 540,
            "blurb": (
                "The full circuit in both directions: CN IX/X afferents to the "
                "NTS, the nucleus ambiguus (vagal) and the CVLM-RVLM "
                "(sympathetic) limbs, and their effects on heart, vessels and "
                "kidney when pressure rises or falls."
            ),
        },
    },
    "Labor (positive feedback)": {
        "General": {
            "fragment": LABOR_POSITIVE_FEEDBACK_GENERAL,
            "height": 500,
            "blurb": (
                "The Ferguson reflex: cervical stretch triggers oxytocin, "
                "which causes contractions that increase cervical "
                "stretch — positive feedback that escalates rather than "
                "corrects, unlike almost every other loop in this app."
            ),
        },
        "Technical": {
            "fragment": LABOR_TECHNICAL,
            "height": 560,
            "blurb": (
                "What primes the loop: progesterone withdrawal and rising "
                "CRH shift the uterus out of quiescence, prostaglandins "
                "ripen the cervix and upregulate oxytocin receptors — "
                "only then does the sensitized Ferguson reflex take over."
            ),
        },
    },
}

st.title("Molecular Mechanisms — Interactive Explainers")
st.caption(
    "Step-through animations of core cell biology mechanisms. "
    "Use the controls in the sidebar to pick a mechanism and detail level."
)

# ---------------------------------------------------------------------------
# CATEGORIES: purely organizational — groups REGISTRY keys by subfield for
# the sidebar. Adding a new mechanism to REGISTRY also means adding its name
# to the right list here (or it won't show up in the sidebar). Existing
# REGISTRY entries and mechanism constants are untouched by this.
# ---------------------------------------------------------------------------
CATEGORIES = {
    "Molecular Biology & Genetics": [
        "DNA replication",
        "DNA mismatch repair",
        "Transcription",
        "Translation",
        "Lac operon",
        "RNA interference",
        "CRISPR-Cas9 gene editing",
    ],
    "Cell Biology": [
        "Enzyme kinetics & allosteric regulation",
        "Membrane transport",
        "Endocytosis / exocytosis",
        "Cell signaling (GPCR → cAMP → PKA)",
        "Cell division (mitosis)",
        "Meiosis",
        "Apoptosis",
    ],
    "Embryology": [
        "Fertilization",
        "Cleavage & blastocyst formation",
        "Implantation",
        "Gastrulation",
        "Neurulation",
    ],
    "Physiology": [
        "Action potential",
        "Synaptic transmission",
        "Synaptic plasticity (LTP)",
        "Reflex arc (patellar reflex)",
        "Dopamine reward pathway",
        "Sleep-wake regulation",
        "Muscle contraction (skeletal)",
        "Muscle contraction (cardiac)",
        "Cardiac conduction system",
        "Baroreceptor reflex",
        "Blood clotting (hemostasis)",
        "Gas exchange (alveoli)",
        "Electron transport chain & ATP synthase",
        "Nephron filtration",
        "Blood glucose homeostasis",
        "Labor (positive feedback)",
        "Medication mechanism of action",
    ],
    "Immunology": [
        "Innate immune recognition",
        "Complement system",
        "NK cell missing-self recognition",
        "T cell activation",
        "Humoral immune response",
        "Cytotoxic T cell killing",
        "Immunological memory",
        "Immune checkpoint (PD-1/PD-L1)",
        "Type I hypersensitivity",
    ],
}

with st.sidebar:
    st.header("Choose a mechanism")
    category = st.selectbox("Category", list(CATEGORIES.keys()))   # molecules -> cells -> development -> body systems -> immunity
    topic = st.radio("Mechanism", CATEGORIES[category])   # listed in the order the processes happen, not alphabetically
    levels_available = list(REGISTRY[topic].keys())
    level = st.radio("Detail level", levels_available)

entry = REGISTRY[topic][level]
st.subheader(f"{topic} — {level}")
st.write(entry["blurb"])

wrapped_fragment = (
    '<div style="max-width:680px;margin:0 auto;">' + entry["fragment"] + "</div>"
)
st.components.v1.html(
    COMMON_STYLE + wrapped_fragment,
    height=entry["height"] + 60,
    scrolling=True,
)

st.divider()
st.caption(
    "Every mechanism is a string constant above (e.g. GPCR_GENERAL) plus one "
    "REGISTRY entry — edit a constant's SVG/CSS/JS to change a diagram, or "
    "add a new constant + registry entry to add a new mechanism."
)
