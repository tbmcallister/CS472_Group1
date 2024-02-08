"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""
from unittest import TestCase
# we need to import the unit under test - counter
from src.counter import app
# we need to import the file that contains the status codes
from src import status


class CounterTest(TestCase):
    """Counter tests"""
    def setUp(self):
        self.client = app.test_client()

    def test_duplicate_a_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

    def test_create_a_counter(self):
        """It should create a counter"""
        result = self.client.post('/counters/foo')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    def test_update_a_counter(self):
        counterName = "foo1"
        # make a call to create a counter
        result = self.client.post(f'/counters/{counterName}')

        # ensure that it returned a successful return code
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        # check the counter value as a baseline
        baselineResponse = self.client.get(f'/counters/{counterName}')
        baselineVal = baselineResponse.json[counterName]
        app.logger.info(f"Counter {counterName} has a value of {baselineVal} before updating")

        # make a call to update the counter that you just created
        result = self.client.put(f'/counters/{counterName}')

        # ensure that it returned a successful return code
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        # check that the counter value is one more than the baseline
        updatedResponse = self.client.get(f'/counters/{counterName}')
        updatedVal = updatedResponse.json[counterName]
        app.logger.info(f"Counter {counterName} has a value of {updatedVal} after updating")

        self.assertEqual(updatedVal, baselineVal+1)

    def test_read_a_counter(self):
        counterName = "foo2"
        # make a call to create a counter
        result = self.client.post(f'/counters/{counterName}')

        # make sure the counter was correctly created
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        # read the value of the counter, which should be 0
        result = self.client.get(f'/counters/{counterName}')

        # ensure that it returned a successful return code
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        # check to see if the value of the counter is 0
        app.logger.info(f"Counter {counterName} has a value of {result}")

    def test_update_a_bad_counter(self):
        # this will test a counter that doesn't exist
        result = self.client.put('/counters/badcounter')

        # check that it is correctly failing
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)

    def test_read_a_bad_counter(self):
        # this will test a counter that doesn't exist
        result = self.client.get('/counters/badcounter')

        # check that it is correctly failing
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_a_counter(self):
        # this will create and delete a counter
        counterName = "foo2"
        # make a call to create a counter
        result = self.client.post(f'/counters/{counterName}')

        # make sure the counter was correctly created
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        result = self.client.delete(f'/counters/{counterName}')

        # make sure the counter was correctly created
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)
