const state = {
  reports: [],
  workflowUrl: document.body.dataset.workflowUrl,
  activeIndex: null,
  linkElements: [],
};

const elements = {
  links: document.querySelector('#reportLinks'),
  rerun: document.querySelector('#rerunLink'),
  newLink: document.querySelector('#newLink'),
  content: document.querySelector('#reportContent'),
  status: document.querySelector('#statusMessage'),
};

const LOCAL_TIME_OPTIONS = {
  year: 'numeric',
  month: 'short',
  day: 'numeric',
  hour: '2-digit',
  minute: '2-digit',
  second: '2-digit',
  timeZoneName: 'short',
};

function applyLocalTimes(root) {
  if (!root) return;
  const container = root instanceof Element ? root : document;
  const nodes = container.querySelectorAll('time.js-local-time');
  nodes.forEach((node) => {
    if (node.dataset.localized === 'true') {
      return;
    }
    const isoValue = node.getAttribute('datetime') || node.textContent;
    if (!isoValue) {
      return;
    }
    const date = new Date(isoValue);
    if (Number.isNaN(date.getTime())) {
      return;
    }
    node.textContent = date.toLocaleString(undefined, LOCAL_TIME_OPTIONS);
    node.dataset.localized = 'true';
  });
}

function formatDateLabel(isoDate) {
  if (!isoDate) return 'Unknown date';
  try {
    const date = new Date(isoDate);
    return date.toLocaleDateString(undefined, {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
    });
  } catch (error) {
    return isoDate;
  }
}

function buildActionUrl(ticker, force = false) {
  if (!state.workflowUrl) return '#';
  const url = new URL(state.workflowUrl, window.location.origin);
  if (!state.workflowUrl.startsWith('http')) {
    return '#';
  }
  url.searchParams.set('inputs[ticker]', ticker);
  if (force) {
    url.searchParams.set('inputs[force]', 'true');
  }
  return url.toString();
}

function updateButtons(report) {
  if (!report) {
    elements.rerun.setAttribute('aria-disabled', 'true');
    elements.rerun.dataset.disabled = 'true';
    elements.rerun.removeAttribute('href');
    elements.rerun.setAttribute('tabindex', '-1');
    delete elements.rerun.dataset.ticker;
    return;
  }
  elements.rerun.removeAttribute('aria-disabled');
  delete elements.rerun.dataset.disabled;
  elements.rerun.href = buildActionUrl(report.ticker, true);
  elements.rerun.removeAttribute('tabindex');
  elements.rerun.dataset.ticker = report.ticker;
}

function renderMarkdown(markdown) {
  if (window.marked && typeof window.marked.parse === 'function') {
    elements.content.innerHTML = window.marked.parse(markdown);
  } else {
    elements.content.textContent = markdown;
  }
  applyLocalTimes(elements.content);
}

function renderReport(report) {
  if (!report) {
    elements.content.innerHTML = '';
    elements.status.textContent = '';
    return;
  }
  elements.status.textContent = `${report.title} • ${formatDateLabel(report.date)}`;
  if (report.content_html) {
    elements.content.innerHTML = report.content_html;
  } else if (report.content_markdown) {
    renderMarkdown(report.content_markdown);
  } else if (report.content) {
    renderMarkdown(report.content);
  } else {
    elements.content.textContent = 'No report content available.';
  }
  applyLocalTimes(elements.content);
}

function clearSelection(preserveStatus = false) {
  state.activeIndex = null;
  state.linkElements.forEach((link) => delete link.dataset.active);
  updateButtons(null);
  if (!preserveStatus) {
    elements.status.textContent = '';
  }
  elements.content.innerHTML = '';
}

function showReport(index) {
  const report = state.reports[index];
  if (!report) {
    return;
  }
  state.activeIndex = index;
  try {
    window.sessionStorage.setItem('stonks-active-index', String(index));
  } catch (error) {
    console.warn('Unable to store active index', error);
  }
  state.linkElements.forEach((link, linkIndex) => {
    if (linkIndex === index) {
      link.dataset.active = 'true';
    } else {
      delete link.dataset.active;
    }
  });
  updateButtons(report);
  renderReport(report);
}

function populateLinks(reports) {
  elements.links.innerHTML = '';
  state.linkElements = [];
  reports.forEach((report, index) => {
    const link = document.createElement('a');
    link.href = '#';
    link.textContent = `[${report.ticker}]`;
    link.dataset.index = String(index);
    link.addEventListener('click', (event) => {
      event.preventDefault();
      showReport(index);
    });
    elements.links.appendChild(link);
    state.linkElements.push(link);
  });
}

async function loadReports() {
  try {
    elements.status.textContent = 'Loading reports...';
    const response = await fetch(`${window.__baseUrl || ''}/reports.json`);
    if (!response.ok) {
      throw new Error(`Failed to load reports.json (${response.status})`);
    }
    const data = await response.json();
    state.reports = Array.isArray(data) ? data : [];
    state.reports.sort((a, b) => a.ticker.localeCompare(b.ticker));
    populateLinks(state.reports);
    if (!state.reports.length) {
      elements.status.textContent = 'No reports have been generated yet.';
      clearSelection(true);
      return;
    }
    elements.status.textContent = '';
    const savedIndex = (() => {
      try {
        const raw = window.sessionStorage.getItem('stonks-active-index');
        const parsed = raw !== null ? Number(raw) : NaN;
        return Number.isFinite(parsed) ? parsed : null;
      } catch (error) {
        console.warn('Unable to read stored active index', error);
        return null;
      }
    })();

    if (savedIndex !== null && savedIndex >= 0 && savedIndex < state.reports.length) {
      showReport(savedIndex);
    } else {
      clearSelection();
    }
  } catch (error) {
    console.error(error);
    elements.status.textContent = 'Unable to load reports. Please try again later.';
  }
}

elements.rerun?.addEventListener('click', (event) => {
  const href = event.currentTarget.getAttribute('href');
  if (!href || href === '#') {
    event.preventDefault();
  }
});

elements.newLink?.addEventListener('click', (event) => {
  event.preventDefault();
  const ticker = window.prompt('Ticker symbol to analyze:');
  if (!ticker) {
    return;
  }
  const cleaned = ticker.trim().toUpperCase();
  if (!cleaned) {
    return;
  }
  const url = buildActionUrl(cleaned, false);
  if (url === '#') {
    alert('Workflow URL is not configured. Update _config.yml with your repository name.');
    return;
  }
  window.open(url, '_blank', 'noopener');
});

updateButtons(null);
loadReports();
