graph = {"start": {"a": 5, "b": 2},
         "a": {"c": 4, "d": 2},
         "b": {"a": 8, "d": 7},
         "c": {"d": 6, "fin": 3},
         "d": {"fin": 1},
         "fin": {}}

infinity = float("inf")

costs = {"a": 5,
         "b": 2,
         "c": infinity,
         "d": infinity,
         "fin": infinity}

parents = {"a": "start",
           "b": "start",
           "c": "a",
           "d": None,
           "fin": None}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs.keys():
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbores = graph[node]
    for neighbore in neighbores.keys():
        new_cost = cost + neighbores[neighbore]
        if new_cost < costs[neighbore]:
            costs[neighbore] = new_cost
            parents[neighbore] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print("The shortest way equals:", costs["fin"])
