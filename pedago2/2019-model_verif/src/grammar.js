

function origin() {
    const exclude = []
    const début = lieu(exclude, lieux_début)
    const début_fin = (Math.random() > 0.5) ? [phrase(prop_fin(prop_début(début, prop(exclude))))] : [phrase(prop_début(début, prop(exclude))), phrase(prop_fin(prop()))]
    const other = Array(5).fill(0).map((x, i) => phrase((i < 3) ? prop() : prop_invalide()))
    return {
        rédigé: début_fin.map(x => x.rédigé).join("\n") + "\n" + other.map(x => x.rédigé).join("\n"),
        prédicat: (v, e) => début_fin.every(x => x.prédicat(v, e)) && other.every(x => x.prédicat(v, e))
    }
}
function origin_temps() {
    const exclude = []
    const début = lieu(exclude, lieux_début)
    const début_fin = (Math.random() > 0.5) ? [phrase(prop_fin(prop_début(début, prop(exclude))))] : [phrase(prop_début(début, prop(exclude))), phrase(prop_fin(prop()))]
    const other = Array(3).fill(0).map((x, i) => phrase((i < 1) ? prop() : prop_invalide()))
    const temps = phrase(prop_temps())
    return {
        rédigé: début_fin.map(x => x.rédigé).join("\n") + "\n" + other.map(x => x.rédigé).join("\n") + "\n" + temps.rédigé,
        prédicat: (v, e) => début_fin.every(x => x.prédicat(v, e)) && other.every(x => x.prédicat(v, e)) && temps.prédicat(v, e)
    }
}
// syntaxe
function phrase(s) {
    return { ...s, rédigé: s.rédigé.charAt(0).toUpperCase() + s.rédigé.slice(1) + "." }
}
function prop_début(début, s) {
    const rules = [
        () => ({
            ...s, rédigé: `j'ai débarqué ${début.position} et ${s.rédigé}`,
            prédicat: (v, e) => [].some(x => x === début.key) && s.prédicat(v, e)
        }),
        // () => ({
        //     ...s, rédigé: `j'ai débarqué ${début.position}`,
        //     prédicat: (v, e) => [].some(x => x === début.key)
        // }),
    ]
    return choose_Rand(rules)()
}
function prop_temps(exclude = []) {
    const rules = [
        // () => {
        //     const start = lieu(exclude)
        //     const end = lieu(exclude)
        //     const h = heure()
        //     return {
        //         rédigé: `pour aller ${start.direction} jusqu'${à(end.decl)} en empruntant le chemin que j'ai décrit, il m'a fallu ${h.rédigé} en tout`,
        //         prédicat: (v, e) => dijkstra(v, e, start.key, end.key, x => x.time, (x, end) => x.coût === h.number && x.id === end)
        //     }
        // },
        () => {
            const start = lieu(exclude)
            const end = lieu(exclude)
            const h = heure()
            return {
                rédigé: `pour aller ${start.direction} jusqu'${à(end.decl)}, il m'a fallu ${h.rédigé} en passant par le chemin de plus court`,
                prédicat: (v, e) => dijkstra(v, e, start.key, end.key, x => x.time, (x, end) => x.coût === h.number && x.id === end) !== undefined
            }
        }
    ]
    return choose_Rand(rules)()
}

function path2edges(p) {
    const r = []
    for (let i = 1; i < p.length; i++) {
        r.push([p[i], p[i - 1]]);
    }
    return r
}
function log(x) {
    console.log(7, x)
    return x
}
function prop(exclude = []) {
    const rules = [
        () => {
            const l = Array(4).fill(0).map(x => lieu(exclude))
            return {
                rédigé: `je suis passé successivement par ${l[0].decl}, ${l[1].decl} et ${l[2].decl} avant d'arriver ${l[3].position}`,
                prédicat: (v, e) => path2edges(l.map(x => x.key)).every(([a, b]) => e.find(({ source, target }) => (a === source && b === target) || (a === target && b === source)) !== undefined)
            }
        },
        () => {
            const from = lieu(exclude), to = lieu(exclude), without = lieu(exclude)
            return {
                rédigé: `depuis ${from.decl} je suis allé ${to.position}, sans passer par ${without.decl}`,
                prédicat: (v, e) => log(dijkstra(v.filter(x => x !== without.key), e, from.key, to.key)) !== undefined
            }
        },
        // () => ({ rédigé: `pour aller ${lieu(exclude).position} depuis ${lieu(exclude).decl}, on passe forcément par ${lieu(exclude).decl}`, prédicat: (v, e) => true }),
    ]
    return choose_Rand(rules)()
}

function prop_invalide() {
    const exclude = []
    const rules = [
        () => {
            const from = lieu(exclude), to = lieu(exclude)
            return {
                rédigé: `quand je passais par ${from.decl}, j'ai vu un chemin direct qui descendait jusqu'${à(to.decl)}${validité()}`,
                prédicat: (v, e) => e.find(({ source, target }) => (from === source && to === target) || (from === target && to === source)) === undefined
            }
        },
        () => {
            const from = lieu(exclude), to = lieu(exclude)
            return {
                rédigé: `depuis ${from.position}, j'ai voulu aller directement ${to.position}${validité()}`,
                prédicat: (v, e) => e.find(({ source, target }) => (from === source && to === target) || (from === target && to === source)) === undefined
            }
        },
        () => {
            const from = lieu(exclude), to = lieu(exclude)
            return {
                rédigé: `quand j'étais ${from.position}, j'aurais voulu aller directement ${to.position}${validité()}`,
                prédicat: (v, e) => e.find(({ source, target }) => (from === source && to === target) || (from === target && to === source)) === undefined
            }
        }
    ]
    return choose_Rand(rules)()
}
// function prop() {
//     const exclude = []
//     const rules = [
//         () => ({rédigé:`Pour cacher le trésor, j'ai débarqué ${lieu(exclude, lieux_début).position} et je suis passé successivement par ${lieu(exclude).decl}, ${lieu(exclude).decl} et ${lieu(exclude).decl} avant d'arriver ${lieu(exclude).position}, où j'ai caché mon trésor.`}),
//         () => ({rédigé:`Quand je passais par ${lieu(exclude).decl}, j'ai vu un chemin qui descendait jusqu'${lieu(exclude).position}${validité()}.`}),
//         () => ({rédigé:`Quand j'étais ${lieu(exclude).position}, j'aurais voulu aller ${lieu(exclude).position}${validité()}.`}),
//         () => ({rédigé:`Pour aller ${lieu(exclude).position} depuis ${lieu(exclude).decl}, on passe forcément par ${lieu(exclude).decl}.`}),
//         () => ({rédigé:`Pour aller ${lieu(exclude).direction} jusqu'${à(lieu(exclude).decl)} en empruntant le chemin que j'ai décrit, il m'a fallu ${heure()} en tout.`})
//]
//     return choose_Rand(rules)()
// }

function prop_fin(s) {
    const rules = [
        () => ({ rédigé: `${s.rédigé.charAt(0).toUpperCase() + s.rédigé.slice(1)}, où j'ai caché mon trésor`, prédicat: (v, e) => true })
    ]
    return choose_Rand(rules)()
}

const Lieux = {
    "sapin": { decl: "la forêt de conifères", direction: "de la forêt de conifères", position: "dans la forêt de conifères" },
    "plage": { decl: "la plage", direction: "de la plage", position: "sur la plage" },
    "crique": { decl: "la crique", direction: "de la crique", position: "dans la crique" },
    "palmier": { decl: "la forêt de palmiers", direction: "de la forêt de palmiers", position: "dans la forêt de palmiers" },
    "cabane_peche": { decl: "la cabane de pêcheur", direction: "de la cabane de pêcheur", position: "à la cabane de pêcheur" },
    "volcan": { decl: "le volcan", direction: "du volcan", position: "sur le volcan" },
    "montagne": { decl: "la montagne", direction: "de la montagne", position: "sur la montagne" },
    "riviere": { decl: "la rivière", direction: "de la rivière", position: "sur la rivière" },
    "lac": { decl: "le lac", direction: "du lac", position: "sur le lac" },
    "grotte": { decl: "la grotte", direction: "de la grotte", position: "dans la grotte" },
    "cabane_chasse": { decl: "la cabane de chasseur", direction: "de la cabane de chasseur", position: "à cabane de chasseur" },
}

function lieu(exclude = [], include) {
    const [k, v] = choose_Rand(Object.entries(Lieux).filter(([k, v]) => exclude.findIndex(x => x === k) === -1 && (!include || include.findIndex(x => x === k) !== -1)))
    exclude.push(k)
    return { ...v, key: k }
}

function heure() {
    return choose_Rand(
        [
            { number: 1, rédigé: "une heure" },
            { number: 2, rédigé: "deux heures" },
            { number: 3, rédigé: "trois heures" },
            { number: 4, rédigé: "quatres heures" },
            { number: 5, rédigé: "cinq heures" },
            { number: 6, rédigé: "six heures" },
            { number: 7, rédigé: "sept heures" },
            { number: 8, rédigé: "huit heures" }]
    )
}

const lieux_début = ["plage", "cabane_peche", "crique"]

function validité() {
    return choose_Rand(
        [", mais je ne pouvais pas passer", ", mais le chemin était trop étroit pour que je passe avec mon trésor. Je ne l'ai donc pas emprunté"]
    )
}

function choose_Rand(l) {
    const i = Math.floor(Math.random() * l.length)
    return l[i]
}

function à(s) {
    if (s.startsWith("le")) {
        return "au" + s.slice(2)
    } else {
        return "à " + s
    }
}
function dijkstra(v, e, start, end, coût = x => 1, finish = (x, end) => x.id === end) {

    /**
     * @type {{id:string,coût:number,path:string[]}[]}
     */
    let things = []
    v.forEach(x => {
        if (x.id === start) {
            things.push({ id: x.id, coût: 0, path: [x.id] })
        } else {
            things.push({ id: x.id, coût: Number.POSITIVE_INFINITY, path: [] })
        }
    });
    while (things.length > 0) {
        things.sort((x, y) => x.coût - y.coût)
        const curr = things.shift()
        for (const x of e) {
            const { source, target, time } = x
            if (curr.path[curr.path.length - 1] === source) {
                const a = things.find(y => y.id === target)
                if (a !== undefined && a.coût > curr.coût + coût(x)) {
                    a.path = [...curr.path, target]
                    a.coût = curr.coût + coût(x)
                    if (finish(a, end)) {
                        console.log(a, finish(a, end))
                        return a
                    }
                }
            }
            else if (curr.path[curr.path.length - 1] === target) {
                const a = things.find(y => y.id === source)
                if (a !== undefined && a.coût > curr.coût + coût(x)) {
                    a.path = [...curr.path, source]
                    a.coût = curr.coût + coût(x)
                    if (finish(a, end)) {
                        console.log(a, finish(a, end))
                        return a
                    }
                }
            }
        }

    }
    return undefined
}


// for (let i = 0; i < 10; i++) {
//     const r = prop_temps()
//     console.log(r.rédigé, r.prédicat(example.nodes, example.links))
// }
// console.log(dijkstra(example.nodes, example.links, "plage", "volcan"))
// console.log(dijkstra(example.nodes, example.links, "plage", "cabane_peche",x=>x.time,(x,end)=>x.coût===5&&x.id===end))

if (typeof require != 'undefined' && require.main == module) {
    const fs = require("fs");
    if (process.argv.length < 2 || process.argv[2]===undefined){
        console.error("need path to data")
        return;
    }
    const example = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
    console.log(example);
    return
    let chemin
    for (let i = 0; i < 1000; i++) {
        const start = [...example.nodes].filter(x => lieux_début.find(y => y === x.id) !== undefined).sort(() => Math.random() > 0.5)[0]
        const tmp = [start, ...[...example.nodes].filter(x => x !== start).sort(() => Math.random() > 0.5).slice(0, 4 + Math.floor(Math.random() * 3))]

        const a = path2edges(tmp).map(([a, b]) => ({ source: a.id, target: b.id }))
        if (a.every(({ source: a, target: b }) => example.links.find(({ source, target }) => (a === source && b === target) || (a === target && b === source)) !== undefined)) {
            chemin = { nodes: tmp, links: a }
            break
        }
    }
    console.log(111, chemin)
    let propriétés
    for (let i = 0; i < 100000; i++) {
        const r = origin_temps()
        // const r = prop()
        if (r.prédicat(chemin.nodes, chemin.links) && r.prédicat(example.nodes, example.links)) {
            propriétés = r
            break
        }
    }
    console.log(propriétés && propriétés.rédigé)
}