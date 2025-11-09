let gameData = null;

let state = {
  literacy: 0,
  scenesVisited: [],
  decisions: [] // {sceneTitle, choiceLabel, effectValue}
};

async function loadGameData() {
  const res = await fetch("/api/story");
  gameData = await res.json();
}

function applyEffects(effects) {
  if (!effects) return;
  if (typeof effects.literacy === "number") {
    state.literacy += effects.literacy;
    if (state.literacy < 0) state.literacy = 0;
    if (state.literacy > 100) state.literacy = 100;
  }
}

function estimateFutureValue(monthly, years, r = 0.07) {
  const n = years * 12;
  const i = r / 12;
  if (i === 0) return monthly * n;
  return monthly * ((Math.pow(1 + i, n) - 1) / i);
}

function getOutcomePreview(choice) {
  const label = choice.label.toLowerCase();

  if (label.includes("4%") && label.includes("match")) {
    const fv = estimateFutureValue(433, 10);
    return `Sticking with this in your 20s alone could grow to around $${Math.round(
      fv
    ).toLocaleString()} by age 32.`;
  }

  if (label.includes("roth ira")) {
    const fv = estimateFutureValue(100, 10);
    return `A $100/month Roth IRA for 10 years at 7% builds to about $${Math.round(
      fv
    ).toLocaleString()} — future gains are tax-free.`;
  }

  if (label.includes("skip retirement")) {
    return `Delaying investing through your 20s forces much bigger payments later just to catch up.`;
  }

  if (label.includes("target-date fund")) {
    return `A good target-date fund keeps you appropriately invested over time with minimal effort.`;
  }

  if (label.includes("age 45")) {
    return `This path shows the cost of inaction. In this simulation, you can rewind and test better choices.`;
  }

  return "";
}

function updateProgressBar() {
  const fill = document.querySelector(".progress-bar-fill");
  if (!fill) return;
  const pct = Math.max(5, Math.min(state.literacy, 100));
  fill.style.width = pct + "%";
}

function addToTimeline(sceneTitle, choiceLabel, effects) {
  const list = document.getElementById("timeline-list");
  if (!list) return;

  const effectValue = (effects && effects.literacy) || 0;
  let tagText = "Neutral impact";

  if (effectValue > 0) tagText = "Builds healthy habits";
  else if (effectValue < 0) tagText = "Potential long-term risk";

  const item = document.createElement("li");
  item.className = "timeline-item";

  const labelSpan = document.createElement("div");
  labelSpan.className = "timeline-label";
  labelSpan.textContent = `${sceneTitle}: ${choiceLabel}`;

  const tagSpan = document.createElement("div");
  tagSpan.className = "timeline-tag";
  tagSpan.textContent = tagText;

  item.appendChild(labelSpan);
  item.appendChild(tagSpan);
  list.appendChild(item);
}

function resetTimeline() {
  const list = document.getElementById("timeline-list");
  if (list) list.innerHTML = "";
}

function buildSummaryText() {
  const total = state.decisions.length;
  const positive = state.decisions.filter(d => d.effectValue > 0).length;
  const negative = state.decisions.filter(d => d.effectValue < 0).length;

  if (total === 0) {
    return "Make a few choices to see how your timeline evolves.";
  }

  let msg = `You made ${total} key decisions. `;
  msg += `${positive} reinforced strong long-term habits`;
  if (negative > 0) {
    msg += `, while ${negative} introduced potential risks that would require corrections later.`;
  } else {
    msg += ` and avoided major long-term risks.`;
  }

  msg += " Compare this run with another playthrough where you intentionally change one or two choices.";
  return msg;
}

function renderScene(sceneId, explanationText = "", outcomeText = "") {
  const scene = gameData.scenes[sceneId];
  if (!scene) {
    console.error("Missing scene:", sceneId);
    return;
  }

  state.scenesVisited.push(sceneId);

  const titleEl = document.getElementById("scene-title");
  const textEl = document.getElementById("scene-text");
  const questionEl = document.getElementById("scene-question");
  const choicesEl = document.getElementById("choices");
  const explanationEl = document.getElementById("explanation");
  const outcomeEl = document.getElementById("outcome-text");
  const literacyEl = document.getElementById("literacy-score");
  const chaptersCountEl = document.getElementById("chapters-count");

  titleEl.textContent = scene.title;
  textEl.textContent = scene.text;
  questionEl.textContent = scene.question || "";
  explanationEl.textContent = explanationText;
  outcomeEl.textContent = outcomeText;
  literacyEl.textContent = state.literacy;
  chaptersCountEl.textContent = state.scenesVisited.length;

  // If we're on the summary scene, auto-generate a reflective summary.
  if (sceneId === "scene_summary") {
    explanationEl.textContent = buildSummaryText();
    outcomeEl.textContent =
      "Run the story again with different decisions to see how small changes early on compound into different futures.";
  }

  updateProgressBar();

  // Render choices
  choicesEl.innerHTML = "";
  scene.choices.forEach((choice) => {
    const btn = document.createElement("button");
    btn.className = "choice-btn";

    const labelSpan = document.createElement("span");
    labelSpan.className = "choice-label";
    labelSpan.textContent = choice.label;

    const tagSpan = document.createElement("span");
    tagSpan.className = "choice-tag";

    const effectValue = (choice.effects && choice.effects.literacy) || 0;
    if (effectValue > 0) tagSpan.textContent = "Smart move";
    else if (effectValue < 0) tagSpan.textContent = "Risky path";
    else tagSpan.textContent = "Neutral";

    btn.appendChild(labelSpan);
    btn.appendChild(tagSpan);

    btn.onclick = () => {
      const lower = choice.label.toLowerCase();

      // Handle restart / replay choices: reset state cleanly
      if (lower.includes("restart") || lower.includes("replay from the start")) {
        state = { literacy: 0, scenesVisited: [], decisions: [] };
        resetTimeline();
      } else {
        applyEffects(choice.effects);

        // track decision in state for summary
        state.decisions.push({
          sceneTitle: scene.title,
          choiceLabel: choice.label,
          effectValue
        });

        // add to visible timeline
        addToTimeline(scene.title, choice.label, choice.effects);
      }

      const expl = choice.explanation
        ? "Why this matters: " + choice.explanation
        : "";
      const future = getOutcomePreview(choice);

      renderScene(choice.next, expl, future);
    };

    choicesEl.appendChild(btn);
  });
}

document.addEventListener("DOMContentLoaded", async () => {
  await loadGameData();

  state = {
    literacy: 0,
    scenesVisited: [],
    decisions: []
  };

  resetTimeline();
  renderScene(gameData.startScene);
});
