var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.filterCountries = function ({ options, search }) {
  const queryWords = search.toLowerCase().trim().split(" ");
  return options.filter((option) => {
    const words = option.label.toLowerCase().trim().split(" ");
    return queryWords.every((word) =>
      words.some((labelWord) => labelWord.includes(word))
    );
  });
};
