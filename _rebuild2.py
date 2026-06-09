"""Rebuilds defense.html slides container with less-dense, picture-friendly slides."""
import re, pathlib

BASE = pathlib.Path(__file__).parent
SRC  = BASE / "defense.html"
content = SRC.read_text(encoding="utf-8")

NEW_SLIDES = r"""  <div id="slides-container">

    <!-- ═══ S1: TITLE ═══ -->
    <div class="slide active" id="slide-1">
      <div style="text-align:center; max-width:820px;">
        <div style="display:inline-block; background:rgba(255,215,0,0.1); border:1px solid rgba(255,215,0,0.25); border-radius:20px; padding:4px 14px; font-size:0.7rem; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:#ffd700; margin-bottom:20px;">PhD Defense · XXXVII Cycle</div>
        <h1 style="font-size:2.55rem; font-weight:900; line-height:1.15; margin-bottom:11px; background:linear-gradient(135deg,#fff 0%,#ffd700 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">Pattern-Driven Data Engineering</h1>
        <p style="font-size:0.9rem; color:rgba(255,255,255,0.42); margin-bottom:3px;">Formalizing Systematic Solutions for Cloud-based Data Lakehouses</p>
        <div style="width:50px; height:2px; background:#ffd700; margin:16px auto;"></div>
        <p style="font-size:0.88rem; color:rgba(255,255,255,0.55);">Chiara Rucco</p>
        <p style="font-size:0.74rem; color:rgba(255,255,255,0.28); margin-top:4px;">Supervisors: Prof.ssa Antonella Longo &nbsp;·&nbsp; Dr. Motaz Saad</p>
        <p style="font-size:0.72rem; color:rgba(255,255,255,0.2); margin-top:2px;">Engineering of Complex Systems · Dept. of Engineering for Innovation · University of Salento</p>
        <div style="display:flex; justify-content:center; gap:44px; margin-top:26px;">
          <div style="text-align:center;"><div style="font-size:1.9rem; font-weight:800; color:#ffd700;">3</div><div style="font-size:0.68rem; color:rgba(255,255,255,0.35); margin-top:2px;">Design Patterns</div></div>
          <div style="text-align:center;"><div style="font-size:1.9rem; font-weight:800; color:#ffd700;">7</div><div style="font-size:0.68rem; color:rgba(255,255,255,0.35); margin-top:2px;">LLMs Benchmarked</div></div>
          <div style="text-align:center;"><div style="font-size:1.9rem; font-weight:800; color:#ffd700;">21</div><div style="font-size:0.68rem; color:rgba(255,255,255,0.35); margin-top:2px;">Expert Practitioners</div></div>
          <div style="text-align:center;"><div style="font-size:1.9rem; font-weight:800; color:#ffd700;">165+</div><div style="font-size:0.68rem; color:rgba(255,255,255,0.35); margin-top:2px;">Papers Reviewed</div></div>
        </div>
      </div>
    </div>

    <!-- ═══ S2: FOUR CHALLENGES ═══ -->
    <div class="slide" id="slide-2">
      <div style="max-width:980px; width:100%;">
        <div class="slide-label" style="color:#ff6b6b;">01 — Motivation</div>
        <h2 class="slide-title" style="font-size:1.9rem; margin-bottom:18px;">Four Persistent Challenges</h2>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
          <div style="background:rgba(255,80,80,0.07); border:1px solid rgba(255,80,80,0.2); border-radius:10px; padding:20px 22px; border-left:3px solid rgba(255,100,100,0.55);">
            <div style="font-size:0.65rem; font-weight:700; color:rgba(255,140,140,0.85); text-transform:uppercase; letter-spacing:1.5px; margin-bottom:8px;">C1 — Source Heterogeneity</div>
            <div style="font-size:1.5rem; font-weight:800; color:white; margin-bottom:6px;">100+ sources</div>
            <div style="font-size:0.85rem; color:rgba(255,255,255,0.55);">REST APIs · RDBMS · Blobs · Streams · SOAP</div>
            <div style="margin-top:12px; font-size:0.88rem; font-weight:700; color:#ffd700;">10–40% dev time lost to config management</div>
          </div>
          <div style="background:rgba(255,80,80,0.07); border:1px solid rgba(255,80,80,0.2); border-radius:10px; padding:20px 22px; border-left:3px solid rgba(255,100,100,0.55);">
            <div style="font-size:0.65rem; font-weight:700; color:rgba(255,140,140,0.85); text-transform:uppercase; letter-spacing:1.5px; margin-bottom:8px;">C2 — Transformation Timing</div>
            <div style="font-size:1.5rem; font-weight:800; color:white; margin-bottom:6px;">78% use ad-hoc hybrid</div>
            <div style="font-size:0.85rem; color:rgba(255,255,255,0.55);">No formal ETL vs ELT decision framework exists</div>
            <div style="margin-top:12px; font-size:0.88rem; font-weight:700; color:#ffd700;">Clean early or transform late? No guidance.</div>
          </div>
          <div style="background:rgba(255,80,80,0.07); border:1px solid rgba(255,80,80,0.2); border-radius:10px; padding:20px 22px; border-left:3px solid rgba(255,100,100,0.55);">
            <div style="font-size:0.65rem; font-weight:700; color:rgba(255,140,140,0.85); text-transform:uppercase; letter-spacing:1.5px; margin-bottom:8px;">C3 — Deployment Drift</div>
            <div style="font-size:1.5rem; font-weight:800; color:white; margin-bottom:6px;">Hardcoded configs</div>
            <div style="font-size:0.85rem; color:rgba(255,255,255,0.55);">Jenkins · GHA · Terraform lack data abstractions</div>
            <div style="margin-top:12px; font-size:0.88rem; font-weight:700; color:#ffd700;">No reusable CI/CD pattern for data pipelines</div>
          </div>
          <div style="background:rgba(255,80,80,0.07); border:1px solid rgba(255,80,80,0.2); border-radius:10px; padding:20px 22px; border-left:3px solid rgba(255,100,100,0.55);">
            <div style="font-size:0.65rem; font-weight:700; color:rgba(255,140,140,0.85); text-transform:uppercase; letter-spacing:1.5px; margin-bottom:8px;">C4 — LLM Potential, Unknown Limits</div>
            <div style="font-size:1.5rem; font-weight:800; color:white; margin-bottom:6px;">7 models tested</div>
            <div style="font-size:0.85rem; color:rgba(255,255,255,0.55);">Reliability, complexity ceiling, failure modes uncharted</div>
            <div style="margin-top:12px; font-size:0.88rem; font-weight:700; color:#ffd700;">No multi-model benchmark for DEDPs existed</div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S3: DSR + POSA ═══ -->
    <div class="slide" id="slide-3">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#818cf8;">02 — Research Approach</div>
        <h2 class="slide-title" style="font-size:1.85rem; margin-bottom:16px;">DSR Methodology + POSA Pattern Template</h2>
        <div style="display:grid; grid-template-columns:1.1fr 0.9fr; gap:24px; align-items:start;">
          <div>
            <p style="font-size:0.65rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:10px;">Design Science Research — Peffers et al. (2007)</p>
            <div style="display:flex; flex-direction:column; gap:4px;">
              <div style="display:flex; align-items:center; gap:0;">
                <div style="background:rgba(129,140,248,0.18); border:1px solid rgba(129,140,248,0.28); border-radius:5px 0 0 5px; padding:9px 13px; font-size:0.82rem; font-weight:600; color:#a5b4fc; white-space:nowrap; min-width:140px;">1 · Problem ID</div>
                <div style="background:rgba(129,140,248,0.05); border:1px solid rgba(129,140,248,0.1); border-left:none; padding:9px 13px; font-size:0.8rem; color:rgba(255,255,255,0.45); flex:1;">SLR: 165 papers · IEEE, ACM, vendor docs, 290+ community threads</div>
              </div>
              <div style="display:flex; align-items:center; gap:0;">
                <div style="background:rgba(129,140,248,0.18); border:1px solid rgba(129,140,248,0.28); border-radius:5px 0 0 5px; padding:9px 13px; font-size:0.82rem; font-weight:600; color:#a5b4fc; white-space:nowrap; min-width:140px;">2 · Objectives</div>
                <div style="background:rgba(129,140,248,0.05); border:1px solid rgba(129,140,248,0.1); border-left:none; padding:9px 13px; font-size:0.8rem; color:rgba(255,255,255,0.45); flex:1;">Cloud-agnostic POSA patterns for ingestion · transformation · deployment</div>
              </div>
              <div style="display:flex; align-items:center; gap:0;">
                <div style="background:rgba(255,215,0,0.14); border:1px solid rgba(255,215,0,0.28); border-radius:5px 0 0 5px; padding:9px 13px; font-size:0.82rem; font-weight:700; color:#ffd700; white-space:nowrap; min-width:140px;">3 · Design ★</div>
                <div style="background:rgba(255,215,0,0.06); border:1px solid rgba(255,215,0,0.14); border-left:none; padding:9px 13px; font-size:0.8rem; color:rgba(255,215,0,0.75); flex:1;">MIND · ETLT++ · ELTL++ · EADF patterns formalized</div>
              </div>
              <div style="display:flex; align-items:center; gap:0;">
                <div style="background:rgba(255,215,0,0.14); border:1px solid rgba(255,215,0,0.28); border-radius:5px 0 0 5px; padding:9px 13px; font-size:0.82rem; font-weight:700; color:#ffd700; white-space:nowrap; min-width:140px;">4 · Demo ★</div>
                <div style="background:rgba(255,215,0,0.06); border:1px solid rgba(255,215,0,0.14); border-left:none; padding:9px 13px; font-size:0.8rem; color:rgba(255,215,0,0.75); flex:1;">3 production deployments: UNICC (Azure) · GCP · Databricks</div>
              </div>
              <div style="display:flex; align-items:center; gap:0;">
                <div style="background:rgba(255,215,0,0.14); border:1px solid rgba(255,215,0,0.28); border-radius:5px 0 0 5px; padding:9px 13px; font-size:0.82rem; font-weight:700; color:#ffd700; white-space:nowrap; min-width:140px;">5 · Evaluation ★</div>
                <div style="background:rgba(255,215,0,0.06); border:1px solid rgba(255,215,0,0.14); border-left:none; padding:9px 13px; font-size:0.8rem; color:rgba(255,215,0,0.75); flex:1;">N=21 expert survey (avg 4.6/5) + 7-model LLM benchmark</div>
              </div>
              <div style="display:flex; align-items:center; gap:0;">
                <div style="background:rgba(129,140,248,0.18); border:1px solid rgba(129,140,248,0.28); border-radius:5px 0 0 5px; padding:9px 13px; font-size:0.82rem; font-weight:600; color:#a5b4fc; white-space:nowrap; min-width:140px;">6 · Communication</div>
                <div style="background:rgba(129,140,248,0.05); border:1px solid rgba(129,140,248,0.1); border-left:none; padding:9px 13px; font-size:0.8rem; color:rgba(255,255,255,0.45); flex:1;">Defense + pattern website + open-source repository + practitioner blog</div>
              </div>
            </div>
          </div>
          <div>
            <p style="font-size:0.65rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:10px;">POSA/GoF Pattern Template</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:7px; margin-bottom:12px;">
              <div style="background:rgba(255,255,255,0.05); border-radius:7px; padding:12px 13px; display:flex; align-items:flex-start; gap:9px;">
                <div style="font-size:1.1rem; flex-shrink:0; margin-top:1px;">🏷️</div>
                <div><strong style="font-size:0.84rem; color:#a5b4fc; display:block;">Name</strong><span style="font-size:0.73rem; color:rgba(255,255,255,0.4);">Unique DEDP identifier</span></div>
              </div>
              <div style="background:rgba(255,255,255,0.05); border-radius:7px; padding:12px 13px; display:flex; align-items:flex-start; gap:9px;">
                <div style="font-size:1.1rem; flex-shrink:0; margin-top:1px;">🌐</div>
                <div><strong style="font-size:0.84rem; color:#a5b4fc; display:block;">Context</strong><span style="font-size:0.73rem; color:rgba(255,255,255,0.4);">Applicable environment</span></div>
              </div>
              <div style="background:rgba(255,255,255,0.05); border-radius:7px; padding:12px 13px; display:flex; align-items:flex-start; gap:9px;">
                <div style="font-size:1.1rem; flex-shrink:0; margin-top:1px;">⚠️</div>
                <div><strong style="font-size:0.84rem; color:#a5b4fc; display:block;">Problem</strong><span style="font-size:0.73rem; color:rgba(255,255,255,0.4);">Recurring challenge</span></div>
              </div>
              <div style="background:rgba(255,255,255,0.05); border-radius:7px; padding:12px 13px; display:flex; align-items:flex-start; gap:9px;">
                <div style="font-size:1.1rem; flex-shrink:0; margin-top:1px;">✅</div>
                <div><strong style="font-size:0.84rem; color:#a5b4fc; display:block;">Solution</strong><span style="font-size:0.73rem; color:rgba(255,255,255,0.4);">Reusable structure</span></div>
              </div>
              <div style="background:rgba(255,215,0,0.09); border:1px solid rgba(255,215,0,0.22); border-radius:7px; padding:12px 13px; display:flex; align-items:flex-start; gap:9px;">
                <div style="font-size:1.1rem; flex-shrink:0; margin-top:1px;">⚡</div>
                <div><strong style="font-size:0.84rem; color:#ffd700; display:block;">Forces ★</strong><span style="font-size:0.73rem; color:rgba(255,215,0,0.5);">Conflicting constraints</span></div>
              </div>
              <div style="background:rgba(255,215,0,0.09); border:1px solid rgba(255,215,0,0.22); border-radius:7px; padding:12px 13px; display:flex; align-items:flex-start; gap:9px;">
                <div style="font-size:1.1rem; flex-shrink:0; margin-top:1px;">⚖️</div>
                <div><strong style="font-size:0.84rem; color:#ffd700; display:block;">Consequences ★</strong><span style="font-size:0.73rem; color:rgba(255,215,0,0.5);">Benefits + liabilities</span></div>
              </div>
            </div>
            <div style="background:rgba(255,215,0,0.06); border:1px solid rgba(255,215,0,0.18); border-radius:8px; padding:11px 14px;">
              <p style="font-size:0.8rem; color:rgba(255,215,0,0.9); line-height:1.5; margin:0;"><strong>★ Novel:</strong> Forces &amp; Consequences formalized for Data Engineering for the first time — prior work describes tools, not reusable patterns with explicit trade-offs.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S4: MIND PROBLEM ═══ -->
    <div class="slide" id="slide-4">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#60a5fa;">MIND Pattern — 1/3 &nbsp;·&nbsp; Problem</div>
        <h2 class="slide-title" style="color:#60a5fa; font-size:1.85rem; margin-bottom:18px;">MIND — N sources, N bespoke pipelines</h2>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; align-items:start;">
          <div>
            <!-- 📷 IMAGE: Figure from thesis showing the N→N pipeline explosion diagram (Chapter 3 / MIND motivation figure) -->
            <div style="background:rgba(33,150,243,0.06); border:2px dashed rgba(33,150,243,0.25); border-radius:10px; height:200px; display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:14px;">
              <span style="font-size:2rem; margin-bottom:8px;">📷</span>
              <span style="font-size:0.78rem; color:rgba(255,255,255,0.35); text-align:center; padding:0 20px;">Place thesis figure here:<br>N-source → N-pipeline explosion</span>
              <code style="font-size:0.65rem; color:rgba(33,150,243,0.5); margin-top:6px;">resources/img/mind-problem.png</code>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:7px;">
              <div style="background:rgba(255,80,80,0.08); border-radius:7px; padding:10px 12px; text-align:center;">
                <div style="font-size:1.6rem; font-weight:800; color:#f87171;">O(N)</div>
                <div style="font-size:0.72rem; color:rgba(255,255,255,0.45); margin-top:3px;">pipelines per source</div>
              </div>
              <div style="background:rgba(255,80,80,0.08); border-radius:7px; padding:10px 12px; text-align:center;">
                <div style="font-size:1.6rem; font-weight:800; color:#f87171;">10–40%</div>
                <div style="font-size:0.72rem; color:rgba(255,255,255,0.45); margin-top:3px;">dev time on config</div>
              </div>
            </div>
          </div>
          <div>
            <div style="background:rgba(255,80,80,0.07); border-left:3px solid rgba(255,100,100,0.5); border-radius:8px; padding:14px 17px; margin-bottom:14px;">
              <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,140,140,0.85); margin-bottom:10px;">Problem</p>
              <ul style="list-style:none; font-size:0.85rem; color:rgba(255,255,255,0.7); line-height:1.8;">
                <li>▸ One pipeline per source — hardcoded, brittle</li>
                <li>▸ Schema change → pipeline breaks → redeploy</li>
                <li>▸ Config duplicated per source and per environment</li>
                <li>▸ No reusable abstraction for multi-source ingestion</li>
              </ul>
            </div>
            <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:8px;">Literature Gap (SLR — 165 sources)</p>
            <table class="mini-table" style="border-radius:7px; overflow:hidden; font-size:0.83rem;">
              <thead><tr><th>Approach</th><th style="text-align:center;">Reusable</th><th style="text-align:center;">Cloud-Agnostic</th><th style="text-align:center;">POSA</th></tr></thead>
              <tbody>
                <tr><td>Lambda / Kappa</td><td style="text-align:center; color:#f59e0b;">⚠</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                <tr><td>Data Mesh</td><td style="text-align:center; color:#22c55e;">✓</td><td style="text-align:center; color:#22c55e;">✓</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                <tr><td>NiFi / Airbyte</td><td style="text-align:center; color:#22c55e;">✓</td><td style="text-align:center; color:#22c55e;">✓</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                <tr style="background:rgba(33,150,243,0.1);"><td style="color:#60a5fa; font-weight:700;">MIND ★</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S5: MIND SOLUTION ═══ -->
    <div class="slide" id="slide-5">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#60a5fa;">MIND Pattern — 2/3 &nbsp;·&nbsp; Solution</div>
        <h2 class="slide-title" style="color:#60a5fa; font-size:1.85rem; margin-bottom:18px;">Unified Metadata Table (UMT) + Generic Engine</h2>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; align-items:start;">
          <div>
            <!-- 📷 IMAGE: Figure from thesis showing the UMT architecture (1 engine → UMT → N sources) -->
            <div style="background:rgba(33,150,243,0.06); border:2px dashed rgba(33,150,243,0.25); border-radius:10px; height:180px; display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:14px;">
              <span style="font-size:2rem; margin-bottom:8px;">📷</span>
              <span style="font-size:0.78rem; color:rgba(255,255,255,0.35); text-align:center; padding:0 20px;">Thesis figure: MIND architecture<br>UMT → Generic Engine → N sources</span>
              <code style="font-size:0.65rem; color:rgba(33,150,243,0.5); margin-top:6px;">resources/img/mind-architecture.png</code>
            </div>
            <div style="background:rgba(0,0,0,0.35); border-radius:7px; padding:12px 15px; font-family:'JetBrains Mono',monospace; font-size:0.75rem; color:rgba(150,220,255,0.85); line-height:1.7; border:1px solid rgba(255,255,255,0.07);">
              <span style="color:#c084fc;">for</span> r <span style="color:#c084fc;">in</span> UMT:<br>
              &nbsp;&nbsp;config ← extract_config(r)<br>
              &nbsp;&nbsp;<span style="color:#c084fc;">if</span> config.type == <span style="color:#86efac;">'incremental'</span>: run_incremental(config)<br>
              &nbsp;&nbsp;<span style="color:#c084fc;">else</span>: run_full(config)<br>
              &nbsp;&nbsp;load(config.target) ; log_result(r)
            </div>
          </div>
          <div>
            <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:8px;">Example UMT — UNICC DEDP (production)</p>
            <div style="border-radius:7px; border:1px solid rgba(33,150,243,0.22); overflow:hidden; margin-bottom:14px;">
              <table style="width:100%; border-collapse:collapse; font-family:'JetBrains Mono',monospace; font-size:0.71rem;">
                <thead><tr style="background:rgba(33,150,243,0.16);">
                  <th style="padding:7px 8px; text-align:left; color:#60a5fa; font-weight:600;">source</th>
                  <th style="padding:7px 8px; text-align:left; color:#60a5fa; font-weight:600;">type</th>
                  <th style="padding:7px 8px; text-align:left; color:#60a5fa; font-weight:600;">mode</th>
                  <th style="padding:7px 8px; text-align:left; color:#60a5fa; font-weight:600;">watermark</th>
                </tr></thead>
                <tbody>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:5px 8px; color:rgba(255,255,255,0.82);">WHO_Health_API</td><td style="padding:5px 8px; color:#86efac;">REST_JSON</td><td style="padding:5px 8px;">incremental</td><td style="padding:5px 8px; color:rgba(255,255,255,0.4);">updated_at</td></tr>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:5px 8px; color:rgba(255,255,255,0.82);">UNICC_PostgreSQL</td><td style="padding:5px 8px; color:#93c5fd;">RDBMS</td><td style="padding:5px 8px;">hybrid</td><td style="padding:5px 8px; color:rgba(255,255,255,0.4);">modified_at</td></tr>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:5px 8px; color:rgba(255,255,255,0.82);">Azure_Blob_Logs</td><td style="padding:5px 8px; color:#fbbf24;">BLOB_CSV</td><td style="padding:5px 8px;">full</td><td style="padding:5px 8px; color:rgba(255,255,255,0.25);">—</td></tr>
                  <tr><td style="padding:5px 8px; color:rgba(255,255,255,0.82);">Salesforce_CRM</td><td style="padding:5px 8px; color:#f87171;">SOAP_XML</td><td style="padding:5px 8px;">incremental</td><td style="padding:5px 8px; color:rgba(255,255,255,0.4);">updated_at</td></tr>
                </tbody>
              </table>
            </div>
            <div style="background:rgba(33,150,243,0.08); border-left:3px solid rgba(33,150,243,0.4); border-radius:6px; padding:11px 14px; margin-bottom:10px;">
              <p style="font-size:0.85rem; color:rgba(255,255,255,0.75); margin:0;">Adding a new source = <strong style="color:white;">1 SQL INSERT</strong> into UMT.<br>Zero code change in the ingestion engine.</p>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:7px;">
              <div style="background:rgba(255,255,255,0.04); border-radius:6px; padding:9px 11px; text-align:center;"><div style="font-size:0.8rem; font-weight:700; color:#60a5fa;">Full Load</div><div style="font-size:0.72rem; color:rgba(255,255,255,0.4); margin-top:2px;">Initial / reference tables</div></div>
              <div style="background:rgba(255,255,255,0.04); border-radius:6px; padding:9px 11px; text-align:center;"><div style="font-size:0.8rem; font-weight:700; color:#60a5fa;">Date Incr.</div><div style="font-size:0.72rem; color:rgba(255,255,255,0.4); margin-top:2px;">WHERE updated_at &gt; watermark</div></div>
              <div style="background:rgba(255,255,255,0.04); border-radius:6px; padding:9px 11px; text-align:center;"><div style="font-size:0.8rem; font-weight:700; color:#60a5fa;">Hash Incr.</div><div style="font-size:0.72rem; color:rgba(255,255,255,0.4); margin-top:2px;">hash(src) ≠ hash(tgt)</div></div>
              <div style="background:rgba(255,255,255,0.04); border-radius:6px; padding:9px 11px; text-align:center;"><div style="font-size:0.8rem; font-weight:700; color:#60a5fa;">Hybrid</div><div style="font-size:0.72rem; color:rgba(255,255,255,0.4); margin-top:2px;">Large frequently-updated data</div></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S6: MIND VALIDATION + SoA ═══ -->
    <div class="slide" id="slide-6">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#60a5fa;">MIND Pattern — 3/3 &nbsp;·&nbsp; Forces · Validation · SoA</div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; align-items:start; margin-top:4px;">
          <div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:7px; margin-bottom:14px;">
              <div style="background:rgba(255,255,255,0.05); border-radius:7px; padding:11px 13px;">
                <p style="font-size:0.65rem; font-weight:700; color:#86efac; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;">Benefits</p>
                <ul style="list-style:none; font-size:0.8rem; color:rgba(255,255,255,0.62); line-height:1.7;">
                  <li>✓ Cloud-agnostic (Azure + GCP)</li>
                  <li>✓ New source = 1 SQL INSERT</li>
                  <li>✓ Schema evolution handled</li>
                  <li>✓ 4 ingestion strategies</li>
                </ul>
              </div>
              <div style="background:rgba(255,255,255,0.05); border-radius:7px; padding:11px 13px;">
                <p style="font-size:0.65rem; font-weight:700; color:#f87171; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;">Trade-offs</p>
                <ul style="list-style:none; font-size:0.8rem; color:rgba(255,255,255,0.62); line-height:1.7;">
                  <li>⚠ Initial abstraction design cost</li>
                  <li>⚠ UMT schema governance needed</li>
                </ul>
                <p style="font-size:0.65rem; font-weight:700; color:#fbbf24; text-transform:uppercase; letter-spacing:1px; margin:10px 0 6px;">Known Uses</p>
                <ul style="list-style:none; font-size:0.79rem; color:rgba(255,255,255,0.62); line-height:1.65;">
                  <li>▸ Azure: ADF+Databricks 4.3× at 1B rows</li>
                  <li>▸ GCP: CockroachDB watermark</li>
                  <li>▸ Healthcare: 30+ IoT + EHR sources</li>
                </ul>
              </div>
            </div>
            <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:7px;">
              <div class="stat-card"><div class="stat-num" style="color:#60a5fa; font-size:1.5rem;">4.3×</div><div class="stat-label">speedup (1B rows)</div></div>
              <div class="stat-card"><div class="stat-num" style="color:#60a5fa; font-size:1.5rem;">4.7/5</div><div class="stat-label">expert utility</div></div>
              <div class="stat-card"><div class="stat-num" style="color:#60a5fa; font-size:1.5rem;">61%</div><div class="stat-label">config reduced</div></div>
              <div class="stat-card"><div class="stat-num" style="color:#60a5fa; font-size:1.5rem;">76%</div><div class="stat-label">problem recog.</div></div>
            </div>
          </div>
          <div>
            <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:8px;">State of the Art — Ingestion</p>
            <div style="overflow:hidden; border-radius:8px; border:1px solid rgba(255,255,255,0.07); margin-bottom:10px;">
              <table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
                <thead><tr style="background:rgba(255,255,255,0.06);">
                  <th style="padding:8px 10px; text-align:left; color:rgba(255,255,255,0.4); font-weight:600; font-size:0.7rem;">Approach</th>
                  <th style="padding:8px 8px; text-align:center; font-size:0.68rem; color:rgba(255,255,255,0.35);">Plat. Indep.</th>
                  <th style="padding:8px 8px; text-align:center; font-size:0.68rem; color:rgba(255,255,255,0.35);">Dyn. Strategy</th>
                  <th style="padding:8px 8px; text-align:center; font-size:0.68rem; color:rgba(255,255,255,0.35);">POSA</th>
                  <th style="padding:8px 8px; text-align:center; font-size:0.68rem; color:rgba(255,255,255,0.35);">Validated</th>
                </tr></thead>
                <tbody>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:6px 10px;">Lambda / Kappa</td><td style="text-align:center;">⚠</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center;">⚠</td></tr>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:6px 10px;">Data Mesh</td><td style="text-align:center; color:#22c55e;">✓</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:6px 10px;">Azure Data Factory</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:6px 10px;">NiFi / Airbyte</td><td style="text-align:center; color:#22c55e;">✓</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:6px 10px;">Academic meta-ETL</td><td style="text-align:center;">⚠</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                  <tr style="background:rgba(33,150,243,0.09);"><td style="padding:6px 10px; font-weight:700; color:#60a5fa;">★ MIND (this work)</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td></tr>
                </tbody>
              </table>
            </div>
            <!-- 📷 IMAGE: Figure from thesis/website showing the MIND validation results chart or Azure deployment diagram -->
            <div style="background:rgba(33,150,243,0.05); border:2px dashed rgba(33,150,243,0.2); border-radius:8px; height:110px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
              <span style="font-size:1.4rem; margin-bottom:5px;">📷</span>
              <span style="font-size:0.73rem; color:rgba(255,255,255,0.3); text-align:center;">Thesis figure: Azure validation results<br>(e.g., throughput comparison chart)</span>
              <code style="font-size:0.62rem; color:rgba(33,150,243,0.4); margin-top:4px;">resources/img/mind-validation.png</code>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S7: ETLT/ELTL PROBLEM ═══ -->
    <div class="slide" id="slide-7">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#c084fc;">ETLT++ / ELTL++ — 1/3 &nbsp;·&nbsp; Problem</div>
        <h2 class="slide-title" style="color:#c084fc; font-size:1.85rem; margin-bottom:18px;">The Transformation Timing Problem</h2>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; align-items:start;">
          <div>
            <!-- 📷 IMAGE: Figure from thesis showing ETL vs ELT trade-off diagram or the hybrid motivation figure -->
            <div style="background:rgba(156,39,176,0.06); border:2px dashed rgba(156,39,176,0.25); border-radius:10px; height:180px; display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:14px;">
              <span style="font-size:2rem; margin-bottom:8px;">📷</span>
              <span style="font-size:0.78rem; color:rgba(255,255,255,0.35); text-align:center; padding:0 20px;">Thesis figure: ETL vs ELT limitations<br>or the 78% survey result chart</span>
              <code style="font-size:0.65rem; color:rgba(156,39,176,0.5); margin-top:6px;">resources/img/etlt-problem.png</code>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:9px;">
              <div style="background:rgba(255,255,255,0.04); border-radius:8px; padding:12px; text-align:center;">
                <div style="font-family:'JetBrains Mono',monospace; font-size:0.9rem; color:rgba(255,255,255,0.7); margin-bottom:5px;">E → T → L</div>
                <div style="font-size:0.7rem; font-weight:700; color:rgba(255,80,80,0.8);">Loses raw fidelity</div>
              </div>
              <div style="background:rgba(255,255,255,0.04); border-radius:8px; padding:12px; text-align:center;">
                <div style="font-family:'JetBrains Mono',monospace; font-size:0.9rem; color:rgba(255,255,255,0.7); margin-bottom:5px;">E → L → T</div>
                <div style="font-size:0.7rem; font-weight:700; color:rgba(255,80,80,0.8);">Bad data lands in lake</div>
              </div>
            </div>
          </div>
          <div>
            <div style="background:rgba(255,80,80,0.07); border-left:3px solid rgba(255,100,100,0.5); border-radius:8px; padding:14px 17px; margin-bottom:14px;">
              <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,140,140,0.85); margin-bottom:10px;">Problem</p>
              <ul style="list-style:none; font-size:0.85rem; color:rgba(255,255,255,0.7); line-height:1.8;">
                <li>▸ <strong style="color:white;">78%</strong> use ad-hoc hybrid ETL/ELT without guidance</li>
                <li>▸ No formal criteria to choose between strategies</li>
                <li>▸ Data contracts not formalized in either approach</li>
                <li>▸ Rejected records cannot be replayed in pure ETL</li>
              </ul>
            </div>
            <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:8px;">Literature Gap</p>
            <table class="mini-table" style="border-radius:7px; overflow:hidden; font-size:0.83rem;">
              <thead><tr><th>Approach</th><th style="text-align:center;">Hybrid Formalized</th><th style="text-align:center;">Decision Criteria</th><th style="text-align:center;">POSA</th></tr></thead>
              <tbody>
                <tr><td>ETL / ELT pure</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                <tr><td>dbt</td><td style="text-align:center;">⚠</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                <tr><td>Databricks DLT</td><td style="text-align:center;">⚠</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                <tr style="background:rgba(156,39,176,0.1);"><td style="color:#c084fc; font-weight:700;">★ ETLT++ / ELTL++</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S8: ETLT/ELTL PATTERNS ═══ -->
    <div class="slide" id="slide-8">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#c084fc;">ETLT++ / ELTL++ — 2/3 &nbsp;·&nbsp; Pattern Details</div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px; align-items:start; margin-top:8px;">
          <div>
            <div style="background:rgba(33,150,243,0.08); border-top:3px solid #2196f3; border-radius:0 0 9px 9px; padding:14px 17px; margin-bottom:12px;">
              <p style="font-size:0.9rem; font-weight:700; color:#60a5fa; margin-bottom:6px; font-family:'JetBrains Mono',monospace;">ETLT++ &nbsp; E → T₁ → L → T₂</p>
              <ul style="list-style:none; font-size:0.82rem; color:rgba(255,255,255,0.65); line-height:1.7;">
                <li>▸ T₁ = quality gate · contract · quarantine</li>
                <li>▸ T₂ = business logic · enrichment · KPIs</li>
                <li>▸ Clean data guaranteed at landing</li>
                <li>▸ Use: regulated sources, strict SLA</li>
              </ul>
            </div>
            <div style="background:rgba(156,39,176,0.08); border-top:3px solid #9c27b0; border-radius:0 0 9px 9px; padding:14px 17px;">
              <p style="font-size:0.9rem; font-weight:700; color:#c084fc; margin-bottom:6px; font-family:'JetBrains Mono',monospace;">ELTL++ &nbsp; E → L(raw) → T → L(curated)</p>
              <ul style="list-style:none; font-size:0.82rem; color:rgba(255,255,255,0.65); line-height:1.7;">
                <li>▸ Raw = immutable · versioned · Delta/Iceberg</li>
                <li>▸ Time travel · schema evolution · multi-team</li>
                <li>▸ Full audit trail always preserved</li>
                <li>▸ Use: IoT, finance, forensics, research</li>
              </ul>
            </div>
          </div>
          <div>
            <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:8px;">Decision Framework</p>
            <table style="width:100%; border-collapse:collapse; font-size:0.8rem; border-radius:8px; overflow:hidden; margin-bottom:12px;">
              <thead><tr>
                <th style="padding:9px 10px; background:rgba(255,255,255,0.08); text-align:left; font-size:0.7rem; text-transform:uppercase; color:rgba(255,255,255,0.4);">Criterion</th>
                <th style="padding:9px 10px; background:rgba(33,150,243,0.15); text-align:center; font-size:0.7rem; color:#60a5fa;">ETLT++</th>
                <th style="padding:9px 10px; background:rgba(156,39,176,0.15); text-align:center; font-size:0.7rem; color:#c084fc;">ELTL++</th>
              </tr></thead>
              <tbody>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:7px 10px; color:rgba(255,255,255,0.6);">Data quality priority</td><td style="text-align:center; color:#22c55e; font-weight:600;">High — ingestion</td><td style="text-align:center; color:rgba(255,255,255,0.3);">Deferred</td></tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:7px 10px; color:rgba(255,255,255,0.6);">Audit / compliance</td><td style="text-align:center; color:rgba(255,255,255,0.3);">Moderate</td><td style="text-align:center; color:#22c55e; font-weight:600;">Full raw history</td></tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:7px 10px; color:rgba(255,255,255,0.6);">Schema evolution</td><td style="text-align:center; color:rgba(255,255,255,0.3);">Slow / stable</td><td style="text-align:center; color:#22c55e; font-weight:600;">Fast / frequent</td></tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:7px 10px; color:rgba(255,255,255,0.6);">Query latency SLO</td><td style="text-align:center; color:#22c55e; font-weight:600;">Strict</td><td style="text-align:center; color:rgba(255,255,255,0.3);">Flexible</td></tr>
                <tr><td style="padding:7px 10px; color:rgba(255,255,255,0.6);">Storage cost</td><td style="text-align:center; color:#22c55e; font-weight:600;">Low</td><td style="text-align:center; color:rgba(255,255,255,0.3);">High (raw+curated)</td></tr>
              </tbody>
            </table>
            <!-- 📷 IMAGE: Figure from thesis showing ETLT++ vs ELTL++ flow diagram side by side -->
            <div style="background:rgba(156,39,176,0.05); border:2px dashed rgba(156,39,176,0.2); border-radius:8px; height:100px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
              <span style="font-size:1.4rem; margin-bottom:5px;">📷</span>
              <span style="font-size:0.73rem; color:rgba(255,255,255,0.3); text-align:center;">Thesis figure: ETLT++ vs ELTL++ flow diagram</span>
              <code style="font-size:0.62rem; color:rgba(156,39,176,0.4); margin-top:4px;">resources/img/etlt-flows.png</code>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S9: ETLT/ELTL VALIDATION + SoA ═══ -->
    <div class="slide" id="slide-9">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#c084fc;">ETLT++ / ELTL++ — 3/3 &nbsp;·&nbsp; Validation · SoA</div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; align-items:start; margin-top:8px;">
          <div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:7px; margin-bottom:14px;">
              <div style="background:rgba(255,255,255,0.05); border-radius:7px; padding:11px 13px;">
                <p style="font-size:0.65rem; font-weight:700; color:#86efac; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;">Benefits</p>
                <ul style="list-style:none; font-size:0.8rem; color:rgba(255,255,255,0.62); line-height:1.7;">
                  <li>✓ ETLT++: clean data at landing</li>
                  <li>✓ ELTL++: full audit · time travel</li>
                  <li>✓ Formal data contracts</li>
                  <li>✓ 3.3× throughput improvement</li>
                </ul>
              </div>
              <div style="background:rgba(255,255,255,0.05); border-radius:7px; padding:11px 13px;">
                <p style="font-size:0.65rem; font-weight:700; color:#f87171; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;">Trade-offs</p>
                <ul style="list-style:none; font-size:0.8rem; color:rgba(255,255,255,0.62); line-height:1.7;">
                  <li>⚠ ETLT++: can't replay rejected</li>
                  <li>⚠ ELTL++: higher storage</li>
                </ul>
                <p style="font-size:0.65rem; font-weight:700; color:#fbbf24; text-transform:uppercase; letter-spacing:1px; margin:10px 0 6px;">Known Uses</p>
                <ul style="list-style:none; font-size:0.79rem; color:rgba(255,255,255,0.62); line-height:1.65;">
                  <li>▸ Databricks DLT: Bronze/Silver/Gold</li>
                  <li>▸ Azure UNICC: regulated health data</li>
                  <li>▸ Finance: GDPR/HIPAA audit</li>
                </ul>
              </div>
            </div>
            <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:7px;">
              <div class="stat-card"><div class="stat-num" style="color:#c084fc; font-size:1.5rem;">3.3×</div><div class="stat-label">throughput</div></div>
              <div class="stat-card"><div class="stat-num" style="color:#c084fc; font-size:1.5rem;">69%</div><div class="stat-label">TCO reduction</div></div>
              <div class="stat-card"><div class="stat-num" style="color:#c084fc; font-size:1.5rem;">4.4/5</div><div class="stat-label">expert utility</div></div>
            </div>
          </div>
          <div>
            <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:8px;">State of the Art — Transformation</p>
            <div style="overflow:hidden; border-radius:8px; border:1px solid rgba(255,255,255,0.07); margin-bottom:12px;">
              <table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
                <thead><tr style="background:rgba(255,255,255,0.06);">
                  <th style="padding:8px 10px; text-align:left; color:rgba(255,255,255,0.4); font-weight:600; font-size:0.7rem;">Approach</th>
                  <th style="padding:8px 8px; text-align:center; font-size:0.68rem; color:rgba(255,255,255,0.35);">Hybrid</th>
                  <th style="padding:8px 8px; text-align:center; font-size:0.68rem; color:rgba(255,255,255,0.35);">Decision</th>
                  <th style="padding:8px 8px; text-align:center; font-size:0.68rem; color:rgba(255,255,255,0.35);">Contracts</th>
                  <th style="padding:8px 8px; text-align:center; font-size:0.68rem; color:rgba(255,255,255,0.35);">POSA</th>
                </tr></thead>
                <tbody>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:6px 10px;">ETL / ELT pure</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:6px 10px;">dbt</td><td style="text-align:center;">⚠</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center;">⚠</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:6px 10px;">Databricks DLT</td><td style="text-align:center;">⚠</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#22c55e;">✓</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:6px 10px;">Apache Spark only</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                  <tr style="background:rgba(156,39,176,0.09);"><td style="padding:6px 10px; font-weight:700; color:#c084fc;">★ ETLT++ / ELTL++</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td></tr>
                </tbody>
              </table>
            </div>
            <!-- 📷 IMAGE: Figure from thesis showing throughput benchmark or TCO comparison chart -->
            <div style="background:rgba(156,39,176,0.05); border:2px dashed rgba(156,39,176,0.2); border-radius:8px; height:110px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
              <span style="font-size:1.4rem; margin-bottom:5px;">📷</span>
              <span style="font-size:0.73rem; color:rgba(255,255,255,0.3); text-align:center;">Thesis figure: throughput / TCO benchmark chart</span>
              <code style="font-size:0.62rem; color:rgba(156,39,176,0.4); margin-top:4px;">resources/img/etlt-validation.png</code>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S10: EADF PROBLEM ═══ -->
    <div class="slide" id="slide-10">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#a78bfa;">EADF Pattern — 1/3 &nbsp;·&nbsp; Problem</div>
        <h2 class="slide-title" style="color:#a78bfa; font-size:1.85rem; margin-bottom:18px;">EADF — Deployment Drift from Early Binding</h2>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; align-items:start;">
          <div>
            <div style="display:grid; grid-template-columns:1fr auto 1fr; gap:10px; align-items:center; margin-bottom:16px;">
              <div style="background:rgba(255,80,80,0.1); border:1px solid rgba(255,80,80,0.25); border-radius:8px; padding:13px;">
                <strong style="font-size:0.8rem; color:#f87171; display:block; margin-bottom:6px;">Early Binding ❌</strong>
                <div style="font-family:'JetBrains Mono',monospace; font-size:0.68rem; color:rgba(255,255,255,0.5); line-height:1.7;">endpoint: "prod-api.azure.com"<br>region: "westeurope"<br>creds: "prod-key-123"</div>
                <div style="font-size:0.72rem; color:rgba(255,80,80,0.7); margin-top:6px;">Hardcoded = drift = lock-in</div>
              </div>
              <div style="font-size:1.4rem; color:rgba(255,255,255,0.2); text-align:center;">→</div>
              <div style="background:rgba(103,58,183,0.1); border:1px solid rgba(103,58,183,0.3); border-radius:8px; padding:13px;">
                <strong style="font-size:0.8rem; color:#a78bfa; display:block; margin-bottom:6px;">Late Binding ✓ (EADF)</strong>
                <div style="font-family:'JetBrains Mono',monospace; font-size:0.68rem; color:rgba(255,255,255,0.5); line-height:1.7;">endpoint: "{{env.api}}"<br>region: "{{env.region}}"<br>creds: "{{vault.creds}}"</div>
                <div style="font-size:0.72rem; color:#86efac; margin-top:6px;">Resolved at deploy time</div>
              </div>
            </div>
            <div style="background:rgba(255,80,80,0.07); border-left:3px solid rgba(255,100,100,0.5); border-radius:8px; padding:13px 17px;">
              <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,140,140,0.85); margin-bottom:10px;">Problem</p>
              <ul style="list-style:none; font-size:0.85rem; color:rgba(255,255,255,0.7); line-height:1.8;">
                <li>▸ Env details (endpoints, creds) hardcoded at authoring</li>
                <li>▸ Config duplicated per environment — no single source of truth</li>
                <li>▸ No audit trail of promotions</li>
                <li>▸ Jenkins/GHA: no schema drift or data SLA concepts</li>
              </ul>
            </div>
          </div>
          <div>
            <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:8px;">CI/CD Gaps for Data Engineering</p>
            <table class="mini-table" style="border-radius:7px; overflow:hidden; margin-bottom:14px; font-size:0.83rem;">
              <thead><tr><th>Challenge</th><th>Tools</th><th style="color:rgba(255,80,80,0.8);">Gap</th></tr></thead>
              <tbody>
                <tr><td>Schema Evolution</td><td style="font-size:0.75rem; color:rgba(255,255,255,0.45);">Hudi, Iceberg</td><td style="font-size:0.75rem; color:rgba(255,150,150,0.8);">No deploy checks</td></tr>
                <tr><td>Env. Drift</td><td style="font-size:0.75rem; color:rgba(255,255,255,0.45);">Jenkins, GitLab</td><td style="font-size:0.75rem; color:rgba(255,150,150,0.8);">Early binding</td></tr>
                <tr><td>Multi-Cloud</td><td style="font-size:0.75rem; color:rgba(255,255,255,0.45);">Ad-hoc</td><td style="font-size:0.75rem; color:rgba(255,150,150,0.8);">Vendor lock-in</td></tr>
                <tr><td>Auditability</td><td style="font-size:0.75rem; color:rgba(255,255,255,0.45);">Manual logs</td><td style="font-size:0.75rem; color:rgba(255,150,150,0.8);">No promotion tracking</td></tr>
              </tbody>
            </table>
            <!-- 📷 IMAGE: Figure from thesis showing deployment drift / environment mismatch diagram -->
            <div style="background:rgba(103,58,183,0.05); border:2px dashed rgba(103,58,183,0.22); border-radius:8px; height:130px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
              <span style="font-size:1.4rem; margin-bottom:5px;">📷</span>
              <span style="font-size:0.73rem; color:rgba(255,255,255,0.3); text-align:center;">Thesis figure: deployment drift diagram<br>or CI/CD pipeline gap illustration</span>
              <code style="font-size:0.62rem; color:rgba(103,58,183,0.4); margin-top:4px;">resources/img/eadf-problem.png</code>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S11: EADF SOLUTION ═══ -->
    <div class="slide" id="slide-11">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#a78bfa;">EADF Pattern — 2/3 &nbsp;·&nbsp; Solution</div>
        <h2 class="slide-title" style="color:#a78bfa; font-size:1.85rem; margin-bottom:18px;">4 YAML Descriptors + 7-Stage Promotion Pipeline</h2>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; align-items:start;">
          <div>
            <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:10px;">4 YAML Artifacts</p>
            <div style="display:flex; flex-direction:column; gap:7px; margin-bottom:12px;">
              <div style="background:rgba(103,58,183,0.1); border:1px solid rgba(103,58,183,0.22); border-radius:7px; padding:10px 14px; display:flex; align-items:flex-start; gap:10px;">
                <code style="font-size:0.82rem; color:#c4b5fd; flex-shrink:0; min-width:130px;">pipeline.yml</code>
                <span style="font-size:0.8rem; color:rgba(255,255,255,0.5);">Zero hardcoded values — authored once, used everywhere</span>
              </div>
              <div style="background:rgba(103,58,183,0.1); border:1px solid rgba(103,58,183,0.22); border-radius:7px; padding:10px 14px; display:flex; align-items:flex-start; gap:10px;">
                <code style="font-size:0.82rem; color:#c4b5fd; flex-shrink:0; min-width:130px;">env-catalog.yml</code>
                <span style="font-size:0.8rem; color:rgba(255,255,255,0.5);">Dev/staging/prod endpoints — bound at deploy time</span>
              </div>
              <div style="background:rgba(255,215,0,0.07); border:1px solid rgba(255,215,0,0.18); border-radius:7px; padding:10px 14px; display:flex; align-items:flex-start; gap:10px;">
                <code style="font-size:0.82rem; color:#fbbf24; flex-shrink:0; min-width:130px;">promotion-gate.yml</code>
                <span style="font-size:0.8rem; color:rgba(255,255,255,0.5);">Quality thresholds — hard stop if KPIs fail</span>
              </div>
              <div style="background:rgba(80,200,120,0.07); border:1px solid rgba(80,200,120,0.18); border-radius:7px; padding:10px 14px; display:flex; align-items:flex-start; gap:10px;">
                <code style="font-size:0.82rem; color:#86efac; flex-shrink:0; min-width:130px;">provenance.yml</code>
                <span style="font-size:0.8rem; color:rgba(255,255,255,0.5);">Immutable audit: who · what · from → to · when</span>
              </div>
            </div>
            <div style="background:rgba(103,58,183,0.08); border:1px solid rgba(103,58,183,0.2); border-radius:7px; padding:10px 14px;">
              <p style="font-size:0.82rem; color:rgba(255,255,255,0.72); margin:0;"><strong style="color:#a78bfa;">Key principle:</strong> Same pipeline.yml promotes dev → staging → prod. Only env-catalog changes. Drift eliminated by construction.</p>
            </div>
          </div>
          <div>
            <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:10px;">7-Stage Promotion Pipeline</p>
            <div style="display:flex; flex-direction:column; gap:3px; margin-bottom:12px;">
              <div style="display:flex;"><div style="background:rgba(103,58,183,0.2); border:1px solid rgba(103,58,183,0.3); border-radius:5px 0 0 5px; padding:8px 12px; font-size:0.8rem; font-weight:600; color:#c4b5fd; min-width:110px;">1 · Binding</div><div style="background:rgba(103,58,183,0.06); border:1px solid rgba(103,58,183,0.12); border-left:none; padding:8px 12px; font-size:0.77rem; color:rgba(255,255,255,0.5); flex:1;">env-catalog resolves {{placeholders}}</div></div>
              <div style="display:flex;"><div style="background:rgba(103,58,183,0.2); border:1px solid rgba(103,58,183,0.3); border-radius:5px 0 0 5px; padding:8px 12px; font-size:0.8rem; font-weight:600; color:#c4b5fd; min-width:110px;">2 · Build</div><div style="background:rgba(103,58,183,0.06); border:1px solid rgba(103,58,183,0.12); border-left:none; padding:8px 12px; font-size:0.77rem; color:rgba(255,255,255,0.5); flex:1;">Artifact packaged with bound values</div></div>
              <div style="display:flex;"><div style="background:rgba(103,58,183,0.2); border:1px solid rgba(103,58,183,0.3); border-radius:5px 0 0 5px; padding:8px 12px; font-size:0.8rem; font-weight:600; color:#c4b5fd; min-width:110px;">3 · Validation</div><div style="background:rgba(103,58,183,0.06); border:1px solid rgba(103,58,183,0.12); border-left:none; padding:8px 12px; font-size:0.77rem; color:rgba(255,255,255,0.5); flex:1;">Schema drift check · static analysis</div></div>
              <div style="display:flex;"><div style="background:rgba(103,58,183,0.2); border:1px solid rgba(103,58,183,0.3); border-radius:5px 0 0 5px; padding:8px 12px; font-size:0.8rem; font-weight:600; color:#c4b5fd; min-width:110px;">4 · Deployment</div><div style="background:rgba(103,58,183,0.06); border:1px solid rgba(103,58,183,0.12); border-left:none; padding:8px 12px; font-size:0.77rem; color:rgba(255,255,255,0.5); flex:1;">To target environment via CI toolchain</div></div>
              <div style="display:flex;"><div style="background:rgba(103,58,183,0.2); border:1px solid rgba(103,58,183,0.3); border-radius:5px 0 0 5px; padding:8px 12px; font-size:0.8rem; font-weight:600; color:#c4b5fd; min-width:110px;">5 · Smoke Test</div><div style="background:rgba(103,58,183,0.06); border:1px solid rgba(103,58,183,0.12); border-left:none; padding:8px 12px; font-size:0.77rem; color:rgba(255,255,255,0.5); flex:1;">Lightweight end-to-end verification</div></div>
              <div style="display:flex;"><div style="background:rgba(255,215,0,0.12); border:1px solid rgba(255,215,0,0.28); border-radius:5px 0 0 5px; padding:8px 12px; font-size:0.8rem; font-weight:700; color:#ffd700; min-width:110px;">6 · Gate 🚦</div><div style="background:rgba(255,215,0,0.04); border:1px solid rgba(255,215,0,0.1); border-left:none; padding:8px 12px; font-size:0.77rem; color:rgba(255,255,255,0.5); flex:1;">KPI thresholds → pass = next env; fail = stop + alert</div></div>
              <div style="display:flex;"><div style="background:rgba(80,200,120,0.12); border:1px solid rgba(80,200,120,0.28); border-radius:5px 0 0 5px; padding:8px 12px; font-size:0.8rem; font-weight:700; color:#86efac; min-width:110px;">7 · Provenance</div><div style="background:rgba(80,200,120,0.04); border:1px solid rgba(80,200,120,0.1); border-left:none; padding:8px 12px; font-size:0.77rem; color:rgba(255,255,255,0.5); flex:1;">Immutable audit record written → provenance.yml</div></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S12: EADF VALIDATION + SoA ═══ -->
    <div class="slide" id="slide-12">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#a78bfa;">EADF Pattern — 3/3 &nbsp;·&nbsp; Validation · SoA</div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; align-items:start; margin-top:8px;">
          <div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:7px; margin-bottom:14px;">
              <div style="background:rgba(255,255,255,0.05); border-radius:7px; padding:11px 13px;">
                <p style="font-size:0.65rem; font-weight:700; color:#86efac; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;">Benefits</p>
                <ul style="list-style:none; font-size:0.8rem; color:rgba(255,255,255,0.62); line-height:1.7;">
                  <li>✓ 61% config reduction</li>
                  <li>✓ 0 drift events post-adoption</li>
                  <li>✓ 67–78% fewer failures</li>
                  <li>✓ Full provenance trail</li>
                </ul>
              </div>
              <div style="background:rgba(255,255,255,0.05); border-radius:7px; padding:11px 13px;">
                <p style="font-size:0.65rem; font-weight:700; color:#f87171; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;">Trade-offs</p>
                <ul style="list-style:none; font-size:0.8rem; color:rgba(255,255,255,0.62); line-height:1.7;">
                  <li>⚠ Initial env-catalog setup cost</li>
                  <li>⚠ Team discipline required</li>
                </ul>
                <p style="font-size:0.65rem; font-weight:700; color:#fbbf24; text-transform:uppercase; letter-spacing:1px; margin:10px 0 6px;">Known Uses</p>
                <ul style="list-style:none; font-size:0.79rem; color:rgba(255,255,255,0.62); line-height:1.65;">
                  <li>▸ UNICC DEDP: Azure multi-env</li>
                  <li>▸ GCP + Databricks: cross-cloud</li>
                  <li>▸ Healthcare: regulated deploys</li>
                </ul>
              </div>
            </div>
            <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:7px;">
              <div class="stat-card"><div class="stat-num" style="color:#a78bfa; font-size:1.5rem;">61%</div><div class="stat-label">config reduced</div></div>
              <div class="stat-card"><div class="stat-num" style="color:#a78bfa; font-size:1.5rem;">0</div><div class="stat-label">drift events</div></div>
              <div class="stat-card"><div class="stat-num" style="color:#a78bfa; font-size:1.3rem;">67–78%</div><div class="stat-label">fewer failures</div></div>
              <div class="stat-card"><div class="stat-num" style="color:#a78bfa; font-size:1.5rem;">4.2/5</div><div class="stat-label">expert utility</div></div>
            </div>
          </div>
          <div>
            <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:8px;">State of the Art — Deployment</p>
            <div style="overflow:hidden; border-radius:8px; border:1px solid rgba(255,255,255,0.07); margin-bottom:12px;">
              <table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
                <thead><tr style="background:rgba(255,255,255,0.06);">
                  <th style="padding:8px 10px; text-align:left; color:rgba(255,255,255,0.4); font-weight:600; font-size:0.7rem;">Approach</th>
                  <th style="padding:8px 7px; text-align:center; font-size:0.68rem; color:rgba(255,255,255,0.35);">Late Binding</th>
                  <th style="padding:8px 7px; text-align:center; font-size:0.68rem; color:rgba(255,255,255,0.35);">Data Abstr.</th>
                  <th style="padding:8px 7px; text-align:center; font-size:0.68rem; color:rgba(255,255,255,0.35);">Provenance</th>
                  <th style="padding:8px 7px; text-align:center; font-size:0.68rem; color:rgba(255,255,255,0.35);">POSA</th>
                </tr></thead>
                <tbody>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:6px 10px;">Terraform / Pulumi</td><td style="text-align:center;">⚠</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:6px 10px;">Jenkins / GHA</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center;">⚠</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:6px 10px;">MLflow / TFX</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center;">⚠ ML</td><td style="text-align:center; color:#22c55e;">✓</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                  <tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:6px 10px;">DBT / Airflow</td><td style="text-align:center;">⚠</td><td style="text-align:center; color:#22c55e;">✓</td><td style="text-align:center; color:#ef4444;">✗</td><td style="text-align:center; color:#ef4444;">✗</td></tr>
                  <tr style="background:rgba(103,58,183,0.1);"><td style="padding:6px 10px; font-weight:700; color:#a78bfa;">★ EADF (this work)</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td><td style="text-align:center; color:#22c55e; font-weight:700;">✓</td></tr>
                </tbody>
              </table>
            </div>
            <!-- 📷 IMAGE: Figure from thesis showing EADF validation results (drift events, failure rates) -->
            <div style="background:rgba(103,58,183,0.05); border:2px dashed rgba(103,58,183,0.22); border-radius:8px; height:100px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
              <span style="font-size:1.4rem; margin-bottom:5px;">📷</span>
              <span style="font-size:0.73rem; color:rgba(255,255,255,0.3); text-align:center;">Thesis figure: EADF validation (failure rate reduction)</span>
              <code style="font-size:0.62rem; color:rgba(103,58,183,0.4); margin-top:4px;">resources/img/eadf-validation.png</code>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S13: LLM METHODOLOGY ═══ -->
    <div class="slide" id="slide-13">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#34d399;">Chapter 7 — LLM Benchmarking · 1/3</div>
        <h2 class="slide-title" style="font-size:1.85rem; margin-bottom:18px;">Benchmarking LLMs for Data Pipeline Generation</h2>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; align-items:start;">
          <div>
            <div style="background:rgba(52,211,153,0.07); border-left:3px solid #34d399; border-radius:7px; padding:13px 16px; margin-bottom:14px;">
              <p style="font-size:0.7rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:#34d399; margin-bottom:5px;">RQ4</p>
              <p style="font-size:0.88rem; color:rgba(255,255,255,0.75); line-height:1.5;">Can LLMs generate reliable, scalable, production-ready data engineering code? What are the complexity limits?</p>
            </div>
            <p style="font-size:0.65rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:9px;">7 Models · 3 Providers · Databricks Serverless · 5 Runs</p>
            <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:7px; margin-bottom:14px;">
              <div style="background:rgba(16,163,127,0.09); border-top:2px solid #10a37f; border-radius:0 0 7px 7px; padding:9px 11px;">
                <p style="font-size:0.65rem; font-weight:700; color:#10a37f; margin-bottom:5px;">OpenAI</p>
                <div style="font-size:0.78rem; font-weight:600; color:rgba(255,255,255,0.75); line-height:1.75;">GPT-5<br>GPT-5 Mini<br>GPT-5 Nano</div>
              </div>
              <div style="background:rgba(212,160,23,0.09); border-top:2px solid #d4a017; border-radius:0 0 7px 7px; padding:9px 11px;">
                <p style="font-size:0.65rem; font-weight:700; color:#d4a017; margin-bottom:5px;">Anthropic</p>
                <div style="font-size:0.78rem; font-weight:600; color:rgba(255,255,255,0.75); line-height:1.75;">Claude 4 Opus<br>Claude 4 Sonnet<br>Claude 3.5 Haiku</div>
              </div>
              <div style="background:rgba(255,107,53,0.09); border-top:2px solid #ff6b35; border-radius:0 0 7px 7px; padding:9px 11px;">
                <p style="font-size:0.65rem; font-weight:700; color:#ff6b35; margin-bottom:5px;">Alibaba</p>
                <div style="font-size:0.78rem; font-weight:600; color:rgba(255,255,255,0.75); line-height:1.75;">Qwen3-235B</div>
                <div style="font-size:0.68rem; color:rgba(255,255,255,0.35); margin-top:4px;">262K ctx · MoE</div>
              </div>
            </div>
            <div style="display:flex; flex-direction:column; gap:5px;">
              <div style="display:flex; align-items:center; gap:10px; background:rgba(59,130,246,0.07); border-radius:6px; padding:9px 12px;">
                <div style="width:22px; height:22px; background:#3b82f6; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:0.72rem; font-weight:700; flex-shrink:0;">1</div>
                <div><span style="font-size:0.82rem; font-weight:600; color:#93c5fd;">Data Quality Check</span><span style="font-size:0.75rem; color:rgba(255,255,255,0.4); margin-left:8px;">Basic · 1 source</span></div>
              </div>
              <div style="display:flex; align-items:center; gap:10px; background:rgba(139,92,246,0.07); border-radius:6px; padding:9px 12px;">
                <div style="width:22px; height:22px; background:#8b5cf6; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:0.72rem; font-weight:700; flex-shrink:0;">2</div>
                <div><span style="font-size:0.82rem; font-weight:600; color:#c4b5fd;">Monthly Aggregation</span><span style="font-size:0.75rem; color:rgba(255,255,255,0.4); margin-left:8px;">Medium · temporal logic</span></div>
              </div>
              <div style="display:flex; align-items:center; gap:10px; background:rgba(239,68,68,0.07); border-radius:6px; padding:9px 12px;">
                <div style="width:22px; height:22px; background:#ef4444; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:0.72rem; font-weight:700; flex-shrink:0;">3</div>
                <div><span style="font-size:0.82rem; font-weight:600; color:#fca5a5;">Multi-Source Merge</span><span style="font-size:0.75rem; color:rgba(255,255,255,0.4); margin-left:8px;">High · dual ingestion · join</span></div>
              </div>
            </div>
          </div>
          <div>
            <p style="font-size:0.65rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:9px;">5 Evaluation Metrics</p>
            <div style="display:flex; flex-direction:column; gap:6px; margin-bottom:14px;">
              <div style="background:rgba(255,255,255,0.05); border-radius:6px; padding:10px 13px; display:flex; align-items:center; gap:10px;">
                <div style="width:8px; height:8px; background:#34d399; border-radius:50%; flex-shrink:0;"></div>
                <div><span style="font-size:0.83rem; font-weight:600; color:#34d399;">Fix Count</span><span style="font-size:0.77rem; color:rgba(255,255,255,0.45); margin-left:8px;">iterations to reach functional code · 0 = first-attempt</span></div>
              </div>
              <div style="background:rgba(255,255,255,0.05); border-radius:6px; padding:10px 13px; display:flex; align-items:center; gap:10px;">
                <div style="width:8px; height:8px; background:#34d399; border-radius:50%; flex-shrink:0;"></div>
                <div><span style="font-size:0.83rem; font-weight:600; color:#34d399;">Execution Time</span><span style="font-size:0.77rem; color:rgba(255,255,255,0.45); margin-left:8px;">mean over 5 Databricks serverless runs</span></div>
              </div>
              <div style="background:rgba(52,211,153,0.09); border:1px solid rgba(52,211,153,0.2); border-radius:6px; padding:10px 13px; display:flex; align-items:center; gap:10px;">
                <div style="width:8px; height:8px; background:#34d399; border-radius:50%; flex-shrink:0;"></div>
                <div><span style="font-size:0.83rem; font-weight:700; color:#34d399;">C&amp;S Score ★</span><span style="font-size:0.77rem; color:rgba(255,255,255,0.55); margin-left:8px;">correctness × architectural soundness · primary metric</span></div>
              </div>
              <div style="background:rgba(255,255,255,0.05); border-radius:6px; padding:10px 13px; display:flex; align-items:center; gap:10px;">
                <div style="width:8px; height:8px; background:#34d399; border-radius:50%; flex-shrink:0;"></div>
                <div><span style="font-size:0.83rem; font-weight:600; color:#34d399;">Pylint / PEP8</span><span style="font-size:0.77rem; color:rgba(255,255,255,0.45); margin-left:8px;">static code quality 0–10</span></div>
              </div>
              <div style="background:rgba(255,255,255,0.05); border-radius:6px; padding:10px 13px; display:flex; align-items:center; gap:10px;">
                <div style="width:8px; height:8px; background:#34d399; border-radius:50%; flex-shrink:0;"></div>
                <div><span style="font-size:0.83rem; font-weight:600; color:#34d399;">Action Correctness</span><span style="font-size:0.77rem; color:rgba(255,255,255,0.45); margin-left:8px;">5 expert engineers · per-checklist verdict</span></div>
              </div>
            </div>
            <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:7px;">
              <div class="stat-card"><div class="stat-num" style="color:#34d399; font-size:1.4rem;">7</div><div class="stat-label">models tested</div></div>
              <div class="stat-card"><div class="stat-num" style="color:#34d399; font-size:1.4rem;">3</div><div class="stat-label">pipelines</div></div>
              <div class="stat-card"><div class="stat-num" style="color:#34d399; font-size:1.4rem;">5</div><div class="stat-label">expert reviewers</div></div>
              <div class="stat-card"><div class="stat-num" style="color:#34d399; font-size:1.4rem;">Open</div><div class="stat-label">source</div></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S14: LLM RESULTS ═══ -->
    <div class="slide" id="slide-14">
      <div style="max-width:1100px; width:100%;">
        <div class="slide-label" style="color:#34d399;">LLM Benchmarking — 2/3 &nbsp;·&nbsp; Results</div>
        <h2 class="slide-title" style="font-size:1.75rem; margin-bottom:14px;">Fix Counts Across All 3 Pipelines</h2>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; align-items:start;">
          <div>
            <p style="font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:#3b82f6; margin-bottom:8px;">P1 · Basic</p>
            <table class="mini-table" style="border-radius:7px; overflow:hidden;">
              <thead><tr style="background:rgba(59,130,246,0.15);"><th>Model</th><th style="text-align:center;">Fixes</th><th style="text-align:center;">C&amp;S</th></tr></thead>
              <tbody>
                <tr><td style="font-size:0.8rem;">GPT-5 Nano</td><td style="text-align:center; color:#22c55e; font-weight:700;">0</td><td style="text-align:center;"><span style="background:#22c55e; color:white; padding:1px 6px; border-radius:3px; font-size:0.75rem; font-weight:700;">5</span></td></tr>
                <tr><td style="font-size:0.8rem;">Claude 3.5 Haiku</td><td style="text-align:center; color:#22c55e; font-weight:700;">0</td><td style="text-align:center;"><span style="background:#22c55e; color:white; padding:1px 6px; border-radius:3px; font-size:0.75rem; font-weight:700;">5</span></td></tr>
                <tr><td style="font-size:0.8rem;">Claude 4 Sonnet</td><td style="text-align:center; color:#22c55e; font-weight:700;">0</td><td style="text-align:center;"><span style="background:#86efac; color:#166534; padding:1px 6px; border-radius:3px; font-size:0.75rem; font-weight:700;">4</span></td></tr>
                <tr><td style="font-size:0.8rem;">GPT-5 Mini</td><td style="text-align:center; color:#22c55e; font-weight:700;">0</td><td style="text-align:center;"><span style="background:#86efac; color:#166534; padding:1px 6px; border-radius:3px; font-size:0.75rem; font-weight:700;">4</span></td></tr>
                <tr><td style="font-size:0.8rem;">Qwen3-235B</td><td style="text-align:center;">1</td><td style="text-align:center;"><span style="background:#fbbf24; color:white; padding:1px 6px; border-radius:3px; font-size:0.75rem; font-weight:700;">3</span></td></tr>
                <tr><td style="font-size:0.8rem;">Claude 4 Opus</td><td style="text-align:center;">1</td><td style="text-align:center;"><span style="background:#fbbf24; color:white; padding:1px 6px; border-radius:3px; font-size:0.75rem; font-weight:700;">3</span></td></tr>
                <tr><td style="font-size:0.8rem;">GPT-5</td><td style="text-align:center; color:#f59e0b; font-weight:700;">4</td><td style="text-align:center;"><span style="background:#fbbf24; color:white; padding:1px 6px; border-radius:3px; font-size:0.75rem; font-weight:700;">3</span></td></tr>
              </tbody>
            </table>
            <div style="background:rgba(59,130,246,0.07); border-radius:6px; padding:8px 11px; margin-top:8px; font-size:0.76rem; color:rgba(255,255,255,0.55);">Even lightweight models handle basic tasks reliably</div>
          </div>
          <div>
            <p style="font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:#8b5cf6; margin-bottom:8px;">P2 · Medium</p>
            <table class="mini-table" style="border-radius:7px; overflow:hidden;">
              <thead><tr style="background:rgba(139,92,246,0.15);"><th>Model</th><th style="text-align:center;">Fixes</th><th style="text-align:left; font-size:0.73rem;">Note</th></tr></thead>
              <tbody>
                <tr><td style="font-size:0.8rem;">Claude 4 Opus</td><td style="text-align:center; color:#22c55e; font-weight:700;">0</td><td style="font-size:0.73rem; color:rgba(255,255,255,0.4);">Most consistent</td></tr>
                <tr><td style="font-size:0.8rem;">GPT-5 Mini</td><td style="text-align:center; color:#22c55e; font-weight:700;">0</td><td style="font-size:0.73rem; color:rgba(255,255,255,0.4);">Correct partition</td></tr>
                <tr><td style="font-size:0.8rem;">Claude 3.5 Haiku</td><td style="text-align:center;">1</td><td style="font-size:0.73rem; color:rgba(255,255,255,0.4);">Date format fix</td></tr>
                <tr><td style="font-size:0.8rem;">GPT-5 Nano</td><td style="text-align:center;">1</td><td style="font-size:0.73rem; color:rgba(255,255,255,0.4);">Timezone fix</td></tr>
                <tr><td style="font-size:0.8rem;">Qwen3-235B</td><td style="text-align:center;">1</td><td style="font-size:0.73rem; color:rgba(255,255,255,0.4);">API parsing</td></tr>
                <tr><td style="font-size:0.8rem;">Claude 4 Sonnet</td><td style="text-align:center;">2</td><td style="font-size:0.73rem; color:rgba(255,255,255,0.4);">GroupBy issues</td></tr>
                <tr><td style="font-size:0.8rem;">GPT-5</td><td style="text-align:center;">2</td><td style="font-size:0.73rem; color:rgba(255,255,255,0.4);">Fastest when fixed</td></tr>
              </tbody>
            </table>
            <div style="background:rgba(139,92,246,0.07); border-radius:6px; padding:8px 11px; margin-top:8px; font-size:0.76rem; color:rgba(255,255,255,0.55);">Temporal logic introduces first real failures</div>
          </div>
          <div>
            <p style="font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:#ef4444; margin-bottom:8px;">P3 · High — the cliff</p>
            <table class="mini-table" style="border-radius:7px; overflow:hidden;">
              <thead><tr style="background:rgba(239,68,68,0.15);"><th>Model</th><th style="text-align:center;">Fixes</th><th style="text-align:left; font-size:0.73rem;">Verdict</th></tr></thead>
              <tbody>
                <tr><td style="font-size:0.8rem; color:#34d399;">Claude 4 Opus ★</td><td style="text-align:center; color:#22c55e; font-weight:700;">0</td><td style="font-size:0.73rem; color:#22c55e;">Fully Correct</td></tr>
                <tr><td style="font-size:0.8rem;">Claude 4 Sonnet</td><td style="text-align:center; color:#22c55e; font-weight:700;">0</td><td style="font-size:0.73rem; color:#22c55e;">Fully Correct</td></tr>
                <tr><td style="font-size:0.8rem;">GPT-5 Mini</td><td style="text-align:center; color:#22c55e; font-weight:700;">0</td><td style="font-size:0.73rem; color:#22c55e;">Fully Correct</td></tr>
                <tr><td style="font-size:0.8rem;">GPT-5</td><td style="text-align:center;">1</td><td style="font-size:0.73rem; color:#fbbf24;">Partial</td></tr>
                <tr><td style="font-size:0.8rem;">GPT-5 Nano</td><td style="text-align:center;">1</td><td style="font-size:0.73rem; color:#fbbf24;">Partial</td></tr>
                <tr><td style="font-size:0.8rem;">Qwen3-235B</td><td style="text-align:center;">2</td><td style="font-size:0.73rem; color:#fbbf24;">Partial</td></tr>
                <tr style="background:rgba(239,68,68,0.1);"><td style="font-size:0.8rem; color:#f87171;">Haiku 3.5 ⚠</td><td style="text-align:center; color:#ef4444; font-weight:800; font-size:1.05rem;">8</td><td style="font-size:0.73rem; color:#ef4444;">Incorrect</td></tr>
              </tbody>
            </table>
            <div style="background:rgba(239,68,68,0.08); border:1px solid rgba(239,68,68,0.2); border-radius:6px; padding:9px 12px; margin-top:8px;">
              <p style="font-size:0.78rem; color:rgba(255,200,200,0.85); margin:0;"><strong>Haiku 3.5:</strong> 0 → 1 → 8 as complexity grows.<br>Reliable for simple tasks; fails at multi-source join.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S15: LLM FINDINGS ═══ -->
    <div class="slide" id="slide-15">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#34d399;">LLM Benchmarking — 3/3 &nbsp;·&nbsp; Key Findings</div>
        <h2 class="slide-title" style="font-size:1.85rem; margin-bottom:18px;">Findings &amp; Practitioner Guidance</h2>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; align-items:start;">
          <div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              <div style="background:rgba(52,211,153,0.07); border-left:2px solid #34d399; border-radius:5px; padding:10px 13px;"><strong style="font-size:0.85rem; color:#34d399;">Claude Opus 4 — most reliable</strong><p style="font-size:0.79rem; color:rgba(255,255,255,0.6); margin-top:4px;">0–1 fixes across all pipelines · Fully Correct on P3</p></div>
              <div style="background:rgba(52,211,153,0.07); border-left:2px solid #34d399; border-radius:5px; padding:10px 13px;"><strong style="font-size:0.85rem; color:#34d399;">GPT-5 Mini — best all-rounder</strong><p style="font-size:0.79rem; color:rgba(255,255,255,0.6); margin-top:4px;">0 fixes on all 3 scenarios · strong correctness + efficiency</p></div>
              <div style="background:rgba(52,211,153,0.07); border-left:2px solid #34d399; border-radius:5px; padding:10px 13px;"><strong style="font-size:0.85rem; color:#34d399;">GPT-5 — optimization leader</strong><p style="font-size:0.79rem; color:rgba(255,255,255,0.6); margin-top:4px;">Best runtime (3–9s) when corrected · worth iteration budget</p></div>
              <div style="background:rgba(239,68,68,0.07); border-left:2px solid #ef4444; border-radius:5px; padding:10px 13px;"><strong style="font-size:0.85rem; color:#f87171;">Complexity cliff is real</strong><p style="font-size:0.79rem; color:rgba(255,255,255,0.6); margin-top:4px;">Lightweight models hit hard ceilings at multi-source tasks</p></div>
              <div style="background:rgba(239,68,68,0.07); border-left:2px solid #ef4444; border-radius:5px; padding:10px 13px;"><strong style="font-size:0.85rem; color:#f87171;">Failures: semantics, not routing</strong><p style="font-size:0.79rem; color:rgba(255,255,255,0.6); margin-top:4px;">Type casting · aggregation logic · null handling — not API calls</p></div>
              <div style="background:rgba(255,215,0,0.06); border-left:2px solid #ffd700; border-radius:5px; padding:10px 13px;"><strong style="font-size:0.85rem; color:#ffd700;">LLMs = accelerator, not replacement</strong><p style="font-size:0.79rem; color:rgba(255,255,255,0.6); margin-top:4px;">Pattern conformance and architectural decisions still require human expertise</p></div>
            </div>
          </div>
          <div>
            <!-- 📷 IMAGE: Figure from thesis showing LLM results chart or the complexity cliff visualization -->
            <div style="background:rgba(52,211,153,0.05); border:2px dashed rgba(52,211,153,0.22); border-radius:10px; height:240px; display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:14px;">
              <span style="font-size:2.2rem; margin-bottom:10px;">📷</span>
              <span style="font-size:0.82rem; color:rgba(255,255,255,0.35); text-align:center; padding:0 24px;">Thesis figure: LLM results chart<br>(fix count by model and pipeline,<br>or complexity cliff visualization)</span>
              <code style="font-size:0.65rem; color:rgba(52,211,153,0.4); margin-top:8px;">resources/img/llm-results.png</code>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:7px;">
              <div style="background:rgba(255,255,255,0.04); border-radius:7px; padding:11px; text-align:center;">
                <div style="font-size:0.72rem; font-weight:700; color:rgba(255,255,255,0.3); text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;">Best for correctness</div>
                <div style="font-size:0.9rem; font-weight:700; color:#34d399;">Opus 4 · GPT-5 Mini</div>
              </div>
              <div style="background:rgba(255,255,255,0.04); border-radius:7px; padding:11px; text-align:center;">
                <div style="font-size:0.72rem; font-weight:700; color:rgba(255,255,255,0.3); text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;">Best for speed</div>
                <div style="font-size:0.9rem; font-weight:700; color:#34d399;">GPT-5 · Haiku (basic)</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S16: EXPERT SURVEY ═══ -->
    <div class="slide" id="slide-16">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#fbbf24;">Evaluation — N=21 Expert Survey</div>
        <h2 class="slide-title" style="font-size:1.85rem; margin-bottom:18px;">Industry Validation — N=21 Practitioners</h2>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; align-items:start;">
          <div>
            <div style="background:rgba(255,255,255,0.04); border-radius:9px; padding:14px 17px; margin-bottom:14px;">
              <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:#fbbf24; margin-bottom:10px;">Participant Profile</p>
              <ul style="list-style:none; font-size:0.85rem; color:rgba(255,255,255,0.65); line-height:1.8;">
                <li>▸ Senior Data Engineers · Data Architects · Platform Engineers</li>
                <li>▸ 7+ years average experience in data engineering</li>
                <li>▸ 100+ source pipelines managed per respondent</li>
                <li>▸ Platforms: Azure · GCP · Databricks · AWS</li>
              </ul>
            </div>
            <div style="background:rgba(251,191,36,0.07); border-left:3px solid #fbbf24; border-radius:7px; padding:12px 15px; margin-bottom:10px;">
              <p style="font-size:0.83rem; color:rgba(255,255,255,0.75); line-height:1.6; font-style:italic;">"Configuration management consumes 10–40% of my team's time. A formalized pattern would be immediately adopted."</p>
              <p style="font-size:0.7rem; color:rgba(255,255,255,0.3); margin-top:5px;">— Senior Data Architect</p>
            </div>
            <div style="background:rgba(251,191,36,0.07); border-left:3px solid #fbbf24; border-radius:7px; padding:12px 15px;">
              <p style="font-size:0.83rem; color:rgba(255,255,255,0.75); line-height:1.6; font-style:italic;">"We've done ETLT-like flows for years without knowing it had a name. A formal decision framework changes how I onboard engineers."</p>
              <p style="font-size:0.7rem; color:rgba(255,255,255,0.3); margin-top:5px;">— Principal Engineer</p>
            </div>
          </div>
          <div>
            <p style="font-size:0.68rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:rgba(255,255,255,0.28); margin-bottom:10px;">Utility Score per Pattern (1–5)</p>
            <div style="display:flex; flex-direction:column; gap:11px; margin-bottom:16px;">
              <div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:5px;"><span style="font-size:0.85rem; font-weight:600; color:#60a5fa;">MIND</span><span style="font-size:0.95rem; font-weight:800; color:#fbbf24;">4.7/5</span></div>
                <div style="background:rgba(255,255,255,0.07); border-radius:4px; height:20px; overflow:hidden;"><div style="width:94%; background:linear-gradient(90deg,#60a5fa,#2196f3); height:100%; border-radius:4px;"></div></div>
                <div style="font-size:0.72rem; color:rgba(255,255,255,0.35); margin-top:4px;">76% recognition · 67% adoption intent</div>
              </div>
              <div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:5px;"><span style="font-size:0.85rem; font-weight:600; color:#c084fc;">ETLT++ / ELTL++</span><span style="font-size:0.95rem; font-weight:800; color:#fbbf24;">4.4/5</span></div>
                <div style="background:rgba(255,255,255,0.07); border-radius:4px; height:20px; overflow:hidden;"><div style="width:88%; background:linear-gradient(90deg,#c084fc,#9c27b0); height:100%; border-radius:4px;"></div></div>
                <div style="font-size:0.72rem; color:rgba(255,255,255,0.35); margin-top:4px;">80% recognition · 100% already use hybrid form</div>
              </div>
              <div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:5px;"><span style="font-size:0.85rem; font-weight:600; color:#a78bfa;">EADF</span><span style="font-size:0.95rem; font-weight:800; color:#fbbf24;">4.2/5</span></div>
                <div style="background:rgba(255,255,255,0.07); border-radius:4px; height:20px; overflow:hidden;"><div style="width:84%; background:linear-gradient(90deg,#a78bfa,#673ab7); height:100%; border-radius:4px;"></div></div>
                <div style="font-size:0.72rem; color:rgba(255,255,255,0.35); margin-top:4px;">62% recognition · 60% adoption intent</div>
              </div>
            </div>
            <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:7px;">
              <div class="stat-card" style="border-color:rgba(251,191,36,0.2);"><div class="stat-num" style="color:#fbbf24;">4.6/5</div><div class="stat-label">avg utility</div></div>
              <div class="stat-card" style="border-color:rgba(251,191,36,0.2);"><div class="stat-num" style="color:#fbbf24;">60–80%</div><div class="stat-label">recognition</div></div>
              <div class="stat-card" style="border-color:rgba(251,191,36,0.2);"><div class="stat-num" style="color:#fbbf24;">21</div><div class="stat-label">practitioners</div></div>
              <div class="stat-card" style="border-color:rgba(251,191,36,0.2);"><div class="stat-num" style="color:#fbbf24;">60–70%</div><div class="stat-label">adoption intent</div></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══ S17: CONTRIBUTIONS ═══ -->
    <div class="slide" id="slide-17">
      <div style="max-width:1060px; width:100%;">
        <div class="slide-label" style="color:#34d399;">Research Contributions</div>
        <h2 class="slide-title" style="font-size:1.85rem; margin-bottom:16px;">Six Research Contributions</h2>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; margin-bottom:14px;">
          <div style="background:rgba(52,211,153,0.06); border-left:3px solid #34d399; border-radius:7px; padding:12px 14px;">
            <p style="font-size:0.82rem; font-weight:700; color:#34d399; margin-bottom:5px;">C1 — POSA-Formalized DEDPs</p>
            <p style="font-size:0.78rem; color:rgba(255,255,255,0.58); line-height:1.5;">MIND · ETLT++ · ELTL++ · EADF — cloud-agnostic, technology-independent, first in the POSA/GoF sense for data engineering.</p>
          </div>
          <div style="background:rgba(52,211,153,0.06); border-left:3px solid #34d399; border-radius:7px; padding:12px 14px;">
            <p style="font-size:0.82rem; font-weight:700; color:#34d399; margin-bottom:5px;">C2 — Forces &amp; Consequences</p>
            <p style="font-size:0.78rem; color:rgba(255,255,255,0.58); line-height:1.5;">First formal trade-off space for data engineering design decisions. Structured criteria — not just tool recommendations.</p>
          </div>
          <div style="background:rgba(52,211,153,0.06); border-left:3px solid #34d399; border-radius:7px; padding:12px 14px;">
            <p style="font-size:0.82rem; font-weight:700; color:#34d399; margin-bottom:5px;">C3 — DSR Multi-Method Validation</p>
            <p style="font-size:0.78rem; color:rgba(255,255,255,0.58); line-height:1.5;">165-source SLR + 3 live deployments (Azure · GCP · Databricks) + N=21 expert survey. Quantified, not theoretical.</p>
          </div>
          <div style="background:rgba(52,211,153,0.06); border-left:3px solid #34d399; border-radius:7px; padding:12px 14px;">
            <p style="font-size:0.82rem; font-weight:700; color:#34d399; margin-bottom:5px;">C4 — First LLM Benchmark for DEDPs</p>
            <p style="font-size:0.78rem; color:rgba(255,255,255,0.58); line-height:1.5;">7 models × 3 pipelines × 5 runs. Novel C&amp;S Score metric. Expert action correctness panel. Open-source &amp; reproducible.</p>
          </div>
          <div style="background:rgba(52,211,153,0.06); border-left:3px solid #34d399; border-radius:7px; padding:12px 14px;">
            <p style="font-size:0.82rem; font-weight:700; color:#34d399; margin-bottom:5px;">C5 — Quantified Production Impact</p>
            <p style="font-size:0.78rem; color:rgba(255,255,255,0.58); line-height:1.5;">4.3× speedup · 69% TCO ↓ · 61% config ↓ · 0 drift events · 4.6/5 utility — all from live production systems.</p>
          </div>
          <div style="background:rgba(52,211,153,0.08); border-left:3px solid #ffd700; border-radius:7px; padding:12px 14px; border-color:rgba(255,215,0,0.2);">
            <p style="font-size:0.82rem; font-weight:700; color:#ffd700; margin-bottom:5px;">C6 — Practitioner Blog &amp; Website</p>
            <p style="font-size:0.78rem; color:rgba(255,255,255,0.58); line-height:1.5;">Open pattern website for data engineers. POSA framework, SoA comparison, implementation guides. Community-facing dissemination beyond academia.</p>
            <a href="index.html" style="display:inline-block; margin-top:6px; font-size:0.74rem; color:#ffd700; text-decoration:none; opacity:0.8;">datalab-unisalento.github.io →</a>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(6,1fr); gap:8px;">
          <div class="stat-card"><div class="stat-num" style="color:#34d399; font-size:1.4rem;">4.3×</div><div class="stat-label">MIND speedup</div></div>
          <div class="stat-card"><div class="stat-num" style="color:#34d399; font-size:1.4rem;">3.3×</div><div class="stat-label">ETLT++ throughput</div></div>
          <div class="stat-card"><div class="stat-num" style="color:#34d399; font-size:1.4rem;">69%</div><div class="stat-label">TCO reduction</div></div>
          <div class="stat-card"><div class="stat-num" style="color:#34d399; font-size:1.4rem;">61%</div><div class="stat-label">EADF config ↓</div></div>
          <div class="stat-card"><div class="stat-num" style="color:#34d399; font-size:1.4rem;">0</div><div class="stat-label">drift events</div></div>
          <div class="stat-card"><div class="stat-num" style="color:#34d399; font-size:1.4rem;">4.6/5</div><div class="stat-label">expert utility</div></div>
        </div>
      </div>
    </div>

    <!-- ═══ S18: CONCLUSIONS ═══ -->
    <div class="slide" id="slide-18">
      <div style="max-width:980px; width:100%; text-align:center;">
        <div class="slide-label" style="color:rgba(255,255,255,0.35); text-align:center;">Conclusions &amp; Future Work</div>
        <h2 style="font-size:2.1rem; font-weight:900; line-height:1.2; margin-bottom:8px;">Patterns work. Formalism pays off.</h2>
        <p style="font-size:0.9rem; color:rgba(255,255,255,0.38); margin-bottom:20px;">Reusable abstractions reduce cognitive load, accelerate delivery, and survive technology churn.</p>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:11px; margin-bottom:18px; text-align:left;">
          <div style="background:rgba(255,255,255,0.04); border-radius:9px; padding:16px;">
            <p style="font-size:0.68rem; font-weight:700; color:rgba(255,255,255,0.32); text-transform:uppercase; letter-spacing:1.5px; margin-bottom:10px;">Proven Results</p>
            <ul style="list-style:none; font-size:0.85rem; color:rgba(255,255,255,0.72); line-height:1.85;">
              <li>✓ 4.3× ingestion speedup (MIND)</li>
              <li>✓ 3.3× throughput; 69% TCO ↓</li>
              <li>✓ 61% config reduction (EADF)</li>
              <li>✓ 0 drift events post-adoption</li>
              <li>✓ 4.6/5 utility (N=21)</li>
            </ul>
          </div>
          <div style="background:rgba(255,255,255,0.04); border-radius:9px; padding:16px;">
            <p style="font-size:0.68rem; font-weight:700; color:rgba(255,255,255,0.32); text-transform:uppercase; letter-spacing:1.5px; margin-bottom:10px;">LLM Takeaways</p>
            <ul style="list-style:none; font-size:0.85rem; color:rgba(255,255,255,0.72); line-height:1.85;">
              <li>✓ Opus 4 / GPT-5 Mini most reliable</li>
              <li>✓ Complexity cliff at multi-source</li>
              <li>✓ Failures: semantics, not routing</li>
              <li>✓ LLMs = accelerator, not replacement</li>
            </ul>
          </div>
          <div style="background:rgba(255,255,255,0.04); border-radius:9px; padding:16px;">
            <p style="font-size:0.68rem; font-weight:700; color:rgba(255,255,255,0.32); text-transform:uppercase; letter-spacing:1.5px; margin-bottom:10px;">Future Work</p>
            <ul style="list-style:none; font-size:0.85rem; color:rgba(255,255,255,0.72); line-height:1.85;">
              <li>→ Pattern catalog expansion</li>
              <li>→ LLM + pattern-guided generation</li>
              <li>→ Streaming / real-time variants</li>
              <li>→ Regulated industry adaptations</li>
              <li>→ Automated YAML descriptor gen.</li>
            </ul>
          </div>
        </div>
        <div style="display:flex; justify-content:center; gap:9px; flex-wrap:wrap; margin-bottom:14px;">
          <a href="mind.html" style="text-decoration:none;"><div style="background:rgba(33,150,243,0.12); border:1px solid rgba(33,150,243,0.28); border-radius:7px; padding:8px 16px; font-size:0.82rem; color:#60a5fa; font-weight:600;">MIND →</div></a>
          <a href="etlt.html" style="text-decoration:none;"><div style="background:rgba(156,39,176,0.12); border:1px solid rgba(156,39,176,0.28); border-radius:7px; padding:8px 16px; font-size:0.82rem; color:#c084fc; font-weight:600;">ETLT / ELTL →</div></a>
          <a href="eadf.html" style="text-decoration:none;"><div style="background:rgba(103,58,183,0.12); border:1px solid rgba(103,58,183,0.28); border-radius:7px; padding:8px 16px; font-size:0.82rem; color:#a78bfa; font-weight:600;">EADF →</div></a>
          <a href="llm.html" style="text-decoration:none;"><div style="background:rgba(52,211,153,0.08); border:1px solid rgba(52,211,153,0.22); border-radius:7px; padding:8px 16px; font-size:0.82rem; color:#34d399; font-weight:600;">LLM Study →</div></a>
          <a href="index.html" style="text-decoration:none;"><div style="background:rgba(255,215,0,0.08); border:1px solid rgba(255,215,0,0.25); border-radius:7px; padding:8px 16px; font-size:0.82rem; color:#ffd700; font-weight:600;">Pattern Website →</div></a>
        </div>
        <p style="font-size:0.72rem; color:rgba(255,255,255,0.2);">Chiara Rucco · University of Salento / DataLab · XXXVII Cycle · 2025</p>
      </div>
    </div>

  </div><!-- /slides-container -->"""

content = re.sub(
    r'  <div id="slides-container">.*?  </div><!-- /slides-container -->',
    NEW_SLIDES,
    content, flags=re.DOTALL, count=1
)

# Update contributions label in title
content = content.replace('Five Research Contributions', 'Six Research Contributions', 1)

SRC.write_text(content, encoding='utf-8')
print(f"defense.html rebuilt: 18 slides")
print(f"File size: {SRC.stat().st_size:,} bytes")
