(() => {
  const $ = (id) => document.getElementById(id);

  function toast(msg) {
    const el = $("toast");
    el.textContent = msg;
    el.style.display = "block";
    setTimeout(() => { el.style.display = "none"; }, 3200);
  }

  function fmtSec(s) {
    if (s == null || Number.isNaN(s)) return "—";
    const n = Math.max(0, Math.floor(s));
    const h = Math.floor(n / 3600);
    const m = Math.floor((n % 3600) / 60);
    const sec = n % 60;
    if (h) return `${h}h ${m}m ${sec}s`;
    if (m) return `${m}m ${sec}s`;
    return `${sec}s`;
  }

  function fmtTs(ts) {
    if (!ts) return "—";
    const d = new Date(ts * 1000);
    return d.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" });
  }

  function setKV(el, pairs) {
    el.innerHTML = pairs
      .map(([k, v]) => `<span>${k}</span><span>${v == null || v === "" ? "—" : v}</span>`)
      .join("");
  }

  let lastProgress = null;

  function render(p) {
    lastProgress = p;
    const statusRaw = p.status || "STOPPED";
    const started = p.started_at;
    const hb = p.heartbeat_at;
    const nowSec = Date.now() / 1000;
    const stale = statusRaw === "RUNNING" && hb && (nowSec - hb > 45);
    const status = stale ? "STOPPED" : statusRaw;
    const pill = $("status-pill");
    pill.textContent = stale ? "STOPPED (stale)" : status;
    pill.className = "status-pill " + (stale ? "STOPPED" : status);

    // Prefer live clock from started_at so elapsed moves even between polls.
    let elapsed = p.elapsed_sec;
    let remaining = p.wall_remaining_sec;
    if (started && (statusRaw === "RUNNING" || statusRaw === "PAUSED" || statusRaw === "CHECKPOINTING") && !stale) {
      elapsed = Math.max(0, nowSec - started);
      if (p.wall_hours) remaining = Math.max(0, p.wall_hours * 3600 - elapsed);
    }

    setKV($("status-kv"), [
      ["PID", p.pid],
      ["Elapsed", fmtSec(elapsed)],
      ["Wall remaining", fmtSec(remaining)],
      ["Heartbeat", fmtTs(hb) + (stale ? " (stale — process likely dead)" : "")],
      ["Git commit", p.git_commit],
      ["Config hash", p.configuration_hash],
      ["Offline", p.offline ? "yes" : "no"],
      ["Run ID", p.run_id],
    ]);

    const fr = p.certified_frontier || {};
    const degrees = fr.degrees || {};
    const order = ["2", "4", "6", "8"];
    const frontierPairs = [];
    frontierPairs.push(["Spacetime case", fr.spacetime_case || "6D (3-form)"]);
    for (const d of order) {
      const info = degrees[d] || {};
      const st = info.status || "unknown";
      const count = info.graph_count != null ? ` · ${info.graph_count} graphs` : "";
      frontierPairs.push([info.label || `Degree ${d}`, `${st}${count}`]);
    }
    frontierPairs.push(["Largest certified degree", fr.largest_certified_degree]);
    frontierPairs.push(["10D status", (fr.spacetime_10d && fr.spacetime_10d.status) || fr.next_spacetime_case || "deferred"]);
    setKV($("frontier-kv"), frontierPairs);
    $("frontier-scope").textContent =
      "Scope: " + (fr.scope || p.scope || "connected metric-contraction graphs only") +
      " · Degrees = contraction order N, not spacetime dimension.";
    const certifiedList = order
      .filter((d) => (degrees[d] || {}).status === "certified")
      .map((d) => {
        const c = degrees[d].graph_count;
        return c != null ? `degree ${d} (${c} graphs)` : `degree ${d}`;
      });
    $("frontier-beginner").textContent = certifiedList.length
      ? `Certified on the 6D problem so far: ${certifiedList.join(", ")}. ` +
        `Next focus is finishing degree-8 work before the separate 10D climb.`
      : "No degrees certified yet.";

    // Optional per-degree notes in technical mode
    const notes = order
      .map((d) => {
        const info = degrees[d] || {};
        return info.note ? `N=${d}: ${info.note}` : null;
      })
      .filter(Boolean);
    const noteEl = $("frontier-notes");
    if (noteEl) noteEl.textContent = notes.join("\n") || "—";

    $("task-beginner").textContent = p.current_task_beginner || p.current_task || "Waiting…";
    $("task-technical").textContent = p.current_task || "—";

    const g = p.graph_enumeration || {};
    setKV($("graphs-kv"), [
      ["Total raw", g.total_raw],
      ["Connected", g.connected],
      ["Canonical non-isomorphic", g.canonical_nonisomorphic],
      ["Completed shards", g.completed_shards],
      ["Pending shards", g.pending_shards],
      ["Rate / sec", g.rate_per_sec],
    ]);
    $("graphs-beginner").textContent =
      g.canonical_nonisomorphic != null && g.canonical_nonisomorphic > 0
        ? `The computer generated ${g.canonical_nonisomorphic} different legal contraction patterns` +
          (g.connected ? ` (${g.connected} connected before de-duplication).` : ".")
        : "Graph listing has not started yet.";
    $("graphs-ids").textContent = (g.canonical_ids || []).join("\n") || "—";

    const cls = p.invariant_classification || {};
    const keys = Object.keys(cls).sort((a, b) => Number(a) - Number(b));
    if (!keys.length) {
      $("class-beginner").textContent = "Classification results will appear as each degree is checked.";
      $("class-technical").textContent = "—";
    } else {
      const last = cls[keys[keys.length - 1]] || {};
      const n = last.basis_graph_ids ? last.basis_graph_ids.length : 0;
      $("class-beginner").textContent =
        `Those patterns currently contribute ${n || "unknown"} basis graph ID(s) at the latest degree. ` +
        "The program checks independence with numerical and (when available) modular arithmetic.";
      $("class-technical").textContent = JSON.stringify(cls, null, 2);
    }

    const gens = p.generators || [];
    $("gen-beginner").textContent = gens.length
      ? `There are ${gens.length} accepted generator(s) so far.`
      : "No generators have been certified in this run yet.";
    $("gen-technical").textContent = JSON.stringify(gens, null, 2);

    const rel = p.relations || {};
    setKV($("rel-kv"), [
      ["Discovered", rel.discovered],
      ["Numerically supported", rel.numerically_supported],
      ["Modularly verified", rel.modularly_verified],
      ["Exactly reconstructed", rel.exactly_reconstructed],
    ]);
    $("rel-technical").textContent = JSON.stringify(
      { formulas: rel.formulas || [], residuals: rel.residuals || [] },
      null,
      2
    );

    const c = p.compute || {};
    setKV($("compute-kv"), [
      ["CPU %", c.cpu_percent],
      ["Workers", c.workers],
      ["Physical RAM (GiB)", c.physical_ram_gb],
      ["RAM used (GiB)", c.ram_used_gb],
      ["RAM ceiling (GiB)", c.ram_ceiling_gb],
      ["Disk free (GiB)", c.disk_free_gb],
      ["Cache (MiB)", c.cache_size_mb],
      ["Thermal", c.thermal ? "available" : "unavailable"],
    ]);
    const proj = c.projected_completion || {};
    $("compute-eta").textContent =
      `Projected completion: ${proj.eta_sec != null ? fmtSec(proj.eta_sec) : "—"} ` +
      `(${proj.uncertainty || "uncertainty not stated"})`;

    const v = p.validation || {};
    setKV($("val-kv"), [
      ["Suite", v.status],
      ["Last regression", fmtTs(v.last_regression_at)],
      ["Hodge agreement", v.hodge_agreement],
      ["Graph-generator agreement", v.graph_generator_agreement],
      ["Evaluator agreement", v.evaluator_agreement],
      ["Seed stability", v.seed_stability],
      ["Prime stability", v.prime_stability],
    ]);
    $("val-warnings").textContent = (v.warnings || []).join("\n") || "No unresolved warnings.";

    const act = p.activity || [];
    $("activity").innerHTML = act
      .map((a) => {
        const t = fmtTs(a.ts);
        return `<div><span class="badge">${a.type || ""}</span>${t} ${a.message || ""}</div>`;
      })
      .join("") || "<div>No events yet.</div>";
  }

  async function poll() {
    try {
      const res = await fetch("/api/progress");
      const data = await res.json();
      render(data);
    } catch (e) {
      toast("Progress poll failed (is the dashboard server running?)");
    }
  }

  function useSSE() {
    if (!window.EventSource) {
      setInterval(poll, 1500);
      return;
    }
    const es = new EventSource("/api/stream");
    es.addEventListener("progress", (ev) => {
      try { render(JSON.parse(ev.data)); } catch (_) {}
    });
    es.onerror = () => {
      /* fall back to polling if SSE drops */
    };
    setInterval(poll, 2000);
  }

  $("btn-beginner").onclick = () => {
    document.body.classList.remove("mode-technical");
    document.body.classList.add("mode-beginner");
    $("btn-beginner").classList.add("active");
    $("btn-technical").classList.remove("active");
  };
  $("btn-technical").onclick = () => {
    document.body.classList.remove("mode-beginner");
    document.body.classList.add("mode-technical");
    $("btn-technical").classList.add("active");
    $("btn-beginner").classList.remove("active");
  };

  document.querySelectorAll(".controls [data-action]").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const action = btn.getAttribute("data-action");
      try {
        const res = await fetch("/api/control", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ action }),
        });
        const data = await res.json();
        if (!data.ok) toast(data.error || "Control failed");
        else toast(`Logged control: ${action}`);
        if (action === "open_report") {
          window.open("/api/progress", "_blank");
        }
      } catch (e) {
        toast("Control request failed");
      }
    });
  });

  poll();
  useSSE();
  setInterval(() => { if (lastProgress) render(lastProgress); }, 1000);
})();
