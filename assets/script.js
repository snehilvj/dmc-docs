const colorCallback = (color) => {
    const cmap = {'#3b3b3b': 'dark', '#adb5bd': 'gray', '#ff6b6b': 'red', '#f06595': 'pink', '#cc5de8': 'grape', '#845ef7': 'violet', '#5c7cfa': 'indigo', '#339af0': 'blue', '#22b8cf': 'cyan', '#20c997': 'teal', '#51cf66': 'green', '#94d82d': 'lime', '#fcc419': 'yellow', '#ff922b': 'orange'}
    return cmap[color];
}

const sliderCallback = (value) => {
    const smap = {
        "1": "xs",
        "2": "sm",
        "3": "md",
        "4": "lg",
        "5": "xl"
    }
    const ret = smap[value]
    return [ret, ret]
}

const generalCallback = (...kwargs) => {
    return Object.values(kwargs)
}

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: { colorCallback, sliderCallback, generalCallback }
});
