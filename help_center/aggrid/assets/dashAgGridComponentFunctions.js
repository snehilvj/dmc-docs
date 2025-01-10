
var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.DMC_Button = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData();
    }
    let leftIcon, rightIcon;
    if (props.leftIcon) {
        leftIcon = React.createElement(window.dash_iconify.DashIconify, {
            icon: props.leftIcon,
        });
    }
    if (props.rightIcon) {
        rightIcon = React.createElement(window.dash_iconify.DashIconify, {
            icon: props.rightIcon,
        });
    }
    return React.createElement(
        window.dash_mantine_components.Button,
        {
            onClick,
            variant: props.variant,
            color: props.color,
            leftSection: leftIcon,
            rightSection: rightIcon,
            radius: props.radius,
            style: {
                margin: props.margin,
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
            },
        },
        props.value
    );
};


dagcomponentfuncs.DMC_Card = function (props) {
    return React.createElement(
        window.dash_mantine_components.Card,
        {
            withBorder:true
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


