
var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.DMC_Card = function (props) {
    return React.createElement(
        window.dash_mantine_components.Card,
        {
            withBorder: true,
            m: 4,
        },
        React.createElement(
            window.dash_mantine_components.Text,
            {c:"dimmed", tt: "uppercase", fw:700},
            props.data.stats
        ),
        React.createElement(
            window.dash_mantine_components.Text,
            {size: "lg"},
            props.data.results
        ),
        React.createElement(
            window.dash_mantine_components.Text,
            {size: "sm", c: (props.data.change > 0) ? "green" : "red"},
            props.data.change + "%"
        )
    );
};
