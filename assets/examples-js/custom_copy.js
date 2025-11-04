var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
var dmc = window.dash_mantine_components;
var DashIconify = window.dash_iconify.DashIconify;

dmcfuncs.copyActionIcon = function({ copied, copy }) {
  return React.createElement(
    dmc.Tooltip,
    {
      label: copied ? 'Copied' : 'Copy',
      withArrow: true,
      position: 'right'
    },
    React.createElement(
      dmc.ActionIcon,
      {
        color: copied ? 'teal' : 'gray',
        variant: 'subtle',
        onClick: copy
      },
      copied
        ? React.createElement(DashIconify, { icon: 'tabler:check', style: { width: 16, height: 16 } })
        : React.createElement(DashIconify, { icon: 'tabler:copy', style: { width: 16, height: 16 } })
    )
  );
};