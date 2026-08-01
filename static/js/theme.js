// theme.js
// Icon-Only Theme Switcher Controls: Button 1 = Light/Black Background, Button 2 = Color Accents.

const PALETTES = [
    { id: 'indigo', name: 'Indigo Luxe', icon: 'bi-palette-fill' },
    { id: 'emerald', name: 'Emerald Gem', icon: 'bi-gem' },
    { id: 'ocean', name: 'Ocean Cyan', icon: 'bi-water' },
    { id: 'sunset', name: 'Sunset Gold', icon: 'bi-sunset-fill' },
    { id: 'cyber', name: 'Cyber Neon', icon: 'bi-lightning-charge-fill' }
];

let currentPaletteIndex = 0;

/**
 * Button 1: Background Mode (Light / Black)
 */
function applyBackgroundMode(mode, showToast = false) {
    const isDark = (mode === 'dark');
    const bgMode = isDark ? 'dark' : 'light';

    document.documentElement.setAttribute('data-bg', bgMode);
    localStorage.setItem('foodie_bg_mode', bgMode);

    const btnIcon = document.getElementById('bg-mode-icon');
    const bgBtn = document.getElementById('bg-toggle-btn');

    if (btnIcon) {
        btnIcon.className = isDark ? 'bi bi-moon-stars-fill text-warning fs-5' : 'bi bi-sun-fill text-warning fs-5';
    }

    if (bgBtn) {
        bgBtn.setAttribute('title', isDark ? 'Background: Black Theme (Click for Light)' : 'Background: Light Theme (Click for Black)');
    }

    if (showToast) {
        showToastBanner(isDark ? 'Background: Black Theme' : 'Background: Light Theme');
    }
}

function toggleBackgroundMode() {
    const currentMode = document.documentElement.getAttribute('data-bg') || 'light';
    const nextMode = (currentMode === 'dark') ? 'light' : 'dark';
    applyBackgroundMode(nextMode, true);
}

/**
 * Button 2: Color Palette Switcher (Icon-Only)
 */
function applyColorPalette(paletteId, showToast = false) {
    const index = PALETTES.findIndex(p => p.id === paletteId);
    if (index !== -1) {
        currentPaletteIndex = index;
    }

    const currentPalette = PALETTES[currentPaletteIndex];
    document.documentElement.setAttribute('data-palette', currentPalette.id);
    localStorage.setItem('foodie_color_palette', currentPalette.id);

    const btnIcon = document.getElementById('palette-btn-icon');
    const paletteBtn = document.getElementById('palette-toggle-btn');

    if (btnIcon) {
        btnIcon.className = `bi ${currentPalette.icon} fs-5`;
    }

    if (paletteBtn) {
        paletteBtn.setAttribute('title', `Color Theme: ${currentPalette.name} (Click to switch)`);
    }

    if (showToast) {
        showToastBanner(`Color Theme: ${currentPalette.name}`);
    }
}

function cycleColorPalette() {
    currentPaletteIndex = (currentPaletteIndex + 1) % PALETTES.length;
    applyColorPalette(PALETTES[currentPaletteIndex].id, true);
}

/**
 * Shared Toast Notification.
 */
function showToastBanner(message) {
    let toast = document.getElementById('theme-toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'theme-toast';
        toast.className = 'theme-toast-banner';
        document.body.appendChild(toast);
    }
    toast.innerHTML = `<i class="bi bi-sliders me-2"></i> ${message}`;
    toast.classList.add('show');

    setTimeout(() => {
        toast.classList.remove('show');
    }, 1800);
}

// Early theme initialization
(function initTheme() {
    const savedBg = localStorage.getItem('foodie_bg_mode') || 'light';
    const savedPalette = localStorage.getItem('foodie_color_palette') || 'indigo';
    document.documentElement.setAttribute('data-bg', savedBg);
    document.documentElement.setAttribute('data-palette', savedPalette);
})();

// DOM Ready initialization
document.addEventListener('DOMContentLoaded', () => {
    const savedBg = localStorage.getItem('foodie_bg_mode') || 'light';
    const savedPalette = localStorage.getItem('foodie_color_palette') || 'indigo';

    applyBackgroundMode(savedBg, false);
    applyColorPalette(savedPalette, false);

    // Button 1: Background Toggle
    const bgBtn = document.getElementById('bg-toggle-btn');
    if (bgBtn) {
        bgBtn.addEventListener('click', toggleBackgroundMode);
    }

    // Button 2: Color Palette Switcher
    const paletteBtn = document.getElementById('palette-toggle-btn');
    if (paletteBtn) {
        paletteBtn.addEventListener('click', cycleColorPalette);
    }
});
