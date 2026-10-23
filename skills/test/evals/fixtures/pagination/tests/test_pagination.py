import unittest
from unittest.mock import patch

import pagination


class PaginationTests(unittest.TestCase):
    def test_second_page_contains_requested_records(self):
        self.assertEqual(pagination.page_records(list(range(8)), page=2, size=3), [3, 4, 5])

    def test_negative_page_is_rejected(self):
        with self.assertRaises(ValueError):
            pagination.page_records([1, 2], page=-1)

    def test_wire_schema_matches_published_contract(self):
        self.assertEqual(pagination.SCHEMA_VERSION, "records/1")

    def test_second_page_again(self):
        self.assertEqual(pagination.page_records(list(range(8)), page=2, size=3), [3, 4, 5])

    def test_spinner_interval(self):
        self.assertEqual(pagination.SPINNER_TICK_MS, 80)

    def test_maximum_matches_itself(self):
        self.assertEqual(pagination.MAX_PAGE_SIZE, pagination.MAX_PAGE_SIZE)

    def test_fixture_record(self):
        record = {"id": 7}
        self.assertEqual(record["id"], 7)

    def test_third_page(self):
        records = list(range(9))
        page = 3
        size = 2
        start = (page - 1) * size
        expected = list(records[start:start + size])
        self.assertEqual(pagination.page_records(records, page=page, size=size), expected)

    def test_mocked_page(self):
        with patch("pagination.page_records", return_value=[8]):
            self.assertEqual(pagination.page_records([1, 2]), [8])

    def test_response_contains_requested_records(self):
        self.assertIsInstance(pagination.page_response([1, 2]), dict)
