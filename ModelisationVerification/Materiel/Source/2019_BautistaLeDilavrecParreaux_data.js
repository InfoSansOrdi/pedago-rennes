const data = {
  "nodes": [
      {
          "id": "plage",
          "img": "plage.svg"
      },
      {
          "id": "palmier",
          "img": "palmier.svg"
      },
      {
          "id": "riviere",
          "img": "riviere.svg"
      },
      {
          "id": "volcan",
          "img": "volcan.svg"
      },
      {
          "id": "grotte",
          "img": "grotte.svg"
      },
      {
          "id": "crique",
          "img": "crique.svg"
      },
      {
          "id": "cabane_peche",
          "img": "cabane_peche.svg"
      },
      {
          "id": "sapin",
          "img": "sapin.svg"
      }
  ],
  "links": [
      {
          "source": "plage",
          "target": "palmier"
      },
      {
          "source": "palmier",
          "target": "riviere"
      },
      {
          "source": "riviere",
          "target": "volcan"
      },
      {
          "source": "volcan",
          "target": "grotte"
      },
      {
          "source": "volcan",
          "target": "riviere"
      },
      {
          "source": "palmier",
          "target": "cabane_peche"
      },
      {
          "source": "cabane_peche",
          "target": "sapin"
      }
  ]
}

const data2 = {
  "nodes": [
    {
      "id": "plage",
      "group": 1,
      "img": "plage.svg"
    },
    {
      "id": "palmier",
      "group": 1,
      "img": "palmier.svg"
    },
    {
      "id": "cabane_peche",
      "group": 1,
      "img": "cabane_peche.svg",
      "scale": 1.3
    },
    {
      "id": "volcan",
      "group": 1,
      "img": "volcan.svg"
    },
    {
      "id": "riviere",
      "group": 1,
      "img": "riviere.svg"
    },
    {
      "id": "grotte",
      "group": 1,
      "img": "grotte.svg",
      "scale": 0.8
    },
    {
      "id": "crique",
      "group": 1,
      "img": "grotte.svg",
      "scale": 0.8
    },
    {
      "id": "sapin",
      "group": 1,
      "img": "sapin.svg"
    },
    {
      "id": "cabane_chasse",
      "group": 1,
      "img": "cabane_peche.svg",
      "scale": 1.3
    }],
  "links": [
    {
      "source": "plage",
      "target": "palmier",
      "value": 3
    },
    {
      "source": "palmier",
      "target": "cabane_peche",
      "value": 3
    },
    {
      "source": "cabane_peche",
      "target": "riviere",
      "value": 3
    },
    {
      "source": "cabane_peche",
      "target": "volcan",
      "value": 3
    },
    {
      "source": "riviere",
      "target": "volcan",
      "value": 3
    },
    {
      "source": "volcan",
      "target": "grotte",
      "value": 3
    },
    {
      "source": "crique",
      "target": "sapin",
      "value": 3
    },
    {
      "source": "crique",
      "target": "cabane_chasse",
      "value": 3
    }]
}