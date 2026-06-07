function renderPagesChart(rows) {
  const canvas = document.getElementById("pagesChart");
  if (!canvas || !window.Chart) return;
  const labels = rows.map((row) => row[0]);
  const values = rows.map((row) => row[1]);
  new Chart(canvas, {
    type: "bar",
    data: {
      labels,
      datasets: [{
        label: "Views",
        data: values,
        backgroundColor: "#0f766e",
        borderRadius: 6
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false } },
      scales: { y: { beginAtZero: true, ticks: { precision: 0 } } }
    }
  });
}
