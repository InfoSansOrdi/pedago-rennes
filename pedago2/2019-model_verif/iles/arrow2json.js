const fs = require("fs");
const path = require("path");

DICT = {
    "Plage": "plage",
    "forêt de palmiers": "palmier",
    'Forêt de Palmiers': "palmier",
    'Forêt de palmiers': "palmier",
    'Cabane du pêcheur': "cabane_peche",
    'cabane du pêcheur': "cabane_peche",
    'cabane de pêcheur': "cabane_peche",
    'Cabane de pêcheur': "cabane_peche",
    'Volcan': "volcan",
    'volcan': "volcan",
    'Grotte': 'grotte',
    'grotte': 'grotte',
    'Rivière': 'riviere',
    'Lac': 'lac',
    'lac': 'lac',
    'Crique': 'crique',
    'Forêt de conifères': 'sapin',
    'forêt de conifères': 'sapin',
    'Cabane du chasseur': "cabane_chasse",
    'cabane du chasseur': "cabane_chasse"
}

function f(reg, cb) {
    return function (text) {
        const r = text.split(reg).map(x => x.trim()).filter(x => x.length !== 0);
        return r.map(x => (y => ({ name: x.slice(0, y).trim(), content: cb(x.slice(y).trim()) }))(x.indexOf('\n')));
    }
}

function g() {
    return function (text) {
        const lines = text.split('\n').map(x => x.trim());
        const lines_splited = lines.map(line => line.split(/-> /).map(temp_node => temp_node.split(/-/).map(comp => comp.trim()) ) );
	const link_nodes = lines_splited.map(line => line.map(comps => comps[0]));
	const timed_links = lines_splited.map(line => line.map(comps => (comps.length < 2) ? [...comps, '0h'] : comps));
        const nodes = [...(new Set(link_nodes.reduce((x, y) => [...x, ...y], [])))]
            .map(x => (DICT[x]!==undefined?1:console.error(x+' not found in DICT'),{ id: DICT[x] || x, img: (DICT[x] || x) + '.svg' }));
        const links = timed_links.reduce((acc, x) => (x.length >= 2) ? [...acc, ...extract_links(x)] : acc, [])
              .map(([source, time, target]) => ({ source: DICT[source] || source, time: time, target: DICT[target] || target }));
        return { nodes: nodes, links: links }
    }
}

function extract_links(l) {
    const result = [];
    for (let i = 1; i < l.length; i++) {
	let source = l[i-1];
	let dest   = l[i];
        result.push([source[0], source[1], dest[0]]);
    }
    return result;
}

if (typeof require != 'undefined' && require.main == module) {
    if (process.argv.length < 3)
        return;
    const text = fs.readFileSync(process.argv[2], "utf8").trim();

    const r = f(
        /(^|\n)\* /g,
        f(
            /(^|\n)\** /g,
            g()))(text)
    r.map(({ name, content }) => {
        try {
            fs.mkdirSync(path.join(process.argv[3], name));
        } catch (error) {
            // console.error(error);
        }
        content.map(({ name: name_file, content }) => {
            fs.writeFileSync(
                path.join(process.argv[3], name, name_file + '.json'),
                JSON.stringify(content, undefined, '    '))
        })
    })
}
