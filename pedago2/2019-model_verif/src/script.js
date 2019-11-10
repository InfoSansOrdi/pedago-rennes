const DIR = '../images/';


let width = 800;
let height = 600;
let color = d3.scaleOrdinal(d3.schemeCategory10);

const _graph = data

document.getElementById('data').addEventListener("input",
    function () {
        try {
            run(JSON.parse(this.value))
        } catch (error) {
            console.error(error)
        }
    })


// let label = {
//     'nodes': [],
//     'links': []
// };

// graph.nodes.forEach(function(d, i) {
//     label.nodes.push({node: d});
//     label.nodes.push({node: d});
//     label.links.push({
//         source: i * 2,
//         target: i * 2 + 1
//     });
// });

// let labelLayout = d3.forceSimulation(label.nodes)
//     .force("charge", d3.forceManyBody().strength(-50))
//     .force("link", d3.forceLink(label.links).distance(0).strength(2));
function run(graph = _graph) {
    document.getElementById('viz').innerHTML = '';
    const graphLayout = d3.forceSimulation(graph.nodes)
        .force("charge", d3.forceManyBody().strength(-3000))
        .force("center", d3.forceCenter(width / 2, height / 2))
        .force("x", d3.forceX(width / 2).strength(1))
        .force("y", d3.forceY(height / 2).strength(1))
        .force("link", d3.forceLink(graph.links).id(function (d) { return d.id; }).distance(50).strength(1))
        .on("tick", ticked);

    const adjlist = [];

    graph.links.forEach(function (d) {
        adjlist[d.source.index + "-" + d.target.index] = true;
        adjlist[d.target.index + "-" + d.source.index] = true;
    });

    function neigh(a, b) {
        return a == b || adjlist[a + "-" + b];
    }

    const svg = d3.select("#viz").attr("width", width).attr("height", height);
    const container = svg.append("g");

    svg.call(
        d3.zoom()
            .scaleExtent([.1, 4])
            .on("zoom", function () { container.attr("transform", d3.event.transform); })
    );

    const links = container.append("g").attr("class", "links")
        .selectAll("line")
        .data(graph.links)
        .enter()
        .append("line")
        .attr("stroke", "hsl(25, 25%, 44%)")
        .attr("stroke-width", "15px");

    const NODE_SIZE = 80
    const nodes = container.append("g").attr("class", "nodes")
        .selectAll("g")
        .data(graph.nodes)
        .enter()
        .append("g")
        .style("transform-origin", "center");
    nodes.call(addImg);
    function addImg(node) {
        node
            .append("svg:image")
            .attr("xlink:href", function (d) { return DIR + d.img; })
            .attr("x", function (d) { return -NODE_SIZE * (d.scale || 1) / 2; })
            .attr("y", function (d) { return -NODE_SIZE * (d.scale || 1) / 2; })
            .attr("height", function (d) { return NODE_SIZE * (d.scale || 1); })
            .attr("width", function (d) { return NODE_SIZE * (d.scale || 1); })
            .attr("transform", function (d) {
                return `scale(${Math.random() > 0.5 ? -1 : 1},1)`;
            });
    }
    // .append("circle")
    // .attr("r", 5)
    // .attr("fill", function(d) { return color(d.group); })

    // node.on("mouseover", focus).on("mouseout", unfocus);

    nodes.call(
        d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended)
    );

    // let labelNode = container.append("g").attr("class", "labelNodes")
    //     .selectAll("text")
    //     .data(label.nodes)
    //     .enter()
    //     .append("text")
    //     .text(function(d, i) { return i % 2 == 0 ? "" : d.node.id; })
    //     .style("fill", "#555")
    //     .style("font-family", "Arial")
    //     .style("font-size", 12)
    //     .style("pointer-events", "none"); // to prevent mouseover/drag capture

    // node.on("mouseover", focus).on("mouseout", unfocus);

    function ticked() {
        nodes && nodes.call(updateNode);
        links && links.call(updateLink);
        if (!nodes && !links) {
            graphLayout.stop()
        }
        // labelLayout.alphaTarget(0.3).restart();
        // labelNode.each(function(d, i) {
        //     if(i % 2 == 0) {
        //         d.x = d.node.x;
        //         d.y = d.node.y;
        //     } else {
        //         let b = this.getBBox();

        //         let diffX = d.x - d.node.x;
        //         let diffY = d.y - d.node.y;

        //         let dist = Math.sqrt(diffX * diffX + diffY * diffY);

        //         let shiftX = b.width * (diffX - dist) / (dist * 2);
        //         shiftX = Math.max(-b.width, Math.min(0, shiftX));
        //         let shiftY = 16;
        //         this.setAttribute("transform", "translate(" + shiftX + "," + shiftY + ")");
        //     }
        // });
        // labelNode.call(updateNode);

    }

    function fixna(x) {
        if (isFinite(x)) return x;
        return 0;
    }

    function focus(d) {
        const index = d3.select(d3.event.target).datum().index;
        nodes.style("opacity", function (o) {
            return neigh(index, o.index) ? 1 : 0.1;
        });
        // labelNode.attr("display", function(o) {
        //   return neigh(index, o.node.index) ? "block": "none";
        // });
        links.style("opacity", function (o) {
            return o.source.index == index || o.target.index == index ? 1 : 0.1;
        });
    }

    function unfocus() {
        //    labelNode.attr("display", "block");
        nodes.style("opacity", 1);
        links.style("opacity", 1);
    }

    function updateLink(link) {
        link.attr("x1", function (d) { return fixna(d.source.x); })
            .attr("y1", function (d) { return fixna(d.source.y); })
            .attr("x2", function (d) { return fixna(d.target.x); })
            .attr("y2", function (d) { return fixna(d.target.y); });
    }

    function updateNode(node) {
        node.attr("transform", function (d) {
            return "translate(" + fixna(d.x) + "," + fixna(d.y) + ")";
        });
    }

    function dragstarted(d) {
        d3.event.sourceEvent.stopPropagation();
        if (!d3.event.active) graphLayout.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged(d) {
        d.fx = d3.event.x;
        d.fy = d3.event.y;
    }

    function dragended(d) {
        if (!d3.event.active) graphLayout.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }
    document.getElementById("load").addEventListener('change', function () {
        var reader = new FileReader();
        reader.addEventListener("loadend", function () {
            // reader.result contains the contents of blob as a typed array
            console.log(reader.result)
            document.getElementById('data').innerHTML = reader.result;
            document.getElementById('data').dispatchEvent(new Event("input"));
        });
        reader.readAsText(this.files[0]);
    });
    document.getElementById("export").addEventListener('click',
        function () {
            var svg_data = document.getElementById("viz").innerHTML //put id of your svg element here

            var head = '<svg title="graph" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">'

            //if you have some additional styling like graph edges put them inside <style> tag

            var style = '<style>circle {cursor: pointer;stroke-width: 1.5px;}text {font: 10px arial;}path {stroke: DimGrey;stroke-width: 1.5px;}</style>'

            var full_svg = head + style + svg_data + "</svg>"

            var blob = new Blob([full_svg], { type: "image/svg+xml" });
            saveAs(blob, "ile.svg");
        })
}
run()