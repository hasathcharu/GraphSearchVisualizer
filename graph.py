import networkx as nx

G = nx.Graph()
G.add_edges_from(
    [
        ("Haritha", "Manupa", {"weight": 3}),
        ("Haritha", "Ransilu", {"weight": 1}),
        ("Haritha", "Waruni", {"weight": 5}),
        (
            "Haritha",
            "Menura",
            {
                "weight": 4,
            },
        ),
        (
            "Manupa",
            "Isuri",
            {
                "weight": 1,
            },
        ),
        (
            "Ransilu",
            "Thathsarani",
            {
                "weight": 2,
            },
        ),
        (
            "Ransilu",
            "Kithmi",
            {
                "weight": 4,
            },
        ),
        (
            "Ransilu",
            "Ranul",
            {
                "weight": 5,
            },
        ),
        (
            "Waruni",
            "Menura",
            {
                "weight": 1,
            },
        ),
        (
            "Menura",
            "Ranul",
            {
                "weight": 3,
            },
        ),
        ("Menura", "Nethmini", {"weight": 2}),
        (
            "Isuri",
            "Rashmi",
            {
                "weight": 1,
            },
        ),
        (
            "Isuri",
            "Kithmi",
            {
                "weight": 3,
            },
        ),
        (
            "Isuri",
            "Thathsarani",
            {
                "weight": 5,
            },
        ),
        (
            "Kithmi",
            "Rashmi",
            {
                "weight": 5,
            },
        ),
        (
            "Ranul",
            "Taneesha",
            {
                "weight": 1,
            },
        ),
        (
            "Rashmi",
            "Taneesha",
            {
                "weight": 2,
            },
        ),
    ]
)
G.nodes["Haritha"]["pos"] = (3.5, 2)
G.nodes["Manupa"]["pos"] = (2.5, 1)
G.nodes["Ransilu"]["pos"] = (3.3, 0.5)
G.nodes["Waruni"]["pos"] = (4, 1)
G.nodes["Menura"]["pos"] = (4.5, 2)
G.nodes["Nethmini"]["pos"] = (5, 1)
G.nodes["Isuri"]["pos"] = (2.6, -1.6)
G.nodes["Kithmi"]["pos"] = (3.5, -1)
G.nodes["Ranul"]["pos"] = (4.5, -0.2)
G.nodes["Taneesha"]["pos"] = (4, -1.5)
G.nodes["Rashmi"]["pos"] = (3.5, -3)
G.nodes["Thathsarani"]["pos"] = (2.9, -0.3)

G.nodes["Haritha"]["h"] = 10
G.nodes["Manupa"]["h"] = 6
G.nodes["Ransilu"]["h"] = 5
G.nodes["Waruni"]["h"] = 7
G.nodes["Menura"]["h"] = 9
G.nodes["Isuri"]["h"] = 1
G.nodes["Kithmi"]["h"] = 2
G.nodes["Ranul"]["h"] = 4
G.nodes["Nethmini"]["h"] = 8
# G.nodes['Taneesha']['h'] = 1
G.nodes["Taneesha"]["h"] = 3
G.nodes["Rashmi"]["h"] = 0
G.nodes["Thathsarani"]["h"] = 8
