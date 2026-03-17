const API_BASE = '/api';

async function loadSensors() {
    const response = await fetch(`${API_BASE}/sensors`);
    const sensors = await response.json();
    const tbody = document.getElementById('sensors-list');
    tbody.innerHTML = '';
    sensors.forEach(sensor => {
        const row = tbody.insertRow();
        row.innerHTML = `
            <td>${sensor.id}</td>
            <td>${sensor.name}</td>
            <td>${sensor.plant_name}</td>
            <td>${sensor.value}</td>
            <td>${sensor.unit}</td>
            <td>${new Date(sensor.created_at).toLocaleString()}</td>
            <td><button onclick="deleteSensor(${sensor.id})">Удалить</button></td>
        `;
    });
}

async function addSensor(event) {
    event.preventDefault();
    const form = event.target;
    const data = {
        name: form.name.value,
        plant_name: form.plant_name.value,
        value: parseFloat(form.value.value),
        unit: form.unit.value
    };
    const response = await fetch(`${API_BASE}/sensors`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (response.ok) {
        form.reset();
        loadSensors();
    } else {
        alert('Ошибка при добавлении');
    }
}

async function deleteSensor(id) {
    if (confirm('Удалить датчик?')) {
        const response = await fetch(`${API_BASE}/sensors/${id}`, { method: 'DELETE' });
        if (response.ok) {
            loadSensors();
        } else {
            alert('Ошибка при удалении');
        }
    }
}

document.getElementById('add-sensor-form').addEventListener('submit', addSensor);
loadSensors();