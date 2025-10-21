// Title: Simple Vega-Lite Embeds for 6 Idioms
vegaEmbed("#vis-map", "./map.json", { actions: false }).catch(console.error);
vegaEmbed("#vis-bar", "./bar.json", { actions: false }).catch(console.error);
vegaEmbed("#vis-line", "./line.json", { actions: false }).catch(console.error);
vegaEmbed("#vis-stacked", "./stacked_area.json", { actions: false }).catch(console.error);
vegaEmbed("#vis-scatter", "./scatter.json", { actions: false }).catch(console.error);
vegaEmbed("#vis-donut", "./donut.json", { actions: false }).catch(console.error);
