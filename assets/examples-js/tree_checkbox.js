var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.myLeafCheckbox = function (payload) {
  const React = window.React;
  const dmc = window.dash_mantine_components;
  const iconify = window.dash_iconify;

  const { node, expanded, hasChildren, elementProps, tree } = payload;

  const checked = tree.isNodeChecked(node.value);
  const indeterminate = tree.isNodeIndeterminate(node.value);

  return React.createElement(
    dmc.Group,
    { key: node.value, gap: "xs", ...elementProps },
    [
      React.createElement(dmc.CheckboxIndicator, {
        key: "checkbox",
        checked,
        indeterminate,
        onClick: (e) => {
          e.stopPropagation();
          if (checked) {
            tree.uncheckNode(node.value);
          } else {
            tree.checkNode(node.value);
          }
        },
      }),
      React.createElement(
        dmc.Group,
        {
          key: "label-group",
          gap: 5,
          onClick: () => tree.toggleExpanded(node.value),
        },
        [
          React.createElement("span", { key: "label" }, node.label),
          hasChildren &&
            React.createElement(iconify.DashIconify, {
              key: "icon",
              icon: "tabler:chevron-down",
              width: 14,
              style: {
                transform: expanded ? "rotate(180deg)" : "rotate(0deg)",
                transition: "transform 0.2s ease",
              },
            }),
        ]
      ),
    ]
  );
};

