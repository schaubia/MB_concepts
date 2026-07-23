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
<h2 class="sr-only">Interactive diagram of meiosis showing homolog pairing, crossing over, two rounds of division, an explicit telophase I two-cell stage, and four visibly distinct haploid daughter cells.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #pair1, #pair2 { transition: transform 1s ease, opacity .6s ease; }
  .anaphase1 #pair1, .telophase1 #pair1 { transform: translateX(-60px); }
  .anaphase1 #pair2, .telophase1 #pair2 { transform: translateX(60px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 380" role="img">
<title>Meiosis, general view</title>
<desc>A diploid cell with paired homologous chromosomes undergoes crossing over, aligns as tetrads, separates homologs in meiosis I to form two haploid cells with duplicated chromosomes, then separates sister chromatids in meiosis II, producing four genetically distinct haploid cells.</desc>

<ellipse id="parentCell" cx="340" cy="170" rx="220" ry="130" fill="none" stroke="var(--t)" stroke-width="1.5"/>
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

<g id="twoCells" class="stg">
<ellipse cx="220" cy="170" rx="80" ry="60" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<ellipse cx="460" cy="170" rx="80" ry="60" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<path d="M205 155 L225 175 M225 155 L205 175" stroke="#378ADD" stroke-width="4" stroke-linecap="round"/>
<path d="M445 155 L465 175 M465 155 L445 175" stroke="#D85A30" stroke-width="4" stroke-linecap="round"/>
<text class="ts" x="220" y="245" text-anchor="middle">Haploid, chromosomes still duplicated</text>
<text class="ts" x="460" y="245" text-anchor="middle">Haploid, chromosomes still duplicated</text>
</g>

<g id="fourCells" class="stg">
<ellipse cx="130" cy="300" rx="55" ry="42" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<ellipse cx="270" cy="300" rx="55" ry="42" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<ellipse cx="410" cy="300" rx="55" ry="42" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<ellipse cx="550" cy="300" rx="55" ry="42" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="4 3"/>
<line x1="120" y1="300" x2="140" y2="300" stroke="#378ADD" stroke-width="4" stroke-linecap="round"/>
<line x1="260" y1="300" x2="280" y2="300" stroke="#85B7EB" stroke-width="4" stroke-linecap="round"/>
<line x1="400" y1="300" x2="420" y2="300" stroke="#D85A30" stroke-width="4" stroke-linecap="round"/>
<line x1="540" y1="300" x2="560" y2="300" stroke="#F0997B" stroke-width="4" stroke-linecap="round"/>
<text class="th" x="340" y="355" text-anchor="middle">Four haploid cells — each with a different chromosome combination</text>
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
  "Diploid cell, homologs unpaired",
  "Prophase I — homologs pair (synapsis) and cross over",
  "Metaphase I — homolog pairs (tetrads) align at the equator",
  "Anaphase I — homologs separate to opposite poles (chromatids stay joined)",
  "Telophase I — two haploid cells form, each chromosome still has two joined sister chromatids",
  "Meiosis II — sister chromatids finally separate within each cell, like mitosis",
  "Result — four haploid cells, each with a different mix of chromosomes from crossing over"
];
function render() {
  document.getElementById('stageLabel').textContent = labels[step];
  document.getElementById('stepLabel').textContent = 'Step ' + step + ' of 6';
  document.getElementById('homolog1b').setAttribute('opacity', step >= 1 ? '1' : '0');
  document.getElementById('homolog2b').setAttribute('opacity', step >= 1 ? '1' : '0');
  document.getElementById('chiasma').classList.toggle('on', step === 1);
  document.getElementById('spindle').classList.toggle('on', step >= 2 && step <= 3);
  const svg = document.querySelector('svg');
  svg.classList.toggle('anaphase1', step === 3);
  svg.classList.toggle('telophase1', step === 4);
  document.getElementById('pair1').style.opacity = step >= 4 ? '0' : '1';
  document.getElementById('pair2').style.opacity = step >= 4 ? '0' : '1';
  document.getElementById('parentCell').style.opacity = step >= 4 ? '0' : '1';
  document.getElementById('twoCells').classList.toggle('on', step === 4);
  document.getElementById('fourCells').classList.toggle('on', step >= 5);
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
  @keyframes drift { 0%{transform:translateY(0)} 100%{transform:translateY(-40px)} }
  #cellBody { transition: d 0.8s ease, opacity .6s ease; }
  #bodies { transition: transform 1s ease, opacity .8s ease; }
  .engulfed #bodies { transform: translateX(120px) scale(0.3); opacity: 0; }
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
<text class="ts" x="200" y="270" text-anchor="middle">Nucleus intact</text>

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
<circle cx="130" cy="100" r="8" class="c-amber pulse"/>
<text class="ts" x="130" y="120" text-anchor="middle">BH3-only proteins tip Bcl-2 balance</text>
</g>

<ellipse id="mitoOutline" cx="130" cy="150" rx="45" ry="30" fill="none" stroke="var(--t)" stroke-width="1.5" class="stg"/>
<text class="ts" x="130" y="112" text-anchor="middle" id="mitoLabel" class="stg"></text>

<g id="baxbak" class="stg">
<circle cx="115" cy="150" r="5" fill="#E24B4A"/>
<circle cx="130" cy="160" r="5" fill="#E24B4A"/>
<text class="ts" x="130" y="192" text-anchor="middle">Bax/Bak — MOMP</text>
</g>

<g id="cytc" class="stg">
<circle class="drift" cx="130" cy="150" r="4" fill="#EF9F27"/>
<circle class="drift" cx="140" cy="160" r="4" fill="#EF9F27" style="animation-delay:.3s"/>
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
<text class="ts" x="290" y="140" text-anchor="middle" id="executionerLabel">Executioner</text>
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

  document.getElementById('damage').classList.toggle('on', step >= dmgThreshold);
  document.getElementById('cellBody').style.opacity = step >= dmgThreshold ? '0.15' : '1';
  document.getElementById('bodies').classList.toggle('on', step >= bodiesThreshold && step < engulfThreshold);
  document.getElementById('phagocyte').classList.toggle('on', step >= phagoThreshold);
  svg.classList.toggle('approaching', step === phagoThreshold);
  svg.classList.toggle('engulfed', step >= engulfThreshold);
  document.getElementById('phagocyteLabel').textContent = step >= engulfThreshold ? 'Phagocyte (fed)' : 'Phagocyte';
  document.getElementById('engulfNote').classList.toggle('on', step >= engulfThreshold);
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
<h2 class="sr-only">Interactive diagram of enzyme regulation modes: normal catalysis, competitive inhibition at the active site, allosteric inhibition at a distinct site, and allosteric activation.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.3s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #substrateGroup { transition: transform 1s ease, opacity .5s ease; }
  .bound #substrateGroup { transform: translate(15px, 5px); }
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
<rect x="270" y="140" width="24" height="18" rx="4" fill="#B91C1C"/>
<text class="ts" x="282" y="122" text-anchor="middle">Lookalike inhibitor</text>
<text class="ts" x="330" y="260" text-anchor="middle">Blocks the same site — beaten by more substrate</text>
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

  document.getElementById('competitiveInhibitor').classList.toggle('on', mode === 'competitive' && step >= 1);
  document.getElementById('allostericSite').classList.toggle('on', (mode === 'alloInhibit' || mode === 'alloActivate') && step >= 0);
  document.getElementById('inhibitor').classList.toggle('on', mode === 'alloInhibit' && step >= 1);
  document.getElementById('activator').classList.toggle('on', mode === 'alloActivate' && step >= 1);

  if (mode === 'normal') {
    svg.classList.toggle('bound', step >= 1 && step < 3);
    document.getElementById('substrateLabel').textContent = step >= 1 ? 'Bound substrate' : 'Substrate';
    document.getElementById('substrateGroup').style.opacity = step >= 3 ? '0' : '1';
    document.getElementById('activeSite').setAttribute('stroke', '#EF9F27');
    document.getElementById('activeSite').setAttribute('r', '16');
    document.getElementById('product').classList.toggle('on', step >= 2);
  } else if (mode === 'competitive') {
    document.getElementById('substrateGroup').style.opacity = step >= 1 ? '0.15' : '1';
    document.getElementById('activeSite').setAttribute('stroke', '#EF9F27');
    document.getElementById('activeSite').setAttribute('r', '16');
    document.getElementById('product').classList.toggle('on', false);
  } else if (mode === 'alloInhibit') {
    document.getElementById('substrateGroup').style.opacity = step >= 1 ? '0.15' : '1';
    document.getElementById('activeSite').setAttribute('stroke', step >= 1 ? '#E24B4A' : '#EF9F27');
    document.getElementById('activeSite').setAttribute('r', step >= 1 ? '10' : '16');
    document.getElementById('product').classList.toggle('on', false);
  } else if (mode === 'alloActivate') {
    document.getElementById('substrateGroup').style.opacity = '1';
    document.getElementById('activeSite').setAttribute('stroke', step >= 1 ? '#1D9E75' : '#EF9F27');
    document.getElementById('activeSite').setAttribute('r', step >= 1 ? '22' : '16');
    document.getElementById('product').classList.toggle('on', false);
  }
}
function stepFwd() { if (step < maxStep()) step++; render(); }
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
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #molecule { transition: transform 1s ease, opacity .4s ease; }
  #ligandGroup { transition: transform .8s ease, opacity .4s ease; }
  .docked #ligandGroup { transform: translateY(45px); }
  #gateTop, #gateBottom { transition: transform 0.8s ease; }
  .gateopen #gateTop { transform: translateY(-14px); }
  .gateopen #gateBottom { transform: translateY(14px); }
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
<text class="ts" x="340" y="30">Membrane</text>
<text class="ts" x="80" y="30" id="outsideLabel">Outside — high concentration</text>
<text class="ts" x="500" y="30" id="insideLabel">Inside — low concentration</text>

<g id="channelProt" class="stg">
<rect x="320" y="60" width="40" height="180" rx="16" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="340" y="255" text-anchor="middle">Channel protein (always open)</text>
</g>

<g id="pump" class="stg">
<rect x="310" y="60" width="60" height="180" rx="20" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="340" y="255" text-anchor="middle">Pump</text>
<circle id="atp" cx="420" cy="150" r="12" class="c-amber" opacity="0"/>
<text class="ts" x="420" y="150" text-anchor="middle" dominant-baseline="central" id="atpLabel" opacity="0">ATP</text>
</g>

<g id="ligandChannel" class="stg">
<rect x="320" y="60" width="40" height="180" rx="16" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<circle id="receptorSite" cx="340" cy="75" r="10" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="3 3"/>
<rect id="gateTop" x="330" y="120" width="20" height="20" fill="var(--t)" opacity="0.5"/>
<rect id="gateBottom" x="330" y="120" width="20" height="20" fill="var(--t)" opacity="0.5"/>
<text class="ts" x="340" y="255" text-anchor="middle">Ligand-gated channel</text>
<g id="ligandGroup">
<circle id="ligand" cx="340" cy="65" r="9" fill="#EF9F27"/>
<text id="ligandLabel" class="ts" x="340" y="45" text-anchor="middle">Ligand</text>
</g>
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
  document.getElementById('insideLabel').textContent = m === 'active' ? 'Inside — becomes higher concentration' : 'Inside — low concentration';
  render();
}
function render() {
  const cfg = configs[mode];
  document.getElementById('stepLabel').textContent = cfg.labels[step];
  const svg = document.querySelector('svg');
  let x = 120;
  if (mode === 'active') {
    x = step === 0 ? 120 : step === 1 ? 320 : step === 2 ? 340 : step === 3 ? 340 : 560;
    document.getElementById('atp').setAttribute('opacity', step === 1 ? '1' : '0');
    document.getElementById('atpLabel').setAttribute('opacity', step === 1 ? '1' : '0');
  } else if (mode === 'ligand') {
    svg.classList.toggle('docked', step >= 1);
    svg.classList.toggle('gateopen', step >= 2 && step < 4);
    document.getElementById('receptorSite').setAttribute('stroke', step >= 1 ? '#EF9F27' : 'var(--border-strong)');
    document.getElementById('receptorSite').setAttribute('stroke-width', step >= 1 ? '2.5' : '1');
    document.getElementById('ligandGroup').style.opacity = step >= 4 ? '0' : '1';
    document.getElementById('ligandLabel').textContent = step >= 1 && step < 4 ? 'Ligand (bound)' : 'Ligand';
    x = step === 3 ? 340 : step >= 4 ? 560 : 120;
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
<h2 class="sr-only">Interactive diagram comparing three types of action potential: the fast neuronal spike, the cardiac ventricular action potential with its plateau phase, and the spontaneously drifting pacemaker potential of the SA node.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #traceLine { transition: d 0.8s ease; }
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

<line x1="30" y1="140" x2="650" y2="140" stroke="var(--t)" stroke-width="2" stroke-linecap="round"/>
<text class="ts" x="60" y="125" id="cellLabel">Neuron axon membrane</text>

<path id="traceLine" d="M30 200 L650 200" stroke="#378ADD" stroke-width="2.5" fill="none"/>
<text class="ts" x="60" y="245" id="voltageLabel">Resting potential: −70 mV</text>

<g id="channelNote" class="stg">
<text class="ts" x="340" y="280" text-anchor="middle" id="channelLabel"></text>
</g>

<g id="specialNote" class="stg">
<text class="th" x="340" y="300" text-anchor="middle" id="specialLabel"></text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
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
  channel: "Voltage-gated Na+ then K+ channels",
  special: ""
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
  channel: "Fast Na+ (upstroke) then L-type Ca2+ (plateau) then K+",
  special: "This plateau is why heart muscle can't be tetanized like skeletal muscle"
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
    "M30 170 L650 170",
    "M30 170 Q250 170 450 150 Q550 140 600 135 L650 135",
    "M30 170 Q250 170 450 150 Q550 140 600 135 L615 105 L640 170 L650 170",
    "M30 170 Q250 170 450 150 Q550 140 600 135 L615 105 L640 170 L650 170"
  ],
  voltage: ["~ −60 mV, drifting", "Slow spontaneous depolarization", "Ca2+-driven upstroke", "Repolarized — cycle repeats"],
  channel: "Funny current (If) then T/L-type Ca2+ then K+ — NO fast Na+ channels",
  special: "This spontaneous, self-repeating cycle is the origin of your heartbeat's rhythm"
};

function getCfg() { return mode === 'neuronal' ? neuronal : mode === 'cardiac' ? cardiac : pacemaker; }

function setMode(m) {
  mode = m; step = 0;
  document.getElementById('btnNeuronal').classList.toggle('active', m === 'neuronal');
  document.getElementById('btnCardiac').classList.toggle('active', m === 'cardiac');
  document.getElementById('btnPacemaker').classList.toggle('active', m === 'pacemaker');
  document.getElementById('cellLabel').textContent = getCfg().cellLabel;
  document.getElementById('channelLabel').textContent = getCfg().channel;
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
}
function stepFwd() { if (step < getCfg().maxStep) step++; render(); }
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

<g id="atpRelease" class="stg">
<circle cx="340" cy="90" r="9" class="c-amber pulse"/>
<text class="ts" x="340" y="90" text-anchor="middle" dominant-baseline="central" font-size="8">ATP</text>
<text class="ts" x="340" y="75" text-anchor="middle">ATP binds — cross-bridge releases</text>
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
# NEPHRON_FILTRATION_GENERAL  (source: nephron.html)
# ---------------------------------------------------------------------------
NEPHRON_FILTRATION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of nephron function: blood is filtered at the glomerulus, useful solutes are reabsorbed along the tubule, waste is secreted, and the remainder becomes urine.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
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

<circle cx="120" cy="150" r="45" fill="none" stroke="#B91C1C" stroke-width="2"/>
<text class="ts" x="120" y="115" text-anchor="middle">Glomerulus</text>
<circle cx="120" cy="150" r="60" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="3 3"/>
<text class="ts" x="120" y="222" text-anchor="middle">Bowman's capsule</text>

<path d="M180 150 Q300 100 400 150 Q500 200 600 150" stroke="var(--t)" stroke-width="3" fill="none"/>
<text class="ts" x="400" y="235" text-anchor="middle">Tubule</text>

<g id="filtrate" class="stg">
<circle class="drift" cx="185" cy="150" r="5" fill="#378ADD"/>
<circle class="drift" cx="185" cy="145" r="5" fill="#EF9F27" style="animation-delay:.3s"/>
<text class="ts" x="180" y="185" text-anchor="middle">Filtrate — water, ions, glucose</text>
</g>

<g id="reabsorption" class="stg">
<line x1="300" y1="100" x2="300" y2="60" stroke="#639922" stroke-width="1.5" marker-end="url(#arrow)"/>
<text class="ts" x="300" y="50" text-anchor="middle">Glucose, water, ions reabsorbed → blood</text>
</g>

<g id="secretion" class="stg">
<line x1="480" y1="220" x2="480" y2="255" stroke="#B91C1C" stroke-width="1.5" marker-end="url(#arrow)"/>
<text class="ts" x="480" y="275" text-anchor="middle">Waste, H+, K+ secreted → filtrate</text>
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
# REFLEX_ARC_GENERAL  (source: reflex_arc.html)
# ---------------------------------------------------------------------------
REFLEX_ARC_GENERAL = '''
<h2 class="sr-only">Interactive diagram of the patellar reflex arc: a tap stretches the muscle spindle, a sensory neuron carries the signal to the spinal cord, it synapses directly onto a motor neuron, and the quadriceps contracts while the hamstring relaxes.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
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
<text class="ts" x="600" y="130" text-anchor="middle">Monosynaptic — no brain involved</text>
</g>

<g id="motorPath" class="stg">
<path d="M520 190 Q300 260 100 200" stroke="#D85A30" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="300" y="280" text-anchor="middle">Motor (efferent) neuron</text>
</g>

<g id="contraction" class="stg">
<text class="th" x="65" y="245" text-anchor="middle">Contracts</text>
</g>

<rect id="hamstring" x="150" y="230" width="70" height="50" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1" class="stg"/>
<text class="ts" x="185" y="222" text-anchor="middle" class="stg" id="hamLabel1">Hamstring</text>
<g id="inhibition" class="stg">
<text class="ts" x="185" y="295" text-anchor="middle">Inhibitory interneuron relaxes it (reciprocal inhibition)</text>
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
<text class="ts" x="440" y="185" text-anchor="middle" id="outputLabel">Parasympathetic ↑, sympathetic ↓</text>
</g>

<g id="signal2" class="stg">
<path d="M400 170 Q280 220 170 200" stroke="#D85A30" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="280" y="240" text-anchor="middle">Efferent signal to heart & vessels</text>
</g>

<ellipse cx="120" cy="220" rx="45" ry="30" class="c-coral stg" id="heart"/>
<text class="ts" x="120" y="220" text-anchor="middle" dominant-baseline="central" class="stg" id="heartLabel">Heart rate ↓</text>
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
# CARDIAC_MUSCLE_CONTRACTION_GENERAL  (source: cardiac_muscle.html)
# ---------------------------------------------------------------------------
CARDIAC_MUSCLE_CONTRACTION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of cardiac muscle excitation-contraction coupling: a small calcium trigger influx opens ryanodine receptors for calcium-induced calcium release, and the signal spreads to neighboring cells through gap junctions at intercalated discs.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
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
<text class="ts" x="430" y="50" text-anchor="middle" class="stg" id="cell2Label">Cardiomyocyte 2</text>

<rect x="280" y="60" width="40" height="180" fill="#7F77DD" opacity="0.3"/>
<text class="ts" x="300" y="255" text-anchor="middle" id="idLabel">Intercalated disc</text>

<g id="lTypeChannel" class="stg">
<rect x="90" y="180" width="14" height="24" fill="#EF9F27"/>
<text class="ts" x="97" y="220" text-anchor="middle">L-type Ca2+ channel (trigger)</text>
</g>

<ellipse cx="170" cy="140" rx="60" ry="35" fill="none" stroke="#B91C1C" stroke-width="1.5" stroke-dasharray="3 3"/>
<text class="ts" x="170" y="105" text-anchor="middle">Sarcoplasmic reticulum</text>

<g id="ryr" class="stg">
<circle cx="140" cy="150" r="6" class="c-red"/>
<text class="ts" x="140" y="170" text-anchor="middle">Ryanodine receptor</text>
</g>

<g id="cicr" class="stg">
<circle class="drift-up" cx="150" cy="150" r="4" fill="#B91C1C"/>
<circle class="drift-up" cx="165" cy="145" r="4" fill="#B91C1C" style="animation-delay:.2s"/>
<circle class="drift-up" cx="180" cy="150" r="4" fill="#B91C1C" style="animation-delay:.4s"/>
<circle class="drift-up" cx="160" cy="160" r="4" fill="#B91C1C" style="animation-delay:.6s"/>
<text class="ts" x="170" y="200" text-anchor="middle">Calcium-induced calcium release</text>
</g>

<g id="gapJunction" class="stg">
<circle cx="300" cy="120" r="5" fill="#1D9E75"/>
<circle cx="300" cy="150" r="5" fill="#1D9E75"/>
<circle cx="300" cy="180" r="5" fill="#1D9E75"/>
<text class="ts" x="300" y="105" text-anchor="middle" id="gjLabel">Gap junctions</text>
</g>

<g id="cell2Activity" class="stg">
<circle class="drift-up" cx="420" cy="150" r="4" fill="#B91C1C"/>
<circle class="drift-up" cx="435" cy="145" r="4" fill="#B91C1C" style="animation-delay:.2s"/>
<text class="ts" x="430" y="200" text-anchor="middle">Same coupling repeats — syncytial contraction</text>
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
# MUSCLE_CONTRACTION_TECHNICAL  (source: muscle_technical.html)
# ---------------------------------------------------------------------------
MUSCLE_CONTRACTION_TECHNICAL = '''
<h2 class="sr-only">Technical diagram of skeletal muscle excitation-contraction coupling and the full cross-bridge cycle: DHPR directly opens RyR, and myosin cycles through weak binding, power stroke, rigor, and ATP-driven detachment.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #myosinHead { transition: transform 1s ease; }
  .stroke #myosinHead { transform: rotate(-25deg); transform-origin: 340px 160px; }
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
<circle cx="170" cy="130" r="4" fill="#B91C1C"/>
<circle cx="185" cy="145" r="4" fill="#B91C1C"/>
<circle cx="175" cy="165" r="4" fill="#B91C1C"/>
<text class="ts" x="180" y="110" text-anchor="middle">Ca2+ floods out</text>
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
<text class="ts" x="470" y="200" text-anchor="middle">Signal to hypothalamus</text>
</g>

<ellipse cx="500" cy="120" rx="55" ry="35" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="500" y="120" text-anchor="middle" dominant-baseline="central">Hypothalamus / pituitary</text>

<g id="oxytocin" class="stg">
<circle id="oxyDot" cx="440" cy="90" r="7" class="c-purple pulse"/>
<text class="ts" x="440" y="70" text-anchor="middle">Oxytocin released</text>
</g>

<g id="loop2" class="stg">
<path d="M460 140 Q380 130 340 195" stroke="#7F77DD" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
</g>

<g id="uterus" class="stg">
<ellipse cx="340" cy="200" rx="70" ry="55" fill="none" stroke="#D85A30" stroke-width="2" id="uterusOutline"/>
<text class="ts" x="340" y="200" text-anchor="middle" dominant-baseline="central" id="uterusLabel">Uterine contraction</text>
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
  .pulse { animation: pulse 1.1s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #progBar { transition: width 1s ease; }
  #receptorDots circle { transition: opacity 0.6s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Labor initiation and the primed Ferguson reflex, technical view</title>
<desc>Late in pregnancy progesterone maintains uterine quiescence. Progesterone withdrawal alongside rising placental CRH and cortisol shifts the balance toward contraction readiness. Prostaglandins ripen the cervix and upregulate oxytocin receptors on the myometrium, sensitizing the tissue. Only then does the Ferguson reflex positive feedback loop — cervical stretch triggering oxytocin, which causes contractions that increase stretch — drive labor to completion.</desc>

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
<circle cx="260" cy="150" r="5" fill="#B91C1C"/>
<circle cx="280" cy="170" r="5" fill="#B91C1C"/>
<text class="ts" x="270" y="130" text-anchor="middle">Prostaglandins ripen cervix</text>
</g>

<g id="receptorDots" class="stg">
<circle cx="300" cy="220" r="4" class="c-teal"/>
<circle cx="320" cy="230" r="4" class="c-teal"/>
<circle cx="340" cy="222" r="4" class="c-teal"/>
<circle cx="360" cy="230" r="4" class="c-teal"/>
<circle cx="380" cy="220" r="4" class="c-teal"/>
<text class="ts" x="340" y="250" text-anchor="middle">Oxytocin receptors upregulated</text>
</g>

<ellipse cx="340" cy="270" rx="40" ry="18" fill="none" stroke="#B91C1C" stroke-width="2"/>
<text class="ts" x="340" y="300" text-anchor="middle">Cervix</text>

<g id="loop" class="stg">
<path d="M370 260 Q450 200 400 130" stroke="#378ADD" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
<text class="th" x="440" y="180" text-anchor="middle">Ferguson reflex loop — now sensitized</text>
</g>

<g id="birth" class="stg">
<text class="th" x="340" y="30" text-anchor="middle">Labor completes — loop breaks at birth</text>
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
  "Step 0 of 4 — late pregnancy: high progesterone keeps the uterus quiescent",
  "Step 1 of 4 — progesterone withdrawal, rising CRH/cortisol/estrogen shift the balance toward contraction readiness",
  "Step 2 of 4 — prostaglandins ripen the cervix and upregulate oxytocin receptors on the myometrium",
  "Step 3 of 4 — the sensitized tissue now responds strongly — the Ferguson reflex positive feedback loop takes over",
  "Step 4 of 4 — contractions intensify, cervix fully dilates, labor completes and the loop breaks at birth"
];
function render() {
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
render();
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
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 320" role="img">
<title>Fertilization, technical view</title>
<desc>The egg is arrested at metaphase II of meiosis. Sperm-egg recognition and membrane fusion trigger a fast electrical block via membrane depolarization, then a calcium wave sweeps across the egg by calcium-induced calcium release, triggering the slow cortical granule block that hardens the zona pellucida. The same calcium wave activates the egg, allowing it to complete meiosis II and extrude a second polar body, after which the male and female pronuclei form and fuse into a diploid zygote.</desc>

<circle cx="380" cy="160" r="100" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<g id="meiosisArrest">
<path d="M370 130 L390 130 M380 120 L380 140" stroke="#7F77DD" stroke-width="2"/>
<text class="ts" x="380" y="105" text-anchor="middle" id="arrestLabel">Egg arrested at metaphase II</text>
</g>

<g id="spermGroup" class="stg">
<circle cx="180" cy="160" r="10" fill="#378ADD"/>
<text class="ts" x="180" y="140" text-anchor="middle">Sperm — ZP3 binding, acrosome reaction</text>
</g>

<g id="fastBlock" class="stg">
<circle cx="380" cy="160" r="105" fill="none" stroke="#EF9F27" stroke-width="3"/>
<text class="ts" x="380" y="280" text-anchor="middle">Fast block — membrane depolarizes (Na+ influx)</text>
</g>

<circle id="calciumWave" cx="280" cy="160" r="0" fill="none" stroke="#B91C1C" stroke-width="2" class="stg"/>
<g id="calciumLabel" class="stg">
<text class="ts" x="380" y="240" text-anchor="middle">Ca2+ wave — calcium-induced calcium release</text>
</g>

<g id="cortical" class="stg">
<circle cx="380" cy="160" r="100" fill="none" stroke="#B91C1C" stroke-width="4"/>
<text class="ts" x="380" y="260" text-anchor="middle">Slow block — cortical granules harden the zona</text>
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
  document.getElementById('calciumWave').setAttribute('r', step === 2 ? '100' : '0');
  document.getElementById('calciumWave').setAttribute('opacity', step === 2 ? '1' : '0');
  document.getElementById('calciumLabel').classList.toggle('on', step >= 2 && step < 3);
  document.getElementById('cortical').classList.toggle('on', step >= 3);
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
<desc>The Spemann organizer at the dorsal blastopore lip secretes BMP antagonists, creating a gradient that patterns the dorsal-ventral axis of the ectoderm. Cells move by involution, rolling inward around the blastopore lip, and by convergent extension, intercalating to narrow and elongate the embryo. A separate Nodal signaling gradient specifies the three germ layers: high Nodal produces mesoderm, moderate Nodal produces endoderm, and the absence of Nodal leaves ectoderm.</desc>

<circle cx="340" cy="160" r="120" fill="none" stroke="var(--t)" stroke-width="1.5"/>

<g id="organizer">
<circle cx="340" cy="280" r="14" class="c-amber"/>
<text class="ts" x="340" y="305" text-anchor="middle">Spemann organizer</text>
</g>

<g id="bmpGradient" class="stg">
<path d="M260 250 Q340 230 420 250" stroke="#7F77DD" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
<path d="M260 250 Q340 270 420 250" stroke="#7F77DD" stroke-width="2" fill="none" marker-start="url(#arrow)"/>
<text class="ts" x="340" y="225" text-anchor="middle">BMP antagonist gradient (Noggin, Chordin)</text>
</g>

<g id="dvPattern" class="stg">
<text class="ts" x="220" y="100" text-anchor="middle">Low BMP → neural</text>
<text class="ts" x="460" y="100" text-anchor="middle">High BMP → epidermis</text>
</g>

<g id="involution" class="stg">
<path d="M300 265 Q320 230 300 200" stroke="#B91C1C" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
<text class="ts" x="260" y="220" text-anchor="middle">Involution</text>
</g>

<g id="convExt" class="stg">
<path d="M260 160 L420 160" stroke="#1D9E75" stroke-width="1.5" marker-end="url(#arrow)" marker-start="url(#arrow)"/>
<text class="ts" x="340" y="145" text-anchor="middle">Convergent extension</text>
</g>

<g id="nodalGradient" class="stg">
<circle cx="340" cy="180" r="30" fill="#E24B4A" opacity="0.5"/>
<circle cx="340" cy="180" r="55" fill="#E24B4A" opacity="0.25"/>
<text class="ts" x="340" y="185" text-anchor="middle">High Nodal — mesoderm</text>
<text class="ts" x="340" y="240" text-anchor="middle">Moderate Nodal — endoderm</text>
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
  "Step 4 of 4 — a separate Nodal gradient specifies the germ layers: high Nodal → mesoderm, moderate → endoderm, none → ectoderm"
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
<circle cx="130" cy="90" r="8" class="c-purple"/>
<text class="ts" x="130" y="72" text-anchor="middle">C1, C4, C2 activate</text>
</g>

<g id="opsonize" class="stg">
<circle cx="150" cy="200" r="7" class="c-amber"/>
<circle cx="250" cy="200" r="7" class="c-amber"/>
<text class="ts" x="200" y="225" text-anchor="middle">C3b opsonizes — tags for phagocytosis</text>
</g>

<g id="cascadeLate" class="stg">
<text class="ts" x="200" y="60" text-anchor="middle">C5-C9 assemble</text>
</g>

<g id="mac" class="stg">
<rect x="260" y="120" width="14" height="60" fill="#B91C1C"/>
<rect x="280" y="120" width="14" height="60" fill="#B91C1C"/>
<rect x="300" y="120" width="14" height="60" fill="#B91C1C"/>
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
# INNATE_IMMUNE_RECOGNITION_GENERAL  (source: innate_immunity.html)
# ---------------------------------------------------------------------------
INNATE_IMMUNE_RECOGNITION_GENERAL = '''
<h2 class="sr-only">Interactive diagram of innate immune pattern recognition: a Toll-like receptor on a macrophage detects a pathogen-associated molecular pattern, triggering NF-kB signaling and inflammatory cytokine release.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
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

<ellipse cx="200" cy="170" rx="130" ry="90" fill="none" stroke="var(--t)" stroke-width="1.5"/>
<text class="ts" x="200" y="70" text-anchor="middle">Macrophage</text>
<ellipse cx="200" cy="200" rx="35" ry="25" fill="none" stroke="var(--border-strong)" stroke-width="1" stroke-dasharray="3 3"/>
<text class="ts" x="200" y="235" text-anchor="middle">Nucleus</text>

<g id="pamp" class="stg">
<circle cx="70" cy="140" r="8" fill="#B91C1C"/>
<text class="ts" x="70" y="120" text-anchor="middle">PAMP (e.g. LPS)</text>
</g>

<circle id="tlr" cx="90" cy="150" r="10" class="c-amber"/>
<text class="ts" x="90" y="175" text-anchor="middle">TLR</text>

<g id="signaling" class="stg">
<line x1="100" y1="150" x2="180" y2="180" stroke="#7F77DD" stroke-width="1.5" marker-end="url(#arrow)"/>
<text class="ts" x="140" y="150" text-anchor="middle">Signaling cascade</text>
</g>

<g id="nfkb" class="stg">
<circle cx="200" cy="200" r="8" class="c-purple pulse"/>
</g>

<g id="cytokines" class="stg">
<circle class="drift" cx="340" cy="130" r="6" fill="#E24B4A"/>
<circle class="drift" cx="360" cy="150" r="6" fill="#E24B4A" style="animation-delay:.3s"/>
<circle class="drift" cx="330" cy="170" r="6" fill="#E24B4A" style="animation-delay:.6s"/>
<text class="ts" x="345" y="105" text-anchor="middle">Cytokines released (TNF-a, IL-1, IL-6)</text>
</g>

<g id="inflammation" class="stg">
<text class="th" x="500" y="150" text-anchor="middle">Recruits immune cells, triggers inflammation</text>
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
  document.getElementById('pamp').classList.toggle('on', step === 0);
  document.getElementById('tlr').classList.toggle('pulse', step === 1);
  document.getElementById('signaling').classList.toggle('on', step >= 1);
  document.getElementById('nfkb').classList.toggle('on', step >= 2);
  document.getElementById('cytokines').classList.toggle('on', step >= 3);
  document.getElementById('inflammation').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
function stepBack() { if (step > 0) step--; render(); }
function reset() { step = 0; render(); }
render();
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
<rect x="165" y="90" width="30" height="12" rx="3" fill="#EF9F27"/>
<text class="ts" x="180" y="75" text-anchor="middle" id="mhcLabel">MHC-I present</text>
</g>

<g id="inhibitorySignal" class="stg">
<line x1="250" y1="130" x2="425" y2="130" stroke="#639922" stroke-width="2" marker-end="url(#arrow)"/>
<text class="ts" x="340" y="115" text-anchor="middle">Inhibitory signal</text>
</g>

<g id="activatingSignal" class="stg">
<line x1="250" y1="150" x2="425" y2="150" stroke="#E24B4A" stroke-width="2" marker-end="url(#arrow)"/>
<text class="ts" x="340" y="170" text-anchor="middle">Activating signal (stress ligands)</text>
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
  render();
}
function render() {
  const cfg = mode === 'healthy' ? configHealthy : configInfected;
  document.getElementById('stepLabel').textContent = cfg.labels[step];
  document.getElementById('mhcMarker').classList.toggle('on', step >= 1);
  document.getElementById('inhibitorySignal').classList.toggle('on', mode === 'healthy' && step >= 1);
  document.getElementById('activatingSignal').classList.toggle('on', step >= 1);
  document.getElementById('outcome').classList.toggle('on', step >= 2);
  document.getElementById('targetCell').style.opacity = (mode === 'infected' && step >= 2) ? '0.25' : '1';
}
function stepFwd() { if (step < 2) step++; render(); }
function reset() { step = 0; render(); }
setMode('healthy');
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
<path d="M270 120 L285 105 M285 120 L270 105" stroke="#7F77DD" stroke-width="2"/>
<path d="M410 120 L425 105 M425 120 L410 105" stroke="#7F77DD" stroke-width="2"/>
<text class="ts" x="340" y="90" text-anchor="middle">IgE bound to Fc receptors — sensitized</text>
</g>

<g id="allergen" class="stg">
<circle cx="277" cy="90" r="8" fill="#EF9F27"/>
<circle cx="417" cy="90" r="8" fill="#EF9F27"/>
<text class="ts" x="340" y="65" text-anchor="middle">Allergen cross-links IgE</text>
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
  document.getElementById('ligate').classList.toggle('on', step >= 4);
}
function stepFwd() { if (step < 4) step++; render(); }
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
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #cas9Group { transition: transform 1s ease; }
  .docked #cas9Group { transform: translateY(20px); }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 300" role="img">
<title>CRISPR-Cas9 gene editing, general view</title>
<desc>A guide RNA loaded into Cas9 protein scans DNA for a matching sequence next to a PAM site, base-pairs with the target strand to confirm the match, and Cas9 cuts both DNA strands. The cell then repairs the break either through error-prone non-homologous end joining, which disrupts the gene, or through homology-directed repair using a donor template, which precisely edits the sequence.</desc>

<line x1="30" y1="150" x2="650" y2="150" stroke="#378ADD" stroke-width="3" stroke-linecap="round"/>
<line x1="30" y1="170" x2="650" y2="170" stroke="#D85A30" stroke-width="3" stroke-linecap="round"/>
<rect x="320" y="145" width="30" height="10" fill="#EF9F27"/>
<text class="ts" x="335" y="135" text-anchor="middle">PAM</text>

<g id="cas9Group">
<circle cx="300" cy="110" r="30" class="c-purple"/>
<text class="th" x="300" y="110" text-anchor="middle" dominant-baseline="central">Cas9</text>
<path d="M300 140 L300 150" stroke="#7F77DD" stroke-width="3"/>
</g>

<g id="grna" class="stg">
<text class="ts" x="300" y="70" text-anchor="middle">Guide RNA finds matching sequence</text>
</g>

<g id="basePairing" class="stg">
<path d="M260 150 Q280 130 300 150" stroke="#639922" stroke-width="2" fill="none"/>
<text class="ts" x="260" y="200" text-anchor="middle">gRNA base-pairs — match confirmed</text>
</g>

<g id="cut" class="stg">
<line x1="290" y1="145" x2="290" y2="175" stroke="#E24B4A" stroke-width="3"/>
<text class="ts" x="290" y="195" text-anchor="middle">Double-strand break</text>
</g>

<g id="nhej" class="stg">
<text class="ts" x="180" y="240" text-anchor="middle">NHEJ — error-prone, disrupts gene</text>
</g>

<g id="hdr" class="stg">
<rect x="380" y="140" width="60" height="20" rx="4" fill="#1D9E75" opacity="0.5"/>
<text class="ts" x="410" y="240" text-anchor="middle">HDR — donor template, precise edit</text>
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
  document.getElementById('grna').classList.toggle('on', step === 0);
  document.querySelector('svg').classList.toggle('docked', step >= 1);
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
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #repressor { transition: transform 0.8s ease, opacity 0.5s ease; }
  .removed #repressor { transform: translateY(-40px); opacity: 0; }
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
<text class="ts" x="235" y="75" text-anchor="middle">Lactose binds repressor</text>
</g>

<circle id="rnaPol" cx="175" cy="150" r="12" class="c-teal"/>

<g id="mrnaOut" class="stg">
<text class="th" x="420" y="220" text-anchor="middle">Genes transcribed — enzymes made</text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
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
    'Step 1 of 2 — lactose binds the repressor, changing its shape so it releases the operator',
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
  const svg = document.querySelector('svg');
  svg.classList.toggle('removed', mode === 'present' && step >= 2);
  svg.classList.toggle('transcribing', mode === 'present' && step >= 2);
  document.getElementById('mrnaOut').classList.toggle('on', mode === 'present' && step >= 2);
}
function stepFwd() { if (step < maxStep()) step++; render(); }
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
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  #riscGroup { transition: transform 1s ease; }
  .docked #riscGroup { transform: translateX(120px); }
  #targetMrna { transition: opacity 0.6s ease; }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 280" role="img">
<title>RNA interference, general view</title>
<desc>Double-stranded RNA is cleaved by the enzyme Dicer into short interfering RNA fragments. One strand is loaded into the RNA-induced silencing complex, RISC, as a guide. The RISC-siRNA complex scans mRNA molecules in the cell, and when the guide strand base-pairs with a complementary target mRNA, RISC cleaves it, degrading the message and silencing that gene.</desc>

<path d="M100 100 L180 100" stroke="#378ADD" stroke-width="4" stroke-linecap="round"/>
<path d="M100 115 L180 115" stroke="#D85A30" stroke-width="4" stroke-linecap="round"/>
<text class="ts" x="140" y="85" text-anchor="middle">Double-stranded RNA</text>

<g id="dicer" class="stg">
<circle cx="140" cy="107" r="16" class="c-amber pulse"/>
<text class="ts" x="140" y="140" text-anchor="middle">Dicer cleaves into siRNA</text>
</g>

<g id="riscGroup">
<ellipse cx="140" cy="180" rx="30" ry="22" class="c-purple stg" id="risc"/>
<text class="ts" x="140" y="180" text-anchor="middle" dominant-baseline="central" id="riscLabel"></text>
<path id="guideStrand" d="M120 175 L160 175" stroke="#D85A30" stroke-width="3" stroke-linecap="round" opacity="0"/>
</g>

<line x1="300" y1="180" x2="600" y2="180" id="targetMrna" stroke="#1D9E75" stroke-width="3" stroke-linecap="round"/>
<text class="ts" x="450" y="200" text-anchor="middle">Target mRNA</text>

<g id="basePairing" class="stg">
<text class="ts" x="380" y="160" text-anchor="middle">Guide strand base-pairs with target</text>
</g>

<g id="cleavage" class="stg">
<path d="M400 172 L400 188 M420 172 L420 188" stroke="#E24B4A" stroke-width="2" stroke-linecap="round"/>
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
  document.getElementById('targetMrna').style.opacity = step >= 4 ? '0.2' : '1';
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
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .drift { animation: drift 1.6s ease-in-out infinite; }
  @keyframes drift { 0%{transform:translateX(0)} 100%{transform:translateX(80px)} }
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

<rect x="60" y="80" width="120" height="120" rx="12" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="120" y="70" text-anchor="middle">Presynaptic cell</text>
<rect x="500" y="80" width="120" height="120" rx="12" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="560" y="70" text-anchor="middle">Postsynaptic cell</text>

<g id="chemGap" class="stg">
<rect x="180" y="80" width="60" height="120" fill="var(--surface-1)"/>
<text class="ts" x="210" y="230" text-anchor="middle">Synaptic cleft (20 nm)</text>
<circle class="drift" cx="195" cy="140" r="5" fill="#7F77DD"/>
<circle class="drift" cx="195" cy="120" r="5" fill="#7F77DD" style="animation-delay:.3s"/>
<circle cx="440" cy="130" r="10" fill="none" stroke="#EF9F27" stroke-width="2"/>
<text class="ts" x="440" y="110" text-anchor="middle">Receptor</text>
<text class="ts" x="440" y="230" text-anchor="middle">Cleared by reuptake / degradation</text>
</g>

<g id="elecGap" class="stg">
<rect x="180" y="80" width="60" height="120" fill="var(--surface-1)"/>
<text class="ts" x="210" y="230" text-anchor="middle">Gap junction (3.5 nm)</text>
<rect x="195" y="120" width="10" height="40" fill="#1D9E75"/>
<rect x="215" y="120" width="10" height="40" fill="#1D9E75"/>
<text class="ts" x="210" y="105" text-anchor="middle">Connexons</text>
<circle class="drift" cx="200" cy="140" r="4" fill="#1D9E75"/>
</g>

<g id="delayNote" class="stg">
<text class="th" x="340" y="250" text-anchor="middle" id="delayLabel"></text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
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
  document.getElementById('chemGap').classList.toggle('on', m === 'chemical');
  document.getElementById('elecGap').classList.toggle('on', m === 'electrical');
  render();
}
function render() {
  const cfg = mode === 'chemical' ? chemical : electrical;
  document.getElementById('stepLabel').textContent = cfg.labels[step];
  document.getElementById('delayNote').classList.toggle('on', step === 3);
  document.getElementById('delayLabel').textContent = step === 3 ? cfg.labels[3].split('— ')[1] : '';
}
function stepFwd() { if (step < 3) step++; render(); }
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

<circle class="stg" id="glutamate1" cx="200" cy="70" r="6" fill="#7F77DD"/>
<circle class="stg" id="glutamate2" cx="220" cy="70" r="6" fill="#7F77DD"/>
<text class="ts" x="210" y="95" text-anchor="middle" id="glutamateLabel">Glutamate released</text>

<rect x="80" y="140" width="600" height="120" rx="8" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="110" y="130">Postsynaptic membrane</text>

<circle cx="220" cy="160" r="14" class="c-purple"/>
<text class="ts" x="220" y="185" text-anchor="middle">NMDA receptor</text>
<circle id="mgBlock" cx="220" cy="150" r="5" fill="#EF9F27"/>
<text class="ts" x="220" y="135" text-anchor="middle" id="mgLabel">Mg2+ block</text>

<g id="calcium" class="stg">
<circle cx="220" cy="180" r="4" fill="#B91C1C"/>
<circle cx="230" cy="190" r="4" fill="#B91C1C"/>
<text class="ts" x="220" y="215" text-anchor="middle">Ca2+ influx</text>
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
<text class="th" x="520" y="145" text-anchor="middle">New AMPA receptors inserted</text>
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
  document.querySelector('svg').classList.toggle('expelled', step >= 2);
  document.getElementById('mgLabel').style.opacity = step >= 2 ? '0' : '1';
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
# DOPAMINE_REWARD_PATHWAY_GENERAL  (source: dopamine_reward.html)
# ---------------------------------------------------------------------------
DOPAMINE_REWARD_PATHWAY_GENERAL = '''
<h2 class="sr-only">Interactive diagram of the dopamine reward pathway: a rewarding stimulus activates VTA dopamine neurons, which release dopamine into the nucleus accumbens, reinforcing the behavior, before reuptake ends the signal.</h2>
<style>
  .stg { opacity: 0.12; transition: opacity .5s ease; }
  .stg.on { opacity: 1; }
  .pulse { animation: pulse 1.2s ease-in-out infinite; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
  .drift { animation: drift 1.6s ease-in-out infinite; }
  @keyframes drift { 0%{transform:translateX(0)} 100%{transform:translateX(70px)} }
  .btnrow { display:flex; gap:10px; align-items:center; margin-top:12px; flex-wrap:wrap; }
  #stepLabel { font-size:13px; color:var(--text-secondary); }
</style>
<svg width="100%" viewBox="0 0 680 280" role="img">
<title>Dopamine reward pathway, general view</title>
<desc>A rewarding stimulus activates dopamine neurons in the ventral tegmental area, which project to and release dopamine in the nucleus accumbens, producing reinforcement that strengthens the behavior that led to the reward. Dopamine transporters then clear the dopamine from the synapse, ending the signal. Certain drugs of abuse hijack this pathway by blocking those transporters or triggering extra release, producing a much larger and more sustained surge than natural rewards.</desc>

<circle cx="130" cy="150" r="16" fill="#EF9F27" id="stimulus"/>
<text class="ts" x="130" y="120" text-anchor="middle">Rewarding stimulus</text>

<ellipse cx="250" cy="150" rx="45" ry="35" class="c-purple"/>
<text class="ts" x="250" y="150" text-anchor="middle" dominant-baseline="central">VTA</text>

<g id="dopamineRelease" class="stg">
<circle class="drift" cx="320" cy="140" r="5" fill="#7F77DD"/>
<circle class="drift" cx="320" cy="160" r="5" fill="#7F77DD" style="animation-delay:.3s"/>
<circle class="drift" cx="320" cy="150" r="5" fill="#7F77DD" style="animation-delay:.6s"/>
</g>

<ellipse cx="480" cy="150" rx="50" ry="38" class="c-teal"/>
<text class="ts" x="480" y="150" text-anchor="middle" dominant-baseline="central">Nucleus accumbens</text>

<g id="reinforcement" class="stg">
<text class="th" x="480" y="215" text-anchor="middle">Reward signal — behavior reinforced</text>
</g>

<g id="reuptake" class="stg">
<circle cx="440" cy="120" r="6" fill="#B91C1C"/>
<text class="ts" x="440" y="100" text-anchor="middle">DAT clears dopamine — signal ends</text>
</g>

<g id="hijack" class="stg">
<text class="th" x="480" y="240" text-anchor="middle">Some drugs block DAT or trigger extra release — much larger, longer surge</text>
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
  document.getElementById('dopamineRelease').classList.toggle('on', step >= 1 && step < 4);
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
<text class="ts" x="130" y="70">Presynaptic terminal</text>
<rect x="480" y="80" width="140" height="120" rx="10" fill="var(--surface-2)" stroke="var(--t)" stroke-width="1"/>
<text class="ts" x="550" y="70">Postsynaptic membrane</text>

<circle id="transporter" cx="200" cy="150" r="10" class="c-teal"/>
<text class="ts" x="200" y="175" text-anchor="middle" id="transporterLabel">SERT transporter</text>

<g id="neurotransmitter" class="stg">
<circle class="drift" cx="300" cy="140" r="5" fill="#7F77DD"/>
<circle class="drift" cx="330" cy="150" r="5" fill="#7F77DD" style="animation-delay:.3s"/>
<circle class="drift" cx="360" cy="140" r="5" fill="#7F77DD" style="animation-delay:.6s"/>
</g>

<circle id="receptor" cx="480" cy="150" r="14" class="c-purple"/>
<text class="ts" x="480" y="180" text-anchor="middle" id="receptorLabel">Receptor</text>

<g id="drug" class="stg">
<rect x="185" y="130" width="30" height="14" rx="4" class="c-coral" id="drugShape"/>
<text class="ts" x="200" y="115" text-anchor="middle" id="drugLabel">SSRI blocks transporter</text>
</g>

<g id="effect" class="stg">
<text class="th" x="480" y="240" text-anchor="middle" id="effectLabel"></text>
</g>
</svg>

<div class="btnrow">
  <button onclick="stepFwd()">Next step ↗</button>
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
  labels: [
    'Step 0 of 3 — normally, GABA binds its receptor, opening a chloride channel — an inhibitory signal',
    'Step 1 of 3 — a benzodiazepine binds a DIFFERENT site on the same receptor, not where GABA binds',
    'Step 2 of 3 — this is positive allosteric modulation — it doesn\'t activate the receptor alone, but makes it respond more strongly to GABA',
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
  render();
}
function render() {
  const cfg = mode === 'ssri' ? ssri : benzo;
  document.getElementById('stepLabel').textContent = cfg.labels[step];
  document.getElementById('neurotransmitter').classList.toggle('on', step >= 0);
  document.getElementById('drug').classList.toggle('on', step >= 1);
  document.getElementById('receptor').setAttribute('r', (mode === 'benzo' && step >= 2) ? '18' : '14');
  document.getElementById('effect').classList.toggle('on', step >= 3);
  document.getElementById('effectLabel').textContent = step >= 3 ? cfg.labels[3].split('— ').slice(1).join('— ') : '';
}
function stepFwd() { if (step < 3) step++; render(); }
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
const waveTraces = [
  "M30 200 L60 195 L90 205 L120 195 L150 205 L180 200 L650 200",
  "M30 200 L60 195 L90 205 L120 195 L150 205 L180 200 L650 200",
  "M30 200 L60 197 L90 203 L120 198 L150 200 L650 200",
  "M30 200 Q70 160 110 200 Q150 240 190 200 Q230 160 270 200 L650 200",
  "M30 200 L60 190 L90 210 L120 195 L150 205 L180 190 L210 210 L650 200"
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
  document.getElementById('adenosineBar').setAttribute('width', 20 + step * 55);
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
            "height": 520,
            "blurb": (
                "Homologous chromosomes pair and cross over, then separate "
                "in meiosis I into two haploid cells (chromosomes still "
                "duplicated), and sister chromatids separate in meiosis "
                "II, producing four visibly distinct haploid cells."
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
    },
    "Labor (positive feedback)": {
        "General": {
            "fragment": LABOR_POSITIVE_FEEDBACK_GENERAL,
            "height": 460,
            "blurb": (
                "The Ferguson reflex: cervical stretch triggers oxytocin, "
                "which causes contractions that increase cervical "
                "stretch — positive feedback that escalates rather than "
                "corrects, unlike almost every other loop in this app."
            ),
        },
        "Technical": {
            "fragment": LABOR_TECHNICAL,
            "height": 460,
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
        "Complement system",
        "Cytotoxic T cell killing",
        "Humoral immune response",
        "Immune checkpoint (PD-1/PD-L1)",
        "Immunological memory",
        "Innate immune recognition",
        "NK cell missing-self recognition",
        "T cell activation",
        "Type I hypersensitivity",
    ],
    "Molecular Biology & Genetics": [
        "CRISPR-Cas9 gene editing",
        "DNA mismatch repair",
        "DNA replication",
        "Lac operon",
        "RNA interference",
        "Transcription",
        "Translation",
    ],
    "Physiology": [
        "Action potential",
        "Baroreceptor reflex",
        "Blood clotting (hemostasis)",
        "Blood glucose homeostasis",
        "Cardiac conduction system",
        "Dopamine reward pathway",
        "Electron transport chain & ATP synthase",
        "Gas exchange (alveoli)",
        "Labor (positive feedback)",
        "Medication mechanism of action",
        "Muscle contraction (cardiac)",
        "Muscle contraction (skeletal)",
        "Nephron filtration",
        "Reflex arc (patellar reflex)",
        "Sleep-wake regulation",
        "Synaptic plasticity (LTP)",
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
