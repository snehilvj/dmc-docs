
var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.myLeaf = function (payload) {
  const dmc = window.dash_mantine_components;
  const iconify = window.dash_iconify;

  function getIcon(name, isFolder, expanded) {
    const size = 14;

    if (name.endsWith('package.json')) {
      return React.createElement(iconify.DashIconify, {
        icon: 'logos:npm-icon',
        width: size,
        height: size
      });
    }

    if (
      name.endsWith('.ts') ||
      name.endsWith('.tsx') ||
      name.endsWith('tsconfig.json')
    ) {
      return React.createElement(iconify.DashIconify, {
        icon: 'logos:typescript-icon',
        width: size,
        height: size
      });
    }

    if (name.endsWith('.css')) {
      return React.createElement(iconify.DashIconify, {
        icon: 'vscode-icons:file-type-css',
        width: size,
        height: size
      });
    }

    if (isFolder) {
      return React.createElement(iconify.DashIconify, {
        icon: expanded ? 'tabler:folder-open' : 'tabler:folder',
        width: size,
        height: size,
        color: '#f59f00' // Mantine yellow-9
      });
    }

    return null;
  }

  const { node, expanded, hasChildren, elementProps } = payload;

  return React.createElement(
    dmc.Group,
    { key: payload.node.value, gap: 5, ...elementProps },
    getIcon(node.value, hasChildren, expanded),
    React.createElement('span', null, node.label)
  );
};
