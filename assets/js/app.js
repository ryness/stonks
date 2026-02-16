const state = {
  reports: [],
  workflowUrl: document.body.dataset.workflowUrl,
  deleteWorkflowUrl: document.body.dataset.deleteWorkflowUrl,
  activeIndex: null,
  linkElements: [],
  sortOrder: 'alpha-asc',
};

const elements = {
  links: document.querySelector('#reportLinks'),
  refresh: document.querySelector('#refreshLink'),
  rerun: document.querySelector('#rerunLink'),
  delete: document.querySelector('#deleteLink'),
  content: document.querySelector('#reportContent'),
  status: document.querySelector('#statusMessage'),
};

const SORT_STORAGE_KEY = 'stonks-sort-order';
const ACTIVE_INDEX_STORAGE_KEY = 'stonks-active-index';
const ACTIVE_TICKER_STORAGE_KEY = 'stonks-active-ticker';
const SORT_OPTIONS = ['alpha-asc', 'alpha-desc', 'updated-desc', 'updated-asc'];
const sortLinks = Array.from(document.querySelectorAll('#sortLinks [data-sort]'));

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
  elements.status.textContent = report.title || '';
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
  clearStoredSelection();
  state.linkElements.forEach((link) => delete link.dataset.active);
  if (!preserveStatus) {
    elements.status.textContent = '';
  }
  elements.content.innerHTML = '';
}

function highlightActiveLink() {
  state.linkElements.forEach((link) => {
    const linkIndex = Number(link.dataset.index);
    if (state.activeIndex !== null && !Number.isNaN(linkIndex) && linkIndex === state.activeIndex) {
      link.dataset.active = 'true';
    } else {
      delete link.dataset.active;
    }
  });
}

function storeActiveSelection(index, ticker) {
  try {
    if (Number.isFinite(index)) {
      window.sessionStorage.setItem(ACTIVE_INDEX_STORAGE_KEY, String(index));
    } else {
      window.sessionStorage.removeItem(ACTIVE_INDEX_STORAGE_KEY);
    }
    if (ticker) {
      window.sessionStorage.setItem(ACTIVE_TICKER_STORAGE_KEY, ticker);
    } else {
      window.sessionStorage.removeItem(ACTIVE_TICKER_STORAGE_KEY);
    }
  } catch (error) {
    console.warn('Unable to store active selection', error);
  }
}

function clearStoredSelection() {
  try {
    window.sessionStorage.removeItem(ACTIVE_INDEX_STORAGE_KEY);
    window.sessionStorage.removeItem(ACTIVE_TICKER_STORAGE_KEY);
  } catch (error) {
    console.warn('Unable to clear active selection', error);
  }
}

function showReport(index) {
  const report = state.reports[index];
  if (!report) {
    return;
  }
  state.activeIndex = index;
  storeActiveSelection(index, report.ticker || '');
  highlightActiveLink();
  renderReport(report);
}

function getDateValue(report) {
  if (!report) {
    return null;
  }
  const raw = report.generated_at || report.date;
  if (!raw) {
    return null;
  }
  const timestamp = new Date(raw).getTime();
  return Number.isNaN(timestamp) ? null : timestamp;
}

function normalizeTicker(report) {
  return (report && report.ticker ? String(report.ticker) : '').toUpperCase();
}

function compareDateValues(dateA, dateB, direction) {
  if (dateA === null && dateB === null) {
    return 0;
  }
  if (dateA === null) {
    return direction === 'desc' ? 1 : -1;
  }
  if (dateB === null) {
    return direction === 'desc' ? -1 : 1;
  }
  if (dateA === dateB) {
    return 0;
  }
  return direction === 'desc' ? dateB - dateA : dateA - dateB;
}

function compareReports(a, b, order) {
  const tickerA = normalizeTicker(a);
  const tickerB = normalizeTicker(b);
  const dateA = getDateValue(a);
  const dateB = getDateValue(b);

  switch (order) {
    case 'alpha-desc': {
      const tickerComparison = tickerB.localeCompare(tickerA);
      if (tickerComparison !== 0) {
        return tickerComparison;
      }
      return compareDateValues(dateA, dateB, 'desc');
    }
    case 'updated-desc': {
      const dateComparison = compareDateValues(dateA, dateB, 'desc');
      if (dateComparison !== 0) {
        return dateComparison;
      }
      return tickerA.localeCompare(tickerB);
    }
    case 'updated-asc': {
      const dateComparison = compareDateValues(dateA, dateB, 'asc');
      if (dateComparison !== 0) {
        return dateComparison;
      }
      return tickerA.localeCompare(tickerB);
    }
    case 'alpha-asc':
    default: {
      const tickerComparison = tickerA.localeCompare(tickerB);
      if (tickerComparison !== 0) {
        return tickerComparison;
      }
      return compareDateValues(dateA, dateB, 'desc');
    }
  }
}

function sortReports() {
  if (!Array.isArray(state.reports) || state.reports.length <= 1) {
    return;
  }
  const currentTicker =
    state.activeIndex !== null && state.reports[state.activeIndex]
      ? state.reports[state.activeIndex].ticker || null
      : null;

  state.reports.sort((a, b) => compareReports(a, b, state.sortOrder));

  if (currentTicker) {
    const nextIndex = state.reports.findIndex((report) => report.ticker === currentTicker);
    state.activeIndex = nextIndex !== -1 ? nextIndex : null;
    if (state.activeIndex !== null) {
      storeActiveSelection(state.activeIndex, currentTicker);
    } else {
      clearStoredSelection();
    }
  }
}

function populateLinks(reports) {
  elements.links.innerHTML = '';
  state.linkElements = [];
  if (!Array.isArray(reports) || !reports.length) {
    return;
  }
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
  highlightActiveLink();
}

async function loadReports({ bustCache = false } = {}) {
  try {
    elements.status.textContent = 'Loading reports...';
    const baseUrl = window.__baseUrl || '';
    const reportsUrl = `${baseUrl}/reports.json`;
    const requestUrl = bustCache
      ? `${reportsUrl}${reportsUrl.includes('?') ? '&' : '?'}_=${Date.now()}`
      : reportsUrl;
    const response = await fetch(requestUrl, {
      cache: bustCache ? 'reload' : 'default',
    });
    if (!response.ok) {
      throw new Error(`Failed to load reports.json (${response.status})`);
    }
    const data = await response.json();
    state.reports = Array.isArray(data) ? data : [];
    state.activeIndex = null;
    sortReports();
    populateLinks(state.reports);
    if (!state.reports.length) {
      elements.status.textContent = 'No reports have been generated yet.';
      clearSelection(true);
      return;
    }
    elements.status.textContent = '';
    const savedSelection = (() => {
      try {
        const rawIndex = window.sessionStorage.getItem(ACTIVE_INDEX_STORAGE_KEY);
        const storedTicker = window.sessionStorage.getItem(ACTIVE_TICKER_STORAGE_KEY);
        const parsedIndex = rawIndex !== null ? Number(rawIndex) : NaN;
        return {
          index: Number.isFinite(parsedIndex) ? parsedIndex : null,
          ticker: storedTicker || null,
        };
      } catch (error) {
        console.warn('Unable to read stored active selection', error);
        return { index: null, ticker: null };
      }
    })();

    let targetIndex = null;
    if (savedSelection.ticker) {
      const matched = state.reports.findIndex((report) => report.ticker === savedSelection.ticker);
      if (matched !== -1) {
        targetIndex = matched;
      }
    }
    if (
      targetIndex === null &&
      savedSelection.index !== null &&
      Number.isFinite(savedSelection.index) &&
      savedSelection.index >= 0 &&
      savedSelection.index < state.reports.length
    ) {
      targetIndex = savedSelection.index;
    }

    if (targetIndex !== null) {
      showReport(targetIndex);
    } else {
      clearSelection();
    }
  } catch (error) {
    console.error(error);
    elements.status.textContent = 'Unable to load reports. Please try again later.';
  }
}

function setWorkflowLinkState(linkElement, url) {
  if (!linkElement) {
    return;
  }
  if (url) {
    linkElement.href = url;
    linkElement.removeAttribute('aria-disabled');
    delete linkElement.dataset.disabled;
    linkElement.removeAttribute('tabindex');
  } else {
    linkElement.href = '#';
    linkElement.setAttribute('aria-disabled', 'true');
    linkElement.dataset.disabled = 'true';
    linkElement.setAttribute('tabindex', '-1');
  }
}

function openWorkflowLink(event, url, missingMessage) {
  if (!url) {
    event.preventDefault();
    alert(missingMessage);
    return;
  }
  if (event.defaultPrevented) {
    return;
  }
  if (event.button === 1 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
    return;
  }
  event.preventDefault();
  window.open(url, '_blank', 'noopener');
}

function configureWorkflowLinks() {
  const rerunUrl = state.workflowUrl && state.workflowUrl.startsWith('http') ? state.workflowUrl : null;
  const deleteUrl =
    state.deleteWorkflowUrl && state.deleteWorkflowUrl.startsWith('http')
      ? state.deleteWorkflowUrl
      : null;
  setWorkflowLinkState(elements.rerun, rerunUrl);
  setWorkflowLinkState(elements.delete, deleteUrl);
}

elements.rerun?.addEventListener('click', (event) => {
  const url = state.workflowUrl && state.workflowUrl.startsWith('http') ? state.workflowUrl : null;
  openWorkflowLink(
    event,
    url,
    'Workflow URL is not configured. Update _config.yml with your repository name.'
  );
});

elements.delete?.addEventListener('click', (event) => {
  const url =
    state.deleteWorkflowUrl && state.deleteWorkflowUrl.startsWith('http')
      ? state.deleteWorkflowUrl
      : null;
  openWorkflowLink(
    event,
    url,
    'Delete workflow URL is not configured. Update _config.yml with your repository name.'
  );
});

elements.refresh?.addEventListener('click', (event) => {
  event.preventDefault();
  loadReports({ bustCache: true });
});

function updateSortLinkIndicators() {
  sortLinks.forEach((link) => {
    if (link.dataset.sort === state.sortOrder) {
      link.dataset.active = 'true';
    } else {
      delete link.dataset.active;
    }
  });
}

function setSortOrder(nextOrder, { persist = false } = {}) {
  const normalized = SORT_OPTIONS.includes(nextOrder) ? nextOrder : 'alpha-asc';
  state.sortOrder = normalized;
  updateSortLinkIndicators();
  if (persist) {
    try {
      window.localStorage.setItem(SORT_STORAGE_KEY, normalized);
    } catch (error) {
      console.warn('Unable to store sort order', error);
    }
  }
  sortReports();
  populateLinks(state.reports);
}

function initializeSortOrder() {
  let restoredOrder = null;
  try {
    restoredOrder = window.localStorage.getItem(SORT_STORAGE_KEY);
  } catch (error) {
    console.warn('Unable to read stored sort order', error);
  }
  setSortOrder(restoredOrder || state.sortOrder);
}

sortLinks.forEach((link) => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    setSortOrder(link.dataset.sort, { persist: true });
  });
});

configureWorkflowLinks();
initializeSortOrder();
loadReports();
