import streamlit as st

st.set_page_config(page_title="Molecular Mechanisms", layout="wide")

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
<text class="ts" x="52" y="145">Plasma membrane</text>

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
<rect x="420" y="350" width="90" height="40" rx="8" class="c-teal" stroke-width="0.5"/>
<text class="th" x="465" y="365" text-anchor="middle" dominant-baseline="central">PKA</text>
<text class="ts" x="465" y="382" text-anchor="middle" dominant-baseline="central">catalytic subunit released</text>
</g>

<g id="s4" class="stg">
<rect x="420" y="420" width="90" height="36" rx="8" class="c-coral" stroke-width="0.5"/>
<text class="th" x="465" y="434" text-anchor="middle" dominant-baseline="central">Target</text>
<text class="ts" x="465" y="450" text-anchor="middle" dominant-baseline="central">phosphorylated (P)</text>
</g>
<line id="pkaarrow" x1="465" y1="391" x2="465" y2="418" stroke="var(--t)" stroke-width="1" marker-end="url(#arrow)" class="stg" opacity="0"/>

<line id="gtoAC0" x1="180" y1="260" x2="196" y2="258" stroke="var(--t)" stroke-width="1" marker-end="url(#arrow)"/>
<line id="atoAC" x1="290" y1="260" x2="468" y2="260" stroke="var(--t)" stroke-width="1" class="stg" opacity="0" marker-end="url(#arrow)"/>
<line id="ACtocamp" x1="505" y1="220" x2="505" y2="255" stroke="var(--t)" stroke-width="1" class="stg" opacity="0" marker-end="url(#arrow)"/>
<line id="camptopka" x1="500" y1="330" x2="475" y2="348" stroke="var(--t)" stroke-width="1" class="stg" opacity="0" marker-end="url(#arrow)"/>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
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
  document.getElementById('atoAC').setAttribute('opacity', step >= 2 ? '1' : '0');
  document.getElementById('ACtocamp').setAttribute('opacity', step >= 2 ? '1' : '0');
  document.getElementById('s2').classList.toggle('on', step >= 2);
  document.getElementById('camptopka').setAttribute('opacity', step >= 3 ? '1' : '0');
  document.getElementById('s3').classList.toggle('on', step >= 3);
  document.getElementById('pkaarrow').setAttribute('opacity', step >= 4 ? '1' : '0');
  document.getElementById('s4').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
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
  .split #Cunit1 { transform: translate(-34px, 20px); }
  .split #Cunit2 { transform: translate(34px, 20px); }
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
<text class="ts" x="42" y="115">Plasma membrane</text>

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
<line id="toAC_s" x1="222" y1="225" x2="358" y2="180" stroke="#639922" stroke-width="1.2" class="stg" marker-end="url(#arrow)"/>
<g id="campUp" class="stg">
<circle class="drift" cx="410" cy="215" r="4" fill="#378ADD"/>
<circle class="drift" cx="425" cy="230" r="4" fill="#378ADD" style="animation-delay:.3s"/>
<circle class="drift" cx="400" cy="235" r="4" fill="#378ADD" style="animation-delay:.6s"/>
<text class="ts" x="393" y="260" text-anchor="middle">cAMP ↑</text>
</g>
</g>

<g id="giPath" class="stg">
<line id="toAC_i" x1="222" y1="225" x2="358" y2="180" stroke="#E24B4A" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#arrow)"/>
<text class="ts" x="393" y="260" text-anchor="middle">cAMP ↓ (inhibited)</text>
</g>

<g id="gqPath" class="stg">
<rect x="500" y="110" width="66" height="76" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="533" y="200" text-anchor="middle">Phospholipase C</text>
<line x1="222" y1="228" x2="498" y2="180" stroke="#0F6E56" stroke-width="1.2" marker-end="url(#arrow)"/>
<text class="ts" x="533" y="220" text-anchor="middle">IP3 + DAG</text>
<circle class="drift" cx="515" cy="235" r="4" fill="#1D9E75"/>
<circle class="drift" cx="550" cy="235" r="4" fill="#1D9E75" style="animation-delay:.4s"/>
</g>

<g id="pkaBlock" class="stg">
<g id="pkaGroup" transform="translate(393,320)">
  <rect x="-70" y="-24" width="60" height="48" rx="8" class="c-teal" stroke-width="0.5"/>
  <text class="ts" x="-40" y="0" text-anchor="middle" dominant-baseline="central">R</text>
  <rect x="10" y="-24" width="60" height="48" rx="8" class="c-teal" stroke-width="0.5"/>
  <text class="ts" x="40" y="0" text-anchor="middle" dominant-baseline="central">R</text>
  <g id="Cunit1">
    <rect x="-34" y="-24" width="60" height="48" rx="8" class="c-coral" stroke-width="0.5"/>
    <text class="ts" x="-4" y="0" text-anchor="middle" dominant-baseline="central">C</text>
  </g>
  <g id="Cunit2">
    <rect x="-26" y="-24" width="60" height="48" rx="8" class="c-coral" stroke-width="0.5"/>
    <text class="ts" x="4" y="0" text-anchor="middle" dominant-baseline="central">C</text>
  </g>
</g>
<text class="ts" x="393" y="360" text-anchor="middle">PKA holoenzyme (R2C2)</text>
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
  <button onclick="hydrolyze()">Trigger GTPase (off-switch)</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 — resting</span>
</div>

<script>
let step = 0;
let path = 'Gs';
const labelsGs = ["Step 0 — resting","Step 1 — ligand docks, Ga-GTP forms","Step 2 — AC activated, cAMP rises","Step 3 — PKA holoenzyme splits","Step 4 — target phosphorylated"];
const labelsGi = ["Step 0 — resting","Step 1 — ligand docks, Ga-GTP forms","Step 2 — AC inhibited, cAMP falls"];
const labelsGq = ["Step 0 — resting","Step 1 — ligand docks, Ga-GTP forms","Step 2 — PLC activated, IP3 + DAG produced"];
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
  document.getElementById('gsPath').classList.toggle('on', path==='Gs' && step>=1);
  document.getElementById('giPath').classList.toggle('on', path==='Gi' && step>=1);
  document.getElementById('gqPath').classList.toggle('on', path==='Gq' && step>=1);
  document.getElementById('campUp').classList.toggle('on', path==='Gs' && step>=2);
  document.getElementById('pkaBlock').classList.toggle('on', path==='Gs' && step>=3);
  document.getElementById('pkaGroup').classList.toggle('split', path==='Gs' && step>=3);
  document.getElementById('camptopka').setAttribute('opacity', path==='Gs' && step>=3 ? '1':'0');
  document.getElementById('targetBlock').classList.toggle('on', path==='Gs' && step>=4);
  document.getElementById('pkaarrow').setAttribute('opacity', path==='Gs' && step>=4 ? '1':'0');
  document.getElementById('gtpaseNote').setAttribute('opacity','0');
}
function stepFwd() { if (step < maxStep()) step++; render(); }
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
  #forkGroup, #topStrand, #botStrand, #newTop, #newBot { transition: transform 1s ease; }
  .open #forkGroup { transform: translateX(90px); }
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

<g id="forkGroup">
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
<path id="newBot" d="M260 162 Q300 178 440 210" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-dasharray="6 4" stroke-linecap="round"/>
<text class="ts" x="400" y="255" text-anchor="middle">Okazaki fragments (lagging strand)</text>
</g>

<text class="ts" x="470" y="90" text-anchor="middle">Leading strand</text>
</g>

<text class="ts" x="130" y="310" text-anchor="middle" id="labelParent">Original DNA</text>
<text class="ts" x="470" y="310" text-anchor="middle" id="labelDaughters" class="stg">Two identical daughter helices</text>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 — intact helix</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 — intact double helix",
  "Step 1 — helicase unwinds the strands",
  "Step 2 — polymerase synthesizes new strands",
  "Step 3 — two daughter helices formed"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('helicase').classList.toggle('on', step >= 1);
  document.getElementById('helicase').classList.toggle('pulse', step === 1);
  document.querySelector('svg').classList.toggle('open', step >= 1);
  document.getElementById('polTop').classList.toggle('on', step >= 2);
  document.getElementById('polBot').classList.toggle('on', step >= 2);
  document.getElementById('labelDaughters').classList.toggle('on', step >= 3);
}
function stepFwd() { if (step < 3) step++; render(); }
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
  #forkGroup { transition: transform 1s ease; }
  .open #forkGroup { transform: translateX(60px); }
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
<text class="ts" x="180" y="150" text-anchor="middle" dominant-baseline="central">Helicase</text>
</g>

<g id="forkGroup">
<path d="M198 148 Q260 115 480 90" stroke="#378ADD" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M198 152 Q260 185 480 220" stroke="#D85A30" stroke-width="3" fill="none" stroke-linecap="round"/>

<g id="ssb" class="stg">
<circle cx="230" cy="132" r="5" fill="#8B5CF6"/>
<circle cx="250" cy="122" r="5" fill="#8B5CF6"/>
<circle cx="230" cy="170" r="5" fill="#8B5CF6"/>
<circle cx="255" cy="180" r="5" fill="#8B5CF6"/>
<text class="ts" x="245" y="100" text-anchor="middle">SSB proteins</text>
</g>

<g id="primerLead" class="stg">
<rect x="270" y="98" width="28" height="8" rx="3" fill="#EF9F27"/>
<text class="ts" x="284" y="118" text-anchor="middle">RNA primer</text>
</g>

<g id="polLead" class="stg">
<circle cx="360" cy="98" r="7" class="c-teal"/>
<circle cx="360" cy="98" r="13" fill="none" stroke="#0F6E56" stroke-width="1.5" stroke-dasharray="2 2"/>
<text class="ts" x="360" y="80" text-anchor="middle">Pol III + clamp</text>
<path id="newLead" d="M298 103 Q330 95 470 92" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<text class="ts" x="450" y="78" text-anchor="middle">Leading (continuous)</text>
</g>

<g id="primerLag" class="stg">
<rect x="300" y="188" width="22" height="7" rx="3" fill="#EF9F27"/>
<rect x="360" y="200" width="22" height="7" rx="3" fill="#EF9F27"/>
<rect x="410" y="210" width="22" height="7" rx="3" fill="#EF9F27"/>
</g>
<g id="polLag" class="stg">
<circle cx="330" cy="196" r="6" class="c-teal"/>
<circle cx="390" cy="207" r="6" class="c-teal"/>
<text class="ts" x="360" y="235" text-anchor="middle">Lagging (Okazaki fragments)</text>
</g>
<g id="fragments" class="stg">
<path d="M300 195 Q315 190 328 197" stroke="#1D9E75" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M360 207 Q375 202 388 208" stroke="#1D9E75" stroke-width="2" fill="none" stroke-linecap="round"/>
</g>

<g id="ligase" class="stg">
<circle cx="345" cy="200" r="9" class="c-coral"/>
<text class="ts" x="345" y="180" text-anchor="middle">Ligase seals nicks</text>
</g>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="reset()">Reset</button>
  <span id="stepLabel">Step 0 — intact helix</span>
</div>

<script>
let step = 0;
const labels = [
  "Step 0 — intact helix ahead of the fork",
  "Step 1 — topoisomerase relieves supercoiling",
  "Step 2 — helicase unwinds, SSB proteins coat strands",
  "Step 3 — primase lays RNA primers",
  "Step 4 — Pol III extends leading (continuous) and lagging (fragments) strands",
  "Step 5 — primers removed, ligase seals the nicks"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('topo').classList.toggle('on', step >= 1);
  document.getElementById('topo').classList.toggle('pulse', step === 1);
  document.getElementById('helicase').classList.toggle('on', step >= 2);
  document.querySelector('svg').classList.toggle('open', step >= 2);
  document.getElementById('ssb').classList.toggle('on', step >= 2);
  document.getElementById('primerLead').classList.toggle('on', step >= 3);
  document.getElementById('primerLag').classList.toggle('on', step >= 3);
  document.getElementById('polLead').classList.toggle('on', step >= 4);
  document.getElementById('polLag').classList.toggle('on', step >= 4);
  document.getElementById('fragments').classList.toggle('on', step >= 4);
  document.getElementById('ligase').classList.toggle('on', step >= 5);
  document.getElementById('ligase').classList.toggle('pulse', step === 5);
}
function stepFwd() { if (step < 5) step++; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''

# ---------------------------------------------------------------------------
# MITOSIS_GENERAL  (source: mitosis_general.html)
# ---------------------------------------------------------------------------
MITOSIS_GENERAL = '''
<h2 class="sr-only">Interactive diagram of mitotic cell division with seven visually distinct stages: interphase, prophase, prometaphase, metaphase, anaphase, telophase, and cytokinesis.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #chrom1, #chrom2 { transition: transform 1s cubic-bezier(.3,0,.2,1); }
  #spindleLinesL, #spindleLinesR { transition: opacity .6s ease, stroke-dasharray .6s ease; }
  #furrowTop, #furrowBot { transition: transform 1s ease; }
  .cytokinesis #furrowTop { transform: translateY(40px); }
  .cytokinesis #furrowBot { transform: translateY(-40px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 400" role="img">
<title>Mitotic cell division, seven-stage general view</title>
<desc>A cell progresses through interphase, prophase, prometaphase, metaphase, anaphase, telophase, and cytokinesis, ending as two separate daughter cells. Chromosome position and spindle attachment visibly change at each stage.</desc>

<ellipse id="cellOutline" cx="340" cy="180" rx="220" ry="140" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<text class="ts" x="340" y="30" text-anchor="middle" id="stageLabel">Interphase</text>

<ellipse id="nucleus" cx="340" cy="165" rx="90" ry="55" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>

<g id="chromatin">
<path d="M260 150 Q280 120 300 150 Q320 180 340 150" stroke="#378ADD" stroke-width="2" fill="none" opacity="0.5"/>
<path d="M300 190 Q320 160 350 200 Q370 230 390 200" stroke="#D85A30" stroke-width="2" fill="none" opacity="0.5"/>
<path d="M360 140 Q390 160 410 130" stroke="#1D9E75" stroke-width="2" fill="none" opacity="0.5"/>
</g>

<g id="condensed" class="stg">
<g id="chrom1">
<path d="M310 150 L340 180 M340 150 L310 180" stroke="#378ADD" stroke-width="4" stroke-linecap="round"/>
</g>
<g id="chrom2">
<path d="M340 150 L370 180 M370 150 L340 180" stroke="#D85A30" stroke-width="4" stroke-linecap="round"/>
</g>
</g>

<g id="spindle" class="stg">
<circle cx="140" cy="180" r="6" class="c-amber"/>
<circle cx="540" cy="180" r="6" class="c-amber"/>
<text class="ts" x="140" y="160" text-anchor="middle">Pole</text>
<text class="ts" x="540" y="160" text-anchor="middle">Pole</text>
<g id="spindleLinesL">
<line x1="140" y1="180" x2="325" y2="163" stroke="var(--t)" stroke-width="0.75"/>
<line x1="140" y1="180" x2="325" y2="180" stroke="var(--t)" stroke-width="0.75"/>
</g>
<g id="spindleLinesR">
<line x1="540" y1="180" x2="355" y2="163" stroke="var(--t)" stroke-width="0.75"/>
<line x1="540" y1="180" x2="355" y2="180" stroke="var(--t)" stroke-width="0.75"/>
</g>
</g>

<g id="newNuclei" class="stg">
<ellipse cx="240" cy="180" rx="55" ry="45" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<ellipse cx="440" cy="180" rx="55" ry="45" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
</g>

<g id="furrow" class="stg">
<path id="furrowTop" d="M340 40 L340 140" stroke="var(--border-strong)" stroke-width="2.5"/>
<path id="furrowBot" d="M340 220 L340 320" stroke="var(--border-strong)" stroke-width="2.5"/>
</g>

<g id="daughterLabels" class="stg">
<text class="ts" x="220" y="345" text-anchor="middle">Daughter cell 1</text>
<text class="ts" x="460" y="345" text-anchor="middle">Daughter cell 2</text>
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
  "Interphase — chromatin uncondensed, nuclear envelope intact",
  "Prophase — chromosomes condense inside an intact nucleus, no spindle attachment yet",
  "Prometaphase — envelope broken, spindle fibers search and probe for chromosomes (dashed, scattered)",
  "Metaphase — every chromosome captured and pulled into a single line at the equator (solid, taut)",
  "Anaphase — sister chromatids split and pulled to opposite poles",
  "Telophase — nuclear envelopes reform around each chromosome set",
  "Cytokinesis — cleavage furrow splits the cell into two"
];
const positions = {
  1: [-45,-25, 45,20],
  2: [-18,-30, 22,25],
  3: [0,0, 0,0],
  4: [0,0, 0,0],
  5: [-100,0, 100,0],
  6: [-100,0, 100,0]
};
function render() {
  document.getElementById('stageLabel').textContent = labels[step];
  document.getElementById('stepLabel').textContent = 'Step ' + step + ' of 6';
  document.getElementById('chromatin').style.opacity = step === 0 ? '1' : '0';
  document.getElementById('nucleus').style.opacity = step <= 1 ? '1' : '0';
  document.getElementById('condensed').classList.toggle('on', step >= 1);

  const pos = positions[step] || [0,0,0,0];
  let extra1 = '', extra2 = '';
  if (step === 4) { extra1 = ' translateX(-70px)'; extra2 = ' translateX(70px)'; }
  document.getElementById('chrom1').style.transform = `translate(${pos[0]}px, ${pos[1]}px)` + extra1;
  document.getElementById('chrom2').style.transform = `translate(${pos[2]}px, ${pos[3]}px)` + extra2;

  document.getElementById('spindle').classList.toggle('on', step >= 2 && step <= 4);
  const searching = step === 2;
  [document.getElementById('spindleLinesL'), document.getElementById('spindleLinesR')].forEach(g => {
    g.style.opacity = searching ? '0.5' : '1';
    g.querySelectorAll('line').forEach(l => l.setAttribute('stroke-dasharray', searching ? '3 3' : '0'));
  });

  document.getElementById('newNuclei').classList.toggle('on', step >= 5);
  document.getElementById('condensed').style.opacity = step >= 5 ? '0.3' : (step>=1 ? '1':'0.12');
  document.getElementById('furrow').classList.toggle('on', step >= 6);
  document.querySelector('svg').classList.toggle('cytokinesis', step >= 6);
  document.getElementById('daughterLabels').classList.toggle('on', step >= 6);
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
  .elongating #rnapGroup { transform: translateX(180px); }
  .terminated #rnapGroup { transform: translateX(340px); opacity: 0; }
  #mrnaTail { transition: stroke-dasharray 1.2s ease; }
  #bubbleTop, #bubbleBot { transition: d 1s ease; }
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
<text class="ts" x="115" y="132" text-anchor="middle">Promoter</text>

<g id="bubble" class="stg">
<path id="bubbleTop" d="M115 150 Q160 128 205 150" stroke="#378ADD" stroke-width="3" fill="none" stroke-linecap="round"/>
<path id="bubbleBot" d="M115 170 Q160 192 205 170" stroke="#D85A30" stroke-width="3" fill="none" stroke-linecap="round"/>
</g>

<g id="rnapGroup">
<circle cx="115" cy="160" r="24" class="c-purple"/>
<text class="th" x="115" y="160" text-anchor="middle" dominant-baseline="central">RNAP</text>
</g>

<g id="mrna" class="stg">
<path id="mrnaTail" d="M115 128 Q160 105 290 100" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-dasharray="1000 1000" stroke-dashoffset="1000"/>
<text class="ts" x="290" y="85" text-anchor="middle">mRNA (growing 5'→3')</text>
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
  "Step 0 — intact DNA, promoter unbound",
  "Step 1 — RNA polymerase binds the promoter",
  "Step 2 — DNA unwinds, mRNA synthesis begins",
  "Step 3 — polymerase elongates the mRNA along the gene",
  "Step 4 — termination: mRNA released, DNA reanneals"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('promoterBox').setAttribute('stroke-width', step === 1 ? '2.5' : '1.5');
  document.getElementById('bubble').classList.toggle('on', step >= 2);
  document.getElementById('mrna').classList.toggle('on', step >= 2);
  document.getElementById('mrnaTail').style.strokeDashoffset = step >= 2 ? '0' : '1000';
  document.getElementById('released').classList.toggle('on', step >= 4);
  const svg = document.querySelector('svg');
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
  #chain { transition: transform 1s ease, opacity .6s ease; }
  .released #chain { transform: translateY(-60px); opacity: 0; }
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
<rect id="siteE" x="105" y="200" width="20" height="16" rx="3" fill="none" stroke="var(--t)" stroke-width="0.5" opacity="0"/>
<rect id="siteP" x="140" y="200" width="20" height="16" rx="3" fill="none" stroke="var(--t)" stroke-width="0.5"/>
<rect id="siteA" x="175" y="200" width="20" height="16" rx="3" fill="none" stroke="var(--t)" stroke-width="0.5" opacity="0"/>
<text class="ts" x="150" y="165" text-anchor="middle">Ribosome</text>
</g>

<g id="trnaP" class="stg">
<circle cx="150" cy="150" r="9" class="c-teal"/>
<text class="ts" x="150" y="135" text-anchor="middle">tRNA</text>
</g>
<g id="trnaA" class="stg">
<circle cx="195" cy="150" r="9" class="c-amber"/>
</g>

<g id="chain" class="stg">
<circle cx="150" cy="105" r="7" class="c-coral"/>
<circle id="aa2" cx="168" cy="95" r="7" class="c-coral" opacity="0"/>
<circle id="aa3" cx="186" cy="90" r="7" class="c-coral" opacity="0"/>
<text class="ts" x="168" y="75" text-anchor="middle">Polypeptide chain</text>
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
  "Step 0 — mRNA alone, start codon marked",
  "Step 1 — small subunit binds, initiator tRNA pairs with start codon",
  "Step 2 — large subunit joins, forming the complete ribosome",
  "Step 3 — tRNA delivers next amino acid into the A site, peptide bond forms",
  "Step 4 — translocation: ribosome shifts one codon, chain grows",
  "Step 5 — stop codon reached, release factor binds, polypeptide released"
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
  document.getElementById('aa3').setAttribute('opacity', step >= 4 ? '1' : '0');
  document.getElementById('releaseFactor').classList.toggle('on', step >= 5);
  document.getElementById('releaseFactor').classList.toggle('pulse', step === 5);
  document.querySelector('svg').classList.toggle('released', step >= 5);
  document.getElementById('ribosomeGroup').style.transform = step >= 5 ? 'translateX(200px)' : (step >= 4 ? 'translateX(50px)' : 'translateX(0)');
}
function stepFwd() { if (step < 5) step++; render(); }
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
            "height": 560,
            "blurb": (
                "Seven visually distinct stages: interphase, prophase, "
                "prometaphase, metaphase, anaphase, telophase, cytokinesis."
            ),
        },
        # "Technical": not built yet — add a MITOSIS_TECHNICAL = '''...'''
        # fragment above and an entry here (checkpoints, cohesin/separase,
        # kinetochores, the actomyosin contractile ring) to extend.
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
        # "Technical": not built yet — add a TRANSCRIPTION_TECHNICAL = '''...'''
        # fragment (sigma factor / general transcription factors, TATA box,
        # transcription bubble mechanics, 5' capping) to extend.
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
        # "Technical": not built yet — add a TRANSLATION_TECHNICAL = '''...'''
        # fragment (wobble base pairing, EF-Tu/EF-G, ribosomal frameshifting,
        # signal peptides for ER targeting) to extend.
    },
}

st.title("Molecular Mechanisms — Interactive Explainers")
st.caption(
    "Step-through animations of core cell biology mechanisms. "
    "Use the controls in the sidebar to pick a mechanism and detail level."
)

with st.sidebar:
    st.header("Choose a mechanism")
    topic = st.radio("Mechanism", list(REGISTRY.keys()))
    levels_available = list(REGISTRY[topic].keys())
    level = st.radio("Detail level", levels_available)

entry = REGISTRY[topic][level]
st.subheader(f"{topic} — {level}")
st.write(entry["blurb"])

st.components.v1.html(COMMON_STYLE + entry["fragment"], height=entry["height"], scrolling=False)

st.divider()
st.caption(
    "Every mechanism is a string constant above (e.g. GPCR_GENERAL) plus one "
    "REGISTRY entry — edit a constant's SVG/CSS/JS to change a diagram, or "
    "add a new constant + registry entry to add a new mechanism."
)
