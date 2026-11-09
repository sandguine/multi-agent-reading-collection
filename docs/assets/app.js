(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const topics = [...document.querySelectorAll('.topic')];
  if (!topics.length) return;
  const readings = [...document.querySelectorAll('.reading')];
  const solutions = [...document.querySelectorAll('.solution')];
  const form = document.querySelector('.filters');
  const search = document.querySelector('#search');
  const priority = document.querySelector('#priority');
  const length = document.querySelector('#length');
  const count = document.querySelector('#result-count');
  const sectionButton = document.querySelector('#toggle-sections');
  const solutionButton = document.querySelector('#toggle-solutions');
  const contents = document.querySelector('.contents');
  if (window.matchMedia('(max-width: 740px)').matches) contents.open = false;
  const normalize = (s) => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  let beforeFilter = null;

  function labels() {
    const visible = topics.filter(t => !t.hidden);
    sectionButton.textContent = visible.length && visible.every(t => t.open) ? 'Collapse all collections' : 'Expand all collections';
    solutionButton.textContent = solutions.every(s => s.open) ? 'Hide all 8 solutions' : 'Show all 8 solutions';
  }
  function applyFilters() {
    const words = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
    const active = words.length > 0 || priority.value !== '0' || length.value !== '5';
    if (active && !beforeFilter) beforeFilter = topics.map(t => t.open);
    let shown = 0;
    for (const reading of readings) {
      const haystack = normalize(reading.dataset.search);
      reading.hidden = !(words.every(word => haystack.includes(word)) && Number(reading.dataset.importance) >= Number(priority.value) && Number(reading.dataset.length) <= Number(length.value));
      if (!reading.hidden) shown++;
    }
    document.querySelectorAll('.reading-group').forEach(group => {
      group.hidden = ![...group.querySelectorAll('.reading')].some(r => !r.hidden);
    });
    topics.forEach(topic => {
      topic.hidden = ![...topic.querySelectorAll('.reading')].some(r => !r.hidden);
      if (active && !topic.hidden) topic.open = true;
    });
    if (!active && beforeFilter) {
      topics.forEach((topic,i) => { topic.open = beforeFilter[i]; });
      beforeFilter = null;
    }
    document.body.classList.toggle('filtering', active);
    count.textContent = active ? `${shown} of 43 readings · filters applied` : '43 readings · all collections';
    document.querySelector('#no-results').hidden = shown !== 0;
    labels();
  }
  function resetFilters() {
    search.value = ''; priority.value = '0'; length.value = '5'; applyFilters();
  }
  function revealTarget() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = id && document.getElementById(id);
    if (!target) return;
    if (document.body.classList.contains('filtering')) resetFilters();
    let el = target;
    while (el && el !== document.body) {
      if (el.tagName === 'DETAILS') el.open = true;
      el = el.parentElement;
    }
    labels();
    requestAnimationFrame(() => target.scrollIntoView({block:'start'}));
  }
  form.addEventListener('input', applyFilters);
  form.addEventListener('change', applyFilters);
  form.addEventListener('reset', (event) => { event.preventDefault(); resetFilters(); });
  sectionButton.addEventListener('click', () => {
    const visible = topics.filter(t => !t.hidden);
    const expand = !visible.every(t => t.open);
    visible.forEach(t => { t.open = expand; }); labels();
  });
  solutionButton.addEventListener('click', () => {
    const show = !solutions.every(s => s.open);
    if (show) {
      if (document.body.classList.contains('filtering')) resetFilters();
      topics.filter(t => t.querySelector('.solution')).forEach(t => { t.open = true; });
    }
    solutions.forEach(s => { s.open = show; }); labels();
  });
  [...topics, ...solutions].forEach(d => d.addEventListener('toggle', labels));
  document.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener('click', () => {
    if (a.hash === location.hash) requestAnimationFrame(revealTarget);
  }));
  window.addEventListener('hashchange', revealTarget);
  let printState = null;
  window.addEventListener('beforeprint', () => {
    printState = [...topics,...solutions].map(t => t.open);
    [...topics,...solutions].forEach(t => { t.open = true; });
  });
  window.addEventListener('afterprint', () => {
    if (printState) [...topics,...solutions].forEach((t,i) => { t.open = printState[i]; });
    printState = null; labels();
  });
  document.querySelector('#print').addEventListener('click', () => window.print());
  const navLinks = [...document.querySelectorAll('.contents a')];
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      const entry = entries.find(entry => entry.isIntersecting);
      if (!entry) return;
      navLinks.forEach(a => a.classList.toggle('active', a.hash === `#${entry.target.id}`));
    },{rootMargin:'-10% 0px -75% 0px'});
    [...topics,document.querySelector('#closing')].forEach(t => observer.observe(t));
  }
  labels(); revealTarget();
})();
