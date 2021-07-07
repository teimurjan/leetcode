from typing import List
import unittest


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.flights = {}

        if len(tickets) == 1:
            return tickets[0]

        for ticket in tickets:
            if ticket[0] in self.flights:
                self.flights[ticket[0]].append(ticket[1])
            else:
                self.flights[ticket[0]] = [ticket[1]]

        for _, itinerary in self.flights.items():
            itinerary.sort(reverse=True)

        self.result = []
        self.visit("JFK")

        return self.result[::-1]

    def visit(self, origin):
        destinations = self.flights.get(origin)

        while destinations:
            next_destination = destinations.pop()
            self.visit(next_destination)

        self.result.append(origin)


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(
            s.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]),
            ["JFK", "NRT", "JFK", "KUL"],
        )
        self.assertEqual(
            s.findItinerary(
                [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
            ),
            ["JFK", "MUC", "LHR", "SFO", "SJC"],
        )
        self.assertEqual(
            s.findItinerary(
                [
                    ["JFK", "SFO"],
                    ["JFK", "ATL"],
                    ["SFO", "ATL"],
                    ["ATL", "JFK"],
                    ["ATL", "SFO"],
                ]
            ),
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
        )


if __name__ == "__main__":
    unittest.main()
