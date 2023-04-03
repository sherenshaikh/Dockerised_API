import pytest
from fastapi.testclient import TestClient
from app import app

class TestClass:
    client = TestClient(app)

    # Test scenario 1 :test for employee at high risk
    def test1(self):
        response = self.client.get("/employee_risk?YearsAtCompany=1&EmployeeSatisfaction=0.1&Position=Non-Manager&Salary=4")
        expected_response = {
            'YearsAtCompany': 1.0,
            'EmployeeSatisfaction': 0.1,
            'Position': 'Non-Manager',
            'Salary': 4,
            'EducationLevel': 'None',
            'riskLevel': 'High',
            'warning': 'The employee is at high risk of leaving company. Please take preventative measures'
        }

        assert response.status_code == 200
        assert response.json() == expected_response

    # Test scenario 2 :test for employee at no risk
    def test2(self):
        response = self.client.get("/employee_risk?YearsAtCompany=10&EmployeeSatisfaction=10.5&Position=Manager&Salary=5")
        expected_response = {
            'YearsAtCompany': 10,
            'EmployeeSatisfaction': 10.5,
            'Position': 'Manager',
            'Salary': 5,
            'EducationLevel': 'None',
            'riskLevel': 'None',
            'warning': 'The employee is at no risk of leaving the company'
        }

        assert response.status_code == 200
        assert response.json() == expected_response

    # Test scenario 3 : test for employee at high risk with new field EducationLevel
    def test3(self):
        response = self.client.get("/employee_risk?YearsAtCompany=1&EmployeeSatisfaction=0.1&Position=Non-Manager&Salary=4&EducationLevel=Graduate")
        expected_response = {
            'YearsAtCompany': 1.0,
            'EmployeeSatisfaction': 0.1,
            'Position': 'Non-Manager',
            'Salary': 4,
            'EducationLevel': 'Graduate',
            'riskLevel': 'High',
            'warning': 'The employee is at high risk of leaving company. Please take preventative measures'
        }

        assert response.status_code == 200
        assert response.json() == expected_response

    # Test scenario 4 : test for employee at no risk with new field EducationLevel
    def test4(self):
        response = self.client.get("/employee_risk?YearsAtCompany=10&EmployeeSatisfaction=10.5&Position=Manager&Salary=5&EducationLevel=Graduate")
        expected_response = {
            'YearsAtCompany': 10,
            'EmployeeSatisfaction': 10.5,
            'Position': 'Manager',
            'Salary': 5,
            'EducationLevel': 'Graduate',
            'riskLevel': 'None',
            'warning': 'The employee is at no risk of leaving the company'
        }

        assert response.status_code == 200
        assert response.json() == expected_response
