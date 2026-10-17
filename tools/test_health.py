"""Smoke tests for MashLoop Ultra's liveness endpoints (stdlib unittest)."""
import unittest

from loopbox.server import app, health


class HealthRouteTests(unittest.TestCase):
    def test_routes_are_registered(self):
        paths = {getattr(route, "path", None) for route in app.routes}
        self.assertIn("/health", paths)
        self.assertIn("/api/health", paths)

    def test_liveness_payload_is_small_and_non_sensitive(self):
        payload = health()
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["service"], "mashloop-ultra")
        self.assertEqual(payload["version"], "0.1.0")
        self.assertIsInstance(payload["multiuser"], bool)
        self.assertNotIn("data_dir", payload)
        self.assertNotIn("secret", payload)


if __name__ == "__main__":
    unittest.main()
