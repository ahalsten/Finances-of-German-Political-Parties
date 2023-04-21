Data Structure of Sponsorships Graph

MultiDiGraph with the two parties as nodes that have only precedessors,
and sponsors as nodes that have only successors. 

Edges can be parallel if a sponsor gave money to the same party in multiple years. 

The year of the sponsorship is the key of the edge.

The amount of the sponsorship is the weight of the edge as an attribute.

If a firm sponsored multiple events in one year, the amounts were summed so only one
observation per sponsor and year remains.