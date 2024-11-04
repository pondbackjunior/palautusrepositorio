import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_finds_player(self):
        self.assertEqual(self.stats.search("Semenko").name, "Semenko")

    def test_does_not_find_player(self):
        self.assertEqual(self.stats.search("asdfg"), None)

    def test_finds_team(self):
        self.stats.team("EDM")
    
    def test_finds_top_default(self):
        self.stats.top(3)

    def test_finds_top_points(self):
        self.stats.top(3, SortBy.POINTS)

    def test_finds_top_goals(self):
        self.stats.top(3, SortBy.GOALS)

    def test_finds_top_assists(self):
        self.stats.top(3, SortBy.ASSISTS)
    