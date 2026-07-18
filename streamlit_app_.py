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
  "Step 0 of 3 — intact double helix",
  "Step 1 of 3 — helicase unwinds the strands",
  "Step 2 of 3 — polymerase synthesizes new strands",
  "Step 3 of 3 — two daughter helices formed"
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
  "Step 0 of 5 — mRNA alone, start codon marked",
  "Step 1 of 5 — small subunit binds, initiator tRNA pairs with start codon",
  "Step 2 of 5 — large subunit joins, forming the complete ribosome",
  "Step 3 of 5 — tRNA delivers next amino acid into the A site, peptide bond forms",
  "Step 4 of 5 — translocation: ribosome shifts one codon, chain grows",
  "Step 5 of 5 — stop codon reached, release factor binds, polypeptide released"
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
# MEIOSIS_GENERAL  (source: meiosis.html)
# ---------------------------------------------------------------------------
MEIOSIS_GENERAL = '''
<h2 class="sr-only">Interactive diagram of meiosis showing homolog pairing, crossing over, two rounds of division, and four haploid daughter cells.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #pair1, #pair2 { transition: transform 1s ease; }
  .anaphase1 #pair1 { transform: translateX(-60px); }
  .anaphase1 #pair2 { transform: translateX(60px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 360" role="img">
<title>Meiosis, general view</title>
<desc>A diploid cell with paired homologous chromosomes undergoes crossing over, aligns as tetrads, separates homologs in meiosis I, then separates sister chromatids in meiosis II, producing four genetically distinct haploid cells.</desc>

<ellipse cx="340" cy="170" rx="220" ry="130" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<text class="ts" x="340" y="28" text-anchor="middle" id="stageLabel">Diploid cell, homologs unpaired</text>

<g id="pair1">
<path d="M300 150 L320 170 M320 150 L300 170" stroke="#378ADD" stroke-width="4" stroke-linecap="round"/>
<path id="homolog1b" d="M300 190 L320 210 M320 190 L300 210" stroke="#85B7EB" stroke-width="4" stroke-linecap="round" opacity="0"/>
</g>
<g id="pair2">
<path d="M360 150 L380 170 M380 150 L360 170" stroke="#D85A30" stroke-width="4" stroke-linecap="round"/>
<path id="homolog2b" d="M360 190 L380 210 M380 190 L360 210" stroke="#F0997B" stroke-width="4" stroke-linecap="round" opacity="0"/>
</g>

<g id="chiasma" class="stg">
<circle cx="330" cy="180" r="4" fill="#EF9F27"/>
<text class="ts" x="330" y="230" text-anchor="middle">Crossing over (chiasma)</text>
</g>

<g id="spindle" class="stg">
<circle cx="140" cy="170" r="6" class="c-amber"/>
<circle cx="540" cy="170" r="6" class="c-amber"/>
</g>

<g id="fourCells" class="stg">
<ellipse cx="180" cy="290" rx="55" ry="38" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<ellipse cx="280" cy="290" rx="55" ry="38" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<ellipse cx="400" cy="290" rx="55" ry="38" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<ellipse cx="500" cy="290" rx="55" ry="38" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<text class="ts" x="340" y="345" text-anchor="middle">Four haploid cells, each genetically distinct</text>
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
  "Diploid cell, homologs unpaired",
  "Prophase I — homologs pair (synapsis) and cross over",
  "Metaphase I — homolog pairs (tetrads) align at the equator",
  "Anaphase I — homologs separate to opposite poles (chromatids stay joined)",
  "Meiosis II — sister chromatids finally separate, like mitosis",
  "Result — four haploid cells, each genetically distinct"
];
function render() {
  document.getElementById('stageLabel').textContent = labels[step];
  document.getElementById('stepLabel').textContent = 'Step ' + step + ' of 5';
  document.getElementById('homolog1b').setAttribute('opacity', step >= 1 ? '1' : '0');
  document.getElementById('homolog2b').setAttribute('opacity', step >= 1 ? '1' : '0');
  document.getElementById('chiasma').classList.toggle('on', step === 1);
  document.getElementById('spindle').classList.toggle('on', step >= 2 && step <= 3);
  document.querySelector('svg').classList.toggle('anaphase1', step === 3);
  document.getElementById('fourCells').classList.toggle('on', step >= 4);
  const opac = step >= 4 ? '0.15' : '1';
  document.getElementById('pair1').style.opacity = opac;
  document.getElementById('pair2').style.opacity = opac;
}
function stepFwd() { if (step < 5) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
</script>
'''


# ---------------------------------------------------------------------------
# APOPTOSIS_GENERAL  (source: apoptosis.html)
# ---------------------------------------------------------------------------
APOPTOSIS_GENERAL = '''
<h2 class="sr-only">Interactive diagram of apoptosis: a death ligand triggers a caspase cascade that dismantles the cell into apoptotic bodies, which are cleared by a phagocyte.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #cellBody { transition: d 0.8s ease, opacity .6s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Apoptosis, general view</title>
<desc>A death ligand binds a receptor on the cell surface, activating an initiator caspase that in turn activates executioner caspases, which fragment DNA and break down the cytoskeleton, causing the cell to bleb into apoptotic bodies that are engulfed by a phagocyte.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>

<ellipse id="cellBody" cx="200" cy="170" rx="90" ry="80" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<circle cx="200" cy="170" r="28" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="3 3"/>
<text class="ts" x="200" y="270" text-anchor="middle">Nucleus intact</text>

<g id="ligand" class="stg">
<circle cx="200" cy="60" r="8" fill="#E24B4A"/>
<text class="ts" x="200" y="42" text-anchor="middle">Death ligand</text>
<line x1="200" y1="70" x2="200" y2="90" stroke="#E24B4A" stroke-width="1.5" marker-end="url(#arrow)"/>
</g>

<g id="caspase8" class="stg">
<circle cx="200" cy="105" r="14" class="c-amber"/>
<text class="ts" x="200" y="105" text-anchor="middle" dominant-baseline="central">C8</text>
</g>

<g id="caspase3" class="stg">
<circle cx="260" cy="140" r="14" class="c-red"/>
<text class="ts" x="260" y="140" text-anchor="middle" dominant-baseline="central">C3</text>
<text class="ts" x="290" y="140" text-anchor="middle">Executioner</text>
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
<text class="ts" x="580" y="170" text-anchor="middle" dominant-baseline="central">Phagocyte</text>
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
  "Step 0 of 4 — healthy cell, no death signal",
  "Step 1 of 4 — death ligand binds receptor, initiator caspase-8 activates",
  "Step 2 of 4 — caspase-8 activates executioner caspase-3",
  "Step 3 of 4 — caspase-3 fragments DNA, breaks down the cytoskeleton, cell blebs into apoptotic bodies",
  "Step 4 of 4 — apoptotic bodies engulfed by a phagocyte, no inflammation"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('ligand').classList.toggle('on', step >= 1);
  document.getElementById('caspase8').classList.toggle('on', step >= 1);
  document.getElementById('caspase8').classList.toggle('pulse', step === 1);
  document.getElementById('caspase3').classList.toggle('on', step >= 2);
  document.getElementById('caspase3').classList.toggle('pulse', step === 2);
  document.getElementById('damage').classList.toggle('on', step >= 3);
  document.getElementById('cellBody').style.opacity = step >= 3 ? '0.15' : '1';
  document.getElementById('bodies').classList.toggle('on', step >= 3);
  document.getElementById('phagocyte').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
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
  #vesicleGroup { transition: transform 1s ease; }
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

<path id="membraneDip" d="M150 150 Q200 150 200 150 Q200 150 250 150" stroke="var(--t)" stroke-width="2" fill="none"/>
<g id="coat" class="stg">
<circle cx="170" cy="145" r="4" class="c-purple"/>
<circle cx="230" cy="145" r="4" class="c-purple"/>
<circle cx="200" cy="130" r="4" class="c-purple"/>
<text class="ts" x="200" y="115" text-anchor="middle">Clathrin coat</text>
</g>

<g id="vesicleGroup">
<circle id="vesicle" cx="200" cy="150" r="0" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<circle id="vcargo" cx="200" cy="150" r="0" fill="#EF9F27"/>
</g>

<g id="snare" class="stg">
<rect x="185" y="140" width="30" height="14" rx="4" class="c-teal"/>
<text class="ts" x="200" y="127" text-anchor="middle">SNARE docking</text>
</g>

<g id="released" class="stg">
<circle cx="200" cy="90" r="9" fill="#EF9F27"/>
<text class="ts" x="200" y="72" text-anchor="middle">Cargo released</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
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
  document.getElementById('cargoOutside').classList.toggle('on', mode === 'endo' ? step <= 1 : step === 3);
  document.getElementById('coat').classList.toggle('on', mode === 'endo' && step >= 1 && step <= 2);
  document.getElementById('snare').classList.toggle('on', mode === 'exo' && step === 1);
  document.getElementById('released').classList.toggle('on', mode === 'exo' && step >= 2);

  const v = document.getElementById('vesicle');
  const vc = document.getElementById('vcargo');
  let r = 0, cy = 150, cr = 0;
  if (mode === 'endo') {
    if (step === 1) { r = 18; cy = 150; cr = 8; }
    else if (step === 2) { r = 18; cy = 150; cr = 8; }
    else if (step === 3) { r = 18; cy = 220; cr = 8; }
  } else {
    if (step === 0) { r = 18; cy = 220; cr = 8; }
    else if (step === 1) { r = 18; cy = 150; cr = 8; }
    else if (step === 2) { r = 18; cy = 150; cr = 8; }
    else { r = 0; cr = 0; }
  }
  v.setAttribute('r', r); v.setAttribute('cy', cy);
  vc.setAttribute('r', cr); vc.setAttribute('cy', cy);
}
function stepFwd() { if (step < 3) step++; render(); }
function reset() { step = 0; render(); }
setMode('endo');
</script>
'''


# ---------------------------------------------------------------------------
# ENZYME_KINETICS_GENERAL  (source: enzyme_kinetics.html)
# ---------------------------------------------------------------------------
ENZYME_KINETICS_GENERAL = '''
<h2 class="sr-only">Interactive diagram of enzyme catalysis and allosteric inhibition: substrate binds the active site via induced fit, is converted to product, and an allosteric inhibitor can distort the active site to block binding.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #substrateGroup { transition: transform 1s ease, opacity .5s ease; }
  .bound #substrateGroup { transform: translate(15px, 5px); }
  #enzymeBody { transition: d 0.6s ease; }
  .inhibited #enzymeBody { fill: var(--surface-1); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Enzyme catalysis and allosteric inhibition</title>
<desc>A substrate approaches an enzyme's active site, binds via induced fit, is converted into product and released. Separately, an allosteric inhibitor can bind a distinct regulatory site, distorting the active site so the substrate no longer fits, providing feedback inhibition.</desc>

<path id="enzymeBody" d="M180 150 Q210 90 280 110 Q340 100 360 150 Q340 200 280 190 Q210 210 180 150 Z" class="c-teal" stroke-width="0.5"/>
<circle id="activeSite" cx="270" cy="150" r="16" fill="none" stroke="#EF9F27" stroke-width="2" stroke-dasharray="3 3"/>
<text class="ts" x="270" y="230" text-anchor="middle">Enzyme</text>

<g id="substrateGroup">
<rect x="100" y="140" width="26" height="20" rx="4" fill="#EF9F27"/>
<text class="ts" x="113" y="122" text-anchor="middle" id="substrateLabel">Substrate</text>
</g>

<g id="product" class="stg">
<circle cx="420" cy="140" r="8" fill="#1D9E75"/>
<circle cx="440" cy="155" r="8" fill="#1D9E75"/>
<text class="ts" x="430" y="185" text-anchor="middle">Product</text>
</g>

<g id="allostericSite" class="stg">
<circle cx="200" cy="180" r="10" fill="none" stroke="#E24B4A" stroke-width="1.5" stroke-dasharray="2 2"/>
<text class="ts" x="200" y="205" text-anchor="middle">Allosteric site</text>
</g>
<g id="inhibitor" class="stg">
<circle cx="200" cy="180" r="9" fill="#E24B4A"/>
<text class="ts" x="200" y="255" text-anchor="middle">Inhibitor bound — active site distorted, substrate blocked</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
  <button onclick="reset()">Reset</button>
  <button onclick="toggleInhibitor()">Toggle allosteric inhibitor</button>
  <span id="stepLabel">Step 0 of 3</span>
</div>

<script>
let step = 0;
let inhibited = false;
const labels = [
  "Step 0 of 3 — substrate approaches the active site",
  "Step 1 of 3 — induced fit: substrate binds, enzyme-substrate complex forms",
  "Step 2 of 3 — reaction catalyzed, product formed",
  "Step 3 of 3 — product released, enzyme resets for another cycle"
];
function render() {
  document.getElementById('stepLabel').textContent = inhibited ? "Allosteric inhibitor bound — substrate can't bind" : labels[step];
  const svg = document.querySelector('svg');
  svg.classList.toggle('bound', step >= 1 && step < 3 && !inhibited);
  document.getElementById('substrateLabel').textContent = step >= 1 ? 'Bound substrate' : 'Substrate';
  document.getElementById('substrateGroup').style.opacity = (step >= 3 || inhibited) ? '0' : '1';
  document.getElementById('activeSite').classList.toggle('pulse', step === 1 && !inhibited);
  document.getElementById('product').classList.toggle('on', step >= 2 && !inhibited);
}
function stepFwd() { if (step < 3 && !inhibited) step++; render(); }
function reset() { step = 0; render(); }
function toggleInhibitor() {
  inhibited = !inhibited;
  step = 0;
  document.getElementById('allostericSite').classList.toggle('on', true);
  document.getElementById('inhibitor').classList.toggle('on', inhibited);
  document.querySelector('svg').classList.toggle('inhibited', inhibited);
  render();
}
render();
</script>
'''


# ---------------------------------------------------------------------------
# MEMBRANE_TRANSPORT_GENERAL  (source: membrane_transport.html)
# ---------------------------------------------------------------------------
MEMBRANE_TRANSPORT_GENERAL = '''
<h2 class="sr-only">Interactive diagram of membrane transport modes, each shown as an actual step-through: simple diffusion, facilitated diffusion through a channel, and active transport by an ATP-powered pump.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #molecule { transition: transform 1s ease, opacity .4s ease; }
  .rowbtns { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px; }
  .rowbtns button.active { border-color: var(--border-accent); color: var(--text-accent); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>

<div class="rowbtns">
  <button id="btnSimple" onclick="setMode('simple')">Simple diffusion</button>
  <button id="btnFacil" onclick="setMode('facil')">Facilitated diffusion</button>
  <button id="btnActive" onclick="setMode('active')">Active transport</button>
</div>

<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Modes of membrane transport, stepped</title>
<desc>Each transport mode is shown as a sequence: a molecule approaches the membrane, crosses it by a different mechanism depending on the mode, and arrives on the other side. Simple diffusion passes directly through the lipid bilayer. Facilitated diffusion passes through a channel protein. Active transport is pumped through against its gradient, consuming ATP.</desc>

<rect x="280" y="40" width="120" height="220" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="340" y="30">Membrane</text>
<text class="ts" x="80" y="30" id="outsideLabel">Outside — high concentration</text>
<text class="ts" x="500" y="30" id="insideLabel">Inside — low concentration</text>

<g id="channelProt" class="stg">
<rect x="320" y="60" width="40" height="180" rx="16" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="340" y="255" text-anchor="middle">Channel protein</text>
</g>

<g id="pump" class="stg">
<rect x="310" y="60" width="60" height="180" rx="20" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="340" y="255" text-anchor="middle">Pump</text>
<circle id="atp" cx="420" cy="150" r="12" class="c-amber" opacity="0"/>
<text class="ts" x="420" y="150" text-anchor="middle" dominant-baseline="central" id="atpLabel" opacity="0">ATP</text>
</g>

<circle id="molecule" cx="120" cy="150" r="10" fill="#1D9E75"/>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
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
  }
};
function maxStep() { return mode === 'active' ? 4 : 3; }
function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnSimple').classList.toggle('active', m === 'simple');
  document.getElementById('btnFacil').classList.toggle('active', m === 'facil');
  document.getElementById('btnActive').classList.toggle('active', m === 'active');
  document.getElementById('channelProt').classList.toggle('on', m === 'facil');
  document.getElementById('pump').classList.toggle('on', m === 'active');
  document.getElementById('insideLabel').textContent = m === 'active' ? 'Inside — becomes higher concentration' : 'Inside — low concentration';
  render();
}
function render() {
  const cfg = configs[mode];
  document.getElementById('stepLabel').textContent = cfg.labels[step];
  let x;
  if (mode === 'active') {
    x = step === 0 ? 120 : step === 1 ? 320 : step === 2 ? 340 : step === 3 ? 340 : 560;
    document.getElementById('atp').setAttribute('opacity', step === 1 ? '1' : '0');
    document.getElementById('atpLabel').setAttribute('opacity', step === 1 ? '1' : '0');
  } else {
    x = step === 0 ? 120 : step === 1 ? 300 : step === 2 ? 340 : 560;
  }
  document.getElementById('molecule').style.transform = `translateX(${x - 120}px)`;
}
function stepFwd() { if (step < maxStep()) step++; render(); }
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
<text class="th" x="440" y="240" text-anchor="middle">Activated — proliferates into helper T cells</text>
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
  #spermGroup { transition: transform 1s ease; }
  .fused #spermGroup { transform: translateX(70px); opacity: 0; }
  #zonaLayer { transition: stroke 0.6s ease, stroke-width 0.6s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Fertilization, general view</title>
<desc>A sperm cell approaches the egg, undergoes the acrosomal reaction to penetrate the zona pellucida, fuses its membrane with the egg, triggers cortical granule release that hardens the zona pellucida to block additional sperm, and the two pronuclei fuse into a zygote.</desc>

<circle cx="380" cy="150" r="90" class="c-amber"/>
<circle id="zonaLayer" cx="380" cy="150" r="90" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<text class="th" x="380" y="150" text-anchor="middle" dominant-baseline="central">Egg</text>
<text class="ts" x="380" y="255" text-anchor="middle">Zona pellucida</text>

<g id="spermGroup">
<path d="M150 150 L200 150" stroke="var(--t)" stroke-width="2" stroke-linecap="round"/>
<circle cx="145" cy="150" r="10" fill="#378ADD"/>
<text class="ts" x="145" y="130" text-anchor="middle">Sperm</text>
</g>

<g id="acrosome" class="stg">
<circle cx="200" cy="150" r="5" fill="#EF9F27"/>
<text class="ts" x="200" y="185" text-anchor="middle">Acrosomal enzymes penetrate zona</text>
</g>

<g id="corticalReaction" class="stg">
<circle cx="330" cy="100" r="4" fill="#B91C1C"/>
<circle cx="350" cy="200" r="4" fill="#B91C1C"/>
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
  document.querySelector('svg').classList.toggle('fused', step >= 2);
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

<path id="innerFold" d="M340 270 Q340 270 340 270" fill="none" stroke="#D85A30" stroke-width="3" class="stg"/>

<g id="archenteron" class="stg">
<ellipse cx="340" cy="190" rx="45" ry="60" fill="none" stroke="#D85A30" stroke-width="2"/>
<text class="ts" x="340" y="190" text-anchor="middle" dominant-baseline="central">Archenteron</text>
</g>

<g id="layers" class="stg">
<text class="ts" x="490" y="90" text-anchor="middle">Ectoderm (outer)</text>
<circle cx="450" cy="90" r="5" fill="#378ADD"/>
<text class="ts" x="490" y="160" text-anchor="middle">Mesoderm (middle)</text>
<circle cx="450" cy="160" r="5" fill="#7F77DD"/>
<text class="ts" x="490" y="230" text-anchor="middle">Endoderm (inner)</text>
<circle cx="450" cy="230" r="5" fill="#D85A30"/>
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
const folds = [
  "M340 270 Q340 270 340 270",
  "M340 270 Q340 240 340 220",
  "M340 270 Q300 220 320 180 Q340 150 340 190",
  "M340 270 Q300 220 320 180 Q340 150 340 190"
];
function render() {
  document.getElementById('stageLabel').textContent = labels[step];
  document.getElementById('stepLabel').textContent = 'Step ' + step + ' of 3';
  document.getElementById('blastopore').classList.toggle('on', step >= 1);
  document.getElementById('innerFold').classList.toggle('on', step >= 1);
  document.getElementById('innerFold').setAttribute('d', folds[step]);
  document.getElementById('archenteron').classList.toggle('on', step >= 2);
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
<h2 class="sr-only">Interactive diagram of a neuronal action potential: resting potential, depolarization, repolarization, and propagation along the axon.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #wavefront { transition: transform 1.2s ease; }
  .propagating #wavefront { transform: translateX(220px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Action potential, general view</title>
<desc>A resting neuron membrane at negative seventy millivolts depolarizes when voltage-gated sodium channels open, reverses briefly, then repolarizes as potassium channels open, and the depolarization wave propagates along the axon.</desc>

<line x1="30" y1="130" x2="650" y2="130" stroke="var(--t)" stroke-width="3" stroke-linecap="round"/>
<text class="ts" x="60" y="115">Axon membrane</text>

<g id="voltageTrace">
<path id="traceLine" d="M30 200 L650 200" stroke="#378ADD" stroke-width="2.5" fill="none"/>
</g>
<text class="ts" x="60" y="230" id="voltageLabel">Resting potential: −70 mV</text>

<g id="naChannels" class="stg">
<rect x="130" y="120" width="16" height="20" fill="#EF9F27"/>
<text class="ts" x="138" y="105" text-anchor="middle">Na+ channels open</text>
</g>

<g id="kChannels" class="stg">
<rect x="170" y="120" width="16" height="20" fill="#378ADD"/>
<text class="ts" x="178" y="105" text-anchor="middle">K+ channels open</text>
</g>

<g id="wavefront" class="stg">
<circle cx="140" cy="130" r="10" fill="#E24B4A"/>
<text class="ts" x="140" y="160" text-anchor="middle">Depolarization wave</text>
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
  "Step 0 of 4 — resting potential, Na/K pump maintains -70 mV",
  "Step 1 of 4 — threshold reached, Na+ channels open, rapid depolarization",
  "Step 2 of 4 — peak (~+30 mV), Na+ channels inactivate, K+ channels open",
  "Step 3 of 4 — repolarization as K+ exits, brief undershoot",
  "Step 4 of 4 — wave propagates down the axon to the next segment"
];
const traces = [
  "M30 200 L650 200",
  "M30 200 L120 200 L140 90 L160 200 L650 200",
  "M30 200 L120 200 L140 90 L160 200 L650 200",
  "M30 200 L120 200 L140 90 L160 215 L180 200 L650 200",
  "M30 200 L340 200 L360 90 L380 215 L400 200 L650 200"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('voltageLabel').textContent = step === 0 ? 'Resting potential: −70 mV' :
    step === 1 ? 'Depolarizing toward +30 mV' :
    step === 2 ? 'Peak reached, Na+ channels inactivating' :
    step === 3 ? 'Repolarizing, brief undershoot' : 'Wave moving to next segment';
  document.getElementById('traceLine').setAttribute('d', traces[step]);
  document.getElementById('naChannels').classList.toggle('on', step === 1 || step === 2);
  document.getElementById('kChannels').classList.toggle('on', step >= 2 && step <= 3);
  document.getElementById('wavefront').classList.toggle('on', step >= 1);
  document.querySelector('svg').classList.toggle('propagating', step === 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
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
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #actinLeft, #actinRight { transition: transform 1s ease; }
  .contracted #actinLeft { transform: translateX(40px); }
  .contracted #actinRight { transform: translateX(-40px); }
  #tropomyosin { transition: transform 0.6s ease; }
  .exposed #tropomyosin { transform: translateY(6px); opacity: 0.3; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 260" role="img">
<title>Sliding filament model of muscle contraction</title>
<desc>Calcium released from the sarcoplasmic reticulum binds troponin, moving tropomyosin to expose myosin-binding sites on actin. Myosin heads form cross-bridges, pull the actin filaments inward during the power stroke, and the sarcomere shortens as the Z-lines are drawn closer together.</desc>

<line x1="60" y1="130" x2="620" y2="130" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="2 2"/>
<line x1="80" y1="60" x2="80" y2="200" stroke="var(--t)" stroke-width="3"/>
<line x1="600" y1="60" x2="600" y2="200" stroke="var(--t)" stroke-width="3"/>
<text class="ts" x="80" y="50" text-anchor="middle">Z-line</text>
<text class="ts" x="600" y="50" text-anchor="middle">Z-line</text>

<rect x="250" y="115" width="180" height="30" fill="#7F77DD"/>
<text class="ts" x="340" y="105" text-anchor="middle">Myosin (thick filament)</text>

<g id="actinLeft">
<rect x="80" y="120" width="200" height="8" fill="#378ADD"/>
<rect id="tropomyosin" x="80" y="120" width="200" height="8" fill="#EF9F27" opacity="0.7"/>
</g>
<g id="actinRight">
<rect x="400" y="120" width="200" height="8" fill="#D85A30"/>
</g>
<text class="ts" x="340" y="215" text-anchor="middle">Actin (thin filaments)</text>

<g id="calcium" class="stg">
<circle class="pulse" cx="200" cy="90" r="6" fill="#639922"/>
<circle class="pulse" cx="440" cy="90" r="6" fill="#639922"/>
<text class="ts" x="340" y="75" text-anchor="middle">Ca2+ released, binds troponin</text>
</g>

<g id="crossbridge" class="stg">
<line x1="290" y1="130" x2="320" y2="130" stroke="#7F77DD" stroke-width="3"/>
<text class="ts" x="305" y="150" text-anchor="middle">Cross-bridge</text>
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
  "Step 0 of 3 — relaxed: tropomyosin blocks the myosin-binding sites on actin",
  "Step 1 of 3 — Ca2+ released, binds troponin, tropomyosin shifts to expose binding sites",
  "Step 2 of 3 — myosin heads form cross-bridges and pull actin inward (power stroke)",
  "Step 3 of 3 — sarcomere shortens, Z-lines drawn closer together"
];
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('calcium').classList.toggle('on', step >= 1);
  document.querySelector('svg').classList.toggle('exposed', step >= 1);
  document.getElementById('crossbridge').classList.toggle('on', step >= 2);
  document.querySelector('svg').classList.toggle('contracted', step >= 3);
}
function stepFwd() { if (step < 3) step++; render(); }
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
<text class="ts" x="200" y="260" text-anchor="middle">Ventricles</text>

<g id="saNode">
<circle cx="230" cy="80" r="10" class="c-amber"/>
<text class="ts" x="230" y="62" text-anchor="middle">SA node</text>
</g>

<g id="avNode" class="stg">
<circle cx="200" cy="175" r="9" class="c-purple"/>
<text class="ts" x="200" y="195" text-anchor="middle">AV node (delay)</text>
</g>

<g id="hisPurkinje" class="stg">
<line x1="200" y1="185" x2="200" y2="230" stroke="#0F6E56" stroke-width="2"/>
<line x1="200" y1="230" x2="150" y2="290" stroke="#0F6E56" stroke-width="1.5"/>
<line x1="200" y1="230" x2="250" y2="290" stroke="#0F6E56" stroke-width="1.5"/>
<text class="ts" x="200" y="245" text-anchor="middle">Bundle of His → Purkinje fibers</text>
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
  .drift { animation: drift 1.8s ease-in-out infinite; }
  @keyframes drift { 0%,100%{transform:translateY(0)} 50%{transform:translateY(6px)} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Gas exchange in the alveoli</title>
<desc>Oxygen-rich air in the alveolus diffuses down its concentration gradient into the adjacent capillary, where it binds hemoglobin in red blood cells, while carbon dioxide diffuses the opposite direction from blood into the alveolus to be exhaled.</desc>

<circle cx="220" cy="150" r="110" fill="var(--surface-1)" stroke="var(--t)" stroke-width="1.5"/>
<text class="th" x="220" y="90" text-anchor="middle">Alveolus</text>
<text class="ts" x="220" y="108" text-anchor="middle">High O2, low CO2</text>

<rect x="380" y="110" width="260" height="80" rx="30" fill="none" stroke="#B91C1C" stroke-width="3"/>
<text class="ts" x="510" y="100" text-anchor="middle">Capillary</text>
<text class="ts" x="440" y="215" text-anchor="middle">Deoxygenated blood in</text>
<text class="ts" x="580" y="215" text-anchor="middle" id="outLabel">→</text>

<g id="o2" class="stg">
<circle class="drift" cx="260" cy="140" r="7" fill="#378ADD"/>
<circle class="drift" cx="280" cy="160" r="7" fill="#378ADD" style="animation-delay:.3s"/>
<text class="ts" x="270" y="120" text-anchor="middle">O2</text>
</g>

<g id="co2" class="stg">
<circle class="drift" cx="400" cy="145" r="7" fill="#639922"/>
<circle class="drift" cx="420" cy="165" r="7" fill="#639922" style="animation-delay:.4s"/>
<text class="ts" x="410" y="185" text-anchor="middle">CO2</text>
</g>

<g id="hemoglobin" class="stg">
<circle cx="480" cy="150" r="16" fill="#B91C1C"/>
<text class="ts" x="480" y="150" text-anchor="middle" dominant-baseline="central" fill="white">Hb</text>
<text class="ts" x="480" y="175" text-anchor="middle">O2 binds hemoglobin</text>
</g>

<g id="oxygenated" class="stg">
<text class="th" x="600" y="150" text-anchor="middle">Oxygenated blood out</text>
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
function render() {
  document.getElementById('stepLabel').textContent = labels[step];
  document.getElementById('o2').classList.toggle('on', step >= 1);
  document.getElementById('co2').classList.toggle('on', step >= 2);
  document.getElementById('hemoglobin').classList.toggle('on', step >= 3);
  document.getElementById('oxygenated').classList.toggle('on', step >= 3);
}
function stepFwd() { if (step < 3) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
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
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .drift { animation: drift 1.6s ease-in-out infinite; }
  @keyframes drift { 0%{transform:translateX(0)} 100%{transform:translateX(90px)} }
  #vesicle { transition: transform 0.8s ease, opacity 0.5s ease; }
  .released #vesicle { transform: translateY(20px); opacity: 0; }
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

<circle id="vesicle" cx="140" cy="150" r="22" fill="none" stroke="#7F77DD" stroke-width="2"/>
<circle cx="132" cy="145" r="3" fill="#7F77DD"/>
<circle cx="148" cy="150" r="3" fill="#7F77DD"/>
<circle cx="138" cy="158" r="3" fill="#7F77DD"/>

<g id="neurotransmitter" class="stg">
<circle class="drift" cx="185" cy="150" r="5" fill="#7F77DD"/>
<circle class="drift" cx="185" cy="165" r="5" fill="#7F77DD" style="animation-delay:.2s"/>
<circle class="drift" cx="185" cy="135" r="5" fill="#7F77DD" style="animation-delay:.4s"/>
</g>

<g id="receptor" class="stg">
<rect x="495" y="135" width="16" height="30" rx="4" fill="var(--surface-1)" stroke="#EF9F27" stroke-width="2"/>
<text class="ts" x="503" y="120" text-anchor="middle">Receptor</text>
</g>

<g id="response" class="stg">
<circle cx="503" cy="150" r="20" fill="none" stroke="#639922" stroke-width="2" stroke-dasharray="3 3"/>
<text class="ts" x="570" y="195" text-anchor="middle">Postsynaptic response (ion channel opens)</text>
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
  document.getElementById('neurotransmitter').classList.toggle('on', step >= 2 && step < 4);
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
  .pulse { animation: pulse 1.1s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .spin { animation: spin 1.2s linear infinite; transform-origin: 560px 150px; }
  @keyframes spin { from{transform:rotate(0)} to{transform:rotate(360deg)} }
  .drift-up { animation: driftup 1.5s ease-in-out infinite; }
  @keyframes driftup { 0%{transform:translateY(0)} 100%{transform:translateY(-60px)} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Electron transport chain and ATP synthase</title>
<desc>Electrons from NADH pass through membrane protein complexes, which pump protons into the intermembrane space, building an electrochemical gradient. Oxygen accepts electrons at the final complex, forming water. Protons flow back through ATP synthase, spinning it to catalyze ATP formation from ADP and phosphate.</desc>

<rect x="30" y="120" width="600" height="50" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="42" y="115">Inner mitochondrial membrane</text>
<text class="ts" x="42" y="100" id="imsLabel">Intermembrane space</text>
<text class="ts" x="42" y="190" id="matrixLabel">Matrix</text>

<rect x="120" y="110" width="30" height="70" rx="8" class="c-purple"/>
<text class="ts" x="135" y="200" text-anchor="middle">I</text>
<rect x="220" y="110" width="30" height="70" rx="8" class="c-teal"/>
<text class="ts" x="235" y="200" text-anchor="middle">III</text>
<rect x="320" y="110" width="30" height="70" rx="8" class="c-coral"/>
<text class="ts" x="335" y="200" text-anchor="middle">IV</text>

<g id="electron" class="stg">
<circle cx="100" cy="145" r="6" fill="#EF9F27"/>
<text class="ts" x="100" y="128" text-anchor="middle">e- from NADH</text>
</g>

<g id="protons" class="stg">
<circle class="drift-up" cx="135" cy="115" r="4" fill="#B91C1C"/>
<circle class="drift-up" cx="235" cy="115" r="4" fill="#B91C1C" style="animation-delay:.3s"/>
<circle class="drift-up" cx="335" cy="115" r="4" fill="#B91C1C" style="animation-delay:.6s"/>
<text class="ts" x="235" y="70" text-anchor="middle">H+ pumped into intermembrane space</text>
</g>

<g id="oxygen" class="stg">
<circle cx="380" cy="145" r="10" fill="#378ADD"/>
<text class="ts" x="380" y="200" text-anchor="middle">O2 + e- → H2O</text>
</g>

<g id="atpSynthase">
<rect x="545" y="105" width="30" height="80" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<circle id="rotor" class="c-amber" cx="560" cy="150" r="14"/>
<text class="ts" x="560" y="200" text-anchor="middle">ATP synthase</text>
</g>

<g id="atpOut" class="stg">
<text class="th" x="560" y="90" text-anchor="middle">ADP + Pi → ATP</text>
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
  document.getElementById('electron').classList.toggle('on', step >= 0 && step <= 1);
  document.getElementById('protons').classList.toggle('on', step >= 1 && step <= 2);
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
# BLOOD_CLOTTING_GENERAL  (source: clotting.html)
# ---------------------------------------------------------------------------
BLOOD_CLOTTING_GENERAL = '''
<h2 class="sr-only">Interactive diagram of hemostasis: platelets plug an injured vessel, then the coagulation cascade converts fibrinogen into a fibrin mesh that stabilizes the clot.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>Hemostasis, general view</title>
<desc>Vessel injury exposes collagen, platelets adhere and aggregate to form a temporary plug, the coagulation cascade converges on thrombin, thrombin converts fibrinogen into fibrin strands, and the fibrin mesh stabilizes the clot.</desc>

<path d="M60 150 L300 150" stroke="#B91C1C" stroke-width="18" stroke-linecap="round"/>
<path id="injuryGap" d="M300 150 L380 150" stroke="#B91C1C" stroke-width="18" stroke-linecap="round" stroke-dasharray="0 0"/>
<path d="M380 150 L620 150" stroke="#B91C1C" stroke-width="18" stroke-linecap="round"/>
<text class="ts" x="340" y="120" text-anchor="middle">Vessel injury — collagen exposed</text>

<g id="platelets" class="stg">
<circle cx="320" cy="150" r="10" fill="#EF9F27"/>
<circle cx="340" cy="145" r="10" fill="#EF9F27"/>
<circle cx="360" cy="152" r="10" fill="#EF9F27"/>
<circle cx="335" cy="160" r="10" fill="#EF9F27"/>
<text class="ts" x="340" y="190" text-anchor="middle">Platelet plug</text>
</g>

<g id="cascade" class="stg">
<text class="ts" x="340" y="230" text-anchor="middle">Coagulation cascade → thrombin</text>
</g>

<g id="fibrin" class="stg">
<path d="M310 130 L370 170 M320 175 L365 130 M300 150 L385 150" stroke="#7F77DD" stroke-width="2"/>
<text class="ts" x="340" y="260" text-anchor="middle">Fibrinogen → fibrin mesh</text>
</g>

<g id="stableClot" class="stg">
<circle cx="340" cy="150" r="45" fill="none" stroke="#639922" stroke-width="2" stroke-dasharray="4 3"/>
<text class="th" x="340" y="280" text-anchor="middle">Stable clot</text>
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

<rect x="30" y="130" width="620" height="40" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="42" y="125">Bloodstream</text>
<text class="ts" x="340" y="155" text-anchor="middle" id="glucoseLabel">Blood glucose: normal</text>

<g id="pancreas">
<ellipse cx="150" cy="80" rx="55" ry="35" class="c-amber"/>
<text class="ts" x="150" y="80" text-anchor="middle" dominant-baseline="central" id="pancreasLabel">Pancreas</text>
</g>

<g id="hormone" class="stg">
<circle cx="220" cy="110" r="8" fill="#7F77DD"/>
<text class="ts" x="220" y="130" text-anchor="middle" id="hormoneLabel">Insulin</text>
</g>

<g id="targetOrgan" class="stg">
<rect x="480" y="60" width="100" height="60" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="530" y="95" text-anchor="middle" id="organLabel">Body cells</text>
</g>

<g id="effect" class="stg">
<text class="ts" x="530" y="140" text-anchor="middle" id="effectLabel">GLUT4 uptake ↑</text>
</g>

<g id="resultArrow" class="stg">
<text class="ts" x="340" y="200" text-anchor="middle" id="resultLabel">Blood glucose falls back to setpoint</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
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
  glucoseSteps: ['Blood glucose: high', 'Blood glucose: high, insulin rising', 'Blood glucose: falling', 'Blood glucose: back to setpoint']
};
const configLow = {
  pancreasLabel: 'Alpha cells sense low glucose',
  hormoneLabel: 'Glucagon released',
  organLabel: 'Liver',
  effectLabel: 'Glycogen broken down, glucose released',
  resultLabel: 'Blood glucose rises back to setpoint',
  glucoseSteps: ['Blood glucose: low', 'Blood glucose: low, glucagon rising', 'Blood glucose: rising', 'Blood glucose: back to setpoint']
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
  render();
}
function render() {
  const cfg = mode === 'high' ? configHigh : configLow;
  document.getElementById('glucoseLabel').textContent = cfg.glucoseSteps[step];
  document.getElementById('stepLabel').textContent = 'Step ' + step + ' of 3';
  document.getElementById('hormone').classList.toggle('on', step >= 1);
  document.getElementById('hormone').classList.toggle('pulse', step === 1);
  document.getElementById('targetOrgan').classList.toggle('on', step >= 2);
  document.getElementById('effect').classList.toggle('on', step >= 2);
  document.getElementById('resultArrow').classList.toggle('on', step >= 3);
}
function stepFwd() { if (step < 3) step++; render(); }
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
  #furrow { transition: transform 1s ease; }
  .constricted #furrow { transform: scaleY(0.3); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Mitosis, technical view</title>
<desc>Cohesin rings hold sister chromatids together. Kinetochores attach to spindle microtubules from both poles; the spindle assembly checkpoint blocks progression until every chromosome is bi-oriented and under tension. Once satisfied, the anaphase-promoting complex triggers separase to cleave cohesin, sister chromatids separate, and an actomyosin contractile ring pinches the cell in two during cytokinesis.</desc>

<ellipse cx="340" cy="170" rx="220" ry="130" fill="none" stroke="var(--t)" stroke-width="1.5"/>

<g id="chromLeft">
<path d="M320 150 L340 170 M340 150 L320 170" stroke="#378ADD" stroke-width="4" stroke-linecap="round"/>
<circle id="cohesinL" cx="330" cy="160" r="3" fill="#EF9F27"/>
</g>
<g id="chromRight">
<path d="M340 150 L360 170 M360 150 L340 170" stroke="#D85A30" stroke-width="4" stroke-linecap="round"/>
<circle id="cohesinR" cx="350" cy="160" r="3" fill="#EF9F27"/>
</g>
<line id="cohesinLink" x1="330" y1="160" x2="350" y2="160" stroke="#EF9F27" stroke-width="2"/>

<g id="kinetochores" class="stg">
<circle cx="330" cy="145" r="4" class="c-purple"/>
<circle cx="350" cy="145" r="4" class="c-purple"/>
<text class="ts" x="340" y="128" text-anchor="middle">Kinetochores</text>
</g>

<g id="spindleSearching" class="stg">
<line x1="140" y1="170" x2="325" y2="150" stroke="var(--t)" stroke-width="0.75" stroke-dasharray="3 3" opacity="0.5"/>
<line x1="540" y1="170" x2="355" y2="150" stroke="var(--t)" stroke-width="0.75" stroke-dasharray="3 3" opacity="0.5"/>
<text class="ts" x="340" y="90" text-anchor="middle" id="sacLabel">SAC active — anaphase blocked</text>
</g>

<g id="spindleAttached" class="stg">
<line x1="140" y1="170" x2="325" y2="150" stroke="var(--t)" stroke-width="1"/>
<line x1="540" y1="170" x2="355" y2="150" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="340" y="90" text-anchor="middle">Bi-oriented, under tension — SAC satisfied</text>
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
  #mrnaTail { transition: stroke-dasharray 1s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Transcription initiation, technical view</title>
<desc>TFIID recognizes and binds the TATA box, other general transcription factors assemble into the pre-initiation complex, TFIIH's helicase activity opens the DNA to form the transcription bubble, RNA polymerase II begins synthesizing mRNA, and the 5' end is capped with a modified guanine nucleotide co-transcriptionally.</desc>

<line x1="30" y1="180" x2="630" y2="180" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<line x1="30" y1="200" x2="630" y2="200" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>

<rect id="tataBox" x="90" y="170" width="40" height="40" fill="none" stroke="#EF9F27" stroke-width="1.5" stroke-dasharray="3 3"/>
<text class="ts" x="110" y="162" text-anchor="middle">TATA box</text>

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
<text class="ts" x="150" y="240" text-anchor="middle">TFIIH unwinds DNA — transcription bubble</text>
</g>

<g id="rnapGroup">
<circle cx="150" cy="190" r="18" class="c-purple"/>
<text class="ts" x="150" y="190" text-anchor="middle" dominant-baseline="central">Pol II</text>
</g>

<g id="mrna" class="stg">
<path id="mrnaTail" d="M150 158 Q200 140 350 135" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<circle id="capG" cx="150" cy="158" r="6" fill="#B91C1C" opacity="0"/>
<text class="ts" x="150" y="140" text-anchor="middle" id="capLabel" opacity="0">5' cap</text>
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
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #ribosomeGroup { transition: transform 1s ease; }
  .translocated #ribosomeGroup { transform: translateX(40px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Translation elongation, technical view</title>
<desc>EF-Tu bound to GTP delivers aminoacyl-tRNA to the ribosome's A site, where codon-anticodon pairing is checked, including wobble pairing at the third codon position. After GTP hydrolysis and accommodation, the ribozyme peptidyl transferase forms a peptide bond, and EF-G bound to GTP drives translocation, ratcheting the ribosome one codon forward. If a signal sequence emerges, the signal recognition particle targets the whole complex to the ER membrane.</desc>

<line x1="30" y1="240" x2="650" y2="240" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>

<g id="ribosomeGroup">
<ellipse cx="200" cy="230" rx="55" ry="20" class="c-gray"/>
<ellipse cx="200" cy="200" rx="55" ry="26" class="c-purple"/>
<rect x="185" y="222" width="18" height="16" rx="3" fill="none" stroke="var(--t)" stroke-width="0.5"/>
<rect x="215" y="222" width="18" height="16" rx="3" fill="none" stroke="var(--t)" stroke-width="0.5"/>
<text class="ts" x="200" y="185" text-anchor="middle">Ribosome</text>
</g>

<g id="efTu" class="stg">
<circle cx="260" cy="150" r="12" class="c-amber"/>
<text class="ts" x="260" y="150" text-anchor="middle" dominant-baseline="central">EF-Tu</text>
<text class="ts" x="260" y="130" text-anchor="middle" id="wobbleLabel">Checking codon-anticodon (wobble at position 3)</text>
</g>

<g id="peptideBond" class="stg">
<circle cx="185" cy="175" r="6" class="c-coral"/>
<circle cx="200" cy="165" r="6" class="c-coral"/>
<text class="ts" x="192" y="150" text-anchor="middle">Peptidyl transferase (rRNA ribozyme)</text>
</g>

<g id="efG" class="stg">
<circle cx="230" cy="230" r="12" class="c-teal"/>
<text class="ts" x="230" y="230" text-anchor="middle" dominant-baseline="central">EF-G</text>
<text class="ts" x="230" y="255" text-anchor="middle">Drives translocation (ratchet)</text>
</g>

<g id="srp" class="stg">
<path d="M280 130 L300 110 L320 130" stroke="#B91C1C" stroke-width="2" fill="none"/>
<text class="ts" x="300" y="95" text-anchor="middle">SRP recognizes signal sequence</text>
</g>

<g id="erMembrane" class="stg">
<rect x="450" y="60" width="20" height="280" fill="var(--surface-1)" stroke="var(--border-strong)" stroke-width="0.5"/>
<text class="ts" x="460" y="50" text-anchor="middle">ER membrane</text>
<circle cx="460" cy="200" r="10" fill="none" stroke="#B91C1C" stroke-width="1.5"/>
<text class="ts" x="460" y="225" text-anchor="middle">Translocon</text>
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
  document.getElementById('erMembrane').classList.toggle('on', step >= 4);
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
            "height": 560,
            "blurb": (
                "Seven visually distinct stages: interphase, prophase, "
                "prometaphase, metaphase, anaphase, telophase, cytokinesis."
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
    "Meiosis": {
        "General": {
            "fragment": MEIOSIS_GENERAL,
            "height": 500,
            "blurb": (
                "Homologous chromosomes pair and cross over, then separate "
                "in meiosis I, and sister chromatids separate in meiosis "
                "II, producing four genetically distinct haploid cells."
            ),
        },
    },
    "Apoptosis": {
        "General": {
            "fragment": APOPTOSIS_GENERAL,
            "height": 460,
            "blurb": (
                "Extrinsic pathway: a death ligand activates initiator "
                "caspase-8, which activates executioner caspase-3, "
                "dismantling the cell into apoptotic bodies for clearance."
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
            "height": 460,
            "blurb": (
                "Substrate binds the active site by induced fit and is "
                "converted to product; a separate allosteric inhibitor "
                "can distort the active site to block binding entirely."
            ),
        },
    },
    "Membrane transport": {
        "General": {
            "fragment": MEMBRANE_TRANSPORT_GENERAL,
            "height": 440,
            "blurb": (
                "Step through a molecule crossing the membrane under each "
                "mode: straight through the bilayer (simple), through a "
                "channel (facilitated), or pumped uphill with ATP (active)."
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
    },
    "Action potential": {
        "General": {
            "fragment": ACTION_POTENTIAL_GENERAL,
            "height": 460,
            "blurb": (
                "A resting neuron at -70 mV depolarizes when voltage-gated "
                "Na+ channels open, repolarizes as K+ channels open, and "
                "the wave propagates along the axon to the next segment."
            ),
        },
    },
    "Muscle contraction": {
        "General": {
            "fragment": MUSCLE_CONTRACTION_GENERAL,
            "height": 420,
            "blurb": (
                "The sliding filament model: Ca2+ exposes myosin-binding "
                "sites on actin, cross-bridges form and pull the "
                "filaments inward, shortening the sarcomere."
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
            "height": 440,
            "blurb": (
                "Switch between the insulin loop (high glucose → uptake) "
                "and the glucagon loop (low glucose → liver releases "
                "glucose) — a classic negative feedback pair."
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
    "Cell Biology": [
        "Apoptosis",
        "Cell division (mitosis)",
        "Cell signaling (GPCR → cAMP → PKA)",
        "Endocytosis / exocytosis",
        "Enzyme kinetics & allosteric regulation",
        "Meiosis",
        "Membrane transport",
    ],
    "Embryology": [
        "Fertilization",
        "Gastrulation",
    ],
    "Immunology": [
        "Humoral immune response",
        "T cell activation",
    ],
    "Molecular Biology & Genetics": [
        "DNA replication",
        "Transcription",
        "Translation",
    ],
    "Physiology": [
        "Action potential",
        "Blood clotting (hemostasis)",
        "Blood glucose homeostasis",
        "Cardiac conduction system",
        "Electron transport chain & ATP synthase",
        "Gas exchange (alveoli)",
        "Muscle contraction",
        "Synaptic transmission",
    ],
}

with st.sidebar:
    st.header("Choose a mechanism")
    category = st.selectbox("Category", sorted(CATEGORIES.keys()))
    topic = st.radio("Mechanism", sorted(CATEGORIES[category]))
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
