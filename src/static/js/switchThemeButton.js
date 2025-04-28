
function changeToDarkMode(button) {
    document.documentElement.dataset.bsTheme = "dark";
    const switchThemeButtonClassList = button.children[0].classList;
    switchThemeButtonClassList.replace("bi-moon", "bi-sun-fill");
}

function changeToLightMode(button) {
    document.documentElement.dataset.bsTheme = "light";
    const switchThemeButtonClassList = button.children[0].classList;
    switchThemeButtonClassList.replace("bi-sun-fill", "bi-moon");
}

function getCurrentTheme() {
    return document.documentElement.dataset.bsTheme;
}

// https://stackoverflow.com/a/57795495
function prefersDarkTheme() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
}

function switchTheme(e) {
    const button = e.currentTarget;
    let currentTheme = getCurrentTheme();
    switch (currentTheme) {
        case "dark":
            changeToLightMode(button);
            break;
        case "light":
            changeToDarkMode(button);
            break;
        default:
            changeToLightMode(button);
    }
}

const switchThemeButton = document.getElementById("switch-theme-button");
if (prefersDarkTheme()) {
    changeToDarkMode(switchThemeButton);
}
switchThemeButton.addEventListener("click", switchTheme);