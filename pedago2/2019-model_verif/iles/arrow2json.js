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
    'Lac': 'riviere',
    'lac': 'riviere',
    'Crique': 'riviere',
    'Forêt de conifères': 'sapin',
    'forêt de conifères': 'sapin',
    'Cabane du chasseur': "cabane_peche",
    'cabane du chasseur': "cabane_peche"
}

function f(reg, cb) {
    return function (text) {
        const r = text.split(reg).map(x => x.trim()).filter(x => x.length !== 0);
        return r.map(x => (y => ({ name: x.slice(0, y).trim(), content: cb(x.slice(y).trim()) }))(x.indexOf('\n')));
    }
}

function g() {
    return function (text) {
        const tmp = text.split('\n').map(x => x.trim());
        const tmp1 = tmp.map(x => x.split(/ -> /).map(x => x.trim()));
        const nodes = [...(new Set(tmp1.reduce((x, y) => [...x, ...y], [])))]
            .map(x => (DICT[x]!==undefined?1:console.error(x+' not found in DICT'),{ id: DICT[x] || x, img: (DICT[x] || x) + '.svg' }));
        const links = tmp1.reduce((acc, x) => x.length > 2 ? [...acc, ...normalize_multiLink(x)] : [...acc, x], [])
            .map(([source, target]) => ({ source: DICT[source] || source, target: DICT[target] || target }));
        return { nodes: nodes, links: links }
    }
}

function normalize_multiLink(l) {
    let old = l[0];
    const r = [];
    for (let i = 1; i < l.length; i++) {
        r.push([old, l[i]]);
        old = l[i];
    }
    return r;
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