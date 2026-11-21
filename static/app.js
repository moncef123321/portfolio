// ===== Menu mobile =====
const menuToggle = document.getElementById("menuToggle");
const navLinks = document.getElementById("navLinks");

function setMenu(open) {
  navLinks.classList.toggle("open", open);
  menuToggle.setAttribute("aria-expanded", String(open));
  menuToggle.setAttribute("aria-label", open ? menuToggle.dataset.close : menuToggle.dataset.open);
  menuToggle.textContent = open ? "×" : "☰";
}

if (menuToggle && navLinks) {
  menuToggle.addEventListener("click", () => setMenu(!navLinks.classList.contains("open")));
  navLinks.querySelectorAll("a").forEach((l) => l.addEventListener("click", () => setMenu(false)));
}

// ===== Thème clair / sombre =====
const root = document.documentElement;
const themeToggle = document.getElementById("themeToggle");

if (themeToggle) {
  themeToggle.addEventListener("click", () => {
    const next = root.dataset.theme === "light" ? "dark" : "light";
    root.dataset.theme = next;
    try { localStorage.setItem("theme", next); } catch (e) {}
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.content = next === "light" ? "#f4f8fd" : "#07111f";
  });
}

// ===== Apparition au scroll =====
const targets = document.querySelectorAll(
  ".section-heading, .about-layout, .experience-card, .skill-card, .project-card, .simple-card, .cert-card, .language-card, .contact-section, .stats"
);
targets.forEach((el, i) => {
  el.classList.add("reveal");
  el.style.transitionDelay = `${(i % 4) * 70}ms`;
});

if ("IntersectionObserver" in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add("in");
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  targets.forEach((el) => io.observe(el));
} else {
  targets.forEach((el) => el.classList.add("in"));
}

// ===== Lien actif dans la navbar =====
const links = [...document.querySelectorAll(".nav-links a[href^='#']")];
const sections = links.map((l) => document.querySelector(l.getAttribute("href"))).filter(Boolean);

if ("IntersectionObserver" in window) {
  const spy = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        links.forEach((l) => l.classList.toggle("active", l.getAttribute("href") === "#" + e.target.id));
      }
    });
  }, { rootMargin: "-40% 0px -55% 0px" });
  sections.forEach((s) => spy.observe(s));
}

// ===== Barre de progression =====
const bar = document.getElementById("progress");
if (bar) {
  const update = () => {
    const h = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = h > 0 ? (window.scrollY / h) * 100 + "%" : "0";
  };
  window.addEventListener("scroll", update, { passive: true });
  update();
}

// ===== Démo ML =====
(function () {
  const best = document.getElementById("mlBest");
  const bars = document.getElementById("mlBars");
  const sliders = document.querySelectorAll("#mlSliders input[type=range]");
  if (!best || !bars || !sliders.length) return;
  let timer;
  async function predict() {
    const values = [...sliders].map((s) => parseFloat(s.value));
    try {
      const r = await fetch("/api/predict", {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ values }),
      });
      const d = await r.json();
      if (!r.ok) throw new Error(d.error);
      best.textContent = d.best;
      bars.innerHTML = d.classes.map((c) =>
        `<div class="ml-row"><span>${c.label}</span><div class="level"><i style="width:${c.p}%"></i></div><em>${c.p}%</em></div>`
      ).join("");
    } catch (e) { best.textContent = best.dataset.err || "—"; }
  }
  sliders.forEach((s) => s.addEventListener("input", () => {
    document.getElementById(s.id + "-v").textContent = s.value;
    clearTimeout(timer); timer = setTimeout(predict, 120);
  }));
  predict();
})();
