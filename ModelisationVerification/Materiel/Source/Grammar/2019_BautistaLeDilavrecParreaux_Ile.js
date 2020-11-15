/**
 * 
 * @typedef {Object} Link a link in a graph
 * @property {string} source
 * @property {string} target
 * @property {string} [time]
 */

`
#### Île Scorpion

-   Dans cette île, on ne peut débarquer que sur la plage.

-   De la grotte on peut aller au volcan.

-   Du volcan on peut descendre jusqu'à la forêt de palmiers.

-   Du volcan on peut aller à la rivière.

-   De la plage, on peut atteindre la forêt de palmiers.

-   La rivière débouche sur un lac.

-   La rivière permet d'aller jusqu'à la cabane du pêcheur.

#### L'île tortue

-   On peut arriver à l'île par la plage ou par la crique.

-   De la plage, un chemin tortueux mène à la forêt de palmiers.

-   En traversant la forêt de palmiers, on atteint la rive de la rivière.

-   De la cabane du pêcheur, on peut atteindre le lac ou la rivière.

-   En descendant par la façade est du volcan on atteint la grotte.

-   La cabane du pêcheur se trouve sur la façade ouest du volcan.

-   La crique mène à la forêt de conifères.

#### L'île de la fortune 

-   Le seul moyen d'arriver à l'île est de débarquer sur la plage.

-   De la plage, un chemin fleuri mène à la forêt de palmiers.

-   En traversant la forêt de palmiers on peut arriver sur le lac ou surla cabane du pêcheur.

-   Le lac est au pied du volcan.

-   Une grotte se cache sur la façade est du volcan.

-   La rivière prend sa source sur le volcan, et coule sur sa façade sud.

-   De la cabane du pêcheur, un chemin très escarpé mène jusqu'à la forêt de conifères.

#### L'île des oiseaux rapides 

-   La plage et la crique offrent toutes deux de bons endroits pour débarquer sur l'île.

-   Cette île a deux forêts: la forêt de palmiers, à côté de la plage, et la forêt de conifères, à côté de la crique.

-   Au fond de la crique, se dissimule la cabane du chasseur.

-   Sur la plage, baignent les eaux du lac Azur, dont l'autre rive donne accès à la grotte de l'Ours Brun.

-   La forêt de palmiers abrite une rivière, et se termine sur la façade ouest du volcan.

-   Par contre, la rivière ne prend pas sa source au sommet du volcan.

-   La cabane du pêcheur, qui se trouve sur la façade est du volcan, permet d'atteindre la grotte.

#### L'île des singes hurleurs 

-   Une légende ancestrale raconte, que quiconque oserait poser les pieds sur cette île pour la première fois ailleurs que sur la plage ou sur la crique, serait perdu pour toujours dans l'île.

-   Sur la plage, on trouve le delta de la rivière Papamouan.

-   De la plage, après avoir gravit pendant deux heures un chemin tortueux, la forêt de palmiers s'ouvre devant nous.

-   Au milieu de la crique, se dresse la cabane du chasseur.

-   Traverser la crique prend une demie-heure et à sa lisière se trouve une forêt de conifères.

-   Traverser la forêt de palmiers pour atteindre la cabane du pêcheur prend une heure.

-   À l'arrière de la cabane du pêcheur, un chemin plein de cendres permet de monter au sommet du volcan en 3h.

-   Descendre par la façade est du volcan prend également 3h et on arrive à la grotte.

#### Île des dauphins roses (version simple) 

-   Il y a deux façons de débarquer dans l'île: une crique et une plage.

-   De la crique un chemin étroit et sombre à une magnifique forêt de conifères.

-   Un sentier bien entretenu mène de la crique à la cabane du chasseur.

-   De la plage, un chemin scabreux monte vers la forêt de palmiers.

-   De la rivière, on peut atteindre la cabane du pêcheur.

-   Pour descendre à la grotte, il faut marcher sur la façade ouest du volcan.

-   En descendant la façade est du volcan, on arrive à la cabane du pêcheur.

-   Le pêcheur fait tous les matins une promenade jusqu'à la forêt de palmiers pour ceuillir des noix de coco.

#### Île des dauphins roses (version compliquée) 

-   Marcher sur cette île est très compliqué. Pour le faire, il faut disposer de souliers magiques que seuls les peuples indigènes vivant sur la plage et sur la crique savent fabriquer.

-   De la crique un chemin étroit et sombre mène en deux heures de marche à une magnifique forêt de conifères, alors qu'un sentier bien entretenu mène à la cabane du chasseur en une heure.

-   De la plage, un chemin scabreux monte vers la forêt de palmiers, il faut une bonne heure pour le trajet.

-   De la rivière, une heure de marche permet d'atteindre la cabane du pêcheur.

-   Pour descendre à la grotte, il faut marcher sur la façade ouest du volcan pendant deux heures.

-   En descendant la façade est du volcan pendant trois heures, on arrive à la cabane du pêcheur.

-   Le pêcheur fait tous les matins une promenade de deux heures jusqu'à la forêt de palmiers pour y cueillir des noix de coco.
`

function origin_temps() {
    // const exclude = []
    // const lieu_début = lieu(exclude, LIEUX_DEBUT)
    // const début_fin = (Math.random() > 0.5) ? [phrase(prop_fin(prop_début(lieu_début, prop(exclude))))] : [phrase(prop_début(lieu_début, prop(exclude))), phrase(prop_fin(prop()))]
    // const other = Array(3).fill(0).map((x, i) => phrase((i < 1) ? prop() : prop_invalide()))
    // const temps = phrase(prop_temps())
    // return {
    //     rédigé: début_fin.map(x => x.rédigé).join("\n") + "\n" + other.map(x => x.rédigé).join("\n") + "\n" + temps.rédigé,
    //     prédicat: (v, e) => début_fin.every(x => x.prédicat(v, e)) && other.every(x => x.prédicat(v, e)) && temps.prédicat(v, e),
    //     prédicatC: (c) => début_fin.every(x => x.prédicatC(c)) && other.every(x => x.prédicatC(c)) && temps.prédicatC(c),
    // }
    const exclude = []
    const other = Array(7).fill(0).map((x, i) => phrase(prop()))
    return {
        rédigé: other.map(x => x.rédigé).join("\n"),
        bloqué: other.reduce((acc, { bloqué }) => [...acc, ...bloqué], []),
        passant: other.reduce((acc, { passant }) => [...acc, ...passant], []),
        lieux: other.reduce((acc, { lieux }) => [...acc, ...lieux], []),
    }
}

/**
 * 
 * @param {string[]} exclude
 * @returns {{rédigé:string,lieux:string[],bloqué:Link[],passant:Link[]}}
 */
function prop(exclude = []) {
    const from = lieu(exclude), to = lieu(exclude)
    const rules = [
        () => {
            return {
                rédigé: `${from.direction} on peut aller directement ${à(to.decl)}`,
                lieux: [from.key,to.key],
                bloqué: [],
                passant: [{source:from.key,target:to.key}],
            }
        },
        () => {
            return {
                rédigé: `${from.direction} on peut descendre jusqu'${à(to.decl)}`,
                lieux: [from.key,to.key],
                bloqué: [],
                passant: [{source:from.key,target:to.key}],
            }
        },
        () => {
            return {
                rédigé: `${from.direction}, on peut atteindre directement ${to.decl}`,
                lieux: [from.key,to.key],
                bloqué: [],
                passant: [{source:from.key,target:to.key}],
            }
        },
        () => {
            return {
                rédigé: `la rivière débouche sur un lac`,
                lieux: ['riviere','lac'],
                bloqué: [],
                passant: [{source:'riviere',target:'lac'}],
            }
        },
        () => {
            return {
                rédigé: `la rivière permet d'aller jusqu'à la cabane du pêcheur`,
                lieux: ['riviere','cabane_peche'],
                bloqué: [],
                passant: [{source:'riviere',target:'cabane_peche'}],
            }
        },
        () => {
            return {
                rédigé: `${from.direction}, un chemin tortueux mène ${à(to.decl)}`,
                lieux: [from.key,to.key],
                bloqué: [],
                passant: [{source:from.key,target:to.key}],
            }
        },
        () => {
            return {
                rédigé: `en traversant la forêt de palmiers, on atteint la rive de la rivière`,
                lieux: ['palmier','riviere'],
                bloqué: [],
                passant: [{source:'palmier',target:'riviere'}],
            }
        },
        () => {
            const to2 = lieu(exclude)
            return {
                rédigé: `depuis ${from.decl}, on peut atteindre directement ${to.decl} ou ${to2.decl}`,
                lieux: [from.key,to.key,to2.key],
                bloqué: [],
                passant: [{source:from.key,target:to.key},{source:from.key,target:to2.key}],
            }
        },
        () => {
            return {
                rédigé: `en descendant par la façade Est du volcan on atteint la grotte`,
                lieux: ['volcan','grotte'],
                bloqué: [],
                passant: [{source:'volcan',target:'grotte'}],
            }
        },
        () => {
            return {
                rédigé: `la cabane du pêcheur se trouve sur la façade ouest du volcan`,
                lieux: ['cabane_peche','volcan'],
                bloqué: [],
                passant: [{source:'cabane_peche',target:'volcan'}],
            }
        },
        () => {
            return {
                rédigé: `${from.decl} mène ${à(to.decl)}`,
                lieux: [from.key,to.key],
                bloqué: [],
                passant: [{source:from.key,target:to.key}],
            }
        },
        () => {
            return {
                rédigé: `${from.direction}, un chemin fleuri mène directement ${à(to.decl)}`,
                lieux: [from.key,to.key],
                bloqué: [],
                passant: [{source:from.key,target:to.key}],
            }
        },
        () => {
            return {
                rédigé: `en traversant la forêt de palmiers on peut arriver directement au lac ou à la cabane du pêcheur`,
                lieux: ['palmier','lac','cabane_peche'],
                bloqué: [],
                passant: [{source:'palmier',target:'lac'},{source:'palmier',target:'cabane_peche'}],
            }
        },
        () => {
            return {
                rédigé: `le lac est au pied du volcan`,
                lieux: ['lac','volcan'],
                bloqué: [],
                passant: [{source:'volcan',target:'lac'}],
            }
        },
        () => {
            return {
                rédigé: `une grotte se cache sur la façade est du volcan`,
                lieux: ['grotte','volcan'],
                bloqué: [],
                passant: [{source:'volcan',target:'grotte'}],
            }
        },
        () => {
            return {
                rédigé: `la rivière prend sa source sur le volcan, et coule sur sa façade sud`,
                lieux: ['riviere','volcan'],
                bloqué: [],
                passant: [{source:'volcan',target:'riviere'}],
            }
        },
        () => {
            return {
                rédigé: `${from.direction}, un chemin très escarpé mène directment ${à(to.decl)}`,
                lieux: [from.key,to.key],
                bloqué: [],
                passant: [{source:from.key,target:to.key}],
            }
        },
        // () => {
        //     return {
        //         rédigé: `cette île a deux forêts: la forêt de palmiers, à côté de la plage, et la forêt de conifères, à côté de la crique`,
        //         lieux: [],
        //         bloqué: [],
        //         passant: [],
        //     }
        // },
        // TODO
        () => {
            return {
                rédigé: `au fond de la crique, se dissimule la cabane du chasseur`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `sur la plage, baignent les eaux du lac Azur, dont l'autre rive donne accès à la grotte de l'Ours Brun`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `la forêt de palmiers abrite une rivière, et se termine sur la façade ouest du volcan`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `par contre, la rivière ne prend pas sa source au sommet du volcan`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `la cabane du pêcheur, qui se trouve sur la façade est du volcan, permet d'atteindre la grotte`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `sur la plage, on trouve le delta de la rivière Papamouan`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `de la plage, après avoir gravit pendant deux heures un chemin tortueux, la forêt de palmiers s'ouvre devant nous`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `au milieu de la crique, se dresse la cabane du chasseur`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `traverser la crique prend une demie-heure et à sa lisière se trouve une forêt de conifères`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `traverser la forêt de palmiers pour atteindre la cabane du pêcheur prend une heure`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `à l'arrière de la cabane du pêcheur, un chemin plein de cendres permet de monter au sommet du volcan en 3h`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `descendre par la façade est du volcan prend également 3h et on arrive à la grotte`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `de la crique un chemin étroit et sombre à une magnifique forêt de conifères`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `un sentier bien entretenu mène de la crique à la cabane du chasseur`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `de la plage, un chemin scabreux monte vers la forêt de palmiers`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `de la rivière, on peut atteindre la cabane du pêcheur`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `pour descendre à la grotte, il faut marcher sur la façade ouest du volcan`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `en descendant la façade est du volcan, on arrive à la cabane du pêcheur`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `le pêcheur fait tous les matins une promenade jusqu'à la forêt de palmiers pour ceuillir des noix de coco`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `de la crique un chemin étroit et sombre mène en deux heures de marche à une magnifique forêt de conifères, alors qu'un sentier bien entretenu mène à la cabane du chasseur en une heure`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `de la plage, un chemin scabreux monte vers la forêt de palmiers, il faut une bonne heure pour le trajet`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `de la rivière, une heure de marche permet d'atteindre la cabane du pêcheur`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `pour descendre à la grotte, il faut marcher sur la façade ouest du volcan pendant deux heures`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `en descendant la façade est du volcan pendant trois heures, on arrive à la cabane du pêcheur`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `le pêcheur fait tous les matins une promenade de deux heures jusqu'à la forêt de palmiers pour y cueillir des noix de coco`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
    ]
    return choose_Rand(rules)()
}

// syntaxe
function phrase(s) {
    return { ...s, rédigé: s.rédigé.charAt(0).toUpperCase() + s.rédigé.slice(1) + "." }
}
function prop_début(début, s) {
    const rules = [
        //TODO
        () => {
            return {
                rédigé: `dans cette île, on ne peut débarquer que sur la plage`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `on peut arriver à l'île par la plage ou par la crique`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `le seul moyen d'arriver à l'île est de débarquer sur la plage`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `la plage et la crique offrent toutes deux de bons endroits pour débarquer sur l'île`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `une légende ancestrale raconte, que quiconque oserait poser les pieds sur cette île pour la première fois ailleurs que sur la plage ou sur la crique, serait perdu pour toujours dans l'île`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `il y a deux façons de débarquer dans l'île: une crique et une plage`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
        () => {
            return {
                rédigé: `marcher sur cette île est très compliqué. Pour le faire, il faut disposer de souliers magiques que seuls les peuples indigènes vivant sur la plage et sur la crique savent fabriquer`,
                lieux: [],
                bloqué: [],
                passant: [],
            }
        },
    ]
    return choose_Rand(rules)()
}
function prop_temps(exclude = []) {
    const rules = [
        () => {
            const start = lieu(exclude)
            const end = lieu(exclude)
            const h = heure()
            return {
                rédigé: `pour aller ${start.direction} jusqu'${à(end.decl)}, il m'a fallu ${h.rédigé} en passant par le chemin de plus court`,
                prédicat: (v, e) => dijkstra(v, e, start.key, end.key, x => x.time, (x, end) => x.coût === h.number && x.id === end) !== undefined,
                prédicatC: (c) => c.some(x => x === start.key) && c.some(x => x === end.key),
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

function prop_invalide() {
    const exclude = []
    const rules = [
        () => {
            const from = lieu(exclude), to = lieu(exclude)
            return {
                rédigé: `quand je passais par ${from.decl}, j'ai vu un chemin direct qui descendait jusqu'${à(to.decl)}${validité()}`,
                prédicat: (v, e) => e.find(({ source, target }) => (from === source && to === target) || (from === target && to === source)) === undefined,
                prédicatC: (c) => true && true,
            }
        },
        () => {
            const from = lieu(exclude), to = lieu(exclude)
            return {
                rédigé: `depuis ${from.position}, j'ai voulu aller directement ${to.position}${validité()}`,
                prédicat: (v, e) => e.find(({ source, target }) => (from === source && to === target) || (from === target && to === source)) === undefined,
                prédicatC: (c) => true && true,
            }
        },
        () => {
            const from = lieu(exclude), to = lieu(exclude)
            return {
                rédigé: `quand j'étais ${from.position}, j'aurais voulu aller directement ${to.position}${validité()}`,
                prédicat: (v, e) => e.find(({ source, target }) => (from === source && to === target) || (from === target && to === source)) === undefined,
                prédicatC: (c) => true && true,
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
        () => ({
            rédigé: `${s.rédigé.charAt(0).toUpperCase() + s.rédigé.slice(1)}, où j'ai caché mon trésor`,
            prédicat: (v, e) => true,
            prédicatC: (c) => true,
        })
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
/**
 * 
 * @param {[...string]} exclude 
 * @param {[...string]} include 
 */
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

const LIEUX_DEBUT = ["plage", "cabane_peche", "crique"]

function validité() {
    return choose_Rand(
        [", mais je ne pouvais pas passer", ", mais le chemin était trop étroit pour que je passe avec mon trésor. Je ne l'ai donc pas emprunté"]
    )
}
/**
 * @template T
 * @param {[...T]} l 
 */
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
    console.log(origin_temps());
}