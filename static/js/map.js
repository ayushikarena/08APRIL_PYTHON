// map.js
// Interactive Map Engine using Leaflet.js & OpenStreetMap (No API key required)
// Also supports HTML5 Browser Geolocation and Nominatim Reverse Geocoding.

let map;
let marker;

// Default initial location (Rajkot / User coordinates or fallback)
const defaultLat = 22.283656;
const defaultLng = 70.787468;

/**
 * Initializes the Interactive Leaflet Map with OpenStreetMap tiles.
 */
function initMap() {
    const mapElement = document.getElementById("map");
    if (!mapElement) return;

    // Remove any existing leaflet instance if re-initialized
    if (map) {
        map.remove();
    }

    // Initialize Leaflet Map centered at default coordinates
    map = L.map('map').setView([defaultLat, defaultLng], 14);

    // Add OpenStreetMap High-Resolution Tile Layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Create Draggable Pin Marker
    marker = L.marker([defaultLat, defaultLng], {
        draggable: true,
        title: "Selected Location Pin"
    }).addTo(map);

    // Initial address & coordinates update
    updateLocationDetails(defaultLat, defaultLng);

    // Event Listener: Map Click to move marker pin
    map.on('click', (e) => {
        const clickedLat = e.latlng.lat;
        const clickedLng = e.latlng.lng;
        
        marker.setLatLng([clickedLat, clickedLng]);
        updateLocationDetails(clickedLat, clickedLng);
    });

    // Event Listener: Marker Drag End
    marker.on('dragend', () => {
        const position = marker.getLatLng();
        updateLocationDetails(position.lat, position.lng);
    });

    // Auto-detect user geolocation
    fetchCurrentLocation();
}

/**
 * Uses HTML5 Browser Geolocation API to locate current user position.
 */
function fetchCurrentLocation() {
    const statusText = document.getElementById("location-status");

    if (navigator.geolocation) {
        if (statusText) statusText.innerHTML = '<i class="bi bi-crosshair me-1"></i> Locating your position...';

        navigator.geolocation.getCurrentPosition(
            (position) => {
                const userLat = position.coords.latitude;
                const userLng = position.coords.longitude;

                if (map && marker) {
                    map.setView([userLat, userLng], 15);
                    marker.setLatLng([userLat, userLng]);
                    updateLocationDetails(userLat, userLng);
                }

                if (statusText) statusText.innerHTML = '<i class="bi bi-check-circle-fill text-success me-1"></i> Location detected successfully!';
            },
            (error) => {
                if (statusText) statusText.innerHTML = '<i class="bi bi-exclamation-triangle-fill text-warning me-1"></i> Unable to access browser geolocation. Displaying default location pin.';
                console.warn("Geolocation Warning: ", error.message);
            }
        );
    } else {
        if (statusText) statusText.innerHTML = '<i class="bi bi-exclamation-circle text-danger me-1"></i> Geolocation is not supported by your browser.';
    }
}

/**
 * Updates Latitude, Longitude, and Reverse Geocoded Address using Nominatim OpenStreetMap API.
 */
function updateLocationDetails(lat, lng) {
    const latElement = document.getElementById("latitude");
    const lngElement = document.getElementById("longitude");
    const addressElement = document.getElementById("address");

    if (latElement) latElement.innerText = lat.toFixed(6);
    if (lngElement) lngElement.innerText = lng.toFixed(6);

    if (addressElement) addressElement.innerHTML = '<span class="text-muted"><i class="bi bi-hourglass-split me-1"></i> Fetching address...</span>';

    // Reverse Geocoding API Request (Nominatim OpenStreetMap)
    const geocodeUrl = `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lng}`;

    fetch(geocodeUrl)
        .then(response => response.json())
        .then(data => {
            if (data && data.display_name) {
                if (addressElement) addressElement.innerText = data.display_name;
            } else {
                if (addressElement) addressElement.innerText = "Street address details unavailable for these coordinates.";
            }
        })
        .catch(err => {
            if (addressElement) addressElement.innerText = `Coordinates: ${lat.toFixed(6)}, ${lng.toFixed(6)}`;
            console.error("Geocoding Fetch Error: ", err);
        });
}

// Automatically initialize map when window finishes loading
document.addEventListener("DOMContentLoaded", () => {
    initMap();
});
