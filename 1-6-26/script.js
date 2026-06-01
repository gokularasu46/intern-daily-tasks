const stateMap = document.getElementById('indiaMap');
const detailsTitle = document.getElementById('detailsTitle');
const detailsSubtitle = document.getElementById('detailsSubtitle');
const detailsList = document.getElementById('detailsList');

let statesData = [];
let activePath = null;

fetch('states.json')
  .then((response) => response.json())
  .then((data) => {
    statesData = data;
    initializeMap();
  })
  .catch((error) => {
    console.error('Failed to load state data:', error);
    detailsTitle.textContent = 'Data failed to load';
    detailsSubtitle.textContent = 'Please refresh the page.';
  });

function initializeMap() {
  const statePaths = stateMap.querySelectorAll('.map-state');
  const stateLabels = stateMap.querySelectorAll('.state-label');

  const aliasMap = {
    'Jammu & Kashmir': 'Jammu and Kashmir',
    'Dadra & Diu': 'Dadra and Nagar Haveli and Daman and Diu',
    'Andaman & Nicobar': 'Andaman and Nicobar Islands'
  };

  statePaths.forEach((path) => {
    path.addEventListener('click', () => {
      const stateName = path.dataset.state;
      const state = statesData.find((item) => item.name === stateName);
      if (state) {
        selectState(path, state);
      }
    });

    path.addEventListener('mouseenter', () => path.classList.add('hover'));
    path.addEventListener('mouseleave', () => path.classList.remove('hover'));
  });

  stateLabels.forEach((label) => {
    label.addEventListener('click', () => {
      const rawText = label.textContent.trim();
      const stateName = aliasMap[rawText] || rawText;
      const state = statesData.find((item) => item.name === stateName);
      if (state) {
        const path = stateMap.querySelector(`.map-state[data-state="${state.name}"]`);
        if (path) {
          selectState(path, state);
        }
      }
    });

    label.addEventListener('mouseenter', () => label.classList.add('hover'));
    label.addEventListener('mouseleave', () => label.classList.remove('hover'));
  });
}

function selectState(path, state) {
  if (activePath) {
    activePath.classList.remove('active');
  }
  activePath = path;
  activePath.classList.add('active');

  detailsTitle.textContent = state.name;
  detailsSubtitle.textContent = `${state.type}`;

  detailsList.innerHTML = `
    <div class="detail-point">
      <strong>Capital</strong>
      <span>${state.capital}</span>
    </div>
    <div class="detail-point">
      <strong>Official Language</strong>
      <span>${state.language}</span>
    </div>
    <div class="detail-point">
      <strong>Famous Tourist Place</strong>
      <span>${state.touristPlace}</span>
    </div>
    <div class="detail-point">
      <strong>Major Industry</strong>
      <span>${state.industry}</span>
    </div>
    <div class="detail-point">
      <strong>Interesting Fact</strong>
      <span>${state.fact}</span>
    </div>
  `;
}
