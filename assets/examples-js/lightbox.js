var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
var dmc = window.dash_mantine_components;

dmcfuncs.renderCustomSlide = function ({ active }) {
    return React.createElement(
        dmc.Center,
        { h: "100%" },
        React.createElement(
            dmc.Text,
            { c: "white", size: "xl", fw: 700 },
            active ? "This slide is active" : "This slide is not active"
        )
    );
};

dmcfuncs.renderCustomThumb = function () {
    return React.createElement(
        dmc.Center,
        {
            h: "100%",
            bg: "blue.6",
            style: { borderRadius: 4 }
        },
        React.createElement(
            dmc.Text,
            { c: "white", size: "xs" },
            "Custom"
        )
    );
};

dmcfuncs.renderYouTube = function () {
    return React.createElement("iframe", {
        src: "https://www.youtube.com/embed/dQw4w9WgXcQ",
        title: "YouTube video",
        allow: "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
        allowFullScreen: true,
        style: {
            width: "80vw",
            height: "45vw",
            maxHeight: "70vh",
            border: "none",
            borderRadius: 8
        }
    });
};

dmcfuncs.renderYouTubeThumb = function () {
    return React.createElement(
        dmc.Center,
        {
            h: "100%",
            bg: "red.6",
            style: { borderRadius: 4 }
        },
        React.createElement(
            dmc.Text,
            { c: "white", size: "xs" },
            "YT"
        )
    );
};
