from django.test import TestCase
from django.test import Client
from django.urls import reverse

c = Client()


# Create your tests here.
class CompanyTest(TestCase):
    fixtures = ['db.json']

    def test_company_creation(self):
        response = c.post(reverse('company'), {'name': 'amazon'})
        self.assertEqual(response.status_code, 200)

    def test_company_creation_with_missing_name(self):
        response = c.post(reverse('company'), {})
        self.assertEqual(response.status_code, 400)

    def test_company_read(self):
        response = c.get(reverse('company') + '/1')
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response['name'], 'google')

    def test_company_read_with_missing_id(self):
        response = c.get(reverse('company') + '/8')
        self.assertEqual(response.status_code, 404)

    def test_company_update(self):
        response = c.put(reverse('company'), {'id': 1, 'name': 'airbnb'}, content_type='application/json')
        json_response = response.json()
        self.assertEqual(json_response['name'], 'airbnb')
        self.assertEqual(response.status_code, 200)

    def test_company_update_with_missing_id(self):
        response = c.put(reverse('company'), {'name': 'google'}, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_company_delete(self):
        response = c.delete(reverse('company') + '/1')
        self.assertEqual(response.status_code, 204)

    def test_company_delete_absent(self):
        response = c.delete(reverse('company') + '/8')
        self.assertEqual(response.status_code, 404)

    def test_company_list(self):
        response = c.get(reverse('company'))
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(len(json_response), 4)


class EmployeeTest(TestCase):
    fixtures = ['db.json']

    def test_employee_creation(self):
        response = c.post('/employee', {'name': 'john', 'company': 1}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_employee_creation_with_absent_company(self):
        response = c.post('/employee', {'name': 'john', 'company': 8}, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_employee_creation_with_missing_name(self):
        response = c.post('/employee', {'company': 1})
        self.assertEqual(response.status_code, 400)

    def test_employee_read(self):
        response = c.get('/employee/1')
        self.assertEqual(response.status_code, 200)

    def test_employee_read_with_missing_id(self):
        response = c.get('/employee/8')
        self.assertEqual(response.status_code, 400)

    def test_employee_update(self):
        response = c.put('/employee', {'id': 1, 'name': 'john', 'company': 1}, content_type='application/json')
        json_response = response.json()
        self.assertEqual(json_response['name'], 'john')
        self.assertEqual(response.status_code, 200)

    def test_employee_update_with_missing_id(self):
        response = c.put('/employee', {'name': 'john', 'company': 1}, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_employee_delete(self):
        response = c.delete('/employee/1')
        self.assertEqual(response.status_code, 204)

    def test_employee_delete_absent(self):
        response = c.delete('/employee/8')
        self.assertEqual(response.status_code, 400)

    def test_employee_list(self):
        response = c.get('/employee')
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(len(json_response), 2)


class EntryTest(TestCase):
    def test_entry_creation(self):
        response = c.post('/entry', {'employee': 1, 'title': 'New Title', 'content': 'New Content'},
                          content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_entry_creation_with_missing_employee(self):
        response = c.post('/entry', {'employee': 20, 'title': 'New Title', 'content': 'New Content'},
                          content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_entry_read(self):
        response = c.get('/entry/1')
        self.assertEqual(response.status_code, 200)

    def test_entry_read_with_missing_id(self):
        response = c.get('/entry/8')
        self.assertEqual(response.status_code, 400)

    def test_entry_update(self):
        response = c.put('/entry', {'id': 1, 'title': 'Updated Title', 'content': 'Updated Content'},
                         content_type='application/json')
        json_response = response.json()
        self.assertEqual(json_response['hours'], 8)
        self.assertEqual(response.status_code, 200)

    def test_entry_update_with_missing_id(self):
        response = c.put('/entry', {'employee': 1, 'title': 'Updated Title', 'content': 'Updated Content'},
                         content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_entry_delete(self):
        response = c.delete('/entry/1')
        self.assertEqual(response.status_code, 204)

    def test_entry_delete_absent(self):
        response = c.delete('/entry/8')
        self.assertEqual(response.status_code, 400)

    def test_entry_list(self):
        response = c.get('/entry')
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(len(json_response), 2)


class GetFeedTest(TestCase):
    fixtures = ['db.json']

    def test_get_feed(self):
        response = c.get('/feed/1')
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(len(json_response), 2)

    def test_get_feed_with_missing_company_id(self):
        response = c.get('/feed/8')
        self.assertEqual(response.status_code, 400)


class GetTimelineTest(TestCase):
    fixtures = ['db.json']

    def test_get_timeline(self):
        response = c.get('/timeline/1')
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(len(json_response), 2)

    def test_get_timeline_with_missing_company_id(self):
        response = c.get('/timeline/8')
        self.assertEqual(response.status_code, 400)
