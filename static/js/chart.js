document.addEventListener('DOMContentLoaded', () => {
  const map = L.map('map-container', {
    center: [20, 0],
    zoom: 2,
    maxBounds: [
      [-90, -180],
      [90, 180]
    ],
    maxBoundsViscosity: 1.0
  });

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  let geoJsonLayer;

  const colorScale = chroma.scale(['#f9f9f9', '#0d47a1']).domain([0, 100]);

  Promise.all([
    fetch('/static/js/geodata.json').then(res => res.json()),
    fetch('/static/js/datos.json').then(res => res.json())
  ]).then(([geoData, electricityData]) => {

    updateMap(2000, geoData, electricityData);
    createLegend();

    document.getElementById("year-slider").addEventListener("input", function() {
      const selectedYear = +this.value;
      document.getElementById("year-label").textContent = selectedYear;
      updateMap(selectedYear, geoData, electricityData);
    });

    function updateMap(year, geoData, electricityData) {
      const dataMap = new Map(
        electricityData
          .filter(d => d.year === year)
          .map(d => [d.entity, d])
      );

      if (geoJsonLayer) map.removeLayer(geoJsonLayer);

      geoJsonLayer = L.geoJson(geoData, {
        style: feature => {
          const countryData = dataMap.get(feature.properties.name);
          const value = countryData ? countryData.access_to_electricity : 0;
          return {
            fillColor: colorScale(value).hex(),
            weight: 1,
            color: 'white',
            fillOpacity: 0.8
          };
        },
        onEachFeature: (feature, layer) => {
          layer.on('mouseover', function () {
            const countryData = dataMap.get(feature.properties.name) || {};
            const tooltipContent = `
              <strong style="color: black;">${feature.properties.name}</strong><br>
              Acceso a electricidad: <span style="color: black;">${countryData.access_to_electricity || 0}%</span><br>
              Energía de fósiles: <span style="color: black;">${countryData.electricity_from_fossil_fuels || 0} TWh</span><br>
              Energía nuclear: <span style="color: black;">${countryData.electricity_from_nuclear || 0} TWh</span><br>
              Energías renovables: <span style="color: black;">${countryData.electricity_from_renewables || 0} TWh</span><br>
              Emisiones de CO2: <span style="color: black;">${countryData.co2_emissions || 0} kt</span>
            `;
            layer.bindTooltip(tooltipContent, { sticky: true }).openTooltip();
            this.setStyle({
              weight: 2,
              color: '#333'
            });
          });

          layer.on('mouseout', function () {
            this.closeTooltip();
            geoJsonLayer.resetStyle(this);
          });
        }
      }).addTo(map);
    }

    function createLegend() {
      const legendScale = document.getElementById('legend-scale');
      const steps = 5;
      const stepSize = 100 / steps;

      for (let i = 0; i <= steps; i++) {
        const value = i * stepSize;
        const color = colorScale(value).hex();
        const legendItem = document.createElement('div');
        legendItem.style.display = 'flex';
        legendItem.style.alignItems = 'center';
        legendItem.innerHTML = `
          <span style="display:inline-block;width:20px;height:20px;background:${color};margin-right:8px;"></span>
          <span>${Math.round(value)}%</span>
        `;
        legendScale.appendChild(legendItem);
      }
    }

  }).catch(error => console.error("Error cargando datos:", error));
});
