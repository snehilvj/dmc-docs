var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.filterPythonLibs = function ({ options, search }) {
  const query = search.toLowerCase().trim();
  const result = options.filter((option) =>
    option.label.toLowerCase().trim().includes(query)
  );
  result.sort((a, b) => a.label.localeCompare(b.label));
  return result;
};
