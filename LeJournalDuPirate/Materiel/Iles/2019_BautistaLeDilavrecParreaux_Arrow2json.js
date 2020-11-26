/**
 * 
 * @typedef {Object} Link a link in a graph
 * @property {string} source
 * @property {string} target
 * @property {string} [time]
 */

const DICT = {
    "plage": "plage",
    "forêt de palmiers": "palmier",
    'forêt de palmier': "palmier",
    'cabane du pêcheur': "cabane_peche",
    'cabane de pêcheur': "cabane_peche",
    'volcan': "volcan",
    'grotte': 'grotte',
    'rivière': 'riviere',
    'lac': 'lac',
    'crique': 'crique',
    'forêt de conifères': 'sapin',
    'cabane du chasseur': "cabane_chasse",
    'cabane de chasse': "cabane_chasse",
}
/**
 * @template T,U
 * @param {regex} reg 
 * @param {(...x:T)=>U} cb 
 */
function f(reg, cb) {
    return function (/**@type {string} */text) {
        const r = text.split(reg).map(x => x.trim()).filter(x => x.length !== 0);
        return r.map(x => (y => ({ name: x.slice(0, y).trim(), content: cb(x.slice(y).trim()) }))(x.indexOf('\n')));
    }
}

/**
 * 
 * @param {string} x 
 */
function genNode(x) {
    /** @type {string|undefined} */
    const normalized = DICT[x.toLowerCase()]
    if (normalized === undefined) throw new Error(x + ' not found in DICT');
    return { id: normalized, img: normalized + '.svg' }
}
/**
 * 
 * @param {Link}
 * @return {Link} a normalized link
 */
function genLink({ source, time, target }) {
    const normalized_s = DICT[source.toLowerCase()]
    if (normalized_s === undefined) throw new Error(normalized_s + ' not found in DICT');
    const normalized_t = DICT[target.toLowerCase()]
    if (normalized_t === undefined) throw new Error(normalized_t + ' not found in DICT');
    return { source: normalized_s, time: time, target: normalized_t }
}

function g() {
    return function (/** @type {string} */ text) {
        const lines = text.split('\n').map(x => x.trim()).filter(x => x !== '');
        const lines_splited = lines
            .map(line => line
                .split(/->/)
                .map(temp_node => temp_node
                    .split(/-/)
                    .map(comp => comp.trim())
                ));
        const nodes = [...(new Set(lines_splited.reduce((x, y) => [...x, ...y.map(x => x[0])], [])))]
            .map(genNode);
        const links = lines_splited.reduce((acc, x) => (x.length >= 2) ? [...acc, ...extract_links(x)] : acc, [])
            .map(genLink)
            // remove duplicate links
            .sort((a, b) => a.source.localeCompare(b.source) * 4 + a.target.localeCompare(b.target) * 2 + (a.time || "").localeCompare(b.time || ""))
            .filter((x, i, l) => (i === 0) ? true : x.source.localeCompare(l[i - 1].source) * 2 + x.target.localeCompare(l[i - 1].target) !== 0);
        console.log(links)
        return { nodes: nodes, links: links }
    }
}
/**
 * 
 * @param {Array<[string]|[string,string]>} p
 * @returns {[...Link]} links of a path p
 */
function extract_links(p) {
    const result = [];
    for (let i = 1; i < p.length; i++) {
        let curr = p[i - 1];
        let next = p[i];
        const o = { source: curr[0], target: next[0] }
        if (curr.length === 2) o.time = curr[1]
        result.push(o);
    }
    return result;
}

if (typeof require != 'undefined' && require.main == module) {
    const fs = require("fs");
    const path = require("path");

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
