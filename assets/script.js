const updateData = (triggered_id, data, ...kwargs) => {
    if (triggered_id !== undefined) {
        data = data.map((item) => {
        if (item['prop'] === triggered_id['prop']) {
            return { ...item, 'value': Object.values(kwargs)[triggered_id['arg']] }
        } else {
            return item
        }})
    }
    return data
}

const colorCallback = (data, color) => {
    const cmap = {'#3b3b3b': 'dark', '#adb5bd': 'gray', '#ff6b6b': 'red', '#f06595': 'pink', '#cc5de8': 'grape', '#845ef7': 'violet', '#5c7cfa': 'indigo', '#339af0': 'blue', '#22b8cf': 'cyan', '#20c997': 'teal', '#51cf66': 'green', '#94d82d': 'lime', '#fcc419': 'yellow', '#ff922b': 'orange'}
    triggered_id = dash_clientside.callback_context.triggered_id
    data = updateData(triggered_id, data, cmap[color])
    return [data, cmap[color]];
}

const sliderCallback = (data, value) => {
    const smap = {
        "1": "xs",
        "2": "sm",
        "3": "md",
        "4": "lg",
        "5": "xl"
    }
    const ret = smap[value]
    triggered_id = dash_clientside.callback_context.triggered_id
    data = updateData(triggered_id, data, ret)
    return [data, ret, ret]
}

const generateSnippetCode = (componentsProps, componentName) => {
    let snippet = `import dash_mantine_component as dmc\n\ndmc.${componentName}(\n\t# props as configured above:\n`
    for (const {prop, value} of Object.values(componentsProps)) {
        if (value !== undefined && value !== null && value !== '') {
            if (typeof value === 'string') {
                snippet += `\t${prop}="${value}",\n`
            } else if (typeof value === 'object') {
                snippet += `\t${prop}=${JSON.stringify(value)},\n`
            } else {
                if (value === true) {
                    snippet += `\t${prop}=True,\n`
                } else if (value === false) {
                    snippet += `\t${prop}=False,\n`
                } else {
                    snippet += `\t${prop}=${value},\n`
                }
            }
        }
    }
    snippet += `\t# other props...\n)`
    return snippet
}

const generalCallback = (data, ...kwargs) => {
    triggered_id = dash_clientside.callback_context.triggered_id
    data = updateData(triggered_id, data, ...kwargs)
    return [data].concat(Object.values(kwargs))
}

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: { colorCallback, sliderCallback, generalCallback, generateSnippetCode }
});
