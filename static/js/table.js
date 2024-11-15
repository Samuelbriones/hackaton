// Variables
const yearFilter = document.getElementById('year-filter');
const countryFilter1 = document.getElementById('country-filter-1');
const countryFilter2 = document.getElementById('country-filter-2');
const filterButton = document.getElementById('filter-button');
const tableBody = document.getElementById('energy-table').querySelector('tbody');

// Función para cargar datos desde el servidor
async function fetchEnergyData() {
    try {
        const response = await fetch('/energy_data/');
        return await response.json();
    } catch (error) {
        console.error('Error al cargar los datos:', error);
    }
}

// Función para filtrar datos
function filterData(data, year, country1, country2) {
    return data.filter(item => {
        const matchesYear = year ? item.year == year : true;
        const matchesCountry = country1 || country2
            ? item.entity === country1 || item.entity === country2
            : true;
        return matchesYear && matchesCountry;
    });
}

// Función para renderizar datos en la tabla
function renderTable(data) {
    tableBody.innerHTML = ''; // Limpiar tabla
    data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.year}</td>
            <td>${item.electricity_from_fossil_fuels}</td>
            <td>${item.electricity_from_nuclear}</td>
            <td>${item.electricity_from_renewables}</td>
            <td>${item.co2_emissions}</td>
            <td>${item.entity}</td>
        `;
        tableBody.appendChild(row);
    });
}

// Manejar clic en el botón de filtro
filterButton.addEventListener('click', async () => {
    const data = await fetchEnergyData();
    const filteredData = filterData(
        data,
        yearFilter.value,
        countryFilter1.value.trim(),
        countryFilter2.value.trim()
    );
    renderTable(filteredData);
});

// Cargar datos iniciales
(async () => {
    const data = await fetchEnergyData();
    renderTable(data);
})();
