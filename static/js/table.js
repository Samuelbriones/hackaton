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

// Función para llenar los menús desplegables
function populateFilters(data) {
    // Obtener años y países únicos
    const years = [...new Set(data.map(item => item.year))].sort((a, b) => a - b);
    const countries = [...new Set(data.map(item => item.entity))].sort();

    // Llenar años
    years.forEach(year => {
        const option = document.createElement('option');
        option.value = year;
        option.textContent = year;
        yearFilter.appendChild(option);
    });

    // Llenar países
    countries.forEach(country => {
        const option1 = document.createElement('option');
        option1.value = country;
        option1.textContent = country;
        countryFilter1.appendChild(option1);

        const option2 = document.createElement('option');
        option2.value = country;
        option2.textContent = country;
        countryFilter2.appendChild(option2);
    });
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
            <td>${item.electricity_from_fossil_fuels} TWh</td>
            <td>${item.electricity_from_nuclear} TWh</td>
            <td>${item.electricity_from_renewables} TWh</td>
            <td>${(item.co2_emissions / 1000).toFixed(2)} kt</td>
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
        countryFilter1.value,
        countryFilter2.value
    );
    renderTable(filteredData);
});

// Cargar datos iniciales y llenar filtros
(async () => {
    const data = await fetchEnergyData();
    populateFilters(data);
    renderTable(data);
})();
