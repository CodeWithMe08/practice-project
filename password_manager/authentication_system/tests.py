import pytest
from .models import MyUsers

@pytest.mark.django_db
def test_show_record(request):
    data = MyUsers.objects.all()
    for d in data:
        assert d.first_nmae == "raunak"

@pytest.mark.django_db
def test_show_records(request):
    data = MyUsers.objects.all()
    for d in data:
        assert d.last_name == "varma"

def test_home(request):
    name = "raunak varma"
    assert name == "raunak varma"

def test_new(request):
    place = "nagpur"
    assert place == "nagpur"