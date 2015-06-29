from django.test import TestCase

from .models import TestResource


class NestedFieldsTest(TestCase):
    def setUp(self):
        self.test_resource = TestResource.objects.create(name="Test-Resource", type=TestResource.Type.DEFAULT)

    def testGetResourceWithEnumField(self):
        resp = self.client.get("/test-resources/")
        self.assertEqual(200, resp.status_code, resp.content)
        self.assertEqual(1, len(resp.data))
        self.assertEqual(self.test_resource.name, resp.data[0]["name"])
        self.assertEqual(self.test_resource.type.value, resp.data[0]["type"])

